
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
INVALID_USER = "INVALID_USER"
USER_MISSING = "USER NOT FOUND"

def create_response(status,messages):

    return {"status": status, "messages" : messages}
