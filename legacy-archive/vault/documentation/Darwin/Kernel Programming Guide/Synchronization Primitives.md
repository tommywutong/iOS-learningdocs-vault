---
title: Kernel Programming Guide
apple_id: TP30000905
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2013-08-08'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/KernelProgramming/synchronization/synchronization.html
archived_at: '2026-07-15T07:23:14.199033Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Kernel Programming Guide](About%20This%20Document.md)


[Next](Miscellaneous%20Kernel%20Services.md)[Previous](Boundary%20Crossings.md)

# Synchronization Primitives

This chapter is not intended as an introduction to synchronization. It is assumed that you have some understanding of the basic concepts of locks and semaphores already. If you need additional background reading, synchronization is covered in most introductory operating systems texts. However, since synchronization in the kernel is somewhat different from locking in an application this chapter does provide a brief overview to help ease the transition, or for experienced kernel developers, to refresh your memory.

As an OS X kernel programmer, you have many choices of synchronization mechanisms at your disposal. The kernel itself provides two such mechanisms: locks and semaphores.

A _lock_ is used for basic protection of shared resources. Multiple threads can attempt to acquire a lock, but only one thread can actually hold it at any given time (at least for traditional locks—more on this later). While that thread holds the lock, the other threads must wait. There are several different types of locks, differing mainly in what threads do while waiting to acquire them.

A _semaphore_ is much like a lock, except that a finite number of threads can hold it simultaneously. Semaphores can be thought of as being much like piles of tokens. Multiple threads can take these tokens, but when there are none left, a thread must wait until another thread returns one. It is important to note that semaphores can be implemented in many different ways, so Mach semaphores may not behave in the same way as semaphores on other platforms.

In addition to locks and semaphores, certain low-level synchronization primitives like test and set are also available, along with a number of other atomic operations. These additional operations are described in `libkern/gen/OSAtomicOperations.c` in the kernel sources. Such atomic operations may be helpful if you do not need something as robust as a full-fledged lock or semaphore. Since they are not general synchronization mechanisms, however, they are beyond the scope of this chapter.

Semaphores and locks are similar, except that with semaphores, more than one thread can be doing a given operation at once. Semaphores are commonly used when protecting multiple indistinct resources. For example, you might use a semaphore to prevent a queue from overflowing its bounds.

OS X uses traditional counting semaphores rather than binary semaphores (which are essentially locks). Mach semaphores obey Mesa semantics—that is, when a thread is awakened by a semaphore becoming available, it is not executed immediately. This presents the potential for starvation in multiprocessor situations when the system is under low overall load because other threads could keep downing the semaphore before the just-woken thread gets a chance to run. This is something that you should consider carefully when writing applications with semaphores.

Semaphores can be used any place where mutexes can occur. This precludes their use in interrupt handlers or within the context of the scheduler, and makes it strongly discouraged in the VM system. The public API for semaphores is divided between the MIG–generated `task.h` file (located in your build output directory, included with `#include <mach/task.h>`) and `osfmk/mach/semaphore.h` (`included with #include <mach/semaphore.h>`).

The public semaphore API includes the following functions:

```
kern_return_t semaphore_create(task_t task, semaphore_t *semaphore,
    int policy, int value)
kern_return_t semaphore_signal(semaphore_t semaphore)
kern_return_t semaphore_signal_all(semaphore_t semaphore)
kern_return_t semaphore_wait(semaphore_t semaphore)
kern_return_t semaphore_destroy(task_t task, semaphore_t semaphore)
kern_return_t semaphore_signal_thread(semaphore_t semaphore,
    thread_act_t thread_act)
```

which are described in `<mach/semaphore.h>` or `xnu/osfmk/mach/semaphore.h` (except for create and destroy, which are described in `<mach/task.h>`.

The use of these functions is relatively straightforward with the exception of the `semaphore_create`, `semaphore_destroy`, and `semaphore_signal_thread` calls.

The `value` and `semaphore` parameters for `semaphore_create` are exactly what you would expect—a pointer to the semaphore structure to be filled out and the initial value for the semaphore, respectively.

The `task` parameter refers to the primary Mach task that will “own” the lock. This task should be the one that is ultimately responsible for the subsequent destruction of the semaphore. The `task` parameter used when calling `semaphore_destroy` must match the one used when it was created.

For communication within the kernel, the `task` parameter should be the result of a call to `current_task`. For synchronization with a user process, you need to determine the underlying Mach task for that process by calling `current_task` on the kernel side and `mach_task_self` on the application side.

```
task_t current_task(void);  // returns the kernel task port
task_t mach_task_self(void);// returns the task port of the current  thread
```

The `policy` parameter is passed as the policy for the wait queue contained within the semaphore. The possible values are defined in `osfmk/mach/sync_policy.h`. Current possible values are:

- `SYNC_POLICY_FIFO`
- `SYNC_POLICY_FIXED_PRIORITY`
- `SYNC_POLICY_PREPOST`

The FIFO policy is, as the name suggests, first-in-first-out. The fixed priority policy causes wait queue reordering based on fixed thread priority policies. The prepost policy causes the `semaphore_signal` function to not increment the counter if no threads are waiting on the queue. This policy is needed for creating condition variables (where a thread is expected to always wait until signalled). See the section [Wait Queues and Wait Primitives](Mach%20Scheduling%20and%20Thread%20Interfaces.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrrgewviucykjcummjrgm) for more information.

The `semaphore_signal_thread` call takes a particular thread from the wait queue and places it back into one of the scheduler’s wait-queues, thus making that thread available to be scheduled for execution. If `thread_act` is `NULL`, the first thread in the queue is similarly made runnable.

With the exception of `semaphore_create` and `semaphore_destroy`, these functions can also be called from user space via RPC. See [Calling RPC From User Applications](Boundary%20Crossings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrrg4wueqkcirauur2h) for more information.

The BSD portion of OS X provides `msleep`, `wakeup`, and `wakeup_one`, which are equivalent to condition variables with the addition of an optional time-out. You can find these functions in `sys/proc.h` in the Kernel framework headers.

```
msleep(void *channel, lck_mtx_t *mtx, int priority, const char *wmesg,  struct  timespec *timeout);
msleep0(vvoid *channel, lck_mtx_t *mtx, int priority, const char  *wmesg, uint64_t  deadline);
wakeup(void *channel);
wakeup_one(void *channel);
```

The `msleep` call is similar to a condition variable. It puts a thread to sleep until `wakeup` or `wakeup_one` is called on that channel. Unlike a condition variable, however, you can set a timeout measured in clock ticks. This means that it is both a synchronization call and a delay. The prototypes follow:

```
msleep(void *channel, lck_mtx_t *mtx, int priority, const char *wmesg,  struct  timespec *timeout);
msleep0(vvoid *channel, lck_mtx_t *mtx, int priority, const char  *wmesg, uint64_t  deadline);
wakeup(void *channel);
wakeup_one(void *channel);
```

The three sleep calls are similar except in the mechanism used for timeouts. The function `msleep0` is not recommended for general use.

In these functions, `channel` is a unique identifier representing a single condition upon which you are waiting. Normally, when `msleep` is used, you are waiting for a change to occur in a data structure. In such cases, it is common to use the address of that data structure as the value for `channel`, as this ensures that no code elsewhere in the system will be using the same value.

The `priority` argument has three effects. First, when `wakeup` is called, threads are inserted in the scheduling queue at this priority. Second, if the bit `(priority & PCATCH)` is set, `msleep0` does not allow signals to interrupt the sleep. Third, if the bit `(priority & PDROP)` is zero, `msleep0` drops the mutex on sleep and reacquires it upon waking. If `(priority & PDROP)` is one, `msleep0` drops the mutex if it has to sleep, but does not reacquire it.

The `subsystem` argument is a short text string that represents the subsystem that is waiting on this channel. This is used solely for debugging purposes.

The `timeout` argument is used to set a maximum wait time. The thread may wake sooner, however, if `wakeup` or `wakeup_one` is called on the appropriate channel. It may also wake sooner if a signal is received, depending on the value of `priority`. In the case of `msleep0`, this is given as a mach abstime deadline. In the case of `msleep`, this is given in relative time (seconds and nanoseconds).

Outside the BSD portion of the kernel, condition variables may be implemented using semaphores.

OS X (and Mach in general) has three basic types of locks: spinlocks, mutexes, and read-write locks. Each of these has different uses and different problems. There are also many other types of locks that are not implemented in OS X, such as spin-sleep locks, some of which may be useful to implement for performance comparison purposes.

A spinlock is the simplest type of lock. In a system with a test-and-set instruction or the equivalent, the code looks something like this:

```
while (test_and_set(bit) != 0);
```

In other words, until the lock is available, it simply “spins” in a tight loop that keeps checking the lock until the thread’s _time quantum_ expires and the next thread begins to execute. Since the entire time quantum for the first thread must complete before the next thread can execute and (possibly) release the lock, a spinlock is very wasteful of CPU time, and should be used _only_ in places where a mutex cannot be used, such as in a hardware exception handler or low-level interrupt handler.

Note that a thread may not block while holding a spinlock, because that could cause deadlock. Further, preemption is disabled on a given processor while a spinlock is held.

There are three basic types of spinlocks available in OS X: `lck_spin_t` (which supersedes `simple_lock_t`), `usimple_lock_t`, and `hw_lock_t`. You are strongly encouraged to _not_ use `hw_lock_t`; it is only mentioned for the sake of completeness. Of these, only `lck_spin_t` is accessible from kernel extensions.

The `u` in `usimple` stands for uniprocessor, because they are the only spinlocks that provide actual locking on uniprocessor systems. Traditional simple locks, by contrast, disable preemption but do not spin on uniprocessor systems. Note that in most contexts, it is not useful to spin on a uniprocessor system, and thus you usually only need simple locks. Use of usimple locks is permissible for synchronization between thread context and interrupt context or between a uniprocessor and an intelligent device. However, in most cases, a mutex is a better choice.

The spinlock functions accessible to kernel extensions consist of the following:

```
 extern lck_spin_t     *lck_spin_alloc_init(
          lck_grp_t     *grp,
          lck_attr_t     *attr);

 extern void lck_spin_init(
          lck_spin_t     *lck,
          lck_grp_t     *grp,
          lck_attr_t     *attr);

 extern void lck_spin_lock(
          lck_spin_t     *lck);

 extern void lck_spin_unlock(
          lck_spin_t     *lck);

 extern void lck_spin_destroy(
          lck_spin_t     *lck,
          lck_grp_t     *grp);

 extern void lck_spin_free(
          lck_spin_t     *lck,
          lck_grp_t     *grp);

 extern wait_result_t lck_spin_sleep(
          lck_spin_t     *lck,
          lck_sleep_action_t     lck_sleep_action,
          event_t     event,
          wait_interrupt_t     interruptible);

 extern wait_result_t lck_spin_sleep_deadline(
          lck_spin_t     *lck,
          lck_sleep_action_t     lck_sleep_action,
          event_t     event,
          wait_interrupt_t     interruptible,
          uint64_t     deadline);
```

Prototypes for these locks can be found in `<kern/locks.h>`.

The arguments to these functions are described in detail in [Using Lock Functions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrrhawueqkcineekskb).

A mutex, mutex lock, or sleep lock, is similar to a spinlock, except that instead of constantly polling, it places itself on a queue of threads waiting for the lock, then yields the remainder of its time quantum. It does not execute again until the thread holding the lock wakes it (or in some user space variations, until an asynchronous signal arrives).

Mutexes are more efficient than spinlocks for most purposes. However, they are less efficient in multiprocessing environments where the expected lock-holding time is relatively short. If the average time is relatively short but occasionally long, spin/sleep locks may be a better choice. Although OS X does not support spin/sleep locks in the kernel, they can be easily implemented on top of existing locking primitives. If your code performance improves as a result of using such locks, however, you should probably look for ways to restructure your code, such as using more than one lock or moving to read-write locks, depending on the nature of the code in question. See [Spin/Sleep Locks](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrrhawugssiirbegqke) for more information.

Because mutexes are based on blocking, they can only be used in places where blocking is allowed. For this reason, mutexes cannot be used in the context of interrupt handlers. Interrupt handlers are not allowed to block because interrupts are disabled for the duration of an interrupt handler, and thus, if an interrupt handler blocked, it would prevent the scheduler from receiving timer interrupts, which would prevent any other thread from executing, resulting in deadlock.

For a similar reason, it is not reasonable to block within the scheduler. Also, blocking within the VM system can easily lead to deadlock if the lock you are waiting for is held by a task that is paged out.

However, unlike simple locks, it is permissible to block while holding a mutex. This would occur, for example, if you took one lock, then tried to take another, but the second lock was being held by another thread. However, this is generally not recommended unless you carefully scrutinize all uses of that mutex for possible circular waits, as it can result in deadlock. You can avoid this by always taking locks in a certain order.

In general, blocking while holding a mutex specific to your code is fine as long as you wrote your code correctly, but blocking while holding a more global mutex is probably not, since you may not be able to guarantee that other developers’ code obeys the same ordering rules.

A Mach mutex is of type `mutex_t`. The functions that operate on mutexes include:

```
lck_mtx_t           *lck_mtx_alloc_init(lck_grp_t       *grp,
                                        lck_attr_t      *attr);
extern void         lck_mtx_init(       lck_mtx_t       *lck,
                                        lck_grp_t       *grp,
                                        lck_attr_t      *attr);

extern void         lck_mtx_lock(   lck_mtx_t           *lck);

extern void         lck_mtx_unlock( lck_mtx_t           *lck);

extern void         lck_mtx_destroy(lck_mtx_t           *lck,
                                    lck_grp_t           *grp);

extern void         lck_mtx_free(   lck_mtx_t           *lck,
                                    lck_grp_t           *grp);

extern wait_result_tlck_mtx_sleep(  lck_mtx_t           *lck,
                                    lck_sleep_action_t  lck_sleep_action,
                                    event_t             event,
                                    wait_interrupt_t    interruptible);

extern wait_result_tlck_mtx_sleep_deadline(
                                    lck_mtx_t           *lck,
                                    lck_sleep_action_t  lck_sleep_action,
                                    event_t             event,
                                    wait_interrupt_t    interruptible,
                                    uint64_t            deadline);

extern void         lck_mtx_assert( lck_mtx_t           *lck,
                                    unsigned int        type);
```

as described in `<kern/locks.h>`.

The arguments to these functions are described in detail in [Using Lock Functions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrrhawueqkcineekskb).

Read-write locks (also called shared-exclusive locks) are somewhat different from traditional locks in that they are not always exclusive locks. A read-write lock is useful when shared data can be reasonably read concurrently by multiple threads except while a thread is modifying the data. Read-write locks can dramatically improve performance if the majority of operations on the shared data are in the form of reads (since it allows concurrency), while having negligible impact in the case of multiple writes.

A read-write lock allows this sharing by enforcing the following constraints:

- Multiple readers can hold the lock at any time.
- Only one writer can hold the lock at any given time.
- A writer must block until all readers have released the lock before obtaining the lock for writing.
- Readers arriving while a writer is waiting to acquire the lock will block until after the writer has obtained and released the lock.

The first constraint allows read sharing. The second constraint prevents write sharing. The third prevents read-write sharing, and the fourth prevents starvation of the writer by a steady stream of incoming readers.

Mach read-write locks also provide the ability for a reader to become a writer and vice-versa. In locking terminology, an upgrade is when a reader becomes a writer, and a downgrade is when a writer becomes a reader. To prevent deadlock, some additional constraints must be added for upgrades and downgrades:

- Upgrades are favored over writers.
- The second and subsequent concurrent upgrades will fail, causing that thread’s read lock to be released.

The first constraint is necessary because the reader requesting an upgrade is holding a read lock, and the writer would not be able to obtain a write lock until the reader releases its read lock. In this case, the reader and writer would wait for each other forever. The second constraint is necessary to prevent the deadlock that would occur if two readers wait for the other to release its read lock so that an upgrade can occur.

The functions that operate on read-write locks are:

```
extern lck_rw_t *lck_rw_alloc_init(
            lck_grp_t               *grp,
            lck_attr_t              *attr);

extern void lck_rw_init(
            lck_rw_t                *lck,
            lck_grp_t               *grp,
            lck_attr_t              *attr);



extern void lck_rw_lock(
            lck_rw_t                *lck,
            lck_rw_type_t   lck_rw_type);

extern void lck_rw_unlock(
            lck_rw_t                *lck,
            lck_rw_type_t   lck_rw_type);

extern void lck_rw_lock_shared(
            lck_rw_t                *lck);

extern void lck_rw_unlock_shared(
            lck_rw_t                *lck);

extern void lck_rw_lock_exclusive(
            lck_rw_t                *lck);

extern void lck_rw_unlock_exclusive(
            lck_rw_t                *lck);

extern void lck_rw_destroy(
            lck_rw_t                *lck,
            lck_grp_t               *grp);

extern void lck_rw_free(
            lck_rw_t                *lck,
            lck_grp_t               *grp);

extern wait_result_t lck_rw_sleep(
            lck_rw_t                        *lck,
            lck_sleep_action_t      lck_sleep_action,
            event_t                         event,
            wait_interrupt_t        interruptible);

extern wait_result_t lck_rw_sleep_deadline(
            lck_rw_t                        *lck,
            lck_sleep_action_t      lck_sleep_action,
            event_t                         event,
            wait_interrupt_t        interruptible,
            uint64_t                        deadline);
```

This is a more complex interface than that of the other locking mechanisms, and actually is the interface upon which the other locks are built.

The functions `lck_rw_lock` and `lck_rw_unlock` lock and unlock a lock as either shared (read) or exclusive (write), depending on the value of `lck_rw_type`., which can contain either `LCK_RW_TYPE_SHARED` or `LCK_RW_TYPE_EXCLUSIVE`. You should always be careful when using these functions, as unlocking a lock held in shared mode using an exclusive call or vice-versa will lead to undefined results.

The arguments to these functions are described in detail in [Using Lock Functions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrrhawueqkcineekskb).

Spin/sleep locks are not implemented in the OS X kernel. However, they can be easily implemented on top of existing locks if desired.

For short waits on multiprocessor systems, the amount of time spent in the context switch can be greater than the amount of time spent spinning. When the time spent spinning while waiting for the lock becomes greater than the context switch overhead, however, mutexes become more efficient. For this reason, if there is a large degree of variation in wait time on a highly contended lock, spin/sleep locks may be more efficient than traditional spinlocks or mutexes.

Ideally, a program should be written in such a way that the time spent holding a lock is always about the same, and the choice of locking is clear. However, in some cases, this is not practical for a highly contended lock. In those cases, you may consider using spin/sleep locks.

The basic principle of spin/sleep locks is simple. A thread takes the lock if it is available. If the lock is not available, the thread may enter a spin cycle. After a certain period of time (usually a fraction of a time quantum or a small number of time quanta), the spin routine’s time-out is reached, and it returns failure. At that point, the lock places the waiting thread on a queue and puts it to sleep.

In other variations on this design, spin/sleep locks determine whether to spin or sleep according to whether the lock-holding thread is currently on another processor (or is about to be).

For short wait periods on multiprocessor computers, the spin/sleep lock is more efficient than a mutex, and roughly as efficient as a standard spinlock. For longer wait periods, the spin/sleep lock is significantly more efficient than the spinlock and only slightly less efficient than a mutex. There is a period near the transition between spinning and sleeping in which the spin/sleep lock may behave significantly worse than either of the basic lock types, however. Thus, spin/sleep locks should not be used unless a lock is heavily contended and has widely varying hold times. When possible, you should rewrite the code to avoid such designs.

While most of the locking functions are straightforward, there are a few details related to allocating, deallocating, and sleeping on locks that require additional explanation. As the syntax of these functions is identical across all of the lock types, this section explains only the usage for spinlocks. Extending this to other lock types is left as a (trivial) exercise for the reader.

The first thing you must do when allocating locks is to allocate a lock group and a lock attribute set. Lock groups are used to name locks for debugging purposes and to group locks by function for general understandability. Lock attribute sets allow you to set flags that alter the behavior of a lock.

The following code illustrates how to allocate an attribute structure and a lock group structure for a lock. In this case, a spinlock is used, but with the exception of the lock allocation itself, the process is the same for other lock types.

__Listing 17-1__  Allocating lock attributes and groups (lifted liberally from kern_time.c)

```
lck_grp_attr_t *tz_slock_grp_attr;
lck_grp_t *tz_slock_grp;
lck_attr_t *tz_slock_attr;
lck_spin_t *tz_slock;

/* allocate lock group attribute and group */
tz_slock_grp_attr = lck_grp_attr_alloc_init();
lck_grp_attr_setstat(tz_slock_grp_attr);

tz_slock_grp =  lck_grp_alloc_init("tzlock", tz_slock_grp_attr);

/* Allocate lock attribute */
tz_slock_attr = lck_attr_alloc_init();
//lck_attr_setdebug(tz_slock_attr); // set the debug flag
//lck_attr_setdefault(tz_slock_attr); // clear the debug flag

/* Allocate the spin lock */
tz_slock = lck_spin_alloc_init(tz_slock_grp, tz_slock_attr);
```

The first argument to the lock initializer, of type `lck_grp_t`, is a lock group. This is used for debugging purposes, including lock contention profiling. The details of lock tracing are beyond the scope of this document, however, every lock must belong to a group (even if that group contains only one lock).

The second argument to the lock initializer, of type `lck_attr_t`, contains attributes for the lock. Currently, the only attribute available is lock debugging. This attribute can be set using `lck_attr_setdebug` and cleared with `lck_attr_setdefault`.

To dispose of a lock, you simply call the matching free functions. For example:

```
lck_spin_free(tz_slock, tz_slock_grp);
lck_attr_free(tz_slock_attr);
lck_grp_free(tz_slock_grp);
lck_grp_attr_free(tz_slock_grp_attr);
```

The other two interesting functions are `lck_spin_sleep` and `lck_spin_sleep_deadline`. These functions release a spinlock and sleep until an event occurs, then wake. The latter includes a timeout, at which point it will wake even if the event has not occurred.

```
extern wait_result_t lck_spin_sleep(
                lck_rspin_t         *lck,
                lck_sleep_action_t  lck_sleep_action,
                event_t             event,
                wait_interrupt_t    interruptible);

extern wait_result_t lck_spin_sleep_deadline(
                lck_spin_t          *lck,
                lck_sleep_action_t  lck_sleep_action,
                event_t             event,
                wait_interrupt_t    interruptible,
                uint64_t            deadline);
```

The parameter `lck_sleep_action` controls whether the lock will be reclaimed after sleeping prior to this function returning. The valid options are:

**`LCK_SLEEP_DEFAULT`**
: Release the lock while waiting for the event, then reclaim it. Read-write locks are held in the same mode as they were originally held.

**`LCK_SLEEP_UNLOCK`**
: Release the lock and return with the lock unheld.

**`LCK_SLEEP_SHARED`**
: Reclaim the lock in shared mode (read-write locks only).

**`LCK_SLEEP_EXCLUSIVE`**
: Reclaim the lock in exclusive mode (read-write locks only).

The `event` parameter can be any arbitrary integer, but it must be unique across the system. To ensure uniqueness, a common programming practice is to use the address of a global variable (often the one containing a lock) as the event value. For more information on these events, see [Event and Timer Waits](Miscellaneous%20Kernel%20Services.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrrhewviucykjcummjqhe).

The parameter `interruptible` indicates whether the scheduler should allow the wait to be interrupted by asynchronous signals. If this is false, any false wakes will result in the process going immediately back to sleep (with the exception of a timer expiration signal, which will still wake `lck_spin_sleep_deadline`).

[Next](Miscellaneous%20Kernel%20Services.md)[Previous](Boundary%20Crossings.md)

