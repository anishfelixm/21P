def main():
    with open("story.txt") as f:
        story = f.read()
    
    words = set()
    start_ind = -1

    target_start = "<"
    target_end = ">"

    for i, char  in enumerate(story):
        if char == target_start:
            start_ind = i
        
        if char == target_end and i != -1:
            word = story[start_ind: i+1]
            words.add(word)
            start_ind = -1
    
    answers = {}

    for word in words:
        answers[word] = input(f"Enter your word for {word}: ")
        story = story.replace(word, answers[word])
    
    print(story)

if __name__ == "__main__":
    main()