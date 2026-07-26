---
title: OSSpinLock Is Unsafe
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
---

> 原文：[OSSpinLock Is Unsafe](https://mjtsai.com/blog/2015/12/16/osspinlock-is-unsafe/)

Wednesday, [December](https://mjtsai.com/blog/2015/12/) [16](https://mjtsai.com/blog/2015/12/16/), [2015](https://mjtsai.com/blog/2015/)

# [OSSpinLock Is Unsafe](https://mjtsai.com/blog/2015/12/16/osspinlock-is-unsafe/)

[John McCall](https://forums.swift.org/t/thread-safety-of-weak-properties/422/7) (via [Peter Steinberger](https://twitter.com/steipete/status/676851647042203648)):

> Spin locks are, unfortunately, illegal on iOS, which does not guarantee progress in the face of priority inversion.

[Greg Parker](https://forums.swift.org/t/thread-safety-of-weak-properties/422/12):

> OSSpinLock is unsafe unless you can guarantee that all users have the same priority.

[David Smith](https://twitter.com/Catfish_Man/status/676851988596809728):

> also applies to the new MacBooks since they will depress priority and throttle in thermal overload situations.

> to compensate, pthread mutexes are 2-2.5x faster than they used to be on new OSs

It’s a shame that this is [not documented](https://developer.apple.com/library/mac/documentation/System/Reference/OSAtomic_header_reference). But how great is it to see Apple engineers discuss these sorts of details in public?

Update (2015-12-31): [Kevin Ballard](http://engineering.postmates.com/Spinlocks-Considered-Harmful-On-iOS/):

> The reason for this comes back to the thread scheduler and QOS. You remember how I said low-priority threads will eventually execute? [That’s no longer true with QOS](https://forums.swift.org/t/thread-safety-of-weak-properties/422/13). More specifically, threads in a higher QOS class will never decay to a lower QOS class, and the scheduler will always prioritize runnable threads in a given QOS class before threads in lower classes. And since threads spinning on a spinlock are always runnable, this means that if there’s enough high-QOS threads waiting on a lock held by a lower-QOS thread, the thread that owns the lock will _never execute_.
> 
> […]
> 
> The Obj-C runtime switched to a handoff lock algorithm, where the spinlock is the size of a word and the owning thread actually stores its thread ID in the lock. Threads that block on the lock can then temporarily donate their priority to the thread that owns the lock, which fixes the priority inversion. There’s potential issues when multiple locks are involved, but in practice it works. The only problem with this solution is [it relies on private API](https://forums.swift.org/t/thread-safety-of-weak-properties/422/17), and the spinlock implementation itself isn’t public, so there’s no way for third-party code to use these locks.

Update (2022-10-10): See also: [Improving Firefox Responsiveness on macOS](https://mjtsai.com/blog/2022/10/10/improving-firefox-responsiveness-on-macos/).

[Concurrency](https://mjtsai.com/blog/tag/concurrency/) [Documentation](https://mjtsai.com/blog/tag/documentation/) [iOS](https://mjtsai.com/blog/tag/ios/) [iOS 9](https://mjtsai.com/blog/tag/ios-9/) [Mac](https://mjtsai.com/blog/tag/mac/) [Mac OS X 10.11 El Capitan](https://mjtsai.com/blog/tag/mac-os-x-10-11/) [Objective-C Runtime](https://mjtsai.com/blog/tag/objective-c-runtime/) [Programming](https://mjtsai.com/blog/tag/programming/) [Thermal](https://mjtsai.com/blog/tag/thermal/)

## 8 Comments [RSS](https://mjtsai.com/blog/2015/12/16/osspinlock-is-unsafe/feed/) · [Twitter](https://twitter.com/search?q=from%3Amjtsai%20since%3A2015-12-16%20until%3A2015-12-17&src=typed_query&f=top)

---

[…] OSSpinLock 外，dispatch_semaphore 和 pthread_mutex 性能是最高的。有消息称，苹果在新系统中已经优化了 pthread_mutex 的性能，所以它看上去和 […]

---

There are several questions on SO. I think they may be related to ths bug:  
 [http://stackoverflow.com/questions/30269243/application-sticks-on-osspinlocklockslow](http://stackoverflow.com/questions/30269243/application-sticks-on-osspinlocklockslow)  
 [http://stackoverflow.com/questions/30082371/how-to-debug-syscall-thread-switch-in-ios-8-3?lq=1](http://stackoverflow.com/questions/30082371/how-to-debug-syscall-thread-switch-in-ios-8-3?lq=1)  
 [http://stackoverflow.com/questions/29624696/syscall-thread-switch-ios-8-3-race-cocoalumberjack-bug-how-to-debug-this?lq=1](http://stackoverflow.com/questions/29624696/syscall-thread-switch-ios-8-3-race-cocoalumberjack-bug-how-to-debug-this?lq=1)

We encountered very similiar issue. We use Unity3d game engine with a lot of lplugins and have no access to the source

Also, OpenRadar bug report:  
 [http://openradar.appspot.com/23896366](http://openradar.appspot.com/23896366)

---

[…] OSSpinLock Is Unsafe, Mutexes and Closure Capture in […]

---

[…] Locks, Thread Safety, and Swift, OSSpinLock Is Unsafe, […]

---

[…] 除了 OSSpinLock 外，dispatch_semaphore 和 pthread_mutex 性能是最高的。有消息称，苹果在新系统中已经优化了 pthread_mutex 的性能，所以它看上去和 OSSpinLock 差距并没有那么大了。 […]

---

[…] 如果问题仍然存在-这是iOS中的错误：OpenRadar崩溃报告另外，您可能会发现此博客文章很有用：博客文章 […]

---

[…] could lead to a near live-lock and Firefox effectively hanging. This problem with OSSpinLock was known within Apple hence its […]

---

The irony here is truly off the scale.

The APIs provided for 3rd party use are so slow, that Firefox is using undocumented reverse engineered APIs, that guarantee it could not ship in the App Store and is liable to break at any moment. Recall that Firefox is the descendant of the first successful web-browser, without which there would be no world-wide-web. Without the WWW, arguably Apple would have a much smaller niche product, since the increasing importance of the Web made it possible for many people to move away from Windows. So Apple has no gratitude.

Oh, and the cherry on top is that Microsoft got into massive trouble for reserving special undocumented APIs for performance for use by its software, to unfairly prevent its competitors from providing as performant products. The fact that Apple replicated the IE and Windows situation with Safari and MacOS, after Microsoft was punished for the same behavior, demonstrates its incredible hubris. It's long past time for the Titan to be smitten down.
