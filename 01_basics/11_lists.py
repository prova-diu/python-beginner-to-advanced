subjects = ["Python", "Math", "English"]
subjects.append("Science")
subjects.insert(1, "Art")
print("First subject:", subjects[0])
subjects[0] = "Advanced Python"
subjects.remove("Art")
last_subject = subjects.pop()
print("Removed last item:", last_subject)
print("Current subjects:", subjects)

scores = [76, 91, 68, 85]
print("Sorted copy:", sorted(scores))
print("Original order:", scores)
scores.sort(reverse=True)
print("Changed in place:", scores)
print("Average:", sum(scores) / len(scores))
