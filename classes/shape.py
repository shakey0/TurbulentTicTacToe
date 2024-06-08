class Shape:
    
    def __init__(self, name, variant, message, coordinates):
        self.name = name
        self.variant = variant
        self.message = message
        self.coordinates = coordinates
        # May store more data like which turn the shape was created, number of points, etc.
        # For some games shapes may be destroyed or damaged, this could change or erase the points for the shape

    def __str__(self):
        return f"<shape_object: {self.name}, {self.variant}, {self.message}, {self.coordinates}>"
