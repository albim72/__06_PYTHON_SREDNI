class ContextManager:
    def __init__(self):
        print("wywołanie funkcji init()")

    def __enter__(self):
        print("wywołanie funkcji enter()")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("wywołanie funkcji exit()")

with ContextManager() as manager:
    print("wykonane bloku with")
