class ticket:
    def _init__(self,staffid,creatorName,contactEmail,desc,status,response):
        self.staffid = 'Paul'
        self.creatorName = 'John'
        self.contactEmail = contactEmail
        self.desc = desc
        self.status = 'Open' # all new tickets start as 'Open'
        self.response = "Password change"
    def generateTicNum(self, num):
        self.num = num + 2000
    def input_response(self,inputResponse):
        self.inputResponse = inputResponse
        # Input response to ticket
    def resolve_password(self):
        first_two = ticket.staffid[:2]
        first_three = ticket.creatorName[:3]
        if ticket.input_response == "Password change":
            print("Password changed to: " + first_two + first_three)
            self.status = 'Closed'
            self.respose = "Password changed to: " + first_two + first_three
        # check if the descprption says 'Password change'
        # if yes generate new password adn update respinse status to closed
        # string operation to create password
        # The first two characters of the staffID, followed by the first three characters of the ticket creator name.
    def reopen(self):
        self.status = 'Opened'
        #change the status to reopened
    def resolve_ticket(self):
        self=self
        # find a ticket with a certain number and resolve it

class help_desk:
    def __init__(self):
        self = self
        helpDeskRecord=[ticket]
        # make attribrute
    def create_ticket(self):
        self=self
        # creates a new ticket and adds it to the list of tickets
    def display_ticket(self):
        self = self
        # write code to diplay all tickets
    def all_records(self):
        self=self
        # Displays all tickets in the system
    def stats(self):
        self=self
        # Shows stats of tickets, shows # of tickets created, # resolved and # open