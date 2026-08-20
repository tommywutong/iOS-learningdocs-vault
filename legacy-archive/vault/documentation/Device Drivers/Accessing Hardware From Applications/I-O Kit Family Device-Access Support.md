---
title: Accessing Hardware From Applications
apple_id: TP30000376
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: IOKit
published: '2007-02-08'
source_url: https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/AccessingHardware/AH_Family_Reference/AH_Family_Reference.html
archived_at: '2026-07-15T07:31:07.564386Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Accessing Hardware From Applications](Introduction%20to%20Accessing%20Hardware%20From%20Applications.md)


[Next](Document%20Revision%20History.md)[Previous](Handling%20Errors.md)

# I/O Kit Family Device-Access Support

This appendix lists the current I/O Kit device families, identifies which families support device interfaces and which can be accessed through device files and POSIX functions, and points to documentation for working with specific devices.

For more information on I/O Kit families, see _[IOKit Fundamentals](../IOKit%20Fundamentals/Introduction%20to%20I-O%20Kit%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridambqgaydcmi)_. For reference documentation of I/O Kit family support of user-space device access, see the Device Drivers Reference Library.

Documentation for working with additional device families will be provided as it becomes available.

- _ADB family._ This family provides an interface (defined in `IOADBLib.h`) for reading and writing registers on ADB devices. The interface permits only polled mode operations. Interrupt operations are only supported for kernel-resident clients.
- _ATA and ATAPI family._ This family does not supply any device interfaces. Access to ATA/ATAPI devices is provided by clients of this family, most commonly the Storage family.

  The SCSI Architecture Model family provides device interfaces for ATAPI devices that comply with the SCSI Architecture Model SCSI Primary Commands specification. See_[SCSI Architecture Model Device Interface Guide](../SCSI%20Architecture%20Model%20Device%20Interface%20Guide/Introduction%20to%20SCSI%20Architecture%20Model%20Device%20Interface%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnzr)_ for more information.
- _Audio family._ The Audio family does not export device interfaces for applications to access audio hardware directly. However, it does provide a device interface that the Audio Hardware Abstraction Layer (Audio HAL) uses to access drivers derived from the Audio family.
- _FireWire family._ The FireWire family provides a general-purpose device interface that is suitable for any FireWire device except those that require an in-kernel driver, such as disk drivers that mount file systems. However, the device interfaces provided by the FireWire DV and FireWire SBP-2 families (described next) provide mechanisms that may be more convenient for working with some devices.

  For the latest information on Apple’s FireWire support, including access to development kits with device interface support, see [http://developer.apple.com/hardwaredrivers/firewire/](https://developer.apple.com/hardwaredrivers/firewire/).

  For more information about accessing FireWire devices (including AV/C and SBP-2 units) from an application, see _[FireWire Device Interface Guide](../FireWire%20Device%20Interface%20Guide/Introduction%20to%20FireWire%20Device%20Interface%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnrz)_.
- _FireWire DV family._ The FireWire DV (digital video) family provides complete driver support so that you can use standard QuickTime functions to access DV devices such as cameras and camcorders. No specific knowledge of FireWire is required and you can use the same functions for OS X and MacOS8and9. Additional documentation for DV support of lower-level device control may be provided at a later date.
- _FireWire SBP-2 family._ This family provides a device interface to communicate with devices that support SBP-2 (Serial Bus Protocol 2).

  The SCSI Architecture Model family provides device interfaces for FireWire SBP-2 devices that comply with the SCSI Architecture Model SCSI Primary Commands specification. See_[SCSI Architecture Model Device Interface Guide](../SCSI%20Architecture%20Model%20Device%20Interface%20Guide/Introduction%20to%20SCSI%20Architecture%20Model%20Device%20Interface%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnzr)_ for more information.
- _Graphics family._ The Graphics family includes Quartz 2D and other graphics libraries that provide high-level graphics-rendering services.

  For information on Quartz 2D and Quartz Compositor (the OS X window server), see [Hardware-Access Options](Hardware-Access%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgnzxfvbecsseiffeisq).
- _HID family._ Through the HID Manager, the HID family provides a device interface for accessing a variety of devices, including joysticks and other game devices, audio devices, non-Apple displays, and UPS (uninterruptible power supply) devices. Note that you can use the Carbon Event Manager and NSEvent interfaces described in [Hardware-Access Options](Hardware-Access%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgnzxfvbecsseiffeisq) to monitor mouse and keyboard actions.

  For more information on using the HID Manager to access HID class devices, see _[HID Class Device Interface Guide](../HID%20Class%20Device%20Interface%20Guide/Introduction%20to%20Working%20With%20HID%20Class%20Device%20Interfaces.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnzq)_. You can also find sample code for using the OS X HID Manager in the [Games Human Interface Device & Force Feedback Sample Code Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000925-TP30000467-TP30000855).
- _Network family._ OS X provides networking functions in Carbon and Cocoa that should handle most standard networking requirements for applications. You can also use the BSD sockets API to obtain network services. A recommended network programming book is _Unix Network Programming, Volume 1, Second Edition_, by W. Richard Stevens, Prentice-Hall PTR, 1998.
- _PC Card family._ There are no direct device interfaces for either CardBus or 16-bit PC Card devices. Direct access to PC Card bus hardware by applications or other code running outside the kernel is not permitted for security reasons. Applications that must communicate with a PC Card must do so through an in-kernel driver.
- _PCI and AGP family._ There are no device interfaces for PCI and AGP devices. Direct access to PCI bus hardware by applications or other code running outside the kernel is not permitted for security reasons. Applications that must communicate with a PCI or AGP card must do so through an in-kernel driver.

  In most cases, applications should interact with higher-level services, such as those provided by the USB storage family or other client families. Applications can access graphics devices through the Quartz Compositor, which is described briefly in [Hardware-Access Options](Hardware-Access%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgnzxfvbecsseiffeisq), or other high-level APIs.
- _SCSI family._ In versions of OS X prior to 10.2, the SCSI family supported user-space access to parallel SCSI devices through the device-interface functions in the `IOSCSILib.h` (in the `cdb` directory of the I/O Kit framework). Your application may still be able to use these functions to find and communicate with parallel SCSI devices. However, if you’re looking up a parallel SCSI device that is not accessible with the SCSI Architecture Model family’s device interfaces and if your application requires compatibility with versions of OS X prior to 10.2, you should employ the device look-up functions of both the new SCSI Parallel family and the old SCSI family. This is because after a user has installed new HBA (host bus adaptor) drivers developed with the new SCSI Parallel family, the device-interface functions of the SCSI family will no longer be supported. By using the functions of both families to look for the device, however, your application has the widest compatibility.

  See _[SCSI Architecture Model Device Interface Guide](../SCSI%20Architecture%20Model%20Device%20Interface%20Guide/Introduction%20to%20SCSI%20Architecture%20Model%20Device%20Interface%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnzr)_ for more information.
- _SCSI Architecture Model family._ Devices that support the SCSI Architecture Model SCSI Primary Commands specification can be controlled by SCSI tasks, which are a means of executing command descriptor block (CDB) commands. The SCSI Architecture Model family provides device interfaces for accessing compliant ATAPI, USB mass storage, FireWire SBP-2, and, in some cases, parallel SCSI devices.

  See _[SCSI Architecture Model Device Interface Guide](../SCSI%20Architecture%20Model%20Device%20Interface%20Guide/Introduction%20to%20SCSI%20Architecture%20Model%20Device%20Interface%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnzr)_ for more information.
- _SCSI Parallel family._ The SCSI Parallel family is new in OS X version 10.2 and is designed to support SCSI controllers. If a user has installed new HBA (host bus adapter) drivers developed with the SCSI Parallel family, your application can access all SCSI devices that do not declare a peripheral device type of $00, $05, $07, or $0E using the device-interface functions of the SCSI Architecture Model family.

  See _[SCSI Architecture Model Device Interface Guide](../SCSI%20Architecture%20Model%20Device%20Interface%20Guide/Introduction%20to%20SCSI%20Architecture%20Model%20Device%20Interface%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnzr)_ for more information.
- _Serial family._ Applications can access devices in this family through the device-file mechanism. You use the I/O Kit to obtain a path to the device files in the `/dev` directory. The filenames start with `cu` or `tty` , such as `cu.modem`, `tty.modem`, `ttyp1`, `ttyp2`, and so on, so that a full device-file name would look like `/dev/cu.modem`. You then perform traditional UNIX serial port access using POSIX `termios` functions. Your application can read and write data using these device files. Data is also routed through to PPP via these device files. For related information, see [Inside the Device-File Mechanism](Device%20Access%20and%20the%20I-O%20Kit.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgnzyfvkfawcsivddcmbs).

  For information on how to use the device-file mechanism to access a serial device from an application, see _[Device File Access Guide for Serial Devices](../Device%20File%20Access%20Guide%20for%20Serial%20Devices/Introduction%20to%20Device%20File%20Access%20Guide%20for%20Serial%20I-O.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnzs)_.
- _Storage family._ OS X provides file-management APIs in Carbon and Cocoa that allow applications to access files and folders on physical storage devices. Applications can also get raw access to media objects in this family through the device file system. You use the I/O Kit to obtain a path to device files in the `/dev` directory, then use traditional UNIX file-system access through POSIX functions. For related information, see [Inside the Device-File Mechanism](Device%20Access%20and%20the%20I-O%20Kit.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgnzyfvkfawcsivddcmbs).

  For information on how to use the device-file mechanism to access storage media from an application, see _[Device File Access Guide for Storage Devices](../Device%20File%20Access%20Guide%20for%20Storage%20Devices/Introduction%20to%20Device%20File%20Access%20Guide%20for%20Storage%20Devices.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnry)_.
- _USB family._ This family provides device interface support for generic Universal Serial Bus (USB) serial devices. Support for USB input devices is provided by the HID family. For more information on accessing USB devices from user space, see _[USB Device Interface Guide](../USB%20Device%20Interface%20Guide/Introduction%20to%20USB%20Device%20Interface%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnzt)_.

  The SCSI Architecture Model family provides device interface support for USB mass storage class devices that comply with the SCSI Architecture Model SCSI Primary Commands specification. See _[SCSI Architecture Model Device Interface Guide](../SCSI%20Architecture%20Model%20Device%20Interface%20Guide/Introduction%20to%20SCSI%20Architecture%20Model%20Device%20Interface%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnzr)_ for more information.

[Next](Document%20Revision%20History.md)[Previous](Handling%20Errors.md)

