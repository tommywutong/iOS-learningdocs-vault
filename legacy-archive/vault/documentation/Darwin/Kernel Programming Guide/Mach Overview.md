---
title: Kernel Programming Guide
apple_id: TP30000905
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2013-08-08'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/KernelProgramming/Mach/Mach.html
archived_at: '2026-07-15T07:23:13.683075Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Kernel Programming Guide](About%20This%20Document.md)


[Next](Memory%20and%20Virtual%20Memory.md)[Previous](Kernel%20Programming%20Style.md)

# Mach Overview

The fundamental services and primitives of
the OS X kernel are based on Mach
3.0. Apple has modified and extended Mach to better meet OS X functional and performance goals.

Mach 3.0 was originally conceived as a simple, extensible,
communications microkernel. It is
capable of running as a stand–alone kernel, with other traditional
operating-system services such as I/O, file systems, and networking
stacks running as user-mode servers.

However, in OS X, Mach is linked with other kernel components
into a single kernel address space. This is primarily for performance;
it is much faster to make a direct call between linked components
than it is to send messages or do remote procedure calls (_RPC)_ between
separate tasks. This modular structure results in a more robust
and extensible system than a monolithic kernel would allow, without
the performance penalty of a pure microkernel.

Thus in OS X, Mach is not primarily a communication hub
between clients and servers. Instead, its value consists of its
abstractions, its extensibility, and its flexibility. In particular,
Mach provides

- object-based
  APIs with communication channels (for example, ports) as object references
- highly parallel execution, including preemptively scheduled threads and support for _SMP_
- a flexible scheduling framework, with support for real-time usage
- a complete set of _IPC_ primitives, including messaging, _RPC_, synchronization, and notification
- support for large virtual address spaces, shared memory
  regions, and memory objects backed by persistent store
- proven extensibility and portability, for example across instruction
  set architectures and in distributed environments
- security and resource management as a fundamental principle
  of design; all resources are virtualized

Mach provides a small set of abstractions that have been designed
to be both simple and powerful. These are the main kernel abstractions:

- _Tasks_. The
  units of resource ownership; each task consists of a virtual address
  space, a _port
  right_ _namespace_, and one or more _threads_.
  (Similar to a process.)
- _Threads_. The units of CPU execution within
  a task.
- _Address
  space_. In conjunction with memory managers, Mach implements
  the notion of a sparse virtual address space and shared memory.
- _Memory
  objects_. The internal units of memory management. Memory
  objects include named entries and regions; they are representations
  of potentially persistent data that may be mapped into address spaces.
- _Ports_.
  Secure, simplex communication channels, accessible only via send
  and receive capabilities (known as port rights).
- _IPC_.
  Message queues, remote procedure calls, notifications, semaphores,
  and lock sets.
- _Time_.
  Clocks, timers, and waiting.

At the trap level, the interface to most Mach abstractions
consists of messages sent to and from kernel ports representing
those objects. The trap-level interfaces (such as `mach_msg_overwrite_trap`)
and message formats are themselves abstracted in normal usage by
the Mach Interface Generator (_MIG_).
MIG is used to compile procedural interfaces to the message-based
APIs, based on descriptions of those APIs.

OS X processes and POSIX
threads (_pthreads_)
are implemented on top of Mach tasks and threads, respectively.
A thread is a point of control flow in a task. A task exists to provide
resources for the threads it contains. This split is made to provide
for parallelism and resource sharing.

A thread

- is a point
  of control flow in a task.
- has access to all of the elements of the containing task.
- executes (potentially) in parallel with other threads, even
  threads within the same task.
- has minimal state information for low overhead.

A task

- is a collection
  of system resources. These resources, with the exception of the
  address space, are referenced by ports. These resources may be shared
  with other tasks if rights to the ports are so distributed.
- provides a large, potentially sparse address space, referenced
  by virtual address. Portions of this space may be shared through
  inheritance or external memory management.
- contains some number of threads.

Note that a task has no life of its own—only threads execute
instructions. When it is said that “task Y does X,” what is
really meant is that “a thread contained within task Y does X.”

A task is a fairly expensive entity. It exists to be a collection
of resources. All of the threads in a task share everything. Two
tasks share nothing without an explicit action (although the action
is often simple) and some resources (such as port receive rights) cannot
be shared between two tasks at all.

A thread is a fairly lightweight entity. It is fairly cheap
to create and has low overhead to operate. This is true because
a thread has little state information (mostly its register state). Its
owning task bears the burden
of resource management. On a multiprocessor computer, it is possible
for multiple threads in a task to execute in parallel. Even when
parallelism is not the goal, multiple threads have an advantage
in that each thread
can use a synchronous programming style, instead of attempting asynchronous
programming with a single thread attempting to provide multiple
services.

A thread
is the basic computational entity. A thread belongs to one and only
one task that defines its virtual address space. To affect the structure
of the address space or to reference any resource other than the
address space, the thread must execute a special trap instruction
that causes the kernel to perform operations on behalf of the thread
or to send a message to some agent on behalf of the thread. In general,
these traps manipulate resources associated with the task containing
the thread. Requests can be made of the kernel to manipulate these
entities: to create them, delete them, and affect their state.

Mach provides a flexible framework for thread–scheduling
policies. Early versions of OS X support both _time-sharing_ and _fixed-priority_ policies.
A time-sharing thread’s priority is raised and lowered to balance
its resource consumption against other time-sharing threads.

Fixed-priority threads execute for a certain quantum of time, and then are
put at the end of the queue of threads of equal priority. Setting
a fixed priority thread’s quantum level to infinity allows the
thread to run until it blocks, or until it is preempted by a thread
of higher priority. High priority real-time threads are usually
fixed priority.

OS X also provides time constraint scheduling for real-time
performance. This scheduling allows you to specify that your thread
must get a certain time quantum within a certain period of time.

Mach scheduling is described further in [Mach Scheduling and Thread Interfaces](Mach%20Scheduling%20and%20Thread%20Interfaces.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrrgewuerkijjcemq2b).

With the exception of the task’s virtual address space,
all other Mach resources are accessed through a level of indirection
known as a _port_.
A port is an endpoint of a unidirectional communication channel
between a client who requests a service and a server who provides
the service. If a reply is to be provided to such a service request,
a second port must be used. This is comparable to a (unidirectional)
pipe in UNIX parlance.

In most cases, the resource that is accessed by the port (that
is, named by it) is referred to as an object. Most objects named
by a port have a single receiver and (potentially) multiple senders.
That is, there is exactly one receive port, and at least one sending
port, for a typical object such as a message queue.

The service to be provided by an object is determined by the
manager that receives the request sent to the object. It follows
that the kernel is the receiver for ports associated with kernel-provided
objects and that the receiver for ports associated with task-provided objects
is the task providing those objects.

For ports that name task-provided objects, it is possible
to change the receiver of requests for that port to a different
task, for example by passing the port to that task in a message. A
single task may have multiple ports that refer to resources it supports.
For that matter, any given entity can have multiple ports that represent
it, each implying different sets of permissible operations. For
example, many objects have a _name port_ and
a _control
port_ (sometimes called the privileged port).
Access to the control port allows the object to be manipulated;
access to the name port simply names the object so that you can
obtain information about it or perform other non-privileged operations
against it.

Tasks have permissions to access ports in certain ways (send,
receive, send-once); these are called _port rights_.
A port can be accessed only via a right. Ports are often used
to grant clients access to objects within Mach. Having the right
to send to the object’s IPC port denotes the right to manipulate
the object in prescribed ways. As such, port right ownership is
the fundamental security mechanism
within Mach. Having a right to an object is to have a capability
to access or manipulate that object.

Port rights can be copied and moved between tasks via IPC. Doing so,
in effect, passes capabilities to some object or server.

One type of object referred to by a port is a _port set_.
As the name suggests, a port set is a set of port rights that can
be treated as a single unit when receiving a message or event from
any of the members of the set. Port sets permit one thread to wait
on a number of message and event sources, for example in _work loops_.

Traditionally in Mach, the communication channel denoted by
a port was always a queue of _messages_.
However, OS X supports additional types of communication channels, and
these new types of IPC object are also represented by ports and
port rights. See the section [Interprocess Communication (IPC)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrqhewugrkhjjcusqkh),
for more details about messages and other IPC types.

Ports and port rights do not have systemwide names that allow
arbitrary ports or rights to be manipulated directly. Ports can
be manipulated by a task only if the task has a port right in its
port namespace. A port right is specified by a _port name_, an integer
index into a 32-bit port
namespace. Each task has associated with it a single port namespace.

Tasks acquire port rights when another task explicitly inserts
them into its namespace, when they receive rights in messages, by
creating objects that return a right to the object, and via Mach
calls for certain special ports (`mach_thread_self`, `mach_task_self`,
and `mach_reply_port`.)

As with most modern operating systems, Mach provides addressing
to large, sparse, virtual address spaces. Runtime access is made
via virtual addresses that may not correspond to locations in physical
memory at the initial time of the attempted access. Mach is responsible
for taking a requested virtual address and assigning it a corresponding
location in physical memory. It does so through demand paging.

A range of a virtual address space is populated with data
when a memory object is mapped into that range. All data in an address
space is ultimately provided through memory objects. Mach asks the
owner of a memory object (a _pager_)
for the contents of a page when establishing it in physical memory
and returns the possibly modified data to the pager before reclaiming
the page. OS X includes two built-in pagers—the _default
pager_ and the _vnode pager_.

The default pager handles nonpersistent memory, known as _anonymous
memory_. Anonymous memory is zero-initialized, and it exists
only during the life of a task. The vnode pager maps files into
memory objects. Mach exports an interface to memory objects to allow
their contents to be contributed by user-mode tasks. This interface
is known as the External Memory Management Interface, or _EMMI_.

The memory management subsystem exports virtual memory handles
known as _named entries_ or _named
memory entries_. Like most kernel resources, these are
denoted by ports. Having a named memory entry handle allows the
owner to map the underlying virtual memory object or to pass the
right to map the underlying object to others. Mapping a named entry
in two different tasks results in a shared memory window between
the two tasks, thus providing a flexible method for establishing
shared memory.

Beginning in OS X v10.1, the EMMI system
was enhanced to support “portless” EMMI. In traditional EMMI,
two Mach ports were created for each memory region, and likewise two
ports for each cached vnode. Portless EMMI, in its initial implementation,
replaces this with direct memory references (basically pointers).
In a future release, ports will be used for communication with pagers
outside the kernel, while using direct references for communication
with pagers that reside in kernel space. The net result of these
changes is that early versions of portless EMMI do not support pagers
running outside of kernel space. This support is expected to be
reinstated in a future release.

Address ranges of virtual memory space may also be populated
through direct allocation (using `vm_allocate`).
The underlying virtual memory object is anonymous and backed by the
default pager. Shared ranges of an address space may also be set
up via inheritance. When new tasks are created, they are cloned
from a parent. This cloning pertains to the underlying memory address
space as well. Mapped portions of objects may be inherited as a
copy, or as shared, or not at all, based on attributes associated
with the mappings. Mach practices a form of delayed copy known as _copy-on-write_ to
optimize the performance of inherited copies on task creation.

Rather than directly copying the range, a copy-on-write optimization is accomplished
by protected sharing. The two tasks share the memory to be copied,
but with read-only access. When either task attempts to modify a
portion of the range, that portion is copied at that time. This
lazy evaluation of memory copies is an important optimization that
permits simplifications in several areas, notably the messaging APIs.

One other form of sharing is provided by Mach, through the
export of _named
regions_. A named region is a form of a named entry, but
instead of being backed by a virtual memory object, it is backed
by a virtual map fragment. This fragment may hold mappings to numerous
virtual memory objects. It is mappable into other virtual maps,
providing a way of inheriting not only a group of virtual memory
objects but also their existing mapping relationships. This feature
offers significant optimization in task setup, for example when sharing
a complex region of the address space used for shared libraries.

Communication between tasks is an important element of the
Mach philosophy. Mach supports a client/server system structure
in which tasks (clients) access services by making requests of other
tasks (servers) via messages sent over a communication channel.

The endpoints of these communication channels in Mach are
called ports, while port rights denote permission to use the channel.
The forms of IPC provided by Mach include

- message
  queues
- semaphores
- notifications
- lock sets
- remote procedure calls (RPCs)

The type of IPC object denoted by the port determines the
operations permissible on that port, and how (and whether) data
transfer occurs.

There are two fundamentally different Mach APIs for raw manipulation
of ports—the `mach_ipc` family
and the `mach_msg` family.
Within reason, both families may be used with any IPC object; however,
the `mach_ipc` calls are
preferred in new code. The `mach_ipc` calls maintain
state information where appropriate in order to support the notion
of a transaction. The `mach_msg` calls
are supported for legacy code but deprecated; they are stateless.

When a thread calls `mach_ipc_dispatch`,
it repeatedly processes events coming in on the registered port
set. These events could be an argument block from an RPC
object (as the results of a client’s call), a lock object being
taken (as a result of some other thread’s releasing the lock),
a notification or semaphore being posted, or a message coming in
from a traditional message queue.

These events are handled via callouts from `mach_msg_dispatch`.
Some events imply a transaction during the lifetime of the callout.
In the case of a lock, the state is the ownership of the lock. When
the callout returns, the lock is released. In the case of remote
procedure calls, the state is the client’s identity, the argument
block, and the reply port. When the callout returns, the reply is
sent.

When the callout returns, the transaction (if any) is completed,
and the thread waits for the next event. The `mach_ipc_dispatch` facility
is intended to support work loops.

Originally, the sole style of interprocess communication in
Mach was the message
queue. Only one task can hold the receive right for a port denoting
a message queue. This one task is allowed to receive (read) messages
from the port queue. Multiple tasks can hold rights to the port
that allow them to send (write) messages into the queue.

A task communicates with another task by building a data structure
that contains a set of data elements and then performing a message-send
operation on a port for which it holds send rights. At some later
time, the task with receive rights to that port will perform a message-receive
operation.

A message may consist of some or all of the following:

- pure data
- copies of memory ranges
- port rights
- kernel implicit attributes, such as the sender’s security token

The message transfer is an asynchronous operation. The message
is logically copied into the receiving task, possibly with copy-on-write
optimizations. Multiple threads within the receiving task can be
attempting to receive messages from a given port, but only one thread can
receive any given message.

Semaphore IPC objects support wait, post, and post all operations.
These are counting semaphores, in that posts are saved (counted)
if there are no threads currently waiting in that semaphore’s
wait queue. A post all operation wakes up all currently waiting
threads.

Like semaphores, notification objects also support post and
wait operations, but with the addition of a state field. The state
is a fixed-size, fixed-format field that is defined when the notification
object is created. Each post updates the state field; there is a
single state that is overwritten by each post.

A lock is an object that provides mutually exclusive access
to a critical section. The primary interfaces to locks are transaction
oriented (see [IPC Transactions and Event Dispatching](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrqhewugrkhijbekqsg)). During the transaction,
the thread holds the lock. When it returns from the transaction,
the lock is released.

As the name implies, an RPC object is designed to facilitate
and optimize remote procedure calls. The primary interfaces to RPC
objects are transaction oriented (see [IPC Transactions and Event Dispatching](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrqhewugrkhijbekqsg))

When an RPC object is created, a set of argument block formats
is defined. When an RPC (a send on the object) is made by a client,
it causes a message in one of the predefined formats to be created
and queued on the object, then eventually passed to the server (the receiver).
When the server returns from the transaction, the reply is returned
to the sender. Mach tries to optimize the transaction by executing
the server using the client’s resources; this is called _thread
migration_.

The traditional abstraction of time in Mach is the clock, which provides a set
of asynchronous alarm services based on `mach_timespec_t`.
There are one or more clock objects, each defining a monotonically
increasing time value expressed in nanoseconds. The real-time clock
is built in, and is the most important, but there may be other clocks
for other notions of time in the system. Clocks support operations
to get the current time, sleep for a given period, set an alarm
(a notification that is sent at a given time), and so forth.

The `mach_timespec_t` API is deprecated
in OS X. The newer and preferred API is based on timer objects
that in turn use `AbsoluteTime` as
the basic data type. `AbsoluteTime` is
a machine-dependent type, typically based on the platform-native
time base. Routines are provided to convert `AbsoluteTime` values
to and from other data types, such as nanoseconds. Timer objects
support asynchronous, drift-free notification, cancellation, and
premature alarms. They are more efficient and permit higher resolution
than clocks.

[Next](Memory%20and%20Virtual%20Memory.md)[Previous](Kernel%20Programming%20Style.md)

