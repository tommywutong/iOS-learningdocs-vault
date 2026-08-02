---
title: Kernel Programming Guide
apple_id: TP30000905
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2013-08-08'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/KernelProgramming/services/services.html
archived_at: '2026-07-15T07:23:14.173708Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Kernel Programming Guide](About%20This%20Document.md)


[Next](Kernel%20Extension%20Overview.md)[Previous](Synchronization%20Primitives.md)

# Miscellaneous Kernel Services

This chapter contains information about miscellaneous services provided by the OS X kernel. For most projects, you will probably never need to use most of these services, but if you do, you will find it hard to do without them.

This chapter contains these sections: [Using Kernel Time Abstractions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrrhewugscejjbemrkg), [Boot Option Handling](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrrhewugsceincueqsk), [Queues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrrhewugscejjeeorkg), and [Installing Shutdown Hooks](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrrhewugscejfcesrcg).

There are two basic groups of time abstractions in the kernel. One group includes functions that provide delays and timed wake-ups. The other group includes functions and variables that provide the current wall clock time, the time used by a given process, and other similar information. This section describes both aspects of time from the perspective of the kernel.

There are a number of ways to get basic time information from within the kernel. The officially approved methods are those that Mach exports in `kern/clock.h`. These include the following:

```
void clock_get_uptime(uint64_t *result);

void clock_get_system_microtime(            uint32_t *secs,
                                            uint32_t *microsecs);

void clock_get_system_nanotime(             uint32_t *secs,
                                            uint32_t *nanosecs);
void clock_get_calendar_microtime(          uint32_t *secs,
                                            uint32_t *microsecs);

void clock_get_calendar_nanotime(           uint32_t *secs,
                                            uint32_t *nanosecs);
```

The function `clock_get_uptime` returns a value in `AbsoluteTime` units. For more information on using `AbsoluteTime`, see [Using Mach Absolute Time Functions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrrhewugscei5dekrsf).

The functions `clock_get_system_microtime` and `clock_get_system_nanotime` return 32-bit integers containing seconds and microseconds or nanoseconds, respectively, representing the system uptime.

The functions `clock_get_calendar_microtime` and `clock_get_calendar_nanotime` return 32-bit integers containing seconds and microseconds or nanoseconds, respectively, representing the current calendar date and time since the epoch (January 1, 1970).

In some parts of the kernel, you may find other functions that return type `mach_timespec_t`. This type is similar to the traditional BSD `struct timespec`, except that fractions of a second are measured in nanoseconds instead of microseconds:

```
struct mach_timespec {
    unsigned int tv_sec;
    clock_res_t tv_nsec;
};
typedef struct mach_timespec *mach_timespec_t;
```

In addition to the traditional Mach functions, if you are writing code in BSD portions of the kernel you can also get the current calendar (wall clock) time as a BSD `timeval`, as well as find out the calendar time when the system was booted by doing the following:

```c
#include <sys/kernel.h>
struct timeval tv=time; /* calendar time */
struct timeval tv_boot=boottime; /* calendar time when booting occurred  */
```

For other information, you should use the Mach functions listed previously.

Each part of the OS X kernel has a distinct API for waiting a certain period of time. In most cases, you can call these functions from other parts of the kernel. The I/O Kit provides `IODelay` and `IOSleep`. Mach provides functions based on `AbsoluteTime`, as well as a few based on microseconds. BSD provides `msleep`.

`IODelay`, provided by the I/O Kit, abstracts a timed spin. If you are delaying for a short period of time, and if you need to be guaranteed that your wait will not be stopped prematurely by delivery of asynchronous events, this is probably the best choice. If you need to delay for several seconds, however, this is a bad choice, because the CPU that executes the wait will spin until the time has elapsed, unable to handle any other processing.

`IOSleep` puts the currently executing thread to sleep for a certain period of time. There is no guarantee that your thread will execute after that period of time, nor is there a guarantee that your thread will not be awakened by some other event before the time has expired. It is roughly equivalent to the `sleep` call from user space in this regard.

The use of `IODelay` and `IOSleep` are straightforward. Their prototypes are:

```
IODelay(unsigned microseconds);
IOSleep(unsigned milliseconds);
```

Note the differing units. It is not practical to put a thread to sleep for periods measured in microseconds, and spinning for several milliseconds is also inappropriate.

The following Mach time functions are commonly used. Several others are described in `osfmk/kern/clock.h`.

```
void delay(uint64_t microseconds);
void clock_delay_until(uint64_t deadline);
void clock_absolutetime_interval_to_deadline(uint64_t abstime,
            uint64_t *result);
void nanoseconds_to_absolutetime(uint64_t nanoseconds, uint64_t  *result);
void absolutetime_to_nanoseconds(uint64_t abstime, uint64_t *result);
```

These functions are generally straightforward. However, a few points deserve explanation. Unless specifically stated, all times, deadlines, and so on, are measured in `abstime` units. The `abstime` unit is equal to the length of one bus cycle, so the duration is dependent on the bus speed of the computer. For this reason, Mach provides conversion routines between `abstime` units and nanoseconds.

Many time functions, however, provide time in seconds with nanosecond remainder. In this case, some conversion is necessary. For example, to obtain the current time as a mach abstime value, you might do the following:

```
uint32_t secpart;
uint32_t nsecpart;
uint64_t nsec, abstime;

clock_get_calendar_nanotime(&secpart, &nsecpart);
nsec = nsecpart + (1000000000ULL * secpart); //convert seconds to  nanoseconds.
nanoseconds_to_absolutetime(nsec, &abstime);
```

The abstime value is now stored in the variable `abstime`.

In addition to Mach and I/O Kit routines, BSD provides `msleep`, which is the recommended way to delay in the BSD portions of the kernel. In other parts of the kernel, you should either use `wait_queue` functions or use `assert_wait` and `thread_wakeup` functions, both of which are closely tied to the Mach scheduler, and are described in [Kernel Thread APIs](Mach%20Scheduling%20and%20Thread%20Interfaces.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrrgewueqkcijcukqsj). Because this function is more commonly used for waiting on events, it is described further in [Condition Variables](Synchronization%20Primitives.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrrhawviucykjcummjqhe).

Many time-related functions such as `clock_get_uptime` changed as a result of the transition to KPIs in OS X v.10.4. While these changes result in a cleaner interface, this can prove challenging if you need to make a kernel extension that needs to obtain time information across multiple versions of OS X in a kernel extension that would otherwise have no version dependencies (such as an I/O Kit KEXT).

Here is a list of time-related functions that are available in both pre-KPI and KPI versions of OS X:

**`uint64_t mach_absolute_time(void);`**
: __Declared In:__  `<mach/mach_time.h>`

__Dependency:__  `com.apple.kernel.mach`

This function returns a Mach absolute time value for the current wall clock time in units of `uint64_t`.

**`void microtime(struct timeval *tv);`**
: __Declared In:__  `<sys/time.h>`

__Dependency:__  `com.apple.kernel.bsd`

This function returns a timeval struct containing the current wall clock time.

**`void microuptime(struct timeval *tv);`**
: __Declared In:__  `<sys/time.h>`

__Dependency:__  `com.apple.kernel.bsd`

This function returns a timeval struct containing the current uptime.

**`void nanotime(struct timespec *ts);`**
: __Declared In:__  `<sys/time.h>`

__Dependency:__  `com.apple.kernel.bsd`

This function returns a timespec struct containing the current wall clock time.

**`void nanouptime(struct timespec *ts);`**
: __Declared In:__  `<sys/time.h>`

__Dependency:__  `com.apple.kernel.bsd`

This function returns a timespec struct containing the current uptime.

In addition to these APIs, the functionality marked `__APPLE_API_UNSTABLE` in `<mach/time_value.h>` was adopted as-is in OS X v.10.4 and is no longer marked unstable.

OS X provides a simple parse routine, `PE_parse_boot_arg`, for basic boot argument passing. It supports both flags and numerical value assignment. For obtaining values, you write code similar to the following:

```
unsigned int argval;

if (PE_parse_boot_arg("argflag", &argval)) {
    /* check for reasonable value */
    if (argval < 10 || argval > 37)
        argval = 37;
} else {
    /* use default value */
    argval = 37;
}
```

Since `PE_parse_boot_arg` returns a nonzero value if the flag exists, you can check for the presence of a flag by using a flag that starts with a dash (-) and ignoring the value stored in `argvalue`.

The `PE_parse_boot_arg` function can also be used to get a string argument. To do this, you must pass in the address of an array of type `char` as the second argument. The behavior of `PE_parse_boot_arg` is undefined if a string is passed in for a numeric variable or vice versa. Its behavior is also undefined if a string exceeds the storage space allocated. Be sure to allow enough space for the largest reasonable string including a null delimiter. No attempt is made at bounds checking, since an overflow is generally a fatal error and should reasonably prevent booting.

As part of its BSD infrastructure, the OS X kernel provides a number of basic support macros to simplify handling of linked lists and queues. These are implemented as C macros, and assume a standard C `struct`. As such, they are probably not suited for writing code in C++.

The basic types of lists and queues included are

- `SLIST`, a singly linked list
- `STAILQ`, a singly linked tail queue
- `LIST`, a doubly linked list
- `TAILQ`, a doubly linked tail queue

`SLIST` is ideal for creating stacks or for handling large sets of data with few or no removals. Arbitrary removal, however, requires an `O(n)` traversal of the list.

`STAILQ` is similar to `SLIST` except that it maintains pointers to both ends of the queue. This makes it ideal for simple FIFO queues by adding entries at the tail and fetching entries from the head. Like `SLIST`, it is inefficient to remove arbitrary elements.

`LIST` is a doubly linked version of `SLIST`. The extra pointers require additional space, but allow `O(1)` (constant time) removal of arbitrary elements and bidirectional traversal.

`TAILQ` is a doubly linked version of `STAILQ`. Like `LIST`, the extra pointers require additional space, but allow `O(1)` (constant time) removal of arbitrary elements and bidirectional traversal.

Because their functionality is relatively simple, their use is equally straightforward. These macros can be found in `xnu/bsd/sys/queue.h`.

Although OS X does not have traditional BSD-style shutdown hooks, the I/O Kit provides equivalent functionality in recent versions. Since the I/O Kit provides this functionality, you must call it from C++ code.

To register for notification, you call `registerSleepWakeInterest` (described in `IOKit/RootDomain.h`) and register for sleep notification. If the system is about to be shut down, your handler is called with the message type `kIOMessageSystemWillPowerOff`. If the system is about to reboot, your handler gets the message type `kIOMessageSystemWillRestart`. If the system is about to reboot, your handler gets the message type `kIOMessageSystemWillSleep`.

If you no longer need to receive notification (for example, if your KEXT gets unloaded), be certain to release the notifier with `IONofitier::release` to avoid a kernel panic on shutdown.

For example, the following sample KEXT registers for sleep notifications, then logs a message with IOLog when a sleep notification occurs:

```c
#include <IOKit/IOLib.h>
#include <IOKit/pwr_mgt/RootDomain.h>
#include <IOKit/pwr_mgt/IOPM.h>
#include <IOKit/IOService.h>
#include <IOKit/IONotifier.h>

#define ALLOW_SLEEP 1

IONotifier *notifier;

extern "C" {

IOReturn mySleepHandler( void * target, void * refCon,
    UInt32 messageType, IOService * provider,
    void * messageArgument, vm_size_t argSize )
{
    IOLog("Got sleep/wake notice.  Message type was %d\n", messageType);
#if ALLOW_SLEEP
    acknowledgeSleepWakeNotification(refCon);
#else
    vetoSleepWakeNotification(refCon);
#endif
    return 0;
}

kern_return_t sleepkext_start (kmod_info_t * ki, void * d) {
        void *myself = NULL; // Would pass the self pointer here if in a class instance

        notifier = registerPrioritySleepWakeInterest(
                &mySleepHandler, myself, NULL);
    return KERN_SUCCESS;
}


kern_return_t sleepkext_stop (kmod_info_t * ki, void * d) {
    notifier->remove();
    return KERN_SUCCESS;
}

} // extern "C"
```

[Next](Kernel%20Extension%20Overview.md)[Previous](Synchronization%20Primitives.md)

