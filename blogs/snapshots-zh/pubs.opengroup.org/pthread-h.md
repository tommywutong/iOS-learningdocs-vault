---
title: '<pthread.h>'
source_url: 'https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/pthread.h.html'
source_domain: pubs.opengroup.org
source_group: single-site
original_language: en
published: ''
archived_at: 2026-07-27
content_hash: 'sha256:2804c7ed9ff2da4d'
plan_ref: 第四周：线程、GCD、Operation 与锁 / Day 2｜了解原始线程，目的是理解上层抽象（对应 W3-03、W3-04）
plan_week: 第四周：线程、GCD、Operation 与锁
plan_day: Day 2｜了解原始线程，目的是理解上层抽象（对应 W3-03、W3-04）
container: //body
container_source: map
translated: true
---

> 原文：[<pthread.h>](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/pthread.h.html)

[\<\<\< 上一页](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/poll.h.html)

[首页](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/contents.html)

[下一页 \>\>\>](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/pwd.h.html)

---

The Open Group Base Specifications Issue 7, 2018 edition
 IEEE Std 1003.1-2017 (Revision of IEEE Std 1003.1-2008)
 Copyright © 2001-2018 IEEE and The Open Group

该文档的更新版本可在[此处](http://pubs.opengroup.org/onlinepubs/9799919799/)找到

---

#### 名称

> pthread.h - 线程

#### 概要

> #include \<pthread.h\>

#### 描述

> _\<pthread.h\>_ 头文件必须定义以下符号常量：
>
> PTHREAD_BARRIER_SERIAL_THREAD
>  PTHREAD_CANCEL_ASYNCHRONOUS
>  PTHREAD_CANCEL_ENABLE
>  PTHREAD_CANCEL_DEFERRED
>  PTHREAD_CANCEL_DISABLE
>  PTHREAD_CANCELED
>  PTHREAD_CREATE_DETACHED
>  PTHREAD_CREATE_JOINABLE
>  ^[[TPS](javascript:open_code('TPS'))] ![[选项开始]](https://pubs.opengroup.org/onlinepubs/9699919799/images/opt-start.gif)
>  PTHREAD_EXPLICIT_SCHED
>  PTHREAD_INHERIT_SCHED
>  ![[选项结束]](https://pubs.opengroup.org/onlinepubs/9699919799/images/opt-end.gif)
>  PTHREAD_MUTEX_DEFAULT
>  PTHREAD_MUTEX_ERRORCHECK
>  PTHREAD_MUTEX_NORMAL
>  PTHREAD_MUTEX_RECURSIVE
>  PTHREAD_MUTEX_ROBUST
>  PTHREAD_MUTEX_STALLED
>  PTHREAD_ONCE_INIT
>  ^[[RPI|TPI](javascript:open_code('RPI'))] ![[选项开始]](https://pubs.opengroup.org/onlinepubs/9699919799/images/opt-start.gif)
>  PTHREAD_PRIO_INHERIT
>  ![[选项结束]](https://pubs.opengroup.org/onlinepubs/9699919799/images/opt-end.gif)
>  ^[[MC1](javascript:open_code('MC1'))] ![[选项开始]](https://pubs.opengroup.org/onlinepubs/9699919799/images/opt-start.gif)
>  PTHREAD_PRIO_NONE
>  ![[选项结束]](https://pubs.opengroup.org/onlinepubs/9699919799/images/opt-end.gif)
>  ^[[RPP|TPP](javascript:open_code('RPP'))] ![[选项开始]](https://pubs.opengroup.org/onlinepubs/9699919799/images/opt-start.gif)
>  PTHREAD_PRIO_PROTECT
>  ![[选项结束]](https://pubs.opengroup.org/onlinepubs/9699919799/images/opt-end.gif)
>  PTHREAD_PROCESS_SHARED
>  PTHREAD_PROCESS_PRIVATE
>  ^[[TPS](javascript:open_code('TPS'))] ![[选项开始]](https://pubs.opengroup.org/onlinepubs/9699919799/images/opt-start.gif)
>  PTHREAD_SCOPE_PROCESS
>  PTHREAD_SCOPE_SYSTEM
>  ![[选项结束]](https://pubs.opengroup.org/onlinepubs/9699919799/images/opt-end.gif)
>
> _\<pthread.h\>_ 头文件必须定义以下编译时常量表达式，这些表达式可作为以下类型的初始化器（initializer）：
>
> **名称**
>
> **初始化器类型**
>
> PTHREAD_COND_INITIALIZER
>
> **pthread_cond_t**
>
> PTHREAD_MUTEX_INITIALIZER
>
> **pthread_mutex_t**
>
> PTHREAD_RWLOCK_INITIALIZER
>
> **pthread_rwlock_t**
>
> _\<pthread.h\>_ 头文件必须定义 **pthread_attr_t**、**pthread_barrier_t**、**pthread_barrierattr_t**、**pthread_cond_t**、**pthread_condattr_t**、**pthread_key_t**、**pthread_mutex_t**、**pthread_mutexattr_t**、**pthread_once_t**、**pthread_rwlock_t**、**pthread_rwlockattr_t**、**pthread_spinlock_t** 和 **pthread_t** 类型，如 [_\<sys/types.h\>_](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/sys_types.h.html) 中所述。
>
> 以下内容必须声明为函数，也可定义为宏。必须提供函数原型。
>
> ```
> int   pthread_atfork(void (*)(void), void (*)(void),
>           void(*)(void));
> int   pthread_attr_destroy(pthread_attr_t *);
> int   pthread_attr_getdetachstate(const pthread_attr_t *, int *);
> int   pthread_attr_getguardsize(const pthread_attr_t *restrict,
>           size_t *restrict);
> [TPS]
> int   pthread_attr_getinheritsched(const pthread_attr_t *restrict,
>           int *restrict);
>
> int   pthread_attr_getschedparam(const pthread_attr_t *restrict,
>           struct sched_param *restrict);
> [TPS]
> int   pthread_attr_getschedpolicy(const pthread_attr_t *restrict,
>           int *restrict);
> int   pthread_attr_getscope(const pthread_attr_t *restrict,
>           int *restrict);
>
> [TSA TSS]
> int   pthread_attr_getstack(const pthread_attr_t *restrict,
>           void **restrict, size_t *restrict);
>
> [TSS]
> int   pthread_attr_getstacksize(const pthread_attr_t *restrict,
>           size_t *restrict);
>
> int   pthread_attr_init(pthread_attr_t *);
> int   pthread_attr_setdetachstate(pthread_attr_t *, int);
> int   pthread_attr_setguardsize(pthread_attr_t *, size_t);
> [TPS]
> int   pthread_attr_setinheritsched(pthread_attr_t *, int);
>
> int   pthread_attr_setschedparam(pthread_attr_t *restrict,
>           const struct sched_param *restrict);
> [TPS]
> int   pthread_attr_setschedpolicy(pthread_attr_t *, int);
> int   pthread_attr_setscope(pthread_attr_t *, int);
>
> [TSA TSS]
> int   pthread_attr_setstack(pthread_attr_t *, void *, size_t);
>
> [TSS]
> int   pthread_attr_setstacksize(pthread_attr_t *, size_t);
>
> int   pthread_barrier_destroy(pthread_barrier_t *);
> int   pthread_barrier_init(pthread_barrier_t *restrict,
>           const pthread_barrierattr_t *restrict, unsigned);
> int   pthread_barrier_wait(pthread_barrier_t *);
> int   pthread_barrierattr_destroy(pthread_barrierattr_t *);
> [TSH]
> int   pthread_barrierattr_getpshared(
>           const pthread_barrierattr_t *restrict, int *restrict);
>
> int   pthread_barrierattr_init(pthread_barrierattr_t *);
> [TSH]
> int   pthread_barrierattr_setpshared(pthread_barrierattr_t *, int);
>
> int   pthread_cancel(pthread_t);
> int   pthread_cond_broadcast(pthread_cond_t *);
> int   pthread_cond_destroy(pthread_cond_t *);
> int   pthread_cond_init(pthread_cond_t *restrict,
>           const pthread_condattr_t *restrict);
> int   pthread_cond_signal(pthread_cond_t *);
> int   pthread_cond_timedwait(pthread_cond_t *restrict,
>           pthread_mutex_t *restrict, const struct timespec *restrict);
> int   pthread_cond_wait(pthread_cond_t *restrict,
>           pthread_mutex_t *restrict);
> int   pthread_condattr_destroy(pthread_condattr_t *);
> int   pthread_condattr_getclock(const pthread_condattr_t *restrict,
>           clockid_t *restrict);
> [TSH]
> int   pthread_condattr_getpshared(const pthread_condattr_t *restrict,
>           int *restrict);
>
> int   pthread_condattr_init(pthread_condattr_t *);
> int   pthread_condattr_setclock(pthread_condattr_t *, clockid_t);
> [TSH]
> int   pthread_condattr_setpshared(pthread_condattr_t *, int);
>
> int   pthread_create(pthread_t *restrict, const pthread_attr_t *restrict,
>           void *(*)(void*), void *restrict);
> int   pthread_detach(pthread_t);
> int   pthread_equal(pthread_t, pthread_t);
> void  pthread_exit(void *);
> [OB XSI]
> int   pthread_getconcurrency(void);
>
> [TCT]
> int   pthread_getcpuclockid(pthread_t, clockid_t *);
>
> [TPS]
> int   pthread_getschedparam(pthread_t, int *restrict,
>           struct sched_param *restrict);
>
> void *pthread_getspecific(pthread_key_t);
> int   pthread_join(pthread_t, void **);
> int   pthread_key_create(pthread_key_t *, void (*)(void*));
> int   pthread_key_delete(pthread_key_t);
> int   pthread_mutex_consistent(pthread_mutex_t *);
> int   pthread_mutex_destroy(pthread_mutex_t *);
> [RPP|TPP]
> int   pthread_mutex_getprioceiling(const pthread_mutex_t *restrict,
>           int *restrict);
>
> int   pthread_mutex_init(pthread_mutex_t *restrict,
>           const pthread_mutexattr_t *restrict);
> int   pthread_mutex_lock(pthread_mutex_t *);
> [RPP|TPP]
> int   pthread_mutex_setprioceiling(pthread_mutex_t *restrict, int,
>           int *restrict);
>
> int   pthread_mutex_timedlock(pthread_mutex_t *restrict,
>           const struct timespec *restrict);
> int   pthread_mutex_trylock(pthread_mutex_t *);
> int   pthread_mutex_unlock(pthread_mutex_t *);
> int   pthread_mutexattr_destroy(pthread_mutexattr_t *);
> [RPP|TPP]
> int   pthread_mutexattr_getprioceiling(
>           const pthread_mutexattr_t *restrict, int *restrict);
>
> [MC1]
> int   pthread_mutexattr_getprotocol(const pthread_mutexattr_t *restrict,
>           int *restrict);
>
> [TSH]
> int   pthread_mutexattr_getpshared(const pthread_mutexattr_t *restrict,
>           int *restrict);
>
> int   pthread_mutexattr_getrobust(const pthread_mutexattr_t *restrict,
>           int *restrict);
> int   pthread_mutexattr_gettype(const pthread_mutexattr_t *restrict,
>           int *restrict);
> int   pthread_mutexattr_init(pthread_mutexattr_t *);
> [RPP|TPP]
> int   pthread_mutexattr_setprioceiling(pthread_mutexattr_t *, int);
>
> [MC1]
> int   pthread_mutexattr_setprotocol(pthread_mutexattr_t *, int);
>
> [TSH]
> int   pthread_mutexattr_setpshared(pthread_mutexattr_t *, int);
>
> int   pthread_mutexattr_setrobust(pthread_mutexattr_t *, int);
> int   pthread_mutexattr_settype(pthread_mutexattr_t *, int);
> int   pthread_once(pthread_once_t *, void (*)(void));
> int   pthread_rwlock_destroy(pthread_rwlock_t *);
> int   pthread_rwlock_init(pthread_rwlock_t *restrict,
>           const pthread_rwlockattr_t *restrict);
> int   pthread_rwlock_rdlock(pthread_rwlock_t *);
> int   pthread_rwlock_timedrdlock(pthread_rwlock_t *restrict,
>           const struct timespec *restrict);
> int   pthread_rwlock_timedwrlock(pthread_rwlock_t *restrict,
>           const struct timespec *restrict);
> int   pthread_rwlock_tryrdlock(pthread_rwlock_t *);
> int   pthread_rwlock_trywrlock(pthread_rwlock_t *);
> int   pthread_rwlock_unlock(pthread_rwlock_t *);
> int   pthread_rwlock_wrlock(pthread_rwlock_t *);
> int   pthread_rwlockattr_destroy(pthread_rwlockattr_t *);
> [TSH]
> int   pthread_rwlockattr_getpshared(
>           const pthread_rwlockattr_t *restrict, int *restrict);
>
> int   pthread_rwlockattr_init(pthread_rwlockattr_t *);
> [TSH]
> int   pthread_rwlockattr_setpshared(pthread_rwlockattr_t *, int);
>
> pthread_t
>       pthread_self(void);
> int   pthread_setcancelstate(int, int *);
> int   pthread_setcanceltype(int, int *);
> [OB XSI]
> int   pthread_setconcurrency(int);
>
> [TPS]
> int   pthread_setschedparam(pthread_t, int,
>           const struct sched_param *);
> int   pthread_setschedprio(pthread_t, int);
>
> int   pthread_setspecific(pthread_key_t, const void *);
> int   pthread_spin_destroy(pthread_spinlock_t *);
> int   pthread_spin_init(pthread_spinlock_t *, int);
> int   pthread_spin_lock(pthread_spinlock_t *);
> int   pthread_spin_trylock(pthread_spinlock_t *);
> int   pthread_spin_unlock(pthread_spinlock_t *);
> void  pthread_testcancel(void);
> ```
>
> 以下内容可声明为函数，或定义为宏，或两者皆可。如果声明为函数，必须提供函数原型。
>
> > ```
> > pthread_cleanup_pop()
> > pthread_cleanup_push()
> > ```
>
> 包含 _\<pthread.h\>_ 头文件必须使 [_\<sched.h\>_](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/sched.h.html) 和 [_\<time.h\>_](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/time.h.html) 头文件中定义的符号可见。

---

_以下部分为参考信息。_

#### 应用用法

> 无。

#### 理由说明

> 无。

#### 未来方向

> 无。

#### 另请参阅

> [_\<sched.h\>_](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/sched.h.html), [_\<sys/types.h\>_](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/sys_types.h.html), [_\<time.h\>_](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/time.h.html)
>
> XSH [_pthread_atfork_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_atfork.html), [_pthread_attr_destroy_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_attr_destroy.html), [_pthread_attr_getdetachstate_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_attr_getdetachstate.html), [_pthread_attr_getguardsize_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_attr_getguardsize.html), [_pthread_attr_getinheritsched_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_attr_getinheritsched.html), [_pthread_attr_getschedparam_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_attr_getschedparam.html), [_pthread_attr_getschedpolicy_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_attr_getschedpolicy.html), [_pthread_attr_getscope_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_attr_getscope.html), [_pthread_attr_getstack_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_attr_getstack.html), [_pthread_attr_getstacksize_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_attr_getstacksize.html), [_pthread_barrier_destroy_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_barrier_destroy.html), [_pthread_barrier_wait_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_barrier_wait.html), [_pthread_barrierattr_destroy_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_barrierattr_destroy.html), [_pthread_barrierattr_getpshared_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_barrierattr_getpshared.html), [_pthread_cancel_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_cancel.html), [_pthread_cleanup_pop_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_cleanup_pop.html), [_pthread_cond_broadcast_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_cond_broadcast.html), [_pthread_cond_destroy_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_cond_destroy.html), [_pthread_cond_timedwait_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_cond_timedwait.html), [_pthread_condattr_destroy_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_condattr_destroy.html), [_pthread_condattr_getclock_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_condattr_getclock.html), [_pthread_condattr_getpshared_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_condattr_getpshared.html), [_pthread_create_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_create.html), [_pthread_detach_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_detach.html), [_pthread_equal_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_equal.html) , [_pthread_exit_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_exit.html), [_pthread_getconcurrency_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_getconcurrency.html), [_pthread_getcpuclockid_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_getcpuclockid.html), [_pthread_getschedparam_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_getschedparam.html), [_pthread_getspecific_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_getspecific.html), [_pthread_join_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_join.html), [_pthread_key_create_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_key_create.html), [_pthread_key_delete_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_key_delete.html), [_pthread_mutex_consistent_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutex_consistent.html), [_pthread_mutex_destroy_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutex_destroy.html), [_pthread_mutex_getprioceiling_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutex_getprioceiling.html), [_pthread_mutex_lock_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutex_lock.html), [_pthread_mutex_timedlock_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutex_timedlock.html), [_pthread_mutexattr_destroy_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutexattr_destroy.html), [_pthread_mutexattr_getprioceiling_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutexattr_getprioceiling.html), [_pthread_mutexattr_getprotocol_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutexattr_getprotocol.html), [_pthread_mutexattr_getpshared_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutexattr_getpshared.html), [_pthread_mutexattr_getrobust_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutexattr_getrobust.html), [_pthread_mutexattr_gettype_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutexattr_gettype.html), [_pthread_once_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_once.html), [_pthread_rwlock_destroy_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_rwlock_destroy.html), [_pthread_rwlock_rdlock_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_rwlock_rdlock.html), [_pthread_rwlock_timedrdlock_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_rwlock_timedrdlock.html), [_pthread_rwlock_timedwrlock_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_rwlock_timedwrlock.html), [_pthread_rwlock_trywrlock_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_rwlock_trywrlock.html), [_pthread_rwlock_unlock_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_rwlock_unlock.html), [_pthread_rwlockattr_destroy_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_rwlockattr_destroy.html), [_pthread_rwlockattr_getpshared_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_rwlockattr_getpshared.html), [_pthread_self_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_self.html), [_pthread_setcancelstate_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_setcancelstate.html), [_pthread_setschedprio_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_setschedprio.html), [_pthread_spin_destroy_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_spin_destroy.html), [_pthread_spin_lock_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_spin_lock.html), [_pthread_spin_unlock_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_spin_unlock.html)

#### 变更历史

> 首次发布于 Issue 5。包含此内容是为了与 POSIX 线程扩展（POSIX Threads Extension）保持一致。

#### Issue 6

> RTT 边界标记已分解到各自的 POSIX 选项中。
>
> 应用了 The Open Group Corrigendum U021/9，更正了 [_pthread_cond_wait_()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_cond_wait.html) 函数的原型。
>
> 应用了 The Open Group Corrigendum U026/2，更正了 [_pthread_setschedparam_()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_setschedparam.html) 函数的原型，使其第二个参数的类型为 **int**。
>
> 添加了 [_pthread_getcpuclockid_()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_getcpuclockid.html) 和 [_pthread_mutex_timedlock_()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutex_timedlock.html) 函数以与 IEEE Std 1003.1d-1999 保持一致。
>
> 添加了以下函数以与 IEEE Std 1003.1j-2000 保持一致：[_pthread_barrier_destroy_()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_barrier_destroy.html)、[_pthread_barrier_init_()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_barrier_init.html)、[_pthread_barrier_wait_()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_barrier_wait.html)、[_pthread_barrierattr_destroy_()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_barrierattr_destroy.html)、[_pthread_barrierattr_getpshared_()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_barrierattr_getpshared.html)、[_pthread_barrierattr_init_()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_barrierattr_init.html)、[_pthread_barrierattr_setpshared_()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_barrierattr_setpshared.html)、[_pthread_condattr_getclock_()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_condattr_getclock.html)、[_pthread_condattr_setclock_()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_condattr_setclock.html)、[_pthread_rwlock_timedrdlock_()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_rwlock_timedrdlock.html)、[_pthread_rwlock_timedwrlock_()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_rwlock_timedwrlock.html)、[_pthread_spin_destroy_()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_spin_destroy.html)、[_pthread_spin_init_()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_spin_init.html)、[_pthread_spin_lock_()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_spin_lock.html)、[_pthread_spin_trylock_()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_spin_trylock.html) 和 [_pthread_spin_unlock_()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_spin_unlock.html)。
>
> 删除了 PTHREAD_RWLOCK_INITIALIZER 以与 IEEE Std 1003.1j-2000 保持一致。
>
> 之前标记为读写锁（Read-Write Locks）选项一部分的函数现在已移至线程（Threads）选项。
>
> **restrict** 关键字已添加到以下函数的原型中：[_pthread_attr_getguardsize_()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_attr_getguardsize.html)、[_pthread_attr_getinheritsched_()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_attr_getinheritsched.html)、[_pthread_attr_getschedparam_()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_attr_getschedparam.html)、[_pthread_attr_getschedpolicy_()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_attr_getschedpolicy.html)、[_pthread_attr_getscope_()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_attr_getscope.html)、[_pthread_attr_getstackaddr_](), [_pthread_attr_getstacksize_()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_attr_getstacksize.html)、[_pthread_attr_setschedparam_()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_attr_setschedparam.html)、[_pthread_barrier_init_()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_barrier_init.html)、[_pthread_barrierattr_getpshared_()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_barrierattr_getpshared.html)、[_pthread_cond_init_()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_cond_init.html)、[_pthread_cond_signal_()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_cond_signal.html)、[_pthread_cond_timedwait_()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_cond_timedwait.html)、[_pthread_cond_wait_()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_cond_wait.html)、[_pthread_condattr_getclock_()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_condattr_getclock.html)、[_pthread_condattr_getpshared_()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_condattr_getpshared.html)、[_pthread_create_()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_create.html)、[_pthread_getschedparam_()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_getschedparam.html)、[_pthread_mutex_getprioceiling_()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutex_getprioceiling.html)、[_pthread_mutex_init_()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutex_init.html)、[_pthread_mutex_setprioceiling_()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutex_setprioceiling.html)、[_pthread_mutexattr_getprioceiling_()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutexattr_getprioceiling.html)、[_pthread_mutexattr_getprotocol_()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutexattr_getprotocol.html)、[_pthread_mutexattr_getpshared_()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutexattr_getpshared.html)、[_pthread_mutexattr_gettype_()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutexattr_gettype.html)、[_pthread_rwlock_init_()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_rwlock_init.html)、[_pthread_rwlock_timedrdlock_()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_rwlock_timedrdlock.html)、[_pthread_rwlock_timedwrlock_()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_rwlock_timedwrlock.html)、[_pthread_rwlockattr_getpshared_()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_rwlockattr_getpshared.html) 和 [_pthread_sigmask_()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_sigmask.html)。
>
> 应用了 IEEE PASC Interpretation 1003.1 #86，允许在包含 _\<pthread.h\>_ 时使 [_\<sched.h\>_](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/sched.h.html) 和 [_\<time.h\>_](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/time.h.html) 中的符号可见。此前这是一个 XSI 选项。
>
> 应用了 IEEE PASC Interpretation 1003.1c #42，移除了对 [_pthread_kill_()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_kill.html) 和 [_pthread_sigmask_()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_sigmask.html) 函数原型的要求。这些函数要求在 [_\<signal.h\>_](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/signal.h.html) 头文件中提供。此处通过命名空间规则允许它们存在。
>
> 应用了 IEEE PASC Interpretation 1003.1 #96，添加了 [_pthread_setschedprio_()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_setschedprio.html) 函数。
>
> 应用了 IEEE Std 1003.1-2001/Cor 1-2002，项目 XBD/TC1/D6/13，纠正了与 POSIX.1-2008 系统接口（System Interfaces）卷相矛盾的选项阴影标记错误。

#### Issue 7

> 应用了 SD5-XBD-ERN-55，向 [_pthread_mutex_timedlock_()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutex_timedlock.html) 函数原型添加了 **restrict** 关键字。
>
> 应用了 SD5-XBD-ERN-62。
>
> 应用了 Austin Group Interpretation 1003.1-2001 #048，恢复了 PTHREAD_RWLOCK_INITIALIZER 符号。
>
> _\<pthread.h\>_ 头文件已从线程选项移至基础部分（Base）。
>
> 以下扩展互斥量（mutex）类型已从 XSI 选项移至基础部分：
>
> > ```
> > PTHREAD_MUTEX_NORMAL
> > PTHREAD_MUTEX_ERRORCHECK
> > PTHREAD_MUTEX_RECURSIVE
> > PTHREAD_MUTEX_DEFAULT
> > ```
>
> PTHREAD_MUTEX_ROBUST 和 PTHREAD_MUTEX_STALLED 符号以及 [_pthread_mutex_consistent_()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutex_consistent.html)、[_pthread_mutexattr_getrobust_()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutexattr_getrobust.html) 和 [_pthread_mutexattr_setrobust_()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutexattr_setrobust.html) 函数已从 The Open Group Technical Standard, 2006, Extended API Set Part 2 中添加。
>
> 与线程优先级保护（Thread Priority Protection）和线程优先级继承（Thread Priority Inheritance）选项相关的功能已分别更改为非健壮互斥量或健壮互斥量优先级保护（Non-Robust Mutex or Robust Mutex Priority Protection）和非健壮互斥量或健壮互斥量优先级继承（Non-Robust Mutex or Robust Mutex Priority Inheritance）。
>
> 此参考页面已就宏和符号常量进行了澄清。
>
> 应用了 POSIX.1-2008, Technical Corrigendum 2, XBD/TC2-2008/0069 [624]。

_参考信息结束。_

---

[返回页面顶部](#top)

---

UNIX ® 是 The Open Group 的注册商标。
 POSIX ™ 是 IEEE 的商标。
 Copyright © 2001-2018 IEEE and The Open Group, All Rights Reserved
 [ [主索引](https://pubs.opengroup.org/onlinepubs/9699919799/mindex.html) | [XBD](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/contents.html) | [XSH](https://pubs.opengroup.org/onlinepubs/9699919799/functions/contents.html) | [XCU](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/contents.html) | [XRAT](https://pubs.opengroup.org/onlinepubs/9699919799/xrat/contents.html) ]

---

[\<\<\< 上一页](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/poll.h.html)

[首页](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/contents.html)

[下一页 \>\>\>](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/pwd.h.html)

---
