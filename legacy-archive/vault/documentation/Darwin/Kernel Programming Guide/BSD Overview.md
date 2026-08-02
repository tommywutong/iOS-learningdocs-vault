---
title: Kernel Programming Guide
apple_id: TP30000905
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2013-08-08'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/KernelProgramming/BSD/BSD.html
archived_at: '2026-07-15T07:23:11.520897Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Kernel Programming Guide](About%20This%20Document.md)


[Next](File%20Systems%20Overview.md)[Previous](I-O%20Kit%20Overview.md)

# BSD Overview

The BSD portion of the OS X kernel is derived primarily from FreeBSD, a version of 4.4BSD that offers advanced networking, performance, security, and compatibility features. BSD variants in general are derived (sometimes indirectly) from 4.4BSD-Lite Release 2 from the Computer Systems Research Group (CSRG) at the University of California at Berkeley. BSD provides many advanced features, including the following:

- Preemptive multitasking with dynamic priority adjustment. Smooth and fair sharing of the computer between applications and users is ensured, even under the heaviest of loads.
- Multiuser access. Many people can use an OS X system simultaneously for a variety of things. This means, for example, that system peripherals such as printers and disk drives are properly shared between all users on the system or the network and that individual resource limits can be placed on users or groups of users, protecting critical system resources from overuse.
- Strong TCP/IP networking with support for industry standards such as SLIP, PPP, and NFS. OS X can interoperate easily with other systems as well as act as an enterprise server, providing vital functions such as NFS (remote file access) and email services, or Internet services such as HTTP, FTP, routing, and firewall (security) services.
- Memory protection. Applications cannot interfere with each other. One application crashing does not affect others in any way.
- Virtual memory and dynamic memory allocation. Applications with large appetites for memory are satisfied while still maintaining interactive response to users. With the virtual memory system in OS X, each application has access to its own 4 GB memory address space; this should satisfy even the most memory-hungry applications.
- Support for kernel threads based on Mach threads. User-level threading packages are implemented on top of kernel threads. Each kernel thread is an independently scheduled entity. When a thread from a user process blocks in a system call, other threads from the same process can continue to execute on that or other processors. By default, a process in the conventional sense has one thread, the _main thread_. A user process can use the POSIX thread API to create other user threads.
- SMP support. Support is included for computers with multiple CPUs.
- Source code. Developers gain the greatest degree of control over the BSD programming environment because source is included.
- Many of the POSIX APIs.

The facilities that are available to a user process are logically divided into two parts: kernel facilities and system facilities implemented by or in cooperation with a server process.

The facilities implemented in the kernel define the _virtual machine_ in which each process runs. Like many real machines, this virtual machine has memory management, an interrupt facility, timers, and counters.

The virtual machine also allows access to files and other objects through a set of descriptors. Each descriptor resembles a device controller and supports a set of operations. Like devices on real machines, some of which are internal to the machine and some of which are external, parts of the descriptor machinery are built into the operating system, while other parts are often implemented in server processes.

The BSD component provides the following kernel facilities:

- processes and protection

  - host and process identifiers
  - process creation and termination
  - user and group IDs
  - process groups
- memory management

  - text, data, stack, and dynamic shared libraries
  - mapping pages
  - page protection control
- POSIX synchronization primitives
- POSIX shared memory
- signals

  - signal types
  - signal handlers
  - sending signals
- timing and statistics

  - real time
  - interval time
- descriptors

  - files
  - pipes
  - sockets
- resource controls

  - process priorities
  - resource utilization and resource limits
  - quotas
- system operation support

  - bootstrap operations
  - shut-down operations
  - accounting

BSD system facilities (facilities that may interact with user space) include

- generic input/output operations such as read and write, nonblocking, and asynchronous operations
- file-system operations
- interprocess communication
- handling of terminals and other devices
- process control
- networking operations

Although the BSD portion of OS X is primarily derived from FreeBSD, some changes have been made:

- The `sbrk()` system call for memory management is deprecated. Its use is not recommended in OS X.
- The OS X runtime model uses a different object file format for executables and shared objects, and a different mechanism for executing some of those executables.

  The primary native format is _Mach-O_. This format is supported by the dynamic link editor (_dyld_).

  The _PEF_ binary file format is supported by the Code Fragment Manager (CFM).

  The kernel supports `execve()` with Mach-O binaries. Mapping and management of Mach-O dynamic shared libraries, as well as launching of PEF-based applications, are performed by user-space code.
- OS X does not support memory-mapped devices through the `mmap()` function. (Graphic device support and other subsystems provide similar functionality, but using different APIs.) In OS X, this interface should be done through user clients. See the Apple I/O Kit documents for additional information.
- The `swapon()` call is not supported; `macx_swapon()` is the equivalent call from the Mach pager.
- The Unified Buffer Cache implementation in OS X differs from that found in FreeBSD.
- Mach provides a number of IPC primitives that are not traditionally found in UNIX. See [Boundary Crossings](Boundary%20Crossings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrrg4wuerkijjcemq2b) for more information on Mach IPC. Some System V primitives are supported, but their use is discouraged in favor of POSIX equivalents.
- Several changes have been made to the BSD security model to support single-user and multiple-administrator configurations, including the ability to disable ownership and permissions on a volume-by-volume basis.
- The locking mechanism used throughout the kernel differs substantially from the mechanism used in FreeBSD.
- The kernel extension mechanism used by OS X is completely different. The OS X driver layer, the I/O Kit, is an object-oriented driver stack written in C++. The general kernel programming interfaces, or KPIs, are used to write non-driver kernel extensions. These mechanisms are described more in [I/O Kit Overview](I-O%20Kit%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrrgmwvgvzr) and _KPI Reference_, respectively.

In addition, several new features have been added that are specific to the OS X (Darwin) implementation of BSD. These features are not found in FreeBSD.

- enhancements to file-system buffer cache and file I/O clustering

  - adaptive and speculative read ahead
  - user-process controlled read ahead
  - time aging of the file-system buffer cache

- enhancements to file-system support

  - implementation of Apple extensions for ISO-9660 file systems
  - multithreaded asynchronous I/O for NFS
  - addition of system calls to support semantics of Mac OS Extended (HFS+) file systems
  - additions to naming conventions for pathnames, as required for accessing multiple forks in Mac OS Extended file systems

The BSD component of the OS X kernel is complex. A complete description is beyond the scope of this document. However, many excellent references exist for this component. If you are interested in BSD, be sure to refer to the bibliography for further information.

Although the BSD layer of OS X is derived from 4.4BSD, keep in mind that it is not identical to 4.4BSD. Some functionality of 4.4 BSD has not been included in OS X. Some new functionality has been added. The cited reference materials are recommended for additional reading. However, they should _not_ be presumed as forming a definitive description of OS X.

[Next](File%20Systems%20Overview.md)[Previous](I-O%20Kit%20Overview.md)

