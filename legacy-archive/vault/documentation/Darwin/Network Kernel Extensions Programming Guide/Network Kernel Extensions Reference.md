---
title: Network Kernel Extensions Programming Guide
apple_id: TP40001858
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2012-01-09'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/NKEConceptual/reference/reference.html
archived_at: '2026-07-15T07:23:18.059210Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Network Kernel Extensions Programming Guide](Introduction%20to%20Network%20Kernel%20Extensions%20Programming%20Guide.md)


[Next](Glossary.md)[Previous](Network%20Interfaces%20and%20Protocol%20Plumbers.md)

# Network Kernel Extensions Reference

The document _KPI Reference_ describes the functions that NKEs can call and describes a few NKE-specific data types. They are organized by header file. This chapter includes a few additional APIs that may be useful when writing an NKE.

- [Kernel Utilities](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnjyfvbuqmrtgiwueqsbi5cuussk) lists some kernel utilities that NKEs can call.
- `kpi_interface.h` includes functions for manipulating network interfaces, including packet injection, attaching/detaching protocols, attaching/detaching interfaces, and so on.
- `kpi_interfacefilter.h` includes functions for filtering at the raw packet level, just above the network interface layer. These functions are appropriate for an interface filter.
- `kpi_ipfilter.h` includes functions for attaching a packet filter for IPv4 or IPv6 packets. These functions are appropriate for a KEXT that filters IP traffic.
- `kpi_mbuf.h` includes functions for manipulating mbuf data structures. These are used heavily for passing packets and packet fragments around throughout the protocol stack.
- `kpi_protocol.h` includes functions for packet injection. It also includes functions to register “plumbers”—handlers that deal with requests for attaching a protocol to an interface (and detaching, and so on).
- `kpi_socket.h` includes functions for manipulating a socket, including packet send/receive and flag manipulation.
- `kpi_socketfilter.h` includes functions and data type definitions for creating a socket filter.

NKEs can call a number of kernel utility functions including the following:

- `[“_MALLOC”](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnjyfvbuqmrtgiwueqsbi5duorke)`
- `[“_FREE”](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnjyfvbuqmrtgiwueqsbjbdeqskd)`
- `[“printf”](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnjyfvbuqmrtgiwueqsbjbceqqkh)`
- `[“proc_exiting”](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnjyfvbuqmrtgiwugskbi5dukrcg)`
- `[“proc_is64bit”](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnjyfvbuqmrtgiwugskbireeoq2b)`
- `[“proc_rele”](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnjyfvbuqmrtgiwugskbizbecqkh)`
- `[“proc_self”](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnjyfvbuqmrtgiwugskbizbeeqsh)`
- `[“proc_suser”](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnjyfvbuqmrtgiwueqsbi5eukr2j)`
- `[“msleep”](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnjyfvbuqmrtgiwueqsbindesrsf)`
- `[“wakeup”](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnjyfvbuqmrtgiwueqsbinbeorsh)`
- `[“wakeup_one”](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnjyfvbuqmrtgiwugskbjjeuursg)`

This list does not attempt to be exhaustive, but highlights many of the more frequently-used utility functions.

Defined in: `<sys/malloc.h>`

Allocates kernel memory.

```
    void *_MALLOC(size_t size, int type, int flags);
```

`_MALLOC` is much like the user-space `malloc` function, but it has additional parameters that require some explanation.

The `types` argument is a number representing the type of data that will be stored in the argument. This is used primarily for accounting purposes. The known types are described in `<sys/malloc.h>`.

The flags argument consists of some combination of `M_WAITOK`, `M_NOWAIT`, and `M_ZERO`.

The flag `M_NOWAIT` causes `_MALLOC` to immediately return a null pointer if no space is available rather than waiting for space to become available. While this is appropriate for time-sensitive tasks that can be retried, it is not always what you want.

The more traditional (and default) behavior is `M_WAITOK`, which indicates that it is safe to wait for space to become available. If your code is in a critical path for performance, you should probably use `M_NOWAIT` if possible, and depend on the networking stack to retry after resources become available.

Finally, the flag `M_ZERO` requests that the allocator should zero the resulting allocation before returning it.

Defined in: `<sys/malloc.h>`

Frees memory allocated with `_MALLOC`

```
    void _FREE(void *addr, int type);
```

The `type` flag passed to `_FREE` must be the same as the flag passed to the corresponding call to `_MALLOC`.

Defined in: `<libkern/libkern.h>`

Print text to the console.

```
    void printf(const char *format, ... );
```

Identical to `printf` in user space. It is not safe to call `printf` from within an interrupt context. This should generally not be an issue, as you should avoid calling NKE functions from within an I/O Kit driver’s filter routine as a matter of course, but it is worth noting.

Defined in: `<sys/proc.h>`

Returns 1 if a process is exiting, else 0.

```
    int proc_exiting(proc_t);
```


Defined in: `<sys/proc.h>`

Returns 1 if a process is a 64-bit executable, else 0.

```
    int proc_is64bit(proc_t);
```


Defined in: `<sys/proc.h>`

Releases a reference to a process entry.

```
    int proc_rele(proc_t);
```


Defined in: `<sys/proc.h>`

Returns a reference to the running process. This must be released with `[“proc_rele”](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnjyfvbuqmrtgiwugskbizbecqkh)`.

```
    proc_t proc_self(void);
```


Defined in: `<sys/proc.h>`

Checks to see if a process is running as the super-user (root).

```
    int proc_suser(struct proc *p);
```


Defined in: `<sys/proc.h>`

Sleep until an event is posted with `[“wakeup”](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnjyfvbuqmrtgiwueqsbinbeorsh)` or until a timeout occurs. This is commonly combined with a timeout value to bound the wait.

```
    int msleep(void *chan, lck_mtx_t *mtx, int pri, const char *wmesg, struct timespec *ts);
```

The timeout value is a standard timespec (defined in `<sys/time.h>`, and is measured in seconds and nanoseconds. To sleep until woken, you should pass a `NULL` value for `ts`.

The parameter `mtx` is a mutex (defined in a processor-specific include, but included with `<sys/lock.h>`) that will be released prior to sleeping. (The mutex _must_ be locked prior to calling msleep.) The mutex will also be reacquired upon wake unless the `PDROP` flag is set in the priority value.

The parameter `chan` should be a unique identifier specific to a given wait event. Usually such an event is associated with the change in a variable, in which case the address of that variable makes a good value for `chan`.

The parameter `pri` is the desired priority on wake (defined in `<sys/param.h>`). After another thread has called `[“wakeup”](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnjyfvbuqmrtgiwueqsbinbeorsh)` on the desired event (specified by the value of `chan`), your code will begin executing at the specified priority. If the `PCATCH` flag is set on `pri`, signal handlers will be tried before and after the sleep.

Returns 0 if awakened with wakeup, `EWOULDBLOCK` on timeout expiry, and `ERESTART` or `EINTR` if `PCATCH` is set and a signal occurred, depending on whether the `SA_RESTART` flag is set on the signal.

Defined in: `<sys/proc.h>`

Wakes all threads sleeping on a given channel through a call to `[“msleep”](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnjyfvbuqmrtgiwueqsbindesrsf)`.

```
    void wakeup(void *chan);
```


Defined in: `<sys/proc.h>`

Wakes the first thread sleeping on a given channel through a call to `[“msleep”](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnjyfvbuqmrtgiwueqsbindesrsf)`.

```
    void wakeup_one(void *chan);
```

[Next](Glossary.md)[Previous](Network%20Interfaces%20and%20Protocol%20Plumbers.md)

