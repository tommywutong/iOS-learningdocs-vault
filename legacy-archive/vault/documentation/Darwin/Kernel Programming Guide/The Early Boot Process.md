---
title: Kernel Programming Guide
apple_id: TP30000905
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2013-08-08'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/KernelProgramming/booting/booting.html
archived_at: '2026-07-15T07:23:13.700225Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Kernel Programming Guide](About%20This%20Document.md)


[Next](Security%20Considerations.md)[Previous](Kernel%20Architecture%20Overview.md)

# The Early Boot Process

When the power to a Macintosh computer is turned on, the BootROM firmware is activated. BootROM (which is part of the computer’s hardware) has two primary responsibilities: it initializes system hardware and it selects an operating system to run. BootROM has two components to help it carry out these functions:

- 

  POST (Power-On Self Test) initializes some hardware interfaces and verifies that sufficient memory is available and in a good state.
- 

  EFI does basic hardware initialization and selects which operating system to use.

If multiple installations of OS X are available, BootROM chooses the one that was last selected by the Startup Disk System Preference. The user can override this choice by holding down the Option key while the computer boots, which causes EFI to display a screen for choosing the boot volume.

Once BootROM is finished and an OS X partition has been selected, control passes to the boot.efi boot loader. The principal job of this boot loader is to load the kernel environment. As it does this, the boot loader draws the “booting” image on the screen.

If full-disk encryption is enabled, the boot loader is responsible for drawing the login UI and prompting for the user’s password, which needed to access the encrypted disk to boot from it. (This UI is drawn by `loginwindow` otherwise.)

In the simplest case, the boot loader can be found in the `/System/Library/CoreServices` directory on the root partition, in a file named `boot.efi`.

In order to speed up boot time, the boot loader uses several caches. The contents and location of these caches varies between versions of OS X, but knowing some details about the caching may be helpful when debugging kernel extensions.

After you install or modify a kernel extension, touch the `/System/Library/Extensions` directory; the system rebuilds the caches automatically.

In OS X v10.7, the boot loader looks for the unified prelinked kernel. This cache contains all kernel extensions that may be needed to boot a Mac with any hardware configuration, with the extensions already linked against the kernel. It is located at `/System/Library/Caches/com.apple.kext.caches/Startup/kernelcache`.

In OS X v10.6 and earlier, the boot loader first looks for the prelinked kernel (also called the kernel cache). This cache contains exactly the set of kernel extensions that were needed during the previous system startup, already linked against the kernel. If the prelinked kernel is missing or unusable (for example, because a hardware configuration has changed), the booter looks for the mkext cache, which contains all kernel extensions that may be needed to boot the system. Using the mkext cache is much slower because the linker must be run. On OS X v10.5 and v10.6, these caches are located in `/System/Library/Caches/com.apple.kext.caches/Startup/`; on previous versions of OS X, it was located at `/System/Library/Caches/com.apple.kernelcaches/`.

Finally, if the caches cannot be used, the boot loader searches `/System/Library/Extensions` for drivers and other kernel extensions whose `OSBundleRequired` property is set to a value appropriate to the type of boot (for example, local or network boot). This process is very slow, because the `Info.plist` file of every kernel extension must be parsed, and then the linker must be run.

For more information on how drivers are loaded, see _[IOKit Fundamentals](../../Device%20Drivers/IOKit%20Fundamentals/Introduction%20to%20I-O%20Kit%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridambqgaydcmi)_, the manual page for `kextcache`, and _[Kernel Extension Programming Topics](../Kernel%20Extension%20Programming%20Topics/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrt)_.

Once the kernel and all drivers necessary for booting are loaded, the boot loader starts the kernel’s initialization procedure. At this point, enough drivers are loaded for the kernel to find the root device.

The kernel initializes the Mach and BSD data structures and then initializes the I/O Kit. The I/O Kit links the loaded drivers into the kernel, using the device tree to determine which drivers to link. Once the kernel finds the root device, it roots(\*) BSD off of it.

_Boot≠Root_ is a technology that allows the system to boot from a partition other than the root partition. This is used to boot systems where the root partition is encrypted using full-disk encryption, or where the root partition is located on a device which requires additional drivers (such as a RAID array). Boot≠Root uses a helper partition to store the files needed to boot, such as the kernel cache. For more information on how to set up the property in a filter-scheme driver, see [Developing a Filter Scheme](https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/MassStorage/08_Media_Example/MS_Media_Example.html#//apple_ref/doc/uid/TP30000739) in _[Mass Storage Device Driver Programming Guide](../../Device%20Drivers/Mass%20Storage%20Device%20Driver%20Programming%20Guide/Introduction%20to%20Mass%20Storage%20Device%20Driver%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnzu)_.

[Next](Security%20Considerations.md)[Previous](Kernel%20Architecture%20Overview.md)

