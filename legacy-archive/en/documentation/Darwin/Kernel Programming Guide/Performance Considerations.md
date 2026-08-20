---
title: Kernel Programming Guide
apple_id: TP30000905
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2013-08-08'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/KernelProgramming/performance/performance.html
archived_at: '2026-07-15T07:23:13.769348Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Kernel Programming Guide](About%20This%20Document.md)


[Next](Kernel%20Programming%20Style.md)[Previous](Security%20Considerations.md)

# Performance Considerations

Performance is a key aspect of any software
system. Nowhere is this more true than in the kernel, where small
performance problems tend to be magnified by repeated execution. For
this reason, it is extremely important that your code be as efficient
as possible.

This chapter discusses the importance of low interrupt latency
and fine-grained locking and tells you how to determine what portions
of your code would benefit most from more efficient design.

In OS X, you will probably never need to write code that
runs in an interrupt context. In general, only motherboard hardware
requires this. However, in the unlikely event that you do need to
write code in an interrupt context, interrupt latency should be
a primary concern.

_Interrupt latency_ refers to the delay between an
interrupt being generated and an interrupt handler actually beginning
to service that interrupt. In practice, the worst case interrupt
latency is closely tied to the amount of time spent in _supervisor
mode_ (also
called kernel mode) with interrupts off while handling some other
interrupt. Low interrupt latency is necessary for reasonable overall
performance, particularly when working with audio and video. In
order to have reasonable soft real-time performance (for example, performance
of multimedia applications), the interrupt latency caused by every
device driver must be both small and bounded.

OS X takes great care to bound and minimize interrupt
latency for built-in drivers. It does this primarily through the
use of _interrupt service threads_ (also known as I/O service threads).

When OS X takes an interrupt, the low-level trap handlers
call up to a generic interrupt handling routine that clears the
pending interrupt bit in the interrupt controller and calls a device-specific
interrupt handler.
That device-specific handler, in turn, sends a message to an interrupt
service thread to notify it that an interrupt has occurred, and
then the handler returns. When no further interrupts are pending,
control returns to the currently executing thread.

The next time the interrupt service thread is scheduled, it
checks to see if an interrupt has occurred, then services the interrupt.
As the name suggests, this actually is happening in a thread context,
not an interrupt context. This design causes two major differences
from traditional operating system design:

- Interrupt
  latency is near zero, since the code executing in an interrupt context
  is very small.
- It is possible for an interrupt to occur while a device driver
  is executing. This means that traditional (threaded) device drivers
  can be preempted and must use locking or other similar methods to
  protect any shared data (although they need to do so anyway to work
  on computers with multiple processors).

This model is crucial to the performance of OS X. You
should not attempt to circumvent this design by doing large amounts
of work in an interrupt context. Doing so will be detrimental to
the overall performance of the system.

It is difficult to communicate data between multiple threads
or between thread and interrupt contexts without using locking or
other synchronization. This locking protects your data from getting
clobbered by another thread. However, it also has the unfortunate side
effect of being a potential bottleneck.

In some types of communication (particularly n-way), locking
can dramatically hinder performance by allowing only one thing to
happen at a time. Read-write locks, discussed in [Synchronization Primitives](Synchronization%20Primitives.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrrhawuerkijjcemq2b),
can help alleviate this problem in the most common situation where
multiple clients need to be able to read information but only rarely
need to modify that data.

However, there are many cases where read-write locks are
not helpful. This section discusses some possible problems and ways
of improving performance within those constraints.

When many threads need to obtain a lock (or a small number
of threads need to obtain a lock frequently), this lock is considered
highly contended. Highly contended locks frequently represent faulty
code design, but they are sometimes unavoidable. In those cases,
the lock tends to become a major performance bottleneck.

Take, for example, the issue of many-to-many communication
that must be synchronized through a common buffer. While some improvement
can be gained by using read-write locks instead of an ordinary mutex,
the issue of multiple writers means that read-write locks still
perform badly.

One possible solution for this many-to-many communication
problem is to break the lock up into multiple locks. Instead of
sharing a single buffer for the communication itself, make a shared
buffer that contains accounting information for the communication
(for example, a list of buffers available for reading). Then assign
each individual buffer its own lock. The readers might then need
to check several locations to find the right data, but this still
frequently yields better performance, since writers must only contend
for a write lock while modifying the accounting information.

Another solution for many-to-many communications is to eliminate
the buffer entirely and communicate using message passing, sockets,
IPC, RPC, or other methods.

Yet another solution is to restructure your code in a way
that the locking is unnecessary. This is often much more difficult.
One method that is often helpful is to take advantage of flags and
atomic increments, as outlined in the next paragraph. For simplicity,
a single-writer, single-reader example is presented, but it is possible
to extend this idea to more complicated designs.

Take a buffer with some number of slots. Keep a read index
and a write index into that buffer. When the write index and read
index are the same, there is no data in the buffer. When writing,
clear the next location. Then do an atomic increment on the pointer.
Write the data. End by setting a flag at that new location that
says that the data is valid.

Note that this solution becomes much more difficult when dealing
with multiple readers and multiple writers, and as such, is beyond
the scope of this section.

One of the fundamental properties of locks is granularity. The granularity
of a lock refers to the amount of code or data that it protects.
A lock that protects a large block of code or a large amount of
data is referred to as a coarse-grained lock, while a lock that
protects only a small amount of code or data is referred to as a
fine-grained lock.
A coarse-grained lock is much more likely to be
contended (needed by one thread while being held by another) than
a more finely grained lock.

There are two basic ways of decreasing granularity. The first
is to minimize the amount of code executed while a lock is held.
For example, if you have code that calculates a value and stores
it into a table, don’t take the lock before calling the function
and release it after the function returns. Instead, take the lock
in that piece of code right before you write the data, and release
it as soon as you no longer need it.

Of course, reducing the amount of protected code is not always
possible or practical if the code needs to guarantee consistency
where the value it is writing depends on other values in the table,
since those values could change before you obtain the lock, requiring
you to go back and redo the work.

It is also possible to reduce granularity by locking the data
in smaller units. In the above example, you could have a lock on
each cell of the table. When updating cells in the table, you would
start by determining the cells on which the destination cell depends,
then lock those cells and the destination cell in some fixed order.
(To avoid deadlock, you must always either lock cells in the same
order or use an appropriate `try` function
and release all locks on failure.)

Once you have locked all the cells involved, you can then
perform your calculation and release the locks, confident that no
other thread has corrupted your calculations. However, by locking
on a smaller unit of data, you have also reduced the likelihood
of two threads needing to access the same cell.

A slightly more radical version of this is to use read-write
locks on a per-cell basis and always upgrade in a particular order.
This is, however, rather extreme, and difficult to do correctly.

Code profiling means determining how often certain
pieces of code are executed. By knowing how frequently a piece of
code is used, you can more accurately gauge the importance of optimizing
that piece of code. There are a number of good tools for profiling user
space applications. However, code profiling in the kernel is a very
different beast, since it isn’t reasonable to attach to it like
you would a running process. (It is possible by using a second computer,
but even then, it is not a trivial task.)

This section describes two useful ways of profiling your kernel
code: counters and lock profiling. Any changes you make to allow
code profiling should be done only during development. These are
not the sort of changes that you want to release to end users.

The first method of code profiling is with counters. To profile
a section of code with a counter, you must first create a global
variable whose name describes that piece of code and initialize
it to zero. You then add something like

```
#ifdef PROFILING
            foo_counter++; #endif
```

in the appropriate piece of code. If you then define `PROFILING`,
that counter is created and initialized to zero, then incremented
each time the code in question is executed.

One small snag with this sort of profiling is the problem
of obtaining the data. This can be done in several ways. The simplest
is probably to install a `sysctl`,
using the address of `foo_counter` as
an argument. Then, you could simply issue the `sysctl` command
from the command line and read or clear the variable. Adding a `sysctl` is
described in more detail in [BSD sysctl API](Boundary%20Crossings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrrg4wueqkcjjfeesch).

In addition to using `sysctl`,
you could also obtain the data by printing its value when unloading
the module (in the case of a KEXT) or by using a remote debugger
to attach to the kernel and directly inspecting the variable. However,
a `sysctl` provides the
most flexibility. With a `sysctl`,
you can sample the value at any time, not just when the module is
unloaded. The ability to arbitrarily sample the value makes it easier
to determine the importance of a piece of code to one particular
action.

If you are developing code for use in the I/O Kit, you should
probably use your driver’s `setProperties` call
instead of a [sysctl](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/sysctl.3.html#//apple_ref/doc/man/3/sysctl).

Lock profiling is another useful
way to find the cause of code inefficiency. Lock profiling can give
you the following information:

- how many
  times a lock was taken
- how long the lock was held on average
- how often the lock was unavailable

Put another way, this allows you to determine the contention
of a lock, and in so doing, can help you to minimize contention
by code restructuring.

There are many different ways to do lock profiling. The most
common way is to create your own lock calls that increment a counter
and then call the real locking functions. When you move from debugging
into a testing cycle before release, you can then replace the functions
with defines to cause the actual functions to be called directly.
For example, you might write something like this:

```swift
extern struct timeval time;

boolean_t   mymutex_try(mymutex_t *lock) {
    int ret;
    ret=mutex_try(lock->mutex);
    if (ret) {
        lock->tryfailcount++;
    }
    return ret;
}

void    mymutex_lock(mymutex_t *lock) {
    if (!(mymutex_try(lock))) {
        mutex_lock(lock->mutex);
    }
    lock->starttime = time.tv_sec;
}
void    mymutex_unlock(mymutex_t *lock) {
    lock->lockheldtime += (time.tv_sec - lock->starttime);
    lock->heldcount++;
    mutex_unlock(lock->mutex);
}
```

This routine has accuracy only to the nearest second, which
is not particularly accurate. Ideally, you want to keep track of
both `time.tv_sec` and `time.tv_usec` and
roll the microseconds into seconds as the number gets large.

From this information, you can obtain the average time the
lock was held by dividing the total time held by the number of times
it was held. It also tells you the number of times a lock was taken
immediately instead of waiting, which is a valuable piece of data
when analyzing contention.

As with counter-based profiling, after you have written code
to record lock use and contention, you must find a way to obtain
that information. A `sysctl` is
a good way of doing this, since it is relatively easy to implement
and can provide a “snapshot” view of the data structure at any
point in time. For more information on adding a `sysctl`,
see [BSD sysctl API](Boundary%20Crossings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrrg4wueqkcjjfeesch).

Another way to do lock profiling is to use the built-in ETAP
(Event Trace Analysis Package). This package consists of additional
code designed for lock profiling. However, since this requires a
kernel recompile, it is generally not recommended.

[Next](Kernel%20Programming%20Style.md)[Previous](Security%20Considerations.md)

