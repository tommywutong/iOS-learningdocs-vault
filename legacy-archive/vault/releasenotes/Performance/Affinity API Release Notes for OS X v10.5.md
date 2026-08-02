---
title: Affinity API Release Notes for OS X v10.5
apple_id: TP40006635
resource_type: Release Note
platform: macOS
topic: Performance
technology: null
published: '2007-10-31'
source_url: https://developer.apple.com/library/archive/releasenotes/Performance/RN-AffinityAPI/index.html
archived_at: '2026-07-18T02:59:02.104912Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# Thread Affinity API Release Notes

#### Contents:

- [Applications, Processors, Memory, and Caches](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dmmzvfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mi)
- [Thread Affinity API](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dmmzvfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mq)
- [The sysctl for Cache Sizes and Sharing Levels](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dmmzvfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6my)
- [The sysctl for Processor Package Count](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dmmzvfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6na)
- [The sysctl for Processor Family](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dmmzvfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6ni)
- [For More Information](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dmmzvfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6nq)

### Applications, Processors, Memory, and Caches

Optimized multithreaded applications need to know the number of available processors (for concurrency), and the size and sharing of the processor caches (for memory sharing).

OS X does not export interfaces that identify processors or control thread placement—explicit thread to processor binding is not supported. Instead, the kernel manages all thread placement.  Applications expect that the scheduler will, under most circumstances, run its threads using a good processor placement with respect to cache affinity.

However, the application itself knows the detailed caching characteristics of its threads and its data—in particular, the organization of threads as disjoint sets characterized by their association with (affinity to) distinct shared data.

While threads within such a set exhibit affinity with each other via shared data, they share a disaffinity or negative affinity with respect to other sets. In other words, a set expresses an affinity with an L2 cache and the scheduler should seek to run threads in a set on processors sharing that L2 cache.

To support this, two new APIs are introduced in Leopard:

- A mechanism for an application to express thread affinity hints to the scheduler as an extension to Mach thread policies.
- A more uniform and complete set of [sysctl(3)](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/sysctl.3.html#//apple_ref/doc/man/3/sysctl) controls to obtain processor cache sharing information.

### Thread Affinity API

An affinity set is a collection of threads which share memory resources and wish to share an L2 cache. Distinct affinity sets represent separate affinities—that is, threads belonging to a different set should use a separate L2 cache and hence be run on a different logical processors.

An affinity set is identified by a "tag". Threads are assigned to a particular affinity set by assigning it the tag identifying that set. A thread can belong to at most one affinity set; that is, it has one affinity tag. The default, null, tag represents no affinity.

Each task has a distinct universe of affinity sets and thus a private namespace of tags; a tag value in one task does not identify the same affinity set in another task.

The Mach thread policy calls are defined in header `/usr/include/mach/thread_policy.h` and in `/System/Library/Frameworks/System.framework/PrivateHeaders/mach/thread_policy.h` as follows:

```
kern_return_t  thread_policy_set(                         thread_t                thread,                         thread_policy_flavor_t  flavor,                         thread_policy_t         policy_info,                         mach_msg_type_number_t  count);
kern_return_t  thread_policy_get(                         thread_t                thread,                         thread_policy_flavor_t  flavor,                         thread_policy_t         policy_info,                         mach_msg_type_number_t  *count);                         boolean_t               *get_default);
```

These calls have been extended by adding a new flavor of thread policy:

```
#define THREAD_AFFINITY_POLICY         4  struct thread_affinity_policy {         integer_t       affinity_tag; }; typedef struct thread_affinity_policy   thread_affinity_policy_data_t; typedef struct thread_affinity_policy   *thread_affinity_policy_t;  #define THREAD_AFFINITY_POLICY_COUNT    ((mach_msg_type_number_t) \                 (sizeof (thread_affinity_policy_data_t) / sizeof (integer_t)))  #define THREAD_AFFINITY_TAG_NULL        0
```

By setting a (non-null) affinity tag for a thread, the thread is placed into the affinity set identified by the "tag". By default, all threads have the `THREAD_AFFINITY_NULL` affinity. A non-null tag is arbitrary and can convey application-specific information.

The `thread_policy_set(THREAD_AFFINITY_POLICY)` call can be made after creating a thread but before starting it running in order to influence its initial placement.

For example, an application wanting to run 2 threads on separate L2 caches would set the threads with different affinity tags. On a dual core machine, this affinity will effectively be ignored. However, on a 4-core MacPro, the scheduler will try to run threads on separate packages. Similarly, on an 8-core MacPro, the scheduler will try to run these threads on separate dies (which may or may not be in the same physical CPU package).

An application with a producer and a consumer thread that should share an L2 cache would perform the following steps:

- Create both threads.
- Set the same affinity tag for each thread.
- Start both threads.

An application that wants to place a thread on every available processor would do the following:

- Obtain the number of processors on the system using [sysctl(3)](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/sysctl.3.html#//apple_ref/doc/man/3/sysctl) (see below).
- Create that number of threads.
- Set each thread with a distinct affinity tag.
- Start all threads.

Threads with default affinity policy will be scheduled more freely on any processor. These threads will be preferentially migrated to run on an idle processor. Threads with affinity tags will tend to remain in place.

Generally, the affinity tag namespace is private to one task (process). However, a child process forked after its parent has made a `THREAD_AFFINITY_POLICY` call will share the affinity namespace of the parent process. This enables a family of forked processes to share an affinity namespace despite comprising separate tasks. Moreover, the forked child inherits the affinity tag of its parent. Hence, a parent can seed a number of child processes within an arbitrary organization of shared affinity sets. Note: affinity namespace inheritance is destroyed by the [exec(3)](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/exec.3.html#//apple_ref/doc/man/3/exec) system call, however.

In addition, the header `/usr/include/mach/task_info.h` includes the following new information request:

|  |
| --- |
| ``` struct task_affinity_tag_info {
        integer_t        count;         integer_t        min;         integer_t        max;         integer_t        task_count; }; typedef struct task_affinity_tag_info   task_affinity_tag_info_data_t; typedef struct task_affinity_tag_info   *task_affinity_tag_info_t; #define TASK_AFFINITY_TAG_INFO          16 #define TASK_AFFINITY_TAG_INFO_COUNT    \                 (sizeof(task_affinity_tag_info_data_t) / sizeof(natural_t)) ``` |

This enables you to obtain the number (`count`) and range [`min` .. `max`] of the affinity tags currently defined for a task.

### The sysctl for Cache Sizes and Sharing Levels

For Leopard, the `hw.cacheconfig` sysctl reports the number of logical processors sharing caches at various levels in the system. That is:

- `hw.cacheconfig[0]` reports the RAM sharing (the total number of logical processors).
- `hw.cacheconfig[1]` reports the L1 sharing (the number of logical processors sharing a level 1 cache).
- `hw.cacheconfig[2]` reports the L2 sharing.
- ...

There are already assorted sysctl controls that report the size of various caches. These continue to exist for compatibility, but this information is now consolidated into hw.cachesize where:

- `hw.cachesize[0]` reports the size of memory.
- `hw.cachesize[1]` reports the size of the L1 data cache.
- `hw.cachesize[2]` reports the size of the L2 cache.
- ...

Both `hw.cacheconfig` and `hw.cachesize` are arrays of 64-bit values.

Hence, `hw.cacheconfig` and `hw.cachesize` provide the information needed for an application to configure:

- its threading level for maximum parallelism
- buffer space for cache residency
- affinity hints for thread placement and cache sharing.

### The sysctl for Processor Package Count

The number of processor packages present on a machine is published through `hw.packages`. For currently shipping machines this is `1` or `2`.

### The sysctl for Processor Family

The sysctl `hw.cpufamily` publishes a value identifying the micro-architectural family of the processor. This value is arbitrarily chosen to be unique for this family. No numerical relationship can be inferred between any two values. Processor features present in any family should be determined by querying other specific `hw.optional` variables.

The values returned for processor families supported by Leopard are:

| Processor | hw.cpufamily |
| --- | --- |
| PowerPC G4 | 2009171118 |
| PowerPC G5 | 3983988906 |
| Intel Core Solo/Duo | 1943433984 |
| Intel Core 2 Duo | 1114597871 |

### For More Information

For more information on using `sysctl` controls, see the [Boundary Crossings](https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/KernelProgramming/boundaries/boundaries.html#//apple_ref/doc/uid/TP30000905-CH217) chapter of _[Kernel Programming Guide](../../documentation/Darwin/Kernel%20Programming%20Guide/About%20This%20Document.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbv)_ and the manual pages for [sysctl(3)](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/sysctl.3.html#//apple_ref/doc/man/3/sysctl), [sysctlbyname(3)](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/sysctlbyname.3.html#//apple_ref/doc/man/3/sysctlbyname), and the `sysctl(8)` command.
