---
title: Kernel Extension Programming Topics
apple_id: TP40001063
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2010-09-01'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/KEXTConcept/KEXTConceptAnatomy/kext_anatomy.html
archived_at: '2026-07-15T07:23:04.202741Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Kernel Extension Programming Topics](Introduction.md)


[Next](Creating%20a%20Generic%20Kernel%20Extension%20with%20Xcode.md)[Previous](Deciding%20Whether%20to%20Create%20a%20Kernel%20Extension.md)

# The Anatomy of a Kernel Extension

Kexts are loadable bundles, and like all loadable bundles, they are loaded dynamically by another application. In the case of a kext, this application is the kernel itself. This has many implications for kexts, such as running in supervisor mode and the ability to load during early boot. Kexts have strict security and location requirements that you need to follow for your kext to work.

To understand the anatomy of a kext, you should have a basic understanding of bundles. For general information on the structure of a bundle, see _[Bundle Programming Guide](../../Core%20Foundation/Bundle%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdg2i)_.

In the most general case, a kext bundle contains two components: an __information property list__ and an __executable__. Along with these components, a kext bundle may include additional resources and plug-ins. Each of these components is described here.

A kext’s `Info.plist` file describes the kext’s contents. Every kext must have an `Info.plist` file. Because a kext can be loaded during early boot when limited processing is available, this file must be in XML format and cannot include comments. The following keys are of particular importance in a kext’s `Info.plist` file:

- `CFBundleIdentifier` is used to locate a kext both on disk and in the kernel. Multiple kexts with a given identifier can exist on disk, but only one such kext can be loaded in the kernel at a time.
- `CFBundleExecutable` specifies the name of your kext’s executable, if it has one.
- `CFBundleVersion` indicates the kext’s version. Kext version numbers follow a strict pattern (see [Info.plist Properties for Kernel Extensions](Info.plist%20Properties%20for%20Kernel%20Extensions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tiobrfvjvomi)).
- `OSBundleLibraries` lists the libraries (which are kexts themselves) that the kext links against.
- `IOKitPersonalities` is used by an I/O Kit driver for automatically loading the driver when it is needed.

There are several more kext-specific `Info.plist` keys that allow you to further describe your kext. For a complete discussion of all kext `Info.plist` keys, including keys that refer to kernel-specific runtime facilities, see [Info.plist Properties for Kernel Extensions](Info.plist%20Properties%20for%20Kernel%20Extensions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tiobrfvjvomi).

This is your kext’s compiled, executable code. Your executable is responsible for defining entry points that allow the kernel to load and unload the kext. These entry points differ depending on the Xcode template you use when creating your kext. Table 1 describes the default differences between the two kext Xcode templates. This table is intended to illustrate only the most common use of each template; the kernel does not differentiate between kexts created with different templates, and it is possible to incorporate elements of both templates into a kext.

__Table 1__  A comparison of the two Xcode templates for creating a kext

|  | Generic kernel extension template | IOKit driver template |
| Programming language | Usually C | C++ |
| Implementation | C functions registered as callbacks with relevant subsystems | Subclasses of one or more I/O Kit driver classes, such as `IOGraphicsDevice` |
| Entry points | Start and stop functions with C linkage | C++ static constructors and destructors |
| Loading behavior | Must be loaded explicitly | Loaded automatically by the I/O Kit when needed |
| Unloading behavior | Must be unloaded explicitly | Unloaded automatically by the I/O Kit after a fixed interval when no longer needed |
| Tutorial | [Creating a Generic Kernel Extension with Xcode](Creating%20a%20Generic%20Kernel%20Extension%20with%20Xcode.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgm3dklkcifbeuscdjjaq) | [Creating a Device Driver with Xcode](Creating%20a%20Device%20Driver%20with%20Xcode.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgm3dmlkdjfeekq2ijbcq) |

Some kexts don’t include an executable. These kexts (called codeless kexts) are typically used to tell I/O Kit to use an existing driver for your device. See [Codeless Kernel Extensions Match New Devices to Existing Drivers](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgm3dilktk44a) for more information.

Kexts sometimes require additional resources, such as firmware for a device. If your kext requires a resource, put it in the `Resources` folder of your kext’s bundle. If you plan to localize your resources, keep in mind that kernel-space code does not detect localized resources. User-space code _does_ detect localized resources in `.lproj` subfolders of the `Resources` folder, so if your resource is accessed _only_ by user-space code, localization is straightforward.

In addition to general resources, kexts can contain plug-ins, including other kexts. If your kext uses a plug-in, put it in the `PlugIns` folder of your kext’s bundle. Make sure that plug-in kexts do not contain plug-in kexts of their own; only one level of plug-ins is detected in order to limit file system traversal during early boot.

Kexts execute in kernel space and run in supervisor mode; consequently, files and folders in a kext bundle must be owned by the `root` user and the `wheel` group. Files must have the permissions `0644`, and folders must have the permissions `0755`. A kext that fails to meet these requirements will not load into the kernel.

During development, to ensure that your kext has the proper ownership and permissions, create a copy of your kext as the root user.

```
% sudo cp -R MyKext.kext /tmp
Password:
```

This method requires creating a new copy of the kext every time you build it.

With System Integrity Protection, kernel extensions must be signed with a Developer ID for Signing Kexts certificate, and installed into the `/Library/Extensions` directory.

You can request a Developer ID Certificate for signing kexts by visiting [https://developer.apple.com/contact/kext](https://developer.apple.com/contact/kext) and filling out the required details.

See [Kernel Extensions](https://developer.apple.com/library/archive/documentation/Security/Conceptual/System_Integrity_Protection_Guide/KernelExtensions/KernelExtensions.html#//apple_ref/doc/uid/TP40016462-CH4) in _[System Integrity Protection Guide](../../Security/System%20Integrity%20Protection%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dinrs)_ for more information.

A codeless kext is a kext bundle that does not contain an executable. A codeless kext’s `IOKitPersonalities` dictionary names other kexts that are loaded when a personality matches on a device. Each of these other kexts must have an executable. Codeless kexts are commonly used with USB and HID devices that are driven from user space. Because the kernel driver implements a standard protocol, it can be used by nearly all devices in these categories.

For example, most USB printers share a generic driver provided by Apple, `AppleUSBMergeNub.kext`. Apple cannot include the matching dictionary for every printer in this kext, so you can install a codeless kext with a personality that matches your printer and set the personality's CFBundleIdentifier to `com.apple.driver.AppleUSBMergeNub`. When your printer is attached to the computer, `AppleUSBMergeNub.kext` is loaded to drive it. Listing 1 shows an example of such a codeless kext’s IOKitPersonalities dictionary, in XML format.

__Listing 1__  The `IOKitPersonalities` dictionary of a codeless kext

```
<key>IOKitPersonalities</key>
<dict>
    <key>My_USB_Printer</key>
    <dict>
        <key>CFBundleIdentifier</key>
        <string>com.apple.driver.AppleUSBMergeNub</string>
        <key>IOClass</key>
        <string>AppleUSBMergeNub</string>
        <key>IOProviderClass</key>
        <string>IOUSBInterface</string>
        <key>idProduct</key>
        <integer>0000</integer>
        <key>idVendor</key>
        <integer>0000</integer>
    </dict>
</dict>
```

[Next](Creating%20a%20Generic%20Kernel%20Extension%20with%20Xcode.md)[Previous](Deciding%20Whether%20to%20Create%20a%20Kernel%20Extension.md)

