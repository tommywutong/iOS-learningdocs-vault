---
title: Accessing Hardware From Applications
apple_id: TP30000376
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: IOKit
published: '2007-02-08'
source_url: https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/AccessingHardware/AH_IOKitLib_API/AH_IOKitLib_API.html
archived_at: '2026-07-15T07:31:09.095153Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Accessing Hardware From Applications](Introduction%20to%20Accessing%20Hardware%20From%20Applications.md)


[Next](Handling%20Errors.md)[Previous](Finding%20and%20Accessing%20Devices.md)

# The IOKitLib API

When you access a device from user space, whether you use a device interface or the POSIX API, you use a combination of I/O Kit functions and specific device-family functions to work with the I/O Kit objects that represent the device. The IOKitLib, located in the I/O Kit framework, contains the generic I/O Kit functions you use to implement user-space task access to in-kernel device objects.

This chapter surveys the IOKitLib functions, describing how to use them to get access to and manipulate in-kernel objects and providing insight into how the IOKitLib implements these functions.

Some of the functions in the IOKitLib are intended for developers of custom device interfaces rather than for developers of applications that use existing device interfaces. Although this chapter covers these functions at a high level, you should read [Making Hardware Accessible to Applications](https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/WritingDeviceDriver/MakingHWAccessible/MakingHWAccessible.html#//apple_ref/doc/uid/TP30000698) in _[IOKit Device Driver Design Guidelines](../IOKit%20Device%20Driver%20Design%20Guidelines/Introduction%20to%20I-O%20Kit%20Device%20Driver%20Design%20Guidelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmoju)_ if you need to develop your own device interface–user client solution.

The IOKitLib functions can be divided into several categories, based on the type of service they provide. This chapter mirrors these groupings and is divided into the following sections, each of which covers a functional category:

- [Object Reference-Counting and Introspection](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgobqfvbecqsdinceqrq) introduces the types of objects you use to communicate with in-kernel entities and describes how to get information about them and keep track of their reference counts.
- [Device Discovery and Notification](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgobqfvbecqskjfbesqi) describes the functions you use to create matching dictionaries, look up and access matching devices in the I/O Registry, and receive notifications about a device’s state change.
- [I/O Registry Access](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgobqfvbecqshizeeuri) describes other IOKitLib functions you can use to get access to objects in the I/O Registry.
- [Device-Interface Development](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgobqfvbecqsfizdesra) gives a brief overview of the IOKitLib functions you use when no I/O Kit device-family or third-party device interface exists and you need to develop your own device interface.

Functions in the IOKitLib communicate with in-kernel objects using the Mach port transport mechanism to cross the user-kernel boundary. The file `IOTypes.h`, located in the I/O Kit framework, defines the objects you use with IOKitLib functions to communicate with such in-kernel entities as I/O Registry entries (objects of class IORegistryEntry) or iterators (objects of class IOIterator). Notice in [Listing 4-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgobqfvbecqsjizbucri), however, that `IOTypes.h` seems to define all these objects in the same way, specifically, as `mach_port_t` objects (`mach_port_t` is defined in `mach/port.h` in the Kernel framework).

__Listing 4-1__  Object definitions in IOTypes.h

```
typedef mach_port_t io_object_t;

typedef io_object_t io_connect_t;
typedef io_object_t io_iterator_t;
typedef io_object_t io_registry_entry_t;
typedef io_object_t io_service_t;
typedef io_object_t io_enumerator_t;
```

To understand why this is so, recall that a Mach port is the communication transport mechanism an application uses to communicate with the I/O Kit. As far as the kernel is concerned, every time your application communicates with any in-kernel object using one of the object types defined in `IOTypes.h`, it’s using the same generic mechanism (namely, a Mach port) to cross the user-kernel boundary.

From the application’s point of view, however, the transport mechanism is unimportant and what matters is the type of object on the other side of the port. The fact that an `io_iterator_t` object, for example, encapsulates the association of a Mach port with an in-kernel IOIterator object is not as important to the application as the fact that an `io_iterator_t` object refers to an in-kernel object that knows how to iterate over the I/O Registry.

The `io_object_t` objects in user space not only refer to the in-kernel objects, they also reflect the in-kernel C++ class hierarchy. Because IOService is a subclass of IORegistryEntry, for example, you can use an `io_service_t` object with any IOKitLib function that expects an `io_registry_entry_t` object, such as `IORegistryEntryGetPath`.

With few exceptions (such as getting the I/O Kit master port to initiate communication with the I/O Kit and reference-counting of the `io_object_t` objects themselves) you should not concern yourself with the cross-boundary communication mechanism. Rather, you should focus on the specific in-kernel object you are working with, making sure you use each object type appropriately.

The IOKitLib contains three reference-counting functions:

- `IOObjectGetRetainCount`
- `IOObjectRetain`
- `IOObjectRelease`

Each of these functions operates on the retain count of the underlying kernel object (the object on the other side of the Mach port) and not on the `io_object_t` object itself. In other words, if you want to retain, release, or get the retain count of the in-kernel IORegistryEntry object an `io_registry_entry_t` object represents, you use one of the IOKitLib reference-counting functions. For example, [Listing 4-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgobqfvbecqsjizbuqrq) shows a code fragment that releases the in-kernel IOIterator object underlying an `io_iterator_t` object after it’s been used to find a serial port modem.

__Listing 4-2__  Releasing the underlying kernel object of an `io_iterator_t` object

```
io_iterator_t serialPortIterator = NULL;
char deviceFilePath[ MAXPATHLEN ];

kernResult = MyFindSerialPortModems(&serialPortIterator, &masterPort);
if (kernResult == kIOReturnSuccess) {
    kernResult = MyGetPathOfFirstModem (serialPortIterator, deviceFilePath,
            sizeof(deviceFilePath));

    //Release the iterator since we want only the first modem.
    IOObjectRelease(serialPortIterator);
    //If MyGetPathOfFirstModem found a modem, communicate with it.
...
}
```

As a matter of good programming practice, you should use `IOObjectRelease` to release all `io_object_t` objects you create in your code when they’re no longer needed.

If you suspect that you are leaking `io_object_t` objects, however, `IOObjectGetRetainCount` won’t help you because this function informs you of the underlying kernel object’s retain count (which is often much higher). Instead, because the retain count of an `io_object_t` object is essentially the retain count of the send rights on the Mach port, you use a Mach function to get this information. [Listing 4-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgobqfvbecqscjbdegra) shows how to use the Mach function`mach_port_get_refs` (defined in `mach/mach_port.h` in the Kernel framework) to get the retain count of an `io_object_t` object.

__Listing 4-3__  Getting the retain count of an `io_object_t` object

```c
#include <mach/mach_port.h>

kern_return_t kr;
unsigned int count;
io_object_t theObject;

kr = mach_port_get_refs ( mach_task_self(), theObject, MACH_PORT_RIGHT_SEND,
            &count );
printf ("Retain count for object ID %#X is %d\n", theObject, count);
```


The IOKitLib provides three object-introspection functions that operate on the in-kernel object the passed-in `io_object_t` object represents (not the `io_object_t` object itself):

- `IOObjectConformsTo`
- `IOObjectGetClass`
- `IOObjectIsEqualTo`

The first function, `IOObjectConformsTo`, simply performs the in-kernel object’s `metaCast` method and returns the Boolean result. The `IOObjectGetClass` function calls the in-kernel object’s `getMetaClass` method and then calls that class’s `getClassName` method to return the class name as a C string. IOKitLib implements the `IOObjectIsEqualTo` function as a shallow pointer comparison of the two passed-in objects, returning the result as a Boolean value.

Even if you use few other IOKitLib functions in your device-access application, you will certainly use the device-discovery functions. If you’re working with hot-pluggable devices, such as USB or FireWire devices, you may also use the notification functions.

The following sections cover the IOKitLib device-discovery and notification functions, describing how the IOKitLib implements:

- Matching dictionary–creation
- Device look-up
- Notification set-up
- Device iteration

When you use IOKitLib functions to create a matching dictionary, you receive a reference to a Core Foundation dictionary object. The IOKitLib uses Core Foundation classes, such as CFMutableDictionary and CFString, because they closely corrrespond to the in-kernel collection and container classes, such as OSDictionary and OSString (defined in `libkern/c++` in the Kernel framework).

The I/O Kit automatically translates a CFDictionary object into its in-kernel counterpart when it crosses the user-kernel boundary, allowing you to create an object in user-space that is later used in the kernel. For more information on using Core Foundation objects to represent in-kernel objects, see [Viewing Properties of I/O Registry Objects](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgobqfvbecqsjirfeisi).

The IOKitLib defines the following functions to create matching dictionaries:

- `IOServiceMatching`
- `IOServiceNameMatching`
- `IOBSDNameMatching`

These functions create a mutable Core Foundation dictionary object containing the appropriate key and your passed-in value. [Table 4-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgobqfvbuirkcindecri) shows the keys each of the dictionary-creation functions use, along with the I/O Kit framework files in which the keys are defined.

__Table 4-1__  Dictionary-creation functions and the keys they use

| Function name | Key name | Key-definition file |
| `IOServiceMatching` | `kIOProviderClassKey` | `IOKitKeys.h` |
| `IOServiceNameMatching` | `kIONameMatchKey` | `IOKitKeys.h` |
| `IOBSDNameMatching` | `kIOBSDNameKey` | `IOBSD.h` |

If, for example, you call `IOServiceNameMatching` with the argument _i2c-modem_, the resulting dictionary looks like this:

```
{
    IONameMatch = i2c-modem;
}
```

All dictionary-creation functions return a reference to a CFMutableDictionary object. Usually, you pass the dictionary to one of the look-up functions (discussed next in [Looking Up Devices](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgobqfvbecqseijfegqi)), each of which consumes one reference to it. If you use the dictionary in some other way, you should adjust its retain count accordingly, using `CFRetain` or `CFRelease` (defined in the Core Foundation framework).

IOKitLib provides three look-up functions that look up registered objects in the I/O Registry that match a passed-in matching dictionary:

- `IOServiceGetMatchingServices`
- `IOServiceGetMatchingService`
- `IOServiceAddMatchingNotification`

IOKitLib implements its most general look-up function, `IOServiceGetMatchingServices`, by transforming your matching dictionary into an OSDictionary object and invoking the IOService method `getMatchingServices`. This method returns an IOIterator object that contains a list of matching IOService objects. `IOServiceGetMatchingServices` then releases the matching dictionary you passed in and returns to you an `io_iterator_t` object representing the in-kernel IOIterator object.

The `IOServiceGetMatchingService` function is simply a special case of `IOServiceGetMatchingServices`: It returns the first matching object in the list instead of an iterator that provides access to the entire list.

If you receive an `io_iterator_t` object from `IOServiceGetMatchingServices`, you should release it with `IOObjectRelease` when you’re finished with it; similarly, you should use `IOObjectRelease` to release the `io_object_t` object you receive from `IOServiceGetMatchingService`.

The `IOServiceAddMatchingNotification` function not only looks up matching objects in the I/O Registry, it also installs a request for notification of matching objects that meet your passed-in criterion. The IOKitLib implements this function by invoking the IOService `addNotification` method, which creates a persistent notification handler that can be notified of IOService events.

To use `IOServiceAddMatchingNotification`, however, you must first use some other functions in the IOKitLib to set up the notification mechanism. For more information on these functions, see the next section, [Setting Up and Receiving Notifications](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgobqfvbecqsfivdeisq). For an outline of the steps your application takes to set up a notification mechanism using a run loop, see [Getting Notifications of Device Arrival and Departure](Finding%20and%20Accessing%20Devices.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgnzzfvbecqsfifbugsq).

The IOKitLib provides several functions you use to set up and manage notification objects:

- `IONotificationPortCreate`
- `IONotificationPortGetRunLoopSource`
- `IONotificationPortGetMachPort`
- `IODispatchCalloutFromMessage`
- `IONotificationPortDestroy`

Whether you choose to receive notifications on a run loop or a Mach port (using a run loop is the recommended approach), you must first create an object that can listen for I/O Kit notifications. To do this, you use the `IONotificationPortCreate` function, which returns an object of type IONotificationPortRef. IOKitLib implements this function by allocating a receive right on the current Mach port, giving it the name of the IONotificationPort object you pass in.

To receive notifications on a run loop, you first use the `IONotificationPortGetRunLoopSource` function to get a run-loop source you can install on your application’s current run loop. In OS X, a run loop registers input sources, such as Mach ports, and enables the delivery of events, such as IOService object status changes, through those sources. The run-loop source object you receive from `IONotificationPortGetRunLoopSource` function is of type CFRunLoopSourceRef. (For more information about how to install the run-loop source on your application’s run loop, see [Getting Notifications of Device Arrival and Departure](Finding%20and%20Accessing%20Devices.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgnzzfvbecqsfifbugsq).)

The IOKitLib provides two functions that allow you use a Mach port you create on which to listen for notifications, rather than a run loop. Although this method is available to you, it’s recommended that you use the easier-to-implement and more automatic run-loop solution instead. The `IONotificationPortGetMachPort` function returns a Mach port on which the IONotificationPortRef object can listen for notifications. When the notification object receives a message, you pass the message to the `IODispatchCalloutFromMessage` function to generate the callback function associated with the notification.

The `IONotificationPortDestroy` function cleans up and destroys all rights named by the passed-in port name (the IONotificationPortRef object you received from `IONotificationPortCreate`). You should call this function when you no longer want to receive notifications.

To access the matching objects a look-up function returns, you use the `IOIteratorNext` function. IOKitLib contains three functions that operate on `io_iterator_t` objects:

- `IOIteratorNext`
- `IOIteratorIsValid`
- `IOIteratorReset`

As a subclass of OSIterator, the in-kernel IOIterator object defines the methods `getNextObject`, `isValid`, and `reset`. IOKitLib invokes these methods in its implementation of `IOIteratorNext`, `IOIteratorIsValid`, and `IOIteratorReset`, respectively.

`IOIteratorNext` simply returns a reference to the current object in the list (an `io_object_t` object) and advances the iterator to the next object.

`IOIteratorIsValid` returns a Boolean value indicating whether the iterator is still valid. Sometimes, if the I/O Registry changes while you’re using an iterator, the iterator becomes invalid. When this is the case, `IOIteratorIsValid` returns zero and you can reset the invalid iterator to the beginning of the list, using `IOIteratorReset`. Of course, you can use `IOIteratorReset` to start over at the beginning of the list for any reason, not only because the iterator is invalid.

The IOKitLib provides a range of functions that find and provide information about objects in the I/O Registry. Unlike the device-discovery functions, which focus on finding and accessing registered device objects that match your matching dictionary, the I/O Registry–access functions allow you to view objects more broadly as entries in the I/O Registry, providing ways to freely navigate the I/O Registry and get information about any object in it. If you’re unfamiliar with the structure of the I/O Registry, you can read more about it in [The I/O Registry](https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/IOKitFundamentals/TheRegistry/TheRegistry.html#//apple_ref/doc/uid/TP0000014) in _[IOKit Fundamentals](../IOKit%20Fundamentals/Introduction%20to%20I-O%20Kit%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridambqgaydcmi)_. The following paragraphs provide a summary.

The I/O Registry is a dynamic database that captures the connections of all driver and nub objects currently active in a running OS X system. You can think of the I/O Registry as a tree-like structure rooted in the Platform Expert, the driver of the main logic board that knows the type of platform your OS X system is running on.

The I/O Registry uses the concept of a plane to describe the different provider-client relationships between objects. The Service plane displays the instantiation hierarchy of the I/O Registry: Every object in the I/O Registry is a client of the services provided by its parent, so every object’s connection to its ancestor in the I/O Registry tree is visible on the Service plane. Other planes express the provider-client relationships between objects that participate in a specific hierarchy, such as the flow of power from power provider to power client.

Many of the I/O Registry–access functions require you to pass in an argument designating a specific plane. In most cases, you will probably specify the all-inclusive Service plane, but there may be times when you want to narrow the focus a bit. The file `IOKitKeys.h` (in the I/O Kit framework) contains the plane name definitions you use in your code.

The IOKitLib provides I/O Registry–access functions that:

- Traverse the I/O Registry in some way
- Provide information about a particular object in the I/O Registry
- Allow you to view an I/O Registry object’s properties
- Allow you to set properties in an I/O Registy object’s property table

IOKitLib implements most of these functions by invoking similarly named IORegistryEntry methods (see `IORegistryEntry.h` in the `IOKit` directory of the Kernel framework for more). The following sections describe how you use the I/O Registry functions.

When you use the `IOServiceGetMatchingServices` look-up function, you get an iterator you can use to access each object in a list of matching I/O Registry objects. But what if you want to search the I/O Registry using some criteria other than a matching dictionary? Say, for example, you want to find all the children (clients) of a particular object, regardless of whether they are currently registered in the I/O Registry. The following functions give you access to the parents and children of an `io_registry_entry_t` object:

- `IORegistryEntryGetChildEntry`
- `IORegistryEntryGetChildIterator`
- `IORegistryEntryGetParentEntry`
- `IORegistryEntryGetParentIterator`

Not surprisingly, the functions with the word “iterator” in their names supply you with an `io_iterator_t` object you can pass to `IOIteratorNext` to access each `io_registry_entry_t` object in the list. `IORegistryEntryGetParentIterator`, for example, looks in the specified plane to find all ancestors of the passed-in object and returns an iterator you can use to access them. As you do with the `IOServiceGetMatchingService` and `IOServiceAddMatchingNotification` functions, be sure to release the returned `io_iterator_t` object when you’re finished with it (recall that releasing the iterator you receive from `IOServiceAddMatchingNotification` also disables that notification). The other two functions, `IORegistryEntryGetChildEntry` and `IORegistryEntryGetParentEntry`, return the first child or ancestor of the passed-in object in the specified plane.

For even broader searches, you can use the following functions to search the entire I/O Registry, from any point and to any depth:

- `IORegistryCreateIterator`
- `IORegistryEntryCreateIterator`
- `IORegistryIteratorEnterEntry`
- `IORegistryIteratorExitEntry`
- `IORegistryGetRootEntry`

The `IORegistryCreateIterator` function returns an `io_iterator_t` object that begins at the root of the I/O Registry and iterates over all its children in the specified plane. Similarly, `IORegistryEntryCreateIterator` returns an `io_iterator_t` object that begins at the passed-in `io_registry_entry_t` object and iterates over either all its ancestors or all its children in the passed-in plane.

Both these functions allow you to specify an option that tells the iterator to automatically recurse into objects as they are returned, or only when you call `IORegistryIteratorEnterEntry` to recurse into the current object. The `IORegistryIteratorExitEntry` function undoes the effect of `IORegistryIteratorEnterEntry` by resetting the iterator to the current object, allowing the iterator to continue from where it left off. As its name implies, `IORegistryGetRootEntry` returns an `io_registry_entry_t` object representing the root of the I/O Registry.

The IOKitLib provides a handful of functions, listed below, that return information about a particular I/O Registry object, such as its name or path.

- `IORegistryEntryGetName`
- `IORegistryEntryGetNameInPlane`
- `IORegistryEntryGetPath`
- `IORegistryEntryGetLocationInPlane`
- `IORegistryEntryInPlane`

IOKitLib implements these functions by invoking IORegistryEntry methods such as `getName` and `getLocation`. Each function returns a C string that contains the object’s name or location. For example, [Listing 4-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgobqfvbecqsgijdugsq) shows how to use some of these functions on the object representing an Apple USB keyboard.

__Listing 4-4__  Using the `IORegistryEntryGet` functions

```
io_service_t device;
io_name_t devName;
io_string_t pathName;

IORegistryEntryGetName(device, devName);
printf("Device's name = %s\n", devName);
IORegistryEntryGetPath(device, kIOServicePlane, pathName);
printf("Device's path in IOService plane = %s\n", pathName);
IORegistryEntryGetPath(device, kIOUSBPlane, pathName);
printf("Device's path in IOUSB plane = %s\n", pathName);
```

The code in [Listing 4-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgobqfvbecqsgijdugsq) displays information like the following:

```
Device's name = Apple Extended USB Keyboard
Device's path in IOService plane = IOService:/MacRISC2PE/pci@f2000000/
    AppleMacRiscPCI/usb@18/AppleUSBOHCI/Apple Extended USB Keyboard@1211000
Device's path in IOUSB plane = IOUSB:/IOUSBHubDevice@1200000/Hub in Apple
    Extended USB Keyboard@1210000/Apple Extended USB Keyboard@1211000
```

If you’re more interested in whether an object exists in a particular plane than in its path or name, you can use the `IORegistryEntryInPlane` function, which returns `TRUE` if the object has a parent in the plane and `FALSE` otherwise.

Each object in the I/O Registry has two dictionaries associated with it:

- The property table for the object—if the object is a driver, this is the matching dictionary that defines one of the driver’s personalities (if the object is a nub, the device family publishes device properties in the nub’s property table).
- The plane dictionary—this dictionary describes how the object is connected to other objects in the I/O Registry.

These dictionaries are instances of OSDictionary. The libkern C++ library defines container classes, which hold primitive values, such as numbers and strings, and collection classes, which hold groups of both container objects and other collection objects. To view the contents of these objects in an application, you must use IOKitLib functions to convert the in-kernel collection or container object (such as OSDictionary or OSString) to the equivalent Core Foundation object. Currently, only the following libkern classes are available as Core Foundation analogues:

- OSDictionary
- OSArray
- OSSet
- OSSymbol
- OSString
- OSData
- OSNumber
- OSBoolean

The following IOKitLib functions allow you to access an object’s properties as Core Foundation types:

- `IORegistryEntryCreateCFProperty`
- `IORegistryEntryCreateCFProperties`
- `IORegistryEntrySearchCFProperty`

The `IORegistryEntryCreateCFProperty` function creates a Core Foundation container representing the value associated with the passed-in property key. For example, you can get a CFTypeRef to a storage device’s device-file name by passing a handle to the device (an `io_object_t` object) and the key `kIOBSDNameKey` (defined in `IOBSD.h`) to `IORegistryEntryCreateCFProperty`:

```
CFTypeRef deviceFileName;
deviceFileName = IORegistryEntryCreateCFProperty(deviceHandle,
                CFSTR(kIOBSDNameKey), kCFAllocatorDefault, 0);
```

The `IORegistryEntryCreateCFProperties` function creates a Core Foundation dictionary object containing the passed-in object’s property table. After your application gets the CFDictionary representation of an object’s property table, it can call Core Foundation functions (such as `CFDictionaryGetValue` and `CFNumberGetValue`) to access the dictionary’s values.

The `IORegistryEntrySearchCFProperty` function searches for the passed-in property, beginning with a specified `io_registry_entry_t` object’s property table, and continuing with either its parents or its children in the specified plane. When it finds the property you passed in, it returns a Core Foundation container object representing the property.

When you’re finished with the Core Foundation container object you receive from these functions, you should call `CFRelease` on it.

Because the I/O Registry is a dynamic database that is constantly being updated, the properties a function such as `IORegistryEntryCreateCFProperties` returns represent a snapshot of the I/O Registry’s state at a single instant. For this reason, you should not assume that the properties you receive are static—if you call these functions multiple times in your application, you may get different results each time.

In addition to viewing an object’s properties in an application, you can also use IOKitLib functions to place new properties into an object’s property table.

Setting properties from user space is suitable for some types of device control, in particular, single downloads of data, such as the loading of firmware. This type of user space–kernel communication works because both the application and the in-kernel object have access to the device object’s property table in the I/O Registry. Of course, when you use IOKitLib functions to set properties in an object’s property table, it’s important to realize that you’re only manipulating the OSDictionary representation of an object’s information property list, not the property list itself.

Before you consider setting an object’s properties in your application, make sure your situation meets the following conditions:

- Your device family implements the `setProperties` method or you control the in-kernel driver, and in it, you implement the `setProperties` method.
- The driver does not have to allocate permanent resources to complete the transaction.
- The data sent either causes no change in the driver’s state, or causes a single, permanent change.
- If the application transfers data by copy, it sends only a limited amount, such as a page or less. (If the application sends data by reference, it can send an arbitrary amount of data.)

The IOKitLib provides four functions that allow you to set properties in an object’s I/O Registry property table:

- `IORegistryEntrySetCFProperty`
- `IORegistryEntrySetCFProperties`
- `IOConnectSetCFProperty`
- `IOConnectSetCFProperties`

The first two functions, `IORegistryEntrySetCFProperty` and `IORegistryEntrySetCFProperties`, are generic functions that set either a single property value or a collection of property values (typically, in a CFDictionary object) in the specified `io_registry_entry_t` object. The in-kernel object interprets the Core Foundation container or collection object as it chooses.

If you’re developing your own device interface–user client solution, you’re more likely to use the `IOConnectSetCFProperty` and `IOConnectSetCFProperties` functions to set properties. This is because you are working with the `io_connect_t` object that represents the connection you opened to the in-kernel driver object with `IOServiceOpen` and these functions provide more access control than `IORegistryEntrySetProperty` and `IORegistryEntrySetProperties`. For a brief overview of how to create a connection to a user client, see [Device-Interface Development](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgobqfvbecqsfizdesra).

The IOKitLib includes a handful of functions that give you information about the busy state of various IOService objects and allow you to wait until these objects are no longer busy:

- `IOServiceGetBusyState`
- `IOKitGetBusyState`
- `IOServiceWaitQuiet`
- `IOKitWaitQuiet`

Because activities such as registration, matching, and termination are asynchronous, an IOService object in the process of one of these activities is considered busy and its `busyState` value is increased by one. When any of these activities concludes, the IOService’s `busyState` value is decreased by one. Additionally, any time an IOService object’s `busyState` value changes, its provider’s `busyState` value changes to match, which means that an IOService object is considered to be busy when any of its clients is busy.

To get the busy state of an individual `io_service_t` object, you use the `IOServiceGetBusyState` function, which IOKitLib implements by invoking the object’s `getBusyState` method.

You can get the busy state of all IOService objects by calling the `IOKitGetBusyState` function. As the provider of all IOService objects in the I/O Registry, the root of the Service plane is busy when any of its clients (in other words, any IOService object) is busy. The `IOKitGetBusyState` function returns the busy state of the Service plane root, effectively informing you of the busy state of the I/O Registry as a whole.

You can wait until objects cease to be busy by calling either the `IOServiceWaitQuiet` or `IOKitWaitQuiet` functions. Both functions allow you to specify a maximum time to wait and block the calling process until either the time runs out or the object becomes nonbusy.

If you need to implement both an in-kernel user client and a device-interface library, you should read [Making Hardware Accessible](https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/WritingDeviceDriver/MakingHWAccessible/MakingHWAccessible.html#//apple_ref/doc/uid/TP30000698) in _[IOKit Device Driver Design Guidelines](../IOKit%20Device%20Driver%20Design%20Guidelines/Introduction%20to%20I-O%20Kit%20Device%20Driver%20Design%20Guidelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmoju)_ for in-depth information on how to do this. This section covers only the user-space side of this process, briefly describing the IOKitLib functions involved.

Although you may not directly use the IOKitLib functions this sections describes, knowing how they work will give you some insight into how device interfaces and user clients cooperate.

The IOKitLib provides several functions that allow you to create and manipulate connections to in-kernel objects, typically user clients. As with the other functions described in this section, you should use them only when your device family does not provide a device-interface solution and you’ve decided to implement both the in-kernel user client and the user-space device interface.

For an application to communicate with a device, the first thing it must do is create a connection between itself and the in-kernel object representing the device. To do this, it creates a user client object.

After it gets the `io_service_t` object representing the device driver (by calling `IOServiceGetMatchingServices`, for example), the application calls the IOKitLib `IOServiceOpen` function to create the connection. The `IOServiceOpen` function invokes the `io_service_t` object’s `newUserClient` method, which instantiates, initializes, and attaches the user client. As a result of calling `IOServiceOpen`, the application receives an `io_connect_t` object (representing the user-client object) that it can use with the IOKitLib `IOConnect` functions.

For example, in the _[SimpleUserClient](../../../samplecode/SimpleUserClient/SimpleUserClient.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydanbvga)_ example project, the application portion of the project creates a user client with code like that shown in [Listing 4-5](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgobqfvbecqsfivcemsq).

__Listing 4-5__  Creating a user client

```
//Code to get the I/O Kit master port, create a matching dictionary, and get
//an io_service_t object representing the in-kernel driver is not shown here.
io_service_t serviceObject;
io_connect_t dataPort;
kern_return_t kernResult;

kernResult = IOServiceOpen(serviceObject, mach_task_self(), 0, &dataPort);
```

An application destroys a connection to a user client with a call to the `IOServiceClose` function, which invokes the `clientClose` method in the user client. If, for some reason, the application terminates before it’s able to call `IOServiceClose`, the user client invokes the `clientDied` method. Typically, the user client responds to both methods by invoking `close` on its provider (usually the device nub).

If you’re developing your own user client and device-interface library, the IOKitLib functions you’re most likely to use are the four `IOConnectMethod` functions (which call the user client’s external methods) and, if your user client can map hardware registers into your application’s address space, `IOConnectMapMemory` and `IOConnectUnmapMemory`.

The `IOConnectMethod` functions use arrays of structures containing pointers to methods to invoke in a user-client object. The user client defines the list of methods it implements in an `IOExternalMethod` array. Typically, these methods include the user client’s `open` and `close` methods and methods that pass data between the in-kernel driver and the application. To use an `IOConnectMethod` function, an application passes in the `io_connect_t` object, the index into the `IOExternalMethod` array, and, if the application is passing or receiving data, arguments that describe the general data type (scalar or structure), number of scalar parameters, size of data structures, and direction (input or output).

To open the user client, the application calls any of the `IOConnectMethod` functions, passing in just the `io_connect_t` object representing the user client and the `IOExternalMethod` array index corresponding to the user client’s `open` method. Because the application is not passing or receiving any data at this point, the remaining two arguments passed to the `IOConnectMethod` function are zero. For example, the code below shows how the application in the SimpleUserClient project uses the `io_connect_t` object it received in [Listing 4-5](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgobqfvbecqsfivcemsq) to open its user client:

```
//kMyUserClientOpen is one of the enum constants the SimpleUserClient
//project uses as indexes into the IOExternalMethod array.
kernResult = IOConnectMethodScalarIScalarO(dataPort, kMyUserClientOpen,
                 0, 0);
```

To pass untyped data back and forth across the user-kernel boundary, an application uses one of the `IOConnectMethod` functions in [Table 4-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgobqfvbecqshi5demqq), depending on the type of data and the direction of data flow.

__Table 4-2__  `IOConnectMethod` functions

| Function | Description |
| `IOConnectMethodScalarIScalarO` | One or more scalar input parameters, one or more scalar output parameters |
| `IOConnectMethodScalarIStructureO` | One or more scalar input parameters, one structure output parameter |
| `IOConnectMethodScalarIStructureI` | One or more scalar input parameters, one structure input parameter |
| `IOConnectMethodStructureIStructureO` | One structure input parameter, one structure output parameter |

The `IOConnectMethod` functions are designed to accept variable argument lists, depending on the data type and direction you choose. Following the first two arguments—the `io_connect_t` object and the method array index—is some combination of arguments that identify:

- The number of scalar input or output values
- The size of the input or output structure
- Scalar input or output values
- A pointer to an input or output structure

The application in the SimpleUserClient, for example, uses the `IOConnectMethodScalarIStructureI` function as shown in [Listing 4-6](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgobqfvbecqshincucsi).

__Listing 4-6__  Requesting I/O with the `IOConnectMethodScalarIStructureI` function

```
//MySampleStruct is defined in the header file both the user client
//and the application include and consists of two integer variable
//declarations.
MySampleStruct sampleStruct = {586, 8756}; //Random numbers.
int sampleNumber = 15; //Random number.
IOByteCount structSize = sizeof(MySampleStruct);
kern_return_t kernResult;

kernResult = IOConnectMethodScalarIStructureI(dataPort, // from IOServiceOpen
                kMyScalarIStructImethod, // method index
                1, // number of scalar input values
                structSize, // size of input structure
                sampleNumber, // scalar input value
                &sampleStruct // pointer to input structure
                );
```


If your device driver has full PIO (Programmed Input/Output) memory management and your device does not require the use of interrupts, you can write a dedicated application that moves large amounts of data to and from the device, using the `IOConnectMapMemory` and `IOConnectUnmapMemory` functions. For example, a frame-buffer application can use these functions to handle the large amounts of on-board memory that needs to be accessible from user space. The `IOConnectMapMemory` function allows a user process to share memory with an in-kernel driver by mapping the same memory into both processes.

When a user process calls `IOConnectMapMemory`, it passes in, among other arguments, a pointer to an area in its own address space that will contain the mapped memory. The call to `IOConnectMapMemory` causes the invocation of the user client’s `clientMemoryForType` method. The user client implements this method by creating an IOMemoryDescriptor object that backs the mapping to the hardware registers. The user process receives a virtual memory `vm_address_t` object containing the address of the mapped memory and a `vm_size_t` object that contains the size of the mapping. At this point, the user process can freely write to and read from the hardware registers.

When the user process or device interface is finished performing I/O with the mapped memory, it should call `IOConnectUnmapMemory` to remove the mapping.

The remaining `IOConnect` functions in IOKitLib are primarily intended to help you manage your custom user space–kernel connection. As with the other `IOConnect` functions, you should not use them with I/O Kit family-supplied or third-party device interfaces because they operate directly on the `io_connect_t` object representing the connection, circumventing the existing device interface.

The IOKitLib contains the following functions to manipulate the `io_connect_t` object:

- `IOConnectAddClient`
- `IOConnectAddRef`
- `IOConnectRelease`
- `IOConnectGetService`
- `IOConnectSetNotificationPort`

The `IOConnectAddClient` function creates a connection between two user-client objects in the kernel by invoking the first user client’s `connectClient` method. You can use this function in the unlikely event that you have two user clients that need to be able to communicate.

As their names suggest, `IOConnectAddRef` and `IOConnectRelease` adjust the reference count on the passed-in `io_connect_t` object.

The `IOConnectGetService` function returns an `io_service_t` object representing the IOService object on which the passed-in `io_connect_t` object was opened. IOKitLib implements this function by invoking the user client’s `getService` method.

To identify a Mach port on which to receive family-specific notifications (notification types not interpreted by the I/O Kit), you use the `IOConnectSetNotificationPort` function. You pass in, among other arguments, the `io_connect_t` object representing the user client connection and a `mach_port_t` object representing the Mach port on which you want to receive notifications. The IOKitLib implements this function by invoking the user client’s `registerNotificationPort` method.

[Next](Handling%20Errors.md)[Previous](Finding%20and%20Accessing%20Devices.md)

