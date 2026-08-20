---
title: FireWire Device Interface Guide
apple_id: TP40000969
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: IOKit
published: '2007-02-08'
source_url: https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/WorkingWFireWireDI/FWDevAccess/FWDevAccess.html
archived_at: '2026-07-15T07:31:34.737225Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [FireWire Device Interface Guide](Introduction%20to%20FireWire%20Device%20Interface%20Guide.md)


[Next](Using%20the%20FireWire%20Device%20Interface%20Libraries.md)[Previous](FireWire%20on%20OS%20X.md)

# Accessing FireWire Devices From Applications

The device interfaces the FireWire family provides are plug-ins that supply functions your application can call to communicate with or control a device. This chapter describes how to find a FireWire device and get one or more device interfaces to communicate with it.

All user-level access of a device begins with a Mach port to communicate with the I/O Kit. You get a Mach port by calling the I/O Kit function `IOMasterPort`, as in the following example:

```
kern_return_t   result;
mach_port_t     masterPort;

result = IOMasterPort( MACH_PORT_NULL, &masterPort );
```

In order to find a device, you create a matching dictionary that describes the device or device type you’re interested in. The I/O Kit function `IOServiceMatching` creates a dictionary that matches on a given class name, as in this example:

```
CFMutableDictionaryRef  matchingDictionary = IOServiceMatching
                                                ( “IOFireWireDevice” );
```

In this example, you can use `matchingDictionary` to find all devices currently represented by an IOFireWireDevice object in the I/O Registry. [Table 2-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnrzfvbuqmrqgiwugq2ijbbuuq2f) lists the FireWire class names you can use to create a matching dictionary.

__Table 2-1__  FireWire class names

| Class name | Definition |
| IOFireWireSBP2Target | A unit in a device that is an SBP-2 target |
| IOFireWireSBP2LUN | A LUN in an SBP-2 target |
| IOFireWireAVCUnit | An AV/C unit in a device |
| IOFireWireUnit | A unit in a device |
| IOFireWireDevice | A device on the FireWire Bus |
| IOFireWireLocalNode | The Macintosh itself |

If you do not need to perform a more specific search, the dictionary `IOServiceMatching` creates will be sufficient to find all devices of a particular class currently in the I/O Registry.

If you want to refine your search, you can add properties to the dictionary to describe a unique device. As described in [In-Kernel FireWire Device Support](FireWire%20on%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnrzfvbuqmrqgewueqsjireecrsj), the IOFireWire family places properties that describe each device and unit into the objects that represent them in the I/O Registry. You can use any of these properties to narrow down your search for a specific device or unit. [Table 2-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnrzfvbuqmrqgiwugq2ijbfeqrkh) shows the properties available in each object.

__Table 2-2__  FireWire class properties

| Class name | Property key | Definition | Type |
| IOFireWireDevice | `FireWire Node ID` | Current node ID | `CFNumber` |
| IOFireWireDevice | `Vendor_ID` | Device vendor ID | `CFNumber` |
| IOFireWireDevice | `FireWire Device ROM` | Currently read contents of config ROM (may not contain entire ROM contents) | `CFData` |
| IOFireWireDevice | `FireWire Vendor Name` | Device vendor name | `CFString` |
| IOFireWireDevice | `FireWire Self IDs` | Self IDs received from device | `CFData` |
| IOFireWireDevice | `FireWire Speed` | Current operating speed of device | `CFNumber` |
| IOFireWireDevice | `GUID` | Globally unique ID of device | `CFNumber` |
| IOFireWireUnit | `Vendor_ID` | Device vendor ID | `CFNumber` |
| IOFireWireUnit | `FireWire Vendor Name` | Device vendor name | `CFString` |
| IOFireWireUnit | `GUID` | Globally unique ID of unit | `CFNumber` |
| IOFireWireUnit | `Unit_Spec_ID` | Unit spec ID for this unit | `CFNumber` |
| IOFireWireUnit | `Unit_SW_Version` | Unit software version of unit | `CFNumber` |
| IOFireWireUnit | `FireWire Product Name` | Product name of device | `CFString` |
| IOFireWireSBP2Target | `Command_Set` | SBP2 command set | `CFNumber` |
| IOFireWireSBP2Target | `Command_Set_Revision` | SBP2 command set revision | `CFNumber` |
| IOFireWireSBP2Target | `Unit_Spec_ID` | Unit spec ID for FireWire unit provider of this SBP-2 target | `CFNumber` |
| IOFireWireSBP2Target | `Command_Set_Spec_ID` | SBP-2 command set spec ID | `CFNumber` |
| IOFireWireSBP2Target | `GUID` | Globally unique ID for this device | `CFNumber` |
| IOFireWireSBP2Target | `Vendor_ID` | Device vendor ID | `CFNumber` |
| IOFireWireSBP2Target | `Device_Type` | SBP-2 device type | `CFNumber` |
| IOFireWireSBP2Target | `Firmware_Revision` | SBP-2 firmware revision | `CFNumber` |
| IOFireWireSBP2Target | `Unit_SW_Version` | Unit software version for this unit | `CFNumber` |
| IOFireWireSBP2LUN | `Vendor_ID` | Device vendor ID | `CFNumber` |
| IOFireWireSBP2LUN | `Command_Set` | SBP-2 command set | `CFNumber` |
| IOFireWireSBP2LUN | `Command_Set_Spec_ID` | SBP-2 command set spec ID | `CFNumber` |
| IOFireWireSBP2LUN | `GUID` | Globally unique ID for this device | `CFNumber` |
| IOFireWireSBP2LUN | `Device_Type` | SBP-2 device type | `CFNumber` |
| IOFireWireSBP2LUN | `Firmware_Revision` | SBP-2 firmware revision | `CFNumber` |
| IOFireWireSBP2LUN | `IOUnit` | SBP-2 LUN number | `CFNumber` |
| IOFireWireAVCUnit | `Unit_Spec_ID` | Unit spec ID for this unit | `CFNumber` |
| IOFireWireAVCUnit | `Unit_Type` | AV/C unit type | `CFNumber` |
| IOFireWireAVCUnit | `Vendor_ID` | Device vendor ID | `CFNumber` |
| IOFireWireAVCUnit | `GUID` | Globally unique ID for this device | `CFNumber` |
| IOFireWireAVCUnit | `Unit_SW_Version` | Unit software version for this unit | `CFNumber` |
| IOFireWireAVCUnit | `FireWire Product Name` | Name of this product | `CFString` |

To use these properties for matching, start with a dictionary from `IOServiceMatching` and use Core Foundation functions to add property key-value pairs to it. [Listing 2-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnrzfvbuqmrqgiwugq2ijfeugskj) shows a dictionary that matches on an IOFireWireUnit object with specific `Unit_Spec_ID` and `Unit_SW_Version` values:

__Listing 2-1__  A matching dictionary for an IOFireWireUnit object

```
CFMutableDictionaryRef  matchingDictionary =
                                    IOServiceMatching(“IOFireWireUnit” );

UInt32      value;
CFNumberRef cfValue;

value = myFireWireUnitSpecID;
cfValue = CFNumberCreate( kCFAllocatorDefault, kCFNumberSInt32Type, &value );
CFDictionaryAddValue( matchingDictionary, CFSTR( “Unit_Spec_ID” ), cfValue );
CFRelease( cfValue );

value = myFireWireUnitSwVersionID;
cfValue = CFNumberCreate( kCFAllocatorDefault, kCFNumberSInt32Type, &value );
CFDictionaryAddValue( matchingDictionary, CFSTR( “Unit_SW_Version” ),
                        cfValue);
CFRelease( cfValue );
```


After setting up a matching dictionary that describes the device or device type you’re looking for, you pass it to the I/O Kit function `IOServiceGetMatchingServices`. This function searches the I/O Registry for objects that match the properties in the given dictionary and returns an iterator you can use to access each one:

```
kern_return_t   result;
io_iterator_t   iterator;

result = IOServiceGetMatchingServices( masterPort, matchingDictionary,
    &iterator );
```

Next, pass the iterator to the I/O Kit function `IOIteratorNext`, which returns a reference to the first matching object. Each call to `IOIteratorNext` returns the next available object:

```
io_object_t aDevice;

while ( (aDevice = IOIteratorNext( iterator ) ) != 0 ) {
    //get a device interface for the device
}
```

You can also use I/O Kit functions to receive device hot-plug and unplug notifications. To do this, you first set up a notification port and add its run loop event source to your program’s run loop. Then, instead of calling `IOServiceGetMatchingServices`, you send the matching dictionary you created earlier to the I/O Kit function `IOServiceAddMatchingNotification` to get an iterator for matching device objects and install a notification request for new device objects that match. The function `myServiceMatchingCallback` is a function you supply to iterate over the matching devices and access each one. [Listing 2-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnrzfvbuqmrqgiwugq2iivcekqkk) shows how to set up a notification.

__Listing 2-2__  Setting up a device hot-plug notification

```
//global variables
IONotificationPortRef   gNotifyPort;
CFRunLoopSourceRef      gNotifySource;

//local variables
io_iterator_t   iterator;
kern_return_t   result;
mach_port_t     masterPort;
CFMutableDictionaryRef  matchingDictionary;

//The acquisition of the Mach port and the creation of the matching
//dictionary are not shown here.
gNotifyPort = IONotificationPortCreate( masterPort );
gNotifySource = IONotificationPortGetRunLoopSource( gNotifyPort );
CFRunLoopAddSource( CFRunLoopGetCurrent(), gNotifySource,
    kCFRunLoopDefaultMode );

result = IOServiceAddMatchingNotification( gNotifyPort,
    kIOMatchedNotification, matchingDictionary,
    myServiceMatchingCallback, NULL, &iterator );

//IOServiceAddMatchingNotification consumes a reference to the
//matching dictionary so if you need to use the dictionary again
//after this call, you must first call CFRetain on it.

//Execute your callback function to iterate over the set of matching
//devices already present and to arm the notification for future devices.
myServiceMatchingCallback( NULL, iterator );
```


After you’ve gotten an iterator and used it to get a reference to each matching device, you need to get a device interface for it. Regardless of which FireWire device interface library you want to use, you first get a plug-in interface of type IOCFPlugInInterface. You use the device’s `io_object_t` reference you got from `IOIteratorNext` and the constant `kIOFireWireLibTypeID`, as in this example:

```
IOCFPlugInInterface**   cfPlugInInterface = 0;
IOReturn                result;
SInt32                  theScore;

result = IOCreatePlugInInterfaceForService( aDevice, kIOFireWireLibTypeID,
    kIOCFPlugInInterfaceID, &cfPlugInInterface, &theScore );
```

Then, you use the IOCFPlugInInterface `QueryInterface` function to get the specific device interface you need. You pass it the identifier of the primary device interface you want to use, for example, `kIOFireWireDeviceInterfaceID` or `kIOFireWireSBP2LibLUNInterfaceID`:

```swift
IOFireWireLibDeviceRef  fwDeviceInterface = 0;

(*cfPlugInInterface)->QueryInterface( cfPlugInInterface, CFUUIDGetUUIDBytes(
    kIOFireWireDeviceInterfaceID ), (void **) fwDeviceInterface );
```

There are three versions of the IOFireWireDeviceInterface you can use. Each version adds new services to the functionality of the previous version. Be sure to check the header files to make sure you’re running the version of OS X that corresponds to the IOFireWireDeviceInterface version you want. If you try to get a later version of IOFireWireDeviceInterface than your version of OS X supports, the `QueryInterface` function will fail. You can, however, get an earlier version of the interface than is currently supported by the version of OS X you’re running.

You can also get instances of IOFireWireUnitInterface and IOFireWireNubInterface. These are synonymous with IOFireWireDeviceInterface and refer to the same object. Their only function is to provide you with a more descriptive name for IOFireWireDeviceInterface if you open it on a unit or the local node.

When you have the primary device interface in the library you want to use, you do not have to use the `IOCreatePlugInForService` and `QueryInterface` functions to get the additional interfaces that library provides. Each library provides its own functions to get its other interfaces.

When you open a device or unit using one of the device interface `open` functions, you have an exclusive connection to the object representing that device or unit in the kernel. Because the `open` function opens not only the object you call it on but also the objects that precede it in the stack, no other application can then open that device or unit. For example, if you open an AV/C unit with the IOFireWireAVCLibUnitInterface’s `open` function, you are automatically opening the IOFireWireUnit and IOFireWireDevice objects as well as the IOFireWireAVCUnit object.

Thus, if you want to use either the IOFireWireSBP2Lib or the IOFireWireAVCLib in cooperation with the IOFireWireLib, you must, in effect, open a device or unit object that is already open. In order to allow this, the IOFireWire family uses the concept of a session reference to refer to a particular connection to a device or unit object.

A session reference is like a key that allows you to override the exclusivity of the `open` function. If your application used a device interface `open` function to open an SBP-2 or AV/C unit, you can use the `GetSessionRef` function (available in both IOFireWireAVCLib and IOFireWireSBP2Lib) to get an `IOFireWireSessionRef` to open the IOFireWireUnit or IOFireWireDevice objects. The `GetSessionRef` function requires a pointer to the current device interface you hold so only your application can successfully use it.

You pass the `IOFireWireSessionRef` to the IOFireWireDeviceInterface function `openWithSessionRef`, opening the in-kernel device or unit object. You can then use the interfaces and functions of both libraries to communicate with your device or unit. [Listing 2-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnrzfvbuqmrqgiwugq2iivaugssg) shows how to use an IOFireWireAVCLibUnitInterface instance to open an AV/C unit and then get the session reference to open the device for an instance of IOFireWireDeviceInterface.

__Listing 2-3__  Getting and using the session reference

```swift
IOFireWireSessionRef    session;

result = (*avcInterface)->open( avcInterface );
session = (*avcInterface)->getSessionRef( avcInterface );
result = (*fwInterface)->openWithSessionRef( fwInterface, session );
```

Before you can use these device interfaces, however, you must first find the device you’re interested in. Device matching is the process of using I/O Kit functions to search the I/O Registry for particular devices (or units) or device types. This section provides general information on this process as it applies to FireWire devices. It supplies code fragments for common tasks such as searching the I/O Registry, setting up notifications for new devices, and getting the primary device interfaces in each FireWire device interface library. In addition, in [Getting Multiple FireWire Device Interfaces](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnrzfvbuqmrqgiwugq2ijjaugskk), it describes how to use the IOFireWireDeviceInterface in conjunction with either the IOFireWireSBP2LibLUNInterface or the IOFireWireAVCLibUnitInterface.

[Next](Using%20the%20FireWire%20Device%20Interface%20Libraries.md)[Previous](FireWire%20on%20OS%20X.md)

