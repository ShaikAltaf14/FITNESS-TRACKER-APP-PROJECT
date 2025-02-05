class User:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight  # in kilograms
        self.height = height  # in meters
        self.total_calories_burned = 0
        self.total_steps = 0
        self.workout_log = []

    def update_workout(self, workout_type, duration_minutes, calories_burned, steps):
        workout = {
            'workout_type': workout_type,
            'duration_minutes': duration_minutes,
            'calories_burned': calories_burned,
            'steps': steps,
        }
        self.workout_log.append(workout)
        self.total_calories_burned += calories_burned
        self.total_steps += steps

    def show_summary(self):
        print(f"Fitness Summary for {self.name}:")
        print(f"Age: {self.age}, Weight: {self.weight}kg, Height: {self.height}m")
        print(f"Total Calories Burned: {self.total_calories_burned} kcal")
        print(f"Total Steps Taken: {self.total_steps} steps")
        print("Workout Log:")
        for workout in self.workout_log:
            print(f"- {workout['workout_type']} for {workout['duration_minutes']} mins, "
                  f"Calories Burned: {workout['calories_burned']} kcal, Steps: {workout['steps']}")

    def set_goal(self, target_calories, target_steps):
        self.target_calories = target_calories
        self.target_steps = target_steps

    def check_progress(self):
        print(f"Progress towards Goals:")
        print(f"Target Calories: {self.target_calories} kcal | Calories Burned: {self.total_calories_burned} kcal")
        print(f"Target Steps: {self.target_steps} steps | Steps Taken: {self.total_steps} steps")



if __name__ == "__main__":
    
    user = User(name="John Doe", age=30, weight=75, height=1.75)

    
    user.update_workout(workout_type="Running", duration_minutes=30, calories_burned=300, steps=4000)
    user.update_workout(workout_type="Cycling", duration_minutes=45, calories_burned=500, steps=600)

    
    user.set_goal(target_calories=1000, target_steps=10000)

    
    user.show_summary()
    user.check_progress()

