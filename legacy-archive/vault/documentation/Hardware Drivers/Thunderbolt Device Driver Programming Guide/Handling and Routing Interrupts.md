---
title: Thunderbolt Device Driver Programming Guide
apple_id: TP40011138
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: null
published: '2013-10-22'
source_url: https://developer.apple.com/library/archive/documentation/HardwareDrivers/Conceptual/ThunderboltDevGuide/Basics02/Basics02.html
archived_at: '2026-07-15T07:41:11.916443Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Thunderbolt Device Driver Programming Guide](About%20the%20Thunderbolt%20Technology.md)


[Next](Debugging%20Thunderbolt%20Drivers.md)[Previous](Working%20with%20Thunderbolt%20Technology.md)

# Handling and Routing Interrupts

This chapter provides guidelines to help you support Thunderbolt devices using Message Signaled Interrupts (MSI) and to understand how to respond to hardware devices that do not support MSI. There is also a section on hot plug operations with PCI Devices that describes how to change PCI drivers so that they are able to deal with unplanned disconnections.

Most modern PCI devices support flexibility when dealing with interrupt routing. With the advent of PCI-X (PCI eXtended) and PCIe (PCI Express), Message Signaled Interrupts were introduced as an in-band mechanism for asserting interrupts.

Apple strongly recommends building only MSI-capable Thunderbolt devices. Ensure your OS X drivers enable MSI when supporting Thunderbolt devices. To ease development, the Mac Pro computers have PCIe slots that support MSI.

OS X services all interrupts on CPU 0 and uses the secondary interrupt context threads to defer work to task-level interrupts rather than primary-interrupt levels. This method ensures that multiple drivers can run in parallel on the available CPUs, that the OS can schedule real-time threads with accuracy, and that the system remains responsive to user interaction. The best practice methods, described in _[IOKit Fundamentals](../../Device%20Drivers/IOKit%20Fundamentals/Introduction%20to%20I-O%20Kit%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridambqgaydcmi)_, encourage the use of the IOWorkLoop abstraction model for device drivers in order to defer work to the IOWorkLoop thread. There may be a small number of devices that require work to be done in the primary interrupt context, however, drivers should spend the least amount of time possible in the primary-interrupt context.

The hardware should support MSI, but in the unlikely event the hardware device does not support MSI, the following three scenarios are most likely to occur. These three scenarios usually occur in the driver’s filter routine and it is important to understand the ramifications of the results returned from the filter routine:

1. __The filter is called, but the device has not signaled an interrupt.__

   This may be due to another device sharing the same interrupt pin. The filter routine should return `false`.
2. __The filter is called and the device has signaled an interrupt.__

   The driver cannot mask the interrupt source, nor can it handle the interrupt at this level for locking or performance reasons. The filter routine should return `true`.
3. __The filter is called and the device has signaled an interrupt.__

   1. The driver can handle the interrupt at this level and return the device to a non interrupting state. If the interrupt action needs to be run, the filter routine should call `signalInterrupt()`.
   2. The driver cannot handle the interrupt at this level, but it can prevent the device from signaling another interrupt (for example, by manipulating an internal mask).

      The filter routine should prevent the device from signaling another interrupt and then call `signalInterrupt()` to cause the interrupt action to be run. The interrupt action should handle the interrupt and return the device to a state where it can again signal an interrupt. The filter routine should return `false`.

Apple provides developers with tools that can track primary interrupt times and help developers to minimize the time needed for primary interrupts.

To enable MSI, a device driver should do the following, assuming that the provider is an `IOPCIDevice` instance:

__Listing 3-1__  Enabling MSIs

```swift
int    index  = 0;
int    source = 0;
for ( index = 0; ; index++ )
{
         IOReturn result      = kIOReturnSuccess;
         int interruptType    = 0;

         result = provider->getInterruptType ( index, &interruptType );
         if ( result != kIOReturnSuccess )
               break;
         if ( interruptType & kIOInterruptTypePCIMessaged )
        {
            source = index;
            break;
        }
}
```


PCI device drivers are typically developed with the expectation that the device will not be removed from the PCI bus during its operation. However, Thunderbolt technology allows PCI data to be tunneled through a Thunderbolt connection, and the Thunderbolt cables may be unplugged from the host or device at any time. Therefore, the system must be able to cope with the removal of PCI devices by the user at any time.

The user may freely unplug Thunderbolt devices at any time, with the exception of storage devices, and should be able to sleep and wake the system with devices attached without causing any problems. For all devices, the user must not be able to hang the system (computer) by unplugging a device or cable.

The PCI device drivers used with Thunderbolt devices may need to be updated in order to handle surprise or unplanned removal. In particular, MMIO cycles and PCI Configuration accesses require special attention. When a PCI device that is connected to a Thunderbolt port is detached from the system, the PCIe Root Port must time out any outstanding transactions sent to the device, terminate the transaction as though an Unsupported Request occurred on the bus, and return a value of `0xFFFFFFFF`. The Root Port has a completion timeout value that is many milliseconds long and varies depending on the system layout. Real-time scheduling, particularly for audio and video threads, can be affected by transactions that must be timed out.

As a basic guideline, developers should modify their drivers to handle a return value of `0xFFFFFFFF`. If any thread, callback, interrupt filter, or code path in a driver receives `0xFFFFFFFF` indicating the device has been unplugged, then all threads, callbacks, interrupt filters, interrupt handlers, and other code paths in that driver must cease MMIO reads and writes immediately and prepare for termination.

If `0xFFFFFFFF` is a legal value for a particular register offset, one additional read of a different register, which is known to never return `0xFFFFFFFF` is the preferred mechanism for determining if the device is still connected. Finally, if I/O Kit has already performed termination and called the driver’s `willTerminate()` method, no further accesses should be performed.

Once it has been determined that a device is no longer connected, do not try to clean up or reset the hardware as attempts to communicate with the hardware may lead to further delays.

Apple recommends auditing usage of MMIO writes when no further access should be performed. MMIO writes are posted transactions and it is possible for device drivers to queue up multiple writes in a row.

A typical way for a developer to solve this problem is to provide a single bottleneck routine for all MMIO reads and have that routine check the status of the device before beginning the actual transaction. An example of such a routine using little endian fields for its memory mapped apertures follows:

__Listing 3-2__  Single Bottleneck Routine (MMIO Read/Write)

```
class AppleSamplePCI
{
      ...
      bool                     fDeviceRemoved;
      volatile unit8_t *       fBaseAddressRegister;
      ...
      unit32_t        ReadRegister ( uint32_t  offset );
      virtual bool    willTerminate ( IOService * provider, IOOptionBits options );
};

unit32_t
AppleSamplePCI::ReadRegister ( unint32_t offset )
{

         unint32_t   result = 0xFFFFFFFF;

         if  ( !fDeviceRemoved )
         {
                result = OSReadLittleInt32 ( fBaseAddressRegister, offset );
                if ( result == 0xFFFFFFFF )
                    fDeviceRemoved = true;
         }
         return result;
}

bool
AppleSamplePCI::willTerminate ( IOService * provider, IOOptionBits options )
{
         fDeviceRemoved = true;
         return super::willTerminate ( provider, options );
}
```

Similar routines can be written for PCI Configuration cycle transactions, which may receive a return value of `0xFFFFFFFF` and MMIO reads of smaller sizes.

Because Thunderbolt allows the addition and removal of arbitrary numbers of peripherals connected in arbitrary topologies, the task of dividing up the PCI tree’s address space can be challenging. Sometimes, particularly when large numbers of devices are attached, it is possible to exhaust portions of that address space. When this happens, a new device cannot be enabled without moving existing devices.

To solve this problem, OS X v10.9 supports PCIe Pause—a special power management state in which all driver and device operations are temporarily suspended. Whenever address space exhaustion occurs, OS X may ask drivers to pause operations. After the drivers are paused, OS X changes the address space layout of the paused devices to make room for new devices, and then tells the drivers to resume normal operation.

To support pause, you must add an additional `Info.plist` key and a new power management state (`kIOPCIDevicePausedState`) to your driver, as described in the following sections.

To declare support for pausing, add the following key to each of the personalities in your driver’s `Info.plist` file:

```
<key>IOPCIPauseCompatible</key>
<true/>
```


When a driver for a `IOPCIDevice` provider registers for power management, it must provide a set of power state definitions indicating which of its power states should be used for each power state of the `IOPCIDevice` object itself. The `inputPowerRequirement` field of these power states is matched against masks of the PCI power state’s `outputPowerCharacter` field.

If you do not add any power states to your driver, your driver is put into its off state during pause, because the pause state does not include the [kIOPMPowerOn](https://developer.apple.com/documentation/kernel/1645009-anonymous/kiopmpoweron) flag. Any clients of the driver in the power management hierarchy then must change their states to match.

Modified drivers can support pause explicitly by adding a power state with the `kIOPMConfigRetained` flag set in the `inputPowerRequirement` field, causing that state to be selected by the power management system when the device needs to enter a paused state. The `outputPowerCharacter` value of the driver’s new power state then dictates what the driver’s power management clients see. Depending on this flag, clients of your driver may or may not change states.

For example, your power state table might look like this:

```
static const IOPMPowerState powerStates[kYourDriverPowerStateCount] = {

    // version, capabilityFlags, outputPowerCharacter,
    // inputPowerRequirement, staticPower, unbudgetedPower
    // powerToAttain timeToAttain settleUpTime
    // timeToLower settleDownTime powerDomainBudget

    // Device off; inputPowerRequirement is 0,
    // which matches the flags for kIOPCIDeviceOffState.
    { kIOPMPowerStateVersion1, 0, 0,
      0, 0, 0,
      0, 0, 0,
      0, 0, 0 },

    // Sleep mode; inputPowerRequirement has kIOPMSoftSleep flag set,
    // which matches the flags for kIOPCIDeviceDozeState.
    { kIOPMPowerStateVersion1, 0, kIOPMSoftSleep,
      kIOPMSoftSleep, 0, 0,
      0, 0, 0,
      0, 0, 0 },

    // Device paused; inputPowerRequirement has kIOPMConfigRetained flag set,
    // which matches the flags for kIOPCIDevicePausedState.
    { kIOPMPowerStateVersion1, kIOPMConfigRetained, kIOPMConfigRetained,
      kIOPMConfigRetained, 0, 0,
      0, 0, 0,
      0, 0, 0 },

    // Device active; inputPowerRequirement has kIOPMPowerOn flag set,
    // which matches the flags for kIOPCIDeviceOnState.
    { kIOPMPowerStateVersion1, kIOPMPowerOn | kIOPMUsable, kIOPMPowerOn,
      kIOPMPowerOn, 0, 0,
      0, 0, 0,
      0, 0, 0 }
};
```

To avoid disrupting service, write your code in a way that makes entering and exiting the pause state as fast as possible. In particular, you do not need to run all of the code that you would use for a `kIOPCIDeviceOffState`/`kIOPCIDeviceOnState` transition, because the device remains powered on through the state transition, making a full reinitialization unnecessary.

However, when OS X tells your driver to pause, your driver should still do many of the things that it would do when the computer goes into safe sleep—that is, it should tell the device to stop issuing additional transactions and then wait until all outstanding transactions have finished before telling OS X that the device’s power state has changed.

While the driver is paused:

- The driver should not access the device using memory-mapped I/O or configuration space transactions
- The device should not generate any interrupts, whether MSI or pin-based interrupts
- The device should not generate any DMA requests
- The device should not be the target of any DMA requests

When a driver is resumed after a pause, the driver should act as though the computer just woke from safe sleep, but without performing any unnecessary hardware initialization (because the device remained powered). In particular, it must determine whether the device has changed addresses, and if it has, it must use the new physical addresses for all future communication with the device. The following values may have changed:

- The device’s base address registers (BARs)
- The device’s bus number
- Registry properties reflecting these values: `"ranges"`, `"assigned-addresses"`, and `"reg"`
- The device’s MSI capability register block values for address and value, but not the number of MSIs allocated

The following values will _not_ change:

- The PCI power management configuration block registers of the device—that is, the device will _not_ be put into a device sleep state (runtime D3)
- The virtual addresses of the BARs

  Any mappings previously created by the driver with `IOPCIDevice::mapDeviceMemoryWithRegister` or `IOPCIDevice::mapDeviceMemoryWithIndex` for memory-mapped I/O access to hardware are automatically remapped with the same virtual address and the new physical address
- Any other configuration registers
- The set of available BAR resources

  Any BAR resource present at pause is guaranteed to be reallocated—that is, a device will never lose resources across reconfiguration.
- The registry hierarchy of the device
- The number or kind of interrupt assignments (shared versus MSI)

Most drivers have few or no dependencies on the items above being changed. If they do, while entering the state `kIOPCIDeviceOnState` (from any other state), these dependencies should be updated to the current configuration of the device.

Drivers should ensure any I/Os that are in flight at the time of surprise removal are properly returned as errors to the upper layers that issued the I/O requests. The exact manner in which this is done is I/O family specific.

[Next](Debugging%20Thunderbolt%20Drivers.md)[Previous](Working%20with%20Thunderbolt%20Technology.md)

