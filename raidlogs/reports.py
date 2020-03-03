from datetime import datetime


# todo abstract report data to its own class.
class FightReport(object):

    def __init__(self, data=None):
        self.data = data

    def get_time_report(self):
        self.__abstract_data(self.data)

        return ""

    """Returns raid duration in delta"""
    def get_raid_duration(self):
        data = self.data
        raid_start = self.__from_timestamp(data.get("start", 0))
        raid_end = self.__from_timestamp(data.get("end", 0))
        return raid_end - raid_start

    def __abstract_data(self, data):
        fight = data.get("fights", [])
        self.__parse_fights(fight)

        # acum = sum(fight_durations)
        # time = fromtimestamp(raid_end) - fromtimestamp(raid_start)
        #
        # time_report = {"raid_duration": time.total_seconds(),
        #                "active_time": acum,
        #                "inactive_time": time.total_seconds() - acum}

    @staticmethod
    def __parse_fights(fights):
        fight_durations = []
        for fight in fights:
            fight_start = fight.get("start_time")
            fight_end = fight.get("end_time")
            # fight_dur = fight_end - fight_start
            fight_dur = fromtimestamp(fight_end) - fromtimestamp(fight_start)
            fight_durations.append(fight_dur.total_seconds())

    @staticmethod
    def __from_timestamp(timestamp):
        # todo add check to identify wheter timestamp is in miliseconds or seconds, miliseconds is assumed.
        return datetime.fromtimestamp(timestamp / 1000.0)

    # TBD a proper way to handle timestamps and what not in order to parse out results in time.
    def print_time_report(self, report):
        raid_time = report["time"] // 60
        active_time = report.get("active_time") / raid_time
        inactive_time = report.get("inactive_time") / raid_time * 100;

        print("time:%s, active:%.2f%%, inactive:%.2f%%" % (report["time"] // 60,
                                                           self.__percentage(active_time, raid_time),
                                                           self.__percentage(inactive_time, raid_time)))

    @staticmethod
    def __percentage(part, whole, base=100):
        return float(part) / float(whole) * base
