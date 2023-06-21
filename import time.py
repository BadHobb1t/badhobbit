# import time


# class RunningCodeJudge:
#     def __init__(self):
#         self.start = None

#     def __enter__(self):
#         print("...start")
#         self.start = time.time()

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         t = time.time()
#         print(f'Время выполнения кода {t - self.start} сек')
#         print("...end")



# with RunningCodeJudge():
#     my_list = [x for x in range(1, 100_000_000)]

