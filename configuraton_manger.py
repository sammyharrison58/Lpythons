# User Configuration Manager

# Test dictionary
test_settings = {
    'theme': 'light',
    'notifications': 'enabled',
    'volume': 'high'
}

# List of available settings (used in some steps)
setting_list = ('theme', 'notifications', 'volume')


def add_setting(settings, new_setting):
    """Add a new setting if it doesn't exist."""
    key = str(new_setting[0]).lower()
    value = str(new_setting[1]).lower()

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        settings[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(settings, new_setting):
    """Update an existing setting."""
    key = str(new_setting[0]).lower()
    value = str(new_setting[1]).lower()

    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


def delete_setting(settings, setting_key):
    """Delete a setting if it exists."""
    key = str(setting_key).lower()

    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return f"Setting not found!"


def view_settings(settings):
    """Return formatted view of all settings."""
    if not settings:
        return "No settings available."

    lines = ["Current User Settings:"]
    for key, value in settings.items():
        lines.append(f"{key.capitalize()}: {value}")

    return "\n".join(lines) + "\n"


