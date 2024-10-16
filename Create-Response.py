from openai import OpenAI

# Initialize OpenAI client
client = OpenAI()

# Define initial variables
CURRENT_X = 0
CURRENT_Y = 0
GOAL_X = 10
GOAL_Y = 10

def get_movement_plan(current_x, current_y, goal_x, goal_y):
    system_message = """You are a high-level movement planner for a robot. 
    Given the current location and goal location, provide a series of movement commands.
    Respond with a list of commands, one per line, using only these options:
    MOVE_FORWARD <distance>
    TURN_LEFT <degrees>
    TURN_RIGHT <degrees>
    Your response should be easily parsable by a simple program."""

    user_message = f"""Current location: ({current_x}, {current_y})
    Goal location: ({goal_x}, {goal_y})
    Plan a series of movements to reach the goal."""

    completion = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message}
        ]
    )

    return completion.choices[0].message.content

def main():
    plan = get_movement_plan(CURRENT_X, CURRENT_Y, GOAL_X, GOAL_Y)
    print("Movement Plan:")
    print(plan)

if __name__ == "__main__":
    main()
