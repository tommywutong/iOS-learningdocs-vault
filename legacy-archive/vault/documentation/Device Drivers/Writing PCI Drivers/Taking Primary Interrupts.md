---
title: Writing PCI Drivers
apple_id: TP40000975
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2006-04-04'
source_url: https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/WritingPCIDrivers/interrupts/interrupts.html
archived_at: '2026-07-15T07:31:53.129870Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Writing PCI Drivers](About%20This%20Book.md)


[Next](Endianness%20and%20Addressing.md)[Previous](Writing%20a%20Driver%20for%20an%20AGP%20Device.md)

# Taking Primary Interrupts

Most device drivers never need to take primary interrupts because their interrupt lines don’t cascade into the system’s interrupt controller. For example, FireWire and USB devices have a notion of interrupts, but are really just messages on a serial bus. These are commonly referred to as software interrupts because apart from the interrupt caused by the message itself, the interrupt is entirely simulated in software.

PCI devices, however, are supported by hardware interrupts. A physical line runs between the PCI slot and the PCI controller, which routes that line to an interrupt input on the interrupt controller, which presents the value of that line as a bit value in a register and raises the processor’s interrupt line.

You can take a hardware interrupt in two ways: directly via an interrupt handler (primary interrupt) and indirectly via an interrupt service thread (secondary interrupt). The second method is strongly preferred, as it avoids generating excessive interrupt latency for other devices on the system. However, the first method can be used to guarantee low latency operation when necessary.

Open Firmware automatically assigns interrupts to PCI devices. Typically a PCI device has only a single interrupt, but it is possible to have PCI devices that generate more than one interrupt (for example, a device interrupt and a DMA interrupt).

In any case, all of the interrupts used by the device are listed in an array as part of the device’s I/O Registry entry. Like a C array, the first interrupt is at offset 0, the second at offset 1, and so on.

When registering to receive an interrupt, you must specify the offset into the interrupt list for the interrupt you want to receive. If you need to receive notification for multiple interrupts, you must enable them each individually.

In the unlikely event that Open Firmware should fail to allocate interrupts correctly for your device, you should contact Apple Developer Technical Support for assistance, as correcting problems with interrupt allocation is beyond the scope of this book.

Interrupt latency refers to the amount of time between when an interrupt is triggered and when the interrupt is seen by software. This can be caused by many factors. Some of these include:

- other drivers keeping interrupts disabled for a long period
- blocking in the interrupt service thread
- scheduling latency (waiting for the interrupt service thread to be scheduled)
- interrupt service thread priority (particularly for non-kernel drivers)

If you are writing device drivers, it is your responsibility to avoid causing too much latency for other devices in the system. In extreme cases, it is possible to actually cause interrupts to be dropped by leaving interrupts turned off for too long. This can cause system instability, and in some machines, can actually cause the computer to spontaneously power down by causing a PMU synchronization failure.

The best way to avoid such problems is to use interrupt service threads. This is the preferred way to service interrupts. However, if your driver is well-behaved and doesn’t spend huge amounts of time copying data, it is also possible to write reasonable device drivers that operate directly in an interrupt context. This is briefly discussed in [Taking Interrupts Directly](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydqnjqfvbuqrcgjfeuesi).

Interrupt service threads are the standard way of handling interrupts in OS X device drivers, though they often go by another name, the work loop.

A work loop is a thread whose sole purpose is to wait for an event such as an interrupt to occur, then call an appropriate handler function to do the actual work of processing the interrupt—checking the result, copying data, and so on. This activity occurs in a kernel thread.

The kernel thread does not receive the actual interrupt, however. A low-level interrupt handler receives the primary interrupt. It then generates a software interrupt known as a secondary interrupt. The interrupt service thread receives that secondary software interrupt. Thus, routines running in an interrupt service thread do not have to obey the same rules as an actual interrupt handler; they can block, call `IOLog`, and so on.

The following code is an example of registering to receive two (secondary) interrupts using a work loop:

```swift
/* class variables */
IOWorkLoop *myWorkLoop;
IOFilterInterruptEventSource *interruptSource;
IOFilterInterruptEventSource *DMAInterruptSource;

/* code in start() */
myWorkLoop = IOWorkLoop::workLoop();

if( myWorkLoop == NULL) {
    IOLog( "org_mklinux_iokit_swim3_driver::start: Couldn't "
        allocate workloop event source\n");
    return false;
}

interruptSource = IOFilterInterruptEventSource::filterInterruptEventSource(
    (OSObject*)this,
    (IOInterruptEventAction)&org_mklinux_iokit_swim3_driver::handleInterrupt,
    (Filter)&org_mklinux_iokit_swim3_driver::filterInterrupt,
    (IOService*)provider,
    (int)0 );

if ( interruptSource == NULL ) {
    IOLog( "org_mklinux_iokit_swim3_driver::start: Couldn't"
        "allocate Interrupt event source\n" );
    return false;
}

if ( myWorkLoop->addEventSource( interruptSource ) != kIOReturnSuccess ) {
    IOLog( "org_mklinux_iokit_swim3_driver::start - Couldn't add Interrupt"
        "event source\n" );    return false;}

DMAInterruptSource = IOFilterInterruptEventSource::
    filterInterruptEventSource(
        (OSObject*)this,
        (IOInterruptEventAction)&org_mklinux_iokit_swim3_driver::
            handleDMAInterrupt,
        (Filter)&org_mklinux_iokit_swim3_driver::filterDMAInterrupt
        (IOService*)provider,        (int)1 );

if ( DMAInterruptSource == NULL ) {
    IOLog( "org_mklinux_iokit_swim3_driver::start: Couldn't"
        "allocate Interrupt event source\n" );
    return false;
    }

if ( myWorkLoop->addEventSource( DMAInterruptSource ) != kIOReturnSuccess )
    {
    IOLog( "org_mklinux_iokit_swim3_driver::start - Couldn't add "
        "Interrupt event source\n" );
    return false;
}

myWorkLoop->enableAllInterrupts();
```

The methods `handleInterrupt` and `handleDMAInterrupt` will now be called for the first and second device interrupts (offsets 0 and 1), respectively.

Notice the methods `filterInterrupt` and `filterDMAInterrupt`. These methods are called upon receipt of a hardware interrupt, and should do the minimum amount of work necessary to determine whether an interrupt belongs to your driver or not.

This use of interrupt filters is strongly recommended over `IOInterruptEventSource` to ensure that your driver performs as well as possible should your device end up sharing an interrupt with another device. If you do not write a filter function, the system will have to call each driver that registers for a given shared interrupt one-by-one, resulting in unpleasant latency for all drivers involved.

If the interrupt belongs to your device, the filter method should return `true`. Otherwise it should return `false`. Because the two interrupts (device and DMA) above could, in theory, be shared on the same interrupt line, additional care should be taken to determine the nature of the interrupt, and to return `true` only for the right kind of interrupt—that is, `filterInterrupt` should return `true`_only_ for a device interrupt, and `filterDMAInterrupt` should return `true`_only_ for a DMA interrupt.

If your interrupt filter returns `true`, your interrupt handler routine will be started on your work loop automatically by the I/O Kit. The interrupt will remain disabled in hardware until your interrupt service routine completes.

In some cases, such as pseudo-DMA, this behavior may not be what you want. For this reason, you may elect to have your filter routine schedule the work on the work loop itself, then return `false`. If you do this, the interrupt will not be disabled in hardware, and thus, you could receive additional primary interrupts before your work-loop–level service routine completes. Because this method has implications on synchronization between your filter routine and interrupt service routine, you should generally avoid doing this unless your driver requires pseudo-DMA.

For additional information, consult the document _[IOKit Fundamentals](../IOKit%20Fundamentals/Introduction%20to%20I-O%20Kit%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridambqgaydcmi)_ and the `IOFilterInterruptEventSource` class documentation in the device drivers API reference, available from the Apple Developer Documentation website.

This method is generally not advisable, as it can cause undesirable behavior including high interrupt latency for other drivers, audio stuttering, lost interrupts, and even erratic overall system behavior.

However, if you need exceptionally low latency for certain specialty devices, it may be necessary to take primary interrupts directly. You should remember that drivers that take primary interrupts must not block in their handler routines, which means that many calls are not allowed, including `IOLog`.

You can register a handler for a raw interrupt in one of two ways: using an `IOFilterInterruptEventSource` or by using `registerInterrupt`.

If you are sharing an interrupt between multiple devices, you should use an `IOFilterInterruptEventSource` handler.

If you are writing a driver whose interrupt handler must run partially in a raw interrupt context, you can use `registerInterrupt`. You should _only_ consider doing processing that is _extremely_ fast in a primary interrupt context. In general, if the amount of work done takes less time than a context switch, it is acceptable to do it in a primary interrupt context.

Regardless, you should do _only_ the low-latency portions in an interrupt context and defer any heavy lifting to an interrupt service thread.

For information on IOFilterInterruptEventSource, see [Interrupts via Interrupt Service Threads](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydqnjqfvkfawcsivddcmbz).

Taking a primary interrupt in this fashion is dangerous. You should not ever do this unless you have determined that it is impossible to get adequate latency using a secondary interrupt handler. Before proceeding, you should contact Apple Developer Technical Support for guidance.

When working in the primary interrupt context, nearly all calls are unsafe. Even things like `IOLog` can block, and blocking in a primary interrupt context will result in a kernel panic (since it would otherwise result in an unexplained hang). Only Mach simple locks (spinlocks) are safe in this context, since they disappear in a uniprocessor environment.

You should be extremely careful to avoid keeping interrupts turned off for an extended period of time. For example, multi-millisecond polling, delays, and copying large amounts of data are not acceptable in a primary interrupt context. Such activity should always be deferred to an interrupt service thread.

With those caveats in mind, the sample code below shows how to register a handler for a primary (hardware) interrupt directly without using work loops. The first example shows how to register a C++ class member function. The second example shows how to register an ordinary C function.

```swift
provider->registerInterrupt(0, this,
        OSMemberFunctionCast(IOInterruptAction, this,
            &MyClass::handleInterrupt), 0);
provider->enableInterrupt(0);
provider->registerInterrupt(1, this,
        (IOInterruptAction) &handleDMAInterrupt, 0);
provider->enableInterrupt(1);
```

As with the previous example, when the first interrupt (offset 0) occurs, the function `handleInterrupt` will be called, and when the second interrupt (offset 1) occurs, the function `handleDMAInterrupt` will be called.

[Next](Endianness%20and%20Addressing.md)[Previous](Writing%20a%20Driver%20for%20an%20AGP%20Device.md)

