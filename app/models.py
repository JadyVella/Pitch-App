class PICKUPLINES:
    all_pickuplines = []
    def __init__(self,title,pitch):
        self.title = title
        self.pitch = pitch

    def save_pickupline(self):
        PICKUPLINES.all_pickuplines.append(self)


class INTERVIEW:
    all_interview = []
    def __init__(self,title,pitch):
        self.title = title
        self.pitch = pitch

    def save_interview(self):
        INTERVIEW.all_interview.append(self)


class BUSINESSPLAN:
    all_businessplan = []
    def __init__(self,title,pitch):
        self.title = title
        self.pitch = pitch

    def save_businessplan(self):
        BUSINESSPLAN.all_businessplan.append(self)