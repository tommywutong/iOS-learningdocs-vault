---
title: Mass Storage Device Driver Programming Guide
apple_id: TP40000974
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2007-04-03'
source_url: https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/MassStorage/07_SCSI_Example/MS_SCSI_Example.html
archived_at: '2026-07-15T07:31:32.871054Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Mass Storage Device Driver Programming Guide](Introduction%20to%20Mass%20Storage%20Device%20Driver%20Programming%20Guide.md)


[Next](Developing%20a%20Filter%20Scheme.md)[Previous](Subclassing%20Logical%20Unit%20Drivers.md)

# Subclassing Protocol Services Drivers

The protocol services driver in the transport driver layer of the mass storage driver stack is responsible for preparing the commands it receives from the logical unit driver for transmission across a particular bus. Each supported bus defines a bus transport protocol that specifies how commands and data are sent across the bus. If your device does not comply with the bus transport protocol of the bus it’s connected to, you need to subclass the appropriate Apple protocol services driver to provide the support your device requires.

Apple provides protocol services drivers for devices that comply with the following bus transport protocols:

- FireWire Serial Bus Protocol 2 specifications (see [http://t10.org](http://t10.org/))
- USB mass storage class specifications (see [http://www.usb.org](http://www.usb.org/))
- ATA/ATAPI-5 specifications (see [http://t13.org](http://t13.org/))

This chapter describes how to subclass an Apple-provided protocol services driver to address bus-specific issues. The sample code in this chapter is generic and emphasizes the form your driver should take, rather than the code required to implement a specific method. Because the sample driver is generic, it will not attach to a particular device. To test it with your device, you can replace the generic values for parameters such as vendor or product identification with values that identify your device.

The sample code in this chapter is from a Xcode project that builds an I/O Kit driver. For more information on how to develop kernel extensions in general and I/O Kit drivers in particular, see _[Kernel Extension Programming Topics](../../Darwin/Kernel%20Extension%20Programming%20Topics/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrt)_ and _[IOKit Device Driver Design Guidelines](../IOKit%20Device%20Driver%20Design%20Guidelines/Introduction%20to%20I-O%20Kit%20Device%20Driver%20Design%20Guidelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmoju)_.

This section describes how to create your driver project and edit your driver’s information property list. The sample driver in this chapter is a protocol services driver for a generic FireWire SBP-2 CD-ROM device so it is a subclass of the Apple-provided `IOFireWireSerialBusProtocolTransport` driver.

The sample project uses `MyFWProtocolServicesDriver` for the name of the driver and generic values such as `MySoftwareCompany` for the developer name. You should replace these names and values with your own information in order to test this code with your device.

Open the Xcode application and create a new I/O Kit driver project named `MyFWProtocolServicesDriver`. Specify a directory for the new project or accept the default.

When you create a new I/O Kit driver project, Xcode supplies several files, including two empty source files—`MyFWProtocolServicesDriver.h` and `MyFWProtocolServicesDriver.cpp`. Before you add any code to these files, however, you should edit your driver’s information property list.

Every driver has an information property list (`Info.plist` file) that contains information about the driver and what it needs, including its personalities. As described in [Driver Personalities and the Matching Process](Mass%20Storage%20Driver%20Matching%20and%20Loading.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomzwfvbeeskejjfeora), a driver’s personality contains the matching information the I/O Kit uses to determine the appropriate driver for a device. To make sure your driver loads for your device, you add several properties to its personality dictionary that identify the device or type of device it supports.

In Xcode, a driver’s `Info.plist` file is listed in the Groups & Files view in the project. You can edit the property list file as plain XML text in the Xcode editor window or you can choose a different application (such as Property List Editor) to use. For more information on how to select another editor, see [Hello I/O Kit: Creating a Driver With Xcode](https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/KEXTConcept/KEXTConceptIOKit/iokit_tutorial.html#//apple_ref/doc/uid/20002366).

The `IOKitPersonalities` dictionary in the driver’s `Info.plist` file can contain multiple personality dictionaries, one for each device or type of device your driver supports. The sample driver in this chapter implements only one personality dictionary but you can create additional dictionaries if your driver can support more than one device or device type.

The sample code uses the following ten property keys:

- `CFBundleIdentifier`
- `Command_Set`
- `Command_Spec_ID`
- `Device_Type`
- `IOClass`
- `IOProbeScore`
- `IOProviderClass`
- `Physical Interconnect`
- `Physical Interconnect Location`
- `Vendor_ID`

Using your chosen editing environment, create a new child of the `IOKitPersonalities` dictionary. Make the name of this new child `MyFWProtocolServicesDriver` and set its class to Dictionary.

Create ten new children of the `MyFWProtocolServicesDriver` dictionary, one for each of the ten properties you’ll be adding. [Table 6-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomzyfvbucscgjjceiri) shows the properties, along with their classes and values. To test the sample code with your device, replace values such as `MyCommandSetNumber` with actual values for your device.

__Table 6-1__  Personality properties for MyFWProtocolServicesDriver

| Property | Class | Value |
| `CFBundleIdentifier` | String | `com.MySoftwareCompany.driver.MyFWProtocolServicesDriver` |
| `Command_Set` | Number | `MyCommandSetNumber` |
| `Command_Spec_ID` | Number | `MyCommandSpecIDNumber` |
| `Device_Type` | Number | `MyDeviceTypeNumber` |
| `IOClass` | String | `com_MySoftwareCompany_driver_MyFWProtocolServicesDriver` |
| `IOProbeScore` | Number | `MyProbeScore` |
| `IOProviderClass` | String | `IOFireWireSBP2LUN` |
| `Physical Interconnect` | String | `FireWire` |
| `Physical Interconnect Location` | String | `External` |
| `Vendor_ID` | Number | `MyVendorID` |

A driver declares its dependencies on other loadable kernel extensions and in-kernel components in the `OSBundleLibraries` dictionary. Each dependency has a string value that declares the earliest version of the dependency the driver is compatible with.

The sample driver depends on loadable extensions from the `IOSCSIArchitectureModel` family and the `IOFireWire` family. To add these dependencies to the `OSBundleLibraries` dictionary, you create a new child for each dependency. [Table 6-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomzyfvbucscjircuira) shows the dependencies you add for the sample driver.

__Table 6-2__  Dependencies for MyFWProtocolServicesDriver

| Property | Class | Value |
| `com.apple.iokit.IOSCSIArchitectureModelFamily` | String | `1.0.0` |
| `com.apple.iokit.IOFireWireFamily` | String | `1.0.0` |
| `com.apple.iokit.IOFireWireSBP2` | String | `1.0.0` |
| `com.apple.iokit.IOFireWireSerialBusProtocolTransport` | String | `1.0.0` |

Because the driver of a CD-ROM drive must be able to mount root on a local volume, you add the `OSBundleRequired` property to the top level of its `Info.plist` file. In other words, the new `OSBundleRequired` property is a sibling of the `IOKitPersonalities` and `OSBundleLibraries` dictionaries, not a child. Edit the new element to match the following: 

```
OSBundleRequired    String      Local-Root
```


This section describes some of the elements that must be included in your driver’s source files. To demonstrate the process of subclassing, the sample driver simply overrides the `init`, `start`, and `stop` methods and prints messages. You should replace these trivial functions with your own code that supports your device’s particular physical interconnect transport protocol requirements.

In Xcode, the driver’s source files are listed in the Groups & Files pane, revealed by the discosure triangle next to the `MyFWProtocolServicesDriver` project and the disclosure triangle next to the Source folder.

The header file provides access to external declarations and supporting type definitions needed by the functions and objects in the C++ file. The header for the sample driver is simple because it includes only method declarations and no constant or variable declarations. Edit the `MyFWProtocolServicesDriver.h` file to match the code in [Listing 6-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomzyfvbuurckjfduuqq).

__Listing 6-1__  The MyFWProtocolServicesDriver header file

```c
#ifndef _MyFWProtocolServicesDriver_H_
#define _MyFWProtocolServicesDriver_H_

// Because the sample driver is a subclass of the Apple-provided
// FireWire Serial Bus Protocol driver, it must include that driver's
// header file.
#include <IOKit/sbp2/IOFireWireSerialBusProtocolTransport.h>

// Here, the sample driver declares its inheritance and the method
// it overrides.
class com_MySoftwareCompany_driver_MyFWProtocolServicesDriver : public
                            IOFireWireSerialBusProtocolTransport
{
    OSDeclareDefaultStructors (
            com_MySoftwareCompany_driver_MyFWProtocolServicesDriver )
public:
    virtual bool init ( OSDictionary * propTable );

    virtual bool start ( IOService * provider );

    virtual void stop ( IOService * provider );
};

#endif /* _MyFWProtocolServicesDriver_H_ */
```


The C++ file provides the code to override the chosen methods. The sample driver’s C++ file contains all the elements required for a subclassed driver even though it accomplishes nothing more substantial than messages sent to the system log file, `/var/log/system.log`.

Edit the `MyFWProtocolServicesDriver.cpp` file to match the code in [Listing 6-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomzyfvbuurckjjbeiry).

__Listing 6-2__  The MyFWProtocolServicesDriver C++ file

```c
// Include the header file you created.
#include "MyFWProtocolServicesDriver.h"

// This definition allows you to use the more convenient "super" in
// place of "IOFireWireSerialBusProtocolTransport", where appropriate.
#define super IOFireWireSerialBusProtocolTransport

// This macro must appear before you define any of your class's methods.
// Note that you must use the literal name of the superclass here, not
// "super" as defined above.
OSDefineMetaClassAndStructors (
            com_MySoftwareCompany_driver_MyFWProtocolServicesDriver,
            IOFireWireSerialBusProtocolTransport );

// Define the methods to override.
bool
com_MySoftwareCompany_driver_MyFWProtocolServicesDriver::init (
                                            OSDictionary * propTable )
{
    bool returnValue;

    IOLog ( "MyFWProtocolServicesDriver overriding init\n" );
// You can add code that initializes your device here.

// Call super's init method to make sure all other initialization is done.
    returnValue = super::init ( propTable );

    return returnValue;
}

bool com_MySoftwareCompany_iokit_MyFWProtocolServicesDriver:: start (
                                            IOService * provider )
{
    bool returnValue = false;

    IOLog ( "MyFWProtocolServicesDriver overriding start\n" );
// You can add code for your driver's start functions here.

// Call super's start method to make sure all other start functions are
// fulfilled.
    returnValue = super::start ( provider );

    return returnValue;
}

void com_MySoftwareCompany_iokit_MyFWProtocolServicesDriver::stop (
                                            IOService * provider )
{
    IOLog ( "MyFWProcolLayerDriver overriding stop\n" );
// You can add code for your driver's stop functions here.

// Call super's stop method to ensure all other necessary clean-up is done.
    super::stop ( provider );
}
```


This section presents some advice on testing your driver. You cannot use `kextload` to load and test your driver “by hand” because there are generic drivers that will always load in its place at boot time. Therefore, you need to make sure you have multiple bootable disks or partitions so you can remove your driver if it behaves badly and reboot the disk or partition.

Because the `OSBundleRequired` property in the sample driver’s `Info.plist` file is set to `Local-Root`, the BootX booter will automatically load it when the system is restarted (for more information on this process, see Loading Kernel Extensions at Boot Time).

For help with debugging, you can open a window in the Terminal application (located at `/Applications/Utilities/Terminal`) and type the following line to view the system log:

```
tail -f /var/log/system.log
```

[Next](Developing%20a%20Filter%20Scheme.md)[Previous](Subclassing%20Logical%20Unit%20Drivers.md)

