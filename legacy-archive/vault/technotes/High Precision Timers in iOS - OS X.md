---
title: 'High Precision Timers in iOS / OS X '
apple_id: DTS40013172
resource_type: Technical Note
platform: iOS|macOS
topic: Performance
technology: null
published: '2013-03-05'
source_url: https://developer.apple.com/library/archive/technotes/tn2169/_index.html
archived_at: '2026-07-26T19:54:10.600234Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2169

# High Precision Timers in iOS / OS X

The note will cover the do's and dont's of using high precision timers on iOS and OS X.

[High Precision Timers in iOS / OS X](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgmjxgiwugsbrfvke4vcbi4ytambq)[Do I need a high precision timer?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgmjxgiwugsbrfvke4vcbi4zdambq)[A suggestion for synchronizing with display updates](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgmjxgiwugsbrfvke4vcbi4ztambq)[How do timers work?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgmjxgiwugsbrfvke4vcbi42dambq)[How do high precision timers work?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgmjxgiwugsbrfvke4vcbi42tambq)[How do I get put into the real time scheduling class?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgmjxgiwugsbrfvke4vcbi43dambq)[Which timing API(s) should I use?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgmjxgiwugsbrfvke4vcbi44dambq)[How accurate should high precision timers be?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgmjxgiwugsbrfvke4vcbi4ytambqga)[What are the do's and dont's of code running with high precision timers?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgmjxgiwugsbrfvke4vcbi4ytcmbqga)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgmjxgiwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## High Precision Timers in iOS / OS X

The note will cover the do's and dont's of using high precision timers on iOS and OS X.

[Back to Top](#)

## Do I need a high precision timer?

Don't use a high precision timer unless you really need it. They consume compute cycles and battery. There can only be a limited number of high precsion timers active at once. A high precision timer is "first in line", and not every timer can be first. When too many try, all the timers lose accuracy.

Example applications that are candidates for high precision timers are games that need to provide precise frame rates, or daemons that are streaming data to hardware with limited buffering, such as audio or video data.

[Back to Top](#)

## A suggestion for synchronizing with display updates

If you're writing code that needs to synchronize with frame buffer or display updates, Apple has already done much of the hard work for you. If you are developing for iOS, please see the CADisplayLink class, found in the QuartzCore.framework. If you are targeting OS X, see CVDisplayLink, also found in QuartzCore.framework.

[iOS: CADisplayLink Class Reference](https://developer.apple.com/library/ios/#documentation/QuartzCore/Reference/CADisplayLink_ClassRef/Reference/Reference.html#//apple_ref/doc/uid/TP40009031)

[OS X: CVDisplayLink Reference](https://developer.apple.com/library/mac/#documentation/QuartzCore/Reference/CVDisplayLinkRef/Reference/reference.html)

[Back to Top](#)

## How do timers work?

There are many API's in iOS and OS X that allow waiting for a specified period of time. They may be Objective C or C, and they take different kinds of arguments, but they all end up using the same code inside the kernel. Each timer api tells the kernel it needs to wait until a certain time, for example 10 seconds from now. The kernel keeps track of every thread, and when a timer request comes in, that thread is marked as "I'd like to run in 10 seconds".

The kernel tries to be as frugal as possible with cpu cycles, so if there is no other work to do, it will put the cpu's to sleep for 10 seconds, then wake up and run your thread.

Of course, that is an optimum situation, and in the real world, things never seem to work that easily! In a real situation, there are many threads that want to run, and many threads making timer requests, and the kernel has to manage them all. With thousands of threads and only a few cpu's, its easy to see how timers might be inaccurate.

[Back to Top](#)

## How do high precision timers work?

The only difference between a regular timer and a high precision timer is the scheduling class of the thread making the timer request. Threads that are in the real time scheduling class get first class treatment. They go to the front of the line whenever they need to run. If there is a conflict with multiple threads wanting to run in 10 seconds, a real time thread always goes first.

[Back to Top](#)

## How do I get put into the real time scheduling class?

__Listing 1__  The following code will move a pthread to the real time scheduling class

```c
#include <mach/mach.h>
#include <mach/mach_time.h>
#include <pthread.h>

void move_pthread_to_realtime_scheduling_class(pthread_t pthread)
{
    mach_timebase_info_data_t timebase_info;
    mach_timebase_info(&timebase_info);

    const uint64_t NANOS_PER_MSEC = 1000000ULL;
    double clock2abs = ((double)timebase_info.denom / (double)timebase_info.numer) * NANOS_PER_MSEC;

    thread_time_constraint_policy_data_t policy;
    policy.period      = 0;
    policy.computation = (uint32_t)(5 * clock2abs); // 5 ms of work
    policy.constraint  = (uint32_t)(10 * clock2abs);
    policy.preemptible = FALSE;

    int kr = thread_policy_set(pthread_mach_thread_np(pthread_self()),
                   THREAD_TIME_CONSTRAINT_POLICY,
                   (thread_policy_t)&policy,
                   THREAD_TIME_CONSTRAINT_POLICY_COUNT);
    if (kr != KERN_SUCCESS) {
        mach_error("thread_policy_set:", kr);
        exit(1);
    }
}
```

The period, computation, constraint, and preemptible fields do have an effect, and more can be learned about them at:

[Using the Mach Thread API to Influence Scheduling](https://developer.apple.com/library/mac/documentation/Darwin/Conceptual/KernelProgramming/scheduler/scheduler.html#//apple_ref/doc/uid/TP30000905-CH211-BABHGEFA)

[Back to Top](#)

## Which timing API(s) should I use?

As mentioned above, all the timer methods end up in the same place inside the kernel. However, some of them are more efficient than the others. At the time this note was written, mach_wait_until() is the api we would recommend using. It has the lowest overhead of all the timing API that we measured. However, if you have specific needs that aren't met by mach_wait_until(), for example you need to wait on a condvar, then feel free to use the appropriate timer API.

__Listing 2__  This example code demonstrates using mach_wait_until() to wait exactly 10 seconds.

```c
#include <mach/mach.h>
#include <mach/mach_time.h>

static const uint64_t NANOS_PER_USEC = 1000ULL;
static const uint64_t NANOS_PER_MILLISEC = 1000ULL * NANOS_PER_USEC;
static const uint64_t NANOS_PER_SEC = 1000ULL * NANOS_PER_MILLISEC;

static mach_timebase_info_data_t timebase_info;

static uint64_t abs_to_nanos(uint64_t abs) {
    return abs * timebase_info.numer  / timebase_info.denom;
}

static uint64_t nanos_to_abs(uint64_t nanos) {
    return nanos * timebase_info.denom / timebase_info.numer;
}

void example_mach_wait_until(int argc, const char * argv[])
{
    mach_timebase_info(&timebase_info);
    uint64_t time_to_wait = nanos_to_abs(10ULL * NANOS_PER_SEC);
    uint64_t now = mach_absolute_time();
    mach_wait_until(now + time_to_wait);
}
```

[Back to Top](#)

## How accurate should high precision timers be?

Timer accuracy depends on many factors, including the type of hardware being run on, the load on that hardware, and the power available (battery vs plugged in). However, if an otherwise unloaded machine or device is consistently missing your scheduled time by more than 500 microseconds, that should be considered an error, please file a bug with Apple. Often times we can do much better than that, but its best to measure for yourself.

Timers are not accurate across a sleep and wake cycle of the hardware.

[Back to Top](#)

## What are the do's and dont's of code running with high precision timers?

Do use as little cpu as possible during your timer loop. Remember that your thread now has special privileges, and when you're running, no one else can. Do try to stretch out your timer requests as much as you safely can. This allows the kernel to use less battery by sleeping more often and longer.

Don't spin loop! This burns cpu and battery at very high rates, and when newer faster hardware is released you'll burn cpu and battery even faster!

Don't create large numbers of real time threads. Real time scheduling isn't magic, it works by making your thread higher priority than other threads on the system. If everyone tries to crowd to the front of the line, all the real time threads will fail.

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2013-03-05 | New document that the note will cover the do's and dont's of using high precision timers on iOS and OS X. |

