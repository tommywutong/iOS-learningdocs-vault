---
title: Porting Drivers to OS X
apple_id: TP30001169
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2009-05-06'
source_url: https://developer.apple.com/library/archive/documentation/Porting/Conceptual/PortingDrivers/unix-model/unix-model.html
archived_at: '2026-07-18T01:50:43.241034Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Porting Drivers to OS X](Introduction%20to%20Porting%20Drivers%20to%20OS%20X.md)


[Next](I-O%20Kit%20Considerations.md)[Previous](Introduction%20to%20Porting%20Drivers%20to%20OS%20X.md)

# Driver Porting Basics

This chapter describes some of the fundamental differences between traditional UNIX-style drivers (including BSD and Linux) and OS X’s I/O Kit drivers. As with any subject as broad as driver porting, there are many details that are specific to the technology area in question. This chapter does not attempt to cover such issues. Instead, it focuses on the more general issues, leaving the implementation details as an exercise for the reader.

This document primarily applies to in-kernel device drivers. Not all device drivers in OS X are in the kernel. For example, most human interface devices (keyboards, mice, and so on) and graphics and imaging devices (printers, scanners, and similar) are controlled by user-space drivers.

In general, your driver should be in the kernel if it is used concurrently across multiple applications or if its primary client is in the kernel. Examples include video drivers, disk or disk controller drivers, and so on.

There are a few cases where a driver has to reside in the kernel even though similar devices can reside in user space. In particular, any device on a PCI or AGP bus must be in the kernel because those busses do not export interfaces to user space for security reasons.

For the most part, PCI devices are things that need to be in the kernel anyway. There are a few exceptions, however, such as MIDI device drivers. While MIDI device drivers live in user space, PCI device drivers must reside in the kernel. Thus PCI cards with MIDI interfaces require two drivers: the actual I/O Kit driver for the device (subclassed from the PCI driver family) and a CFPlugIn in user space to provide a driver to CoreMIDI. Interfacing drivers across user-kernel boundaries is beyond the scope of this book. For help creating drivers that span user-kernel boundaries, you should contact Apple Developer Technical Support.

Before you actually start porting code, you should create a stub driver using the correct base class for your type of device. The _[I/O Kit Family Reference](https://developer.apple.com/documentation/kernel)_ provides documentation for each of these base classes.

In general, you will need to use two classes in your drivers: a base class (whose name typically ends with “driver”) and a nub class (whose name typically ends with “device”).

The base class instance will represent the driver itself. It must then instantiate an instance of the nub class for each device that it is controlling. This nub abstraction provides a mechanism for other parts of the system to actually use your driver to communicate with the device. The mechanism for instantiating this nub varies from class to class.

For detailed information on this process, you should read _[IOKit Fundamentals](../../Device%20Drivers/IOKit%20Fundamentals/Introduction%20to%20I-O%20Kit%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridambqgaydcmi)_ and follow the [Hello I/O Kit tutorial](https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/KEXTConcept/KEXTConceptIOKit/iokit_tutorial.html#//apple_ref/doc/uid/20002366).

Drivers in OS X are designed around the concept of a workloop. (Many drivers on other UNIX-based platforms are written in a similar fashion, but not as part of the primary driver model.)

The idea of a workloop is simple. It is basically just a helper thread. When an interrupt occurs, instead of a handler routine being executed immediately, the kernel sets that thread to “ready to execute”. Thus, the interrupt handling occurs at a kernel thread priority instead of at an interrupt priority. This ensures that interrupts don’t get lost while handling routines have interrupts turned off. It also means that routines running in an interrupt service thread context do not have to obey the same rules as an actual interrupt handler; they can block, call IOLog, and so on.

Creating a workloop is relatively simple. The following code is an example of registering to receive two interrupts using a workloop:

```swift
/* class variables */
IOWorkLoop *myWorkLoop;
IOInterruptEventSource *interruptSource;
IOInterruptEventSource *DMAInterruptSource;

/* code in start() */
myWorkLoop = IOWorkLoop::workLoop();

if( myWorkLoop == NULL) {    IOLog( "org_mklinux_iokit_swim3_driver::start: Couldn't allocate ”
        “workLoop event source\n" );
    return false;
}

interruptSource = IOInterruptEventSource::interruptEventSource(
    (OSObject*)this,
    (IOInterruptEventAction)&org_mklinux_iokit_swim3_driver::handleInterrupt,
    (Filter)&org_mklinux_iokit_swim3_driver::interruptPending,
    (IOService*)provider,
    (int)0 );

if ( interruptSource == NULL ) {
    IOLog( "org_mklinux_iokit_swim3_driver::start: Couldn't allocate “
        “Interrupt event source\n" );
    return false;
}

if ( myWorkLoop->addEventSource( interruptSource ) != kIOReturnSuccess ) {
    IOLog( "org_mklinux_iokit_swim3_driver::start - Couldn't add Interrupt”
        “event source\n" );    return false;}

DMAInterruptSource = IOInterruptEventSource::interruptEventSource(
    (OSObject*)this,
    (IOInterruptEventAction)&org_mklinux_iokit_swim3_driver::
        handleDMAInterrupt,    (IOService*)provider,    (int)1 );

if ( DMAInterruptSource == NULL ) {
    IOLog( "org_mklinux_iokit_swim3_driver::start: Couldn't allocate “
        “Interrupt event source\n" );
    return false;
    }

if ( myWorkLoop->addEventSource( DMAInterruptSource ) != kIOReturnSuccess )
    {
    IOLog( "org_mklinux_iokit_swim3_driver::start - Couldn't add “
        “Interrupt event source\n" );
    return false;
}

myWorkLoop->enableAllInterrupts();
```

The methods `handleInterrupt` and `handleDMAInterrupt` will now called for the first and second device interrupts (offsets 0 and 1), respectively.

For the most part, this interrupt handler will behave much like any interrupt handler would in any other OS (except that you can call `printf` and `IOLog` safely). However, there are some exceptions, particularly in the area of interrupt priority.

You should note that this source example uses `IOFilterInterruptEventSource` instead of `IOInterruptEventSource`. This is strongly recommended for two reasons. First, if you are writing a driver for a multifunction PCI card), this will avoid having the OS call all of the drivers for all of the devices on that card. Second, if your card is installed into an environment where an interrupt line gets shared, this will significantly improve performance.

Unlike `IOInterruptEventSource`, when you create an `IOFilterInterruptEventSource` object, you pass in a filter function in addition to the handler.

In the filter function (`org_mklinux_iokit_swim3_driver::interruptPending` in this example), you should test to see whether your device generated the interrupt, and return `true` if your driver should handle the interrupt or `false` if it belongs to another device on the card. This generally involves polling a register in your device to see which interrupt flags are set, then storing the value for later use. Note that because the filter function runs in the primary hardware interrupt context, you must treat it like any other direct hardware interrupt—don’t block, don’t call `IOLog`, don’t copy data around or allocate memory, and so on.

For more information, read _[IOKit Fundamentals](../../Device%20Drivers/IOKit%20Fundamentals/Introduction%20to%20I-O%20Kit%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridambqgaydcmi)_ and _[Kernel Programming Guide](../../Darwin/Kernel%20Programming%20Guide/About%20This%20Document.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbv)_.

For any given location in a computer’s memory, computer architectures define (at least) three distinct addresses: the physical address (the actual address line values as seen by the processor), the logical/virtual address (the address as seen by software), and the bus address (the address as seen by an arbitrary I/O device).

On most 32-bit hardware, the physical address is the same as the bus address. Thus, most people ignore the distinction. In OS X, you must treat them as two different things, particularly on 64-bit hardware. For this reason, using physical addresses obtained with kvtophys is unsafe, and the function kvtophys has actually been removed from availability to KEXTs to prevent its improper use.

Instead, you should use an `IOMemoryDescriptor` for your memory allocation so that you can obtain the bus address associated with the block of memory and hand that information to the peripheral.

To do this, you use the method `IOMemoryDescriptor::getPhysicalSegment`. The first argument is an offset from the beginning of the descriptor. The second is the address where the segment length should be stored. If the segment length returned is less than the total descriptor length (which you can obtain using the method `IOMemoryDescriptor::getLength`), then you must get the physical address of the next segment, and so on, until you have dealt with the entire descriptor.

For more information about the `IOMemoryDescriptor` class, see the I/O Kit reference documentation, available from Apple’s developer documentation website.

I/O Kit drivers are written in C++. Most device drivers in other operating systems are written in C. This often poses interesting issues, primarily related to the way driver-specific data is stored. It also can lead to a number of other surprises. These are described further in [C++ Language Considerations](C%2B%2B%20Language%20Considerations.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrzfvbuqmrqg4wviucykjcummjqgy).

Data types tend to be of different sizes in various driver models. to avoid any nasty surprises, you should always check the bit width of the various data types in the original OS, then explicitly use data types of the same width. For example, if type `int` on Linux is 32 bits, for maximum longevity, you should use the type `uint32_t` in OS X.

Suggested types are:

- `uint8_t`—unsigned 8-bit integer
- `uint16_t`—unsigned 16-bit integer
- `uint32_t`—unsigned 32-bit integer
- `uint64_t`—unsigned 64-bit integer
- `int8_t`—signed 8-bit integer
- `int16_t`—signed 16-bit integer
- `int32_t`—signed 32-bit integer
- `int64_t`—signed 64-bit integer

The definition for these types can be included in both user-space and kernel-space code with the following:

```c
#include <stdint.h>
```

You can also use the equivalent Mac-specific types, such as `UInt32`, which can be included with the following:

```c
#include <libkern/OSTypes.h>
```

A note of caution: boolean variables can be problematic as there is no standard rule about their size. Rather than use built-in boolean types, you should generally stick with an explicit integer of your choice of sizes to avoid inadvertent alignment differences between your C and C++ code.

OS X does not use `ioctl` support at the driver level. Instead, higher level driver families handle `ioctl` calls and turn them into explicit function calls. The details of these calls are dependent on the type of driver in question.

If the driver family you are using does not provide an `ioctl` that you need, you can either file a bug requesting that the `ioctl` be added or you can provide a similar solution through the use of a user client/device interface pair. These are described in more detail in the document _[IOKit Device Driver Design Guidelines](../../Device%20Drivers/IOKit%20Device%20Driver%20Design%20Guidelines/Introduction%20to%20I-O%20Kit%20Device%20Driver%20Design%20Guidelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmoju)_, available from the Apple Technical Publications website.

If none of these options is acceptable, you can also sometimes subclass the BSD user client for a particular class of devices (such as `IOMediaBSDClient`) and add additional `ioctl` support. For example, to add an ioctl for a particular type of media, you would need to override the following methods:

- `start`—determine if the media is of the desired type
- `ioctl`—handle the ioctl

A brief code snipped follows:

```swift
bool FloppyMediaBSDClient::start(IOService *provider)
{
    IOMedia * media = (IOMedia *) provider;
    u_int64_t size;
    IOStorage *storage;

    /* Make sure our provider’s start routine succeeds */
    if (super::start(provider) == false)
        return false;

    /* Make sure our provider is a block storage device */
    media = getProvider();
    storage = media->getProvider();
    this->driver = OSDynamicCast(IOBlockStorageDriver, storage);
    if (!this->driver)
        return false;

    /*
     * Determine if this is really the type of media we’re looking for,
     * in this case by its size. This could also be done using a more
     * specific OSDynamicCast if we are looking for a particular driver
     * to be upstream.
     */
    size = media->getSize() / (u_int64_t) 512;

    switch (size) {
    case 0: // unformatted
    case 720: // 360k
    case 800: // 400k
    case 1440: // 720k
    case 1600: // 800k
    case 2880: // 1440k
    case 2881: // 1440k also
    case 3360: // 1680k
    case 5760: // 2880k
        dIOLog("Floppy Disk Media Detected.\n");
        break;
    default:
        dIOLog("Non-floppy disk media detected: %ld\n", (unsigned long)size);
        return false;
    }
    return true;
}

int FloppyMediaBSDClient::ioctl (
    dev_t           dev,
    u_long          cmd,
    caddr_t         data,
    int             flags,
    struct proc *   proc )
{
    //
    // Process a Floppy-specific ioctl.
    //

    int *buffer;
    int error  = 0;
    IOReturn status = kIOReturnSuccess;
    int formatflags;

    switch(cmd) {
        case FD_VERIFY:
            buffer = NULL;
            break;
        case FD_FORMAT:
            buffer = (int *)data;
            if (!buffer) {
                dIOLog("ioctl (floppy): null buffer!\n");
                error=EINVAL;
                break;
            }
    }
    switch (cmd)
    {
        case FD_VERIFY:
        {
            IOLog("Got FD_VERIFY -- not supported yet.\n");
            error = ENOTTY;
            break;
        }
        case FD_FORMAT:
        {
            formatflags = *buffer;
            IOLog("Got FD_FORMAT -- not supported yet (flags = 0x%x).\n",
                formatflags);
            error = ENOTTY;
            break;
        }
    default:
        {
            //
            // A foreign ioctl was received.  Ask our superclass' opinion.
            //
            IOLog("fd: unknown ioctl, calling parent.\n");
            error = super::ioctl(dev, cmd, data, flags, proc);
            break;
        }
    }
return error; // (return error status)
}
```


Much like `ioctl` support, OS X drivers do not generally use `sysctl` or `syscall` interfaces except those provided by their respective families. Instead, user client/device interface pairs are used. These are described in more detail in the document _[IOKit Device Driver Design Guidelines](../../Device%20Drivers/IOKit%20Device%20Driver%20Design%20Guidelines/Introduction%20to%20I-O%20Kit%20Device%20Driver%20Design%20Guidelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmoju)_, available from the Apple Technical Publications website.

However, OS X does provide ways of adding additional `sysctl` and `syscall` support. This is described in detail in the document _[Kernel Programming Guide](../../Darwin/Kernel%20Programming%20Guide/About%20This%20Document.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbv)_.

Many UNIX-based driver models use interrupt priority levels as a means of protecting critical sections in drivers using functions like things like `splhigh`, `splbio`, and `splx`. Using interrupt priority to protect critical sections doesn’t work particularly well on SMP systems, and thus most operating systems are moving away from this design. However, these functions are still in common use.

OS X does not support the use of interrupt priority levels for disabling interrupts for critical section protection. Instead, you should use locks, semaphores, or other synchronization mechanisms. If you compile your code using these functions, the code may compile, but will either not work properly (because the function in question is a no-op) or will result in a kernel panic, depending on the functions used.

Instead of using these functions, you should generally use `IOLock` mutex lock. These are described in the _[I/O Kit Family Reference](https://developer.apple.com/documentation/kernel)_, and are briefly summarized below:

```
/*  Allocate an I/O Lock */
IOLock *IOLockAlloc( void );

/*  Free an I/O Lock */
void IOLockFree( IOLock * lock);

/*  Lock an I/O Lock */
static __inline__ void IOLockLock( IOLock * lock);

/*  Lock an I/O Lock if it doing so would not block. Returns true if
    lock was obtained. */
static __inline__boolean_t IOLockTryLock( IOLock * lock);

/*  Unlock an I/O Lock */
void IOLockUnlock( IOLock * lock);

/*  Wait on condition specified by event (where event is usually
    generated by taking the address of a variable, much like
    timeout/untimeout in BSD */
static __inline__ int IOLockSleep(
        IOLock * lock,
        void *event,
        UInt32 interType);

/*  Similar to IOLockSleep, only with a timeout specified */
static __inline__ int IOLockSleepDeadline(
        IOLock * lock,
        void *event,
        AbsoluteTime deadline,
        UInt32 interType);

/*  Wake up an event waiting on the condition specified by event
    The boolean oneThread specifies whether to signal on the condition
    (wake the first waiting thread) or broadcast (wake all threads
    that are waiting).
 */
static __inline__ void IOLockWakeup(IOLock * lock,
        void *event,
        bool oneThread);
```

If you find that you can’t live without a semaphore implementation, you can either implement one using an `IOLock` or use the Mach semaphores described in _[Kernel Programming Guide](../../Darwin/Kernel%20Programming%20Guide/About%20This%20Document.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbv)_. The former is strongly recommended, as binary compatibility is not guaranteed for KEXTs that use Mach directly.

[Next](I-O%20Kit%20Considerations.md)[Previous](Introduction%20to%20Porting%20Drivers%20to%20OS%20X.md)

