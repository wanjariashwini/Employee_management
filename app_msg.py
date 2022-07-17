
SERVER_HEALTH_STATUS = "Server is running fine"
SUCCESS = "SUCCESS"
FAILED = "FAILED"
REGISTERED = "Registered successfully"
REGISTERED_FAILED = "Registration failed"
UPDATED = "Updated Successfully"
UPDATED_FAILED = "Failed to update"
NOT_FOUND = "Employee not found"
DELETED = "Deleted Successfully"
DELETED_FAILED = "Failed to delete"
MISSING_DATA = "Input data is missing"
EMAIL_NOT_VALID = "Email is not valid"
MISSING_DATA_EMAIL = "Missing email"
USER_MISSING = "USER NOT MENTION"
INVALID_USER = "User not valid"
NOT_ACTIVE = "User is not active, contact admin"

def create_response(status,messages):

    return {"status": status, "messages" : messages}
