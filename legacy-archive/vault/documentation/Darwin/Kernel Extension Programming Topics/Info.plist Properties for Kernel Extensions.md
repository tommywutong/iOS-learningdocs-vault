---
title: Kernel Extension Programming Topics
apple_id: TP40001063
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2010-09-01'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/KEXTConcept/Articles/infoplist_keys.html
archived_at: '2026-07-15T07:23:04.187317Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Kernel Extension Programming Topics](Introduction.md)


[Next](Document%20Revision%20History.md)[Previous](Packaging%20a%20Kernel%20Extension%20for%20Distribution%20and%20Installation.md)

# Info.plist Properties for Kernel Extensions

This appendix describes the properties you can use for your kext’s `Info.plist` file.

__`CFBundleIdentifier`__: The `CFBundleIdentifier` property uniquely identifies your kext. Two kexts with the same value for this property cannot both be loaded into the kernel. The value for this property should be in a reverse-DNS format, for example `com.MyCompany.driver.MyDriver` for an I/O Kit driver or `org.MyCompany.kext.MyKext` for a generic kext.

This property is required.

__`CFBundleExecutable`__: The `CFBundleExecutable` property specifies the name of your kext’s executable code. Xcode automatically creates and populates this value correctly for all kext projects, so you should not need to change it.

This property is required if your kext contains an executable. If you are developing a codeless kext, do not include this property.

__`CFBundleVersion`__: The `CFBundleVersion` property indicates your kext’s version. Kext version numbers must adhere to a strict format:

- The version number is divided into three parts by periods, for example `3.1.2`.

  The first number represents the most recent major release, the second number represents the most recent significant revision, and the third number represents the most recent minor bug fix.

  The first number is limited to four digits; the second and third numbers are limited to two digits each.

  If the value of the third number is `0`, you can omit it and the second period.
- While developing a new version of your kext, include a suffix after the number that is being updated, for example `3.1.3a1`.

  The letter in the suffix represents the stage of development the new version is in (development, alpha, beta, or final candidate, represented by `d`, `a`, `b`, and `fc`), and the number in the suffix is the build version. The build version cannot be `0` or exceed `255`.

  When you release the new version of your kext, make sure to remove the suffix.

This property is required.

__`OSBundleLibraries`__: The `OSBundleLibraries` property is a dictionary that lists the library kexts that your kext links against.

Each element in the dictionary consists of a key-value pair. The key is the CFBundleIdentifier of the dependency (such as `com.apple.kernel.mach`), and the value is the required version of the dependency. When a kext is about to be loaded, the required version of each element in its `OSBundleLibraries` dictionary is compared to the current and compatible versions of the dependency. If the required version lies between the current version of the dependency and its `OSBundleCompatibleVersion` value, the kext and its dependencies are deemed compatible.

You determine the kexts to add with the `kextlibs` command-line tool (see [Determine Kext Dependencies](Command-Line%20Tools%20for%20Analyzing%20Kernel%20Extensions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tinjvfvjvoni)).

This property is required if your kext contains an executable.

This property can be architecture-specific (see [Architecture-Specific Properties](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tiobrfvjvomy)).

__`OSBundleRequired`__: The `OSBundleRequired` property informs the system that your kext must be available for loading during early boot. Kexts that don’t set this property can’t load during early boot. You can specify one of the following values for this property:

__`Root`__: This kext is required to mount root, regardless of where root comes from—for example, platform drivers and families, PCI, or USB.

__`Network-Root`__: This kext is required to mount root on a remote volume—for example, the network family, Ethernet drivers, or NFS.

__`Local-Root`__: This kext is required to mount root on a local volume—for example, the storage family, disk drivers, or file systems.

__`Console`__: This kext is required to provide character console support (single-user mode)—for example, keyboard drivers or the ADB family.

__`Safe Boot`__: This kext is required even during safe-boot (unnecessary extensions disabled)—for example, mouse drivers or graphics drivers.

This property can be architecture-specific (see [Architecture-Specific Properties](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tiobrfvjvomy)).

__`OSBundleCompatibleVersion`__: The `OSBundleCompatibleVersion` property is used to enable linking against a kext as a library. It indicates the oldest version of your library kext that other kexts can link against and still use the current version successfully.

You should increment the value of this property when you remove a symbol from the library, or when an exported symbol's semantics change significantly enough to impact binary compatibility.

The format of this value is the same as that of `CFBundleVersion`.

This property can be architecture-specific (see [Architecture-Specific Properties](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tiobrfvjvomy)).

__`OSBundleAllowUserLoad`__: The `OSBundleAllowUserLoad` property allows non-root users to load your kext. Using this property is not recommended.

I/O Kit drivers should never include this property, because they are loaded by the kernel when they are needed.

Specify a boolean value of true to enable this option.

This property can be architecture-specific (see [Architecture-Specific Properties](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tiobrfvjvomy)).

__`OSBundleEnableKextLogging`__: The `OSBundleEnableKextLogging` property indicates that logging information specific to your kext should be logged in the kernel log (available at `/var/log/kernel.log`). The `kextutil` tool automatically enables this option to assist with debugging. Specify a boolean value of `true` to enable this option. See `kext_logging` for more information.

This property can be architecture-specific (see [Architecture-Specific Properties](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tiobrfvjvomy)).

__`IOKitPersonalities`__: The `IOKitPersonalities` property is used by I/O Kit drivers. It is a nested dictionary of information describing hardware that the driver can operate.

See [IOKitPersonalities Properties](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tiobrfvjvona) for a list of properties to include in the `IOKitPersonalities` dictionary.

See [Driver Personalities and Matching Languages](../../Device%20Drivers/IOKit%20Fundamentals/Driver%20and%20Device%20Matching.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridambqgaydcnjnijauurkjinbeo) in _[IOKit Fundamentals](../../Device%20Drivers/IOKit%20Fundamentals/Introduction%20to%20I-O%20Kit%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridambqgaydcmi)_ for more information on personalities.

This property is required for I/O Kit drivers.

This property can be architecture-specific (see [Architecture-Specific Properties](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tiobrfvjvomy)).

__`IOClass`__: The `IOClass` property names the C++ class to instantiate from your driver when it matches on a nub.

__`IOKitDebug`__: The `IOKitDebug` property indicates that I/O Kit-specific events such as attaching, matching, and probing should be logged in the kernel log (available at `/var/log/kernel.log`). The value of this property defines which events are logged. To log all relevant information, specify `65535` as the value. See `IOKitDebug.h` (available in `/System/Library/Frameworks/Kernel.framework/Headers/IOKit`) for itemized logging values.

__`IOProviderClass`__: The `IOProviderClass` property names the C++ class of the I/O Kit device object that your driver matches on. This is typically the nub that controls the port that your device connects to. For example, if your driver connects to a PCI bus, you should specify `IOPCIDevice` as your driver’s provider class.

__`IOMatchCategory`__: The `IOMatchCategory` property allows multiple drivers with unique values for the property to match on the same provider class. Typically, only one driver can match on a given provider class. Include this property if you are matching on `IOResources` or on a port with multiple devices attached to it. The value for this property should be the same as the value for `CFBundleIdentifier`, with periods replaced with underscores (for example `com_MyCompany_driver_MyDriver`).

__`IOResourceMatch`__: The `IOResourceMatch` property allows you to declare a dependency between your driver and a specific resource, such as the BSD kernel or a particular resource on a device, like an audio video jack. If you provide this property, your driver will not load into the kernel until the specified resource is available.

Top-level kext `Info.plist` properties that begin with `OS` or `IO` have architecture-specific versions you can use to differentiate your kext’s behavior on different architectures. To specify an architecture-specific property, add an underscore followed by the architecture name to a property name, for example, `OSBundleCompatibleVersion_x86_64` or `OSBundleCompatibleVersion_i386`. Make sure to keep the base property in your `Info.plist` file for backwards compatibility.

[Next](Document%20Revision%20History.md)[Previous](Packaging%20a%20Kernel%20Extension%20for%20Distribution%20and%20Installation.md)

