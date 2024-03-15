""" Module for message handling. """


def print_message(message, message_type):
    """Function to print messages"""
    if message_type == "error":
        print(f"❌ {message}.")
    elif message_type == "success":
        print(f"✔ {message}.")
    elif message_type == "warning":
        print(f"⚠ {message}.")
    elif message_type == "info":
        print(f"🔍 {message}.")
    else:
        print(message)
