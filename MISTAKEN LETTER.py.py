# SSUUBI STEPHEN
# M24B13/007


class Letter:
    def __init__(self, sender, recipient_name, recipient_school, content):
        self.sender = sender
        self.recipient_name = recipient_name
        self.recipient_school = recipient_school
        self.content = content

    def __str__(self):
        return f"From: {self.sender}\nTo: {self.recipient_name} ({self.recipient_school})\nMessage: {self.content}"


class School:
    def __init__(self, name, students):
        self.name = name
        self.students = students  # List of student names

    def receive_letter(self, letter):
        print(f"\nLetter received at {self.name}:")
        print(letter)
        # Check if intended recipient is in this school
        if letter.recipient_name in self.students:
            print(f"{letter.recipient_name} replies: Thankyou for the letter!")
        else:
            # Pick a random student to reply
            responder = self.students[0]
            print(f"{responder} (not the intended recipient) replies: Opps! Wrong receipient, hey though!")


# Setup schools
school_A = School("Makerere College", ["Stephen", "Joshua"])
school_B = School("Acorn International", ["Ethan", "Liam"])

# Girl writes the first letter with a mistaken school name
letter1 = Letter(sender="Ashley", recipient_name="Stephen", recipient_school="Acorn International",
                 content="Hi Stephen, You good? Hope all is well!")

# Letter goes to Bluefield Academy (mistaken school)
school_B.receive_letter(letter1)

# Girl realizes the mistake and writes again
letter2 = Letter(sender="Ashley", recipient_name="Stephen", recipient_school="Makerere College",
                 content="Oops! I sent it to the wrong school. Here's the correct one. Hope you're well!")

# Letter goes to Greenhill High (correct school)
school_A.receive_letter(letter2)