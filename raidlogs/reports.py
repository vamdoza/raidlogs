from datetime import datetime


# todo abstract report data to its own class.
# todo cache parsed data to avoid re-calculation every time.
class FightReport(object):

    def __init__(self, data=None):
        self.data = data

    """Returns raid duration in seconds"""

    def get_raid_duration(self):
        data = self.data
        raid_start = self.__from_timestamp(data.get("start", 0))
        raid_end = self.__from_timestamp(data.get("end", 0))
        duration = raid_end - raid_start
        return duration.total_seconds()

    def get_active_time(self):
        data = self.data
        fights = data.get("fights", [])
        fight_durations = self.__extract_fight_durations(fights)
        return sum(fight_durations)

    def get_inactive_time(self):
        data = self.data
        fights = data.get("fights", [])
        fight_durations = self.__extract_fight_durations(fights)
        return self.get_raid_duration() - sum(fight_durations)

    def get_time_report(self):
        time_report = {"raid_duration": self.get_raid_duration(),
                       "active_time": self.get_active_time(),
                       "inactive_time": self.get_inactive_time()}

        return time_report

    def __extract_fight_durations(self, fights):
        durations = []
        for fight in fights:
            start = self.__from_timestamp(fight.get("start_time", 0))
            end = self.__from_timestamp(fight.get("end_time", 0))
            duration = end - start
            durations.append(duration.total_seconds())
        return durations

    def print_time_report(self, report):
        raid_time = report["raid_time"]
        active_time = report.get("active_time")
        inactive_time = report.get("inactive_time")

        print("time:%s, active:%.2f%%, inactive:%.2f%%" % (report["raid_time"] // 60,
                                                           self.__percentage(active_time, raid_time),
                                                           self.__percentage(inactive_time, raid_time)))

    @staticmethod
    def __from_timestamp(timestamp):
        # todo add check to identify if timestamp is in miliseconds or seconds, miliseconds is assumed.
        return datetime.fromtimestamp(timestamp / 1000.0)

    @staticmethod
    def __percentage(part, whole, base=100):
        return float(part) / float(whole) * float(base)
