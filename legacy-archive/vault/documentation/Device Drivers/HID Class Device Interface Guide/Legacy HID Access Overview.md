---
title: HID Class Device Interface Guide
apple_id: TP40000970
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: IOKit
published: '2009-10-19'
source_url: https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/HID/basics/basics.html
archived_at: '2026-07-15T07:31:12.617581Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [HID Class Device Interface Guide](Introduction%20to%20Working%20With%20HID%20Class%20Device%20Interfaces.md)


[Next](Working%20With%20Legacy%20HID%20Class%20Device%20Interfaces.md)[Previous](Accessing%20a%20HID%20Device.md)

# Legacy HID Access Overview

This chapter provides step-by-step instructions, including listings of sample code, for accessing a HID class device on older versions of OS X. If you are developing new code for OS X v10.5 or later, you should use the APIs described in [Accessing a HID Device](Accessing%20a%20HID%20Device.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnzqfvbuqmrrgqwvgvzs).

The sample code shows how to find all HID class devices, how to narrow the search to devices of a specific type, and how to open and communicate with the device.

To search the I/O Registry for a currently available HID class device, create a device interface for the device, and communicate with it, you perform the steps described in the following sections:

1. [HID Access Overview](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnzqfvbuqmrrgewugskijbfecq2e)
2. [Setting Up Your Programming Environment](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnzqfvbuqmrrgewugsceirfekqkg)
3. [Accessing the I/O Kit Master Port](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnzqfvbuqmrrgewugscejbcuoqkk)
4. [Finding a HID Class Device](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnzqfvbuqmrrgewugscei5bukrcd)

The following list of steps briefly describes how to find a HID class device, create a device interface for it, connect to it, and communicate with it. The remainder of this chapter gives a detailed example of this process, including sample code.

1. Find the object that represents the device in the I/O Registry. For an overview of this process, see the discussion of device matching in the chapter[Device Access and the I/O Kit](https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/AccessingHardware/AH_Device_Access_IOKit/AH_Device_Access_IOKit.html#//apple_ref/doc/uid/TP30000378) of _Accessing Hardware From Applications_.
2. Create a device interface for the device. For a HID class device, you create a device interface of type `IOHIDDeviceInterface`. This device interface, defined in `IOHIDLib.h`, provides all the functions you need to access and communicate with your device.
3. Open a connection to the device by calling the `open` function of the device interface.
4. Communicate with the device using the functions provided by the HID Manager. For example, to get an element’s most recent value, use the `getElementValue` function.

   Functions for queue creation and manipulation are also provided by the HID Manager. For example, to read the next event from a queue, use the `getNextEvent` function; to request notification when a queue is no longer empty, use the function `setEventCallout`.
5. When you are finished with the device, call the `close` function of the device interface.
6. Release the device interface.

The sample code in this document is from a Xcode project that builds a command-line tool. This section focuses on the use of Xcode to develop a test function for the device interface functions you’ll be using. You can find more detailed documentation for Xcode at [http://developer.apple.com/documentation/DeveloperTools/index.html](https://developer.apple.com/documentation/DeveloperTools/index.html).

To set up Xcode to build the device interface, do the following:

1. Choose “CoreFoundation Tool” (in the Command Line Utility) when creating your project or add `CoreFoundation.framework` to your External Frameworks and Libraries of an existing project.
2. Add `IOKit.framework` and `System.framework` to the External Frameworks and Libraries section of your project. (Click and drag from Finder.)
3. It is recommended that you initially build your project with debugging turned on. To do this in Xcode, open the target list by clicking on the disclosure triangle. Double-click on the only target listed. In the inspector that appears, click on the build tab, then check the checkbox next to ‘Generate Debug Symbols’.

[Listing 3-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnzqfvbuqmrrgewugq2ijbeecskk) shows the header files you’ll need to include for the sample code in this document. Some of these headers include others; a shorter list may be possible. Except for `CoreFoundation.h`, these headers are generally part of `IOKit.framework` or `System.framework`, both of which are located in `/System/Library/Frameworks`.

__Listing 3-1__  Header files to include for the sample code in this document

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <ctype.h>
#include <sys/errno.h>
#include <sysexits.h>
#include <mach/mach.h>
#include <mach/mach_error.h>
#include <IOKit/IOKitLib.h>
#include <IOKit/IOCFPlugIn.h>
#include <IOKit/hid/IOHIDLib.h>
#include <IOKit/hid/IOHIDKeys.h>
#include <CoreFoundation/CoreFoundation.h>
```


The sample code for working with HID class device interfaces begins with the `MyStartHIDDeviceInterfaceTest` function, shown in [Listing 3-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnzqfvbuqmrrgewugscei5aukssd). This function establishes a connection to the I/O Kit and then calls functions to search for HID class devices and perform tests on each HID class device found. It accomplishes most of its work by calling the following functions:

- `MyFindHIDDevices`, shown in [Listing 3-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnzqfvbuqmrrgewueqkcinducscj), sets up a matching dictionary and then searches for matching HID class devices
- `MyTestHIDDevices`, available in the downloadable source package, iterates over the set of matching devices and calls many of the functions in this sample to print property information and create and test a device interface for each device.

__Listing 3-2__  A function that finds HID class devices in the I/O Registry and performs a test on each device

```
static void MyStartHIDDeviceInterfaceTest(void)
{
    io_iterator_t hidObjectIterator = NULL;
    IOReturn ioReturnValue = kIOReturnSuccess;

    MyFindHIDDevices(kIOMasterPortDefault, &hidObjectIterator);

    if (hidObjectIterator != NULL)
    {
        MyTestHIDDevices(hidObjectIterator);

        //Release iterator. Don't need to release iterator objects.
        IOObjectRelease(hidObjectIterator);
    }
}
```

The `MyStartHIDDeviceInterfaceTest` function releases both the master port it obtained and the iterator returned by the `MyFindHIDDevices` function, but it doesn’t release the iterator’s objects. They are released in the `MyTestHIDDevices` function after it uses the objects.

Before your application can create a device interface to access a device, it must first find the device in the I/O Registry. To do this, you create a matching dictionary specifying the type of device you want to find. Then you get an iterator for the list of devices that match your criteria so you can examine each one.

The following functions demonstrate this process by creating a matching dictionary and searching the I/O Registry for matching devices. If the search is successful, the function `MyFindHIDDevices` (shown in [Listing 3-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnzqfvbuqmrrgewueqkcinducscj)) returns an iterator for the list of matched devices.

The `MyFindHIDDevices` function is the starting point for finding a specific type of device in the I/O Registry. First, it sets up a matching dictionary by passing `kIOHIDDeviceKey` (defined in `IOHIDLib.h`) to the I/O Kit function `IOServiceMatching`. This defines a broad search for all objects in the I/O Registry that represent HID class devices. Then it calls the I/O Kit function `IOServiceGetMatchingServices`, which performs the search and, if successful, returns an iterator for the set of matching devices.

The parameters to `MyFindHIDDevices` are a Mach port and a pointer to an object iterator. The Mach port is obtained in a previous call to the `IOMasterPort` function—see [Listing 3-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnzqfvbuqmrrgewugscei5aukssd). The `MyFindHIDDevices` function uses the pointer to an object iterator to return an iterator that provides access to matching driver objects from the I/O Registry.

__Listing 3-3__  A function that searches for HID devices that match the specified criteria

```
static void MyFindHIDDevices(mach_port_t masterPort,
                io_iterator_t *hidObjectIterator)
{
    CFMutableDictionaryRef hidMatchDictionary = NULL;
    IOReturn ioReturnValue = kIOReturnSuccess;
    Boolean noMatchingDevices = false;

    // Set up a matching dictionary to search the I/O Registry by class
    // name for all HID class devices
    hidMatchDictionary = IOServiceMatching(kIOHIDDeviceKey);

    // Now search I/O Registry for matching devices.
    ioReturnValue = IOServiceGetMatchingServices(masterPort,
                            hidMatchDictionary, hidObjectIterator);

    noMatchingDevices = ((ioReturnValue != kIOReturnSuccess)
                                | (*hidObjectIterator == NULL));

    //If search is unsuccessful, print message and hang.
    if (noMatchingDevices)
        print_errmsg_if_err(ioReturnValue, "No matching HID class devices found.");

    // IOServiceGetMatchingServices consumes a reference to the
    //   dictionary, so we don't need to release the dictionary ref.
    hidMatchDictionary = NULL;
}
```

The `MyFindHIDDevices` function doesn’t release the reference it obtains to a matching dictionary because when it calls the I/O Kit function `IOServiceGetMatchingServices`, that function consumes a reference to the dictionary.

[Next](Working%20With%20Legacy%20HID%20Class%20Device%20Interfaces.md)[Previous](Accessing%20a%20HID%20Device.md)

