---
title: Mass Storage Device Driver Programming Guide
apple_id: TP40000974
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2007-04-03'
source_url: https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/MassStorage/06_LUD_Example/MS_LUD_Example.html
archived_at: '2026-07-15T07:31:32.846155Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Mass Storage Device Driver Programming Guide](Introduction%20to%20Mass%20Storage%20Device%20Driver%20Programming%20Guide.md)


[Next](Subclassing%20Protocol%20Services%20Drivers.md)[Previous](Developing%20a%20Universal%20Binary.md)

# Subclassing Logical Unit Drivers

The SCSI Architecture Model defines several shared command set specifications, each associated with a peripheral device type. These specifications document how SCSI commands are processed by a device’s firmware. If your device does not conform with the shared command set specification for its peripheral device type in some way, either because it processes commands differently or because it services additional commands, you need to subclass the appropriate Apple logical unit driver to provide the support your device requires.

This chapter describes how to subclass an Apple-provided logical unit driver to address SCSI command set implementation issues. The sample code in this chapter is generic and emphasizes the form your driver should take, rather than the code required to implement a specific command. Because the sample drivers are generic, they will not attach to a particular device. To test them with your device, replace the generic values for parameters such as vendor or product identification with values that identify your device. For more information on how to develop kernel extensions in general and I/O Kit drivers in particular, see _[Kernel Extension Programming Topics](../../Darwin/Kernel%20Extension%20Programming%20Topics/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrt)_ and _[IOKit Device Driver Design Guidelines](../IOKit%20Device%20Driver%20Design%20Guidelines/Introduction%20to%20I-O%20Kit%20Device%20Driver%20Design%20Guidelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmoju)_.

This chapter also contains code that shows how your driver can use a `SCSITask` object to send a command to a device and how to use the SCSI Architecture Model family’s command-builder functions to build a custom CDB.

This section describes how to create your driver project and edit your driver’s information property list (`Info.plist` file). The sample driver in this chapter is a logical unit driver for a generic CD-ROM device so it is a subclass of the Apple-provided `IOSCSIPeripheralDeviceType05` driver.

The sample project uses `MyLogicalUnitDriver` for the name of the driver and generic values such as `MySoftwareCompany` for the developer name. You should replace these names and values with your own information in order to test this code with your device.

Open the Xcode application and create a new I/O Kit driver project named `MyLogicalUnitDriver`. Specify a directory for the new project or accept the default.

When you create a new I/O Kit driver project, Xcode supplies several files, including two empty source files—`MyLogicalUnitDriver.h` and `MyLogicalUnitDriver.cpp`. Before you add any code to these files, however, you should edit your driver’s information property list.

Every driver has an `Info.plist` file that contains information about the driver and what it needs, including its personalities. As described in [Driver Personalities and the Matching Process](Mass%20Storage%20Driver%20Matching%20and%20Loading.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomzwfvbeeskejjfeora), a driver’s personality contains the matching information the I/O Kit uses to determine the appropriate driver for a device. To make sure your driver loads for your device, you add several properties to its personality dictionary that identify the device or type of device it supports.

In Xcode, a driver’s `Info.plist` file is listed in the Groups & Files view in the project. You can edit the property list file as plain XML text in the Xcode editor window or you can choose a different application (such as Property List Editor) to use. For more information on how to select another editor, see [Hello I/O Kit: Creating a Driver With Xcode](https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/KEXTConcept/KEXTConceptIOKit/iokit_tutorial.html#//apple_ref/doc/uid/20002366).

The `IOKitPersonalities` dictionary in the driver’s `Info.plist` file can contain multiple personality dictionaries, one for each device or type of device your driver supports. The sample driver in this chapter implements only one personality dictionary but you can create additional dictionaries if your driver can support more than one device or device type.

The sample code uses the following six property keys:

- `CFBundleIdentifier`
- `IOClass`
- `IOProviderClass`
- `Peripheral Device Type`
- `Vendor Identification`
- `Product Identification`

If you are developing a driver for a particular version of your device, you can add the product revision identification key to the personality for even more specific matching.

Using your chosen editing environment, create a new child of the `IOKitPersonalities` dictionary. Make the name of this new child `MyLogicalUnitDriver` and set its class to Dictionary.

Create six new children of the `MyLogicalUnitDriver` dictionary, one for each of the six properties you’ll be adding. [Table 5-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomzxfvbucscgjjceiri) shows the properties, along with their classes and values. To test the sample code with your device, replace values such as `MyProductIdentification` with actual values for your device.

__Table 5-1__  Personality properties for MyLogicalUnitDriver

| Property | Class | Value |
| `CFBundleIdentifier` | String | `com.MySoftwareCompany.driver.MyLogicalUnitDriver` |
| `IOClass` | String | `com_MySoftwareCompany_driver_MyLogicalUnitDriver` |
| `IOProviderClass` | String | `IOSCSIPeripheralDeviceNub` |
| `Peripheral Device Type` | Number | `5` |
| `Vendor Identification` | String | `MyProductIdentification` |
| `Product Identification` | String | `MyVendorIdentification` |

A driver declares its dependencies on other loadable kernel extensions and in-kernel components in the `OSBundleLibraries` dictionary. Each dependency has a string value that declares the earliest version of the dependency the driver is compatible with.

The sample driver depends on two loadable extensions from the `IOSCSIArchitectureModel` family. To add these dependencies to the `OSBundleLibraries` dictionary, you create a new child for each dependency. [Table 5-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomzxfvbucscjircuira) shows the dependencies you add for the sample driver.

__Table 5-2__  Dependencies for MyLogicalUnitDriver

| Property | Class | Value |
| `com.apple.iokit.IOSCSIArchitectureModelFamily` | String | `1.0.0` |
| `com.apple.iokit.IOSCSIMultimediaCommandsDevice` | String | `1.0.0` |

Because the driver of a CD-ROM drive must be able to mount root on a local volume, you add the `OSBundleRequired` property to the top level of its `Info.plist` file. In other words, the new `OSBundleRequired` property is a sibling of the `IOKitPersonalities` and `OSBundleLibraries` dictionaries, not a child. Edit the new element to match the following: 

```
OSBundleRequired        String  Local-Root
```


This section describes some of the elements that must be included in your driver’s source files. To demonstrate the process of subclassing, the sample driver simply overrides the `GetConfiguration` method and prints a message. You should replace this trivial function with your own code that supports your device’s particular command implementations.

In Xcode, the driver’s source files are listed in the Groups & Files pane, revealed by the discosure triangle next to the `MyLogicalUnitDriver` project and the disclosure triangle next to the Source folder.

The header file provides access to external declarations and supporting type definitions needed by the functions and objects in the C++ file. The header for the sample driver is simple because it includes only one method declaration. Edit the `MyLogicalUnitDriver.h` file to match the code in [Listing 5-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomzxfvbuurckjfduuqq).

__Listing 5-1__  The MyLogicalUnitDriver header file

```c
#ifndef _MyLogicalUnitDriver_H_
#define _MyLogicalUnitDriver_H_

// Because the sample driver is a subclass of the Apple-provided
// peripheral device type 05 driver, it must include that driver's
// header file.
#include <IOKit/scsi-commands/IOSCSIPeripheralDeviceType05.h>

// Here, the sample driver declares its inheritance and the method
// it overrides.
class com_MySoftwareCompany_driver_MyLogicalUnitDriver : public
        IOSCSIPeripheralDeviceType05
{
    OSDeclareDefaultStructors (
                com_MySoftwareCompany_driver_MyLogicalUnitDriver )
protected:
    virtual IOReturn GetConfiguration ( void );
};

#endif /* _MyLogicalUnitDriver_H_ */
```


The C++ file provides the code to override the chosen methods. The sample driver’s C++ file contains all the elements required for a subclassed driver even though it accomplishes nothing more substantial than a message sent to the system log file, `/var/log/system.log`.

Edit the `MyLogicalUnitDriver.cpp` file to match the code in [Listing 5-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomzxfvbuurckjjbeiry).

__Listing 5-2__  The MyLogicalUnitDriver C++ file

```c
// Include the header file you created
#include "MyLogicalUnitDriver.h"

// This definition allows you to use the more convenient "super" in
// place of "IOSCSIPeripheralDeviceType05", where appropriate.
#define super IOSCSIPeripheralDeviceType05

// This macro must appear before you define any of your class's methods.
// Note that you must use the literal name of the superclass here, not
// "super" as defined above.
OSDefineMetaClassAndStructors (
        com_MySoftwareCompany_driver_MyLogicalUnitDriver,
        IOSCSIPeripheralDeviceType05 );

// Define the method to override.
IOReturn
com_MySoftwareCompany_driver_MyLogicalUnitDriver::GetConfiguration ( void )
{
    IOLog( "MyLogicalUnitDriver overriding GetConfiguration\n" );
// You can add code that accesses your device here.
// Call super's GetConfiguration method before returning.
    return super::GetConfiguration();
}
```


This section presents some advice on testing your driver. You cannot use `kextload` to load and test your driver “by hand” because there are generic drivers that will always load in its place at boot time. Therefore, you need to make sure you have multiple bootable disks or partitions so you can remove your driver if it behaves badly and reboot the disk or partition.

Because the `OSBundleRequired` property in the sample driver’s `Info.plist` file is set to `Local-Root`, the BootX booter will automatically load it when the system is restarted (for more information on this process, see Loading Kernel Extensions at Boot Time).

For help with debugging, you can open a window in the Terminal application (located at `/Applications/Utilities/Terminal`) and type the following line to view the system log:

```
tail -f /var/log/system.log
```


As described in [The Transport Driver Layer](Mass%20Storage%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomzufvbeur2fjjbuusq), a logical unit driver subclass creates a `SCSITask` object to contain a command descriptor block (or CDB) and various status indicators related to the execution of a SCSI command. To create a command to put into a `SCSITask` object, you can use the built-in command-creation functions or you can build a custom CDB. The built-in command-creation functions are appropriate when you need to send standard SCSI commands, such as `INQUIRY`, `TEST_UNIT_READY`, and `REPORT_SENSE`. When you need to send a vendor-specific SCSI command, you use the `SetCommandDescriptorBlock` function to build an appropriately sized CDB. Note that `SetCommandDescriptorBlock` and the built-in command-creation functions are defined in `IOSCSIPrimaryCommandsDevice.h`. The sample code in this section shows both ways to build and send SCSI commands.

The code in this section shows a simple logical unit driver for a block commands device, specifically, a subclass of `IOSCSIPeripheralDeviceType00`. It shows how to use one of the built-in command-creation functions and it demonstrates how to set up your own command-creation function to build a custom command. It also shows how to check the command response and the status of the `SCSITask` object. Listing 5-3 shows the header file for the sample driver.

__Listing 5-3__  Header file for a driver that sends standard and custom SCSI commands

```c
#ifndef _SampleINQUIRYDriver_H_
#define _SampleINQUIRYDriver_H_
#include <IOKit/scsi/IOSCSIPeripheralDeviceType00.h>

class com_MySoftwareCompany_driver_SampleINQUIRYDriver : public IOSCSIPeripheralDeviceType00
{
    OSDeclareDefaultStructors ( com_MySoftwareCompany_driver_SampleINQUIRYDriver )

protected:
    bool    InitializeDeviceSupport ( void );
    void    SendBuiltInINQUIRY ( void );
    void    SendCreatedINQUIRY ( void );
    bool    BuildINQUIRY ( SCSITaskIdentifier    request,
                           IOBufferMemoryDescriptor *    buffer,
                           SCSICmdField1Bit      CMDDT,
                           SCSICmdField1Bit      EVPD,
                           SCSICmdField1Byte     PAGE_OR_OPERATION_CODE,
                           SCSICmdField1Byte     ALLOCATION_LENGTH,
                           SCSICmdField1Byte     CONTROL );
};
#endif /* _SampleINQUIRYDriver_H_ */
```

Listing 5-4 shows the implementation of the sample driver. Although there is some error handling shown, you should add more extensive error-handling code when you use this sample as the basis for an actual driver.

__Listing 5-4__  Implementation of a driver that sends standard and custom SCSI commands

```c
#include <IOKit/IOBufferMemoryDescriptor.h>
#include <IOKit/scsi/SCSICmds_INQUIRY_Definitions.h>
#include <IOKit/scsi/SCSICommandOperationCodes.h>
#include <IOKit/scsi/SCSITask.h>
#include "SampleINQUIRYDriver.h"
#define super IOSCSIPeripheralDeviceType00

OSDefineMetaClassAndStructors ( com_MySoftwareCompany_driver_SampleINQUIRYDriver, IOSCSIPeripheralDeviceType00 );

bool
com_MySoftwareCompany_driver_SampleINQUIRYDriver::InitializeDeviceSupport ( void )
{
    bool    result = false;
    result = super::InitializeDeviceSupport ( );
    if ( result == true ) {
        SendBuiltInINQUIRY ( );
        SendCreatedINQUIRY ( );
    }
    return result;
}

void
com_MySoftwareCompany_driver_SampleINQUIRYDriver::SendBuiltInINQUIRY ( void )
{
    // The Service Response represents the execution status of a service request.
    SCSIServiceResponse                serviceResponse = kSCSIServiceResponse_SERVICE_DELIVERY_OR_TARGET_FAILURE;
    IOBufferMemoryDescriptor *         buffer  = NULL;
    SCSITaskIdentifier                 request = NULL;
    UInt8 *                            ptr     = NULL;
    // Get a new IOBufferMemoryDescriptor object with a buffer large enough
    // to hold the SCSICmd_INQUIRY_StandardData structure (defined
    // in SCSICmds_INQUIRY_Definitions.h).
    buffer = IOBufferMemoryDescriptor::withCapacity ( sizeof ( SCSICmd_INQUIRY_StandardData ), kIODirectionIn, false );


    require ( ( buffer != NULL ), ErrorExit );

    // Get the address of the beginning of the buffer and zero-fill the buffer.
    ptr = ( UInt8 * ) buffer->getBytesNoCopy ( );
    bzero ( ptr, buffer->getLength ( ) );

    // Create a new SCSITask object; if unsuccessful, release

    request = GetSCSITask ( );
    require ( ( request != NULL ), ReleaseBuffer );

    // Prepare the buffer for an I/O transaction. This call must be
    // balanced by a call to the complete method (shown just before
    // ReleaseTask).
    require ( ( buffer->prepare ( ) == kIOReturnSuccess ), ReleaseTask );

    // Use the INQUIRY method to assemble the command. Then use the
    // SendCommand method to synchronously issue the request.

    if ( INQUIRY (  request,
                    buffer,
                    0,
                    0,
                    0x00,
                    buffer->getLength ( ),
                    0 ) == true )
    {
        serviceResponse = SendCommand ( request, kTenSecondTimeoutInMS );
    }

    // Check the SendCommand method's return value and the status of the SCSITask object.
    if ( ( serviceResponse == kSCSIServiceResponse_TASK_COMPLETE ) &&
           GetTaskStatus ( request ) == kSCSITaskStatus_GOOD )
    {
        IOLog ( "INQUIRY succeeded\n" );
    }
    else
    {
        IOLog ( "INQUIRY failed\n" );
    }

    // Complete the processing of this buffer after the I/O transaction
    // (this call balances the earlier call to prepare).
    buffer->complete ( );

// Clean up before exiting.
ReleaseTask:
    require_quiet ( ( request != NULL ), ReleaseBuffer );
    ReleaseSCSITask ( request );
    request = NULL;

ReleaseBuffer:
    require_quiet ( ( buffer != NULL ), ErrorExit );
    buffer->release ( );
    buffer = NULL;

ErrorExit:
    return;
}

void
com_MySoftwareCompany_driver_SampleINQUIRYDriver::SendCreatedINQUIRY ( void )
{
    SCSIServiceResponse                serviceResponse = kSCSIServiceResponse_SERVICE_DELIVERY_OR_TARGET_FAILURE;
    IOBufferMemoryDescriptor *        buffer            = NULL;
    SCSITaskIdentifier                request            = NULL;
    UInt8 *                            ptr                = NULL;

    // Get a new IOBufferMemoryDescriptor object with a buffer large enough
    // to hold the SCSICmd_INQUIRY_StandardData structure (defined in
    // SCSICmds_INQUIRY_Definitions.h).
    buffer = IOBufferMemoryDescriptor::withCapacity ( sizeof ( SCSICmd_INQUIRY_StandardData ), kIODirectionIn, false );

    // Return immediately if the buffer wasn't created.
    require ( ( buffer != NULL ), ErrorExit );

    // Get the address of the beginning of the buffer and zero-fill the buffer.
    ptr = ( UInt8 * ) buffer->getBytesNoCopy ( );
    bzero ( ptr, buffer->getLength ( ) );

    // Create a new SCSITask object; if unsuccessful, release the buffer and return.
    request = GetSCSITask ( );
    require ( ( request != NULL ), ReleaseBuffer );

    // Prepare the buffer for an I/O transaction. This call must be
    // balanced by a call to the complete method (shown just before
    // ReleaseTask).
    require ( ( buffer->prepare ( ) == kIOReturnSuccess ), ReleaseTask );

    // The BuildINQUIRY function shows how you can design and use a
    // command-building function to create a custom command to send
    // to your device. Although the BuildINQUIRY function builds a standard INQUIRY
    // command from the passed-in values, you do not create a custom function to
    // build a standard command in a real driver. Instead, you use the SCSI
    // Architecture Model family's built-in command-building functions. The
    // BuildINQUIRY function uses INQUIRY as an example merely because
    // it is a well-understood command.
    if ( BuildINQUIRY ( request,
                        buffer,
                        0x00, // CMDDT (Command support data)
                        0x00, // EVPD  (Vital product data)
                        0x00, // PAGE_OR_OPERATION_CODE
                        buffer->getLength ( ), // ALLOCATION_LENGTH
                        0x00 )  // CONTROL
                == true)
    {
        serviceResponse = SendCommand ( request, kTenSecondTimeoutInMS );
    }
    if ( ( serviceResponse == kSCSIServiceResponse_TASK_COMPLETE ) &&
           GetTaskStatus ( request ) == kSCSITaskStatus_GOOD )
    {
        IOLog ( "Vendor-created INQUIRY command succeeded\n" );
    }
    else
    {
        IOLog ( "Vendor-created INQUIRY command failed\n" );
    }

    buffer->complete ( );

ReleaseTask:
    require_quiet ( ( request != NULL ), ReleaseBuffer );
    ReleaseSCSITask ( request );
    request = NULL;

ReleaseBuffer:
    require_quiet ( ( buffer != NULL ), ErrorExit );
    buffer->release ( );
    buffer = NULL;

ErrorExit:
    return;
}

bool
com_MySoftwareCompany_driver_SampleINQUIRYDriver::BuildINQUIRY (
                                            SCSITaskIdentifier    request,
                                            IOBufferMemoryDescriptor *    dataBuffer,
                                            SCSICmdField1Bit     CMDDT,
                                            SCSICmdField1Bit     EVPD,
                                            SCSICmdField1Byte     PAGE_OR_OPERATION_CODE,
                                            SCSICmdField1Byte     ALLOCATION_LENGTH,
                                            SCSICmdField1Byte     CONTROL )
{
    bool result = false;

    // Validate the parameters here.
    require ( ( request != NULL ), ErrorExit );
    require ( ResetForNewTask ( request ), ErrorExit );

    // The helper functions ensure that the parameters fit within the
    // CDB fields and that the buffer passed in is large enough for
    // the transfer length.
    require ( IsParameterValid ( CMDDT, kSCSICmdFieldMask1Bit ), ErrorExit );
    require ( IsParameterValid ( EVPD, kSCSICmdFieldMask1Bit ), ErrorExit );
    require ( IsParameterValid ( PAGE_OR_OPERATION_CODE, kSCSICmdFieldMask1Byte ), ErrorExit );
    require ( IsParameterValid ( ALLOCATION_LENGTH, kSCSICmdFieldMask1Byte ), ErrorExit );
    require ( IsParameterValid ( CONTROL, kSCSICmdFieldMask1Byte ), ErrorExit );
    require ( IsMemoryDescriptorValid ( dataBuffer, ALLOCATION_LENGTH ), ErrorExit );

    // Check the validity of the PAGE_OR_OPERATION_CODE parameter, when using both the CMDDT and EVPD parameters.

    if ( PAGE_OR_OPERATION_CODE != 0 )
    {
        if ( ( ( CMDDT == 1 ) && ( EVPD == 1 ) ) || ( ( CMDDT == 0 ) && ( EVPD == 0 ) ) )
        {
            goto ErrorExit;
        }
    }

    // This is a 6-byte command: fill out the CDB appropriately
    SetCommandDescriptorBlock ( request,
                                kSCSICmd_INQUIRY,
                                ( CMDDT << 1 ) | EVPD,
                                PAGE_OR_OPERATION_CODE,
                                0x00,
                                ALLOCATION_LENGTH,
                                CONTROL );

    SetDataTransferDirection ( request, kSCSIDataTransfer_FromTargetToInitiator );
    SetTimeoutDuration ( request, 0 );
    SetDataBuffer ( request, dataBuffer );
    SetRequestedDataTransferCount ( request, ALLOCATION_LENGTH );

    result = true;

ErrorExit:
    return result;
}
```


[Next](Subclassing%20Protocol%20Services%20Drivers.md)[Previous](Developing%20a%20Universal%20Binary.md)

