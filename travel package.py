class Travel:
    def __init__(self, destination, hotel, transport, meal_plan, activities, insurance):
        self.destination = destination
        self.hotel = hotel
        self.transport = transport
        self.meal_plan = meal_plan
        self.activities = activities
        self.insurance = insurance

    def show_travel_info(self):
        print(f"Destination: {self.destination}")
        print(f"Hotel: {self.hotel}")
        print(f"Transport: {self.transport}")
        print(f"Meal Plan: {self.meal_plan}")
        print(f"Activities: {self.activities}")
        print(f"Insurance: {self.insurance}")

class TravelBuilder:
    def __init__(self):
        self.destination = None
        self.hotel = None
        self.transport = None
        self.meal_plan = None
        self.activities = None
        self.insurance = None

    def set_destination(self, destination):
        self.destination = destination
        return self

    def set_hotel(self, hotel):
        self.hotel = hotel
        return self

    def set_transport(self, transport):
        self.transport = transport
        return self

    def set_meal_plan(self, meal_plan):
        self.meal_plan = meal_plan
        return self

    def add_activities(self, activities):
        self.activities = activities
        return self

    def set_insurance(self, insurance):
        self.insurance = insurance
        return self

    def build(self):
        return Travel(
            self.destination,
            self.hotel,
            self.transport,
            self.meal_plan,
            self.activities,
            self.insurance
        )

travel = (
    TravelBuilder()
    .set_destination("Paris")
    .set_hotel("Hotel ABC")
    .set_transport("Flight")
    .set_meal_plan("Breakfast and Dinner")
    .add_activities("City Tour")
    .set_insurance("Comprehensive")
    .build())

travel.show_travel_info()
