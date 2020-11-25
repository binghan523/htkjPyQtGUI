# *************************************************
# 进程池Pool，适用于任务比较多的时候。重复利用进程去做多任务
from multiprocessing import Pool
import os, time, random


def worker(msg):
    t_start = time.time()
    print("%s开始执行，进程号为%d" % (msg, os.getpid()))  # getpid()用于获取进程号
    time.sleep(random.random() * 2)
    t_stop = time.time()
    print(msg, "执行完毕，耗时%0.2f" % (t_stop - t_start))


if __name__ == '__main__':
    po = Pool(3) # 定义一个进程池，最大进程数为3
    for i in range(0, 10):
        # Pool().apply_async(要调用的目标,(传递给目标的参数元组，))
        # 每次循环将会用空闲出来的子进程去调用目标
        po.apply_async(worker, (i,))

    print("-----start-----")
    po.close()  # 关闭进程池，关闭后po不再接收新的请求
    po.join()  # 等待po中所有子进程执行完成，必须放在close语句之后
    print("-----end-----")


# *************************************************
# # 多进程学习
# import multiprocessing
#
#
# def download(q):
#     """模拟从网上下载数据"""
#     data = [11, 22, 33, 44]
#     # 向队列中写入数据
#     for temp in data:
#         q.put(temp)
#
#     print("下载器已经下载完毕，并且存入到队列中...")
#
#
# def analysis(q):
#     """从队列中获取数据"""
#     waiting_analysis_data = list()
#     while True:
#         data = q.get()
#         waiting_analysis_data.append(data)
#
#         if q.empty():
#             break
#
#     # 模拟数据处理
#     print(waiting_analysis_data)
#
#
# def main():
#     # 1、创建一个队列：
#     q = multiprocessing.Queue()
#
#     # 2、创建多个进程，将队列的引用当做实参进行传递到里面
#     p1 = multiprocessing.Process(target=download, args=(q,))
#     p2 = multiprocessing.Process(target=analysis, args=(q,))
#     p1.start()
#     p2.start()
#
#
# if __name__ == '__main__':
#     main()

# # *************************************************
# # 进程间通信
# # - 当进程在不同电脑上时，使用socket
# # - 当在同一台主机上是，用queue，先进先出，类似于电梯进人下人。用于解耦
# q = multiprocessing.Queue(3)  # 最多放3个
# q.put("111")
# q.put(222)
# q.put([11, 22, 33])
# q.full()  # 判断是否满，返回bool值
# q.empty()  # 判断是否空
# q.get()  # 当没有元素时，阻塞式等待
# q.get_nowait()  # 当没有元素时，不阻塞，返回异常
