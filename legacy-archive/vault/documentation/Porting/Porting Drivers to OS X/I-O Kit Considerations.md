---
title: Porting Drivers to OS X
apple_id: TP30001169
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2009-05-06'
source_url: https://developer.apple.com/library/archive/documentation/Porting/Conceptual/PortingDrivers/other-iokit/other-iokit.html
archived_at: '2026-07-18T01:50:43.107238Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Porting Drivers to OS X](Introduction%20to%20Porting%20Drivers%20to%20OS%20X.md)


[Next](C%2B%2B%20Language%20Considerations.md)[Previous](Driver%20Porting%20Basics.md)

# I/O Kit Considerations

The I/O Kit is a powerful and relatively straightforward driver environment. However, as with most things that are powerful, there are a few things that won’t behave the way you might expect, particularly if you are used to writing drivers for other platforms.

This chapter describes some of the things you should consider when porting a driver from another operating system, including ways to avoid potential kernel panics, driver loading failures, and so on down the road

Some UNIX driver models provide additional support for logging, such as the use of multiple levels of verbosity. The I/O Kit does not provide such support, relying on the developer to implement such a scheme if it is desired.

A convenient way to simulate this is to replace calls to `printf` with calls to the a macro like this one:

```
#define dIOLog(level, a, b...) {if (org_mklinux_iokit_swim3_debug & \
    level) IOLog(a, ## b); }
```

and then define various level macros as powers of two. This provides even greater control over debugging than a level-based scheme, allowing you to have up to 32 distinct log options (or 64 if you declare the debug variable as a 64-bit type) that can be turned on or off individually by changing the value of a global variable (in this case, called `org_mklinux_iokit_swim3_debug`).

Note that if you are going to use this sort of debugging in a C driver core, you must either use a global variable, pass the variable’s value as an argument, or pass a pointer to the variable as an argument, since the C code cannot access class variables directly.

In many parts of the I/O Kit, the template class includes both synchronous and asynchronous methods. In these cases, it is absolutely necessary to implement both asynchronous and synchronous calls. Asynchronous calls usually include a callback for a completion routine. If you call the `complete` method on this completion routine from the same thread that called your function, you may get random kernel panics or stack corruption.

The problem is that most traditional driver architectures are not designed with asynchronous I/O in mind. There are a number of ways to retrofit asynchronous support into a driver. Each has its own difficulties.

The most obvious solution is to spawn a temporary helper thread to perform the operation. However, this runs into problems with concurrency. Specifically, the helper thread needs to be able to obtain data from the main thread, which means that the buffer must be in a shared location (for example as part of the class instance). However, some other thread could be in the same code at the same time, resulting in corruption of the request.

The obvious (but wrong) fix for this is to use a lock. Mach locks, however, do not like it when you lock them in one thread and release them in another. Instead, you should use an `IOCommandGate`.

In your class declaration, you should include a place to store the command gate:

```
IOCommandGate *myGate;
```

In your start routine, you must initialize the command gate. To do this, you might add code that looks like this:

```
myGate = new IOCommandGate();
```

You need a wrapper function to pass arguments to the doSyncReadWrite function. It might look like this:

```swift

struct asyncAction {
    IOMemoryDescriptor *buffer;
    UInt32 block;
    UInt32 nblks;
};

extern “C” static void org_mklinux_iokit_swim3_driver_doAsyncWrapper(
        void *selfref,
        void *actref,
        void *completionptr,
        void *)
{
    int retval;
    org_mklinux_iokit_swim3_driver *driver = selfref;

    retval = driver->doSyncReadWrite(myaction->buffer,
        myaction->block,
        myaction->nblks);

    IOStorage::complete(completion, retval, (retval ? 0 :
        (args.nblks * 512)));

}
```

In `doAsyncReadWrite`, you would do something like:

```swift
org_mklinux_iokit_swim3_driver::doAsyncReadWrite(IOMemoryDescriptor *buffer,
                                UInt32 block,UInt32 nblks,
                                IOStorageCompletion completion)
{

    struct asyncAction myaction;

    myaction.buffer = buffer;
    myaction.block = block;
    myaction.nblks = nblks;

    return (myGate->runAction(
        (Action)&org_mklinux_iokit_swim3_driver_doAsyncWrapper
        (void *)self,
        (void *)&myaction,
        (void *)&completion,
        NULL));

}
```


Many traditional BSD-style drivers use the functions `sleep`, `timeout`, and `untimeout` as synchronization primitives akin to condition variables. You might have a block of code that looks something like this:

```
timeout((timeout_fcn_t) wakeup, event, (2 * timeOut * HZ + 999) / 1000);
sleep((char *)event, PZERO);
```

where `event` is a pointer to an integer where the result of the wait will be stored, `wakeup` is a (bogus) function pointer called when the event occurs, the timeout is usually measured in some fraction of a second, and `PZERO` is the priority level of the current operation. This ensures that lower-priority interrupts do not wake this code prior to timeout. In such a system, interrupts are lower than PZERO, so they could still result in a wakeup.

Such code would also typically contain something like the following:

```
untimeout((timeout_fcn_t) wakeup, (void *) event);
```

in a different part of the code (generally in an interrupt handler). This part of the code wakes up the part of the code that is waiting for an event.

OS X uses similar constructs in the BSD part of the kernel. However, these are not exposed to the I/O Kit. Instead, you need to use an alternative mechanism.

If you are not using timeouts, you could simply use an `IOCommandGate` instance. However, this is rarely the case in code ported from BSD.

There are two recommended solutions to this: `IOLock` locks and an `IOTimerEventSource`/`IOCommandGate` combination

**`IOLock` locks**
: This is the easiest way to replace the `timeout`/`sleep`/`untimeout` combination. Instead of setting the timeout and sleeping, you calculate the time stamp when you want to wake, take a lock, and sleep on the lock.

**`IOCommandGate` with an `IOTimerEventSource`**
: If you are rearchitecting your code, this provides some additional flexibility at the cost of complexity. This will be described in a forthcoming code example.

This code sample assumes that the use of priority is strictly to prevent stray wakeups. If your code is doing something more sophisticated with priority levels, you will have to substantially enhance this code.

This code also assumes that there is only one request in flight at any given time, and one thread doing a sleep wait at any given time. Otherwise, you will need to add some sort of queue in place of simply having a single variable to hold the return status of the wait.

With those caveats, an alternative to sleep and wakeup follows:

__Listing 2-1__  Use of IOLock for sleep/timeout/untimeout

```c
#include <kern/kern_types.h>    /* for THREAD_UNINT */
#include <IOKit/IOLocks.h>      /* for IOLock */
#include <osfmk/kern/clock.h>   /* for time manipulation functions */

/* instance-specific driver state structure */
struct driverstate_t {
    IOLock *lock;
    int wait_return;
    .
    .
    .
}

/* This function waits */
dosomething( ... , driverstate_t mydriverstate)
{
    IOLock *lock = mydriverstate->unitlock;
    int nanoseconds_to_delay = 1000000; # 1 msec for an example
    AbsoluteTime absinterval, deadline;
    .
    .
    .
    // timeout((timeout_fcn_t) wakeup, event, (2*timeOut * HZ + 999) / 1000);
    // sleep((char *)event, PZERO);

    IOLockLock(lock);
    nanoseconds_to_absolutetime(nanoseconds_to_delay, (uint64_t *)&absinterval);
    clock_absolutetime_interval_to_deadline(absinterval, (uint64_t *)&deadline);
    IOLockSleepDeadline(lock, event, deadline, THREAD_UNINT);
    wakeup = mydriverstate->wait_return;
    IOLockUnlock(lock);
}



/* This function wakes up the waiting thread */
interrupt_handler( ... , driverstate_t mydriverstate)
{

    // untimeout((timeout_fcn_t) wakeup, (void *) event);
    IOLockLock(lock);
    mydriverstate->wait_return =

    IOLockUnlock(lock);

}
```


There are two major fundamental namespace problems with porting drivers from UNIX to OS X: sharing between drivers and sharing between driver instances.

Namespace pollution is a problem for any driver developer that is using C code. The problem is that your function namespace is potentially shared with other drivers. If you name a C function or global variable with the same name as that of a function or global variable in someone else’s driver, one of the two drivers will fail to load.

Namespace pollution also is a problem for drivers that depend on global variables if it is possible for more than one instance of the driver to be loaded at a time. Because C global variables are shared across driver instances, the two instances will end up clobbering each other’s data. (Since the driver is already loaded, there will be no linking problems, unlike the case where two different drivers have variables or functions with the same name.)

This section describes solutions to both of these problems in detail.

The biggest problem with using a C core for an I/O Kit driver is the issue of a shared namespace. While this won’t prevent multiple instances from being instantiated, it will mean that they will share any global variables across those multiple instances. For this reason, special care is needed when working with global variables.

Most UNIX-based driver architectures solve this by providing some sort of unit argument to their core functions. As a quick fix, the addition of a “used” flag in the data structure can be used to allow the C++ core to provide this same functionality, with some fixed limit to the number of concurrent instances. This is not an ideal long-term solution, however, and should only be used during early development.

To do this, however, multiple driver instances must cooperate. This requires a shared lock between them. Sharing the lock is easy. Initializing the lock without race conditions, however, requires a little more effort, specifically a static initializer. An example of this methodology is show in [Listing 2-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrzfvbuqmrqgywueqkcivduqsse).

__Listing 2-2__  Use of instance table for global variables

```swift
/**** in the header ****/

/* Added “used” since there are no fixed interface numbers */
struct scsipi {
    int used = 0;
    .
    .
    .
};
struct scsipi interface[NSCSI];

kern_return_t read(int unit, ...)
{
.
.
.
}


class org_mklinux_driver_IOLockClass : public OSObject
{
    org_mklinux_driver_IOLockClass();
    ~org_mklinux_driver_IOLockClass();

    public:
        IOLock *lock;
};

/**** in the C++ wrapper ****/
extern “C” {
    IOLock *org_mklinux_driver_swim3_lock = NULL;
    int org_mklinux_driver_swim3_lock_refcount = 0;
    extern scsipi *interface;
}

/*  declare a statically-initialized instance of the class so that
    its constructor will be called on driver load and its destructor
    will be called on unload. */
class org_mklinux_driver_IOLockClass org_mklinux_driver_swim3_lock;

class org_mklinux_driver_IOLockClass : public OSObject
{
    org_mklinux_driver_IOLockClass()
    {
        lock = IOLockAlloc();
    }
    ~org_mklinux_driver_IOLockClass();
    {
        IOLockFree(lock);
    }

    public:
        IOLock *lock;
};

int org_mklinux_driver_swim3::new_unit() {
    int i;
    IOLockLock(org_mklinux_driver_swim3_lock->lock);
        for (i=0; i<NSCSI; i++) {
            if (!interface[i]->used) {
                interface[i]->used = 1;
                IOLockUnlock(org_mklinux_driver_swim3_lock->lock);
                return i;
            }
        }
    IOLockUnlock(org_mklinux_driver_swim3_lock->lock);
    return -1;
}

void org_mklinux_driver_swim3::free_unit(int unit) {
    IOLockLock(org_mklinux_driver_swim3_lock->lock);
    interface[unit]->used = 0;
    IOLockUnlock(org_mklinux_driver_swim3_lock->lock);
}

org_mklinux_driver_swim3::init(){
    .
    .
    .
    /* unit should be an instance variable in your c++ wrapper class */
    unit = new_unit()
    if (unit == -1) {
        /* Maybe print a warning here */
        return false;
    }
}

org_mklinux_driver_swim3::free(){
    unit_free(unit)
}
```

A better long-term solution, however, is to declare the data structure as a member of the C++ wrapper class, then rewrite the functions to pass a pointer instead of an integer argument, and use pointer dereferencing (`mystructptr->field`) instead of structure dereferencing (`mystruct.field`).

To avoid confusion, you should always name your functions in ways that prevent namespace pollution. It is not always practical to name functions with names like `org_mklinux_iokit_swim3_foo`, though, as this quickly becomes unreadable. Instead, a more sane solution is to use macros to rename the functions at compile time.

For example, say you have functions called `bingo`, `nameo`, and `dog`. You want to rename then with the prefix `farmer_had_a_`. You might include macros in a project-wide header file that look like this:

```
#define dog(a, b, c) farmer_had_a_dog(a, b, c)
#define bingo(a, b, c) farmer_had_a_bingo(a, b, c)
#define nameo(a, b, c) farmer_had_a_nameo(a, b, c)
```

Now there is some risk that you will forget to include these defines for a function. There is a simple fix for that problem, though. First, instead of just including the macros, intersperse the prototypes for the functions in the same file. For example:

```
void farmer_had_a_dog(int and, int bingo, void *was_his, char *nameo);
#define dog(a, b, c) farmer_had_a_dog(a, b, c)

void farmer_had_a_bingo(int clap_i_n_g_o);
#define bingo(a, b, c) farmer_had_a_bingo(a, b, c)

void farmer_had_a_nameo(int dog);
#define nameo(a, b, c) farmer_had_a_nameo(a, b, c)
```

Now this is only a partial solution. To make it a complete solution, add the compiler flag `-Wmissing-prototypes` to the `gcc` compiler options (`CFLAGS`) in your driver’s `Makefile` or in its Project Builder plist. If you see notices of missing prototypes, you’ll know that you forgot one (or more).

For more information about namespace pollution, see _[Kernel Programming Guide](../../Darwin/Kernel%20Programming%20Guide/About%20This%20Document.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbv)_ in Apple’s Developer Documentation.

[Next](C%2B%2B%20Language%20Considerations.md)[Previous](Driver%20Porting%20Basics.md)

