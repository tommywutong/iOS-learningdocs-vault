---
title: Kernel Programming Guide
apple_id: TP30000905
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2013-08-08'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/KernelProgramming/boundaries/boundaries.html
archived_at: '2026-07-15T07:23:13.706758Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Kernel Programming Guide](About%20This%20Document.md)


[Next](Synchronization%20Primitives.md)[Previous](Network%20Architecture.md)

# Boundary Crossings

Two applications can communicate in a number of ways—for example, by using pipes or sockets. The applications themselves are unaware of the underlying mechanisms that provide this communication. However this communication occurs by sending data from one program into the kernel, which then sends the data to the second program.

As a kernel programmer, it is your job to create the underlying mechanisms responsible for communication between your kernel code and applications. This communication is known as crossing the user-kernel boundary. This chapter explains various ways of crossing that boundary.

In a protected memory environment, each process is given its own address space. This means that no program can modify another program’s data unless that data also resides in its own memory space (shared memory). The same applies to the kernel. It resides in its own address space. When a program communicates with the kernel, data cannot simply be passed from one address space to the other as you might between threads (or between programs in environments like Mac OS 9 and most real-time operating systems, which do not have protected memory).

We refer to the kernel’s address space as _kernel space_, and collectively refer to applications’ address spaces as _user space_. For this reason, applications are also commonly referred to as _user-space programs_, or _user programs_ for short.

When the kernel needs a small amount of data from an application, the kernel cannot just dereference a pointer passed in from that application, since that pointer is relative to the application’s address space. Instead, the kernel generally copies that information into storage within its own address space. When a large region of data needs to be moved, it may map entire pages into kernel space for efficiency. The same behavior can be seen in reverse when moving data from the kernel to an application.

Because it is difficult to move data back and forth between the kernel and an application, this separation is called a _boundary_. It is inherently time consuming to copy data, even if that data is just the user-space address of a shared region. Thus, there is a performance penalty whenever a data exchange occurs. If this penalty is a serious problem, it may affect which method you choose for crossing the user-kernel boundary. Also, by trying to minimize the number of boundary crossings, you may find ways to improve the overall design of your code. This is particularly significant if your code is involved in communication between two applications, since the user-kernel boundary must be crossed twice in that case.

There are a number of ways to cross the user-kernel boundary. Some of them are covered in this chapter in the following sections:

- [Mach Messaging and Mach Interprocess Communication (IPC)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrrg4wueqkcircugrkh)
- [BSD syscall API](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrrg4wueqkcincuoqsg)
- [BSD ioctl API](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrrg4wueqkci5feersk)
- [BSD sysctl API](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrrg4wueqkcjjfeesch)
- [Memory Mapping and Block Copying](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrrg4wueqkcivceossk)

In addition, the I/O Kit uses the user-client/device-interface API for most communication. Because that API is specific to the I/O Kit, it is not covered in this chapter. The user client API is covered in _[IOKit Fundamentals](../../Device%20Drivers/IOKit%20Fundamentals/Introduction%20to%20I-O%20Kit%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridambqgaydcmi)_, _[Accessing Hardware From Applications](../../Device%20Drivers/Accessing%20Hardware%20From%20Applications/Introduction%20to%20Accessing%20Hardware%20From%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgnzw)_, and _[IOKit Device Driver Design Guidelines](../../Device%20Drivers/IOKit%20Device%20Driver%20Design%20Guidelines/Introduction%20to%20I-O%20Kit%20Device%20Driver%20Design%20Guidelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmoju)_.

The `ioctl` API is also specific to the construction of device drivers, and is largely beyond the scope of this document. However, since `ioctl` is a BSD API, it is covered at a glance for your convenience.

This chapter covers one subset of Mach IPC—the Mach remote procedure call (RPC) API. It also covers the `syscall`, `sysctl`, memory mapping, and block copying APIs.

Crossing the user-kernel boundary represents a security risk if the kernel code operates on the data in any substantial way (beyond writing it to disk or passing it to another application). You must carefully perform bounds checking on any data passed in, and you must also make sure your code does not dereference memory that no longer belongs to the client application. Also, under _no circumstances_ should you run unverified program code passed in from user space within the kernel. See [Security Considerations](Security%20Considerations.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrqgywuerkijjcemq2b) for further information.

The first step in setting up user-kernel data exchange is choosing a means to do that exchange. First, you must consider the purpose for the communication. Some crucial factors are latency, bandwidth, and the kernel subsystem involved. Before choosing a method of communication, however, you should first understand at a high-level each of these forms of communication.

Mach messaging and Mach interprocess communication (IPC) are relatively low-level ways of communicating between two Mach tasks (processes), as well as between a Mach task and the kernel. These form the basis for most communication outside of BSD and the I/O Kit. The Mach remote procedure call (RPC) API is a high level procedural abstraction built on top of Mach IPC. Mach RPC is the most common use of IPC.

The BSD `syscall` API is an API for calling kernel functions from user space. It is used extensively when writing file systems and networking protocols, in ways that are very subsystem-dependent. Developers are strongly discouraged from using the `syscall` API outside of file-system and network extensions, as no plug-in API exists for registering a new system call with the `syscall` mechanism.

The BSD `sysctl` API (in its revised form) supersedes the `syscall` API and also provides a relatively painless way to change individual kernel variables from user space. It has a straightforward plug-in architecture, making it a good choice where possible.

Memory mapping and block copying are used in conjunction with one of the other APIs mentioned, and provide ways of moving large amounts of data (more than a few bytes) or variably sized data to and from kernel space.

The choice of boundary crossing methods depends largely on the part of the kernel into which you are adding code. In particular, the boundary crossing method preferred for the I/O Kit is different from that preferred for BSD, which is different from that preferred for Mach.

If you are writing a device driver or other related code, you are probably dealing with the I/O Kit. In that case, you should instead read appropriate sections in _[IOKit Fundamentals](../../Device%20Drivers/IOKit%20Fundamentals/Introduction%20to%20I-O%20Kit%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridambqgaydcmi)_, _[Accessing Hardware From Applications](../../Device%20Drivers/Accessing%20Hardware%20From%20Applications/Introduction%20to%20Accessing%20Hardware%20From%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgnzw)_, and _[IOKit Device Driver Design Guidelines](../../Device%20Drivers/IOKit%20Device%20Driver%20Design%20Guidelines/Introduction%20to%20I-O%20Kit%20Device%20Driver%20Design%20Guidelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmoju)_.

If you are writing code that resides in the BSD subsystem (for example, a file system), you should generally use BSD APIs such as `syscall` or `sysctl` unless you require high bandwidth or exceptionally low latency.

If you are writing code that resides anywhere else, you will probably have to use Mach messaging.

The guidelines in the previous section apply to most communication between applications and kernel code. The methods mentioned, however, are somewhat lacking where high bandwidth or low latency are concerns.

If you require high bandwidth, but latency is not an issue, you should probably consider doing memory-mapped communication. For large messages this is handled somewhat transparently by Mach RPC, making it a reasonable choice. For BSD portions of the kernel, however, you must explicitly pass pointers and use `copyin` and `copyout` to move large quantities of data. This is discussed in more detail in [Memory Mapping and Block Copying](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrrg4wueqkcivceossk).

If you require low latency but bandwidth is not an issue, `sysctl` and `syscall` are not good choices. Mach RPC, however, may be an acceptable solution. Another possibility is to actually wire a page of memory (see [Memory Mapping and Block Copying](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrrg4wueqkcivceossk) for details), start an asynchronous Mach RPC `simpleroutine` (to process the data), and use either locks or high/low water marks (buffer fullness) to determine when to read and write data. This can work for high-bandwidth communication as well.

If you require both high bandwidth and low latency, you should also look at the user client/device interface model used in the I/O Kit, since that model has similar requirements.

Mach IPC and Mach messaging are the basis for much of the communication in OS X. In many cases, however, these facilities are used indirectly by services implemented on top of one of them. Mach messaging and IPC are fundamentally similar except that Mach messaging is stateless, which prevents certain types of error recovery, as explained later. Except where explicitly stated, this section treats the two as equivalent.

The fundamental unit of Mach IPC is the _port_. The concept of Mach ports can be difficult to explain in isolation, so instead this section assumes a passing knowledge of a similar concept, that of ports in TCP/IP.

In TCP/IP, a server listens for incoming connections over a network on a particular port. Multiple clients can connect to the port and send and receive data in word-sized or multiple-word–sized blocks. However, only one server process can be bound to the port at a time.

In Mach IPC, the concept is the same, but the players are different. Instead of multiple hosts connecting to a TCP/IP port, you have multiple Mach tasks on the same computer connecting to a Mach port. Instead of firewall rules on a port, you have _port rights_ that specify what tasks can send data to a particular Mach port.

Also, TCP/IP ports are bidirectional, while Mach ports are unidirectional, much like UNIX pipes. This means that when a Mach task connects to a port, it generally allocates a reply port and sends a message containing send rights to that reply port so that the receiving task can send messages back to the sending task.

As with TCP/IP, multiple client tasks can open connections to a Mach port, but only one task can be listening on that port at a time. Unlike TCP/IP, however, the IPC mechanism itself provides an easy means for one task to hand off the right to listen to an arbitrary task. The term _receive rights_ refers to a task’s ability to listen on a given port. Receive rights can be sent from task to task in a Mach message. In the case of Mach IPC (but _not_ Mach messaging), receive rights can even be configured to automatically return to the original task if the new task crashes or becomes unreachable (for example, if the new task is running on another computer and a router crashes).

In addition to specifying receive rights, Mach ports can specify which tasks have the right to send data. A task with send rights may be able to send once, or may be able to arbitrarily send data to a given port, depending on the nature of the rights.

Before you can use Mach IPC for task communication, the sending task must be able to obtain send rights on the receiving task’s _task port_. Historically, there are several ways of doing this, not all of which are supported by OS X. For example, in OS X, unlike most other Mach derivatives, there is no service server or name server. Instead, the bootstrap task and _mach_init_ subsume this functionality.

When a task is created, it is given send rights to a bootstrap port for sending messages to the bootstrap task. Normally a task would use this port to send a message that gives the bootstrap task send rights on another port so that the bootstrap task can then return data to the calling task. Various routines exist in `bootstrap.h` that abstract this process. Indeed, most users of Mach IPC or Mach messaging actually use Mach remote procedure calls (RPC), which are implemented on top of Mach IPC.

Since direct use of IPC is rarely desirable (because it is not easy to do correctly), and because the underlying IPC implementation has historically changed on a regular basis, the details are not covered here. You can find more information on using Mach IPC directly in the _Mach 3 Server Writer’s Guide_ from Silicomp (formerly the Open Group, formerly the Open Software Foundation Research Institute), which can be obtained from the developer section of Apple’s website. While much of the information contained in that book is not fully up-to-date with respect to OS X, it should still be a relatively good resource on using Mach IPC.

Mach RPC is the most common use for Mach IPC. It is frequently used for user-kernel communication, but can also be used for task to task or even computer-to-computer communication. Programmers frequently use Mach RPC for setting certain kernel parameters such as a given thread’s scheduling policy.

RPC is convenient because it is relatively transparent to the programmer. Instead of writing long, complex functions that handle ports directly, you have only to write the function to be called and a small _RPC definition_ to describe how to export the function as an RPC interface. After that, any application with appropriate permissions can call those functions as if they were local functions, and the compiler will convert them to RPC calls.

In the directory `osfmk/mach` (relative to your checkout of the xnu module from CVS), there are a number of files ending in `.defs`; these files contain the RPC definitions. When the kernel (or a kernel module) is compiled, the _Mach Interface Generator (MIG)_ uses these definitions to create IPC code to support the functions exported via RPC. Normally, if you want to add a new remote procedure call, you should do so by adding a definition to one of these existing files. (See [Building and Debugging Kernels](Building%20and%20Debugging%20Kernels.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgewuerkijjcemq2b) for more information on obtaining kernel sources.)

What follows is an example of the definition for a _routine_, one of the more common uses of RPC.

```
routine thread_policy_get(
                    thread      : thread_act_t;
                    flavor      : thread_policy_flavor_t;
            out     policy_info : thread_policy_t, CountInOut;
            inout   get_default : boolean_t);
```

Notice the C-like syntax of the definition. Each parameter in the routine roughly maps onto a parameter in the C function. The C prototype for this function follows.

```
kern_return_t thread_policy_get(
    thread_act_t            act,
    thread_policy_flavor_t  flavor,
    thread_policy_t         policy_info,
    mach_msg_type_number_t  *count,
    boolean_t               get_default);
```

The first two parameters are integers, and are passed as call-by-value. The third is a `struct` containing integers. It is an outgoing parameter, which means that the values stored in that variable will _not_ be received by the function, but _will_ be overwritten on return.

From there it becomes more interesting. The fourth parameter in the C prototype is a representation of the size of the third. In the definition file, this is represented by an added option, `CountInOut`.

The MIG option `CountInOut` specifies that there is to be an `inout` parameter called `count`. An `inout` parameter is one in which the original value can be read by the function being called, and its value is replaced on return from that function. Unlike a separate `inout` parameter, however, the value initially passed through this parameter is not directly set by the calling function. Instead, it is tied to the `policy_info` parameter so that the number of integers in `policy_info` is transparently passed in through this parameter.

In the function itself, the function checks the count parameter to verify that the buffer size is at least the size of the data to be returned to prevent exceeding array bounds. The function changes the value stored in count to be the desired size and returns an error if the buffer is not large enough (unless the buffer pointer is null, in which case it returns success). Otherwise, it dereferences the various fields of the `policy_info` parameter and in so doing, stores appropriate values into it, then returns.

In addition to the `routine`, Mach RPC also has a _simpleroutine_. A `simpleroutine` is a routine that is, by definition, asynchronous. It can have no `out` or `inout` parameters and no return value. The caller does not wait for the function to return. One possible use for this might be to tell an I/O device to send data as soon as it is ready. In that use, the `simpleroutine` might simply wait for data, then send a message to the calling task to indicate the availability of data.

Another important feature of MIG is that of the _subsystem_. In MIG, a subsystem is a group of `routines` and `simpleroutines` that are related in some way. For example, the semaphore subsystem contains related routines that operate on semaphores. There are also subsystems for various timers, parts of the virtual memory (VM) system, and dozens of others in various places throughout the kernel.

Most of the time, if you need to use RPC, you will be doing it within an existing subsystem. The details of creating a new subsystem are beyond the scope of this document. Developers needing to add a new Mach subsystem should consult the _Mach 3 Server Writer’s Guide_ from The Open Group (TOG), which can be obtained from various locations on the internet.

Another feature of MIG is the type. A type in MIG is exactly the same thing as it is in programming languages. However, the construction of aggregate types differs somewhat.

```
type clock_flavor_t     = int;
type clock_attr_t       = array[*:1] of int;
type mach_timespec_t    = struct[2] of int;
```

Data of type `array` is passed as the user-space address of what is assumed to be a contiguous array of the base type, while a struct is passed by copying all of the individual values of an array of the base type. Otherwise, these are treated similarly. A “struct” is not like a C struct, as elements of a MIG struct must all be of the same base type.

The declaration syntax is similar to Pascal, where `*:1` and `2` represent sizes for the array or structure, respectively. The `*:1` construct indicates a variable-sized array, where the size can be up to 1, inclusive, but no larger.

RPC, as mentioned previously, is virtually transparent to the client. The procedure call looks like any other C function call, and no additional library linkage is needed. You need only to bring the appropriate headers in with a `#include` directive. The compiler automatically recognizes the call as a remote procedure call and handles the underlying MIG aspects for you.

The [syscall](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/syscall.2.html#//apple_ref/doc/man/2/syscall) API is the traditional UNIX way of calling kernel functions from user space. Its implementation varies from one part of the kernel to the next, however, and it is completely unsupported for loadable modules. For this reason, it is not a recommended way of getting data into or out of the kernel in OS X unless you are writing a file system.

File systems have to support a number of standard system calls (for example, [mount](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/mount.2.html#//apple_ref/doc/man/2/mount)), but do so by means of generic file system routines that call the appropriate file-system functions. Thus, if you are writing a file system, you need to implement those functions, but you do not need to write the code that handles the system calls directly. For more information on implementing [syscall](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/syscall.2.html#//apple_ref/doc/man/2/syscall) support in file systems, see the chapter [File Systems Overview](File%20Systems%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrrguwueqkcivcuqrsg).

The [ioctl](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/ioctl.2.html#//apple_ref/doc/man/2/ioctl) interface provides a way for an application to send certain commands or information to a device driver. These can be used for parameter tuning (though this is more commonly done with [sysctl](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/sysctl.3.html#//apple_ref/doc/man/3/sysctl)), but can also be used for sending instructions for the driver to perform a particular task (for example, rewinding a tape drive).

The use of the [ioctl](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/ioctl.2.html#//apple_ref/doc/man/2/ioctl) interface is essentially the same under OS X as it is in other BSD-derived operating systems, except in the way that device drivers register themselves with the system. In OS X, unlike most BSDs, the contents of the `/dev` directory are created dynamically by the kernel. This file system mounted on `/dev` is referred to as _devfs_. You can, of course, still manually create device nodes with [mknod](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/mknod.2.html#//apple_ref/doc/man/2/mknod), because devfs is union mounted over the root file system.

The I/O Kit automatically registers some types of devices with devfs, creating a node in `/dev`. If your device family does not do that, you can manually register yourself in devfs using `cdevsw_add` or `bdevsw_add` (for character and block devices, respectively).

When registering a device manually with devfs, you create a `struct cdevsw` or `struct bdevsw` yourself. In that device structure, one of the function pointers is to an [ioctl](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/ioctl.2.html#//apple_ref/doc/man/2/ioctl) function. You must define the particular values passed to the [ioctl](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/ioctl.2.html#//apple_ref/doc/man/2/ioctl) function in a header file accessible to the person compiling the application.

A user application can also look up the device using the I/O Kit function call `getMatchingServices` and then use various I/O Kit calls to tune parameter instead. For more information on looking up a device driver from an application, see the document _[Accessing Hardware From Applications](../../Device%20Drivers/Accessing%20Hardware%20From%20Applications/Introduction%20to%20Accessing%20Hardware%20From%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgnzw)_.

You can also find additional information about writing an [ioctl](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/ioctl.2.html#//apple_ref/doc/man/2/ioctl) in _The Design and Implementation of the 4.4 BSD Operating System_. See the bibliography at the end of this document for more information.

The system control ([sysctl](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/sysctl.3.html#//apple_ref/doc/man/3/sysctl)) API is specifically designed for kernel parameter tuning. This functionality supersedes the [syscall](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/syscall.2.html#//apple_ref/doc/man/2/syscall) API, and also provides an easy way to tune simple kernel parameters without actually needing to write a handler routine in the kernel. The [sysctl](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/sysctl.3.html#//apple_ref/doc/man/3/sysctl) namespace is divided into several broad categories corresponding to the purpose of the parameters in it. Some of these areas include

- kern—general kernel parameters
- vm—virtual memory options
- fs—filesystem options
- machdep—machine dependent settings
- net—network stack settings
- debug—debugging settings
- hw—hardware parameters (generally read-only)
- user—parameters affecting user programs
- ddb—kernel debugger

Most of the time, programs use the [sysctl](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/sysctl.3.html#//apple_ref/doc/man/3/sysctl) call to retrieve the current value of a kernel parameter. For example, in OS X, the hw [sysctl](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/sysctl.3.html#//apple_ref/doc/man/3/sysctl) group includes the option `ncpu`, which returns the number of processors in the current computer (or the maximum number of processors supported by the kernel on that particular computer, whichever is less).

The [sysctl](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/sysctl.3.html#//apple_ref/doc/man/3/sysctl) API can also be used to modify parameters (though most parameters can only be changed by the root). For example, in the net hierarchy, `net.inet.ip.forwarding` can be set to 1 or 0, to indicate whether the computer should forward packets between multiple interfaces (basic routing).

When adding a sysctl, you must do all of the following _first_:

- add the following includes:

  `#include <mach/mach_types.h>`

  `#include
  <sys/systm.h>`

  `#include
  <sys/types.h>`

  `#include
  <sys/sysctl.h>`
- add `-no-cpp-precomp` to your compiler options in Project Builder (or to `CFLAGS` in your makefile if building by hand).

Adding a system control ([sysctl](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/sysctl.3.html#//apple_ref/doc/man/3/sysctl)) was once a daunting task requiring changes to dozens of files. With the current implementation, a system control can be added simply by writing the appropriate handler functions and then registering the handler with the system at runtime. The old-style [sysctl](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/sysctl.3.html#//apple_ref/doc/man/3/sysctl), which used fixed numbers for each control, is deprecated.

The preferred way of adding a [sysctl](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/sysctl.3.html#//apple_ref/doc/man/3/sysctl) looks something like the following:

```
SYSCTL_PROC(_hw, OID_AUTO, l2cr, CTLTYPE_INT|CTLFLAG_RW,
    &L2CR, 0, &sysctl_l2cr, "I", "L2 Cache Register");
```

The `_PROC` part indicates that you are registering a procedure to provide the value (as opposed to simply reading from a static address in kernel memory). `_hw` is the top level category (in this case, hardware), and `OID_AUTO` indicates that you should be assigned the next available control ID in that category (as opposed to the old-style, fixed ID controls). `l2cr` is the name of your control, which will be used by applications to look up the number of your control using [sysctlbyname](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/sysctlbyname.3.html#//apple_ref/doc/man/3/sysctlbyname).

`CTLTYPE_INT` indicates that the value being changed is an integer. Other legal values are `CTLTYPE_NODE`, `CTLTYPE_STRING`, `CTLTYPE_QUAD`, and `CTLTYPE_OPAQUE` (also known as `CTLTYPE_STRUCT`). `CTLTYPE_NODE` is the only one that isn’t somewhat obvious. It refers to a node in the [sysctl](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/sysctl.3.html#//apple_ref/doc/man/3/sysctl) hierarchy that isn’t directly usable, but instead is a parent to other entries. Two examples of nodes are `hw` and `kern`.

`CTLFLAG_RW` indicates that the value can be read and written. Other legal values are `CTLFLAG_RD`, `CTLFLAG_WR`, `CTLFLAG_ANYBODY`, and `CTLFLAG_SECURE`. `CTLFLAG_ANYBODY` means that the value should be modifiable by anybody. (The default is for variables to be changeable only by root.) `CTLFLAG_SECURE` means that the variable can be changed only when running at `securelevel
<= 0` (effectively, in single-user mode).

`L2CR` is the location where the sysctl will store its data. Since the address is set at compile time, however, this must be a global variable or a static local variable. In this case, `L2CR` is a global of type `unsigned int`.

The number `0` is a second argument that is passed to your function. This can be used, for example, to identify which [sysctl](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/sysctl.3.html#//apple_ref/doc/man/3/sysctl) was used to call your handler function if the same handler function is used for more than one control. In the case of strings, this is used to store the maximum allowable length for incoming values.

`sysctl_l2cr` is the handler function for this [sysctl](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/sysctl.3.html#//apple_ref/doc/man/3/sysctl). The prototype for these functions is of the form

```
static int sysctl_l2cr SYSCTL_HANDLER_ARGS;
```

If the [sysctl](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/sysctl.3.html#//apple_ref/doc/man/3/sysctl) is writable, the function may either use `sysctl_handle_int` to obtain the value passed in from user space and store it in the default location or use the `SYSCTL_IN` macro to store it into an alternate buffer. This function must also use the `SYSCTL_OUT` macro to return a value to user space.

`“I”` indicates that the argument should refer to a variable of type `integer` (or a constant, pointer, or other piece of data of equivalent width), as opposed to `“L”` for a `long`, `“A”` for a `string`, `“N”` for a `node` (a `sysctl` that is the parent of a `sysctl` category or subcategory), or `“S”` for a `struct`. `“L2 Cache
Register”` is a human-readable description of your [sysctl](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/sysctl.3.html#//apple_ref/doc/man/3/sysctl).

In order for a control to be accessible from an application, it must be registered. To do this, you do the following:

```
sysctl_register_oid(&sysctl__hw_l2cr);
```

You should generally do this in an init routine for a loadable module. If your code is not part of a loadable module, you should add your [sysctl](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/sysctl.3.html#//apple_ref/doc/man/3/sysctl) to the list of built-in OIDs in the file `kern/sysctl_init.c`.

If you study the `SYSCTL_PROC` constructor macro, you will notice that `sysctl__hw_l2cr` is the name of a variable created by that macro. This means that the `SYSCTL_PROC` line must be before `sysctl_register_oid` in the file, and must be in the same (or broader) scope. This name is in the form of `sysctl_` followed by the name of it’s parent node, followed by another underscore ( `_` ) followed by the name of your `sysctl`.

A similar function, `sysctl_unregister_oid` exists to remove a `sysctl` from the registry. If you are writing a loadable module, you should be certain to do this when your module is unloaded.

In addition to registering your handler function, you also have to write the function. The following is a typical example

```swift
static int myhandler SYSCTL_HANDLER_ARGS
{

    int error, retval;

    error = sysctl_handle_int(oidp, oidp->oid_arg1, oidp->oid_arg2,  req);
    if (!error && req->newptr) {
        /* We have a new value stored in the standard location.*/
        /* Do with it as you see fit here. */
        printf("sysctl_test: stored %d\n", SCTEST);
    } else if (req->newptr) {
        /* Something was wrong with the write request */
        /* Do something here if you feel like it.... */
    } else {
        /* Read request. Always return 763, just for grins. */
        printf("sysctl_test: read %d\n", SCTEST);
        retval=763;
        error=SYSCTL_OUT(req, &retval, sizeof retval);
    }
    /* In any case, return success or return the reason for failure  */
    return error;
}
```

This demonstrates the use of `SYSCTL_OUT` to send an arbitrary value out to user space from the `sysctl` handler. The “phantom” `req` argument is part of the function prototype when the `SYSCTL_HANDLER_ARGS` macro is expanded, as is the `oidp` variable used elsewhere. The remaining arguments are a pointer (type indifferent) and the length of data to copy (in bytes).

This code sample also introduces a new function, `sysctl_handle_int`, which takes the arguments passed to the `sysctl`, and writes the integer into the usual storage area (`L2CR` in the earlier example, `SCTEST` in this one). If you want to see the new value without storing it (to do a sanity check, for example), you should instead use the `SYSCTL_IN` macro, whose arguments are the same as `SYSCTL_OUT`.

In addition to adding new [sysctl](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/sysctl.3.html#//apple_ref/doc/man/3/sysctl) options, you can also add a new category or subcategory. The macro `SYSCTL_DECL` can be used to declare a node that can have children. This requires modifying one additional file to create the child list. For example, if your main C file does this:

```
SYSCTL_DECL(_net_newcat);
SYSCTL_NODE(_net, OID_AUTO, newcat, CTLFLAG_RW, handler, "new  category");
```

then this is basically the same thing as declaring `extern
sysctl_oid_list sysctl__net_newcat_children` in your program. In order for the kernel to compile, or the module to link, you must then add this line:

```
struct sysctl_oid_list sysctl__net_newcat_children;
```

If you are not writing a module, this should go in the file `kern/kern_newsysctl.c`. Otherwise, it should go in one of the files of your module. Once you have created this variable, you can use `_net_newcat` as the parent when creating a new control. As with any [sysctl](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/sysctl.3.html#//apple_ref/doc/man/3/sysctl), the node (`sysctl__net_newcat`) must be registered with `sysctl_register_oid` and can be unregistered with `sysctl_unregister_oid`.

If your [sysctl](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/sysctl.3.html#//apple_ref/doc/man/3/sysctl) only needs to read a value out of a variable, then you do not need to write a function to provide access to that variable. Instead, you can use one of the following macros:

- `SYSCTL_INT(parent,
  nbr, name, access, ptr, val, descr)`
- `SYSCTL_LONG(parent,
  nbr, name, access, ptr, descr)`
- `SYSCTL_STRING(parent,
  nbr, name, access, arg, len, descr)`
- `SYSCTL_OPAQUE(parent,
  nbr, name, access, ptr, len, descr)`
- `SYSCTL_STRUCT(parent,
  nbr, name, access, arg, type, descr)`

The first four parameters for each macro are the same as for `SYSCTL_PROC` (described in the previous section) as is the last parameter. The `len` parameter (where applicable) gives a length of the string or opaque object in bytes.

The `arg` parameters are pointers just like the `ptr` parameters. However, the parameters named `ptr` are explicitly described as pointers because you must explicitly use the “address of” (`&`) operator unless you are already working with a pointer. Parameters called arg either operate on base types that are implicitly pointers or add the & operator in the appropriate place during macro expansion. In both cases, the argument should refer to the integer, character, or other object that the `sysctl` will use to store the current value.

The `type` parameter is the name of the type minus the “`struct`”. For example, if you have an object of type `struct scsipi`, then you would use `scsipi` as that argument. The `SYSCTL_STRUCT` macro is functionally equivalent to `SYSCTL_OPAQUE`, except that it hides the use of `sizeof`.

Finally, the `val` parameter for `SYSCTL_INT` is a default value. If the value passed in `ptr` is `NULL`, this value is returned when the `sysctl` is used. You can use this, for example, when adding a [sysctl](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/sysctl.3.html#//apple_ref/doc/man/3/sysctl) that is specific to certain hardware or certain compile options. One possible example of this might be a special value for `feature.version` that means “not present.” If that feature became available (for example, if a module were loaded by some user action), it could then update that pointer. If that module were subsequently unloaded, it could set the pointer back to `NULL`.

Unlike RPC, [sysctl](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/sysctl.3.html#//apple_ref/doc/man/3/sysctl) requires explicit intervention on the part of the programmer. To complicate things further, there are two different ways of calling [sysctl](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/sysctl.3.html#//apple_ref/doc/man/3/sysctl) functions, and neither one works for every control. The old-style [sysctl](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/sysctl.3.html#//apple_ref/doc/man/3/sysctl) call can only invoke a control if it is listed in a static OID table in the kernel. The new-style [sysctlbyname](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/sysctlbyname.3.html#//apple_ref/doc/man/3/sysctlbyname) call will work for any user-added [sysctl](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/sysctl.3.html#//apple_ref/doc/man/3/sysctl), but not for those listed in the static table. Occasionally, you will even find a control that is registered in both ways, and thus available to both calls. In order to understand the distinction, you must first consider the functions used.

If you are calling a `sysctl` that was added using the new sysctl method (including any sysctl that you may have added), then your sysctl does not have a fixed number that identifies it, since it was added dynamically to the system. Since there is no approved way to get this number from user space, and since the underlying implementation is not guaranteed to remain the same in future releases, you cannot call a dynamically added control using the [sysctl](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/sysctl.3.html#//apple_ref/doc/man/3/sysctl) function. Instead, you must use [sysctlbyname](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/sysctlbyname.3.html#//apple_ref/doc/man/3/sysctlbyname).

```
sysctlbyname(char *name, void *oldp, size_t *oldlenp,
        void *newp, u_int newlen)
```

The parameter `name` is the name of the `sysctl`, encoded as a standard C string.

The parameter `oldp` is a pointer to a buffer where the old value will be stored. The `oldlenp` parameter is a pointer to an integer-sized buffer that holds the current size of the `oldp` buffer. If the `oldp` buffer is not large enough to hold the returned data, the call will fail with errno set to `ENOMEM`, and the value pointed to by `oldlenp` will be changed to indicate the buffer size needed for a future call to succeed.

Here is an example for reading an integer, in this case a buffer size.

```
int get_debug_bufsize()
{
char *name="debug.bpf_bufsize";
int bufsize, retval;
size_t len;
len=4;
retval=sysctlbyname(name, &bufsize, &len, NULL, 0);
/* Check retval here */
return bufsize;
}
```


The [sysctlbyname](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/sysctlbyname.3.html#//apple_ref/doc/man/3/sysctlbyname) system call is the recommended way to call system calls. However, not every built-in system control is registered in the kernel in such a way that it can be called with [sysctlbyname](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/sysctlbyname.3.html#//apple_ref/doc/man/3/sysctlbyname). For this reason, you should also be aware of the [sysctl](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/sysctl.3.html#//apple_ref/doc/man/3/sysctl) system call.

The [sysctl](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/sysctl.3.html#//apple_ref/doc/man/3/sysctl) system call is part of the original historical BSD implementation of system controls. You should not depend on its use for any control that you might add to the system. The classic usage of [sysctl](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/sysctl.3.html#//apple_ref/doc/man/3/sysctl) looks like the following

```
sysctl(int *name, u_int namelen, void *oldp, size_t *oldlenp,
        void *newp, u_int newlen)
```

System controls, in this form, are based on the _MIB_, or Management Information Base architecture. A MIB is a list of objects and identifiers for those objects. Each object identifier, or OID, is a list of integers that represent a tokenization of a path through the [sysctl](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/sysctl.3.html#//apple_ref/doc/man/3/sysctl) tree. For example, if the `hw` class of [sysctl](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/sysctl.3.html#//apple_ref/doc/man/3/sysctl) is number 3, the first integer in the OID would be the number 3. If the `l2cr` option is built into the system and assigned the number 75, then the second integer in the OID would be 75. To put it another way, each number in the OID is an index into a node’s list of children.

Here is a short example of a call to get the bus speed of the current computer:

```
int get_bus_speed()
{
int mib[2], busspeed, retval;
unsigned int miblen;
size_t len;
mib[0]=CTL_HW;
mib[1]=HW_BUS_FREQ;
miblen=2;
len=4;
retval=sysctl(mib, miblen, &busspeed, &len, NULL, 0);
/* Check retval here */
return busspeed;
}
```

For more information on the [sysctl](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/sysctl.3.html#//apple_ref/doc/man/3/sysctl) system call, see the manual page [sysctl](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/sysctl.3.html#//apple_ref/doc/man/3/sysctl).

Memory mapping is one of the more common means of communicating between two applications or between an application and the kernel. While occasionally used by itself, it is usually used in conjunction with one of the other means of boundary crossing.

One way of using memory mapping is known as _shared memory_. In this form, one or more pages of memory are mapped into the address space of two processes. Either process can then access or modify the data stored in those shared pages. This is useful when moving large quantities of data between processes, as it allows direct communication without multiple user-kernel boundary crossings. Thus, when moving large amounts of data between processes, this is preferable to traditional message passing.

The same holds true with memory mapping between an application and the kernel. The BSD [sysctl](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/sysctl.3.html#//apple_ref/doc/man/3/sysctl) and [syscall](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/syscall.2.html#//apple_ref/doc/man/2/syscall) interfaces (and to an extent, Mach IPC) were designed to transfer small units of data of known size, such as an array of four integers. In this regard, they are much like a traditional C function call. If you need to pass a large amount of data to a function in C, you should pass a pointer. This is also true when passing data between an application and the kernel, with the addition of memory mapping or copying to allow that pointer to be dereferenced in the kernel.

There are a number of limitations to the way that memory mapping can be used to exchange data between an application and the kernel. For one, memory allocated in the kernel cannot be written to by applications, including those running as root (unless the kernel is running in an insecure mode, such as single user mode). For this reason, if a buffer must be modified by an application, the buffer must be allocated by that program, _not_ by the kernel.

When you use memory mapping for passing data to the kernel, the application allocates a block of memory and fills it with data. It then performs a system call that passes the address to the appropriate function in kernel space. It should be noted, however, that the address being passed is a virtual address, not a physical address, and more importantly, it is relative to the address space of the program, which is _not_ the same as the address space of the kernel.

Since the address is a user-space virtual address, the kernel must call special functions to copy the block of memory into a kernel buffer or to map the block of memory into the kernel’s address space.

In the OS X kernel, data is most easily copied into kernel space with the BSD `copyin` function, and back out to user space with the `copyout` function. For large blocks of data, entire pages will be memory mapped using copy-on-write. For this reason, it is generally not useful to do memory mapping by hand.

Getting data from the kernel _to_ an application can be done in a number of ways. The most common method is the reverse of the above, in which the application passes in a buffer pointer, the kernel scribbles on a chunk of data, uses `copyout` to copy the buffer data into the address space of the application, and returns `KERN_SUCCESS`. Note that this is really using the buffer allocated in the application, even though the physical memory may have actually been allocated by the kernel. Assuming the kernel frees its reference to the buffer, no memory is wasted.

A special case of memory mapping occurs when doing I/O to a device from user space. Since I/O operations can, in some cases, be performed by DMA hardware that operates based on physical addressing, it is vital that the memory associated with I/O buffers not be paged out while the hardware is copying data to or from the buffer.

For this reason, when a driver or other kernel entity needs a buffer for I/O, it must take steps to mark it as not pageable. This step is referred to as _wiring_ the pages in memory.

Wiring pages into memory can also be helpful where high bandwidth, low latency communication is desired, as it prevents shared buffers from being paged out to disk. In general, however, this sort of workaround should be unnecessary, and is considered to be bad programming practice.

Pages can be wired in two ways. When a memory region is allocated, it may be allocated in a nonpageable fashion. The details of allocating memory for I/O differ, depending on what part of the kernel you are modifying. This is described in more detail in the appropriate sections of this document, or in the case of the I/O Kit, in the API reference documentation (available from the developer section of Apple’s web site). Alternately, individual pages may be wired after allocation.

The recommended way to do this is through a call to `vm_wire` in BSD parts of the kernel, with [mlock](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/mlock.2.html#//apple_ref/doc/man/2/mlock) from applications (but only by processes running as root), or with [IOMemoryDescriptor](https://developer.apple.com/documentation/kernel/iomemorydescriptor)::`prepare` in the I/O Kit. Because this can fail for a number of reasons, it is particularly crucial to check return values when wiring memory. The `vm_wire` call and other virtual memory topics are discussed in more detail in [Memory and Virtual Memory](Memory%20and%20Virtual%20Memory.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrrgawuerkijjcemq2b). The [IOMemoryDescriptor](https://developer.apple.com/documentation/kernel/iomemorydescriptor) class is described in more detail in the I/O Kit API reference available from the developer section of Apple’s web site.

Crossing the user-kernel boundary is not a trivial task. Many mechanisms exist for this communication, and each one has specific advantages and disadvantages, depending on the environment and bandwidth requirements. Security is a constant concern to prevent inadvertently allowing one program to access data or files from another program or user. It is every kernel programmer’s personal responsibility to take security into account any time that data crosses the user-kernel boundary.

[Next](Synchronization%20Primitives.md)[Previous](Network%20Architecture.md)

