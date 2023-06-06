"""En este segundo ejercicios tendréis que crear un script que nos diga si es la hora de ir a casa.
Tendréis que hacer uso del modulo time. Necesitaréis la fecha del sistema y poder comprobar la hora.

En el caso de que sean más de las 7, se mostrará un mensaje y en caso contrario,
haréis una operación para calcular el tiempo que queda de trabajo."""

import time


def check_time():
    """Codigo para comprobar la hora"""
    seconds = time.time()
    date_time = time.gmtime(seconds)
    if date_time.tm_hour < 19 or (
            date_time.tm_hour == 19 and date_time.tm_min == 0 and date_time.tm_sec == 0):
        date_time_exit = (date_time.tm_year, date_time.tm_mon, date_time.tm_mday,
                          19, 0, 0, date_time.tm_wday, date_time.tm_yday, date_time.tm_isdst)
        seconds_exit = time.mktime(date_time_exit)
        seconds_to_exit = seconds_exit - seconds
        result = time.gmtime(seconds_to_exit)
        print(
            f"Te quedan {result.tm_hour} hora, {result.tm_min} minutos y {result.tm_sec} para irte a casa.")
    else:
        print("Ya son mas de las 19. Es hora de volver a casa!")


if __name__ == '__main__':
    check_time()
