---
title: 深入ObjC GCD中的dispatch group工作原理。
source_url: 'https://www.cnblogs.com/bbqzsl/p/5287970.html'
source_domain: cnblogs.com
source_group: platform
original_language: zh
published: ''
archived_at: 2026-07-27
content_hash: 'sha256:2d3cb017715113e3'
plan_ref: 第四周：线程、GCD、Operation 与锁 / Day 3｜GCD 从四格矩阵开始，再扩 API（对应 W3-06）
plan_week: 第四周：线程、GCD、Operation 与锁
plan_day: Day 3｜GCD 从四格矩阵开始，再扩 API（对应 W3-06）
container: '//div[@id=''cnblogs_post_body'']'
container_source: map
---

> 原文：[深入ObjC GCD中的dispatch group工作原理。](https://www.cnblogs.com/bbqzsl/p/5287970.html)

本文是基于GCD的支持库libdispatch的源代码分析的结果或是用于作为源代码阅读的参考，尽量不帖代码，力求用UML图来说明工作流。

本文参考的源代码版本为v501.20.1，如有兴趣请自行到苹果的开源项目网站下载。

dispatch group的相关代码位于dispatch_semaphore.c模块中。下面是分析后的活动图：

![](http://images2015.cnblogs.com/blog/665551/201603/665551-20160317160626443-1405925397.jpg)

dispatch group是一个基于信号量的同步机制，主要提供了下面5个函数：

enter,

leave,

wait,

async,

notify.

活动图中有4组控制流，分别开始于图的四个角，中间有一个同步符号，结合在一起来反应dispatch group的运作原理。

左上角有三条并行的async控制流。调用async方法，将会隐式进行enter和leave，并且分别在不同的两条（并行或异步的控制流）中进行。

右上角是基本形式，在同一条控制流中，enter，处理，然后leave。

左下角是wait的控制流，使用了阻塞等待，等待full semaphore。

右下角是notify的控制流，有两个分支，一个是full semaphore满足，直接唤醒各方的wait，接着就处理notify块；另一个分支则是不满足，但并不用像wait那样采用阻塞等待的方式，而是放入到group的notifyqueue中让将来满足full semaphore后，由另它控制流fork一条控制流(使用notify函数时，指定了dispatch的队列)来处理notify块。

最后就是由谁来唤醒，由图的中间唯一的同步符号可以看到，同步的入流都是或显式或隐式地进行了leave，也就是说在每条控制流执行了leave，都要负责检查full semaphore是否满足，满足则然后唤醒。

说明：这里的fork不一定产生一条线程，在libdispatch框架中，dispatch_async来dispatch到不同的队列由线程调度，达到并行目的。

多谢路过的你观看。

后面将会有两篇文补充，一篇是再说明libdispatch中的group，另一篇则是facebook的开源框架asdk是如何使用了这种同步机制。
