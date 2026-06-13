def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def is_valid_pod_name(name):
    # K8s pod names: lowercase alphanumeric and hyphens, max 63 chars, must start/end with alphanumeric
    import re
    return bool(re.match(r'^[a-z0-9][a-z0-9\-]{0,61}[a-z0-9]$', name))

def get_current_time():
    import time
    return time.time()

def is_pod_expired(created_at, max_age_seconds=3600):
    return (get_current_time() - created_at) > max_age_seconds