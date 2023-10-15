import sqlite3
import datetime as DT


class DataBase:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM 'users' WHERE user_id = ?",
                                         (user_id,)).fetchall()  # Проверяем на наличие в БД
            return bool(len(result))

    def add_user(self, user_id, name, start_time, end_time, refer_id=None):
        with self.connection:
            if refer_id != None:
                return self.cursor.execute(
                    "INSERT INTO 'users' ('user_id', 'name', 'start_time', 'end_time', 'refer_id')"
                    " VALUES (?, ?, ?, ?, ?)", (user_id, name, start_time, end_time, refer_id))
            else:
                return self.cursor.execute(
                    "INSERT INTO 'users' ('user_id', 'name', 'start_time', 'end_time') VALUES (?, ?, ?, ?)",

                    (user_id, name, start_time, end_time))  # Добавляем значение в БД

    def count_refer(self, user_id):
        with self.connection:
            return \
            self.cursor.execute("SELECT COUNT('id') as count FROM 'users' WHERE refer_id = ?", (user_id,)).fetchone()[0]

    def pro(self, active, user_id):
        with self.connection:
            return self.cursor.execute("UPDATE 'users' SET 'vip' = ? WHERE user_id = ?",
                                       (active, user_id,))  # Обновляем значение

    def end_time(self, user_id):
        with self.connection:
            return self.cursor.execute("SELECT end_time FROM 'users' WHERE user_id = ?", (user_id,)).fetchone()[0]

    def start_time(self, user_id):
        with self.connection:
            return self.cursor.execute("SELECT start_time FROM 'users' WHERE user_id = ?", (user_id,)).fetchone()[0]

    def get_vip_status(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT vip FROM 'users' WHERE user_id = ?",
                                         (user_id,)).fetchone()  # Достаём ОДНО значение
            return result[0]

    def get_active_status(self, user_id):
        with self.connection:
            return self.cursor.execute("SELECT active FROM 'users' WHERE user_id = ?", (user_id,)).fetchone()[0]

    def get_all_user_id(self):
        with self.connection:
            return self.cursor.execute("SELECT user_id FROM 'users'").fetchall()  # Получить все user_id

    def get_users(self):
        with self.connection:
            return self.cursor.execute("SELECT user_id, active FROM 'users'").fetchall()

    def change_seb_3day(self, vip_status, end_time):
        now_3 = DT.datetime.now()

        # now_3 = now + DT.timedelta(days=3)
        last_year_3 = str(now_3)[:4]
        last_month_3 = str(now_3)[5:7]
        last_day_3 = str(now_3)[8:10]

        if bool(vip_status) and int(end_time[:2]) == int(last_day_3) and end_time[3:5] == last_month_3 and\
                end_time[6:11] == last_year_3:
            return 'ok'

        if bool(vip_status) and int(end_time[:2]) - 2 == int(last_day_3) and end_time[3:5] == last_month_3 and\
                end_time[6:11] == last_year_3:
            return 2

        if bool(vip_status) and int(end_time[:2]) - 1 == int(last_day_3) and end_time[3:5] == last_month_3 and\
                end_time[6:11] == last_year_3:
            return 1

    def change_seb_week(self, vip_status, end_time):
        now_7 = DT.datetime.now()

        # now_7 = now + DT.timedelta(days=7)
        last_year_7 = str(now_7)[:4]
        last_month_7 = str(now_7)[5:7]
        last_day_7 = str(now_7)[8:10]

        if bool(vip_status) and int(end_time[:2]) == int(last_day_7) and end_time[3:5] == last_month_7 and\
                end_time[6:11] == last_year_7:
            return 'ok'

        if bool(vip_status) and int(end_time[:2]) - 4 == int(last_day_7) and end_time[3:5] == last_month_7 and\
                end_time[6:11] == last_year_7:
            return 4

        if bool(vip_status) and int(end_time[:2]) - 2 == int(last_day_7) and end_time[3:5] == last_month_7 and\
                end_time[6:11] == last_year_7:
            return 2

        if bool(vip_status) and int(end_time[:2]) - 1 == int(last_day_7) and end_time[3:5] == last_month_7 and\
                end_time[6:11] == last_year_7:
            return 1

    def change_seb_month(self, vip_status, end_time):
        now_month = DT.datetime.now()

        # now_month = now + DT.timedelta(days=31)
        last_year_month = str(now_month)[:4]
        last_month_month = str(now_month)[5:7]
        last_day_month = str(now_month)[8:10]

        if bool(vip_status) and int(end_time[:2]) == int(last_day_month) and end_time[3:5] == last_month_month and\
                end_time[6:11] == last_year_month:
            return 'ok'

        if bool(vip_status) and int(end_time[:2]) - 4 == int(last_day_month) and end_time[3:5] == last_month_month and\
                end_time[6:11] == last_year_month:
            return 4

        if bool(vip_status) and int(end_time[:2]) - 2 == int(last_day_month) and end_time[3:5] == last_month_month and\
                end_time[6:11] == last_year_month:
            return 2

        if bool(vip_status) and int(end_time[:2]) - 1 == int(last_day_month) and end_time[3:5] == last_month_month and\
                end_time[6:11] == last_year_month:
            return 1

    def change_seb_midle_year(self, vip_status, end_time):
        now_midle_year = DT.datetime.now()

        # now_midle_year = now + DT.timedelta(days=183)
        last_year_midle_year = str(now_midle_year)[:4]
        last_month_midle_year = str(now_midle_year)[5:7]
        last_day_midle_year = str(now_midle_year)[8:10]

        if bool(vip_status) and int(end_time[:2]) == int(last_day_midle_year) and end_time[3:5] == last_month_midle_year\
                and end_time[6:11] == last_year_midle_year:
            return 'ok'

        if bool(vip_status) and int(end_time[:2]) - 4 == int(last_day_midle_year) and\
                end_time[3:5] == last_month_midle_year and end_time[6:11] == last_year_midle_year:
            return 4

        if bool(vip_status) and int(end_time[:2]) - 2 == int(last_day_midle_year) and\
                end_time[3:5] == last_month_midle_year and end_time[6:11] == last_year_midle_year:
            return 2

        if bool(vip_status) and int(end_time[:2]) - 1 == int(last_day_midle_year) and\
                end_time[3:5] == last_month_midle_year and end_time[6:11] == last_year_midle_year:
            return 1

    def change_seb_year(self, vip_status, end_time):
        now_year = DT.datetime.now()

        # now_year = now + DT.timedelta(days=366)
        last_year_year = str(now_year)[:4]
        last_month_year = str(now_year)[5:7]
        last_day_year = str(now_year)[8:10]

        if bool(vip_status) and int(end_time[:2]) == int(last_day_year) and end_time[3:5] == last_month_year and\
                end_time[6:11] == last_year_year:
            return 'ok'

        if bool(vip_status) and int(end_time[:2]) - 4 == int(last_day_year) and end_time[3:5] == last_month_year and\
                end_time[6:11] == last_year_year:
            return 4

        if bool(vip_status) and int(end_time[:2]) - 2 == int(last_day_year) and end_time[3:5] == last_month_year and\
                end_time[6:11] == last_year_year:
            return 2

        if bool(vip_status) and int(end_time[:2]) - 1 == int(last_day_year) and end_time[3:5] == last_month_year and\
                end_time[6:11] == last_year_year:
            return 1

    # ************************************** УДАЛЯТЬ И СТАВИТЬ ПОДПИСКУ ******************************

    def unviped(self, user_id):
        with self.connection:
            return self.cursor.execute("UPDATE 'users' SET 'vip' = ? WHERE user_id = ?", (0, user_id,)), \
                   self.cursor.execute("UPDATE 'users' SET 'start_time' = ? WHERE user_id = ?", (0, user_id,)), \
                   self.cursor.execute("UPDATE 'users' SET 'end_time' = ? WHERE user_id = ?", (0, user_id,))

    def viped_3(self, user_id):
        now = DT.datetime.now()

        start_time = now.strftime("%d-%m-%Y")

        now = now + DT.timedelta(days=3)
        last_year = str(now)[:4]
        last_month = str(now)[5:7]
        last_day = str(now)[8:10]

        end_time = last_day + '-' + last_month + '-' + last_year

        with self.connection:
            return self.cursor.execute("UPDATE 'users' SET 'vip' = ? WHERE user_id = ?", (1, user_id,)), \
                   self.cursor.execute("UPDATE 'users' SET 'start_time' = ? WHERE user_id = ?", (start_time, user_id,)), \
                   self.cursor.execute("UPDATE 'users' SET 'end_time' = ? WHERE user_id = ?", (end_time, user_id,))

    def viped_week(self, user_id):
        now = DT.datetime.now()

        start_time = now.strftime("%d-%m-%Y")

        now = now + DT.timedelta(days=7)
        last_year = str(now)[:4]
        last_month = str(now)[5:7]
        last_day = str(now)[8:10]

        end_time = last_day + '-' + last_month + '-' + last_year

        with self.connection:
            return self.cursor.execute("UPDATE 'users' SET 'vip' = ? WHERE user_id = ?", (1, user_id,)), \
                   self.cursor.execute("UPDATE 'users' SET 'start_time' = ? WHERE user_id = ?", (start_time, user_id,)), \
                   self.cursor.execute("UPDATE 'users' SET 'end_time' = ? WHERE user_id = ?", (end_time, user_id,))

    def viped_month(self, user_id):
        now = DT.datetime.now()

        start_time = now.strftime("%d-%m-%Y")

        now = now + DT.timedelta(days=31)
        last_year = str(now)[:4]
        last_month = str(now)[5:7]
        last_day = str(now)[8:10]

        end_time = last_day + '-' + last_month + '-' + last_year

        with self.connection:
            return self.cursor.execute("UPDATE 'users' SET 'vip' = ? WHERE user_id = ?", (1, user_id,)), \
                   self.cursor.execute("UPDATE 'users' SET 'start_time' = ? WHERE user_id = ?", (start_time, user_id,)), \
                   self.cursor.execute("UPDATE 'users' SET 'end_time' = ? WHERE user_id = ?", (end_time, user_id,))

    def viped_midle_year(self, user_id):
        now = DT.datetime.now()

        start_time = now.strftime("%d-%m-%Y")

        now = now + DT.timedelta(days=183)
        last_year = str(now)[:4]
        last_month = str(now)[5:7]
        last_day = str(now)[8:10]

        end_time = last_day + '-' + last_month + '-' + last_year

        with self.connection:
            return self.cursor.execute("UPDATE 'users' SET 'vip' = ? WHERE user_id = ?", (1, user_id,)), \
                   self.cursor.execute("UPDATE 'users' SET 'start_time' = ? WHERE user_id = ?", (start_time, user_id,)), \
                   self.cursor.execute("UPDATE 'users' SET 'end_time' = ? WHERE user_id = ?", (end_time, user_id,))

    def viped_year(self, user_id):
        now = DT.datetime.now()

        start_time = now.strftime("%d-%m-%Y")

        now = now + DT.timedelta(days=366)
        last_year = str(now)[:4]
        last_month = str(now)[5:7]
        last_day = str(now)[8:10]

        end_time = last_day + '-' + last_month + '-' + last_year

        with self.connection:
            return self.cursor.execute("UPDATE 'users' SET 'vip' = ? WHERE user_id = ?", (1, user_id,)), \
                   self.cursor.execute("UPDATE 'users' SET 'start_time' = ? WHERE user_id = ?", (start_time, user_id,)), \
                   self.cursor.execute("UPDATE 'users' SET 'end_time' = ? WHERE user_id = ?", (end_time, user_id,))

    def add_bill_id(self, bill_id, user_id):
        with self.connection:
            return self.cursor.execute("UPDATE 'users' SET 'bill_id' = ? WHERE user_id = ?", (bill_id, user_id,))

    def get_bill_id(self, user_id):
        with self.connection:
            return self.cursor.execute("SELECT bill_id FROM 'users' WHERE user_id = ?", (user_id,)).fetchone()[0]

    def get_info_users(self, user_id):
        with self.connection:
            name = self.cursor.execute("SELECT name FROM 'users' WHERE user_id = ?", (user_id,)).fetchone()[0]
            id = self.cursor.execute("SELECT user_id FROM 'users' WHERE user_id = ?", (user_id,)).fetchone()[0]
            sub = self.cursor.execute("SELECT vip FROM 'users' WHERE user_id = ?", (user_id,)).fetchone()[0]
            start_time = self.cursor.execute("SELECT start_time FROM 'users' WHERE user_id = ?", (user_id,)).fetchone()[
                0]
            end_time = self.cursor.execute("SELECT end_time FROM 'users' WHERE user_id = ?", (user_id,)).fetchone()[0]

            return name, id, sub, start_time, end_time

    def set_active(self, user_id, active):
        with self.connection:
            return self.cursor.execute("UPDATE 'users' SET 'active' = ? WHERE user_id = ?", (active, user_id,))

    def set_proffessional(self, user_id):
        with self.connection:
            return self.cursor.execute("UPDATE 'users' SET 'professional' = ? WHERE user_id = ?", (0, user_id,))
