#Exercise 1 — Age Category Resolver

def give_age_category(age: int) -> str:
    age_category = ""
    if age >= 65 :
        age_category = "senior"
    elif age >= 18 :
        age_category = "adult"
    elif age >= 13 :
        age_category = "teenager"
    else :
        age_category = "child"
    return age_category

#Exercise 2 — System Access Authorization

def access_checking(is_authenticated: bool, is_not_banned: bool) -> bool: # -_- , I think the name should have been check_user_acces but I will keep for this time
    has_access = False
    if is_authenticated and is_not_banned :
        has_access = True
    return has_access

#Exercise 3 — Required Field Validation

def check_field_validity(my_string: str) ->str:
    # a field is invalid for none or empty string
    is_field_valid = False 
    if my_string:
        is_field_valid = True
    return is_field_valid

#Exercise 4 — Discount Eligibility Engine
def check_discount(age: int, student_status: bool) -> bool:
    apply_discount = False
    if age < 18 or student_status:
        apply_discount = True
    return apply_discount

#Exercise 5 — Default Value Resolver (Short-Circuit Logic)

def set_username(user: str) -> str:
    return user or "Anonymous" #I tried and it worked
    

# Exercise 6 — Guard Clause Practice

def check_admin_access(is_system_available: bool, is_admin:bool) -> str:
    access_message = ""
    if not is_system_available:
        access_message = "System unavailable"
    elif is_admin:
        access_message = "Access granted"
    else:
        access_message = "Access denied"
    return access_message





if __name__ == "__main__":
    print(give_age_category(96),
          access_checking(True, False),
          check_field_validity("a"),
          check_discount(13, False),
          set_username(""),
          check_admin_access(True, True)          
          )
    