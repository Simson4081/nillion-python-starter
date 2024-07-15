from nada_dsl import *
import random

def nada_main():
    num_mentees = 10
    num_mentors = 5

    # Define parties (mentees and mentors)
    mentees = [Party(name=f"Mentee_{i+1}") for i in range(num_mentees)]
    mentors = [Party(name=f"Mentor_{i+1}") for i in range(num_mentors)]

    # Collect mentee preferences and mentor expertise as secret inputs
    mentee_preferences = []
    mentor_expertise = []
    for i in range(num_mentees):
        preferences = [SecretInteger(Input(name=f"mentee_{i}_pref_{j}", party=mentees[i])) for j in range(num_mentors)]
        mentee_preferences.append(preferences)
    for j in range(num_mentors):
        expertise = [SecretInteger(Input(name=f"mentor_{j}_expertise_{i}", party=mentors[j])) for i in range(num_mentees)]
        mentor_expertise.append(expertise)

    # Matching algorithm: simple preference sum matching
    matches = []
    for i in range(num_mentees):
        best_match = None
        best_score = SecretInteger(Input(name=f"best_score_{i}", party=mentees[i], value=0))
        for j in range(num_mentors):
            score = mentee_preferences[i][j] + mentor_expertise[j][i]
            if score > best_score:
                best_score = score
                best_match = j
        matches.append(best_match)

    # Return the matches as outputs
    outputs = []
    for i in range(num_mentees):
        outputs.append(Output(matches[i], f"mentee_{i}_match", mentees[i]))

    return outputs

# Simulated NADA execution environment
def run_nada_program():
    num_mentees = 10
    num_mentors = 5

    # Simulate mentee preferences and mentor expertise
    mentee_preferences = [[random.randint(1, 10) for _ in range(num_mentors)] for _ in range(num_mentees)]
    mentor_expertise = [[random.randint(1, 10) for _ in range(num_mentees)] for _ in range(num_mentors)]

    # Matching algorithm: simple preference sum matching
    matches = []
    for i in range(num_mentees):
        best_match = None
        best_score = 0
        for j in range(num_mentors):
            score = mentee_preferences[i][j] + mentor_expertise[j][i]
            if score > best_score:
                best_score = score
                best_match = j
        matches.append(best_match)

    return matches

# Running the NADA program to determine matches
matches = run_nada_program()

# Display the matches
print("Mentorship Matches:")
for i, match in enumerate(matches):
    print(f"Mentee {i + 1} is matched with Mentor {match + 1}")
