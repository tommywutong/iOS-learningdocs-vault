---
title: 对iOS中自旋锁与优先级反转（Priority inversion）的理解
source_url: 'https://juejin.cn/post/7070416276564213791'
source_domain: juejin.cn
source_group: platform
original_language: zh
published: 2022-03-02
archived_at: 2026-07-27
content_hash: 'sha256:543854c2d1d58661'
plan_ref: 第四周：线程、GCD、Operation 与锁 / Day 6｜锁的学习方式是“按约束选择”（对应 W3-11）
plan_week: 第四周：线程、GCD、Operation 与锁
plan_day: Day 6｜锁的学习方式是“按约束选择”（对应 W3-11）
container: '//div[contains(@class,''markdown-body'')]'
container_source: map
---

> 原文：[对iOS中自旋锁与优先级反转（Priority inversion）的理解](https://juejin.cn/post/7070416276564213791)

> 深入理解代替单纯记忆

## 优先级反转

关于优先级反转，参考资料中《优先级反转那点事儿》讲的比较清晰。此处直接贴过来

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fcf64e4fb34c47319980a5fa18564610~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp)

- 线程A在一个比较低的优先级上工作, 假设是10吧。然后在时间点T1的时候，线程A锁定了一把互斥锁，并开始操作互斥数据。
- 这时有个高优线级线程C（比如优先级20）在时间点T2被唤醒，它也也需要操作互斥数据。当它加锁互斥锁时，因为互斥锁在T1被线程A锁掉了，所以线程C放弃CPU进入阻塞状态，而线程A得以占据CPU，继续执行。
- 事情到这一步还是正确的，虽然优先级10的A线程看上去抢了优先级20的C线程的时间，但因为程序逻辑，C确实需要退出CPU等完成互斥数据操作后，才能获得CPU。
- 但是，假设我们有个线程B在优先级15上，在T3时间点上醒了过来，因为他比当前执行的线程A优先级高，所以它会立即抢占CPU。而线程A被迫进入READY状态等待。
- 一直到时间点T4，线程B放弃CPU，这时优先级10的线程A是唯一READY线程，它再次占据CPU继续执行，最后在T5解锁了互斥锁。
- 在T5，线程A解锁的瞬间，线程C立即获取互斥锁，并在优先级20上等待CPU。因为它比线程A的优先级高，系统立刻调度线程C执行，而线程A再次进入READY状态。

上面这个时序里，线程B从T3到T4占据CPU运行的行为，就是事实上的优先级反转。一个优先级15的线程B，通过压制优线级10的线程A，而事实上导致高优先级线程C无法正确得到CPU。这段时间是不可控的，因为线程B可以长时间占据CPU（即使轮转时间片到时，线程A和B都处于可执行态，但是因为B的优先级高，它依然可以占据CPU），其结果就是高优先级线程C可能长时间无法得到 CPU。

## 优先级反转 vs 自旋锁

- 优先级反转问题的出现跟自旋锁没有关系
- 不使用自旋锁时也可能出现优先级反转问题。只要是线程或任务有多个优先级，理论上就可能有反转问题
- 操作系统在优先级反转发生时通常都会有自动的解决方案，比如提高低优先级线程的优先级等
- 在使用iOS中的`OSSpinLock`时

    - 由于这种锁不会记录持有它的线程信息，所有当发生优先级反转时，系统找不到低优先级的线程，可能因此无法通过提高优先级解决优先级反转问题
    - 再加上，高优先级线程使用自旋锁进行轮训等待锁时在一直占用CPU时间片，使得低优先级线程拿到时间片的概率降低
- 总结下来是

    - 优先级反转问题的出现跟自旋锁没有关系
    - 但一旦出现优先级反转问题，自旋锁会让优先级反转问题不容易解决，甚至造成更严重的线程等待问题

### atomic和os_unfair_lock

- OSSpinLock被废弃后，官方建议使用os_unfair_lock代替；
- os_unfair_lock其实是互斥锁（参考资料中有提到）
- 在老版本中，atomic内部也是用自旋锁实现的，但后续也改成互斥锁了

### 疑惑

1. iOS系统中优先级反转问题是如何解决的？--参考资料中的苹果官方文档有提到

## 参考

- [谈 iOS 的锁](https://link.juejin.cn?target=http%3A%2F%2Fzenonhuang.me%2F2018%2F03%2F08%2Ftechnology%2F2018-03-01-LockForiOS%2F)
- [优先级反转那点事儿](https://link.juejin.cn?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F146132061)
- [不再安全的 OSSpinLock](https://link.juejin.cn?target=https%3A%2F%2Fblog.ibireme.com%2F2016%2F01%2F16%2Fspinlock_is_unsafe_in_ios%2F)
- [dispatch_semaphore 会造成优先级反转，慎用！](https://link.juejin.cn?target=https%3A%2F%2Fblog.51cto.com%2Fu_15064655%2F2573045)
- [Prioritize Work with Quality of Service Classes](https://link.juejin.cn?target=https%3A%2F%2Fdeveloper.apple.com%2Flibrary%2Farchive%2Fdocumentation%2FPerformance%2FConceptual%2FEnergyGuide-iOS%2FPrioritizeWorkWithQoS.html%23%2F%2Fapple_ref%2Fdoc%2Fuid%2FTP40015243-CH39)
