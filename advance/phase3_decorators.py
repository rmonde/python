import random

def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Done: {func.__name__}")
        return result
    return wrapper

@log_call
def deploy(service_name):
    print(f"Deploying {service_name}...")

def retry(max_attempts):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {i+1} failed: {e}")
                    last_error = e
            raise last_error
        return wrapper
    return decorator

@retry(max_attempts=3)
def deploy_with_retry(service_name):
    print(f"Deploying {service_name} with retry...")
    # Simulate a failure
    if random.random() < 0.7:
        raise Exception("Deployment failed..")

def main():
    deploy("User Service")
    deploy_with_retry("Payment Service")

if __name__=="__main__":
    main()