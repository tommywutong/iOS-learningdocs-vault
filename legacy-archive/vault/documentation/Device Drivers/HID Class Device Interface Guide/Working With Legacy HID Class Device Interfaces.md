---
title: HID Class Device Interface Guide
apple_id: TP40000970
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: IOKit
published: '2009-10-19'
source_url: https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/HID/workingwith/workingwith.html
archived_at: '2026-07-15T07:31:12.737698Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [HID Class Device Interface Guide](Introduction%20to%20Working%20With%20HID%20Class%20Device%20Interfaces.md)


[Next](Complete%20Code%20Samples.md)[Previous](Legacy%20HID%20Access%20Overview.md)

# Working With Legacy HID Class Device Interfaces

This chapter provides step-by-step instructions, including listings of sample code, for accessing a HID class device on older versions of OS X. If you are developing new code for OS X v10.5 or later, you should use the APIs described in [Accessing a HID Device](Accessing%20a%20HID%20Device.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnzqfvbuqmrrgqwvgvzs)..

These examples assume that you have already obtained an iterator for a list of devices matching certain properties (for example, by using the `MyFindHIDDevices` function, [Listing 3-3](Legacy%20HID%20Access%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnzqfvbuqmrrgewueqkcinducscj)).

Now that you have a device iterator, you can use it to examine each device and create a device interface for it. The functions in this chapter demonstrate this process by first displaying the properties and then creating and testing a device interface for each device in turn.

This chapter contains the following sections:

1. [Printing the Properties of a HID Class Device](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydcmbvfvbugscdindeosa)
2. [Creating a HID Class Device Interface](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydcmbvfvbugschifbeisa)
3. [Obtaining HID Cookies](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydcmbvfvbecqshjbduqsa)
4. [Performing Operations on a HID Class Device](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydcmbvfvbugscki5ceesa)
5. [Using Queue Callbacks](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydcmbvfvbecqsiijcuesq)

For code to help you locate HID class devices, see [Legacy HID Access Overview](Legacy%20HID%20Access%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnzqfvbuqmrrgewugskiizeucske).

Since the properties of a HID class device often contain nested element dictionaries, the functions that access the elements must do so in a recursive manner. In the sample code, the `MyShowHIDProperties` function uses CFShow to print a dictionary.

__Listing 4-1__  A function that shows all properties for a HID class device

```
static void MyShowHIDProperties(io_registry_entry_t hidDevice)
{
        kern_return_t                                   result;
        CFMutableDictionaryRef                          properties = 0;
        char                                            path[512];

        result = IORegistryEntryGetPath(hidDevice, kIOServicePlane, path);
        if (result == KERN_SUCCESS)
                printf("[ %s ]", path);

        //Create a CF dictionary representation of the I/O
        //Registry entry's properties
        result = IORegistryEntryCreateCFProperties(hidDevice, &properties,
                kCFAllocatorDefault, kNilOptions);
        if ((result == KERN_SUCCESS) && properties)
        {
                CFShow(properties);
                /* Some common properties of interest include:
                    kIOHIDTransportKey, kIOHIDVendorIDKey,
                    kIOHIDProductIDKey, kIOHIDVersionNumberKey,
                    kIOHIDManufacturerKey, kIOHIDProductKey,
                    kIOHIDSerialNumberKey, kIOHIDLocationIDKey,
                    kIOHIDPrimaryUsageKey, kIOHIDPrimaryUsagePageKey,
                    and kIOHIDElementKey.
                */

                //Release the properties dictionary
                CFRelease(properties);
        }
        printf("\n\n");
}
```

`MyShowHIDProperties` takes the HID class device found in the I/O Registry and uses `IORegistryEntryCreateCFProperties` to create a CF dictionary representation of the device’s properties. It then calls CFShow to format the information and print it to the screen.

A device interface provides functions your application or other code running on OS X can use to access a device. The `MyCreateHIDDeviceInterface` function, shown in [Listing 4-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydcmbvfvbugscciffegra), creates and returns a HID class device interface based on a passed object from the I/O Registry. It also demonstrates how to obtain the class name of the passed object by calling the I/O Kit function `IOObjectGetClass`.

To create a HID class device interface, the `MyCreateHIDDeviceInterface` function performs the following steps:

1. It obtains an interface of type `IOCFPlugInInterface` for the HID class device represented by the passed `hidDevice` object.

   To obtain this interface, it calls the `IOCreatePlugInInterfaceForService` function, passing the value `kIOHIDDeviceUserClientTypeID` for the plug-in type parameter and the value `kIOCFPlugInInterfaceID` for the interface type parameter. `kIOHIDDeviceUserClientTypeID` is defined in `IOHIDLib.h` and `kIOCFPlugInInterfaceID` is defined in `IOCFPlugIn.h` (located in `IOKit.framework`).
2. It obtains a HID class device interface by calling the `QueryInterface` method of the `IOCFPlugInInterface` object. To specify a HID class device interface, it uses the following term:

   `CFUUIDGetUUIDBytes(`[kIOHIDDeviceInterfaceID](https://developer.apple.com/documentation/iokit/kiohiddeviceinterfaceid)`)`

   This term produces a UUID (universally unique identifier) for the device interface. UUIDs are described in the Core Foundation developer documentation, available in the [Reference Library > Core Foundation](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943-TP30000421) section of the developer documentation website. [kIOHIDDeviceInterfaceID](https://developer.apple.com/documentation/iokit/kiohiddeviceinterfaceid) is defined in `IOHIDLib.h`.
3. It releases the `IOCFPlugInInterface` object and returns the HID class device interface in the `hidDeviceInterface` parameter.

__Listing 4-2__  A function that creates and returns a HID class device interface based on a passed object from the I/O Registry

```swift
static void MyCreateHIDDeviceInterface(io_object_t hidDevice,
                            IOHIDDeviceInterface ***hidDeviceInterface)
{
    io_name_t               className;
    IOCFPlugInInterface     **plugInInterface = NULL;
    HRESULT                 plugInResult = S_OK;
    SInt32                  score = 0;
    IOReturn                ioReturnValue = kIOReturnSuccess;

    ioReturnValue = IOObjectGetClass(hidDevice, className);

    print_errmsg_if_io_err(ioReturnValue, "Failed to get class name.");

    printf("Found device type %s\n", className);

    ioReturnValue = IOCreatePlugInInterfaceForService(hidDevice,
                            kIOHIDDeviceUserClientTypeID,
                            kIOCFPlugInInterfaceID,
                            &plugInInterface,
                            &score);

    if (ioReturnValue == kIOReturnSuccess)
    {
        //Call a method of the intermediate plug-in to create the device
        //interface
        plugInResult = (*plugInInterface)->QueryInterface(plugInInterface,
                            CFUUIDGetUUIDBytes(kIOHIDDeviceInterfaceID),
                            (LPVOID *) hidDeviceInterface);
        print_errmsg_if_err(plugInResult != S_OK, "Couldn't create HID class device interface");

        (*plugInInterface)->Release(plugInInterface);
    }
}
```


The following function, `getHIDCookies` (shown in [Listing 4-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydcmbvfvbugschifbeqqq)), places certain cookies associated with the HID class device’s x axis, button 1, button 2, and button 3 into a data structure so the queue handling functions can add these elements to a queue.

__Listing 4-3__  A function that stores selected cookies in global variables for later use

```swift
typedef struct cookie_struct
{
        IOHIDElementCookie gXAxisCookie;
        IOHIDElementCookie gButton1Cookie;
        IOHIDElementCookie gButton2Cookie;
        IOHIDElementCookie gButton3Cookie;
} *cookie_struct_t;

cookie_struct_t getHIDCookies(IOHIDDeviceInterface122 **handle)
{
        cookie_struct_t cookies = memset(malloc(sizeof(*cookies)), 0,
            sizeof(*cookies));
        CFTypeRef                               object;
        long                                    number;
        IOHIDElementCookie                      cookie;
        long                                    usage;
        long                                    usagePage;
        CFArrayRef                              elements; //
        CFDictionaryRef                         element;
        IOReturn                                success;

        if (!handle || !(*handle)) return cookies;

        // Copy all elements, since we're grabbing most of the elements
        // for this device anyway, and thus, it's faster to iterate them
        // ourselves. When grabbing only one or two elements, a matching
        // dictionary should be passed in here instead of NULL.
        success = (*handle)->copyMatchingElements(handle, NULL, &elements);

        printf("LOOKING FOR ELEMENTS.\n");
        if (success == kIOReturnSuccess) {
                CFIndex i;
                printf("ITERATING...\n");
                for (i=0; i<CFArrayGetCount(elements); i++)
                {
                        element = CFArrayGetValueAtIndex(elements, i);
                        // printf("GOT ELEMENT.\n");

                        //Get cookie
                        object = (CFDictionaryGetValue(element,
                            CFSTR(kIOHIDElementCookieKey)));
                        if (object == 0 || CFGetTypeID(object) != CFNumberGetTypeID())
                            continue;
                        if(!CFNumberGetValue((CFNumberRef) object, kCFNumberLongType,
                            &number))
                                continue;
                        cookie = (IOHIDElementCookie) number;

                        //Get usage
                        object = CFDictionaryGetValue(element, CFSTR(kIOHIDElementUsageKey));
                        if (object == 0 || CFGetTypeID(object) != CFNumberGetTypeID())
                            continue;
                        if (!CFNumberGetValue((CFNumberRef) object, kCFNumberLongType,
                            &number))
                                continue;
                        usage = number;

                        //Get usage page
                        object = CFDictionaryGetValue(element,
                            CFSTR(kIOHIDElementUsagePageKey));
                        if (object == 0 || CFGetTypeID(object) != CFNumberGetTypeID())
                            continue;
                        if (!CFNumberGetValue((CFNumberRef) object, kCFNumberLongType,
                            &number))
                                continue;
                        usagePage = number;

                        //Check for x axis
                        if (usage == 0x30 && usagePage == 0x01)
                            cookies->gXAxisCookie = cookie;
                        //Check for buttons
                        else if (usage == 0x01 && usagePage == 0x09)
                            cookies->gButton1Cookie = cookie;
                        else if (usage == 0x02 && usagePage == 0x09)
                            cookies->gButton2Cookie = cookie;
                        else if (usage == 0x03 && usagePage == 0x09)
                            cookies->gButton3Cookie = cookie;
                }
                printf("DONE.\n");
        } else {
                printf("copyMatchingElements failed with error %d\n", success);
        }

        return cookies;
}
```


Once you have found a HID class device in the I/O Registry and created a device interface for it, you can perform operations such as:

- opening the device
- getting element values
- creating and manipulating queues
- closing the device

The sample code in this section performs these types of operations through the test function `MyTestHIDDeviceInterface`, shown in [Listing 4-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydcmbvfvbugschifeegrq). This function is passed a HID class device interface and it first calls the device interface function `open` to open the device. Next, it calls `MyTestQueues`, shown in [Listing 4-5](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydcmbvfvbugsccizeuora), to create and manipulate a queue. Then, it calls `MyTestHIDInterface` to get various element values and print them. Finally, it closes the device by calling the device interface function `close`.

__Listing 4-4__  A function that performs testing on a passed HID class device interface

```swift
static void MyTestHIDDeviceInterface(IOHIDDeviceInterface **hidDeviceInterface, cookie_struct_t cookies)
{
        IOReturn ioReturnValue = kIOReturnSuccess;

        //open the device
        ioReturnValue = (*hidDeviceInterface)->open(hidDeviceInterface, 0);
        printf("Open result = %d\n", ioReturnValue);

        //test queue interface
        MyTestQueues(hidDeviceInterface, cookies);

        //test the interface
        MyTestHIDInterface(hidDeviceInterface, cookies);

        //close the device
        if (ioReturnValue == KERN_SUCCESS)
                ioReturnValue = (*hidDeviceInterface)->close(hidDeviceInterface);

        //release the interface
        (*hidDeviceInterface)->Release(hidDeviceInterface);
}
```

The `MyTestQueues` function (shown in [Listing 4-5](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydcmbvfvbugsccizeuora)) first calls the HID device interface function `allocQueue` to allocate a queue. Next, it uses the queue handling functions `addElement`, `hasElement`, and `removeElement` to add elements to the queue, check to see if an element is in the queue, and remove an element, respectively. Finally, `MyTestQueues` simulates a game loop by calling the `start` queue function to start data delivery to the queue and then repeatedly calling the `getNextEvent` queue function to retrieve the values for elements in the queue. All queue handling functions for HID class devices are defined in `IOHIDLib.h`.

__Listing 4-5__  A function to test the HID class device interface queue handling functions

```swift
static void MyTestQueues(IOHIDDeviceInterface **hidDeviceInterface, cookie_struct_t cookies)
{
        HRESULT                                                 result;
        IOHIDQueueInterface **                                          queue;
        Boolean                                         hasElement;
        long                                            index;
        IOHIDEventStruct                                                event;

        queue = (*hidDeviceInterface)->allocQueue(hidDeviceInterface);

        if (queue)
        {
                printf("Queue allocated: %lx\n", (long) queue);
                //create the queue
                result = (*queue)->create(queue, 0, 8);
                    /*  depth (8): maximum number of elements in queue before oldest
                        elements in queue begin to be lost.
                     */
                printf("Queue create result: %lx\n", result);

                //add elements to the queue
                result = (*queue)->addElement(queue, cookies->gXAxisCookie, 0);
                printf("Queue added x axis result: %lx\n", result);
                result = (*queue)->addElement(queue, cookies->gButton1Cookie, 0);
                printf("Queue added button 1 result: %lx\n", result);
                result = (*queue)->addElement(queue, cookies->gButton2Cookie, 0);
                printf("Queue added button 2 result: %lx\n", result);
                result = (*queue)->addElement(queue, cookies->gButton3Cookie, 0);
                printf("Queue added button 3 result: %lx\n", result);


                //check to see if button 3 is in queue
                hasElement = (*queue)->hasElement(queue,cookies->gButton3Cookie);
                printf("Queue has button 3 result: %s\n", hasElement ? "true" :
                    "false");

                //remove button 3 from queue
                result = (*queue)->removeElement(queue, cookies->gButton3Cookie);
                printf("Queue remove button 3 result: %lx\n",result);

                //start data delivery to queue
                result = (*queue)->start(queue);
                printf("Queue start result: %lx\n", result);

                //check queue a few times to see accumulated events
                sleep(1);
                printf("Checking queue\n");
                for (index = 0; index < 10; index++)
                {
                        AbsoluteTime                            zeroTime = {0,0};

                        result = (*queue)->getNextEvent(queue, &event, zeroTime, 0);
                        if (result)
                                printf("Queue getNextEvent result: %lx\n", result);
                        else
                                printf("Queue: event:[%lx] %ld\n",
                                                                (unsigned long) event.elementCookie,
                                                                event.value);

                        sleep(1);
                }

                //stop data delivery to queue
                result = (*queue)->stop(queue);
                printf("Queue stop result: %lx\n", result);

                //dispose of queue
                result = (*queue)->dispose(queue);
                printf("Queue dispose result: %lx\n", result);

                //release the queue we allocated
                (*queue)->Release(queue);
        }
}
```

The `MyTestHIDInterface` function uses the passed-in HID device interface to call the device interface `getElement` function to get the element values associated with the cookies stored in the global variables `gXAxisCookie`, `gButton1Cookie`, `gButton2Cookie`, and `gButton3Cookie` by `getHIDCookies` (shown in [Listing 4-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydcmbvfvbugschifbeqqq)). The sample code simulates a game loop by repeatedly calling `getElementValue` in a `for` loop.

__Listing 4-6__  A function that uses HID class device interface functions to get and display selected element values over time

```swift
static void MyTestHIDInterface(IOHIDDeviceInterface ** hidDeviceInterface, cookie_struct_t cookies)
{
        HRESULT                                 result;
        IOHIDEventStruct                                        hidEvent;
        long                                    index;

        printf("X Axis (%lx), Button 1 (%lx), Button 2 (%lx), Button 3 ($lx)\n",
                        (long) cookies->gXAxisCookie, (long) cookies->gButton1Cookie,
                        (long) cookies->gButton2Cookie, (long) cookies->gButton3Cookie);

        for (index = 0; index < 10; index++)
        {
                long xAxis, button1, button2, button3;

                //Get x axis
                result = (*hidDeviceInterface)->getElementValue(hidDeviceInterface,
                    cookies->gXAxisCookie, &hidEvent);
                if (result)
                     printf("getElementValue error = %lx", result);
                xAxis = hidEvent.value;

                //Get button 1
                result = (*hidDeviceInterface)->getElementValue(hidDeviceInterface,
                    cookies->gButton1Cookie, &hidEvent);
                if (result)
                     printf("getElementValue error = %lx", result);
                button1 = hidEvent.value;

                //Get button 2
                result = (*hidDeviceInterface)->getElementValue(hidDeviceInterface,
                    cookies->gButton2Cookie, &hidEvent);
                if (result)
                     printf("getElementValue error = %lx", result);
                button2 = hidEvent.value;

                //Get button 3
                result = (*hidDeviceInterface)->getElementValue(hidDeviceInterface,
                    cookies->gButton3Cookie, &hidEvent);
                if (result)
                     printf("getElementValue error = %lx", result);
                button3 = hidEvent.value;

                //Print values
                printf("%ld %s%s%s\n", xAxis, button1 ? "button1 " : "",
                                button2 ? "button2 " : "", button3 ? "button3 " : "");

                sleep(1);
        }
}
```


There are two basic ways of using queues when interacting with HID devices: polling and callbacks. In [Listing 4-5](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydcmbvfvbugsccizeuora), queues are accessed in a polled fashion. The example project “hidexample” uses this mechanism.

For performance reasons (and for programming convenience), it often makes more sense to use queue callbacks. In this usage, a function in your program is called whenever the queue becomes non-empty.

The code snippet is relatively straightforward. Essentially, you allocate a private data structure that contains a reference to the queue, create an asynchronous event source for the queue, add a queue callback handler, and finally, add the newly-created queue event source to your run loop.

The queue callback is passed two `void *` parameters, `callbackRefcon` and `callbackTarget`, both of which can contain pointers to arbitrary data. With this design, the same callback function can operate on multiple queues, feeding data to multiple class instances, simply by passing different queue and class pointers to the `setEventCallout` function.

In [Listing 4-7](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydcmbvfvbecqscjbfegqi), the `callbackTarget` parameter will be passed `NULL`, and the `callbackRefcon` parameter will be passed a dynamically-allocated object containining the `hidQueueInterface` pointer (just for grins).

__Listing 4-7__  Adding a Queue Callback

```swift
bool addQueueCallbacks(IOHIDQueueInterface **hidQueueInterface)
{
    IOReturn ret;
    CFRunLoopSourceRef eventSource;
    /*  We could use any data structure here. This data structure
        will be passed to the callback, and should probably
        include some information about the queue, assuming your
        program deals with more than one. */
    IOHIDQueueInterface ***myPrivateData = malloc(sizeof(*myPrivateData));
    *myPrivateData = hidQueueInterface;

    // In the calling function, we did something like:
    // hidQueueInterface = (*hidDeviceInterface)->
    //      allocQueue(hidDeviceInterface);
    // (*hidQueueInterface)->create(hidQueueInterface, 0, 8);
    ret = (*hidQueueInterface)->
        createAsyncEventSource(hidQueueInterface,
        &eventSource);
    if ( ret != kIOReturnSuccess )
        return false;
    ret = (*hidQueueInterface)->
        setEventCallout(hidQueueInterface,
        QueueCallbackFunction, NULL, myPrivateData);
    if ( ret != kIOReturnSuccess )
        return false;
    CFRunLoopAddSource(CFRunLoopGetCurrent(), eventSource,
        kCFRunLoopDefaultMode);
    return true;
}
```

The final example in this section is taken from the “HidTestTool” example. This snippet shows how to handle a queue callback. This code is structurally somewhat different in that a data structure is passed as the `refcon` argument. This allows it to pass in both information about the queue and information about the elements supported by a given HID device.

__Listing 4-8__  A Basic Queue Callback Function

```swift
static void QueueCallbackFunction(
                            void *          target,
                            IOReturn            result,
                            void *          refcon,
                            void *          sender)
{
    HIDDataRef          hidDataRef      = (HIDDataRef)refcon;
    AbsoluteTime    zeroTime    = {0,0};
    CFNumberRef     number      = NULL;
    CFMutableDataRef    element     = NULL;
    HIDElementRef   tempHIDElement  = NULL;//(HIDElementRef)refcon;
    IOHIDEventStruct    event;
    bool                change;
    bool                stateChange = false;

    if ( !hidDataRef || ( sender != hidDataRef->hidQueueInterface))
        return;

    while (result == kIOReturnSuccess)
    {
        result = (*hidDataRef->hidQueueInterface)->getNextEvent(
                                        hidDataRef->hidQueueInterface,
                                        &event,
                                        zeroTime,
                                        0);

        if ( result != kIOReturnSuccess )
            continue;

        // Only intersted in 32 values right now
        if ((event.longValueSize != 0) && (event.longValue != NULL))
        {
            free(event.longValue);
            continue;
        }

        number = CFNumberCreate(kCFAllocatorDefault, kCFNumberIntType,
            &event.elementCookie);
        if ( !number )  continue;
        element = (CFMutableDataRef)CFDictionaryGetValue(hidDataRef->
            hidElementDictionary, number);
        CFRelease(number);

        if ( !element ||
            !(tempHIDElement = (HIDElement *)CFDataGetMutableBytePtr(element)))
            continue;

        change = (tempHIDElement->currentValue != event.value);
        tempHIDElement->currentValue = event.value;

    }

}
```

[Next](Complete%20Code%20Samples.md)[Previous](Legacy%20HID%20Access%20Overview.md)

