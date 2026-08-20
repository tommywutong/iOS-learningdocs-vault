---
title: Code Speed Performance Guidelines
apple_id: 10000150i
resource_type: Guide
platform: macOS
topic: Performance
technology: null
published: '2014-03-10'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/CodeSpeed/Articles/TuningJavaCode.html
archived_at: '2026-07-18T01:47:09.222842Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Code Speed Performance Guidelines](Introduction%20to%20Code%20Speed%20Performance%20Guidelines.md)


[Next](Document%20Revision%20History.md)[Previous](Tuning%20for%20Specific%20Hardware.md)

# Tuning Your Java Code

If you are developing Java applications for OS X, there are several things you can do in your programs to reduce performance problems. The following sections list some of the basic things you can do in your code. For additional tips, see the performance documentation on the Sun website ([http://java.sun.com/docs/performance/](http://java.sun.com/docs/performance/)).

In large, threaded programs, synchronization is often unavoidable but can be a significant performance penalty if you are not careful. In earlier Java Virtual Machines (JVMs), synchronization used to be an extremely expensive operation. In most modern JVMs, including the HotSpot (TM) Java VM in OS X, only synchronized methods that lead to contention are expensive.

It is a good idea to measure your program's performance and while doing so try to identify any highly contended objects. Wherever you find such objects, consider redesigning or re-implementing your code to avoid that contention. If you manage your data structures carefully, either by restricting that data to a single thread or using `java.lang.ThreadLocal` to maintain per-thread data, you can avoid many contention issues and increase performance.

In earlier JVMs, object allocation was very expensive for a very simple reason. The garbage collection algorithms employed in these virtual machines operated conservatively by walking the entire heap to look for object references. Because all Java objects are allocated on the heap, each new allocation linearly increased the workload of the garbage collector.

The HotSpot (TM) Java VM in OS X now uses a generational garbage collection algorithm. This algorithm is fast. During each garbage collection pass, objects without references are cleaned up at no cost because they are simply never copied. Object allocation in the new JVM is also much faster because it uses an atomic pointer increment.

For your own programs, you should pick a garbage collection algorithm that works best with the allocation patterns your program uses. Information about tuning your program's garbage collection algorithm, as well as other performance-related Java information, is available on the Sun website at [http://java.sun.com/docs/performance/](http://java.sun.com/docs/performance/).

Exception handling in Java is very slow. Unnecessary exception handlers, in particular, make code slightly slower and much larger. Even in places where exception handlers are necessary, handling those exceptions is a very expensive operation.

As you write Java code, use exceptions only for truly exceptional cases. Do not use exceptions to indicate simple errors from which your code could otherwise recover. Instead, use them only to indicate abnormal conditions that your code does not know how to handle.

[Next](Document%20Revision%20History.md)[Previous](Tuning%20for%20Specific%20Hardware.md)

