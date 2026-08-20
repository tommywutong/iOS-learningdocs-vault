---
title: USB Device Interface Guide
apple_id: TP40000973
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: IOKit
published: '2012-01-09'
source_url: https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/USBBook/USBDeviceInterfaces/USBDevInterfaces.html
archived_at: '2026-07-15T07:31:34.664977Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [USB Device Interface Guide](Introduction%20to%20USB%20Device%20Interface%20Guide.md)


[Next](Document%20Revision%20History.md)[Previous](USB%20Device%20Overview.md)

# Working With USB Device Interfaces

This chapter describes how to develop a user-space tool that finds and communicates with an attached USB device and one of its interfaces.

Applications running in OS X get access to USB devices by using I/O Kit functions to acquire a device interface, a type of plug-in that specifies functions the application can call to communicate with the device. The USB family provides two types of device interface:

- `IOUSBDeviceInterface` for communicating with the device itself
- `IOUSBInterfaceInterface` for communicating with an interface in the device

Both device interfaces are defined in `/System/Library/Frameworks/IOKit.framework/Headers/usb/IOUSBLib.h`.

Communicating with the device itself is usually only necessary when you need to set or change its configuration. For example, vendor-specific devices are often not configured because there are no default drivers that set a particular configuration. In this case, your application must use the device interface for the device to set the configuration it needs so the interfaces become available.

The process of finding and communicating with a USB device is divided into two sets of steps. The first set outlines how to find a USB device, acquire a device interface of type `IOUSBDeviceInterface` for it, and set or change its configuration. The second set describes how to find an interface in a device, acquire a device interface of type `IOUSBInterfaceInterface` for it, and use it to communicate with that interface. If you need to communicate with an unconfigured device or if you need to change a device’s configuration, you follow both sets of steps. If you need to communicate with a device that is already configured to your specification, you follow only the second set of steps. The sample code in [Accessing a USB Device](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnbvfvbeeskeireegsi) follows both sets of steps and extends them to include setting up notifications it can receive when devices are dynamically added or removed.

Follow this first set of steps _only_ to set or change the configuration of a device. If the device you’re interested in is already configured for your needs, skip these steps and follow the second set of steps.

1. Find the `IOUSBDevice` object that represents the device in the I/O Registry. This includes setting up a matching dictionary with a key from the _USB Common Class Specification_ (see [Finding USB Devices and Interfaces](USB%20Device%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnbufvbeeskei5buqqq)). The sample code uses the key elements `kUSBVendorName` and `kUSBProductName` to find a particular USB device (this is the second key listed in [Table 1-2](USB%20Device%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnbufvbeeq2di5cukrq)).
2. Create a device interface of type `IOUSBDeviceInterface` for the device. This device interface provides functions that perform tasks such as setting or changing the configuration of the device, getting information about the device, and resetting the device.
3. Examine the device’s configurations with `GetConfigurationDescriptorPtr`, choose the appropriate one, and call `SetConfiguration` to set the device’s configuration and instantiate the `IOUSBInterface` objects for that configuration.

Follow this second set of steps to find and choose an interface, acquire a device interface for it, and communicate with the device.

1. Create an interface iterator to iterate over the available interfaces.
2. Create a device interface for each interface so you can examine its properties and select the appropriate one. To do this, you create a device interface of type `IOUSBInterfaceInterface`. This device interface provides functions that perform tasks such as getting information about the interface, setting the interface’s alternate setting, and accessing its pipes.
3. Use the `USBInterfaceOpen` function to open the selected interface. This will cause the pipes associated with the interface to be instantiated so you can examine the properties of each and select the appropriate one.
4. Communicate with the device through the selected pipe. You can write to and read from the pipe synchronously or asynchronously—the sample code in [Accessing a USB Device](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnbvfvbeeskeireegsi) shows how to do both.

This section provides snippets of sample code that show how to access a Cypress EZ-USB chip with an 8051 microcontroller core. The sample code follows the first set of steps in section [Using USB Device Interfaces](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnbvfvbeeskiineuqqq) to find the Cypress EZ-USB chip in its default, unprogrammed state (also referred to as the “raw device”). It then configures the device and downloads firmware provided by Cypress to program the chip to behave as a device that echoes all information it receives on its bulk out pipe to its bulk in pipe.

Once the chip has been programmed, the device nub representing the default, unprogrammed device is detached from the I/O Registry and a new device nub, representing the programmed chip, is attached. To communicate with the programmed chip (also referred to as the “bulk test device”), the sample code must perform the first set of steps again to find the device, create a device interface for it, and configure it. Then it performs the second set of steps to find an interface, create a device interface for it, and test the device. The sample code also shows how to set up notifications for the dynamic addition and removal of a device.

The code in the USB Notification Example uses the definitions and global variables shown in [Listing 2-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnbvfvbugsccjfeeisi). The definition of `USE_ASYNC_IO` allows you to choose to use either synchronous or asynchronous calls to read from and write to the chip by commenting out the line or leaving it in, respectively. The definition of `kTestMessage` sets up a simple message to write to the device. The remaining definitions are specific to the Cypress EZ-USB chip.

__Listing 2-1__  Definitions and global variables

```
#define USE_ASYNC_IO    //Comment this line out if you want to use
                        //synchronous calls for reads and writes
#define kTestMessage        "Bulk I/O Test"
#define k8051_USBCS         0x7f92
#define kOurVendorID        1351    //Vendor ID of the USB device
#define kOurProductID           8193    //Product ID of device BEFORE it
                                        //is programmed (raw device)
#define kOurProductIDBulkTest   4098    //Product ID of device AFTER it is
                                        //programmed (bulk test device)

//Global variables
static IONotificationPortRef    gNotifyPort;
static io_iterator_t            gRawAddedIter;
static io_iterator_t            gRawRemovedIter;
static io_iterator_t            gBulkTestAddedIter;
static io_iterator_t            gBulkTestRemovedIter;
static char                     gBuffer[64];
```


The `main` function in the USB Notification Example project (contained in the file `main.c`) accomplishes the following tasks.

- It establishes communication with the I/O Kit and sets up a matching dictionary to find the Cypress EZ-USB chip.
- It sets up an asynchronous notification to be called when an unprogrammed (raw) device is first attached to the I/O Registry and another to be called when the device is removed.
- It modifies the matching dictionary to find the programmed (bulk test) device.
- It sets up additional notifications to be called when the bulk test device is first attached or removed.
- It starts the run loop so the notifications that have been set up will be received.

The `main` function uses I/O Kit functions to set up and modify a matching dictionary and set up notifications, and Core Foundation functions to set up the run loop for receiving the notifications. It calls the following functions to access both the raw device and the bulk test device.

- `RawDeviceAdded`, shown in [Listing 2-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnbvfvbeeskfjbeeori), iterates over the set of matching devices and creates a device interface for each one. It calls `ConfigureDevice` (shown in [Listing 2-5](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnbvfvbeeskkivfeksi)) to set the device’s configuration, and then `DownloadToDevice` (shown in [Listing 2-6](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnbvfvbeeskgijfeuqi)) to download the firmware to program it.
- `RawDeviceRemoved`, shown in [Listing 2-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnbvfvbeeskiizfemsq), iterates over the set of matching devices and releases each one in turn.
- `BulkTestDeviceAdded`, shown in [Listing 2-7](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnbvfvbeeskcifduisa), iterates over the new set of matching devices, creates a device interface for each one, and calls `ConfigureDevice` (shown in [Listing 2-5](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnbvfvbeeskkivfeksi)) to set the device’s configuration. It then calls `FindInterfaces` (shown in [Listing 2-8](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnbvfvbeeskfjfcussi)) to get access to the interfaces on the device.
- `BulkTestDeviceRemoved` iterates over the new set of matching devices and releases each one in turn. This function is not shown in this chapter; see `RawDeviceRemoved` ([Listing 2-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnbvfvbeeskiizfemsq)) for a nearly identical function.

__Listing 2-2__  The main function

```
int main (int argc, const char *argv[])
{
    mach_port_t             masterPort;
    CFMutableDictionaryRef  matchingDict;
    CFRunLoopSourceRef      runLoopSource;
    kern_return_t           kr;
    SInt32                  usbVendor = kOurVendorID;
    SInt32                  usbProduct = kOurProductID;

    // Get command line arguments, if any
    if (argc > 1)
        usbVendor = atoi(argv[1]);
    if (argc > 2)
        usbProduct = atoi(argv[2]);

    //Create a master port for communication with the I/O Kit
    kr = IOMasterPort(MACH_PORT_NULL, &masterPort);
    if (kr || !masterPort)
    {
        printf("ERR: Couldn’t create a master I/O Kit port(%08x)\n", kr);
        return -1;
    }
    //Set up matching dictionary for class IOUSBDevice and its subclasses
    matchingDict = IOServiceMatching(kIOUSBDeviceClassName);
    if (!matchingDict)
    {
        printf("Couldn’t create a USB matching dictionary\n");
        mach_port_deallocate(mach_task_self(), masterPort);
        return -1;
    }

    //Add the vendor and product IDs to the matching dictionary.
    //This is the second key in the table of device-matching keys of the
    //USB Common Class Specification
    CFDictionarySetValue(matchingDict, CFSTR(kUSBVendorName),
                        CFNumberCreate(kCFAllocatorDefault,
                                     kCFNumberSInt32Type, &usbVendor));
    CFDictionarySetValue(matchingDict, CFSTR(kUSBProductName),
                        CFNumberCreate(kCFAllocatorDefault,
                                    kCFNumberSInt32Type, &usbProduct));

    //To set up asynchronous notifications, create a notification port and
    //add its run loop event source to the program’s run loop
    gNotifyPort = IONotificationPortCreate(masterPort);
    runLoopSource = IONotificationPortGetRunLoopSource(gNotifyPort);
    CFRunLoopAddSource(CFRunLoopGetCurrent(), runLoopSource,
                        kCFRunLoopDefaultMode);

    //Retain additional dictionary references because each call to
    //IOServiceAddMatchingNotification consumes one reference
    matchingDict = (CFMutableDictionaryRef) CFRetain(matchingDict);
    matchingDict = (CFMutableDictionaryRef) CFRetain(matchingDict);
    matchingDict = (CFMutableDictionaryRef) CFRetain(matchingDict);

    //Now set up two notifications: one to be called when a raw device
    //is first matched by the I/O Kit and another to be called when the
    //device is terminated
    //Notification of first match:
    kr = IOServiceAddMatchingNotification(gNotifyPort,
                    kIOFirstMatchNotification, matchingDict,
                    RawDeviceAdded, NULL, &gRawAddedIter);
    //Iterate over set of matching devices to access already-present devices
    //and to arm the notification
    RawDeviceAdded(NULL, gRawAddedIter);

    //Notification of termination:
    kr = IOServiceAddMatchingNotification(gNotifyPort,
                    kIOTerminatedNotification, matchingDict,
                    RawDeviceRemoved, NULL, &gRawRemovedIter);
    //Iterate over set of matching devices to release each one and to
    //arm the notification
    RawDeviceRemoved(NULL, gRawRemovedIter);

    //Now change the USB product ID in the matching dictionary to match
    //the one the device will have after the firmware has been downloaded
    usbProduct = kOurProductIDBulkTest;
    CFDictionarySetValue(matchingDict, CFSTR(kUSBProductName),
                        CFNumberCreate(kCFAllocatorDefault,
                                    kCFNumberSInt32Type, &usbProduct));

    //Now set up two notifications: one to be called when a bulk test device
    //is first matched by the I/O Kit and another to be called when the
    //device is terminated.
    //Notification of first match
    kr = IOServiceAddMatchingNotification(gNotifyPort,
                    kIOFirstMatchNotification, matchingDict,
                    BulkTestDeviceAdded, NULL, &gBulkTestAddedIter);
    //Iterate over set of matching devices to access already-present devices
    //and to arm the notification
    BulkTestDeviceAdded(NULL, gBulkTestAddedIter);

    //Notification of termination
    kr = IOServiceAddMatchingNotification(gNotifyPort,
                    kIOTerminatedNotification, matchingDict,
                    BulkTestDeviceRemoved, NULL, &gBulkTestRemovedIter);
    //Iterate over set of matching devices to release each one and to
    //arm the notification. NOTE: this function is not shown in this document.
    BulkTestDeviceRemoved(NULL, gBulkTestRemovedIter);

    //Finished with master port
    mach_port_deallocate(mach_task_self(), masterPort);
    masterPort = 0;

    //Start the run loop so notifications will be received
    CFRunLoopRun();

    //Because the run loop will run forever until interrupted,
    //the program should never reach this point
    return 0;
}
```


Now that you’ve obtained an iterator for a set of matching devices, you can use it to gain access to each raw device, configure it, and download the appropriate firmware to it. The function `RawDeviceAdded` (shown in [Listing 2-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnbvfvbeeskfjbeeori)) uses I/O Kit functions to create a device interface for each device and then calls the following functions to configure the device and download firmware to it.

- `ConfigureDevice`, shown in [Listing 2-5](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnbvfvbeeskkivfeksi), uses device interface functions to get the number of configurations, examine the first one, and set the device’s configuration.
- `DownloadToDevice`, shown in [Listing 2-6](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnbvfvbeeskgijfeuqi), downloads the firmware in `bulktest.c` to the device.

__Listing 2-3__  Accessing and programming the raw device

```swift
void RawDeviceAdded(void *refCon, io_iterator_t iterator)
{
    kern_return_t               kr;
    io_service_t                usbDevice;
    IOCFPlugInInterface         **plugInInterface = NULL;
    IOUSBDeviceInterface        **dev = NULL;
    HRESULT                     result;
    SInt32                      score;
    UInt16                      vendor;
    UInt16                      product;
    UInt16                      release;

    while (usbDevice = IOIteratorNext(iterator))
    {
        //Create an intermediate plug-in
        kr = IOCreatePlugInInterfaceForService(usbDevice,
                    kIOUSBDeviceUserClientTypeID, kIOCFPlugInInterfaceID,
                    &plugInInterface, &score);
        //Don’t need the device object after intermediate plug-in is created
        kr = IOObjectRelease(usbDevice);
        if ((kIOReturnSuccess != kr) || !plugInInterface)
        {
            printf("Unable to create a plug-in (%08x)\n", kr);
            continue;
        }
        //Now create the device interface
        result = (*plugInInterface)->QueryInterface(plugInInterface,
                        CFUUIDGetUUIDBytes(kIOUSBDeviceInterfaceID),
                        (LPVOID *)&dev);
        //Don’t need the intermediate plug-in after device interface
        //is created
        (*plugInInterface)->Release(plugInInterface);

        if (result || !dev)
        {
            printf("Couldn’t create a device interface (%08x)\n",
                                                    (int) result);
            continue;
        }

        //Check these values for confirmation
        kr = (*dev)->GetDeviceVendor(dev, &vendor);
        kr = (*dev)->GetDeviceProduct(dev, &product);
        kr = (*dev)->GetDeviceReleaseNumber(dev, &release);
        if ((vendor != kOurVendorID) || (product != kOurProductID) ||
            (release != 1))
        {
            printf("Found unwanted device (vendor = %d, product = %d)\n",
                    vendor, product);
            (void) (*dev)->Release(dev);
            continue;
        }

        //Open the device to change its state
        kr = (*dev)->USBDeviceOpen(dev);
        if (kr != kIOReturnSuccess)
        {
            printf("Unable to open device: %08x\n", kr);
            (void) (*dev)->Release(dev);
            continue;
        }
        //Configure device
        kr = ConfigureDevice(dev);
        if (kr != kIOReturnSuccess)
        {
            printf("Unable to configure device: %08x\n", kr);
            (void) (*dev)->USBDeviceClose(dev);
            (void) (*dev)->Release(dev);
            continue;
        }

        //Download firmware to device
        kr = DownloadToDevice(dev);
        if (kr != kIOReturnSuccess)
        {
            printf("Unable to download firmware to device: %08x\n", kr);
            (void) (*dev)->USBDeviceClose(dev);
            (void) (*dev)->Release(dev);
            continue;
        }

        //Close this device and release object
        kr = (*dev)->USBDeviceClose(dev);
        kr = (*dev)->Release(dev);
    }
}
```

The function `RawDeviceRemoved` simply uses the iterator obtained from the `main` function (shown in [Listing 2-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnbvfvbeeskgizausqi)) to release each device object. This also has the effect of arming the raw device termination notification so it will notify the program of future device removals. `RawDeviceRemoved` is shown in [Listing 2-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnbvfvbeeskiizfemsq).

__Listing 2-4__  Releasing the raw device objects

```
void RawDeviceRemoved(void *refCon, io_iterator_t iterator)
{
    kern_return_t   kr;
    io_service_t    object;

    while (object = IOIteratorNext(iterator))
    {
        kr = IOObjectRelease(object);
        if (kr != kIOReturnSuccess)
        {
            printf("Couldn’t release raw device object: %08x\n", kr);
            continue;
        }
    }
}
```

Although every USB device has one or more configurations, unless the device is a composite class device that’s been matched by the `AppleUSBComposite` driver which automatically sets the first configuration, none of those configurations may have been set. Therefore, your application may have to use device interface functions to get the appropriate configuration value and use it to set the device’s configuration. In the sample code, the function `ConfigureDevice` (shown in [Listing 2-5](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnbvfvbeeskkivfeksi)) accomplishes this task. In fact, it is called twice: once by `RawDeviceAdded` to configure the raw device and again by `BulkTestDeviceAdded` (shown in [Listing 2-7](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnbvfvbeeskcifduisa)) to configure the bulk test device.

__Listing 2-5__  Configuring a USB device

```swift
IOReturn ConfigureDevice(IOUSBDeviceInterface **dev)
{
    UInt8                           numConfig;
    IOReturn                        kr;
    IOUSBConfigurationDescriptorPtr configDesc;

    //Get the number of configurations. The sample code always chooses
    //the first configuration (at index 0) but your code may need a
    //different one
    kr = (*dev)->GetNumberOfConfigurations(dev, &numConfig);
    if (!numConfig)
        return -1;

    //Get the configuration descriptor for index 0
    kr = (*dev)->GetConfigurationDescriptorPtr(dev, 0, &configDesc);
    if (kr)
    {
        printf("Couldn’t get configuration descriptor for index %d (err =
                %08x)\n", 0, kr);
        return -1;
    }

    //Set the device’s configuration. The configuration value is found in
    //the bConfigurationValue field of the configuration descriptor
    kr = (*dev)->SetConfiguration(dev, configDesc->bConfigurationValue);
    if (kr)
    {
        printf("Couldn’t set configuration to value %d (err = %08x)\n", 0,
                kr);
        return -1;
    }
    return kIOReturnSuccess;
}
```

Now that the device is configured, you can download firmware to it. Cypress makes firmware available to program the EZ-USB chip to emulate different devices. The sample code in this document uses firmware that programs the chip to be a bulk test device, a device that takes the data it receives from its bulk out pipe and echoes it to its bulk in pipe. The firmware, contained in the file `bulktest.c`, is an array of `INTEL_HEX_RECORD` structures (defined in the file `hex2c.h`).

The function `DownloadToDevice` uses the function `WriteToDevice` (shown together in [Listing 2-6](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnbvfvbeeskgijfeuqi)) to prepare the device to receive the download and then to write information from each structure to the appropriate address on the device. When all the firmware has been downloaded, `DownloadToDevice` calls `WriteToDevice` a last time to inform the device that the download is complete. At this point, the raw device detaches itself from the bus and reattaches as a bulk test device. This causes the device nub representing the raw device to be removed from the I/O Registry and a new device nub, representing the bulk test device, to be attached.

__Listing 2-6__  Two functions to download firmware to the raw device

```swift
IOReturn DownloadToDevice(IOUSBDeviceInterface **dev)
{
    int         i;
    UInt8       writeVal;
    IOReturn    kr;

    //Assert reset. This tells the device that the download is
    //about to occur
    writeVal = 1;   //For this device, a value of 1 indicates a download
    kr = WriteToDevice(dev, k8051_USBCS, 1, &writeVal);
    if (kr != kIOReturnSuccess)
    {
        printf("WriteToDevice reset returned err 0x%x\n", kr);
        (*dev)->USBDeviceClose(dev);
        (*dev)->Release(dev);
        return kr;
    }

    //Download firmware
    i = 0;
    while (bulktest[i].Type == 0)   //While bulktest[i].Type == 0, this is
    {                               //not the last firmware record to
                                    //download
        kr = WriteToDevice(dev, bulktest[i].Address,
                            bulktest[i].Length, bulktest[i].Data);
        if (kr != kIOReturnSuccess)
        {
            printf("WriteToDevice download %i returned err 0x%x\n", i,
                    kr);
            (*dev)->USBDeviceClose(dev);
            (*dev)->Release(dev);
            return kr;
        }
        i++;
    }

    //De-assert reset. This tells the device that the download is complete
    writeVal = 0;
    kr = WriteToDevice(dev, k8051_USBCS, 1, &writeVal);
    if (kr != kIOReturnSuccess)
        printf("WriteToDevice run returned err 0x%x\n", kr);

    return kr;
}


IOReturn WriteToDevice(IOUSBDeviceInterface **dev, UInt16 deviceAddress,
                        UInt16 length, UInt8 writeBuffer[])
{
    IOUSBDevRequest     request;

    request.bmRequestType = USBmakebmRequestType(kUSBOut, kUSBVendor,
                                                kUSBDevice);
    request.bRequest = 0xa0;
    request.wValue = deviceAddress;
    request.wIndex = 0;
    request.wLength = length;
    request.pData = writeBuffer;

    return (*dev)->DeviceRequest(dev, &request);
}
```


After you download the firmware to the device, the raw device is no longer attached to the bus. To gain access to the bulk test device, you repeat most of the same steps you used to get access to the raw device.

- Use the iterator obtained by a call to `IOServiceAddMatchingNotification` in the `main` function (shown in [Listing 2-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnbvfvbeeskgizausqi)) to iterate over a set of matching devices.
- Create a device interface for each device.
- Configure the device.

This time, however, the next step is to find the interfaces on the device so you can choose the appropriate one and get access to its pipes. Because of the similarities of these tasks, the function `BulkTestDeviceAdded` follows the same outline of the `RawDeviceAdded` function except that instead of downloading firmware to the device, it calls `FindInterfaces` (shown in [Listing 2-8](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnbvfvbeeskfjfcussi)) to examine the available interfaces and their pipes. The code in [Listing 2-7](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnbvfvbeeskcifduisa) replaces most of the `BulkTestDeviceAdded` function’s code with comments, focusing on the differences between it and the `RawDeviceAdded` function.

__Listing 2-7__  Accessing the bulk test device

```swift
void BulkTestDeviceAdded(void *refCon, io_iterator_t iterator)
{
    kern_return_t           kr;
    io_service_t            usbDevice;
    IOUSBDeviceInterface    **device=NULL;

    while (usbDevice = IOIteratorNext(iterator))
    {
        //Create an intermediate plug-in using the
        //IOCreatePlugInInterfaceForService function

        //Release the device object after getting the intermediate plug-in

        //Create the device interface using the QueryInterface function

        //Release the intermediate plug-in object

        //Check the vendor, product, and release number values to
        //confirm we’ve got the right device

        //Open the device before configuring it
        kr = (*device)->USBDeviceOpen(device);

        //Configure the device by calling ConfigureDevice

        //Close the device and release the device interface object if
        //the configuration is unsuccessful

        //Get the interfaces
        kr = FindInterfaces(device);
        if (kr != kIOReturnSuccess)
        {
            printf("Unable to find interfaces on device: %08x\n", kr);
            (*device)->USBDeviceClose(device);
            (*device)->Release(device);
            continue;
        }

//If using synchronous IO, close and release the device interface here
#ifndef USB_ASYNC_IO
        kr = (*device)->USBDeviceClose(device);
        kr = (*device)->Release(device);
#endif
    }
}
```

The function `BulkTestDeviceRemoved` simply uses the iterator obtained from the `main` function (shown in [Listing 2-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnbvfvbeeskgizausqi)) to release each device object. This also has the effect of arming the bulk test device termination notification so it will notify the program of future device removals.The `BulkTestDeviceRemoved` function is identical to the `RawDeviceRemoved` function (shown in [Listing 2-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnbvfvbeeskiizfemsq)), with the exception of the wording of the printed error statement.

Now that you’ve configured the device, you have access to its interfaces. The `FindInterfaces` function (shown in [Listing 2-8](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnbvfvbeeskfjfcussi)) creates an iterator to iterate over all interfaces on the device and then creates a device interface to communicate with each one. For each interface found, the function opens the interface, determines how many endpoints (or pipes) it has, and prints out the properties of each pipe. Because opening an interface causes its pipes to be instantiated, you can get access to any pipe by using its pipe index. The pipe index is the number of the pipe within the interface, ranging from one to the number of endpoints returned by `GetNumEndpoints`. You can communicate with the default control pipe (described in [USB Transfer Types](USB%20Device%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnbufvbeeskiifeucry)) from any interface by using pipe index 0, but it is usually better to use the device interface functions for the device itself (see the use of `IOUSBDeviceInterface` functions in [Listing 2-5](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnbvfvbeeskkivfeksi)).

The sample code employs conditional compilation using `#ifdef` and `#ifndef` to demonstrate both synchronous and asynchronous I/O. If you’ve chosen to test synchronous I/O, `FindInterfaces` writes the test message (defined in [Listing 2-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnbvfvbugsccjfeeisi)) to pipe index 2 on the device and reads its echo before returning. For asynchronous I/O, `FindInterfaces` first creates an event source and adds it to the run loop created by the `main` function (shown in [Listing 2-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnbvfvbeeskgizausqi)). It then sets up an asynchronous write and read that will cause a notification to be sent upon completion. The completion functions `WriteCompletion` and `ReadCompletion` are shown together in [Listing 2-9](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnbvfvbeeskjijfeura).

__Listing 2-8__  Finding interfaces on the bulk test device

```swift
IOReturn FindInterfaces(IOUSBDeviceInterface **device)
{
    IOReturn                    kr;
    IOUSBFindInterfaceRequest   request;
    io_iterator_t               iterator;
    io_service_t                usbInterface;
    IOCFPlugInInterface         **plugInInterface = NULL;
    IOUSBInterfaceInterface     **interface = NULL;
    HRESULT                     result;
    SInt32                      score;
    UInt8                       interfaceClass;
    UInt8                       interfaceSubClass;
    UInt8                       interfaceNumEndpoints;
    int                         pipeRef;

#ifndef USE_ASYNC_IO
    UInt32                      numBytesRead;
    UInt32                      i;
#else
    CFRunLoopSourceRef          runLoopSource;
#endif

    //Placing the constant kIOUSBFindInterfaceDontCare into the following
    //fields of the IOUSBFindInterfaceRequest structure will allow you
    //to find all the interfaces
    request.bInterfaceClass = kIOUSBFindInterfaceDontCare;
    request.bInterfaceSubClass = kIOUSBFindInterfaceDontCare;
    request.bInterfaceProtocol = kIOUSBFindInterfaceDontCare;
    request.bAlternateSetting = kIOUSBFindInterfaceDontCare;

    //Get an iterator for the interfaces on the device
    kr = (*device)->CreateInterfaceIterator(device,
                                        &request, &iterator);
    while (usbInterface = IOIteratorNext(iterator))
    {
        //Create an intermediate plug-in
        kr = IOCreatePlugInInterfaceForService(usbInterface,
                            kIOUSBInterfaceUserClientTypeID,
                            kIOCFPlugInInterfaceID,
                            &plugInInterface, &score);
        //Release the usbInterface object after getting the plug-in
        kr = IOObjectRelease(usbInterface);
        if ((kr != kIOReturnSuccess) || !plugInInterface)
        {
            printf("Unable to create a plug-in (%08x)\n", kr);
            break;
        }

        //Now create the device interface for the interface
        result = (*plugInInterface)->QueryInterface(plugInInterface,
                    CFUUIDGetUUIDBytes(kIOUSBInterfaceInterfaceID),
                    (LPVOID *) &interface);
        //No longer need the intermediate plug-in
        (*plugInInterface)->Release(plugInInterface);

        if (result || !interface)
        {
            printf("Couldn’t create a device interface for the interface
                    (%08x)\n", (int) result);
            break;
        }

        //Get interface class and subclass
        kr = (*interface)->GetInterfaceClass(interface,
                                                    &interfaceClass);
        kr = (*interface)->GetInterfaceSubClass(interface,
                                                &interfaceSubClass);

        printf("Interface class %d, subclass %d\n", interfaceClass,
                                                    interfaceSubClass);

        //Now open the interface. This will cause the pipes associated with
        //the endpoints in the interface descriptor to be instantiated
        kr = (*interface)->USBInterfaceOpen(interface);
        if (kr != kIOReturnSuccess)
        {
            printf("Unable to open interface (%08x)\n", kr);
            (void) (*interface)->Release(interface);
            break;
        }

        //Get the number of endpoints associated with this interface
        kr = (*interface)->GetNumEndpoints(interface,
                                        &interfaceNumEndpoints);
        if (kr != kIOReturnSuccess)
        {
            printf("Unable to get number of endpoints (%08x)\n", kr);
            (void) (*interface)->USBInterfaceClose(interface);
            (void) (*interface)->Release(interface);
            break;
        }

        printf("Interface has %d endpoints\n", interfaceNumEndpoints);
        //Access each pipe in turn, starting with the pipe at index 1
        //The pipe at index 0 is the default control pipe and should be
        //accessed using (*usbDevice)->DeviceRequest() instead
        for (pipeRef = 1; pipeRef <= interfaceNumEndpoints; pipeRef++)
        {
            IOReturn        kr2;
            UInt8           direction;
            UInt8           number;
            UInt8           transferType;
            UInt16          maxPacketSize;
            UInt8           interval;
            char            *message;

            kr2 = (*interface)->GetPipeProperties(interface,
                                        pipeRef, &direction,
                                        &number, &transferType,
                                        &maxPacketSize, &interval);
            if (kr2 != kIOReturnSuccess)
                printf("Unable to get properties of pipe %d (%08x)\n",
                                        pipeRef, kr2);
            else
            {
                printf("PipeRef %d: ", pipeRef);
                switch (direction)
                {
                    case kUSBOut:
                        message = "out";
                        break;
                    case kUSBIn:
                        message = "in";
                        break;
                    case kUSBNone:
                        message = "none";
                        break;
                    case kUSBAnyDirn:
                        message = "any";
                        break;
                    default:
                        message = "???";
                }
                printf("direction %s, ", message);

                switch (transferType)
                {
                    case kUSBControl:
                        message = "control";
                        break;
                    case kUSBIsoc:
                        message = "isoc";
                        break;
                    case kUSBBulk:
                        message = "bulk";
                        break;
                    case kUSBInterrupt:
                        message = "interrupt";
                        break;
                    case kUSBAnyType:
                        message = "any";
                        break;
                    default:
                        message = "???";
                }
                printf("transfer type %s, maxPacketSize %d\n", message,
                                                    maxPacketSize);
            }
        }

#ifndef USE_ASYNC_IO    //Demonstrate synchronous I/O
        kr = (*interface)->WritePipe(interface, 2, kTestMessage,
                                            strlen(kTestMessage));
        if (kr != kIOReturnSuccess)
        {
            printf("Unable to perform bulk write (%08x)\n", kr);
            (void) (*interface)->USBInterfaceClose(interface);
            (void) (*interface)->Release(interface);
            break;
        }

        printf("Wrote \"%s\" (%ld bytes) to bulk endpoint\n", kTestMessage,
                                        (UInt32) strlen(kTestMessage));

        numBytesRead = sizeof(gBuffer) - 1; //leave one byte at the end
                                             //for NULL termination
        kr = (*interface)->ReadPipe(interface, 9, gBuffer,
                                            &numBytesRead);
        if (kr != kIOReturnSuccess)
        {
            printf("Unable to perform bulk read (%08x)\n", kr);
            (void) (*interface)->USBInterfaceClose(interface);
            (void) (*interface)->Release(interface);
            break;
        }

        //Because the downloaded firmware echoes the one’s complement of the
        //message, now complement the buffer contents to get the original data
        for (i = 0; i < numBytesRead; i++)
            gBuffer[i] = ~gBuffer[i];

        printf("Read \"%s\" (%ld bytes) from bulk endpoint\n", gBuffer,
                    numBytesRead);

#else   //Demonstrate asynchronous I/O
        //As with service matching notifications, to receive asynchronous
        //I/O completion notifications, you must create an event source and
        //add it to the run loop
        kr = (*interface)->CreateInterfaceAsyncEventSource(
                                    interface, &runLoopSource);
        if (kr != kIOReturnSuccess)
        {
            printf("Unable to create asynchronous event source
                                    (%08x)\n", kr);
            (void) (*interface)->USBInterfaceClose(interface);
            (void) (*interface)->Release(interface);
            break;
        }
        CFRunLoopAddSource(CFRunLoopGetCurrent(), runLoopSource,
                            kCFRunLoopDefaultMode);
        printf("Asynchronous event source added to run loop\n");
        bzero(gBuffer, sizeof(gBuffer));
        strcpy(gBuffer, kTestMessage);
        kr = (*interface)->WritePipeAsync(interface, 2, gBuffer,
                                    strlen(gBuffer),
                                    WriteCompletion, (void *) interface);
        if (kr != kIOReturnSuccess)
        {
            printf("Unable to perform asynchronous bulk write (%08x)\n",
                                                    kr);
            (void) (*interface)->USBInterfaceClose(interface);
            (void) (*interface)->Release(interface);
            break;
        }
#endif
        //For this test, just use first interface, so exit loop
        break;
    }
    return kr;
}
```

When an asynchronous write action is complete, the `WriteCompletion` function is called by the notification. `WriteCompletion` then calls the interface function `ReadPipeAsync` to perform an asynchronous read from the pipe. When the read is complete, control passes to `ReadCompletion` which simply prints status messages and adds a `NULL` termination to the global buffer containing the test message read from the device. The `WriteCompletion` and `ReadCompletion` functions are shown together in [Listing 2-9](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnbvfvbeeskjijfeura).

__Listing 2-9__  Two asynchronous I/O completion functions

```swift
void WriteCompletion(void *refCon, IOReturn result, void *arg0)
{
    IOUSBInterfaceInterface **interface = (IOUSBInterfaceInterface **) refCon;
    UInt32                  numBytesWritten = (UInt32) arg0;
    UInt32                  numBytesRead;

    printf("Asynchronous write complete\n");
    if (result != kIOReturnSuccess)
    {
        printf("error from asynchronous bulk write (%08x)\n", result);
        (void) (*interface)->USBInterfaceClose(interface);
        (void) (*interface)->Release(interface);
        return;
    }
    printf("Wrote \"%s\" (%ld bytes) to bulk endpoint\n", kTestMessage,
                                        numBytesWritten);

    numBytesRead = sizeof(gBuffer) - 1; //leave one byte at the end for
                                            //NULL termination
    result = (*interface)->ReadPipeAsync(interface, 9, gBuffer,
                                    numBytesRead, ReadCompletion, refCon);
    if (result != kIOReturnSuccess)
    {
        printf("Unable to perform asynchronous bulk read (%08x)\n", result);
        (void) (*interface)->USBInterfaceClose(interface);
        (void) (*interface)->Release(interface);
        return;
    }
}


void ReadCompletion(void *refCon, IOReturn result, void *arg0)
{
    IOUSBInterfaceInterface **interface = (IOUSBInterfaceInterface **) refCon;
    UInt32      numBytesRead = (UInt32) arg0;
    UInt32      i;

    printf("Asynchronous bulk read complete\n");
    if (result != kIOReturnSuccess) {
        printf("error from async bulk read (%08x)\n", result);
        (void) (*interface)->USBInterfaceClose(interface);
        (void) (*interface)->Release(interface);
        return;
    }
    //Check the complement of the buffer’s contents for original data
    for (i = 0; i < numBytesRead; i++)
        gBuffer[i] = ~gBuffer[i];

    printf("Read \"%s\" (%ld bytes) from bulk endpoint\n", gBuffer,
                                                    numBytesRead);
}
```

[Next](Document%20Revision%20History.md)[Previous](USB%20Device%20Overview.md)

