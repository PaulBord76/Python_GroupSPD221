answer = []

print("What has legs but can't walk? ")
answer += input().split()
print("What goes up when the rain comes down? ")
answer += input().split()
print("What do you call a snowman in the summer? ")
answer += input().split()
print("What is the only vegetable that will make you cry? ")
answer += input().split()
print("It's not a watch, but it ticks. ")
answer += input().split()

print(answer)

correct_answers = ("chair", "umbrella", "puddle", "onion", "heart")

print(correct_answers)

total = {}

i = 0

while i < len(answer):
    if answer[i] == correct_answers[i]:
        total[correct_answers[i]] = 1
    else:
        total[correct_answers[i]] = 0
    i += 1

print(total)
