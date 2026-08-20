---
title: Mass Storage Device Driver Programming Guide
apple_id: TP40000974
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2007-04-03'
source_url: https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/MassStorage/03_Compliance/MS_Compliance.html
archived_at: '2026-07-15T07:31:32.796517Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Mass Storage Device Driver Programming Guide](Introduction%20to%20Mass%20Storage%20Device%20Driver%20Programming%20Guide.md)


[Next](Mass%20Storage%20Driver%20Matching%20and%20Loading.md)[Previous](Mass%20Storage%20Overview.md)

# Mass Storage Device Compliance

Apple provides mass storage device drivers in the transport driver layer that support various device specifications. In order for your device to work with these drivers, it must comply with the appropriate specifications. This chapter describes device compliance and lists the logical unit and protocol services drivers Apple provides.

The concept of device compliance has no meaning in the device services layer. The generic block storage driver treats the device as a storage space and media filter-scheme drivers work with media present in the device; neither makes any assumptions about underlying transport specifications or implementation. For more information about how to develop your own filter-scheme driver, see [Filter-Scheme Driver Matching](Mass%20Storage%20Driver%20Matching%20and%20Loading.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomzwfvbegskcifbuosa) and [Developing a Filter Scheme](Developing%20a%20Filter%20Scheme.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomzzfvkfawcsivddcmbr).

Apple provides logical unit and protocol services drivers at the transport driver layer of the mass storage driver stack (shown in [Figure 1-2](Mass%20Storage%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomzufvbeeq2kinceqqy)). These drivers will drive any mass storage device that complies with the supported specifications.

There are two areas in which a device must be compliant in order to partake of the services of the provided drivers:

- SCSI command set implementation
- Physical interconnect transport protocol

SCSI command set implementation compliance means that a device’s firmware processes commands as documented in a SCSI Architecture Model shared command set specification. For example, if a multimedia device processes commands as defined by the SCSI multimedia command set specification, it is considered compliant and the Apple-provided `IOSCSIPeripheralDeviceType05` driver will drive it successfully.

Compliance with a physical interconnect transport protocol means that a device sends and receives commands according to the protocol defined by the bus it’s on. For example, in order for a USB device to be compliant with the USB mass storage class, it must comply with one of the subclasses defined by the USB Mass Storage Class Specification. The Apple-provided `IOUSBMassStorageClass` protocol services driver will drive such a device successfully.

For SCSI command set implementation-compliant devices, Apple provides four logical unit drivers that support the following specifications:

- The `IOSCSIPeripheralDeviceType00` driver supports block storage devices that comply with the SCSI block commands specification.
- The `IOSCSIPeripheralDeviceType05` driver supports multimedia devices that comply with the SCSI multimedia commands specification.
- The `IOSCSIPeripheralDeviceType07` driver supports magneto-optical devices that comply with the SCSI block commands specification.
- The `IOSCSIPeripheralDeviceType0E` driver supports reduced block command devices that comply with the SCSI reduced block commands specification.

For physical interconnect transport protocol-compliant devices, Apple provides protocol services drivers that support the following bus transport protocols:

- The `IOFireWireSerialBusProtocolTransport` driver supports FireWire Serial Bus Protocol 2 (SBP-2) mass storage devices defined in the SCSI Architecture Model specifications ([http://t10.org](http://t10.org/)).
- The `IOUSBMassStorageClass` driver supports USB mass storage devices that comply with the USB Mass Storage Class specification ([http://www.usb.org](http://www.usb.org/)). For a listing of the supported USB Mass Storage Class subclasses and protocols, see[The USB Mass Storage Class Protocol Services Driver](Mass%20Storage%20Driver%20Matching%20and%20Loading.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomzwfvbeeskgjjeecsa).
- The `IOATAPIProtocolTransport` driver supports ATAPI mass storage devices that comply with the ATA/ATAPI-5 specification ([http://t13.org](http://t13.org/)).

If your device is compliant with both a SCSI Architecture Model shared command set specification and a physical interconnect transport protocol, you will not have to write your own driver for it. If, however, your device is not compliant with these specifications or protocols, you will need to subclass the appropriate Apple-provided driver to address the difference. Similarly, if your device provides additional functionality at the command set implementation or bus transport level, you will need to develop a subclass that supports the new feature.

[Next](Mass%20Storage%20Driver%20Matching%20and%20Loading.md)[Previous](Mass%20Storage%20Overview.md)

