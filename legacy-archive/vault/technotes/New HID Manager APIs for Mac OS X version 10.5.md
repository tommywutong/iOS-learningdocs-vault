---
title: New HID Manager APIs for Mac OS X version 10.5
apple_id: DTS10004224
resource_type: Technical Note
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: IOKit
published: '2009-05-04'
source_url: https://developer.apple.com/library/archive/technotes/tn2187/_index.html
archived_at: '2026-07-26T19:54:09.086739Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2187

# New HID Manager APIs for Mac OS X version 10.5

Mac OS X version 10.5 ("Leopard") introduces new APIs that abstract the current complexities of utilizing the I/O Kit to communicate with the HID Manager. New procedural APIs are provided to enumerate HID devices and elements, access their properties, register for notifications of HID device discovery and removal (hot plugging and unplugging), send and receive device reports, use queues to get notifications of HID element value changes and use transactions to talk to HID devices. Application developers that need to communicate with HID devices should read this document.

This documentation assumes a basic understanding of the material contained in [Accessing Hardware From Applications](https://developer.apple.com/documentation/DeviceDrivers/Conceptual/AccessingHardware/index.html). For definitions of I/O Kit terms used in this documentation (such as matching dictionaries) see the overview of I/O Kit terms and concepts in the [Device Access and the I/O Kit](https://developer.apple.com/documentation/DeviceDrivers/Conceptual/AccessingHardware/AH_Device_Access_IOKit/AH_Device_Access_IOKit.html#//apple_ref/doc/uid/TP30000378-BAJDAJDJ) chapter. A detailed description of the HID class specification is beyond the scope of this document. For more information, including the complete listing of HID usage tables, visit the USB website at [http://www.usb.org/developers/hidpage/](http://www.usb.org/developers/hidpage/).

__Note:__ For binary compatibility, HID code written for Mac OS X version 10.4 ("Tiger") will continue to work for the lifetime of Mac OS X version 10.5 ("Leopard"). New development targeting Leopard should use the new HID Manager APIs.

[HID Manager Functions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimrsgqwugsbrfvjukq2ujfhu4mi)[HID Device Functions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimrsgqwugsbrfvjukq2ujfhu4mq)[HID Element Functions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimrsgqwugsbrfvjukq2ujfhu4my)[HID Queue Functions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimrsgqwugsbrfvjukq2ujfhu4na)[HID Transaction Functions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimrsgqwugsbrfvjukq2ujfhu4ni)[HID Value Functions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimrsgqwugsbrfvjukq2ujfhu4nq)[References](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimrsgqwugsbrfvjukq2ujfhu4ny)[Sample code:](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimrsgqwugsbrfvjvkqstivbviskpjy3q)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimrsgqwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## HID Manager Functions

HID Manager references are used to communicate with the IOHID subsystem. They are created by using the IOHIDManagerCreate function:

```
// Create HID Manager reference IOHIDManagerRef IOHIDManagerCreate(                     CFAllocatorRef  inCFAllocatorRef,   // Allocator to be used during creation                     IOOptionBits    inOptions ); // options Reserved for future use
```

The first parameter ( allocator ) is a CFAllocator to be used when allocating the returned IOHIDManagerRef. The last parameter ( options ) is currently reserved for future use. Developers should pass kIOHIDOptionsTypeNone ( zero ) for this parameter.

There is no IOHIDManagerDestroy ( or release, free, etc. ); but since the HID Manager reference is a Core Foundation object reference then CFRelease should be used to dispose of it.

A CFTypeRef can be verified to be a HID Manager reference by comparing its Core Foundation type against IOHIDManagerGetTypeID:

__Listing 1__  Validating a HID Manager reference

```
 if ( CFGetTypeID( tCFTypeRef ) == IOHIDManagerGetTypeID( ) ) {         // this is a HID Manager reference!     }
```

Once a HID Manager reference has been created, it has to be opened before it can be used to access the HID devices associated with it. To restrict the HID devices with which a HID Manager reference is associated set a matching dictionary ( single criteria ) or array of matching dictionaries ( multiple criteria ). The functions are:

```
// Sets single matching criteria ( dictionary ) for device enumeration. void IOHIDManagerSetDeviceMatching(          IOHIDManagerRef inIOHIDManagerRef,  // HID Manager reference         CFDictionaryRef inMatchingDictRef ); // single dictionary containing device matching criteria.  // Sets multiple matching criteria ( array of dictionaries ) for device enumeration. void IOHIDManagerSetDeviceMatchingMultiple(          IOHIDManagerRef inIOHIDManagerRef,    // HID Manager reference         CFArrayRef      inCFArrayRef ); // array of dictionaries containing device matching criteria.
```

__Note:__ Ether one of the above APIs must be called before any devices will be matched.

The matching keys used in the dictionary entries are declared in <IOKit/hid/IOHIDKeys.h>:

__Listing 2__  HID device property keys

```c
#include <IOKit/hid/IOHIDKeys.h>  #define kIOHIDTransportKey                  "Transport" #define kIOHIDVendorIDKey                   "VendorID" #define kIOHIDVendorIDSourceKey             "VendorIDSource" #define kIOHIDProductIDKey                  "ProductID" #define kIOHIDVersionNumberKey              "VersionNumber" #define kIOHIDManufacturerKey               "Manufacturer" #define kIOHIDProductKey                    "Product" #define kIOHIDSerialNumberKey               "SerialNumber" #define kIOHIDCountryCodeKey                "CountryCode" #define kIOHIDLocationIDKey                 "LocationID" #define kIOHIDDeviceUsageKey                "DeviceUsage" #define kIOHIDDeviceUsagePageKey            "DeviceUsagePage" #define kIOHIDDeviceUsagePairsKey           "DeviceUsagePairs" #define kIOHIDPrimaryUsageKey               "PrimaryUsage" #define kIOHIDPrimaryUsagePageKey           "PrimaryUsagePage" #define kIOHIDMaxInputReportSizeKey         "MaxInputReportSize" #define kIOHIDMaxOutputReportSizeKey        "MaxOutputReportSize" #define kIOHIDMaxFeatureReportSizeKey       "MaxFeatureReportSize" #define kIOHIDReportIntervalKey             "ReportInterval"
```

__Note:__ kIOHIDPrimaryUsageKey and kIOHIDPrimaryUsagePageKey are no longer rich enough to describe a HID device's capabilities. For example, take a HID device that describes both a keyboard and a mouse in the same descriptor. The previous behavior was to only describe the keyboard behavior with the primary usage and usage page. Needless to say, this would sometimes cause a program interested in mice to skip this device when matching. To resolve this issue three additional keys have been added:

- kIOHIDDeviceUsageKey
- kIOHIDDeviceUsagePageKey
- kIOHIDDeviceUsagePairsKey

kIOHIDDeviceUsagePairsKey is used to represent an array of dictionaries containing key/value pairs referenced by kIOHIDDeviceUsageKey and kIOHIDDeviceUsagePageKey. These usage pairs describe all application type collections ( behaviors ) defined by the HID device.

An application interested in only matching on one criteria would only add the kIOHIDDeviceUsageKey and kIOHIDDeviceUsagePageKey keys to the matching dictionary. If it is interested in a HID device that has multiple behaviors, the application would instead add an array of dictionaries referenced by kIOHIDDeviceUsagePairsKey to their matching dictionary.

This is equivalent to passing an array of dictionaries each containing two entries with keys kIOHIDDeviceUsagePageKey and kIOHIDDeviceUsageKey to IOHIDManagerSetDeviceMatchingMultiple.

Passing a NULL dictionary will result in all devices being enumerated. Any subsequent calls will cause the HID Manager to release previously enumerated devices and restart the enumeration process using the revised criteria.

__Listing 3__  Matching against a single set ( a dictionary ) of properties

```
// function to create matching dictionary static CFMutableDictionaryRef hu_CreateDeviceMatchingDictionary( UInt32 inUsagePage, UInt32 inUsage ) {     // create a dictionary to add usage page/usages to     CFMutableDictionaryRef result = CFDictionaryCreateMutable(          kCFAllocatorDefault, 0, &kCFTypeDictionaryKeyCallBacks, &kCFTypeDictionaryValueCallBacks );     if ( result ) {         if ( inUsagePage ) {             // Add key for device type to refine the matching dictionary.             CFNumberRef pageCFNumberRef = CFNumberCreate(                              kCFAllocatorDefault, kCFNumberIntType, &inUsagePage );             if ( pageCFNumberRef ) {                 CFDictionarySetValue( result,                          CFSTR( kIOHIDDeviceUsagePageKey ), pageCFNumberRef );                 CFRelease( pageCFNumberRef );                  // note: the usage is only valid if the usage page is also defined                 if ( inUsage ) {                     CFNumberRef usageCFNumberRef = CFNumberCreate(                                      kCFAllocatorDefault, kCFNumberIntType, &inUsage );                     if ( usageCFNumberRef ) {                         CFDictionarySetValue( result,                              CFSTR( kIOHIDDeviceUsageKey ), usageCFNumberRef );                         CFRelease( usageCFNumberRef );                     } else {                         fprintf( stderr, "%s: CFNumberCreate( usage ) failed.", __PRETTY_FUNCTION__ );                     }                 }             } else {                 fprintf( stderr, "%s: CFNumberCreate( usage page ) failed.", __PRETTY_FUNCTION__ );             }         }     } else {         fprintf( stderr, "%s: CFDictionaryCreateMutable failed.", __PRETTY_FUNCTION__ );     }     return result; }   // hu_CreateDeviceMatchingDictionary  // Create a matching dictionary CFDictionaryRef matchingCFDictRef =                      hu_CreateDeviceMatchingDictionary( kHIDPage_GenericDesktop, kHIDUsage_GD_Keyboard ); if ( matchingCFDictRef ) {     // set the HID device matching dictionary     IOHIDManagerSetDeviceMatching( managerRef, matchingCFDictRef ); } else {     fprintf( stderr, "%s: hu_CreateDeviceMatchingDictionary failed.", __PRETTY_FUNCTION__ ); }
```

__Listing 4__  Matching against multiple sets ( an array of dictionaries ) of properties

```
// create an array of matching dictionaries CFArrayRef matchingCFArrayRef = CFArrayCreateMutable( kCFAllocatorDefault, 0, &kCFTypeArrayCallBacks ); if ( matchingCFArrayRef ) {     // create a device matching dictionary for joysticks     CFDictionaryRef matchingCFDictRef =                          hu_CreateDeviceMatchingDictionary( kHIDPage_GenericDesktop, kHIDUsage_GD_Joystick );     if ( matchingCFDictRef ) {         // add it to the matching array         CFArrayAppendValue( matchingCFArrayRef, matchingCFDictRef );         CFRelease( matchingCFDictRef ); // and release it     } else {         fprintf( stderr, "%s: hu_CreateDeviceMatchingDictionary( joystick ) failed.", __PRETTY_FUNCTION__ );     }      // create a device matching dictionary for game pads     matchingCFDictRef = hu_CreateDeviceMatchingDictionary( kHIDPage_GenericDesktop, kHIDUsage_GD_GamePad );     if ( matchingCFDictRef ) {         // add it to the matching array         CFArrayAppendValue( matchingCFArrayRef, matchingCFDictRef );         CFRelease( matchingCFDictRef ); // and release it     } else {         fprintf( stderr, "%s: hu_CreateDeviceMatchingDictionary( game pad ) failed.", __PRETTY_FUNCTION__ );     } } else {     fprintf( stderr, "%s: CFArrayCreateMutable failed.", __PRETTY_FUNCTION__ ); }  -- EITHER --  // create a dictionary for the kIOHIDDeviceUsagePairsKey entry matchingCFDictRef = CFDictionaryCreateMutable(      kCFAllocatorDefault, 0, &kCFTypeDictionaryKeyCallBacks, &kCFTypeDictionaryValueCallBacks );  // add the matching array to it CFDictionarySetValue( matchingCFDictRef, CFSTR( kIOHIDDeviceUsagePairsKey ), matchingCFArrayRef ); // release the matching array CFRelease( matchingCFArrayRef );  // set the HID device matching dictionary IOHIDManagerSetDeviceMatching( managerRef, matchingCFDictRef );  // and then release it CFRelease( matchingCFDictRef );  -- OR --  // set the HID device matching array IOHIDManagerSetDeviceMatchingMultiple( managerRef, matchingCFArrayRef );  // and then release it CFRelease( matchingCFArrayRef );
```

Before opening the HID Manager reference it may be desirable to register routines to be called when ( matching ) devices are connected or disconnected.

__Note:__ This matching routine will be called once for each currently connected ( and matching ) device when the HID Manager reference is opened.

```
// Register device matching callback routine // This routine will be called when a new ( matching ) device is connected. void IOHIDManagerRegisterDeviceMatchingCallback(          IOHIDManagerRef     inIOHIDManagerRef,      // HID Manager reference         IOHIDDeviceCallback inIOHIDDeviceCallback,  // Pointer to the callback routine         void *              inContext ); // Pointer to be passed to the callback  // Registers a routine to be called when any currently enumerated device is removed. // This routine will be called when a ( matching ) device is disconnected. void IOHIDManagerRegisterDeviceRemovalCallback(          IOHIDManagerRef     inIOHIDManagerRef,      // HID Manager reference         IOHIDDeviceCallback inIOHIDDeviceCallback,  // Pointer to the callback routine         void *              inContext ); // Pointer to be passed to the callback
```

__Note:__ There is no function to unregister IOHID callback routines. They are unregistered by calling the register function and passing NULL for the pointer to the callback routine.

__Note:__ All IOHID register callback routines include a context pointer that will be passed to it when it's called. These parameters are intended for developers use and are passed as-is to the callback routines.

__Listing 5__  Examples of HID device matching & removal callback routines

```
// this will be called when the HID Manager matches a new ( hot plugged ) HID device static void Handle_DeviceMatchingCallback(              void *          inContext,       // context from IOHIDManagerRegisterDeviceMatchingCallback             IOReturn        inResult,        // the result of the matching operation             void *          inSender,        // the IOHIDManagerRef for the new device             IOHIDDeviceRef  inIOHIDDeviceRef // the new HID device  ) {     printf( "%s( context: %p, result: %p, sender: %p, device: %p ).\n",          __PRETTY_FUNCTION__, inContext, ( void * ) inResult, inSender, ( void* ) inIOHIDDeviceRef ); }   // Handle_DeviceMatchingCallback  // this will be called when a HID device is removed ( unplugged ) static void Handle_RemovalCallback(                  void *         inContext,       // context from IOHIDManagerRegisterDeviceMatchingCallback                 IOReturn       inResult,        // the result of the removing operation                 void *         inSender,        // the IOHIDManagerRef for the device being removed                 IOHIDDeviceRef inIOHIDDeviceRef // the removed HID device  ) {     printf( "%s( context: %p, result: %p, sender: %p, device: %p ).\n",          __PRETTY_FUNCTION__, inContext, ( void * ) inResult, inSender, ( void* ) inIOHIDDeviceRef ); }   // Handle_RemovalCallback
```

__Note:__ For all callback routines that include an inResult parameter—this is the error result of the operation that is calling the callback. It should be checked for non-zero to determine the success or failure of the operation.

Before HID Manager callback routines can be dispatched the HID Manager reference must first be scheduled with a run loop:

```
// Schedule HID Manager with run loop void IOHIDManagerScheduleWithRunLoop(          IOHIDManagerRef inIOHIDManagerRef,  // HID Manager reference         CFRunLoopRef    inRunLoop,          // Run loop to be used when scheduling asynchronous activity         CFStringRef     inRunLoopMode ); // Run loop mode to be used when scheduling
```

This formally associates the HID Manager with the client's run loop. This schedule will propagate to all HID devices that are currently enumerated and to new HID devices as they are matched by the HID Manager.

__Listing 6__  Scheduling a HID Manager with the current run loop

```
 IOHIDManagerScheduleWithRunLoop( inIOHIDManagerRef, CFRunLoopGetCurrent( ), kCFRunLoopDefaultMode );
```

There is a corresponding function to unschedule a HID Manager reference from a run loop:

```
void IOHIDManagerUnscheduleFromRunLoop(          IOHIDManagerRef inIOHIDManagerRef,  // HID Manager reference         CFRunLoopRef    inRunLoop,          // Run loop to be used when unscheduling asynchronous activity         CFStringRef     inRunLoopMode ); // Run loop mode to be used when unscheduling
```

__Listing 7__  Unscheduling a HID Manager from a run loop

```
IOHIDManagerUnscheduleFromRunLoop( managerRef, CFRunLoopGetCurrent( ), kCFRunLoopDefaultMode );
```

Now we're ready to open the HID Manager reference.

```
// Open a HID Manager reference IOReturn IOHIDManagerOpen(              IOHIDManagerRef inIOHIDManagerRef,  // HID Manager reference             IOOptionBits    inOptions ); // Option bits
```

This will open all matching HID devices. It returns kIOReturnSuccess if successful. Currently the only valid options ( second parameter ) are kIOHIDOptionsTypeNone or kIOHIDOptionsTypeSeizeDevice ( which will force exclusive access for all matching devices ).

__Note:__ As of Leopard, the kIOHIDOptionsTypeSeizeDevice option requires root privileges to be used with keyboard devices.

If there is a device matching callback routine registered when IOHIDManagerOpen is called then this routine will be called once for each HID device currently connected that matches the current matching criteria. This routine will also be called when new devices that match the current matching criteria are connected to the computer ( but only if the HID Manager reference is still open ).

__Listing 8__  Opening a HID Manager reference

```
// open it IOReturn tIOReturn = IOHIDManagerOpen( managerRef, kIOHIDOptionsTypeNone );
```

Once a HID Manager reference has been opened it may be closed by using the IOHIDManagerClose function:

```
// Closes the IOHIDManager IOReturn IOHIDManagerClose( IOHIDManagerRef inIOHIDManagerRef,  // HID Manager reference                             IOOptionBits    inOptions ); // Option bits
```

This will also close all devices that are currently enumerated. The options are propagated to the HID device close function.

Once a connection to the HID manager is open developers may register a routine to be called when input values change:

```
// Register a routine to be called when an input value changes void IOHIDManagerRegisterInputValueCallback(          IOHIDManagerRef     inIOHIDManagerRef,  // HID Manager reference         IOHIDValueCallback  inCallback,         // Pointer to the callback routine         void *              inContext ); // Pointer to be passed to the callback
```

The registered callback routine will be called when the HID value of any element of type kIOHIDElementTypeInput changes for all matching HID devices.

__Note:__ To unregister pass NULL for the callback.

__Note:__ The HID Manager must be scheduled with a run loop for HID Manager callbacks to be dispatched.

( See Listing 6 )

__Listing 9__  Registering for an input value callback

```
IOHIDManagerRegisterInputValueCallback( managerRef, Handle_IOHIDInputValueCallback, context );
```

This routine will be called when an input value changes for any input element for all matching devices.

__Listing 10__  Example input value callback routine

```c
static void Handle_IOHIDInputValueCallback(                  void *          inContext,      // context from IOHIDManagerRegisterInputValueCallback                 IOReturn        inResult,       // completion result for the input value operation                 void *          inSender,       // the IOHIDManagerRef                 IOHIDValueRef   inIOHIDValueRef // the new element value  ) {     printf( "%s( context: %p, result: %p, sender: %p, value: %p ).\n",          __PRETTY_FUNCTION__, inContext, ( void * ) inResult, inSender, ( void* ) inIOHIDValueRef ); }   // Handle_IOHIDInputValueCallback
```

__Note:__ HID values are documented in the "HID Value Functions" section.

If only notifications from specific devices are of interest then the IOHIDDeviceRegisterInputValueCallback function ( See Listing 19 ) should be used; For value changes on specific HID element(s) the HID queue functions ( See HID Queue Functions ) may be used or an element matching dictionary ( single criteria ) or array of matching dictionaries ( multiple criteria ) may be set via the IOHIDManagerSetInputValueMatching[Multiple] APIs.

```
// Sets single element matching criteria ( dictionary ) for the input value callback. void IOHIDManagerSetInputValueMatching(          IOHIDManagerRef inIOHIDManagerRef,  // HID Manager reference         CFDictionaryRef inMatchingDictRef ); // single dictionary containing element matching criteria.  // Sets multiple matching criteria ( array of dictionaries ) for the input value callback. void IOHIDManagerSetInputValueMatchingMultiple(          IOHIDManagerRef inIOHIDManagerRef,    // HID Manager reference         CFArrayRef      inCFArrayRef ); // array of dictionaries containing element matching criteria.
```

__Note:__ The default element criteria is to match all elements. Specific matching criteria can be reset to this default by passing NULL to ether of the above APIs.

__Note:__ The IOHIDManagerSetInputValueMatching[Multiple] and the IOHIDDeviceSetInputValueMatching[Multiple] (documented below) APIs override each other. The last one called has precedence.

The matching keys for HID elements are prefixed by kIOHIDElement and declared in <IOKit/hid/IOHIDKeys.h> ( See Listing 30 )

The IOHIDManagerGetProperty and IOHIDManagerSetProperty functions are available to access the HID Manager's properties:

```
// Obtains a property of a HIDManagerRef CFTypeRef IOHIDManagerGetProperty(              IOHIDManagerRef inIOHIDManagerRef,  // HID Manager reference             CFStringRef     inKeyCFStringRef ); // CFStringRef for the key  // Sets a property for a HIDManagerRef void IOHIDManagerSetProperty(              IOHIDManagerRef inIOHIDManagerRef,  // HID Manager reference             CFStringRef     inKeyCFStringRef,   // CFStringRef for the key             CFTypeRef       inValueCFTypeRef ); // the HID value for the property
```

Currently there are not any default HID Manager properties set by the system. However since HID Manager properties are propagated to all HID devices as they are enumerated ( matched ) this might be a convient way to set default HID device property values.

__Note:__ Currently all HID Manager, device and element properties are lost when the HID Manager reference that they are associated with is closed. Developers should save and restore any values that they want to persist outside that scope.

__Listing 11__  Accessing HID Manager properties

```
CFTypeRef tCFTypeRef = IOHIDManagerGetProperty( managerRef, key ); IOHIDManagerSetProperty( managerRef, key, tCFTypeRef );
```

To determine what devices match the current matching criteria use IOHIDManagerCopyDevices:

```
CFSetRef IOHIDManagerCopyDevices( IOHIDManagerRef inIOHIDManagerRef ); // HID Manager reference
```

The parameter is a HID Manager reference and it returns a Core Foundation set ( CFSet ) of IOHIDDeviceRefs.

__Listing 12__  Getting the set of matching HID device references

```
CFSetRef tCFSetRef = IOHIDManagerCopyDevices( managerRef );
```

The HID device references in the returned set can be obtained by using the CFSetGetValues function or or iterated over by using the CFSetApplyFunction function.

[Back to Top](#)

## HID Device Functions

A CFTypeRef can be verified to be a HID device reference by comparing its Core Foundation type against IOHIDDeviceGetTypeID:

__Listing 13__  Validating a HID device reference

```
 if ( CFGetTypeID( tCFTypeRef ) == IOHIDDeviceGetTypeID( ) ) {         // this is a valid HID device reference     }
```

Once you have a valid HID device reference the IOHIDDeviceGetProperty function can be used to access its properties ( manufacturer, vendor, product IDs, etc. ) using the HID device keys defined in <IOKit/HID/IOHIDKeys.h> ( see Listing 2 )

__Listing 14__  Examples of getting HID device properties

```
// Get a HID device's transport ( string ) CFStringRef IOHIDDevice_GetTransport( IOHIDDeviceRef inIOHIDDeviceRef ) {     return IOHIDDeviceGetProperty( inIOHIDDeviceRef, CFSTR( kIOHIDTransportKey ) ); }  // function to get a long device property // returns FALSE if the property isn't found or can't be converted to a long static Boolean IOHIDDevice_GetLongProperty(      IOHIDDeviceRef inDeviceRef,     // the HID device reference     CFStringRef inKey,              // the kIOHIDDevice key ( as a CFString )     long * outValue ) // address where to return the output value {     Boolean result = FALSE;      CFTypeRef tCFTypeRef = IOHIDDeviceGetProperty( inDeviceRef, inKey );     if ( tCFTypeRef ) {         // if this is a number         if ( CFNumberGetTypeID( ) == CFGetTypeID( tCFTypeRef ) ) {             // get its value             result = CFNumberGetValue( ( CFNumberRef ) tCFTypeRef, kCFNumberSInt32Type, outValue );         }     }     return result; }   // IOHIDDevice_GetLongProperty  // Get a HID device's vendor ID ( long ) long IOHIDDevice_GetVendorID( IOHIDDeviceRef inIOHIDDeviceRef ) {     long result = 0;     ( void ) IOHIDDevice_GetLongProperty( inIOHIDDeviceRef, CFSTR( kIOHIDVendorIDKey ), &result );     return result; } // IOHIDDevice_GetVendorID  // Get a HID device's product ID ( long ) long IOHIDDevice_GetProductID( IOHIDDeviceRef inIOHIDDeviceRef ) {     long result = 0;     ( void ) IOHIDDevice_GetLongProperty( inIOHIDDeviceRef, CFSTR( kIOHIDProductIDKey ), &result );     return result; } // IOHIDDevice_GetProductID
```

There is a convenience function that will scan a device's application collection elements to determine if it confirms to a specified usage page and usage:

```
Boolean IOHIDDeviceConformsTo( IOHIDDeviceRef   inIOHIDDeviceRef, // IOHIDDeviceRef for the HID device                                 uint32_t        inUsagePage,      // the usage page to test conformance with                                 uint32_t        inUsage ); // the usage to test conformance with
```

Some examples of application collection usage pairs are:

- usagePage = kHIDPage_GenericDesktop, usage = kHIDUsage_GD_Mouse
- usagePage = kHIDPage_GenericDesktop, usage = kHIDUsage_GD_Keyboard

Before you can communicate with a HID device it has to be opened; Opened HID device references should be closed when communications are complete. Here are the functions to open and close a HID device reference:

```
IOReturn IOHIDDeviceOpen( IOHIDDeviceRef  inIOHIDDeviceRef, // IOHIDDeviceRef for the HID device                           IOOptionBits    inOptions ); // Option bits to be sent down to the HID device IOReturn IOHIDDeviceClose( IOHIDDeviceRef  IOHIDDeviceRef,  // IOHIDDeviceRef for the HID device                           IOOptionBits    inOptions ); // Option bits to be sent down to the HID device
```

On the IOHIDDeviceOpen call developers may pass kIOHIDOptionsTypeNone or kIOHIDOptionsTypeSeizeDevice option to request exclusive access to the HID device. Both functions return kIOReturnSuccess if successful.

__Note:__ As of Leopard, the kIOHIDOptionsTypeSeizeDevice option requires root privileges to be used with keyboard devices.

Callbacks can be registered that will be called when a HID device is unplugged, when input values change, when input reports are received, or when asynchronous get and set value and report functions complete ( all these callbacks are documented below ). For these HID device callbacks to be dispatched the HID device must first be scheduled with a run loop.

__Note:__ By default when new devices are matched they are automatically scheduled with the same run loop as the HID Manager used to match the HID device ( if it is scheduled with a run loop ) in which case this additional step is unnecessary.

__Listing 15__  Scheduling a HID device with a run loop

```
 IOHIDDeviceScheduleWithRunLoop( inIOHIDDeviceRef, CFRunLoopGetCurrent( ), kCFRunLoopDefaultMode );
```

There is a corresponding function to unschedule a HID device from a run loop:

__Listing 16__  Unscheduling a HID device from a run loop

```
IOHIDDeviceUnscheduleFromRunLoop( deviceRef, CFRunLoopGetCurrent( ), kCFRunLoopDefaultMode );
```

To register a routine to be called when a HID device is removed:

__Listing 17__  Registering a HID device removal callback routine

```
IOHIDDeviceRegisterRemovalCallback( deviceRef, Handle_IOHIDDeviceRemovalCallback, context );
```

__Note:__ To unregister pass NULL for the callback.

__Listing 18__  HID device removal callback routine

```c
static void Handle_IOHIDDeviceRemovalCallback(                  void *      inContext,  // context from IOHIDDeviceRegisterRemovalCallback                 IOReturn    inResult,   // the result of the removal                 void *      inSender    // IOHIDDeviceRef for the HID device being removed  ) {     printf( "%s( context: %p, result: %p, sender: %p ).\n",          __PRETTY_FUNCTION__, inContext, ( void * ) inResult, inSender ); }   // Handle_IOHIDDeviceRemovalCallback
```

To register a routine to be called when an input value is changed by a HID device:

__Listing 19__  Registering a HID device input value callback routine

```
IOHIDDeviceRegisterInputValueCallback( deviceRef, Handle_IOHIDDeviceInputValueCallback, context );
```

The first parameter is a HID device reference; the second is the callback routine and the third parameter is a user context parameter that is passed to the callback routine.

__Note:__ To unregister pass NULL for the callback.

__Listing 20__  HID device input value callback routine

```c
static void Handle_IOHIDDeviceInputValueCallback(                  void *          inContext,      // context from IOHIDDeviceRegisterInputValueCallback                 IOReturn        inResult,       // completion result for the input value operation                 void *          inSender,       // IOHIDDeviceRef of the device this element is from                 IOHIDValueRef   inIOHIDValueRef // the new element value  ) {     printf( "%s( context: %p, result: %p, sender: %p, value: %p ).\n",          __PRETTY_FUNCTION__, inContext, ( void * ) inResult, inSender, ( void* ) inIOHIDValueRef ); }   // Handle_IOHIDDeviceInputValueCallback
```

__Note:__ HID values are documented in the "HID Value Functions" section.

The limit the element value changes reported by this callback to specific HID element(s) an element matching dictionary ( single criteria ) or array of matching dictionaries ( multiple criteria ) may be set via the IOHIDDeviceSetInputValueMatching[Multiple] APIs.

```
// Sets single element matching criteria ( dictionary ) for the input value callback. void IOHIDDeviceSetInputValueMatching(          IOHIDDeviceRef  inIOHIDDeviceRef,		// IOHIDDeviceRef for the HID device         CFDictionaryRef inMatchingDictRef ); // single dictionary containing element matching criteria.  // Sets multiple matching criteria ( array of dictionaries ) for the input value callback. void IOHIDDeviceSetInputValueMatchingMultiple(          IOHIDDeviceRef  inIOHIDDeviceRef,	// IOHIDDeviceRef for the HID device         CFArrayRef      inCFArrayRef ); // array of dictionaries containing element matching criteria.
```

__Note:__ The default element criteria is to match all elements. Specific matching criteria can be reset to this default by passing NULL to ether of the above APIs.

__Note:__ The IOHIDDeviceSetInputValueMatching[Multiple] and IOHIDManagerSetInputValueMatching[Multiple] (documented above) APIs override each other. The last one called has precedence.

The matching keys for HID elements are prefixed by kIOHIDElement and declared in <IOKit/hid/IOHIDKeys.h> ( See Listing 30 )

To register a routine to be called when an input report is issued by a HID device:

__Listing 21__  Registering a HID device input report callback routine

```
CFIndex reportSize = 64; // note: this should be greater than or equal to the size of the report uint8_t report = malloc( reportSize ); IOHIDDeviceRegisterInputReportCallback( deviceRef,          // IOHIDDeviceRef for the HID device                                         report,             // pointer to the report data ( uint8_t's )                                         reportSize,         // number of bytes in the report ( CFIndex )                                         Handle_IOHIDDeviceIOHIDReportCallback,   // the callback routine                                         context ); // context passed to callback
```

The first parameter is a HID device reference; the second is the address where to store the input report, the third parameter is the address of the callback routine and the last parameter is a user context parameter that is passed to the callback routine.

__Note:__ To unregister pass NULL for the callback.

The report buffer should be large enough to store the largest report that can be expected to be received from the HID device. This size can be obtained by passing kIOHIDMaxInputReportSizeKey as the key to IOHIDDeviceGetProperty.

__Listing 22__  HID device input report callback routine

```c
static void Handle_IOHIDDeviceIOHIDReportCallback(                  void *          inContext,          // context from IOHIDDeviceRegisterInputReportCallback                 IOReturn        inResult,           // completion result for the input report operation                 void *          inSender,           // IOHIDDeviceRef of the device this report is from                 IOHIDReportType inType,             // the report type                 uint32_t        inReportID,         // the report ID                 uint8_t *       inReport,           // pointer to the report data                 CFIndex         inReportLength ) // the actual size of the input report {     printf( "%s( context: %p, result: %p, sender: %p," \             "type: %d, id: %p, report: %p, length: %d ).\n",          __PRETTY_FUNCTION__, inContext, ( void * ) inResult, inSender,         ( long ) inType, inReportID, inReport, inReportLength ); }   // Handle_IOHIDDeviceIOHIDReportCallback
```

__Note:__ The layout and the size of the report data is device specific and requires advanced knowledge of how elements are bundled into reports. While this knowledge is available by parsing HID device descriptors this also requires advanced knowledge. A higher level abstraction that doesn't require as much advanced knowledge is the HID transactions APIs described in the "HID Transaction Functions" section.

To set the HID value of a single output or feature type element the IOHIDDeviceSetValue ( synchronous ) or IOHIDDeviceSetValueWithCallback ( asynchronous ) functions may be used. ( to set multiple values consider using reports or transactions ):

```
// synchronous IOReturn  tIOReturn = IOHIDDeviceSetValue(                              deviceRef,      // IOHIDDeviceRef for the HID device                             elementRef,     // IOHIDElementRef for the HID element                             valueRef ); // IOHIDValueRef for the HID element's new value  // asynchronous IOReturn  tIOReturn = IOHIDDeviceSetValueWithCallback(                              deviceRef,          // IOHIDDeviceRef for the HID device                             elementRef,         // IOHIDElementRef for the HID element                             valueRef,           // IOHIDValueRef for the HID element's new value                             tCFTimeInterval,    // timeout duration                             Handle_IOHIDDeviceSetValueCallback,  // the callback routine                             context ); // context passed to callback
```

The first parameter is a HID device reference; the second is HID element reference and the third parameter is a HID value reference. For the asynchronous version the fourth parameter is a timeout, the fifth parameter is the callback routine and the last parameter is the context to pass to the callback routine:

__Listing 23__  HID device set value callback routine

```c
static void Handle_IOHIDDeviceSetValueCallback(                  void *          inContext,          // context from IOHIDDeviceSetValueWithCallback                 IOReturn        inResult,           // completion result for the set value operation                 void *          inSender,           // IOHIDDeviceRef of the device                 IOHIDValueRef   inIOHIDValueRef ) // the HID element value {     printf( "%s( context: %p, result: %p, sender: %p, value: %p ).\n",          __PRETTY_FUNCTION__, inContext, ( void * ) inResult, inSender, inIOHIDValueRef ); }   // Handle_IOHIDDeviceSetValueCallback
```

__Note:__ HID values are documented in the "HID Value Functions" section.

To get the HID value of a single element the IOHIDDeviceGetValue ( synchronous ) or IOHIDDeviceGetValueWithCallback ( asynchronous ) functions may be used. ( To get multiple values consider using reports or transactions. ) For input type elements the synchronous function returns immediately; for feature type elements it will block until the get value report has been issued to the HID device.

```
// synchronous IOReturn  tIOReturn = IOHIDDeviceGetValue(                              deviceRef,  // IOHIDDeviceRef for the HID device                             elementRef, // IOHIDElementRef for the HID element                             valueRef ); // IOHIDValueRef for the HID element's new value  // asynchronous IOReturn  tIOReturn = IOHIDDeviceGetValueWithCallback(                              deviceRef,          // IOHIDDeviceRef for the HID device                             elementRef,         // IOHIDElementRef for the HID element                             valueRef,           // IOHIDValueRef for the HID element's new value                             tCFTimeInterval,    // timeout duration                             Handle_IOHIDDeviceGetValueCallback,  // the callback routine                             context ); // context passed to callback
```

For both of these functions the first parameter is a HID device reference; the second is HID element reference and the third parameter is a HID value reference. For the asynchronous version the fourth parameter is a timeout, the fifth parameter is the callback routine and the last parameter is the context to pass to the callback routine:

__Listing 24__  HID device get value callback routine

```c
static void Handle_IOHIDDeviceGetValueCallback(                  void *          inContext,          // context from IOHIDDeviceGetValueWithCallback                 IOReturn        inResult,           // completion result for the get value operation                 void *          inSender,           // IOHIDDeviceRef of the device                 IOHIDValueRef   inIOHIDValueRef ) // the HID element value {     printf( "%s( context: %p, result: %p, sender: %p, value: %p ).\n",          __PRETTY_FUNCTION__, inContext, ( void * ) inResult, inSender, inIOHIDValueRef ); }   // Handle_IOHIDDeviceGetValueCallback
```

__Note:__ HID values are documented in the "HID Value Functions" section.

USB data is transferred to and from HID devices packetized into reports. These reports consist of one or more element fields usually contained in a hierarchy of collections. Developers that understand how elements are packaged into reports can use the IOHIDDeviceGetReport[WithCallback] or IOHIDDeviceSetReport[WithCallback] to talk directly with HID devices. ( Developers unfamiliar with how HID reports are constructed may use the HID transaction functions ( See HID Transaction Functions ). )

To send a report to a HID device the IOHIDDeviceSetReport ( synchronous ) or IOHIDDeviceSetReportWithCallback ( asynchronous ) functions should be used:

__Listing 25__  Sending a HID Report

```
CFIndex reportSize = 64; uint8_t report = malloc( reportSize );  // synchronous IOReturn  tIOReturn = IOHIDDeviceSetReport(                              deviceRef,          // IOHIDDeviceRef for the HID device                             tIOHIDReportType,   // IOHIDReportType for the report                             reportID,           // CFIndex for the report ID                             report,             // address of report buffer                             reportLength ); // length of the report  // asynchronous IOReturn  tIOReturn = IOHIDDeviceSetReportWithCallback(                              deviceRef,          // IOHIDDeviceRef for the HID device                             tIOHIDReportType,   // IOHIDReportType for the report                             reportID,           // CFIndex for the report ID                             report,             // address of report buffer                             reportLength,       // length of the report                             tCFTimeInterval,    // timeout duration                             Handle_IOHIDDeviceSetReportCallback,  // the callback routine                             context ); // context passed to callback
```

For both of these functions the first parameter is a HID device reference. The second is a IOHIDReportType for the report; the third parameter is the report ID; the fourth parameter is the address of the report buffer and the fifth parameter is the size of the report being sent. For the asynchronous version the sixth parameter is a timeout; the seventh parameter is the callback routine and the last parameter is the context to pass to the callback routine:

__Listing 26__  HID device set report callback routine

```c
static void Handle_IOHIDDeviceSetReportCallback(                  void *          inContext,          // context from IOHIDDeviceSetReportWithCallback                 IOReturn        inResult,           // completion result for the set value operation                 void *          inSender,           // IOHIDDeviceRef of the device this report is from                 IOHIDReportType inIOHIDReportType,  // the report type                 uint32_t        inReportID,         // the report ID                 uint8_t*        inReport,           // the address of the report                 CFIndex         inReportLength ) // the length of the report {     printf( "%s( context: %p, result: %p, sender: %p, "  \             "type: %d, id: %d, report: %p, length: %p ).\n",          __PRETTY_FUNCTION__, inContext, ( void * ) inResult, inSender,          inIOHIDReportType, inReportID, inReport, inReportLength ); }   // Handle_IOHIDDeviceSetReportCallback
```

To request a report from a HID device the IOHIDDeviceGetReport ( synchronous ) or IOHIDDeviceGetReportWithCallback ( asynchronous ) functions should be used:

```
// synchronous IOReturn  tIOReturn = IOHIDDeviceGetReport(                              deviceRef,          // IOHIDDeviceRef for the HID device                             tIOHIDReportType,   // IOHIDReportType for the report                             reportID,           // CFIndex for the report ID                             report,             // address of report buffer                             &reportSize ); // address of length of the report  // asynchronous IOReturn  tIOReturn = IOHIDDeviceGetReportWithCallback(                              deviceRef,          // IOHIDDeviceRef for the HID device                             tIOHIDReportType,   // IOHIDReportType for the report                             reportID,           // CFIndex for the report ID                             report,             // address of report buffer                             &reportSize,        // address of length of the report                             tCFTimeInterval,    // timeout duration                             Handle_IOHIDDeviceGetReportCallback,  // the callback routine                             context ); // context passed to callback
```

For both of these functions the first parameter is a HID device reference. The second is a IOHIDReportType for the report; the third parameter is the report ID; the fourth parameter is the address of the report buffer and the fifth parameter on input points to the size of the report being requested; After completion it's the size of the returned report. For the asynchronous version the sixth parameter is a timeout; the seventh parameter is the callback routine and the last parameter is the context to pass to the callback routine:

__Listing 27__  HID device get report callback routine

```c
static void Handle_IOHIDDeviceGetReportCallback(                  void *          inContext,          // context from IOHIDDeviceGetReportWithCallback                 IOReturn        inResult,           // completion result for the get report operation                 void *          inSender,           // IOHIDDeviceRef of the device this report is from                 IOHIDReportType inIOHIDReportType,  // the report type                 uint32_t        inReportID,         // the report ID                 uint8_t*        inReport,           // the address of the report                 CFIndex         inReportLength ) // the length of the report {     printf( "%s( context: %p, result: %p, sender: %p, "  \             "type: %d, id: %d, report: %p, length: %p ).\n",          __PRETTY_FUNCTION__, inContext, ( void * ) inResult, inSender,          inIOHIDReportType, inReportID, inReport, inReportLength ); }   // Handle_IOHIDDeviceGetReportCallback
```

To obtain the HID elements associated with a specific device use the IOHIDDeviceCopyMatchingElements function:

```
// return the HID elements that match the criteria contained in the matching dictionary CFArrayRef IOHIDDeviceCopyMatchingElements(                  IOHIDDeviceRef  inIOHIDDeviceRef,       // IOHIDDeviceRef for the HID device                 CFDictionaryRef inMatchingCFDictRef,    // the matching dictionary                 IOOptionBits    inOptions ); // Option bits
```

The first parameter is the HID Manager reference; the second parameter is a matching dictionary ( which may be NULL to return all elements ) and the third parameter are any option bits ( currently unused, pass kIOHIDOptionsTypeNone ). This API returns a CFArrayRef of IOHIDElementRefs. Developers may then use CFArrayGetValueAtIndex to retrieve a specific IOHIDElementRef, CFArrayGetValues to retrieve all IOHIDElementRefs or CFSetApplyFunction to iterate all IOHIDElementRefs from this array.

The matching keys for HID elements are prefixed by kIOHIDElement and declared in <IOKit/hid/IOHIDKeys.h> ( See Listing 30 )

__Listing 28__  IOHIDDeviceCopyMatchingElements examples

```
// to return all elements for a device CFArrayRef elementCFArrayRef = IOHIDDeviceCopyMatchingElements( deviceRef, NULL, kIOHIDOptionsTypeNone );  // to return all elements with usage page keyboard  // create a dictionary to add element properties to CFMutableDictionaryRef tCFDictRef = CFDictionaryCreateMutable(      kCFAllocatorDefault, 0, &kCFTypeDictionaryKeyCallBacks, &kCFTypeDictionaryValueCallBacks ); if ( tCFDictRef ) {     // Add key for element usage page to matching dictionary     int usagePage = kHIDUsage_GD_Keyboard;     CFNumberRef pageCFNumberRef = CFNumberCreate( kCFAllocatorDefault, kCFNumberIntType, &usagePage );     if ( pageCFNumberRef ) {         CFDictionarySetValue( tCFDictRef, CFSTR( kIOHIDElementUsagePageKey ), pageCFNumberRef );         CFRelease( pageCFNumberRef );     } else {         fprintf( stderr, "%s: CFNumberCreate( usage page ) failed.", __PRETTY_FUNCTION__ );     } } else {     fprintf( stderr, "%s: CFDictionaryCreateMutable failed.", __PRETTY_FUNCTION__ ); }  if ( tCFDictRef ) {     CFArrayRef elementCFArrayRef = IOHIDDeviceCopyMatchingElements(          deviceRef, tCFDictRef, kIOHIDOptionsTypeNone );     CFRelease( tCFDictRef ); }
```

[Back to Top](#)

## HID Element Functions

A CFTypeRef can be verified to be a HID element reference by comparing its Core Foundation type against IOHIDElementGetTypeID:

__Listing 29__  Validating a HID element reference

```
 if ( CFGetTypeID( tCFTypeRef ) == IOHIDElementGetTypeID( ) ) {         // this is a valid HID element reference     }
```

Once a valid HID element reference is available the IOHIDElementGetProperty function may be used to access its properties ( type, usage page & usage, etc. ) using the HID element keys defined in <IOKit/HID/IOHIDKeys.h>:

__Listing 30__  HID element keys

```
From <IOKit/hid/IOHIDKeys.h>:  #define kIOHIDElementCookieKey                      "ElementCookie" #define kIOHIDElementTypeKey                        "Type" #define kIOHIDElementCollectionTypeKey              "CollectionType" #define kIOHIDElementUsageKey                       "Usage" #define kIOHIDElementUsagePageKey                   "UsagePage" #define kIOHIDElementMinKey                         "Min" #define kIOHIDElementMaxKey                         "Max" #define kIOHIDElementScaledMinKey                   "ScaledMin" #define kIOHIDElementScaledMaxKey                   "ScaledMax" #define kIOHIDElementSizeKey                        "Size" #define kIOHIDElementReportSizeKey                  "ReportSize" #define kIOHIDElementReportCountKey                 "ReportCount" #define kIOHIDElementReportIDKey                    "ReportID" #define kIOHIDElementIsArrayKey                     "IsArray" #define kIOHIDElementIsRelativeKey                  "IsRelative" #define kIOHIDElementIsWrappingKey                  "IsWrapping" #define kIOHIDElementIsNonLinearKey                 "IsNonLinear" #define kIOHIDElementHasPreferredStateKey           "HasPreferredState" #define kIOHIDElementHasNullStateKey                "HasNullState" #define kIOHIDElementFlagsKey                       "Flags" #define kIOHIDElementUnitKey                        "Unit" #define kIOHIDElementUnitExponentKey                "UnitExponent" #define kIOHIDElementNameKey                        "Name" #define kIOHIDElementValueLocationKey               "ValueLocation" #define kIOHIDElementDuplicateIndexKey              "DuplicateIndex" #define kIOHIDElementParentCollectionKey            "ParentCollection" #define kIOHIDElementVendorSpecificKey              "VendorSpecific"  #define kIOHIDElementCalibrationMinKey              "CalibrationMin" #define kIOHIDElementCalibrationMaxKey              "CalibrationMax" #define kIOHIDElementCalibrationSaturationMinKey    "CalibrationSaturationMin" #define kIOHIDElementCalibrationSaturationMaxKey    "CalibrationSaturationMax" #define kIOHIDElementCalibrationDeadZoneMinKey      "CalibrationDeadZoneMin" #define kIOHIDElementCalibrationDeadZoneMaxKey      "CalibrationDeadZoneMax" #define kIOHIDElementCalibrationGranularityKey      "CalibrationGranularity"
```

__Note:__ Use the CFSTR( ) macro to pass these keys to the get/set property functions as CFStringRefs:

__Important:__ Convenience functions have been provided to allow developers to access many of these properties directly without having to use intermediary CFTypes ( See Listing 33 ). Due to an unintentional implementation detail ( bug ) these element properties may or may not be accessible via the IOHIDElement[Get/Set]Property APIs. Please use the convenience APIs to access these properties.

All the kIOHIDElementCalibration\*\*\*Key properties are accessible via the IOHIDElement[Get/Set]Property APIs.

__Listing 31__  Passing HID element keys to the Get/Set Property functions

```
IOHIDElementGetProperty( element, CFSTR( kIOHIDElementTypeKey ), &tCFNumberRef );
```

Here are two functions that can be used to get or set long properties:

__Listing 32__  Examples of how to get or set long HID element properties

```c
static Boolean IOHIDElement_GetLongProperty(      IOHIDElementRef inElementRef,   // the HID element      CFStringRef inKey,              // the kIOHIDElement key ( as a CFString )     long * outValue ) // address where to return the output value {     Boolean result = FALSE;      CFTypeRef tCFTypeRef = IOHIDElementGetProperty( inElementRef, inKey );     if ( tCFTypeRef ) {         // if this is a number         if ( CFNumberGetTypeID( ) == CFGetTypeID( tCFTypeRef ) ) {             // get its value             result = CFNumberGetValue( ( CFNumberRef ) tCFTypeRef, kCFNumberSInt32Type, outValue );         }     }     return result; }  static void IOHIDElement_SetLongProperty(      IOHIDElementRef inElementRef,   // the HID element      CFStringRef inKey,              // the kIOHIDElement key ( as a CFString )     long inValue ) // the long value to be set {     CFNumberRef tCFNumberRef = CFNumberCreate( kCFAllocatorDefault, kCFNumberSInt32Type, &inValue );     if ( tCFNumberRef ) {         IOHIDElementSetProperty( inElementRef, inKey, tCFNumberRef );         CFRelease( tCFNumberRef );     } }  // access the kIOHIDElementVendorSpecificKey if it exists: long longValue; if ( IOHIDElement_GetLongProperty( elementRef, CFSTR( kIOHIDElementVendorSpecificKey ), &longValue ) ) {     printf( "Element 0x%08lX has a vendor specific key of value 0x%08lX.\n", elementRef, longValue ); }
```

There are convenience functions to retrieve many of these element properties directly:

__Listing 33__  HID element property functions

```
// IOHIDElementCookie represent a unique identifier for a HID element within a HID device. IOHIDElementCookie cookie = IOHIDElementGetCookie( elementRef );  // return the collection type: //  kIOHIDElementTypeInput_Misc         = 1, //  kIOHIDElementTypeInput_Button       = 2, //  kIOHIDElementTypeInput_Axis         = 3, //  kIOHIDElementTypeInput_ScanCodes    = 4, //  kIOHIDElementTypeOutput             = 129, //  kIOHIDElementTypeFeature            = 257, //  kIOHIDElementTypeCollection         = 513 IOHIDElementType tType = IOHIDElementGetType( elementRef );  // If the HID element type is of type kIOHIDElementTypeCollection then  // the collection type is one of: //  kIOHIDElementCollectionTypePhysical         = 0x00, //  kIOHIDElementCollectionTypeApplication      = 0x01, //  kIOHIDElementCollectionTypeLogical          = 0x02, //  kIOHIDElementCollectionTypeReport           = 0x03, //  kIOHIDElementCollectionTypeNamedArray       = 0x04, //  kIOHIDElementCollectionTypeUsageSwitch      = 0x05, //  kIOHIDElementCollectionTypeUsageModifier    = 0x06 IOHIDElementCollectionType collectionType = IOHIDElementGetCollectionType( elementRef );  // usage and usage pages are defined on the USB website at: <http://www.usb.org> uint32_t page = IOHIDElementGetUsagePage( elementRef ); uint32_t usage = IOHIDElementGetUsage( elementRef );  // Boolean properties Boolean isVirtual = IOHIDElementIsVirtual( elementRef ); Boolean isRelative = IOHIDElementIsRelative( elementRef ); Boolean isWrapping = IOHIDElementIsWrapping( elementRef ); Boolean isArray = IOHIDElementIsArray( elementRef ); Boolean isNonLinear = IOHIDElementIsNonLinear( elementRef ); Boolean hasPreferred = IOHIDElementHasPreferredState( elementRef ); Boolean hasNullState = IOHIDElementHasNullState( elementRef );  // the HID element name CFStringRef name = IOHIDElementGetName( elementRef );  // element report information uint32_t reportID = IOHIDElementGetReportID( elementRef ); uint32_t reportSize = IOHIDElementGetReportSize( elementRef ); uint32_t reportCount = IOHIDElementGetReportCount( elementRef );  // element unit & exponent uint32_t unit = IOHIDElementGetUnit( elementRef ); uint32_t unitExp = IOHIDElementGetUnitExponent( elementRef );  // logical & physical minimums & maximums CFIndex logicalMin = IOHIDElementGetLogicalMin( elementRef ); CFIndex logicalMax = IOHIDElementGetLogicalMax( elementRef ); CFIndex physicalMin = IOHIDElementGetPhysicalMin( elementRef ); CFIndex physicalMax = IOHIDElementGetPhysicalMax( elementRef );
```

There are also functions to determine the device, parent and child of a specified HID element:

__Listing 34__  HID element hierarchy functions

```
// return the HID device that a element belongs to IOHIDDeviceRef deviceRef = IOHIDElementGetDevice( elementRef );  // return the collection element that a HID element belongs to ( if any ) IOHIDElementRef elementRef = IOHIDElementGetParent( elementRef );  // return the child elements of a collection element ( if any ) CFArrayRef tCFArrayRef = IOHIDElementGetChildren( elementRef );
```

[Back to Top](#)

## HID Queue Functions

While developers can use the IOHIDDeviceGetValue to get the most recent value of a HID element, for some elements this is not sufficient. If it is necessary to keep track of all value changes of a HID element, rather than just the most recent one, developers can create a queue and add the HID elements of interest to it. Then all value change events involving those elements will be captured by the HID queue ( up to the depth of the HID queue ).

HID queue references ( IOHIDQueueRefs ) are used to communicate with the HID queues. They are created by using the IOHIDQueueCreate function:

```
// Create HID queue reference IOHIDQueueRef IOHIDQueueCreate(                      CFAllocatorRef  inCFAllocatorRef,   // Allocator to be used during creation                     IOHIDDeviceRef  inIOHIDDeviceRef,   // the HID device to be associated with this queue                     CFIndex         inDepth,            // the maximum number of values to queue                     IOOptionBits    inOptions ) // options ( currently reserved )
```

The first parameter is a CFAllocator to be used when allocating the returned IOHIDQueueRef. The second parameter is the HID device to be associated with this queue. The third parameter is the maximum depth of the HID queue. The last parameter ( options ) is currently reserved for future use. Developers should pass kIOHIDOptionsTypeNone ( zero ) for this parameter.

There is no IOHIDQueueDestroy ( or release, free, etc. ); But since the HID queue reference is a Core Foundation object reference then CFRelease should be used to dispose of it.

A CFTypeRef can be verified to be a HID queue reference by comparing its Core Foundation type against IOHIDQueueGetTypeID:

__Listing 35__  Validating a HID queue reference

```
 if ( CFGetTypeID( tCFTypeRef ) == IOHIDQueueGetTypeID( ) ) {         // this is a valid HID queue reference!     }
```

Once a HID queue reference has been created, it has to be started before it can be used to access the HID devices associated with it.

```
void IOHIDQueueStart( IOHIDQueueRef inIOHIDQueueRef );
```

The corresponding function to stop a HID queue is:

```
void IOHIDQueueStop( IOHIDQueueRef inIOHIDQueueRef );
```

__Note:__ HID queues have to be stopped before HID elements can be added or removed. Also HID elements can only be added to the HID queue for their device. You can't use a single HID queue for multiple devices.

To determine the HID device associated with a specific HID queue use the IOHIDQueueGetDevice function:

```
IOHIDDeviceRef IOHIDQueueGetDevice( IOHIDQueueRef inIOHIDQueueRef );
```

There are accessor function to get and set the HID queue's depth:

```
CFIndex IOHIDQueueGetDepth( IOHIDQueueRef inIOHIDQueueRef ); void IOHIDQueueSetDepth( IOHIDQueueRef inIOHIDQueueRef, CFIndex inDepth );
```

HID elements can be added and removed by using these functions:

```
void IOHIDQueueAddElement( IOHIDQueueRef inIOHIDQueueRef, IOHIDElementRef inIOHIDElementRef ); void IOHIDQueueRemoveElement( IOHIDQueueRef inIOHIDQueueRef, IOHIDElementRef inIOHIDElementRef );
```

To determine if a HID element has been added to a HID queue use this function:

```
Boolean IOHIDQueueContainsElement( IOHIDQueueRef inIOHIDQueueRef, IOHIDElementRef inIOHIDElementRef );
```

Once a HID queue has been created, HID elements added and then started then HID values can be dequeued by using one of these functions:

```
IOHIDValueRef IOHIDQueueCopyNextValue( IOHIDQueueRef inIOHIDQueueRef ); IOHIDValueRef IOHIDQueueCopyNextValueWithTimeout( IOHIDQueueRef inIOHIDQueueRef, CFTimeInterval inTimeout );
```

__Note:__ The first function is synchronous and will block until there is a HID value available. While this may be desirable when called from a secondary thread blocking as the main thread should always be avoided. So on the main thread developers will most likely want to use the the second function with a zero timeout. This is essentially a method for polling the HID queue without blocking.

__Note:__ Because the HID value is a retained copy, it is up to the caller to release the HID value ( using CFRelease ).

__Note:__ HID values are documented in the "HID Value Functions" section.

To avoid polling the HID queue for HID value changes developers can instead register a callback routine:

```
void IOHIDQueueRegisterValueAvailableCallback(                                 IOHIDQueueRef inIOHIDQueueRef,   // reference to the HID queue                                 IOHIDCallback inCallback,        // address of the callback routine                                 void *        inContext ); // context passed to callback
```

__Note:__ The HID queue must be scheduled with a run loop for this callback routine to be dispatched.

The functions to schedule and unschedule a HID queue from a run loop are:

```
// Schedule a HID queue with a runloop void IOHIDQueueScheduleWithRunLoop( IOHIDQueueRef       inIOHIDQueueRef,    // reference to the HID queue                                     CFRunLoopRef        inRunLoop,          // Run loop to be scheduled with                                     CFStringRef         inRunLoopMode ); // Run loop mode for scheduling  // Unschedule a HID queue from a runloop void IOHIDQueueUnscheduleFromRunLoop(                         IOHIDQueueRef   inIOHIDQueueRef,    // reference to the HID queue                         CFRunLoopRef    inRunLoop,          // Run loop to be unscheduling from                         CFStringRef     inRunLoopMode ); // Run loop mode for unscheduling
```

__Listing 36__  Scheduling a HID queue with a run loop

```
IOHIDQueueScheduleWithRunLoop( inIOHIDQueueRef, CFRunLoopGetCurrent( ), kCFRunLoopDefaultMode );
```

__Listing 37__  HID queue value available callback routine

```c
static void Handle_ValueAvailableCallback(                  void *   inContext, // context from IOHIDQueueRegisterValueAvailableCallback                 IOReturn inResult,  // the inResult                 void *   inSender,  // IOHIDQueueRef of the queue  ) {     printf( "%s( context: %p, result: %p, sender: %p ).\n",          __PRETTY_FUNCTION__, inContext, ( void * ) inResult, inSender );     do {         IOHIDValueRef valueRef = IOHIDQueueCopyNextValueWithTimeout( ( IOHIDQueueRef ) inSender, 0. );         if ( !valueRef ) break;         // process the HID value reference         .         .         .         CFRelease( valueRef ); // Don't forget to release our HID value reference     } while ( 1 ) ; }   // Handle_ValueAvailableCallback
```

__Note:__ This routine is not called every time a new value is added to a queue; It is only called when the HID queue transitions to non-empty. For this reason the HID queue should be emptied ( by calling IOHIDQueueCopyNextValueWithTimeout until it returns NULL ) before expecting this routine to be called again.

__Note:__ HID values are documented in the "HID Value Functions" section.

[Back to Top](#)

## HID Transaction Functions

HID transactions are an abstraction above using the IOHIDDeviceGetReport[WithCallback] ( See IOHIDDeviceGetReport[WithCallback] ) or IOHIDDeviceSetReport[WithCallback] ( See Listing 25 ) functions. Those functions require knowing the details of how HID device descriptors are used to define the reports sent to and received from HID devices. Instead, HID transactions allow you to assemble a transaction, add the relevant values, set default values and then commit the transaction in order to actually force a report to be sent across the USB bus.

To build a transaction you first have to create a HID transaction reference by using the IOHIDTransactionCreate function:

```
IOHIDTransactionRef IOHIDTransactionCreate(                          CFAllocatorRef  inCFAllocatorRef,   // Allocator to be used during creation                         IOHIDDeviceRef  inIOHIDDeviceRef,   // the HID device for this transaction                         IOHIDTransactionDirectionType   inDirection,  // The direction: in or out                         IOOptionBits    inOptions ); // options ( currently reserved )
```

The first parameter is a CFAllocator to be used when allocating the returned IOHIDTransactionRef. The second parameter is the HID device to be associated with this transaction. The third parameter is the direction for the transfer ( kIOHIDTransactionDirectionTypeInput or kIOHIDTransactionDirectionTypeOutput ) and the last parameter ( options ) is currently reserved for future use. Developers should pass kIOHIDOptionsTypeNone ( zero ) for this parameter.

__Note:__ HID Transaction references can be used to either send or receive multiple element values. As such the direction used should represent they type of HID elements that will be added to the transaction.

There is no IOHIDTransactionDestroy ( or release, free, etc. ); But since the HID transaction reference is a Core Foundation object reference then CFRelease should be used to dispose of it.

A CFTypeRef can be verified to be a HID transaction reference by comparing its Core Foundation type against IOHIDTransactionGetTypeID:

__Listing 38__  Validating a HID transaction reference

```
 if ( CFGetTypeID( tCFTypeRef ) == IOHIDTransactionGetTypeID( ) ) {         // this is a valid HID transaction reference!     }
```

There are convenience functions to get the HID device associated with a HID transaction and to get or set the direction for a HID transaction:

```
// Obtain the HID device associated with a transaction IOHIDDeviceRef IOHIDTransactionGetDevice(                                     IOHIDTransactionRef inIOHIDTransactionRef ); // HID transaction reference  // Obtain the direction of the transaction. IOHIDTransactionDirectionType IOHIDTransactionGetDirection(                                      IOHIDTransactionRef IOHIDTransactionRef ); // HID transaction reference  // Sets the direction of the transaction void IOHIDTransactionSetDirection( IOHIDTransactionRef IOHIDTransactionRef,     // HID transaction reference                                    IOHIDTransactionDirectionType direction ); // The direction: in or out
```

__Note:__ The IOHIDTransactionSetDirection function is useful for manipulating bi-direction ( feature ) elements such that you can set or get element values without having to create an additional transaction object.

Once a HID transaction has been created then the HID elements associated with it may be added by using the IOHIDTransactionAddElement function:

```
void IOHIDTransactionAddElement(              IOHIDTransactionRef inIOHIDTransactionRef,  // HID transaction reference             IOHIDElementRef     inIOHIDElementRef ); // the HID element to associate with this transaction
```

__Important:__ To minimize device traffic only add HID elements that share a common report type and id.

HID Elements may be removed from a HID transaction by using the IOHIDTransactionRemoveElement function:

```
void IOHIDTransactionRemoveElement(              IOHIDTransactionRef inIOHIDTransactionRef,  // HID transaction reference             IOHIDElementRef     inIOHIDElementRef ); // the HID element to associate with this transaction
```

To determine if a HID element is currently associated with a HID transaction the IOHIDTransactionContainsElement function may be used:

```
// Queries the transaction to determine if elemement has been added. Boolean IOHIDTransactionContainsElement(                     IOHIDTransactionRef inIOHIDTransactionRef, // HID transaction reference                     IOHIDElementRef     inIOHIDElementRef ); // the HID element to test for
```

To set the HID values associated with the HID elements in a HID transaction use the IOHIDTransactionSetValue functions:

```
void IOHIDTransactionSetValue( IOHIDTransactionRef  inIOHIDTransactionRef,  // HID transaction reference                                 IOHIDElementRef     inIOHIDElementRef,      // the HID element                                  IOHIDValueRef       inIOHIDValueRef,        // the HID element value                                 IOOptionBits        inOptions ); // options
```

The HID value set is pended until the transaction is committed and is only used if the transaction direction is kIOHIDTransactionDirectionTypeOutput. Use the kIOHIDTransactionOptionDefaultOutputValue option to set default element values.

To retrieve the HID values associated with the HID elements in a HID transaction developers may use the IOHIDTransactionGetValue function:

```
// Obtains the HID value for a transaction element. IOHIDValueRef IOHIDTransactionGetValue(                                  IOHIDTransactionRef inIOHIDTransactionRef,  // HID transaction reference                                 IOHIDElementRef     inIOHIDElementRef,      // the HID element                                  IOOptionBits        inOptions ); // options
```

If the HID transaction direction is kIOHIDTransactionDirectionTypeInput the HID value represents what was obtained from the HID device from the HID transaction. Otherwise, if the transaction direction is kIOHIDTransactionDirectionTypeOutput the HID value represents the pending value to be sent to the HID device. Use the kIOHIDTransactionOptionDefaultOutputValue option to get the default HID value associated with the HID elements of a HID transaction.

The values for HID elements associated with a HID transaction can be reset to their default values by using the IOHIDTransactionClear function:

```
// Clears element transaction values. void IOHIDTransactionClear( IOHIDTransactionRef inIOHIDTransactionRef ); // HID transaction reference
```

Once all the appropriate HID elements have been added to a HID transaction ( and values set for output transactions ) then in order to cause the actual bus transaction to occur they should be committed by using one of the two following functions:

```
// Synchronously commits element transaction to the HID device. IOReturn IOHIDTransactionCommit( IOHIDTransactionRef inIOHIDTransactionRef ); // HID transaction reference  // Asynchronously commits element transaction to the HID device. IOReturn IOHIDTransactionCommitWithCallback(                          IOHIDTransactionRef inIOHIDTransactionRef,  // HID transaction reference                         CFTimeInterval      inTimeout,              // timeout duration                         IOHIDCallback       inCallback,             // address of the callback routine                         void *              inContext ); // Pointer to be passed to the callback
```

For both functions the first parameter is the HID transaction reference to be committed. For the asynchronous function the second parameter is a timeout; the third parameter is the callback routine ( Pass NULL for synchronous behavior w/timeout ) and the last parameter is the context to pass to the callback routine.

__Note:__ In regards to kIOHIDTransactionDirectionTypeOutput direction, default element values will be used if element values are not set. If neither are set, that element will be omitted from the commit. After a transaction is committed, transaction element values will be cleared and default values preserved.

__Note:__ It is possible for elements from different reports to be present in a given transaction causing a commit to transcend multiple reports. Keep this in mind when setting a appropriate timeout.

__Note:__ The HID transaction must be scheduled with a run loop In order for the callback routine to be dispatched.

The functions to schedule and unschedule a HID transaction from a run loop are:

```
// Schedule a HID transaction with a runloop void IOHIDTransactionScheduleWithRunLoop(          IOHIDTransactionRef inIOHIDTransactionRef,  // reference to the HID transaction         CFRunLoopRef        inRunLoop,              // Run loop to be scheduled with         CFStringRef         inRunLoopMode ); // Run loop mode for scheduling  // Unschedule a HID transaction from a runloop void IOHIDTransactionUnscheduleFromRunLoop(          IOHIDTransactionRef inIOHIDTransactionRef,  // reference to the HID transaction         CFRunLoopRef        inRunLoop,              // Run loop to be unscheduling from         CFStringRef         inRunLoopMode ); // Run loop mode for unscheduling
```

__Listing 39__  Scheduling a HID transaction with a run loop

```
IOHIDTransactionScheduleWithRunLoop( inIOHIDTransactionRef, CFRunLoopGetCurrent( ), kCFRunLoopDefaultMode );
```

[Back to Top](#)

## HID Value Functions

HID value references are used by the HID Manager and HID device input value callbacks, the HID device get and set value functions and callbacks and the HID queue copy value [with timeout] functions. Three functions are available to be used to create HID value references:

```
IOHIDValueRef IOHIDValueCreateWithIntegerValue(              CFAllocatorRef  inCFAllocatorRef,   // Allocator to be used during creation             IOHIDElementRef inIOHIDElementRef,  // the HID element to be associated with this value             uint64_t        inTimeStamp,        // OS AbsoluteTime             CFIndex         inValue ); // the integer ( 32-bit ) value used to create this HID value  IOHIDValueRef IOHIDValueCreateWithBytes(              CFAllocatorRef  inCFAllocatorRef,   // Allocator to be used during creation             IOHIDElementRef inIOHIDElementRef,  // the HID element to be associated with this value             uint64_t        inTimeStamp,        // OS AbsoluteTime             const uint8_t * inBytes,            // a pointer to the data used to create this HID value             CFIndex         inLength ); // the length of the data used to create this HID value  IOHIDValueRef IOHIDValueCreateWithBytesNoCopy(              CFAllocatorRef  inCFAllocatorRef,   // Allocator to be used during creation             IOHIDElementRef inIOHIDElementRef,  // the HID element to be associated with this value             uint64_t        inTimeStamp,        // OS AbsoluteTime             const uint8_t * inBytes,            // a pointer to the data used to create this HID value             CFIndex         inLength ); // the length of the data used to create this HID value
```

For all three of these functions the first parameter is a CFAllocator to be used when allocating the returned IOHIDValueRef. The second parameter is the HID element to be associated with this value and the third parameter is a timestamp. For the IOHIDValueCreateWithIntegerValue function the last parameter is a CFIndex value. For the last two functions the fourth parameter is a pointer to the data and the last parameter is the length of the data.

__Note:__ For all three of these functions the timeStamp should represent an OS AbsoluteTime, not a CFAbsoluteTime. ( See <mach/mach_time.h> )

__Note:__ For the IOHIDValueCreateWithBytesNoCopy function the data is expected to exist until the HID value reference is released. Any attempt to access the data after it has been released may result in a crash.

A CFTypeRef can be verified to be a HID value reference by comparing its Core Foundation type against IOHIDValueGetTypeID:

__Listing 40__  Validating a HID value reference

```
 if ( CFGetTypeID( tCFTypeRef ) == IOHIDValueGetTypeID( ) ) {         // this is a valid HID value reference!     }
```

Convenience functions are provided to access the HID element, time stamp and integer value for HID values:

```
// Returns the HID element value associated with this HID value reference. IOHIDElementRef IOHIDValueGetElement( IOHIDValueRef inIOHIDValueRef );  // Returns the timestamp value associated with this HID value reference. uint64_t IOHIDValueGetTimeStamp( IOHIDValueRef inIOHIDValueRef );  // Returns an integer representation for this HID value reference. CFIndex IOHIDValueGetIntegerValue( IOHIDValueRef inIOHIDValueRef );
```

Additional functions are provided to access the data associated with a HID value and its length:

```
// Returns the size, in bytes, of the data associated with this HID value reference. CFIndex IOHIDValueGetLength( IOHIDValueRef inIOHIDValueRef );  // Returns a byte pointer to the data associated with this HID value reference. const uint8_t * IOHIDValueGetBytePtr( IOHIDValueRef inIOHIDValueRef )
```

One additional function exists to return a scaled representation of a HID value:

```
// return the scaled value of a HID value reference double_t IOHIDValueGetScaledValue( IOHIDValueRef inIOHIDValueRef, IOHIDValueScaleType inType );
```

There are currently two types of scaling that can be applied:

- kIOHIDValueScaleTypePhysical: Scales values using the physical bounds of the HID element.
- kIOHIDValueScaleTypeCalibrated: Scales values using the calibration properties of the HID element.

__Note:__ Currently there are no calibration properties associated with HID elements by default. Developers are expected to set the appropriate calibration properties for all elements that they want to scale using the IOHIDValueGetScaledValue function with the kIOHIDValueScaleTypeCalibrated scale type.

The first two HID element calibration properties define the desired range of the returned scaled value:

```
kIOHIDElementCalibrationMinKey - The minimum bounds for a calibrated value ( default = -1. ) kIOHIDElementCalibrationMaxKey - The maximum bounds for a calibrated value ( default = +1. )
```

For example, where the logical min/max values of a HID element may be 0 and 255 the developer may want the scaled value to be returned between the values of +/- 32.0 in which case these properties should be set to -32.0 and +32.0 respectively.

The next two HID element calibration properties define the range of expected values:

```
kIOHIDElementCalibrationSaturationMinKey - The minimum value to be used when calibrating a HID value kIOHIDElementCalibrationSaturationMaxKey - The maximum value to be used when calibrating a HID value
```

Some HID devices may have elements that aren't able to return the full range of values defined by their logical min/max value limits. For example, where the logical values for an element might be defined as ranging from 0 to 255 the actual device may actually only be able to return values in the range of 5 to 250. This may be caused by digitization errors or mechanical limits on an encoder, etc. If these calibration properties are set then logical values within this range will be scaled out to the full logical range for the HID device. For this example these two values would be set to 5 and 250 respectively.

The next two HID element calibration properties define the range of a dead zone ( if it exists ):

```
kIOHIDElementCalibrationDeadZoneMinKey - The minimum bounds near the midpoint where values are ignored.  kIOHIDElementCalibrationDeadZoneMaxKey - The maximum bounds near the midpoint where values are ignored.
```

Some HID devices ( such as joysticks ) have elements that have a mechanical return-to-center feature. Because of mechanical slop or drift or digitization noise these elements don't always return the exact same values when the HID element is returned to the center position. For example, an element with a logical range of 0 to 255 might return center values ranging from anywhere between 124 and 130. The dead zone properties allow developers to define a range of values that will be ignored and returned as the center scaled value instead. If these dead zone properties are set ( to 124 and 130 in this case ) then any value between these two numbers will be returned as the center value ( 127 in this case ).

The last HID element calibration property defines a granularity:

```
kIOHIDElementCalibrationGranularityKey - The scale or level of detail returned in a calibrated element value
```

For example, if the granularity property is set to 0.1, the returned values after calibration are exact multiples of 0.1: { 0.0, 0.1, 0.2, 0.3, 0.4, etc. }.

__Listing 41__  Setting HID element calibration properties

```c
static void IOHIDElement_SetDoubleProperty(                                 IOHIDElementRef inElementRef,   // the HID element                                  CFStringRef     inKey,          // the kIOHIDElement key ( as a CFString )                                 double          inValue ) // the double value to be set {     CFNumberRef tCFNumberRef = CFNumberCreate( kCFAllocatorDefault, kCFNumberDoubleType, &inValue );     if ( tCFNumberRef ) {         IOHIDElementSetProperty( inElementRef, inKey, tCFNumberRef );         CFRelease( tCFNumberRef );     } }  // These define the range of the returned scaled values IOHIDElement_SetDoubleProperty( elementRef, CFSTR( kIOHIDElementCalibrationMinKey ), -32. ); IOHIDElement_SetDoubleProperty( elementRef, CFSTR( kIOHIDElementCalibrationMaxKey ), +32. );  // these define the range of values expected from the device ( logical values ) IOHIDElement_SetDoubleProperty( elementRef, CFSTR( kIOHIDElementCalibrationSaturationMinKey ), 5. ); IOHIDElement_SetDoubleProperty( elementRef, CFSTR( kIOHIDElementCalibrationSaturationMaxKey ), 250. );  // these define the range of the dead zone ( logical values ) IOHIDElement_SetDoubleProperty( elementRef, CFSTR( kIOHIDElementCalibrationDeadZoneMinKey ), 124. ); IOHIDElement_SetDoubleProperty( elementRef, CFSTR( kIOHIDElementCalibrationDeadZoneMaxKey ), 130. );  // this defines the granularity of the returned scaled values IOHIDElement_SetDoubleProperty( elementRef, CFSTR( kIOHIDElementCalibrationGranularityKey ), 0.1 );
```

__Listing 42__  Pseudo code for the IOHIDValueGetScaledValue function

```
// first a convenience function to access HID element properties stored as doubles: static Boolean IOHIDElement_GetDoubleProperty(      IOHIDElementRef inElementRef,   // the HID element     CFStringRef inKey,              // the kIOHIDElement key ( as a CFString )     double * outValue ) // address where to return the output value {     Boolean result = FALSE;      CFTypeRef tCFTypeRef = IOHIDElementGetProperty( inElementRef, inKey );     if ( tCFTypeRef ) {         // if this is a number         if ( CFNumberGetTypeID( ) == CFGetTypeID( tCFTypeRef ) ) {             // get its value             result = CFNumberGetValue( ( CFNumberRef ) tCFTypeRef, kCFNumberDoubleType, outValue );         }     }     return result; }  double_t IOHIDValueGetScaledValue( IOHIDValueRef inValue, IOHIDValueScaleType inType ) {     IOHIDElementRef element = IOHIDValueGetElement( inValue );      double_t logicalValue = IOHIDValueGetIntegerValue( inValue );      double_t logicalMin = IOHIDElementGetLogicalMin( element );     double_t logicalMax = IOHIDElementGetLogicalMax( element );      double_t scaledMin = 0;     double_t scaledMax = 0;      double_t granularity = 0.;      double_t returnValue = 0.;      switch ( inType ) {         case kIOHIDValueScaleTypeCalibrated: {              double_t calibrateMin = 0.;             ( void ) IOHIDElement_GetDoubleProperty( element,                          CFSTR( kIOHIDElementCalibrationMinKey ), &calibrateMin );             double_t calibrateMax = 0.;             ( void ) IOHIDElement_GetDoubleProperty( element,                          CFSTR( kIOHIDElementCalibrationMaxKey ), &calibrateMax );              // if there are calibration min/max values...             if ( calibrateMin != calibrateMax ) {                 // ...use them...                 scaledMin = calibrateMin;                 scaledMax = calibrateMax;             } else {                 // ...otherwise use +/- 1.0                 scaledMin = -1.;                 scaledMax = +1.;             }              double_t saturationMin = 0.;             ( void ) IOHIDElement_GetDoubleProperty( element,                          CFSTR( kIOHIDElementCalibrationSaturationMinKey ), &saturationMin );             double_t saturationMax = 0.;             ( void ) IOHIDElement_GetDoubleProperty( element,                          CFSTR( kIOHIDElementCalibrationSaturationMaxKey ), &saturationMax );              // if there are saturation min/max values...             if ( saturationMin != saturationMax ) {                 // .. and the logical value is less than the minimum saturated value...                 if ( logicalValue <= saturationMin ) {                     // ...then return the minimum scaled value                     return scaledMin;                 } else                 // otherwise if the logical value is greater than the maximum saturated value...                 if ( logicalValue >= saturationMax ) {                     // ...return the maximum scaled value.                     return scaledMax;                 } else                 // otherwise use the min/max saturated values for the logical min/max                 {                     logicalMin = saturationMin;                     logicalMax = saturationMax;                 }             }              double_t deadzoneMin = 0.;             ( void ) IOHIDElement_GetDoubleProperty( element,                          CFSTR( kIOHIDElementCalibrationDeadZoneMinKey ), &deadzoneMin );             double_t deadzoneMax = 0.;             ( void ) IOHIDElement_GetDoubleProperty( element,                          CFSTR( kIOHIDElementCalibrationDeadZoneMaxKey ), &deadzoneMax );              // if there are deadzone min/max values...             if ( deadzoneMin != deadzoneMax ) {                     double_t scaledMid = ( scaledMin + scaledMax ) / 2.;                  // if the logical value is less than the deadzone min...                 if ( logicalValue < deadzoneMin ) {                     // ...then use the deadzone min as our logical max...                     logicalMax = deadzoneMin;                     // ...and the middle of our scaled range as our scaled max.                     scaledMax = scaledMid;                 } // otherwise if the logical value is greater than the deadzone max...                 else if ( logicalValue > deadzoneMax ) {                     // ...then use the deadzone max as our logical min...                     logicalMin = deadzoneMax;                     // ...and the middle of our scaled range as our scaled min.                     scaledMin = scaledMid;                 } else {                     // otherwise return the middle of our scaled range                     return scaledMid;                 }             }              ( void ) IOHIDElement_GetDoubleProperty( element,                          CFSTR( kIOHIDElementCalibrationGranularityKey ), &granularity );             break;         }         case kIOHIDValueScaleTypePhysical: {             scaledMin = IOHIDElementGetPhysicalMin( element );             scaledMax = IOHIDElementGetPhysicalMax( element );             break;         }         default: {             return returnValue; // should be 0.0         }     }      double_t logicalRange = logicalMax - logicalMin;     double_t scaledRange = scaledMax - scaledMin;      returnValue = ( ( logicalValue - logicalMin ) * scaledRange / logicalRange ) + scaledMin;      if ( granularity ) {         returnValue = round( returnValue / granularity ) * granularity;     }     return returnValue; }
```

[Back to Top](#)

## References

### Sample code:

- _[HID Config Save](../samplecode/HID%20Config%20Save/HID%20Config%20Save.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydanbugi)_
- _[HID Explorer](../samplecode/HID%20Explorer/HID%20Explorer.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydanbugm)_
- _[HID Manager Basics](../samplecode/HID%20Manager%20Basics/HID%20Manager%20Basics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydanbugq)_
[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2009-05-04 | Added documentation for the IOHID[Manager/Device]SetInputValueMatching[Multiple] API's. |
| 2008-01-23 | Fixed typo's, indentation and some (miss)parameterization. Run loop code now Carbon/Cocoa agnostic. |
| 2007-12-18 | New document that mac OS X version 10.5 introduces new APIs for the HID Manager. |

