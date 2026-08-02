---
title: Writing PCI Drivers
apple_id: TP40000975
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2006-04-04'
source_url: https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/WritingPCIDrivers/agp_device/agp_device.html
archived_at: '2026-07-15T07:31:53.103988Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Writing PCI Drivers](About%20This%20Book.md)


[Next](Taking%20Primary%20Interrupts.md)[Previous](Writing%20a%20Driver%20for%20a%20PCI%20Device.md)

# Writing a Driver for an AGP Device

AGP is a superset of PCI providing additional functionality that is optimized for video devices. This chapter describes this added functionality at a high level. For detailed programming information, you should consult the documentation for the `IOAGPDevice` family, which can be found on the Apple Developer Documentation website ([http://developer.apple.com/Documentation](https://developer.apple.com/Documentation)).

Fundamentally, supporting an AGP device does not require much more effort than supporting a PCI device. PCI drivers should “just work” for AGP devices as-is with the possible addition of a new matching personality if the device has a different ID or Open Firmware name. You can add an additional personality for AGP in exactly the same way as you would add a personality for a standard PCI device, as described in [Matching](Writing%20a%20Driver%20for%20a%20PCI%20Device.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgnbxfvkfawcsivddcmbs).

You should note, however, that a standard PCI driver will not see AGP’s performance gains without additional driver changes to facilitate the use of AGP memory transactions to and from the device.

To add this support, you must first detect whether the device your driver matched against is, in fact, an AGP device. You can do this by trying to cast your provider to the type `IOAGPDevice` by calling `OSDynamicCast`. If this call succeeds, your driver matched against an AGP device. If it fails, your driver matched against a non-AGP PCI device such as a standard PCI card or a CardBus card.

Once you have determined that your driver has matched against an AGP device, you should use the `IOAGPDevice` method `createAGPSpace` to create an AGP space for communication with the device and enable AGP transactions on the bus. You should use the method `destroyAGPSpace` when your driver unloads.

From there, you can use the method `commitAGPMemory` to make blocks of memory accessible to your device via AGP calls—for example, if your graphics card needs to read a texture out of main memory. You should use `releaseAGPMemory` to free the AGP mappings for these memory regions when you’re finished with them.

With those changes, the PCI device driver should reflect the added performance benefits that AGP provides without further modification.

For more information on AGP devices, consult the documentation for the `IOAGPDevice` family and the graphics acceleration SDK.

[Next](Taking%20Primary%20Interrupts.md)[Previous](Writing%20a%20Driver%20for%20a%20PCI%20Device.md)

