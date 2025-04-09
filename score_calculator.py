def calculate_average(feedback_list):
    if not feedback_list:
        return 0.0
    return sum(entry["score"] for entry in feedback_list) / len(feedback_list)

if __name__ == "__main__":
    sample = [{"name": "A", "score": 8}, {"name": "B", "score": 6}]
    print("Average:", calculate_average(sample))
