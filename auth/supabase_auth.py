from supabase import create_client
from core.config import SUPABASE_KEY, SUPABASE_URL

supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)

def sign_in(email, password):
    return supabase.auth.sign_in_with_password({
        "email": email,
        "password": password
    })

def sign_up(email, password):
    return supabase.auth.sign_up({
        "email": email,
        "password": password
    })