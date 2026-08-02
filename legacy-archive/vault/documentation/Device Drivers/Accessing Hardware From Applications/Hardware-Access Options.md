---
title: Accessing Hardware From Applications
apple_id: TP30000376
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: IOKit
published: '2007-02-08'
source_url: https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/AccessingHardware/AH_Other_APIs/AH_Other_APIs.html
archived_at: '2026-07-15T07:31:09.126070Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Accessing Hardware From Applications](Introduction%20to%20Accessing%20Hardware%20From%20Applications.md)


[Next](Device%20Access%20and%20the%20I-O%20Kit.md)[Previous](Introduction%20to%20Accessing%20Hardware%20From%20Applications.md)

# Hardware-Access Options

Many applications can handle all their hardware-access needs using high-level APIs, such as QuickTime, CFNetwork, and Core Audio. Before you embark upon the development of an application-based device driver, you should read this chapter to determine if there is a more suitable (and probably easier) solution.

If you find that you must use I/O Kit or BSD APIs to access a device, note that Apple does not provide Objective-C interfaces for these APIs. However, because these are pure C APIs, you can call them from your Cocoa application.

The high-level OS X APIs listed here provide some access to hardware and do not require the use of I/O Kit services. This list is not exhaustive. A pointer to documentation for these APIs is provided, where available; otherwise, look for the for the latest documentation in the [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943-TP40003576-TP30000511).

- BSD networking

  You can access networking services from user space using the BSD socket API. The `socket` structure is used to keep track of network information on a per file-descriptor basis: Applications can reference the `socket` structure using file descriptors.

  For more information on the BSD socket API, refer to the `man` pages. In a Terminal window, type `man socket`. To view the man pages in HTML, see OS X Man Pages.
- BSD file systems

  You can use POSIX file I/O functions to access disks represented as device files. These functions use a file descriptor, an integer index into a list of files a process has open, to access files. You can manipulate file descriptors using the standard file descriptor functions, such as `open`, `close`, `read`, and `write`. In addition, you can use the `fcntl` and `ioctl` functions to control files and devices.

  For more information on these functions, refer to the `man` pages. For example, in a Terminal window, type `man open` or `man ioctl`. To view the man pages in HTML, see OS X Man Pages. See _[Device File Access Guide for Serial Devices](../Device%20File%20Access%20Guide%20for%20Serial%20Devices/Introduction%20to%20Device%20File%20Access%20Guide%20for%20Serial%20I-O.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnzs)_ and _[Device File Access Guide for Storage Devices](../Device%20File%20Access%20Guide%20for%20Storage%20Devices/Introduction%20to%20Device%20File%20Access%20Guide%20for%20Storage%20Devices.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnry)_ for examples of how to use file-descriptor functions to access these devices.
- Carbon Event Manager

  The Carbon Event Manager provides routines that communicate user actions and give notice of changes in processing status. You can use the Carbon Event Manager, for example, to obtain information about mouse and keyboard events.

  For more information about the Carbon Event manager, see the [Carbon Events and Other Input Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943-TP30000420-TP30000447).
- Carbon Printing Manager

  The Carbon Printing Manager defines an API that allows applications to print in both Mac OS 8 and 9 with existing printer drivers and in OS X with new printer drivers.

  For more information on how any application (even non-Carbon ones) can use the functions of the Carbon Printing Manager, see the [Carbon Printing Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943-TP30000420-TP30000455).
- CFNetwork

  The CFNetwork API provides abstractions that allow you to easily work with BSD sockets, manage information about remote hosts, and work with HTTP and FTP servers.

  For more information about the CFNetwork API, see _[CFNetwork Programming Guide](../../Networking/CFNetwork%20Programming%20Guide/Introduction%20to%20CFNetwork%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmzs)_.
- Core Audio

  The Audio HAL (Hardware Abstraction Layer) is at the heart of the Core Audio system and provides the interface between applications and hardware. The Audio HAL allows applications to manipulate devices through both an input/output procedure for streaming and a property mechanism for control.

  For more information about the Audio HAL in particular and Core Audio in general, see the [Music & Audio Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943-TP30000428).
- Quartz 2D and Quartz Compositor

  Quartz Compositor (sometimes referred to as “Core Graphics Services” in older documentation) consists of the OS X window server and the private system programming interfaces (SPIs) it implements. It creates the OS X graphical user interface by compositing content from client graphics-rendering libraries, such as Quartz 2D and QuickDraw.

  For more information about Quartz Compositor and about using Quartz 2D, see the [Graphics & Imaging Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943-TP30000424).
- File Manager

  The File Manager allows your application to access files and folders on physical storage devices such as disk drives. It supports several volume formats, including HFS and HFS Plus.

  For more information on how to use the File Manager, see the [Carbon File Management Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943-TP30000420-TP30000448).
- NSEvent (Cocoa object class)

  An NSEvent object, or simply an event, contains information about an input action such as a mouse click or a key down. The Cocoa Application Kit associates each such user action with a window, reporting the event to the application that created the window.

  In OS X version 10.4, applications can receive tablet events, such as tablet-pointing and tablet-proximity events, as NSEvent objects.

  For more information about Cocoa and the Application Kit, see the [Cocoa Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943-TP30000416).
- Open Transport

  Open Transport is the Mac OS 8 and 9 API for accessing TCP/IP networks at the transport level. Apple provides Open Transport as a compatibility library to support migration of legacy applications to OS X. New Mac apps should instead use BSD sockets or higher-level Core Services and Core Foundation APIs, such as CFNetwork.

  For more information on Open Transport, see the [Carbon Networking Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943-TP30000420-TP30000453).
- Power-source information

  You can get information about power sources and UPS (uninterruptible power supply) devices using the I/O Kit’s power-source API located in `/System/Library/Frameworks/IOKit.framework/Headers/ps`. The header files in this folder, `IOPowerSources.h` and `IOPSKeys.h`, contain methods and keys to extract information about both external and internal power sources. For example, an application can get a list of attached power sources, request notifications for changes in its power sources, and determine how much power is left in a battery.
- QuickTime

  QuickTime is a package of system-level code that higher-level software can use to control time-based data. QuickTime can handle video data, still images, animated images (sprites), vector graphics, multiple sound channels, MIDI music, 3D objects, virtual reality panoramas and objects, and even text. For example, you can use the QuickTime video digitizer and video output components to access FireWire DV devices such as DV camcorders.

  For more information on QuickTime, see the [QuickTime Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943-TP30000433).

  (For further information on Apple’s FireWire support, including access to development kits with device-interface support, see [http://developer.apple.com/hardwaredrivers/firewire/](https://developer.apple.com/hardwaredrivers/firewire/).)
- SCSI Manager 4.3

  Beginning with OS X version 10.2, the SCSI Manager 4.3 `SCSIAction` function is deprecated, although it will continue to function on previous versions of OS X until users install SCSI HBA (host bus adapter) drivers developed with the new SCSI Parallel family API (shipped with OS X version 10.2).

  If your application must access a SCSI Parallel device that was not previously accessible with the SCSI Architecture Model family’s device interfaces and your application requires compatibility with versions of OS X earlier than 10.2, your application should look up SCSI devices using both the new IOSCSITaskDeviceInterface and the old IOSCSIDeviceInterface APIs. If a user has installed the new HBA drivers, the new IOSCSITaskDeviceInterface API will find the device and your code can use that interface to communicate with the device. If a function of the old API succeeds in finding the device, it’s because the user hasn’t yet installed the new HBA drivers and your code should use the old API to communicate with the device.

  For more information on how to access SCSI devices, see _[SCSI Architecture Model Device Interface Guide](../SCSI%20Architecture%20Model%20Device%20Interface%20Guide/Introduction%20to%20SCSI%20Architecture%20Model%20Device%20Interface%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnzr)_.

If you’ve determined that the hardware access options listed in [Other APIs That Provide Access to Hardware](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgnzxfvkfawcsivddcmbu) do not meet your application’s needs, you can use the device interface mechanism that many I/O Kit device families provide to access your device.

If you’re unfamiliar with the device interface mechanism, be sure to read the next chapter, [Device Access and the I/O Kit](Device%20Access%20and%20the%20I-O%20Kit.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgnzyfvbecsseiffeisq), for more information. If you’re wondering if an I/O Kit family provides a device interface for your device, see [I/O Kit Family Device-Access Support](I-O%20Kit%20Family%20Device-Access%20Support.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmojtfvbecqsdinbessq).

[Next](Device%20Access%20and%20the%20I-O%20Kit.md)[Previous](Introduction%20to%20Accessing%20Hardware%20From%20Applications.md)

