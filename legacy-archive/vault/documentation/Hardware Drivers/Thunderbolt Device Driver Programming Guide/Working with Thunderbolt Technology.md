---
title: Thunderbolt Device Driver Programming Guide
apple_id: TP40011138
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: null
published: '2013-10-22'
source_url: https://developer.apple.com/library/archive/documentation/HardwareDrivers/Conceptual/ThunderboltDevGuide/Basics01/Basics01.html
archived_at: '2026-07-15T07:41:11.895222Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Thunderbolt Device Driver Programming Guide](About%20the%20Thunderbolt%20Technology.md)


[Next](Handling%20and%20Routing%20Interrupts.md)[Previous](Thunderbolt%20Technology%20Overview.md)

# Working with Thunderbolt Technology

This chapter provides guidelines for working with the Thunderbolt technology. Keep these guidelines in mind when creating compatible devices.

System software is used to discover Thunderbolt devices and to determine when a new Thunderbolt device has been attached. The software discovers all DisplayPort and PCI devices, and creates Thunderbolt paths to those devices using any available resources. Once the paths are created, the applicable OS driver(s) are notified to the presence of the devices.

In the case of DisplayPort, graphics drivers may light up the screen. The screen is only lit up based on the capabilities of the GPU.

In the case of PCI, the I/O PCI family (`IOPCIFamily`) within the I/O Kit is responsible for enumerating the PCI bridge in the controller chip and any downstream bridges or devices.

PCI resources (bus numbers, memory apertures) are scarce and programmers and device manufacturers should do their best to present the true requirements of the device.

For example, consider a PCI device that has multiple functions, where only function 0 will be used in the application. PCI functions other than function 0 should be hidden from the OS if possible, by returning `0xFFFFFFFF` for a Configuration Read at offset 0 for that function. Another example is a device that requires only 2 KB of aperture for Memory Mapped I/O (MMIO) space, but instead reports 64 KB of aperture during enumeration. These devices should report accurate aperture values.

I/O space cannot be counted on when designing for the Thunderbolt interface. PCI limitations require an I/O space allocation of 4 KB per PCI Bridge, and the total system-wide I/O space is only 64 KB. Therefore, use MMIO instead of relying on I/O space allocations for devices. Using MMIO allows the operating system to load the device driver, even if I/O space could not be properly allocated for the device.

Devices on a Thunderbolt bus exhibit higher latency than devices on internal slots—about 1.5 microseconds of round-trip latency per hop. This means that putting a device at the end of a Thunderbolt chain can add up to 9 microseconds of round-trip latency. Most devices and drivers handle this additional communication latency with no particular difficulty. In some cases, however, your driver or device firmware must be tweaked to tolerate that latency.

For example:

- If your driver uses timers to detect device failures, you may need to lengthen the timeout value.
- If your driver needs to perform an operation the moment an interrupt occurs, you may have to find another way to schedule the operation, such as telling the device to delay the action until the next interrupt or using a software-defined phase-locked loop.
- If your device expects the driver to send some data and then wait for the device to acknowledge it before sending more data, then the device needs to be more tolerant of delays than it otherwise might need to be, or else the driver needs to handle failure gracefully.
- If your driver tells an isochronous endpoint to stop sending data, it may continue to send data longer than usual.

And so on. The details are highly dependent on the driver.

Each Thunderbolt device _must_ have a Device ROM (DROM) that contains information about the vendor and the device, as well as a 64-bit UID, which uniquely identifies the device. Each vendor must have a registered vendor ID with the Thunderbolt naming authority (Intel).

To declare support for Thunderbolt technology, the following key must be added to _each_ of the personalities in your driver’s `Info.plist` file.

__Listing 2-1__  PCI Driver Key (Thunderbolt Operation)

```
<key>IOPCITunnelCompatible</key>
<true/>
```

You must include the key in the IOKitPersonalities section of the `Info.plist` file or the `IOPCIFamily` will not load the drivers for Thunderbolt connected PCI devices. This opt-in key protects consumers against older drivers that have not yet been updated to support Thunderbolt technology. This method also makes it easy for third party developers, who have properly updated their driver, to signify they have done so. (See example driver [Listing 2-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcmzyfvbuqnjnknltq).)

An example driver that includes this key in one of its personalities is `AppleAHCIPort.kext`, which is shown in the PCI Driver Personality (Thunderbolt Key Set).

__Listing 2-2__  PCI Driver Personality (Thunderbolt Key Set)

```
<key>GenericAHCI</key>
<dict>
         <key>CFBundleIdentifier</key>
         <string>com.apple.driver.AppleAHCIPort</string>
         <key>Chipset Name</key>
         <string>AHCI Standard Controller</string>
         <key>IOClass</key>
         <string>AppleAHCI</string>
         <key>IOPCIClassMatch</key>
         <string>0x01060100&0xffffff00</string>
         <key>IOProbeScore</key>
         <integer>800</integer>
         <key>IOProviderClass</key>
         <string>IOPCIDevice</string>
         <key>Vendor Name</key>
         <string>Unknown</string>
         key>IOPCITunnelCompatible/key>
         <true/>
</dict>
```


PCI device drivers can determine if a Thunderbolt device is connected by recursively searching over parents in the I/O Registry for the key `IOPCITunnelled`. (See code example [Listing 2-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcmzyfvbuqnjnknltcma) .)

__Listing 2-3__  Verifying Thunderbolt Connections

```c
#include < IOKit/pci/IOPCIDevice.h>
bool tb = false;
if ( getProperty ( kIOPCITunnelledKey, gIOServicePlane, kIORegistryIterateRecursively | kIORegistryIterateParents ) )
     tb = true;
```

Additionally, PCI device drivers that present storage to the operating system _must_ ensure the “Physical Interconnect Location” key is set to indicate that the device is externally connected. (See physical interconnect location key example [Listing 2-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcmzyfvbuqnjnknltcmi) .)

__Listing 2-4__  PCI Driver: External Storage Key Set

```
setProperty ( kIOPropertyPhysicalInterconnectLocationKey,
kIOPropertyExternalKey );
```

[Next](Handling%20and%20Routing%20Interrupts.md)[Previous](Thunderbolt%20Technology%20Overview.md)

