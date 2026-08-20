---
title: Kernel Programming Guide
apple_id: TP30000905
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2013-08-08'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/KernelProgramming/Glossary/Glossary.html
archived_at: '2026-07-15T07:23:11.555635Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Kernel Programming Guide](About%20This%20Document.md)


[Previous](Document%20Revision%20History.md)

# Glossary

- 
  __abstraction__

  (v)
  The process of separating the interface to some functionality from
  the underlying implementation in such a way that the implementation
  can be changed without changing the way that piece of code is used.
  (n) The API (interface) for some piece of functionality that has
  been separated in this way.

- __address space__

  The virtual address ranges available to a given
  task (note: the task may be the kernel). In OS X, processes
  do not share the same address space. The address spaces of multiple
  processes can, however, point to the same physical address ranges.
  This is referred to as shared memory.

- __anonymous
  memory__

  Virtual memory backed by
  the default pager to swap files, rather than by a persistent object.
  Anonymous memory is zero-initialized and exists only for the life
  of the task. See also [default pager](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugscejbdusssh); [task](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugsceineeor2b).

- __API (application programming
  interface)__

  The interface (calling
  convention) by which an application program accesses a service.
  This service may be provided by the operating system, by libraries,
  or by other parts of the application.

- __Apple Public Source License__

  Apple’s Open Source license, available at [http://www.apple.com/publicsource](http://www.apple.com/publicsource).
  Darwin is distributed under this license. See also [Open Source](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugscejbbeersc).

- __AppleTalk__

  A suite of network protocols that is standard
  on Macintosh computers.

- __ASCII (American Standard
  Code for Information Interchange)__

  A
  7-bit character set (commonly represented using 8 bits) that defines 128
  unique character codes. See also [Unicode](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugscejfdukskg).

- __BSD (Berkeley Software Distribution__

  Formerly known as the Berkeley version of UNIX,
  BSD is now simply called the BSD operating system. The BSD portion
  of the OS X kernel is based on FreeBSD, a version of BSD.

- __bundle__

  A directory that stores executable code and
  the software resources related to that code. Applications, plug-ins,
  and frameworks represent types of bundles. Except for frameworks,
  bundles are presented by the Finder as if they were a single file.

- __Carbon__

  An application environment in OS X that
  features a set of programming interfaces derived from earlier versions
  of the Mac OS. The Carbon APIs have been modified to work properly
  with OS X. Carbon applications can run in OS X, Mac OS 9,
  and all versions of Mac OS 8 later than Mac OS 8.1 (with appropriate
  libraries).

- __Classic__

  An application environment in OS X that
  lets users run non-Carbon legacy Mac OS software. It supports programs
  built for both Power PC and 68K processor architectures.

- __clock__

  An object used to abstract time in Mach.

- __Cocoa__

  An advanced object-oriented development platform
  on OS X. Cocoa is a set of frameworks with programming interfaces in
  both Java and Objective-C. It is based on the integration of OPENSTEP,
  Apple technologies, and Java.

- __condition variable__

  Essentially a wait queue with additional locking
  semantics. When a thread sleeps waiting for some event to occur,
  it releases a related lock so that another thread can cause that
  event to occur. When the second thread posts the event, the first
  thread wakes up, and, depending on the condition variable semantics
  used, either takes the lock immediately or begins waiting for the
  lock to become available.

- __console__

  (1) A text-based login environment that also
  displays system log messages, kernel panics, and other information.
  (2) A special window in OS X that displays messages that would
  be printed to the text console if the GUI were not in use. This
  window also displays output written to the standard error and standard
  output streams by applications launched from the Finder. (3) An
  application by the same name that displays the console window.

- __control
  port__

  In Mach, access to the
  control port allows an object to be manipulated. Also called the
  privileged port. See also [port](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugscei5eeiqsk); [name port](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugsceinceqr2k).

- __cooperative
  multitasking__

  A multitasking environment
  in which a running program can receive processing time only if other
  programs allow it; each application must give up control of the
  processor cooperatively in order to allow others to run. Mac OS
  9 is a cooperative multitasking environment. See also [preemptive multitasking](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugsceirduirkh).

- __copy-on-write__

  A delayed copy optimization used in Mach. The
  object to be copied is marked temporarily read-only. When a thread
  attempts to write to any page in that object, a trap occurs, and
  the kernel copies only the page or pages that are actually being
  modified. See also [thread](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugsceiveegssj).

- __daemon__

  A long-lived process, usually without a visible
  user interface, that performs a system-related service. Daemons
  are usually spawned automatically by the system and may either live
  forever or be regenerated at intervals. They may also be spawned
  by other daemons.

- __Darwin__

  The core of OS X, Darwin is an Open Source
  project that includes the Darwin kernel, the BSD commands and C
  libraries, and several additional features.The Darwin kernel is synonymous
  with the OS X kernel.

- __default
  pager__

  In Mach, one of the built-in pagers.
  The default pager handles nonpersistent (anonymous) memory. See
  also [anonymous memory](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugqsbi5ausski); [vnode pager](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugsceinducq2k); [pager](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugscejbbeuq2b).

- __demand paging__

  An operating-system facility that brings pages
  of data from disk into physical memory only as they are needed.

- __DLIL (Data Link Interface
  Layer)__

  The part of the OS X kernel’s networking infrastructure that provides the interface
  between protocol handling and network device drivers in the I/O Kit.
  A generalization of the BSD “ifnet” architecture.

- __DMA
  (direct memory access)__

  A means
  of transferring data between host memory and a peripheral device
  without requiring the host processor to move the data itself. This
  reduces processor overhead for I/O operations and may reduce contention
  on the processor bus.

- __driver__

  Software that deals with getting data to and
  from a device, as well as control of that device. In the I/O Kit,
  an object that manages a piece of hardware (a device), implementing
  the appropriate I/O Kit abstractions for that device. See also [object](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugscei5euoqsh).

- __DVD (Digital Versatile
  Disc)__

  Originally, Digital Video
  Disc. An optical storage medium that provides greater capacity and
  bandwidth than CD-ROM; DVDs are frequently used for multimedia as
  well as data storage.

- __dyld (dynamic link editor)__

  A utility that allows programs to dynamically
  load (and link to) needed functions.

- __EMMI
  (External Memory Management Interface)__

  Mach’s interface to memory objects that allows
  their contents to be contributed by user-mode tasks. See also [external pager](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugsceindegrsk).

- __Ethernet__

  A family of high-speed local area network technologies
  in common use. Some common variants include 802.3 and 802.11 (Airport).

- __exception__

  An interruption to the normal flow of program
  control, caused by the program itself or by executing an illegal
  instruction.

- __exception port__

  A Mach port on which a task or thread receives
  messages when exceptions occur.

- __external
  pager__

  A module that manages
  the relationship between virtual memory and a backing store. External
  pagers are clients of Mach’s EMMI. The pager API is currently
  not exported to user space. The built-in pagers in OS X are
  the default pager, the device pager, and the vnode pager. See also [EMMI (External Memory Management Interface)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugscejjbegrkc).

- __family__

  In the I/O Kit, a family defines a collection
  of software abstractions that are common to all devices of a particular
  category (for example, PCI, storage, USB). Families provide functionality
  and services to drivers. See also [driver](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugscejffeurkg).

- __FAT (file allocation
  table)__

  A data structure used
  in the MS-DOS file system. Also synonymous with the file system
  that uses it. The FAT file system is also used as part of Microsoft
  Windows and has been adopted for use inside devices such as digital
  cameras.

- __fat files__

  See [universal binaries](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwuer2cijeekqsf).

- __FIFO (first-in first-out)__

  A data processing scheme in which data is read
  in the order in which it was written, processes are run in the order
  in which they were scheduled, and so forth.

- __file descriptor__

  A per-process unique, nonnegative integer used
  to identify an open file (or socket).

- __firewall__

  Software (or a computer running such software)
  that prevents unauthorized access to a network by users outside
  of the network.

- __fixed-priority policy__

  In Mach, a scheduling policy in which threads
  execute for a certain quantum of time, and then are put at the end
  of the queue of threads of equal priority.

- __fork__

  (1) A stream of data that can be opened and
  accessed individually under a common filename. The Macintosh Standard
  and Extended file systems store a separate “data” fork and a “resource”
  fork as part of every file; data in each fork can be accessed and
  manipulated independently of the other. (2) In BSD, `fork` is
  a system call that creates a new process.

- __framework__

  A bundle containing a dynamic shared library
  and associated resources, including image files, header files, and documentation.
  Frameworks are often used to provide an abstraction for manipulating
  device driver families from applications.

- __FreeBSD__

  A variant of the BSD operating system. See [http://www.freebsd.org](http://www.freebsd.org/) for
  details.

- __gdb (GNU debugger)__

  `gdb` is
  a powerful, source-level debugger with a command-line interface. `gdb` is
  a popular Open Source debugger and is included with the OS X
  developer tools.

- __HFS (hierarchical file
  system)__

  The Mac OS Standard
  file system format, used to represent a collection of files as a
  hierarchy of directories (folders), each of which may contain either
  files or folders themselves.

- __HFS+__

  The Mac OS Extended file system format. This
  file system format was introduced as part of Mac OS 8.1, adding
  support for filenames longer than 31 characters, Unicode representation
  of file and directory names, and efficient operation on larger disks.

- __host__

  (1) The computer that is running (is host to)
  a particular program or service. The term is usually used to refer
  to a computer on a network. (2) In debugging, the computer that
  is running the debugger itself. In this context, the target is the
  machine running the application, kernel, or driver being debugged.

- __host processor__

  The microprocessor on which an application
  program resides. When an application is running, the host processor
  may call other, peripheral microprocessors, such as a digital signal
  processor, to perform specialized operations.

- __IDE (integrated development environment)__

  An application or set of tools that allows
  a programmer to write, compile, edit, and in some cases test and
  debug within an integrated, interactive environment.

- __inheritance attribute__

  In Mach, a value indicating the degree to which
  a parent process and its child process share pages in the parent process’s
  address space. A memory page can be inherited as copy-on-write,
  shared, or not at all.

- __in-line
  data__

  Data that’s included
  directly in a Mach message, rather than referred to by a pointer.
  See also [out-of-line data](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugscejjbukscf).

- __info plist__

  See [information property list](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugscejfcuorsh).

- __information
  property list__

  A special form
  of property list with predefined keys for specifying basic bundle
  attributes and information of interest, such as supported document
  types and offered services. See also [bundle](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugsceizfeqscf); [property list](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugsceizeuur2f).

- __interrupt
  service thread__

  A thread running
  in kernel space for handling I/O that is triggered by an interrupt,
  but does not run in an interrupt context. Also called an I/O service
  thread.

- __I/O (input/output)__

  The exchange of data between two parts of a
  computer system, usually between system memory and a peripheral device.

- __I/O Kit__

  Apple’s object-oriented I/O development model.
  The I/O Kit provides a framework for simplified driver development, supporting
  many families of devices. See also [family](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugsceivdecskj).

- __I/O service thread__

  See [interrupt service thread](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugsceizeukrcd).

- __IPC (interprocess communication)__

  The transfer of information between processes
  or between the kernel and a process.

- __IPL
  (interrupt priority level)__

  A
  means of basic synchronization on uniprocessor systems in traditional
  BSD systems, set using the `spl` macro. Interrupts
  with lower priority than the current IPL will not be acted upon
  until the IPL is lowered. In many parts of the kernel, changing the
  IPL in OS X is not useful as a means of synchronization. New
  use of `spl` macros is discouraged. See
  also [spl (set priority level)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugsceivceorsb).

- __KDP__

  The kernel shim used for communication with
  a remote debugger (`gdb`).

- __Kerberos__

  An authentication system based on symmetric
  key cryptography. Used in MIT Project Athena and adopted by the
  Open Software Foundation (OSF).

- __kernel__

  The complete OS X core operating-system
  environment that includes Mach, BSD, the I/O Kit, file systems,
  and networking components.

- __kernel
  crash__

  An unrecoverable system
  failure in the kernel caused by an illegal instruction, memory access
  exception, or other failure rather than explicitly triggered as
  in a panic. See also [panic](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwuer2cijfeusck).

- __kernel extension__

  See [KEXT (kernel extension)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugsceijdesrsk).

- __kernel mode__

  See [supervisor mode](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugsceiraugrkc).

- __kernel panic__

  See [panic](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwuer2cijfeusck).

- __kernel
  port__

  A Mach port whose receive
  right is held by the kernel. See also [task port](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugsceizdeusch); [thread port](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugscejjcegscf).

- __KEXT
  (kernel extension)__

  A bundle
  that extends the functionality of the kernel. The I/O Kit, File
  system, and Networking components are designed to allow and expect
  the creation and use of KEXTs.

- __KEXT binary__

  A file (or files) in Mach-O format, containing
  the actual binary code of a KEXT. A KEXT binary is the minimum unit
  of code that can be loaded into the kernel. Also called a kernel
  module or KMOD. See also [KEXT (kernel extension)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugsceijdesrsk); [Mach-O](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugsceivaukrsj).

- __key signing__

  In public key cryptography, to (electronically)
  state your trust that a public key really belongs to the person
  who claims to own it, and potentially that the person who claims
  to own it really is who he or she claims to be.

- __KMOD (kernel module)__

  See KEXT binary.

- __lock__

  A basic means of synchronizing multiple threads.
  Generally only one thread can “hold” a lock at any given time.
  While a thread is holding the lock, any other thread that tries
  to take it will wait, either by blocking or by spinning, depending
  on the nature of the lock. Some lock variants such as read-write
  locks allow multiple threads to hold a single lock under certain conditions.

- __Mach__

  The lowest level of the OS X kernel. Mach
  provides such basic services and abstractions as threads, tasks,
  ports, IPC, scheduling, physical and virtual address space management,
  VM, and timers.

- __Mach-O__

  Mach object file format. The preferred object
  file format for OS X.

- __Mach server__

  A task that provides services to clients, using
  a MIG-generated RPC interface. See also [MIG (Mach interface generator)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugsceivdecrce).

- __main thread__

  By default, a process has one thread, the main
  thread. If a process has multiple threads, the main thread is the
  first thread in the process. A user process can use the POSIX thread API
  to create other user threads.

- __makefile__

  A makefile details the files, dependencies,
  and rules by which an executable application is built.

- __memory-mapped files__

  A facility that maps virtual memory onto a
  physical file. Thereafter, any access to that part of virtual memory
  causes the corresponding page of the physical file to be accessed.
  The contents of the file can be changed by changing the contents
  in memory.

- __memory object__

  An object managed by a pager that represents
  the memory, file, or other storage that backs a VM object. See also [pager](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugscejbbeuq2b).

- __memory
  protection__

  A system of memory management
  in which programs are prevented from being able to modify or corrupt
  the memory partition of another program, usually through the use
  of separate address spaces.

- __message__

  A unit of data sent by one task or thread that
  is guaranteed to be delivered atomically to another task or thread.
  In Mach, a message consists of a header and a variable-length body.
  Some system services are invoked by passing a message from a thread
  to the Mach port representing the task that provides the desired
  service.

- __microkernel__

  A kernel implementing a minimal set of abstractions.
  Typically, higher-level OS services such as file systems and device
  drivers are implemented in layers above a microkernel, possibly
  in trusted user-mode servers. OS X is a hybrid between microkernel
  and monolithic kernel architectures. See also [monolithic kernel](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugscejjfekssc).

- __MIG
  (Mach interface generator)__

  (1)
  A family of software that generates and supports the use of a procedure
  call interface to Mach’s system of interprocess communication.
  (2) The interface description language supported by MIG.

- __monolithic
  kernel__

  A kernel architecture
  in which all pieces of the kernel are closely intertwined. A monolithic
  kernel provides substantial performance improvements. It is difficult
  to evolve the individual components independently, however. The
  OS X kernel is a hybrid of the monolithic and microkernel models.
  See also [microkernel](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugscejbbumski).

- __multicast__

  A process in which a single packet can be addressed
  to multiple recipients. Multicast is used, for example, in streaming video,
  in which many megabytes of data are sent over the network.

- __multihoming__

  The ability to have multiple network addresses
  in one computer, usually on different networks. For example, multihoming might
  be used to create a system in which one address is used to talk
  to hosts outside a firewall and the other to talk to hosts inside;
  the computer provides facilities for passing information between
  the two.

- __multitasking__

  The concurrent execution of multiple programs.
  OS X uses preemptive multitasking. Mac OS 9 uses cooperative multitasking.

- __mutex__

  See [mutex lock (mutual exclusion lock)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugqsbjfeeoskj).

- __mutex
  lock (mutual exclusion lock)__

  A
  type of lock characterized by putting waiting threads to sleep until
  the lock is available.

- __named (memory) entry__

  A handle (a port) to a mappable object backed
  by a memory manager. The object can be a region or a memory object.

- __name
  port__

  In Mach, access to the
  name port allows non-privileged operations against an object (for
  example, obtaining information about the object). In effect, it
  provides a name for the object without providing any significant
  access to the object. See also [port](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugscei5eeiqsk); [control port](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugscejfbegrkd).

- __named region__

  In Mach, a form of named memory entry that
  provides a form of memory sharing.

- __namespace__

  An agreed-upon context in which names (identifiers)
  can be defined. Within a given namespace, all names must be unique.

- __NAT (network address
  translation)__

  A scheme that transforms
  network packets at a gateway so network addresses that are valid
  on one side of the gateway are translated into addresses that are
  valid on the other side.

- __network__

  A group of hosts that can communicate with
  each other.

- __NFS (network file system)__

  A commonly used file server protocol often
  found in UNIX and UNIX-based environments.

- __NKE (network kernel extension)__

  A type of KEXT that provides a way to extend
  and modify the networking infrastructure of OS X dynamically
  without recompiling or relinking the kernel.

- __NMI (nonmaskable interrupt)__

  An interrupt produced by a particular keyboard
  sequence or button that cannot be blocked in software. It can be
  used to interrupt a hung system, for example to drop into a debugger.

- __nonsimple
  message__

  In Mach, a message that contains
  either a reference to a port or a pointer to data. See also [simple message](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugsceivduessk).

- __notify port__

  A special Mach port that is part of a task.
  A task’s notify port receives messages from the kernel advising
  the task of changes in port access rights and of the status of messages
  it has sent.

- __nub__

  An I/O Kit object that represents a point of
  connection for a device or logical service. Each nub provides access
  to the device or service it represents, and provides such services
  as matching, arbitration, and power management. It is most common
  that a driver publishes one nub for each individual device or service
  it controls; it is possible for a driver that vends only a single
  device or service to act as its own nub.

- __NVRAM (nonvolatile RAM)__

  RAM storage that retains its state even when
  the power is off. See also [RAM (random-access memory)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugsceizbusr2k).

- __object__

  (1) A collection of data. (2) In Mach, a collection
  of data, with permissions and ownership. (3) In object-oriented
  programming, an instance of a class.

- __OHCI (Open Host Controller
  Interface)__

  The register-level
  standards that are used by most USB and Firewire controller chips.

- __Open
  Source__

  Software that includes
  freely available access to source code, redistribution, modification,
  and derived works. The full definition is available at [http://www.opensource.org](http://www.opensource.org/).

- __Open Transport__

  A communications architecture for implementing
  network protocols and other communication features on computers
  running classic Mac OS. Open Transport provides a set of programming interfaces
  that supports, among other things, both the AppleTalk and TCP/IP
  protocols.

- __out-of-line
  data__

  Data that’s passed by reference
  in a Mach message, rather than being included in the message. See
  also [in-line data](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugsceijdegqkk).

- __packet__

  An individual piece of information sent on
  a network.

- __page__

  (n) (1) The largest block of virtual address space
  for which the underlying physical address space is guaranteed contiguous—in
  other words, the unit of mapping between virtual and physical addresses.
  (2) logical page size: The minimum unit of information that an anonymous
  pager transfers between system memory and the backing store. (3)
  physical page size: The unit of information treated as a unit by a
  hardware MMU. The logical page size must be at least as large as
  the physical page size for hardware-based memory protection to be possible.
  (v) To move data between memory and a backing store.

- __pager__

  A module responsible for providing the data
  for the pages of a memory object. See also [default pager](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugscejbdusssh); [vnode pager](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugsceinducq2k).

- __panic__

  An unrecoverable system failure explicitly
  triggered by the kernel with a call to `panic`.
  See also [kernel crash](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwuer2cjjbumssk).

- __PEF (Preferred Executable
  Format)__

  The format of executable
  files used for applications and shared libraries in Mac OS 9; supported
  in OS X. The preferred format for OS X is [Mach-O](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugsceivaukrsj).

- __physical
  address__

  An address to which
  a hardware device, such as a memory chip, can directly respond.
  Programs, including the Mach kernel, use virtual addresses that
  are translated to physical addresses by mapping hardware controlled
  by the Mach kernel.

- __pmap__

  Part of Mach VM that provides an abstract way
  to set and fetch virtual to physical mappings from hardware. The
  pmap system is the machine-dependent layer of the VM system.

- __port__

  In Mach, a secure unidirectional channel for
  communication between tasks running on a single system. In IP transport
  protocols, an integer identifier used to select a receiving service
  for an incoming packet, or to specify the sender of an outgoing
  packet.

- __port
  name__

  In Mach, an integer index
  into a port namespace; a port right is specified with respect to
  its port name. See also [port rights](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugscejbaumq2g).

- __port
  rights__

  In Mach, the ability
  to send to or receive from a Mach port. Also known as port access
  rights.

- __port set__

  In Mach, a set of zero or more Mach ports.
  A thread can receive messages sent to any of the ports contained
  in a port set by specifying the port set as a parameter to `msg_receive()`.

- __POSIX
  (Portable Operating System Interface)__

  A standard that defines a set of operating-system
  services. It is supported by ISO/IEC, IEEE, and The Open Group.

- __preemption__

  The act of interrupting a currently running
  program in order to give time to another task.

- __preemptive
  multitasking__

  A type of multitasking
  in which the operating system can interrupt a currently running
  task in order to run another task, as needed. See also [cooperative multitasking](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugscei5euessf).

- __priority__

  In scheduling, a number that indicates how
  likely a thread is to run. The higher the thread’s priority, the
  more likely the thread is to run. See also [scheduling policy](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugsceireuuqsg).

- __process__

  A BSD abstraction for a running program. A
  process’s resources include an address space, threads, and file
  descriptors. In OS X, a process is based on one Mach task and
  one or more Mach threads.

- __process identifier (PID),__

  A number that uniquely identifies a process.
  Also called a process ID.

- __programmed I/O__

  I/O in which the CPU accomplishes data transfer
  with explicit load and store instructions to device registers, rather than
  DMA, and without the use of interrupts. This data transfer is often
  done in a byte-by-byte, or word-by-word fashion. Also known as direct or
  polled I/O. See also [DMA (direct memory access)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugsceircegrkb).

- __property
  list__

  A textual way to represent
  data. Elements of the property list represent data of certain types,
  such as arrays, dictionaries, and strings. System routines allow
  programs to read property lists into memory and convert the textual
  data representation into “real” data. See also [information property list](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugscejfcuorsh).

- __protected memory__

  See [memory protection](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugscei5auiqkg).

- __protocol handler__

  A network module that extracts data from input
  packets (giving the data to interested programs) and inserts data
  into output packets (giving the output packet to the appropriate
  network device driver).

- __pthreads__

  The POSIX threads implementation. See also [POSIX (Portable Operating System Interface)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugscejbceir2j); [thread](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugsceiveegssj).

- __quantum__

  The fixed amount of time a thread or process
  can run before being preempted.

- __RAM
  (random-access memory)__

  Memory
  that a microprocessor can either read from or write to.

- __real-time performance__

  Performance characterized by guaranteed worst-case response
  times. Real-time support is important for applications such as multimedia.

- __receive
  rights__

  In Mach, the ability
  to receive messages on a Mach port. Only one task at a time can
  have receive rights for any one port. See also [send rights](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugsceiraueqsf).

- __remote procedure call__

  See [RPC (remote procedure call)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwuer2cjjcuerke).

- __reply port__

  A Mach port associated with a thread that is
  used in remote procedure calls.

- __ROM (read-only memory)__

  Memory that cannot be written to.

- __root__

  (1) An administrative account with special privileges.
  For example, only the root account can load kernel extensions.(2)
  In graph theory, the base of a tree. (3) root directory: The base
  of a file system tree. (4) root file system: The primary file system
  off which a computer boots, so named because it includes the root
  node of the file system tree.

- __routine__

  In Mach, a remote procedure call that returns
  a value. This can be used for synchronous or asynchronous operations.
  See also [simpleroutine](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwuer2cireemrcg).

- __RPC
  (remote procedure call)__

  An interface
  to IPC that appears (to the caller) as an ordinary function call.
  In Mach, RPCs are implemented using MIG-generated interface libraries
  and Mach messages.

- __scheduling__

  The determination of when each process or task
  runs, including assignment of start times.

- __scheduling
  policy__

  In Mach, how the thread’s priority
  is set and under what circumstances the thread runs. See also [priority](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugscejbdesq2d).

- __SCSI (Small Computer
  Systems Interface)__

  A standard
  communications protocol used for connecting devices such as disk
  drives to computers. Also, a family of physical bus designs and
  connectors commonly used to carry SCSI communication.

- __semaphore__

  Similar to a lock, except that a finite number
  of threads can be holding a semaphore at the same time. See also [lock](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugscejjdeuskk).

- __send
  rights__

  In Mach, the ability
  to send messages to a Mach port. Many tasks can have send rights
  for the same port. See also [receive rights](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugscei5bumrsd).

- __session key__

  In cryptography, a temporary key that is only
  used for one message, one connection session, or similar. Session
  keys are generally treated as shared secrets, and are frequently
  exchanged over a channel encrypted using public key cryptography.

- __shadow object__

  In Mach VM, a memory object that holds modified
  pages that originally belonged to another memory object. This is
  used when an object that was duplicated in a copy-on-write fashion
  is modified. If a page is not found in this shadow object, the original object
  is referenced.

- __simple
  message__

  In Mach, a message that contains
  neither references to ports nor pointers to data. See also [nonsimple message](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugsceizeucq2e).

- __simpleroutine__

  In Mach, a remote procedure call that does
  not return a value, and has no `out` or `inout` parameters.
  This can be used for asynchronous operations. See also [routine](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwuer2ci5eeiqsd).

- __SMP
  (symmetric multiprocessing)__

  A
  system architecture in which two or more processors are managed
  by one kernel, share the same memory, have equal access to I/O devices,
  and in which any task, including kernel tasks, can run on any processor.

- __spinlock__

  Any of a family of lock types characterized
  by continuously polling to see if a lock is available, rather than
  putting the waiting thread to sleep.

- __spin/sleep lock__

  Any of a family of lock types characterized
  by some combination of the behaviors of spinlocks and mutex (sleep)
  locks.

- __spl
  (set priority level)__

  A macro
  that sets the current IPL. Interrupts with lower priority than the
  current IPL will not be acted upon until the IPL is lowered. The `spl` macros
  have no effect in many parts of OS X, so their use is discouraged
  as a means of synchronization in new programming except when modifying
  code that already uses `spl` macros.
  See also [IPL (interrupt priority level)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugscejfauiqsd).

- __socket__

  (1) In a user process, a file descriptor that
  has been allocated using `socket(2)`.
  (2) In the kernel, the data structure allocated when the kernel’s
  implementation of the `socket(2)` call
  is made. (3) In AppleTalk protocols, a socket serves the same purpose
  as a port in IP transport protocols.

- __submap__

  A collection of mappings in the VM system that
  is shared among multiple Mach tasks.

- __supervisor
  mode__

  Also known as kernel mode, the
  processor mode in which certain privileged instructions can be executed,
  including those related to page table management, cache management,
  clock setting, and so on.

- __symmetric multiprocessing__

  See [SMP (symmetric multiprocessing)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwuer2ci5fecscg).

- __task__

  A Mach abstraction, consisting of a virtual address
  space and a port namespace. A task itself performs no computation;
  rather, it is the framework in which threads run. See also [thread](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugsceiveegssj).

- __task
  port__

  A kernel port that represents
  a task and is used to manipulate that task. See also [kernel port](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugsceireeisci); [thread port](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugscejjcegscf).

- __TCP/IP (Transmission
  Control Protocol/Internet Protocol)__

  An industry standard protocol used to deliver
  messages between computers over the network. TCP/IP is the primary
  networking protocol used in OS X.

- __thread__

  The unit of program execution. A thread consists
  of a program counter, a set of registers, and a stack pointer. See
  also [task](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugsceineeor2b).

- __thread
  port__

  A kernel port that represents
  a thread and is used to manipulate that thread. See also [kernel port](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugsceireeisci); [task port](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugsceizdeusch).

- __thread-safe code__

  Code that can be executed safely by multiple
  threads simultaneously.

- __time-sharing policy__

  In Mach, a scheduling policy in which a thread’s
  priority is raised and lowered to balance its resource consumption against
  other timesharing threads.

- __UDF (Universal Disk Format)__

  The file system format used in DVD disks.

- __UFS (UNIX file system)__

  An industry standard file system format used
  in UNIX and similar operating systems such as BSD. UFS in OS X
  is a derivative of 4.4BSD UFS.

- __Unicode__

  A 16-bit character set that defines unique
  character codes for characters in a wide range of languages. Unlike
  ASCII, which defines 128 distinct characters typically represented
  in 8 bits, there are as many as 65,536 distinct Unicode characters
  that represent the unique characters used in most foreign languages.

- __universal
  binaries__

  Executable files containing object
  code for more than one machine architecture.

- __UPL (universal page list)__

  A data structure used when communicating with
  the virtual memory system. UPLs can be used to change the behavior
  of pages with respect to caching, permissions, mapping, and so on.

- __USB (Universal Serial
  Bus)__

  A multiplatform bus standard
  that can support up to 127 peripheral devices, including printers,
  digital cameras, keyboards and mice, and storage devices.

- __UTF-8 (Unicode Transformation
  Format 8)__

  A format used to represent
  a sequence of 16-bit Unicode characters with an equivalent sequence of
  8-bit characters, none of which are zero. This sequence of characters
  can be represented using an ordinary C language string.

- __VFS (virtual file system)__

  A set of standard internal file-system interfaces
  and utilities that facilitate support for additional file systems.
  VFS provides an infrastructure for file systems built into the kernel.

- __virtual address__

  An address as viewed from the perspective of
  an application. Each task has its own range of virtual addresses,
  beginning at address zero. The Mach VM system makes the CPU hardware
  map these addresses onto physical memory. See also [physical address](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugscejfdegssb).

- __virtual
  memory__

  A system in which addresses as
  seen by software are not the same as addresses seen by the hardware.
  This provides support for memory protection, reduces the need for
  code relocatability, and allows the operating system to provide
  the illusion to each application that it has resources much larger
  than those that could actually be backed by RAM.

- __VM__

  See [virtual memory](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugscejfaumrcf).

- __vnode__

  An in-memory data structure containing information
  about a file.

- __vnode
  pager__

  In Mach, one of the built-in pagers.
  The vnode pager maps files into memory objects. See also [default pager](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugscejbdusssh); [pager](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgqwugscejbbeuq2b).

- __work loop__

  The main loop of an application or KEXT that
  waits repeatedly for incoming events and dispatches them.

- __XML (Extensible Markup
  Language)__

  A dialect of SGML
  (Standard Generalized Markup Language), XML provides a metalanguage containing
  rules for constructing specialized markup languages. XML users can
  create their own tags, making XML very flexible.

[Previous](Document%20Revision%20History.md)

