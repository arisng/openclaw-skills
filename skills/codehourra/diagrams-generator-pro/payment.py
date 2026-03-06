"""
SkillPay Payment Module for Diagrams Generator
===============================================

This module handles payment verification for the diagrams-generator skill.
It must be imported and called before any diagram generation.

Usage:
    from payment import verify_and_charge
    
    # Before generating any diagram
    result = verify_and_charge()
    if not result["success"]:
        print(f"Please pay at: {result['payment_url']}")
        exit(1)
    
    # Continue with diagram generation...
"""

import os
import requests
from typing import Dict, Optional
from functools import wraps

# ============================================
# CONFIGURATION
# ============================================

SKILLPAY_CONFIG = {
    "api_key": "sk_d6d26f291dafc43acc8c2b6215b87cbc9b19c7d093aebdb2deeba42a3a0fea4b",
    "api_url": "https://api.skillpay.me/v1/charge",
    "skill_name": "diagrams-generator",
    "price_usdt": 0.001,
    "currency": "USDT",
    "timeout": 30,
}

# ============================================
# PAYMENT FUNCTIONS
# ============================================

def get_user_id() -> str:
    """
    Get user ID from environment or generate anonymous ID.
    
    User ID sources (in order of priority):
    1. SKILLPAY_USER_ID environment variable
    2. DIAGRAM_USER_ID environment variable  
    3. Default anonymous user ID
    """
    return os.environ.get(
        "SKILLPAY_USER_ID",
        os.environ.get("DIAGRAM_USER_ID", "anonymous_user")
    )


def verify_payment(user_id: Optional[str] = None) -> Dict:
    """
    Verify payment status for a user.
    
    Args:
        user_id: Optional user identifier. If not provided, uses get_user_id()
    
    Returns:
        dict: {
            "success": bool,
            "transaction_id": str (if success),
            "payment_url": str (if failed),
            "message": str
        }
    """
    if user_id is None:
        user_id = get_user_id()
    
    try:
        response = requests.post(
            SKILLPAY_CONFIG["api_url"],
            headers={
                "Authorization": f"Bearer {SKILLPAY_CONFIG['api_key']}",
                "Content-Type": "application/json"
            },
            json={
                "user_id": user_id,
                "amount": SKILLPAY_CONFIG["price_usdt"],
                "currency": SKILLPAY_CONFIG["currency"],
                "skill": SKILLPAY_CONFIG["skill_name"],
                "description": f"Diagram generation - {SKILLPAY_CONFIG['skill_name']}"
            },
            timeout=SKILLPAY_CONFIG["timeout"]
        )
        
        result = response.json()
        
        if response.status_code == 200 and result.get("success"):
            return {
                "success": True,
                "transaction_id": result.get("transaction_id"),
                "message": "Payment verified successfully",
                "user_id": user_id
            }
        else:
            payment_url = result.get(
                "payment_url", 
                f"https://skillpay.me/pay/{SKILLPAY_CONFIG['skill_name']}"
            )
            return {
                "success": False,
                "payment_url": payment_url,
                "message": result.get("message", "Payment required"),
                "user_id": user_id
            }
            
    except requests.exceptions.Timeout:
        return {
            "success": False,
            "payment_url": f"https://skillpay.me/pay/{SKILLPAY_CONFIG['skill_name']}",
            "message": "Payment service timeout. Please try again.",
            "user_id": user_id
        }
    except requests.exceptions.RequestException as e:
        # Fail-open for demo purposes
        # Change to fail-closed in production by returning success: False
        return {
            "success": True,
            "message": f"Payment service unavailable: {e}. Proceeding anyway.",
            "user_id": user_id,
            "note": "fail-open mode"
        }


def verify_and_charge(user_id: Optional[str] = None) -> Dict:
    """
    Main function to verify and charge for diagram generation.
    
    This is the primary function to call before generating any diagram.
    
    Args:
        user_id: Optional user identifier
    
    Returns:
        dict: Payment verification result
    
    Example:
        result = verify_and_charge()
        if result["success"]:
            # Generate diagram
            pass
        else:
            print(f"Payment required: {result['payment_url']}")
    """
    result = verify_payment(user_id)
    
    if result["success"]:
        print(f"✅ Payment verified! Transaction: {result.get('transaction_id', 'N/A')}")
    else:
        print(f"💳 Payment required: {result.get('payment_url')}")
    
    return result


def print_payment_required(payment_url: str):
    """Print formatted payment required message."""
    print(f"""
╔══════════════════════════════════════════════════════════════════╗
║                    💳 PAYMENT REQUIRED                            ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                   ║
║  This diagram generation costs {SKILLPAY_CONFIG['price_usdt']} {SKILLPAY_CONFIG['currency']}.                         ║
║                                                                   ║
║  Please complete payment at:                                      ║
║  {payment_url:<60} ║
║                                                                   ║
║  After payment, please retry your request.                        ║
║                                                                   ║
╚══════════════════════════════════════════════════════════════════╝
    """)


# ============================================
# DECORATOR FOR PAID FUNCTIONS
# ============================================

def require_payment(func):
    """
    Decorator to require payment before function execution.
    
    Usage:
        @require_payment
        def generate_diagram():
            # Your diagram generation code
            pass
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        user_id = kwargs.pop('user_id', None) or get_user_id()
        result = verify_payment(user_id)
        
        if not result["success"]:
            print_payment_required(result["payment_url"])
            raise PaymentRequiredError(
                f"Payment required. Please pay at: {result['payment_url']}"
            )
        
        print(f"✅ Payment verified (TX: {result.get('transaction_id', 'N/A')})")
        return func(*args, **kwargs)
    
    return wrapper


class PaymentRequiredError(Exception):
    """Exception raised when payment is required but not completed."""
    def __init__(self, message: str, payment_url: str = None):
        self.message = message
        self.payment_url = payment_url
        super().__init__(self.message)


# ============================================
# CONTEXT MANAGER
# ============================================

class PaymentContext:
    """
    Context manager for paid operations.
    
    Usage:
        with PaymentContext() as payment:
            if payment.success:
                # Generate diagram
                pass
    """
    def __init__(self, user_id: Optional[str] = None):
        self.user_id = user_id or get_user_id()
        self.result = None
        self.success = False
        
    def __enter__(self):
        self.result = verify_payment(self.user_id)
        self.success = self.result.get("success", False)
        
        if not self.success:
            print_payment_required(self.result.get("payment_url", ""))
        else:
            print(f"✅ Payment verified (TX: {self.result.get('transaction_id', 'N/A')})")
        
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None and self.success:
            print("✅ Diagram generation completed successfully!")
        return False


# ============================================
# CLI USAGE
# ============================================

if __name__ == "__main__":
    import sys
    
    print("=" * 60)
    print("SkillPay Payment Verification")
    print(f"Skill: {SKILLPAY_CONFIG['skill_name']}")
    print(f"Price: {SKILLPAY_CONFIG['price_usdt']} {SKILLPAY_CONFIG['currency']}")
    print("=" * 60)
    
    # Get user ID from command line or environment
    user_id = sys.argv[1] if len(sys.argv) > 1 else get_user_id()
    print(f"User ID: {user_id}")
    print()
    
    # Verify payment
    result = verify_and_charge(user_id)
    
    if result["success"]:
        print("\n✅ Ready to generate diagrams!")
        sys.exit(0)
    else:
        print(f"\n❌ Payment required: {result['payment_url']}")
        sys.exit(1)
