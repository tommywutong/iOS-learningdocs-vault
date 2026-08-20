---
title: Getting Started with Hardware and Drivers
apple_id: TP40003522
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: null
published: '2009-05-28'
source_url: https://developer.apple.com/library/archive/referencelibrary/GettingStarted/GS_HardwareDrivers/_index.html
archived_at: '2026-07-18T02:39:24.079494Z'
---
> 导航：[总目录](../../README.md) · [referencelibrary](../../_indexes/referencelibrary.md)



## Introduction

Apple's adoption of open standards and support for standard peripheral families yields opportunities for both hardware and device-driver developers.

- Hardware developers can take advantage of standard high-performance interfaces to develop add-on or peripheral products that extend the capabilities of the Macintosh.
- Driver developers can use the I/O Kit, Apple's object-oriented driver-development framework, to create in-kernel or application-level drivers for their own or another vendor's devices.

In addition, OS X provides several services that allow applications to communicate with hardware from plug-ins, shared libraries, and other code running outside the kernel.

### Start Here

To write code that controls a hardware device in OS X, you should:

- Decide whether your code should be in the kernel or in user space. In OS X, many drivers can be written in user space. Network kernel extensions and file systems generally must be in the kernel.
- If you determine that you can write your code in user space, create matching dictionaries to match the appropriate device, then open the device.
- If you determine that you must write a kernel-mode driver, determine what I/O Kit class your driver should subclass and what nubs your driver should publish (if applicable).

  Also create a set of matching rules to tell the `kextd` daemon when to load your kernel extension and create a property list file that reflects this.
- Start writing code that communicates with the hardware.

To develop hardware devices for the Mac, read the relevant developer notes.

To develop a network kernel extension, read [Network Kernel Extensions Programming Guide](../../documentation/Darwin/Network%20Kernel%20Extensions%20Programming%20Guide/Introduction%20to%20Network%20Kernel%20Extensions%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnjy).

To develop a file system, read the [MFSLives](../../samplecode/MFSLives/MFSLives.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimbsgy) sample code.

Choose next how you want to get started—by reading about the basics, getting your hands on some code, or diving into specific technologies.

#### Want to get familiar with the fundamentals?

- Coding in the Kernel explains the pros and cons of developing in-kernel code.
- [What Is the I/O Kit?](https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/IOKitFundamentals/Features/Features.html#//apple_ref/doc/uid/TP0000012) in [IOKit Fundamentals](../../documentation/Device%20Drivers/IOKit%20Fundamentals/Introduction%20to%20I-O%20Kit%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridambqgaydcmi) provides an overview of the OS X driver development environment.
- The [Darwin and Core Technologies](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/OSX_Technology_Overview/SystemTechnology/SystemTechnology.html#//apple_ref/doc/uid/TP40001067-CH207) article in [Mac Technology Overview](../../documentation/Mac%20OSX/Mac%20Technology%20Overview/About%20Developing%20for%20Mac.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrx) describes Darwin (the UNIX-based foundation of OS X) and other low-level technologies.
- [I/O Kit Family Device-Access Support](https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/AccessingHardware/AH_Family_Reference/AH_Family_Reference.html#//apple_ref/doc/uid/TP30000693) in [Accessing Hardware From Applications](../../documentation/Device%20Drivers/Accessing%20Hardware%20From%20Applications/Introduction%20to%20Accessing%20Hardware%20From%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgnzw) provides guidance about what device access is available from user-space applications.
- [I/O Kit Family Reference](https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/IOKitFundamentals/Families_Ref/Families_Ref.html#//apple_ref/doc/uid/TP0000021) in [IOKit Fundamentals](../../documentation/Device%20Drivers/IOKit%20Fundamentals/Introduction%20to%20I-O%20Kit%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridambqgaydcmi) provides additional details for some device types.
- [Network Kernel Extensions Programming Guide](../../documentation/Darwin/Network%20Kernel%20Extensions%20Programming%20Guide/Introduction%20to%20Network%20Kernel%20Extensions%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnjy) explains how to write kernel extensions that work with network packets.

#### Prefer to learn by example?

- [USBPrivateDataSample](../../samplecode/USBPrivateDataSample/USBPrivateDataSample.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydanbvgy): Provides an example of controlling a USB device from user space code.
- [Hello Kernel: Creating a Kernel Extension With Xcode](https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/KEXTConcept/KEXTConceptKEXT/kext_tutorial.html#//apple_ref/doc/uid/20002365): Provides an overview of creating a non-I/O Kit kernel extension.
- [Hello I/O Kit: Creating a Device Driver With Xcode](https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/KEXTConcept/KEXTConceptIOKit/iokit_tutorial.html#//apple_ref/doc/uid/20002366): Provides an overview of creating an I/O Kit kernel extension.
- [SimpleUserClient](../../samplecode/SimpleUserClient/SimpleUserClient.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydanbvga): Provides an example of how to provide communication between a kernel-mode driver and user-space applications.
- [SampleFilterScheme](../../samplecode/SampleFilterScheme/SampleFilterScheme.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydanbtgi): Shows how to interpose a driver between existing driver layers.
- [AppleFWAudio Vendor Specific Override Driver](../../samplecode/AppleFWAudio%20Vendor%20Specific%20Override%20Driver/AppleFWAudio%20Vendor%20Specific%20Override%20Driver.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimzuhe) and [SampleUSBAudioPlugin](../../samplecode/SampleUSBAudioPlugin/SampleUSBAudioPlugin.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnbxge): Shows how to extend Apple’s existing USB and FireWire audio drivers to add device-specific functionality.
- [MFSLives](../../samplecode/MFSLives/MFSLives.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimbsgy): Gives an example of how to add support for a local file system.
- [enetlognke](../../samplecode/enetlognke/enetlognke.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnjxhe) and [tcplognke](https://developer.apple.com/library/archive/samplecode/tcplognke/Introduction/Intro.html#//apple_ref/doc/uid/DTS10003669): Demonstrates how to write network kernel extensions.

In addition to these examples and other examples in [Hardware and Drivers Sample Code](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000925-TP40003576), the [Darwin open source project](http://www.opensource.apple.com/darwinsource/) provides dozens of device drivers that you can use as a starting point for understanding the I/O Kit.

#### Want to learn how to leverage your existing code and knowledge?

- [Porting UNIX/Linux Applications to OS X](../../documentation/Porting/Porting%20UNIX-Linux%20Applications%20to%20OS%20X/Introduction%20to%20Porting%20UNIX-Linux%20Applications%20to%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambt) provides an overview of OS X targeted at UNIX developers. As a device-driver developer, you should read the [Porting File, Device, and Network I/O](https://developer.apple.com/library/archive/documentation/Porting/Conceptual/PortingUnix/io_porting/io_porting.html#//apple_ref/doc/uid/TP40002854) chapter in particular.
- [Porting Drivers to OS X](../../documentation/Porting/Porting%20Drivers%20to%20OS%20X/Introduction%20to%20Porting%20Drivers%20to%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrz) provides explanation of some of the fundamental driver constructs that OS X provides and relates them to driver architectures on other platforms.

### Go In Depth

Sometimes you need task-focused information or answers to specific questions to get started. Browse the popular tasks described below for a more targeted way to start developing your web app or web content.

#### Using High-Level APIs to Access Hardware

Many applications can handle all their hardware-access needs using high-level APIs that are available through Carbon and Cocoa. Unless you’re absolutely certain you need to develop a device driver, read the following to find out if there is an easier solution:

- __Learn alternative approaches to accessing hardware.__ Read [Hardware-Access Options](https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/AccessingHardware/AH_Other_APIs/AH_Other_APIs.html#//apple_ref/doc/uid/TP30000377) in [Accessing Hardware From Applications](../../documentation/Device%20Drivers/Accessing%20Hardware%20From%20Applications/Introduction%20to%20Accessing%20Hardware%20From%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgnzw) to learn how to access hardware devices from user-space code.
- __Access a specific device.__ See the appropriate topic (such as Bluetooth) in [Hardware & Drivers Guides](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000440-TP40003576) for more information.

#### Accessing Hardware from Application

- __Access hardware from user space.__ [Accessing Hardware From Applications](../../documentation/Device%20Drivers/Accessing%20Hardware%20From%20Applications/Introduction%20to%20Accessing%20Hardware%20From%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgnzw) explains how to use device interfaces to develop an application-based device driver.
- __Work with human interface devices.__ [HID Class Device Interface Guide](../../documentation/Device%20Drivers/HID%20Class%20Device%20Interface%20Guide/Introduction%20to%20Working%20With%20HID%20Class%20Device%20Interfaces.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnzq) explains how to work with human interface devices (game controllers, keyboards, control surfaces, and so on) in user-space applicatinos.
- __Control USB devices from user space.__ [USB Device Interface Guide](../../documentation/Device%20Drivers/USB%20Device%20Interface%20Guide/Introduction%20to%20USB%20Device%20Interface%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnzt) explains how to control other USB devices from user-space applications.
- __Control FireWire devices from user space.__ [FireWire Device Interface Guide](../../documentation/Device%20Drivers/FireWire%20Device%20Interface%20Guide/Introduction%20to%20FireWire%20Device%20Interface%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnrz) explains how to control FireWire devices from user-space applications.

The subtopics in [Hardware & Drivers Guides](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000440-TP40003576) provide additional information about specific device types.

#### Developing an In-Kernel Device Driver

Developing a kernel-resident device driver is difficult at best and should be done only if there is no alternative. If you’ve determined that your device driver must reside in the kernel, you want to learn more about the kernel and how to program in it.

- [Kernel Programming Guide](../../documentation/Darwin/Kernel%20Programming%20Guide/About%20This%20Document.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbv) gives a high level overview of the kernel environment.
- [About Kernel Extensions](https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/KEXTConcept/KEXTConceptAnatomy/kext_anatomy.html#//apple_ref/doc/uid/20002364) provides an overview of how to create kernel extensions.
- The [Hello Kernel](https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/KEXTConcept/KEXTConceptKEXT/kext_tutorial.html#//apple_ref/doc/uid/20002365) and [Hello I/O Kit](https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/KEXTConcept/KEXTConceptIOKit/iokit_tutorial.html#//apple_ref/doc/uid/20002366) tutorials provide step-by-step directions about creating an in-kernel device driver.
- [IOKit Device Driver Design Guidelines](../../documentation/Device%20Drivers/IOKit%20Device%20Driver%20Design%20Guidelines/Introduction%20to%20I-O%20Kit%20Device%20Driver%20Design%20Guidelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmoju) provides in-depth information on all aspects of in-kernel driver development for OS X.

If you need to know how to write a device driver for a specific device, see the appropriate topic (such as Bluetooth) in [Hardware & Drivers Guides](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000440-TP40003576).

#### Developing, Supporting, and Servicing Hardware

- __Develop compatible add-on or peripheral devices.__ The [Hardware and Drivers Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943-TP40003576) provides hardware developer notes that explain the internal design of the system, its hardware input-output and expansion capabilities, and potential compatibility issues.
- __Add support for a printer.__ [Getting Started with Printing](https://developer.apple.com/library/archive/referencelibrary/GettingStarted/GS_Printing/_index.html#//apple_ref/doc/uid/TP30001080) lists the resources you should read first. [Bonjour Overview](../../documentation/Cocoa/Bonjour%20Overview/About%20Bonjour.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeyts2i) explains Bonjour, Apple’s zero-configuration networking solution.
- __Sign up for [AppleCare Technician Training](http://www.apple.com/support/products/techtrain.html) to learn peripheral device installation or hardware diagnosis and repair.__ This program also gives you access to Apple’s Service Source materials, including diagnostic tools and take-apart instructions.

### Ready for More?

The OS X Reference Library holds plenty more resources that make your job easier. To narrow the list of resources, you can set filters to focus on specific resource types (such as guides or sample code) or on specific topics (such as user experience or data management).

