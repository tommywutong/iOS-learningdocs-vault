---
title: OSSpinLock 不安全
source_url: 'https://mjtsai.com/blog/2015/12/16/osspinlock-is-unsafe/'
source_domain: mjtsai.com
source_group: single-site
original_language: en
published: 2015-12-16
archived_at: 2026-07-27
content_hash: 'sha256:2e4290ec84780865'
plan_ref: 第四周：线程、GCD、Operation 与锁 / Day 6｜锁的学习方式是“按约束选择”（对应 W3-11）
plan_week: 第四周：线程、GCD、Operation 与锁
plan_day: Day 6｜锁的学习方式是“按约束选择”（对应 W3-11）
container: '//div[@id=''main'']'
container_source: guess
translated: true
---

> 原文：[OSSpinLock Is Unsafe](https://mjtsai.com/blog/2015/12/16/osspinlock-is-unsafe/)

Wednesday, [December](https://mjtsai.com/blog/2015/12/) [16](https://mjtsai.com/blog/2015/12/16/), [2015](https://mjtsai.com/blog/2015/)

# [OSSpinLock 不安全](https://mjtsai.com/blog/2015/12/16/osspinlock-is-unsafe/)

[John McCall](https://forums.swift.org/t/thread-safety-of-weak-properties/422/7)（via [Peter Steinberger](https://twitter.com/steipete/status/676851647042203648)）：

> 自旋锁在 iOS 上是不合法的，因为它无法在优先级反转（priority inversion）情况下保证执行进度。

[Greg Parker](https://forums.swift.org/t/thread-safety-of-weak-properties/422/12)：

> 除非你能够保证所有使用者具有相同的优先级，否则 OSSpinLock 是不安全的。

[David Smith](https://twitter.com/Catfish_Man/status/676851988596809728)：

> 这也适用于新的 MacBook，因为它们在热过载（thermal overload）情况下会降低优先级并限制频率。

> 作为补偿，在新系统中 pthread mutex 比过去快 2–2.5 倍。

遗憾的是这一点[没有文档记录](https://developer.apple.com/library/mac/documentation/System/Reference/OSAtomic_header_reference)。但能看到 Apple 工程师公开讨论这类细节，这难道不是很棒吗？

更新（2015-12-31）：[Kevin Ballard](http://engineering.postmates.com/Spinlocks-Considered-Harmful-On-iOS/)：

> 造成这个问题的根源在于线程调度器（thread scheduler）和 QOS。你还记得我说过低优先级线程最终也会得到执行吗？[有了 QOS 之后，情况就不再是这样了](https://forums.swift.org/t/thread-safety-of-weak-properties/422/13)。更具体地说，高 QOS 类别的线程永远不会衰减到低 QOS 类别，而调度器总是优先执行给定 QOS 类别下的可运行线程，然后才会考虑较低类别的线程。由于在自旋锁上自旋的线程始终是可运行的，这意味着如果有足够多的高 QOS 线程在等待一个被低 QOS 线程持有的锁，那么持有锁的那个线程将**永远不会执行**。
>
> […]
>
> Obj-C Runtime 转而使用了一种交接锁（handoff lock）算法，其中自旋锁的大小为一个字（word），而持有锁的线程实际上会将其线程 ID 存储到锁中。阻塞在该锁上的线程可以临时把自己的优先级捐给持有锁的线程，这样就修复了优先级反转问题。涉及多个锁时可能会有潜在问题，但在实践中是有效的。这个方案唯一的问题是[它依赖于私有 API](https://forums.swift.org/t/thread-safety-of-weak-properties/422/17)，而且自旋锁的实现本身也不是公开的，所以第三方代码无法使用这些锁。

更新（2022-10-10）：另请参阅：[Improving Firefox Responsiveness on macOS](https://mjtsai.com/blog/2022/10/10/improving-firefox-responsiveness-on-macos/)。

[Concurrency](https://mjtsai.com/blog/tag/concurrency/) [Documentation](https://mjtsai.com/blog/tag/documentation/) [iOS](https://mjtsai.com/blog/tag/ios/) [iOS 9](https://mjtsai.com/blog/tag/ios-9/) [Mac](https://mjtsai.com/blog/tag/mac/) [Mac OS X 10.11 El Capitan](https://mjtsai.com/blog/tag/mac-os-x-10-11/) [Objective-C Runtime](https://mjtsai.com/blog/tag/objective-c-runtime/) [Programming](https://mjtsai.com/blog/tag/programming/) [Thermal](https://mjtsai.com/blog/tag/thermal/)

## 8 条评论 [RSS](https://mjtsai.com/blog/2015/12/16/osspinlock-is-unsafe/feed/) · [Twitter](https://twitter.com/search?q=from%3Amjtsai%20since%3A2015-12-16%20until%3A2015-12-17&src=typed_query&f=top)

---

[…] 除 OSSpinLock 外，dispatch_semaphore 和 pthread_mutex 性能是最高的。有消息称，苹果在新系统中已经优化了 pthread_mutex 的性能，所以它看上去和 […]

---

Stack Overflow 上有几个相关问题。我认为它们可能与这个 bug 有关：
 [http://stackoverflow.com/questions/30269243/application-sticks-on-osspinlocklockslow](http://stackoverflow.com/questions/30269243/application-sticks-on-osspinlocklockslow)
 [http://stackoverflow.com/questions/30082371/how-to-debug-syscall-thread-switch-in-ios-8-3?lq=1](http://stackoverflow.com/questions/30082371/how-to-debug-syscall-thread-switch-in-ios-8-3?lq=1)
 [http://stackoverflow.com/questions/29624696/syscall-thread-switch-ios-8-3-race-cocoalumberjack-bug-how-to-debug-this?lq=1](http://stackoverflow.com/questions/29624696/syscall-thread-switch-ios-8-3-race-cocoalumberjack-bug-how-to-debug-this?lq=1)

我们遇到了非常相似的问题。我们使用的是 Unity3D 游戏引擎，包含大量插件，且无法访问源代码。

另外，OpenRadar 的 bug 报告：
 [http://openradar.appspot.com/23896366](http://openradar.appspot.com/23896366)

---

[…] OSSpinLock 不安全，Mutexes 与闭包捕获（Closure Capture）之间的关系 […]

---

[…] 锁、线程安全与 Swift，OSSpinLock 不安全， […]

---

[…] 除了 OSSpinLock 外，dispatch_semaphore 和 pthread_mutex 性能是最高的。有消息称，苹果在新系统中已经优化了 pthread_mutex 的性能，所以它看上去和 OSSpinLock 的差距并没有那么大了。 […]

---

[…] 如果问题仍然存在——这是 iOS 中的 bug：OpenRadar 崩溃报告。另外，你可能会发现这篇博客文章很有用：[博客文章] […] .

---

[…] 可能会导致接近活锁（near live-lock）的状态，让 Firefox 实际上挂起（hang）。Apple 内部已知 OSSpinLock 存在这个问题，因此它的 […]

---

这里的讽刺意味真是无以复加。

Apple 提供给第三方使用的 API 如此缓慢，以至于 Firefox 不得不使用未经文档记录、逆向工程来的 API——这意味着它既无法在 App Store 上架，也随时可能因系统更新而失效。别忘了，Firefox 是第一个成功 web 浏览器的后继者，没有它就没有万维网（world-wide-web）。而没有万维网，Apple 大概率只是一个市场小得多的利基产品——因为 Web 日益重要的地位使得许多人得以摆脱 Windows。所以 Apple 毫无感恩之心。

哦，最精彩的是：Microsoft 曾因保留未文档化的专有 API 来让自己的软件获得性能优势、不公平地阻止竞争对手提供相同性能的产品而陷入巨大麻烦。Apple 在 Microsoft 因同样行为受到惩罚之后，仍然用 Safari 和 MacOS 复制了 IE 与 Windows 的局面，这显示出其令人难以置信的傲慢。这位巨人早就该被击倒了。
