import threading
from time import sleep,ctime

loops=[4,2]

class ThreadFunc(object):
    def __init__(self,func,args,name=''):
        self.name=name
        self.func=func
        self.args=args
    def __call__(self):
        self.func(*self.args)

def loop(i,sec):
    print ('this is thread', i , ' start at ', ctime())
    sleep(sec)
    print ('this is thread', i , ' end at ', ctime())

def main():
    print (ctime())
    threads=[]
    i=range(len(loops))
    for n in i:
        t=threading.Thread(target=ThreadFunc(loop,(n,loops[n]),loop.__name__))
        threads.append(t)
    for n in i:
        threads[n].start()
    for n in i:
        threads[n].join()
    print ('All done'+ ctime())

if __name__=='__main__':
    main()