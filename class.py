class Ml_journey:
    def __init__(self,name,date):
        self.name =name
        self.date = date
    def __str__(self):
        return f"{self.name} started on {self.date}"

ml = Ml_journey("ML Journey","2024-06-01")
print(ml)