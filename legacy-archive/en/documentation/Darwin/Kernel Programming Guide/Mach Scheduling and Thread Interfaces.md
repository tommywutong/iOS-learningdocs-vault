---
title: Kernel Programming Guide
apple_id: TP30000905
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2013-08-08'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/KernelProgramming/scheduler/scheduler.html
archived_at: '2026-07-15T07:23:13.777471Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Kernel Programming Guide](About%20This%20Document.md)


[Next](Bootstrap%20Contexts.md)[Previous](Memory%20and%20Virtual%20Memory.md)

# Mach Scheduling and Thread Interfaces

OS X is based on Mach and BSD. Like Mach and most BSD UNIX systems, it contains an advanced scheduler based on the CMU Mach 3 scheduler. This chapter describes the scheduler from the perspective of both a kernel programmer and an application developer attempting to set scheduling parameters.

This chapter begins with the [Overview of Scheduling](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrrgewueqkcizduiscb), which describes the basic concepts behind Mach scheduling at a high level, including real-time priority support.

The second section, [Using Mach Scheduling From User Applications](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrrgewueqkcineekrkc), describes how to access certain key Mach scheduler routines from user applications and from other parts of the kernel outside the scheduler.

The third section, [Kernel Thread APIs](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrrgewueqkcijcukqsj), explains scheduler-related topics including how to create and terminate kernel threads and describes the BSD `spl` macros and their limited usefulness in OS X.

The OS X scheduler is derived from the scheduler used in OSFMK 7.3. In general, much documentation about prior implementations applies to the scheduler in OS X, although you will find numerous differences. The details of those differences are beyond the scope of this overview.

Mach scheduling is based on a system of run queues at various priorities that are handled in different ways. The priority levels are divided into four bands according to their characteristics, as described in [Table 10-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrrgewviucykjcummjrgq).

__Table 10-1__  Thread priority bands

| Priority Band | Characteristics |
| Normal | normal application thread priorities |
| System high priority | threads whose priority has been raised above normal threads |
| Kernel mode only | reserved for threads created inside the kernel that need to run at a higher priority than all user space threads (I/O Kit workloops, for example) |
| Real-time threads | threads whose priority is based on getting a well-defined fraction of total clock cycles, regardless of other activity (in an audio player application, for example). |

Threads can migrate between priority levels for a number of reasons, largely as an artifact of the time sharing algorithm used. However, this migration is within a given band.

Threads marked as being real-time priority are also special in the eyes of the scheduler. A real-time thread tells the scheduler that it needs to run for `A` cycles out of the next `B` cycles. For example, it might need to run for 3000 out of the next 7000 clock cycles in order to keep up. It also tells the scheduler whether those cycles must be contiguous. Using long contiguous quanta is generally frowned upon but is occasionally necessary for specialized real-time applications.

The kernel will make every effort to honor the request, but since this is soft real-time, it cannot be guaranteed. In particular, if the real-time thread requests something relatively reasonable, its priority will remain in the real-time band, but if it lies blatantly about its requirements and behaves in a compute-bound fashion, it may be demoted to the priority of a normal thread.

Changing a thread’s priority to turn it into a real-time priority thread using Mach calls is described in more detail in [Using Mach Scheduling From User Applications](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrrgewueqkcineekrkc).

In addition to the raw Mach RPC interfaces, some aspects of a thread’s priority can be controlled from user space using the POSIX thread priority API. The POSIX thread API is able to set thread priority only within the lowest priority band (0–63). For more information on the POSIX thread priority API, see [Using the pthreads API to Influence Scheduling](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrrgewviucykjcummjqhe).

There are many reasons that a thread’s priority can change. This section attempts to explain the root cause of these thread priority changes.

A real-time thread, as mentioned previously, is penalized (and may even be knocked down to normal thread priority) if it exceeds its time quantum without blocking repeatedly. For this reason, it is very important to make a reasonable guess about your thread’s workload if it needs to run in the real-time band.

Threads that are heavily compute-bound are given lower priority to help minimize response time for interactive tasks so that high–priority compute–bound threads cannot monopolize the system and prevent lower–priority I/O-bound threads from running. Even at a lower priority, the compute–bound threads still run frequently, since the higher–priority I/O-bound threads do only a short amount of processing, block on I/O again, then allow the compute-bound threads to execute.

All of these mechanisms are operating continually in the Mach scheduler. This means that threads are frequently moving up or down in priority based upon their behavior and the behavior of other threads in the system.

There are three basic ways to change how a user thread is scheduled. You can use the BSD `pthreads` API to change basic policy and importance. You can also use Mach RPC calls to change a task’s importance. Finally, you can use RPC calls to change the scheduling policy to move a thread into a different scheduling band. This is commonly used when interacting with CoreAudio.

The `pthreads` API is a user space API, and has limited relevance for kernel programmers. The Mach thread and task APIs are more general and can be used from anywhere in the kernel. The Mach thread and task calls can also be called from user applications.

OS X supports a number of policies at the POSIX threads API level. If you need real-time behavior, you must use the Mach `thread_policy_set` call. This is described in [Using the Mach Thread API to Influence Scheduling](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrrgewueqkcjbdukrsb).

The `pthreads` API adjusts the priority of threads within a given task. It does not necessarily impact performance relative to threads in other tasks. To increase the priority of a task, you can use `nice` or `renice` from the command line or call `getpriority` and `setpriority` from your application.

The API provides two functions: [pthread_getschedparam](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/pthread_getschedparam.3.html#//apple_ref/doc/man/3/pthread_getschedparam) and [pthread_setschedparam](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/pthread_setschedparam.3.html#//apple_ref/doc/man/3/pthread_setschedparam). Their prototypes look like this:

```
pthread_setschedparam(pthread_t thread, int policy,
        struct sched_param *param);
pthread_getschedparam(pthread_t thread, int *policy,
        struct sched_param *param)
```

The arguments for [pthread_getschedparam](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/pthread_getschedparam.3.html#//apple_ref/doc/man/3/pthread_getschedparam) are straightforward. The first argument is a thread ID, and the others are pointers to memory where the results will be stored.

The arguments to [pthread_setschedparam](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/pthread_setschedparam.3.html#//apple_ref/doc/man/3/pthread_setschedparam) are not as obvious, however. As with [pthread_getschedparam](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/pthread_getschedparam.3.html#//apple_ref/doc/man/3/pthread_getschedparam), the first argument is a thread ID.

The second argument to [pthread_setschedparam](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/pthread_setschedparam.3.html#//apple_ref/doc/man/3/pthread_setschedparam) is the desired policy, which can currently be one of `SCHED_FIFO` (first in, first out), `SCHED_RR` (round-robin), or `SCHED_OTHER`. The `SCHED_OTHER` policy is generally used for extra policies that are specific to a given operating system, and should thus be avoided when writing portable code.

The third argument is a structure that contains various scheduling parameters.

Here is a basic example of using `pthreads` functions to set a thread’s scheduling policy and priority.

```
int set_my_thread_priority(int priority) {
    struct sched_param sp;

    memset(&sp, 0, sizeof(struct sched_param));
    sp.sched_priority=priority;
    if (pthread_setschedparam(pthread_self(), SCHED_RR, &sp)  == -1) {
        printf("Failed to change priority.\n");
        return -1;
    }
    return 0;
}
```

This code snippet sets the scheduling policy for the current thread to round-robin scheduling, and sets the thread’s relative importance within the task to the value passed in through the `priority` argument.

For more information, see the manual page for [pthread](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/pthread.3.html#//apple_ref/doc/man/3/pthread).

This API is frequently used in multimedia applications to obtain real-time priority. It is also useful in other situations when the [pthread](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/pthread.3.html#//apple_ref/doc/man/3/pthread) scheduling API cannot be used or does not provide the needed functionality.

The API consists of two functions, `thread_policy_set` and `thread_policy_get`.

```
kern_return_t thread_policy_set(
                thread_act_t thread,
                thread_policy_flavor_t flavor,
                thread_policy_t policy_info,
                mach_msg_type_number_t count);

kern_return_t thread_policy_get(
                thread_act_t thread,
                thread_policy_flavor_t flavor,
                thread_policy_t policy_info,
                mach_msg_type_number_t *count,
                boolean_t *get_default);
```

The parameters of these functions are roughly the same, except that the `thread_policy_get` function takes pointers for the `count` and the `get_default` arguments. The count is an `inout` parameter, meaning that it is interpreted as the maximum amount of storage (in units of `int32_t`) that the calling task has allocated for the return, but it is also overwritten by the scheduler to indicate the amount of data that was actually returned.

These functions get and set several parameters, according to the thread policy chosen. The possible thread policies are listed in [Table 10-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrrgewueqkcijcuurci).

__Table 10-2__  Thread policies

| Policy | Meaning |
| `THREAD_STANDARD_POLICY` | Default value |
| `THREAD_TIME_CONSTRAINT_POLICY` | Used to specify real-time behavior. |
| `THREAD_PRECEDENCE_POLICY` | Used to indicate the importance of computation relative to other threads in a given task. |

The following code snippet shows how to set the priority of a task to tell the scheduler that it needs real-time performance. The example values provided in comments are based on the estimated needs of `esd` (the Esound daemon).

```c
#include <mach/mach_init.h>
#include <mach/thread_policy.h>
#include <mach/sched.h>
#include <pthread.h>

int set_realtime(int period, int computation, int constraint) {
    struct thread_time_constraint_policy ttcpolicy;
    int ret;
    thread_port_t threadport = pthread_mach_thread_np(pthread_self());

    ttcpolicy.period=period; // HZ/160
    ttcpolicy.computation=computation; // HZ/3300;
    ttcpolicy.constraint=constraint; // HZ/2200;
    ttcpolicy.preemptible=1;

    if ((ret=thread_policy_set(threadport,
        THREAD_TIME_CONSTRAINT_POLICY, (thread_policy_t)&ttcpolicy,
        THREAD_TIME_CONSTRAINT_POLICY_COUNT)) != KERN_SUCCESS) {
            fprintf(stderr, "set_realtime() failed.\n");
            return 0;
    }
    return 1;
}
```

The time values are in terms of Mach absolute time units. Since these values differ on different CPUs, you should generally use numbers relative to HZ (a global variable in the kernel that contains the current number of ticks per second). You can either handle this conversion yourself by dividing this value by an appropriate quantity or use the conversion routines described in [Using Kernel Time Abstractions](Miscellaneous%20Kernel%20Services.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrrhewugscejjbemrkg).

Say your computer reports 133 million for the value of HZ. If you pass the example values given as arguments to this function, your thread tells the scheduler that it needs approximately 40,000 (HZ/3300) out of the next 833,333 (HZ/160) bus cycles. The `preemptible` value (1) indicates that those 40,000 bus cycles need not be contiguous. However, the `constraint` value (HZ/2200) tells the scheduler that there can be no more than 60,000 bus cycles between the start of computation and the end of computation.

A straightforward example using this API is code that displays video directly to the framebuffer hardware. It needs to run for a certain number of cycles every frame to get the new data into the frame buffer. It can be interrupted without worry, but if it is interrupted for too long, the video hardware starts displaying an outdated frame before the software writes the updated data, resulting in a nasty glitch. Audio has similar behavior, but since it is usually buffered along the way (in hardware and in software), there is greater tolerance for variations in timing, to a point.

Another policy call is `THREAD_PRECEDENCE_POLICY`. This is used for setting the relative importance of non-real-time threads. Its calling convention is similar, except that its structure is `thread_precedence_policy`, and contains only one field, an `integer_t` called `importance`. While this is a signed 32-bit value, the minimum legal value is zero (`IDLE_PRI`). threads set to `IDLE_PRI` will only execute when no other thread is scheduled to execute.

In general, larger values indicate higher priority. The maximum limit is subject to change, as are the priority bands, some of which have special purposes (such as real-time threads). Thus, in general, you should use pthreads APIs to achieve this functionality rather than using this policy directly unless you are setting up an idle thread.

This relatively simple API is not particularly useful for most developers. However, it may be beneficial if you are developing a graphical user interface for Darwin. It also provides some insight into the prioritization of tasks in OS X. It is presented here for completeness.

The API consists of two functions, `task_policy_set` and `task_policy_get`.

```
kern_return_t task_policy_set(
                task_t task,
                task_policy_flavor_t flavor,
                task_policy_t policy_info,
                mach_msg_type_number_t count);

kern_return_t task_policy_get(
                task_t task,
                task_policy_flavor_t flavor,
                task_policy_t policy_info,
                mach_msg_type_number_t *count,
                boolean_t *get_default);
```

As with `thread_policy_set` and `thread_policy_get`, the parameters are similar, except that the `task_policy_get` function takes pointers for the `count` and the `get_default` arguments. The `count` argument is an `inout` parameter. It is interpreted as the maximum amount of storage that the calling task has allocated for the return, but it is also overwritten by the scheduler to indicate the amount of data that was actually returned.

These functions get and set a single parameter, that of the role of a given task, which changes the way the task’s priority gets altered over time. The possible roles of a task are listed in [Table 10-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrrgewueqkcindecrce).

__Table 10-3__  Task roles

| Role | Meaning |
| `TASK_UNSPECIFIED` | Default value |
| `TASK_RENICED` | This is set when a process is executed with `nice` or is modified by `renice`. |
| `TASK_FOREGROUND_APPLICATION` | GUI application in the foreground. There can be more than one foreground application. |
| `TASK_BACKGROUND_APPLICATION` | GUI application in the background. |
| `TASK_CONTROL_APPLICATION` | Reserved for the dock or equivalent (assigned FCFS). |
| `TASK_GRAPHICS_SERVER` | Reserved for `WindowServer` or equivalent (assigned FCFS). |

The following code snippet shows how to set the priority of a task to tell the scheduler that it is a foreground application (regardless of whether it really is).

```c
#include <mach/mach_init.h>
#include <mach/task_policy.h>
#include <mach/sched.h>

int set_my_task_policy(void) {
    int ret;
    struct task_category_policy tcatpolicy;

    tcatpolicy.role = TASK_FOREGROUND_APPLICATION;

    if ((ret=task_policy_set(mach_task_self(),
        TASK_CATEGORY_POLICY, (thread_policy_t)&tcatpolicy,
        TASK_CATEGORY_POLICY_COUNT)) != KERN_SUCCESS) {
            fprintf(stderr, "set_my_task_policy() failed.\n");
            return 0;
    }
    return 1;
}
```


The OS X scheduler provides a number of public APIs. While many of these APIs should not be used, the APIs to create, destroy, and alter kernel threads are of particular importance. While not technically part of the scheduler itself, they are inextricably tied to it.

The scheduler directly provides certain services that are commonly associated with the use of kernel threads, without which kernel threads would be of limited utility. For example, the scheduler provides support for wait queues, which are used in various synchronization primitives such as mutex locks and semaphores.

The recommended interface for creating threads within the kernel is through the I/O Kit. It provides [IOCreateThread](https://developer.apple.com/documentation/kernel/1575312-iocreatethread), [IOThreadSelf](https://developer.apple.com/documentation/kernel/iothreadself), and [IOExitThread](https://developer.apple.com/documentation/kernel/1575306-ioexitthread) functions that make it relatively painless to create threads in the kernel.

The basic functions for creating and terminating kernel threads are:

```
IOThread IOCreateThread(IOThreadFunc function, void *argument);
IOThread IOThreadSelf(void);
void IOExitThread(void);
```

With the exception of [IOCreateThread](https://developer.apple.com/documentation/kernel/1575312-iocreatethread) (which is a bit more complex), the I/O Kit functions are fairly thin wrappers around Mach thread functions. The types involved are also very thin abstractions. [IOThread](https://developer.apple.com/documentation/kernel/iothread) is really the same as [thread_t](https://developer.apple.com/documentation/kernel/thread_t).

The `IOCreateThread` function creates a new thread that immediately begins executing the function that you specify. It passes a single argument to that function. If you need to pass more than one argument, you should dynamically allocate a data structure and pass a pointer to that structure.

For example, the following code creates a kernel thread and executes the function `myfunc` in that thread:

```c
#include <IOKit/IOLib.h>
#include <libkern/libkern.h>
#include <sys/malloc.h>

struct mydata {
    int three;
    char *string;
};

static void myfunc(void *myarg) {
    struct mydata *md = (struct mydata *)myarg;
    IOLog("Passed %d = %s\n", md->three, md->string);
    IOExitThread();
}

void start_threads() {
    IOThread mythread;
    struct mydata *md = (struct mydata *)malloc(sizeof(*md));
    md->three = 3; md->string = (char *)malloc(2 * sizeof(char));
    md->string[0] = '3'; md->string[1] = '\0';

    // Start a thread using IOCreateThread
    mythread = IOCreateThread(&myfunc, (void *)md);
}
```

One other useful function is `thread_terminate`. This can be used to destroy an arbitrary thread (except, of course, the currently running thread). This can be _extremely_ dangerous if not done correctly. Before tearing down a thread with `thread_terminate`, you should lock the thread and disable any outstanding timers against it. If you fail to deactivate a timer, a kernel panic will occur when the timer expires.

With that in mind, you may be able to terminate a thread as follows:

```
thread_terminate(getact_thread(thread));
```

There thread is of type [thread_t](https://developer.apple.com/documentation/kernel/thread_t). In general, you can only be assured that you can kill yourself, not other threads in the system. The function [thread_terminate](https://developer.apple.com/documentation/kernel/1418708-thread_terminate) takes a single parameter of type [thread_act_t](https://developer.apple.com/documentation/kernel/thread_act_t) (a thread activation). The function `getact_thread` takes a thread shuttle (`thread_shuttle_t`) or [thread_t](https://developer.apple.com/documentation/kernel/thread_t) and returns the thread activation associated with it.

BSD–based and Mach–based operating systems contain legacy functions designed for basic single-processor synchronization. These include functions such as `splhigh`, `splbio`, `splx`, and other similar functions. Since these functions are not particularly useful for synchronization in an SMP situation, they are not particularly useful as synchronization tools in OS X.

If you are porting legacy code from earlier Mach–based or BSD–based operating systems, you must find an alternate means of providing synchronization. In many cases, this is as simple as taking the kernel or network funnel. In parts of the kernel, the use of `spl` functions does nothing, but causes no harm if you are holding a funnel (and results in a panic if you are not). In other parts of the kernel, `spl` macros are actually used. Because `spl` cannot necessarily be used for its intended purpose, it should not be used in general unless you are writing code it a part of the kernel that already uses it. You should instead use alternate synchronization primitives such as those described in [Synchronization Primitives](Synchronization%20Primitives.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrrhawuerkijjcemq2b).

The wait queue API is used extensively by the scheduler and is closely tied to the scheduler in its implementation. It is also used extensively in locks, semaphores, and other synchronization primitives. The wait queue API is both powerful and flexible, and as a result is somewhat large. Not all of the API is exported outside the scheduler, and parts are not useful outside the context of the wait queue functions themselves. This section documents only the public API.

The wait queue API includes the following functions:

```
void wait_queue_init(wait_queue_t wq, int policy);
extern wait_queue_t wait_queue_t wait_queue_alloc(int policy);
void wait_queue_free(wait_queue_t wq);
void wait_queue_lock(wait_queue_t wq);
void wait_queue_lock_try(wait_queue_t wq);
void wait_queue_unlock(wait_queue_t wq);
boolean_t wait_queue_member(wait_queue_t wq, wait_queue_sub_t wq_sub);
boolean_t wait_queue_member_locked(wait_queue_t wq, wait_queue_sub_t  wq_sub);
kern_return_t wait_queue_link(wait_queue_t wq, wait_queue_sub_t  wq_sub);
kern_return_t wait_queue_unlink(wait_queue_t wq, wait_queue_sub_t  wq_sub);
kern_return_t wait_queue_unlink_one(wait_queue_t wq,
            wait_queue_sub_t *wq_subp);
void wait_queue_assert_wait(wait_queue_t wq, event_t event,
            int interruptible);
void wait_queue_assert_wait_locked(wait_queue_t wq, event_t event,
            int interruptible, boolean_t unlocked);
kern_return_t wait_queue_wakeup_all(wait_queue_t wq, event_t event,
            int result);
kern_return_t wait_queue_peek_locked(wait_queue_t wq, event_t event,
            thread_t *tp, wait_queue_t *wqp);
void wait_queue_pull_thread_locked(wait_queue_t wq, thread_t thread,
            boolean_t unlock);
thread_t wait_queue_wakeup_identity_locked(wait_queue_t wq, event_t  event,
            int result, boolean_t unlock);
kern_return_t wait_queue_wakeup_one(wait_queue_t wq, event_t event,
            int result);
kern_return_t wait_queue_wakeup_one_locked(wait_queue_t wq, event_t  event,
            int result, boolean_t unlock);
kern_return_t wait_queue_wakeup_thread(wait_queue_t wq, event_t  event,
            thread_t thread, int result);
kern_return_t wait_queue_wakeup_thread_locked(wait_queue_t wq, event_t  event,
            thread_t thread, int result, boolean_t unlock);
kern_return_t wait_queue_remove(thread_t thread);
```

Most of the functions and their arguments are straightforward and are not presented in detail. However, a few require special attention.

Most of the functions take an event_t as an argument. These can be arbitrary 32-bit values, which leads to the potential for conflicting events on certain wait queues. The traditional way to avoid this problem is to use the address of a data object that is somehow related to the code in question as that 32-bit integer value.

For example, if you are waiting for an event that indicates that a new block of data has been added to a ring buffer, and if that ring buffer’s head pointer was called `rb_head`, you might pass the value `&rb_head` as the event ID. Because wait queue usage does not generally cross address space boundaries, this is generally sufficient to avoid any event ID conflicts.

Notice the functions ending in `_locked`. These functions require that your thread be holding a lock on the wait queue before they are called. Functions ending in `_locked` are equivalent to their nonlocked counterparts (where applicable) except that they do not lock the queue on entry and may not unlock the queue on exit (depending on the value of `unlock`). The remainder of this section does not differentiate between locked and unlocked functions.

The `wait_queue_alloc` and `wait_queue_init` functions take a policy parameter, which can be one of the following:

- `SYNC_POLICY_FIFO`—first-in, first-out
- `SYNC_POLICY_FIXED_PRIORITY`—policy based on thread priority
- `SYNC_POLICY_PREPOST`—keep track of number of wakeups where no thread was waiting and allow threads to immediately continue executing without waiting until that count reaches zero. This is frequently used when implementing semaphores.

You should not use the `wait_queue_init` function outside the scheduler. Because a wait queue is an opaque object outside that context, you cannot determine the appropriate size for allocation. Thus, because the size could change in the future, you should always use `wait_queue_alloc` and `wait_queue_free` unless you are writing code within the scheduler itself.

Similarly, the functions `wait_queue_member`, `wait_queue_member_locked`, `wait_queue_link`, `wait_queue_unlink`, and `wait_queue_unlink_one` are operations on subordinate queues, which are not exported outside the scheduler.

The function `wait_queue_member` determines whether a subordinate queue is a member of a queue.

The functions `wait_queue_link` and `wait_queue_unlink` link and unlink a given subordinate queue from its parent queue, respectively.

The function `wait_queue_unlink_one` unlinks the first subordinate queue in a given parent and returns it.

The function `wait_queue_assert_wait` causes the calling thread to wait on the wait queue until it is either interrupted (by a thread timer, for example) or explicitly awakened by another thread. The `interruptible` flag indicates whether this function should allow an asynchronous event to interrupt waiting.

The function `wait_queue_wakeup_all` wakes up all threads waiting on a given queue for a particular event.

The function `wait_queue_peek_locked` returns the first thread from a given wait queue that is waiting on a given event. It does not remove the thread from the queue, nor does it wake the thread. It also returns the wait queue where the thread was found. If the thread is found in a subordinate queue, other subordinate queues are unlocked, as is the parent queue. Only the queue where the thread was found remains locked.

The function `wait_queue_pull_thread_locked` pulls a thread from the wait queue and optionally unlocks the queue. This is generally used with the result of a previous call to `wait_queue_peek_locked`.

The function `wait_queue_wakeup_identity_locked` wakes up the first thread that is waiting for a given event on a given wait queue and starts it running but leaves the thread locked. It then returns a pointer to the thread. This can be used to wake the first thread in a queue and then modify unrelated structures based on which thread was actually awakened before allowing the thread to execute.

The function `wait_queue_wakeup_one` wakes up the first thread that is waiting for a given event on a given wait queue.

The function `wait_queue_wakeup_thread` wakes up a given thread if and only if it is waiting on the specified event and wait queue (or one of its subordinates).

The function `wait_queue_remove` wakes a given thread without regard to the wait queue or event on which it is waiting.

[Next](Bootstrap%20Contexts.md)[Previous](Memory%20and%20Virtual%20Memory.md)

