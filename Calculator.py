# calculator.py

def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

def calculate_variance(numbers):
    mean = calculate_mean(numbers)
    return sum((x - mean) ** 2 for x in numbers) / len(numbers)

def calculate_stddev(numbers):
    variance = calculate_variance(numbers)
    return variance ** 0.5

def main():
    print("Mean, Variance, Standard Deviation Calculator")
    data_input = input("Numbers daalo, comma se separate kar ke (e.g. 10,20,30): ")
    try:
        numbers = [float(x.strip()) for x in data_input.split(',')]
        mean = calculate_mean(numbers)
        variance = calculate_variance(numbers)
        stddev = calculate_stddev(numbers)
        
        print(f"Mean: {mean:.2f}")
        print(f"Variance: {variance:.2f}")
        print(f"Standard Deviation: {stddev:.2f}")
    except Exception as e:
        print("Error: Please enter valid numbers separated by commas.")

if __name__ == "__main__":
    main()