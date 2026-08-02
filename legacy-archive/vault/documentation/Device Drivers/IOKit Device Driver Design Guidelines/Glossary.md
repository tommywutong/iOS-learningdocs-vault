---
title: IOKit Device Driver Design Guidelines
apple_id: TP30000694
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2009-08-14'
source_url: https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/WritingDeviceDriver/Glossary/Glossary.html
archived_at: '2026-07-15T07:31:49.292299Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [IOKit Device Driver Design Guidelines](Introduction%20to%20I-O%20Kit%20Device%20Driver%20Design%20Guidelines.md)


[Next](Document%20Revision%20History.md)[Previous](Developing%20a%20Device%20Driver%20to%20Run%20on%20an%20Intel-Based%20Macintosh.md)

# Glossary

- __base class__

  In C++, the class from which another class (a subclass) inherits. It can also be used to specify a class from which all classes in a hierarchy ultimately derive (also known as a root class).

- __BSD__

  Berkeley Software Distribution. Formerly known as the Berkeley version of UNIX, BSD is now simply called the BSD operating system. The BSD portion of Darwin is based on 4.4BSD Lite 2 and FreeBSD, a flavor of 4.4BSD.

- __bundle__

  A directory in the file system that typically stores executable code and the software resources related to that code. (A bundle can store only resources.) Applications, plug-ins, frameworks, and kernel extensions are types of bundles. Except for frameworks, bundles are file packages, presented by the Finder as a single file instead of folder. See also [kernel extension](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydombtfvbuuqskinduosa)

- __CFM__

  Code Fragment Manager, the library manager and code loader for processes based on PEF (Preferred Executable Format) object files (Carbon).

- __client__

  A driver object that consumes services of some kind supplied by its provider. In a driver stack, the client in a provider/client relationship is farther away from the Platform Expert. See also [provider](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydombtfvbuuqseizdussq).

- __command gate__

  A mechanism that controls access to the lock of a work loop, thereby serializing access to the data involved in I/O requests. A command gate does not require a thread context switch to ensure single-threaded access. IOCommandGate event-source objects represent command gates in the I/O Kit.

- __cross-boundary I/O__

  The transport of data across the boundary between the kernel and user space. In OS X, cross-boundary I/O can be performed using I/O Kit family device interfaces, POSIX APIs, I/O Registry properties, or custom user clients.

- __Darwin__

  Another name for the OS X core operating system, or kernel environment. The Darwin kernel environment is equivalent to the OS X kernel plus the BSD libraries and commands essential to the BSD Commands environment. Darwin is Open Source technology.

- __DMA__

  (Direct Memory Access) A capability of some bus architectures that enables a bus controller to transfer data directly between a device (such as a disk drive) and a device with physically addressable memory, such as that on a computer's motherboard. The microprocessor is freed from involvement with the data transfer, thus speeding up overall computer operation.

- __device__

  Computer hardware, typically excluding the CPU and system memory, which can be controlled and can send and receive data. Examples of devices include monitors, disk drives, buses, and keyboards.

- __device driver__

  A component of an operating system that deals with getting data to and from a device, as well as the control of that device. A driver written with the I/O Kit is an object that implements the appropriate I/O Kit abstractions for controlling hardware.

- __device file__

  In BSD, a device file is a special file located in `/dev` that represents a block or character device such as a terminal, disk drive, or printer. If a program knows the name of a device file, it can use POSIX functions to access and control the associated device. The program can obtain the device name (which is not persistent across reboots or device removal) from the I/O Kit.

- __device interface__

  In I/O Kit, an mechanism that uses a plug-in architecture to allow a program in user space to communicate with a nub in the kernel that is appropriate to the type of device the program wishes to control. Through the nub the program gains access to I/O Kit services and to the device itself. From the perspective of the kernel, the device interface appears as a driver object called a [user client](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydombtfvbuuqsjizdukqi).

- __device matching__

  In I/O Kit, a process by which an application finds an appropriate device to load. The application calls a special I/O Kit function that uses a “matching dictionary” to search the I/O Registry. The function returns one or more matching driver objects that the application can then use to load an appropriate device interface. Also referred to as device discovery.

- __driver__

  See [device driver](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydombtfvbuuqsii5deiri).

- __driver matching__

  In I/O Kit, a process in which a nub, after discovering a specific hardware device, searches for the driver or drivers most suited to that device. Matching requires that a driver have one or more personalities that specify whether it is a candidate for a particular device. Driver matching is a subtractive process involving three phases: class matching, passive matching, and active matching. See also [personality](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydombtfvbuuqsiircueqy).

- __driver stack__

  In an I/O connection, the series of driver objects (drivers and nubs) in client/provider relationships with each other. A driver stack often refers to the entire collection of software between a device and its client application (or applications).

- __event source__

  An I/O object that corresponds to a type of event that a device driver can be expected to handle; there are currently event sources for hardware interrupts, timer events, and I/O commands. The I/O Kit defines a class for each of these event types, respectively IOInterruptEventSource, IOTimerEventSource, and IOCommandGate.

- __family__

  A collection of software abstractions that are common to all devices of a particular category. Families provide functionality and services to drivers. Examples of families include protocol families (such as SCSI, USB, and Firewire), storage families (disk drives), network families, and families that describe human interface devices (mouse and keyboard).

- __framework__

  A type of bundle that packages a dynamic shared library with the resources that the library requires, including header files and reference documentation.

  Note that the Kernel framework (which contains the I/O Kit headers) contains no dynamic shared library. All library-type linking for the Kernel framework is done using the `mach_kernel` file itself and kernel extensions. This linking is actually static (with vtable patch-ups) in implementation

- __gdb__

  gdb is the GNU Debugger, a powerful source-level debugger with a command-line interface. Used in conjunction with kdp to perform two-machine debugging. See also [kdp](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydombtfvbuuqsgjbeuqqi).

- __host computer__

  Also called the development computer, the host computer runs the debugger in a two-machine debugging scenario. Most often, the host computer is also the computer on which the KEXT is being developed. See also [two-machine debugging](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydombtfvbuuqscifeuuri); [target computer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydombtfvbuuqsdijbugri).

- __information property list__

  A property list that contains essential configuration information for bundles such as kernel extensions. A file named `Info.plist` (or a platform-specific variant of that filename) contains the information property list and is packaged inside the bundle.

- __internationalization__

  The design or modification of a software product, including online help and documentation, to facilitate localization. Internationalization of software typically involves writing or modifying code to make use of locale-aware operating-system services for appropriate localized text input, display, formatting, and manipulation. See also [localization](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydombtfvbuuqsijfcecra).

- __interrupt__

  An asynchronous event that suspends the currently scheduled process and temporarily diverts the flow of control through an interrupt handler routine. Interrupts can be caused by both hardware (I/O, timer, machine check) and software (supervisor, system call, or trap instruction).

- __interrupt handler__

  A routine executed when an interrupt occurs. Interrupt handlers typically deal with low-level events in the hardware of a computer system, such as a character arriving at a serial port or a tick of a real-time clock.

- __I/O Kit__

  A kernel-resident, object-oriented environment in Darwin that provides a model of system hardware. Each type of service or device is represented by one or more C++ classes in a family; each available service or device is represented by an instance (object) of that class.

- __I/O Kit framework__

  The framework that includes IOKitLib and makes the I/O Registry, user client plug-ins, and other I/O Kit services available from user space.It lets applications and other user processes access common I/O Kit object types and services. See also [framework](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydombtfvbuuqsjireugsq).

- __kdp__

  (Kernel Debugger Protocol) The kernel shim used for communication with a remote debugger. See also [gdb](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydombtfvbuuqseirbuesi).

- __I/O Registry__

  A dynamic database that describes a collection of driver objects, each of which represents an I/O Kit entity. As hardware is added to or removed from the system, the registry changes to accommodate the addition or removal.

- __kernel__

  The complete OS X core operating-system environment, which includes Mach, BSD, the I/O Kit, drivers, file systems, and networking components. The kernel resides in its own protected memory partition. The kernel includes all code executed in the kernel task, which consists of the file `mach_kernel` (at file-system root) and all loaded kernel extensions. Also called the kernel environment.

- __kernel extension__

  (KEXT) A dynamically loaded bundle that extends the functionality of the kernel. A KEXT can contain zero or one kernel modules as well as other (sub) KEXTs, each of which can contain zero or one kernel modules. The I/O Kit, file system, and networking components of Darwin can be extended by KEXTs. See also [kernel module](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydombtfvbuuqsfi5ceesi).

- __kernel module__

  (KMOD) A binary in Mach-O format that is packaged in a kernel extension. A KMOD is the minimum unit of code that can be loaded into the kernel. See also [kernel extension](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydombtfvbuuqskinduosa).

- __localization__

  The adaptation of a software product, including online help and documentation, for use in one or more regions of the world, in addition to the region for which the original product was created. Localization of software can include translation of user-interface text, resizing of text-related graphical elements, and replacement or modification of user-interface images and sound. See also [internationalization](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydombtfvbuuqseifduery).

- __lock__

  A data structure used to synchronize access to a shared resource. The most common use for a lock is in multithreaded programs where multiple threads need access to global data. Only one thread can hold the lock at a time; by convention, this thread is the only one that can modify the data during this period.

- __Mach__

  A central component of the kernel that provides such basic services and abstractions as threads, tasks, ports, interprocess communication (IPC), scheduling, physical and virtual address space management, virtual memory, and timers.

- __Mach-O__

  The Mach object file format. Mach-O is the preferred object file format for OS X. See also [PEF](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydombtfvbuuqsjjfeumsi).

- __map__

  To translate a range of memory in one address space (physical or virtual) to a range in another address space. The virtual-memory manager accomplishes this by adjusting its VM tables for the kernel and user processes.

- __matching__

  See [device matching](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydombtfvbuuqscirceqqq) and [driver matching](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydombtfvbuuqsdivduqqi).

- __memory descriptor__

  An object that describes how a stream of data, depending on direction, should either be laid into memory or extracted from memory. It represents a segment of memory holding the data involved in an I/O transfer and is specified as one or more physical or virtual address ranges. The object is derived from the IOMemoryDescriptor class. See also [DMA](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydombtfvbuuqsejbfeerq).

- __memory leak__

  A bug in a program that prevents it from freeing discarded memory and causes it to use increasing amounts of memory. A KEXT that experiences a memory leak may not be able to unload.

- __memory protection__

  A system of memory management in which programs are prevented from being able to modify or corrupt the memory partition of another program. Although OS X has memory protection, Mac OS 8 and 9 do not.

- __NMI__

  (Nonmaskable interrupt) An interrupt produced by a particular keyboard sequence or button. It can be used to interrupt a hung system and, in two-machine debugging, drop into the debugger.

- __notification__

  A programmatic mechanism for alerting interested recipients (sometimes called observers) that an event has occurred.

- __nub__

  An I/O Kit object that represents a detected, controllable entity such as a device or logical service. A nub may represent a bus, disk, graphics adaptor, or any number of similar entities. A nub supports dynamic configuration by providing a bridge between two drivers (and, by extension, between two families). See also [device](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydombtfvbuuqscizaucrq); [driver](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydombtfvbuuqsjircecqq).

- __nvram__

  (Nonvolatile RAM) RAM storage that retains its state even when the power is off.

- __page__

  (1) The smallest unit (in bytes) of information that the virtual memory system can transfer between physical memory and backing store. In Darwin, a page is currently 4 kilobytes. (2) As a verb, page refers to the transfer of pages between physical memory and backing store. Refer to `Kernel.framework/Headers/mach/machine/vm_params.h` for specifics. See also [virtual memory](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydombtfvbuuqsfizfessa).

- __panic__

  An unrecoverable system failure detected by the kernel.

- __PEF__

  Preferred Executable Format. An executable format understood by the Code Fragment Manager (CFM). See also [Mach-O](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydombtfvbuuqseizeuksi).

- __personality__

  A set of properties specifying the kinds of devices a driver can support. This information is stored in an XML matching dictionary defined in the information property list (`Info.plist`) in the driver’s KEXT bundle. A single driver may present one or more personalities for matching; each personality specifies a class to instantiate. Such instances are passed a reference to the personality dictionary at initialization.

- __physical memory__

  Electronic circuitry contained in random-access memory (RAM) chips, used to temporarily hold information at execution time. Addresses in a process’s virtual memory are mapped to addresses in physical memory. See also [virtual memory](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydombtfvbuuqsfizfessa).

- __PIO__

  (Programmed Input/Output) A way to move data between a device and system memory in which each byte is transferred under control of the host processor. See also [DMA](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydombtfvbuuqsejbfeerq).

- __plane__

  A subset of driver (or service) objects in the I/O Registry that have a certain type of provider/client relationship connecting them. The most general plane is the Service plane, which displays the objects in the same hierarchy in which they are attached during Registry construction. There are also the Audio, Power, Device Tree, FireWire, and USB planes.

- __Platform Expert__

  A driver object for a particular motherboard that knows the type of platform the system is running on. The Platform Expert serves as the root of the I/O Registry tree.

- __plug-in__

  An module that can be dynamically added to a a running system or application. Core Foundation Plug-in Services uses the basic code-loading facility of Core Foundation Bundle Services to provide a standard plug-in architecture, known as the CFPlugIn architecture, for Mac OS applications. A kernel extension is a type of kernel plug-in.

- __policy maker__

  A power-management object that decides when to change the power state of a device and instructs the power controller for the device to carry out this change. A policy maker uses factors such as device idleness and aggressiveness to make its decision. See also [power controller](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydombtfvbuuqsgijeemsi).

- __port__

  A heavily overloaded term which in Darwin has two particular meanings: (1) In Mach, a secure unidirectional channel for communication between tasks running on a single system; (2) In IP transport protocols, an integer identifier used to select a receiver for an incoming packet or to specify the sender of an outgoing packet.

- __POSIX__

  The Portable Operating System Interface. An operating-system interface standardization effort supported by ISO/IEC, IEEE, and The Open Group.

- __power controller__

  A power-management object that knows about the various power states of a device and can switch the device between them. A power controller changes the power state of a device only upon instruction from its policy maker. See also [policy maker](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydombtfvbuuqsiineeusa).

- __power domain__

  A switchable source of power in a system, providing power for one or more devices that are considered members of the domain. Power domains are nested hierarchically, with the root power domain controlling power to the entire system.

- __probe__

  A phase of active matching in which a candidate driver communicates with a device and verifies whether it can drive it. The driver’s `probe` member function is invoked to kick off this phase. The driver returns a probe score that reflects its ability to drive the device. See also [driver matching](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydombtfvbuuqsdivduqqi).

- __process__

  A BSD abstraction for a running program. A process’s resources include a virtual address space, threads, and file descriptors. In OS X, a process is based on one Mach task and one or more Mach threads.

- __provider__

  A driver object that provides services of some kind to its client. In a driver stack, the provider in a provider/client relationship is closer to the Platform Expert. See also [client](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydombtfvbuuqseindemra).

- __release__

  Decrementing the reference count of an object. When an object’s reference count reaches zero, it is freed. When your code no longer needs to reference a retained object, it should release it. Some APIs automatically execute a release on the caller’s behalf, particularly in cases where the object in question is being “handed off.” Retains and releases must be carefully balanced; too many releases can cause panics and other unexpected failures due to accesses of freed memory. See also [retain](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydombtfvbuuqskjjeuusa).

- __retain__

  Incrementing the reference count of an object. An object with a positive reference count is not freed. (A newly created object has a reference count of one.) Drivers can ensure the persistence of an object beyond the present scope by retaining it. Many APIs automatically execute a retain on the caller’s behalf, particularly APIs used to create or gain access to objects. Retains and releases must be carefully balanced; too many retains will result in wired memory leak. See also [release](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydombtfvbuuqscirfeesi).

- __scheduler__

  That part of Mach that determines when each program (or program thread) runs, including assignment of start times. The priority of a program’s thread can affect its scheduling. See also [task](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydombtfvbuuqsgi5cuqra); [thread](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydombtfvbuuqsdjbduusi).

- __service__

  A service is an I/O Kit entity, based on a subclass of IOService, that has been published with the `registerService` method and provides certain capabilities to other I/O Kit objects. In the I/O Kit’s layered architecture, each layer is a client of the layer below it and a provider of services to the layer above it. A service type is identified by a matching dictionary that describes properties of the service. A nub or driver can provide services to other I/O Kit objects.

- __target computer__

  In two-machine debugging, the computer on which the KEXT being debugged is run. The target computer must have a copy of the KEXT being debugged. See also [two-machine debugging](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydombtfvbuuqscifeuuri); [host computer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydombtfvbuuqsjindecqi).

- __task__

  A Mach abstraction consisting of a virtual address space and a port name space. A task itself performs no computation; rather, it is the context in which threads run. See also [process](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydombtfvbuuqsdjjeueqi); [thread](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydombtfvbuuqsdjbduusi).

- __thread__

  In Mach, the unit of CPU utilization. A thread consists of a program counter, a set of registers, and a stack pointer. See also [task](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydombtfvbuuqsgi5cuqra).

- __timer__

  A kernel resource that triggers an event at a specified interval. The event can occur only once or can be recurring. A timer is an example of an event source for a work loop.

- __two-machine debugging__

  A debugging process in which one computer (the host) runs the debugger (often gdb) and another computer (the target) runs the program being debugged. Debugging KEXTs requires two-machine debugging because a buggy KEXT will often panic the system, making it impossible to run the debugger on that computer. See also [host computer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydombtfvbuuqsjindecqi); [target computer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydombtfvbuuqsdijbugri).

- __user client__

  An interface provided by an I/O Kit family, that enables a user process (which can’t call a kernel-resident driver or other service directly) to access hardware. In the kernel, this interface appears as a driver object called a user client; in user space, it is called a device interface and is implemented as a Core Foundation Plug-in Services (CFPlugin) object. See also [device interface](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydombtfvbuuqsgincecry).

- __user space__

  Virtual memory outside the protected partition in which the kernel resides. Applications, plug-ins, and other types of modules typically run in user space.

- __virtual address__

  A memory address that is usable by software. Each task has its own range of virtual addresses, which begins at address zero. The Mach operating system makes the CPU hardware map these addresses onto physical memory only when necessary, using disk memory at other times.

- __virtual memory__

  The use of a disk partition or a file on disk to provide the same facilities usually provided by RAM. The virtual-memory manger in OS X provides 32-bit (minimum) protected address space for each task and facilitates efficient sharing of that address space.

- __virtual table__

  Often called a vtable, a virtual table is a structure in the header of every class object that contains pointers to the methods the class implements.

- __vram__

  (Video RAM) A special form of RAM used to store image data for a computer display. Vram can be accessed for screen updates at the same time the video processor is providing new data.

- __wired memory__

  A range of memory that the virtual-memory system will not page out or move. The memory involved in an I/O transfer must be wired down to prevent the physical relocation of data being accessed by hardware. In the I/O kit memory is wired when the memory descriptor describing the memory prepares the memory for I/O (which happens when its `prepare` method is invoked).

- __work loop__

  A gating mechanism that ensures single-threaded access to the data structures and hardware registers used by a driver. A work loop typically has several event sources attached to it; they use the work loop to ensure a protected, gated context for processing events. See also [event source](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydombtfvbuuqsejfbukra).

- __XML__

  (Extensible Markup Language) A simplified dialect of SGML (Standard Generalized Markup Language) that provides a metalanguage containing rules for constructing specialized markup languages.

[Next](Document%20Revision%20History.md)[Previous](Developing%20a%20Device%20Driver%20to%20Run%20on%20an%20Intel-Based%20Macintosh.md)

