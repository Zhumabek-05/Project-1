# Global
name = "Global Name"

def outer_function():
    # Enclosing
    name = "Enclosing Name"

    def inner_function():
        # Local
        name = "Local Name"
        print("Внутри inner_function:", name)

    inner_function()
    print("Внутри outer_function:", name)

outer_function()
print("На глобальном уровне:", name)
