def collect_feedback():
    feedback_list = []
    while True:
        name = input("Enter student name (or 'done' to finish): ")
        if name.lower() == 'done':
            break
        score = float(input(f"Enter feedback score for {name}: "))
        feedback_list.append({"name": name, "score": score})
    return feedback_list

if __name__ == "__main__":
    feedback = collect_feedback()
    print(feedback)
