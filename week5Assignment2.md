
---

## 🎭 Activity 2: Polymorphism Challenge — *Vehicles in Motion*

```markdown
# 🚗✈️🚤 Activity 2: Polymorphism with Vehicles

## 🎯 Objective
Create multiple vehicle classes that share a common method (`move()`), but each defines it differently.

## 🧠 Concepts Covered
- Polymorphism
- Method Overriding
- Looping through objects

## 🧪 Code Example

```python
class Vehicle:
    def move(self):
        print("The vehicle is moving.")

class Car(Vehicle):
    def move(self):
        print("Driving on the road 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying through the sky ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing across the water 🚤")

# Example usage
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
