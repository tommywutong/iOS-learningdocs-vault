---
title: FireWire Device Interface Guide
apple_id: TP40000969
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: IOKit
published: '2007-02-08'
source_url: https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/WorkingWFireWireDI/FWDevInterfaces/FWChapter.html
archived_at: '2026-07-15T07:31:34.763740Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [FireWire Device Interface Guide](Introduction%20to%20FireWire%20Device%20Interface%20Guide.md)


[Next](FireWire%20Device%20Access%20in%20an%20Intel-Based%20Macintosh.md)[Previous](Accessing%20FireWire%20Devices%20From%20Applications.md)

# Using the FireWire Device Interface Libraries

This chapter uses sample code from the FireWire SDK to illustrate how to use the FireWire device interface libraries. (The latest version of the SDK is available for download at [http://developer.apple.com/hardwaredrivers/download](https://developer.apple.com/hardwaredrivers/download).) The first section, [Using the IOFireWireLib](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnrzfvbuqmrqgmwugq2ijbbeir2e), describes two sample projects. The first sets up isochronous communication with a device and the second sets up a pseudo-address space in the Macintosh to handle FireWire packets. The second section, [Using the IOFireWireSBP2Lib](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnrzfvbuqmrqgmwugq2ijjfeiqkf), presents a sample project that creates a user-space driver to access an SBP-2 device. Finally, [Using the IOFireWireAVCLib](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnrzfvbuqmrqgmwugq2iircuessi) describes a project that accesses an AV/C unit with the IOFireWireAVCLib interfaces.

The code samples in this chapter omit most of the steps required to create matching dictionaries, search the I/O Registry, and get device interfaces. For code samples that show how to perform these tasks, see [Accessing FireWire Devices From Applications](Accessing%20FireWire%20Devices%20From%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnrzfvbuqmrqgiwviucykjcummjqge) or the code projects in the FireWire SDK.

The IOFireWireLib provides the lowest level interfaces available to communicate directly with a FireWire device from an application. It also provides interfaces to set up isochronous communication with a FireWire device.

Isochronous communication takes place on channels that can each have at most one talker and any number of listeners. The IOFireWire family abstracts these concepts into channel objects and port objects. Channel objects correspond to FireWire bus channels and port objects are either remote or local and correspond to either talkers or listeners. Remote ports correspond to external devices and have methods you can override to support your device. The local port corresponds to the Macintosh and does not have methods you can override. You use these objects in your application to map out the flow of isochronous communication before any actual data transfer begins.

To manage the isochronous data your device sends and receives, you create a datastream control language (or DCL) program. The DCL program is a linked list of DCL commands that specify where to place each received packet and where to find the data to send. A DCL program can run both linearly, from beginning to end, and nonlinearly, by jumping from one command to another. You can even set up a DCL program to modify its jumps during execution, creating a dynamically changeable program. The IOFireWire family makes writing DCL programs easier by providing a function that allows you to create a pool of DCL command objects ready for use and functions that fill in DCL command objects with your parameters.

The IOFireWireLibIsochTest project creates a remote port and a local port, allocates an isochronous channel, sets up the remote port as a listener and the local port as the talker, and then starts the channel. The program includes a simple DCL program that manages the packets. IOFireWireLibIsochTest matches on the local node (the Macintosh itself) so you can run it even if no external FireWire devices are currently plugged in.

To begin with, the IOFireWireLibIsochTest project acquires a Mach port, creates a matching dictionary for the local node, and gets an IOFireWireDeviceInterface object for it. These steps closely follow those described in [Finding FireWire Devices](Accessing%20FireWire%20Devices%20From%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnrzfvbuqmrqgiwugq2iineuercc) so this section does not repeat them.

The code fragments and listings in this section use the variables in [Listing 3-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnrzfvbuqmrqgmwugq2ijjducrse).

__Listing 3-1__  Variable definitions for IOFireWireLibIsochTest

```
//global declarations
IOFireWireLibDCLCommandPoolRef  gCommandPool;
UInt8                           gBuf[1024];
UInt8                           gBuf2[1024];

//local declarations in the main function
IOReturn                        result;
IOFireWireLibNubRef             localNode;
IOFireWireLibLocalIsochPortRef  localIsochPort;
IOFireWireLibRemoteIsochPortRef remoteIsochPort;
IOFireWireLibIsochChannelRef    isochChannel;
```

To exclusively open the device (in this case, the Macintosh), IOFireWireLibIsochTest `main` function calls the IOFireWireLibDeviceInterface function `open`:

```swift
result = (*localNode)->Open( localNode );
```

Next, it creates a pool of DCL command structures. The function `CreateDCLCommandPool` calls the IOFireWireLibDeviceInterface function of the same name, creating a DCL command pool object and returning an interface to it that the program can use to build a DCL program. [Listing 3-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnrzfvbuqmrqgmwugq2iirfekssd) shows the function call followed by the function definition, excluding error checking.

__Listing 3-2__  Creating a DCL command pool

```swift
//Call to CreateDCLCommandPool from main.
result = CreateDCLCommandPool( localNode, &gCommandPool );
//...
//CreateDCLCommandPool function.
IOReturn CreateDCLCommandPool( IOFireWireLibNubRef inNub,
    IOFireWireLibDCLCommandPoolRef* outCommandPool ) {

    //Create a DCL command pool.
    *outCommandPool = (*inNub)->CreateDCLCommandPool( inNub, 0x1000,
        CFUUIDGetUUIDBytes( kIOFireWireDCLCommandPoolInterfaceID ) );
}
```

Before it can start the isochronous channel, the IOFireWireLibIsochTest `main` function first creates the remote and local port objects and an isochronous channel object. The IOFireWireLib contains interfaces for each of these objects that provide functions to manage them.

[Listing 3-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnrzfvbuqmrqgmwugq2ijbaucq2j) shows the `CreateRemoteIsochPort` function (along with its call from `main`) which includes a number of callback functions you can override to provide device-specific functions, such as how to start and stop the port and which channels your device supports.

__Listing 3-3__  Creating a remote isochronous port

```swift
//Call to CreateRemoteIsochPort from main.
result = CreateRemoteIsochPort( localNode, &remoteIsochPort );
//...
//CreateRemoteIsochPort function.
IOReturn CreateRemoteIsochPort( IOFireWireLibNubRef inNub,
    IOFireWireLibRemoteIsochPortRef* outPort ) {
    IOFireWireLibRemoteIsochPortRef port;

    //Call the IOFireWireDeviceInterface function CreateRemoteIsochPort to
    //create a remote port object and return an interface to it. The “false”
    //parameter indicates that this port will not be a talker.

    port = (*inNub)->CreateRemoteIsochPort( inNub, false, CFUUIDGetUUIDBytes
                                (kIOFireWireRemoteIsochPortInterfaceID ) );
    (*port)->SetGetSupportedHandler( port, &RemotePort_GetSupported );
    (*port)->SetAllocatePortHandler( port, &RemotePort_AllocatePort );
    (*port)->SetReleasePortHandler( port, &RemotePort_ReleasePort );
    (*port)->SetStartHandler( port, &RemotePort_Start );
    (*port)->SetStopHandler( port, &RemotePort_Stop );
    *outPort = port;
}
```

In IOFireWireLibIsochTest, the `RemotePort_GetSupported` function indicates that it supports all channels and the remaining callback functions simply print messages. You should add your own code to these callback functions to support your device.

To create the local isochronous port, the IOFireWireLibIsochTest `main` function calls the function `CreateLocalIsochPort`. This function uses the IOFireWireDeviceInterface function of the same name to create a local isochronous port object with a particular DCL program and return an interface to it. [Listing 3-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnrzfvbuqmrqgmwugq2iinfeiq2c) shows the `CreateLocalIsochPort` function, along with its call from `main`.

__Listing 3-4__  Creating a local isochronous port

```swift
//Call to CreateLocalIsochPort from main.
result = CreateLocalIsochPort( localNode, &localIsochPort );
//...
//CreateLocalIsochPort function.
IOReturn CreateLocalIsochPort( IOFireWireLibNubRef inNub,
    IOFireWireLibLocalIsochPortRef* outPort ) {

    //Set the pointer dclProgram to a simple DCL program created in
    //the IOFireWireLibIsochTest function WriteTalkingDCLProgram (not shown).
    DCLCommandStruct*   dclProgram = WriteTalkingDCLProgram();

    //Use the IOFireWireDeviceInterface function PrintDCLProgram
    //to print the contents of the DCL program.
    (*inNub)->PrintDCLProgram( inNub, dclProgram, 6 );

    //Create a local isochronous port object and return an interface
    //for it. The “true” parameter indicates that this port will be a talker.
    *outPort = (*inNub)->CreateLocalIsochPort( inNub, true, dclProgram, 0, 0,
        0, nil, 0, nil, 0, CFUUIDGetUUIDBytes(
        kIOFireWireLocalIsochPortInterfaceID ) );
    return *outPort;
}
```

Now the IOFireWireLibIsochTest `main` function uses channel interface functions to set up isochronous communication. First, it designates the remote port as a listener and the local port as the talker:

```swift
result = (*isochChannel)->AddListener( isochChannel,
    (IOFireWireLibIsochPortRef) remoteIsochPort );
//...
result = (*isochChannel)->SetTalker( isochChannel,
    (IOFireWireLibIsochPortRef) localIsochPort );
```

Then, it uses another channel interface function to allocate the channel:

```swift
result = (*isochChannel)->AllocateChannel( isochChannel );
```

The channel interface function `AllocateChannel` calls the `GetSupported` methods on all the ports to find out which channels they support, reconciles the answers, and requests a particular channel and bandwidth from the FireWire bus.

After the channel is allocated, the IOFireWireLibIsochTest `main` function calls the channel interface `Start` function which calls the `Start` functions on all the ports:

```swift
result = (*isochChannel)->Start( isochChannel );
```

To make sure the callbacks get called, the `main` function then calls an IOFireWireDeviceInterface function to add the isochronous callback dispatcher to the program’s run loop:

```swift
(*localNode)->AddIsochCallbackDispatcherToRunLoop( localNode,
    CFRunLoopGetCurrent() );
```

For the purposes of testing, the `main` function calls the Core Foundation function `CFRunLoopRunInMode` to run the run loop and trigger the callback functions for 15 seconds. After that time, the `main` function then calls the channel interface `Stop` function which calls the `_Stop` functions on all the ports:

```swift
result = (*isochChannel)->Stop( isochChannel );
```

Finally, the IOFireWireLibIsochTest `main` function releases the interfaces it acquired. It first releases the isochronous channel object with the channel interface function `ReleaseChannel` and then it uses the IOCFPlugInInterface function `Release` to release the interface itself:

```swift
result = (*isochChannel)->ReleaseChannel( isochChannel );
//...
(*isochChannel)->Release( isochChannel );
```

The `main` function similarly releases the local and remote port interfaces, then calls the IOFireWireDeviceInterface function `Close` on the local node before releasing its interface, and releases the original CFPlugInInterface:

```
IODestroyPlugInInterface( gCFPlugInInterface );
```


The IOFireWire family defines two types of address space on the Macintosh: Physical address space and pseudo-address space. The IOFireWireDeviceInterface provides IOFireWirePhysicalAddressSpace objects, which are allocated in a range of hardware-backed addresses and IOFireWirePseudoAddressSpace objects, which are allocated in a range of addresses outside the physical range and are accessible only through software.

As mentioned in [FireWire Overview](FireWire%20on%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnrzfvbuqmrqgewugq2ijjeuqssh), FireWire defines 64-bit addresses of which the lower 48 bits are for device-specific use. The physical address space range is the lower 32 bits of the device-specific range mapped onto the 32 -bit Macintosh RAM. Thus, in terms of FireWire addresses, an IOFireWirePhysicalAddressSpace object is an allocated subrange in the range $0000.00000000 to $0000.FFFFFFFF. An IOFireWirePseudoAddressSpace object is an allocated subrange of FireWire addresses of $1.00000000 and higher.

The FireWire controller chip can write directly to and read directly from a physical address space without any software intervention. For this reason, you can transfer large amounts of data to and from this address space efficiently. Because there is no software involvement in such a transfer, however, there is no indication of when the transfer is complete or if it failed. To handle this, you must also allocate a pseudo-address space to serve as a messaging area. Your remote device then transfers its data to a physical address space and sends a message of success or failure to a pseudo-address space that alerts your software.

The IOFireWirePacketQueueTest project uses functions of the IOFireWireDeviceInterface to create an IOFireWirePseudoAddressSpace interface object that represents a pseudo-address space on the local node. The project then uses functions of the IOFireWirePseudoAddressSpace interface to get the FireWire address of the address space and set up callback routines for writing and reading to the address space. It also sets up a callback routine for handling packets that must be dropped when the queue of packets coming into the pseudo-address space fills up too quickly.

The `main` function of the `IOFireWirePacketQueueTest.cpp` first calls the `GetIOFireWireDevices` function to put all IOFireWireLocalNode device objects into an array. Then, it uses standard Core Foundation and I/O Kit functions to get an IOFireWireDeviceInterface for the first object in the array (see [Getting FireWire Device Interfaces](Accessing%20FireWire%20Devices%20From%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnrzfvbuqmrqgiwugq2iivausrkf) for sample code illustrating this process). After using IOFireWireDeviceInterface functions to open the device and set up a callback dispatcher, the `main` function then creates a pseudo-address space object and gets an interface to it, as [Listing 3-5](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnrzfvbuqmrqgmwugq2iijceirsi) shows.

__Listing 3-5__  Getting an IOFireWirePseudoAddressSpaceInterface

```swift
Ptr                     gBuf = 0; //Buffer for backing store.
//...
IOFireWireLibDeviceRef  interface;
//...
IOFireWireLibPseudoAddressSpaceRef  addressSpace = 0;
IOFireWireLibPhysicalAddressSpaceRefphysAddressSpace = 0;

//Allocate backing store and put some text into gBuf for testing.
gBuf = (Ptr) new char[40960];
sprintf( gBuf, “Testing...” );

//Use IOFireWireDeviceInterface function CreatePseudoAddressSpace to
//create a pseudo-address space object and get an interface to it.
//In the call to CreatePseudoAddressSpace, 40960 is the size of the
//address space, addressSpace is the reference value passed to all
//callback functions, and 4096 is the size of the queue that
//receives packets from the bus.

addressSpace = (*interface)->CreatePseudoAddressSpace( interface,
    40960, (void*) addressSpace, 4096, gBuf, kFWAddressSpaceAutoCopyOnWrite,
    CFUUIDGetUUIDBytes( kIOFireWirePseudoAddressSpaceInterfaceID ) );
```

Next, the `main` function uses IOFireWirePseudoAddressSpaceInterface functions to set up callback handler routines for reading and writing to the pseudo-address space and handling skipped packets. When a `write` to the pseudo-address space occurs, the `PacketWriteHandler` routine prints out information about the pseudo-address space and the packets it received. Similarly, when a `read` occurs, the `PacketReadHandler` routine handles the `read` and then prints out information about the `read` request. The `SkippedPacketHandler` routine simply prints out the number of skipped packets. All three handler routines end with a call to the IOFireWirePseudoAddressSpaceInterface function `ClientCommandIsComplete`, which notifies the pseudo-address space that a packet notification handler has completed its work, as in this example from `SkippedPacketHandler`:

```swift
//In the following function call, commandID is the same ID that was
//passed to the packet notification handler and kIOReturnSuccess is
//the completion status of the packet handler.

(*addressSpace)->ClientCommandIsComplete( addressSpace,
    commandID, kIOReturnSuccess );
```

The `main` function then sets everything in motion by calling `CFRunLoopRun`. Finally, it releases all the interfaces it acquired and ends.

The SBP2SampleProject in the FireWire SDK adds another layer of complexity to the standard application-level access of a FireWire device. Instead of acquiring interfaces from the IOFireWireSBP2Lib and using them to communicate with a device, the SBP2SampleProject provides a user-space driver plug-in that exists between the application and the IOFireWireSBP2Lib. The application in the SBP2SampleProject creates a matching dictionary and gets an interface, but it is an interface to the user-space driver, not to the device object itself. The user-space driver then gets an interface from the IOFireWireSBP2Lib and uses it to access the in-kernel SBP-2 services. This design allows multiple applications to use the same user-space driver plug-in to access a device.

The SBP2SampleProject is a multi-threaded project. For an example of the same project in a single-threaded environment, see the SBP2SampleProject-SingleThread project.

The SBP2SampleProject driver abstracts device access into two logical layers. The lower layer is a transport layer that handles such tasks as SBP-2 ORB chaining and login maintenance. The upper layer is a protocol layer that receives commands from the application and creates and submits the appropriate ORBs to the transport layer to execute them. This architecture allows you to modify the upper, protocol layer to meet your device’s needs without having to change much of the transport layer of the driver.

This section introduces the main features of the SBP2SampleProject and points out where you can change the code to use it as a foundation for your own project. In order to be universally applicable, the SBP2SampleProject accesses the computer’s hard disk. To test the unmodified project on your Macintosh, follow the instructions included in the FireWire SDK to disable the built-in hard disk driver and allow the sample driver to attach.

Although disabling a built-in driver to allow your user-space driver to attach is an acceptable testing procedure, you should provide your own kernel extension (or KEXT) that can successfully compete with other drivers. This not only ensures that the I/O Kit finds and loads your KEXT for your device, but also provides the CFPlugIn information that identifies your user-space driver plug-in. In general, you should provide your own KEXT when your driver is a user-space plug-in that your application loads using the function `IOCreatePlugInInterfaceForService` or when there may be other drivers competing for your device. Examine the bundle settings of the `SBP2SampleDriver.kext` to see how the driver plug-in is identified. For more information on developing a KEXT, see _[IOKit Device Driver Design Guidelines](../IOKit%20Device%20Driver%20Design%20Guidelines/Introduction%20to%20I-O%20Kit%20Device%20Driver%20Design%20Guidelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmoju)_.

The application portion of the SBP2SampleProject is written in Objective-C using the Cocoa framework and contains two code files: `SelectorController.m` and `LUNController.m`. In addition to GUI-related tasks, the implementation of the SelectorController class is responsible for:

- Getting the Mach port
- Creating a matching dictionary for IOFireWireSBP2LUN objects
- Getting an iterator over the set of matching objects
- Instantiating a LUNController object to create a name string for each matching IOFireWireSBP2LUN object
- Populating an array with matching IOFireWireSBP2LUN objects
- Using the LUNController object to get an interface to the driver plug-in for each IOFireWireSBP2LUN object the user selects
- Releasing the Mach port

The main task of the implementation of the LUNController class is to get the driver plug-in interface and use it to communicate with the device. An instance of the LUNController class:

- Uses the device object reference from an instance of SelectorController to get device properties from the I/O Registry
- Gets the driver plug-in interface for the device object and sets up callbacks on the current run loop
- Performs device `login` and `logout`
- Performs a `read` of the first four blocks of the device
- Releases the driver plug-in interface

The implementation of the LUNController class uses the same Core Foundation functions to get the interface to the driver plug-in as described in [Getting FireWire Device Interfaces](Accessing%20FireWire%20Devices%20From%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnrzfvbuqmrqgiwugq2iivausrkf). For example,

```swift
//Get CFPlugIn interface.
status = IOCreatePlugInInterfaceForService( fLUNReference,
    kSBP2SampleDriverTypeID, kIOCFPlugInInterfaceID, &fCFPlugInInterface,
    &score );
//...
//Get driver plug-in interface.
result = (*fCFPlugInInterface)->QueryInterface( fCFPlugInInterface,
    CFUUIDGetUUIDBytes( kSBP2SampleDriverInterfaceID ), (LPVOID *)
    &fDriverInterface );
```

The only difference is in the parameters identifying the type of interface. Instead of using `kIOFireWireSBP2LibTypeID`, it uses `kSBP2SampleDriverTypeID` to get the IOCFPlugInInterface. Then, it calls `QueryInterface` with `kSBP2SampleDriverInterfaceID` to get the interface to the driver plug-in. Both `kSBP2SampleDriverTypeID` and `kSBP2SampleDriverInterfaceID` are defined in `SBP2SampleDriverInterface.h`.

An instance of the LUNController class performs device functions (`login`, `logout`, and `read`) using functions of the driver plug-in interface. The `login` and `logout` functions are straightforward calls to the driver plug-in interface:

```swift
(*fDriverInterface)->loginToDevice( fDriverInterface );
//...
(*fDriverInterface)->logoutOfDevice( fDriverInterface );
```

The LUNController instance uses a separate thread to perform the `read` function:

```
[NSThread detachNewThreadSelector:@selector(runReadTransaction:)
    toTarget:self withObject:nil];
```

Then, in the `runReadWorker` method, the LUNController instance uses the driver plug-in interface to send the `read` command:

```swift
(*fDriverInterface)->readBlock( fDriverInterface, transactionID, 1, &block );
```


The SBP2SampleProject classes SBP2SampleDriver and SBP2SampleDriverPlugInGlue define objects that comprise the protocol layer. The protocol layer first creates the transport layer, then creates the ORBs, fills and queues them, and communicates with the transport layer to submit them. In turn, the transport layer relays ORB-status and login-status messages to the protocol layer so the SBP2SampleDriver object can react accordingly.

The “glue” in SBP2SampleDriverPlugInGlue mainly refers to code that supplies the SBP2SampleDriver’s methods as CFPlugIn functions (other code handles C++ idiosyncrasies, such as supplying static methods that can call virtual methods on objects). Recall that the application uses standard CFPlugIn functions, such as `QueryInterface`, to get and use the driver plug-in interface. If your application is getting IOFireWireLib or IOFireWireSBP2Lib interfaces directly, the libraries provide this “glue” behind the scenes. The SBP2SampleProject, however, must explicitly provide this code so the application can use the driver plug-in interface as if it were an IOFireWire family device interface.

The SBP2SampleDriver class implements many of the same methods an in-kernel driver does, such as `start`, `stop`, and `probe`. In its `start` method, the driver calls a method of the SBP2SampleORBTransport class to create the transport layer and uses the returned reference to tell the layer to start.

Next, it uses the transport layer’s `createORB` method to create a `TEST_UNIT_READY` ORB. The `TEST_UNIT_READY` ORB is part of the configuration process for SBP-2 hard drives (see [Handling Device Configuration and Reconfiguration](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnrzfvbuqmrqgmwugq2iineuurse) for more information on the device configuration process). Your device may have different configuration needs. Finally, it uses the `createORB` method again to create a pool of free ORBs to draw from later and the Core Foundation function `CFArrayCreateMutable` to create an array to hold in-progress ORBs.

The `stop` method of the SBP2SampleDriver class releases the ORB pool and in-progress ORB array and calls the `stop` method of the SBP2SampleORBTransport class to initiate the shutdown of the transport layer. The `probe` method merely checks to be sure that the referenced device object is of type IOFireWireSBP2LUN.

The SBP2SampleDriver class implementation uses Core Foundation array-handling functions to create and manage its queue of in-progress ORBs, as in this example:

```
CFMutableArrayRef   fInProgressORBQueue;
//...
//kSBP2SampleFreeORBCount is defined in SBP2SampleDriver.h
fInProgressORBQueue = CFArrayCreateMutable( kCFAllocatorDefault,
    kSBP2SampleFreeORBCount, SBP2SampleORB::getCFArrayCallbacks() );
```

Because the SBP2SampleDriver project is multithreaded, it’s possible that one thread might remove an ORB from the free ORB pool at the same time another thread appends one. To protect against this, the SBP2SampleDriver methods that handle the free ORB pool get a lock on a mutex before removing or appending ORBs and release the lock afterwards, as [Listing 3-6](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnrzfvbuqmrqgmwugq2iirbecssj) shows.

__Listing 3-6__  The getORBFromFreePool method of the SBP2SampleDriver class

```swift
SBP2SampleORB * SBP2SampleDriver::getORBFromFreePool( void )
{
    CFIndex freeORBCount;

    pthread_mutex_lock( &fFreePoolLock );
    while ( ( freeORBCount = CFArrayGetCount( fFreeORBPool ) ) == 0 ) {
        //If there are no free ORBs, wait for one.
        pthread_cond_wait( &fFreePoolCondition, &fFreePoolLock );
    }
    //Remove the ORB from the pool.
    SBP2SampleORB * orb = (SBP2SampleORB*) CFArrayGetValueAtIndex(
        fFreeORBPool, 0 );
    orb->retain();
    CFArrayRemoveValueAtIndex( fFreeORBPool, 0 );

    pthread_mutex_unlock( &fFreePoolLock );
    return orb;
}
```

If you need to customize the sample driver’s queueing mechanisms, examine the following methods in which the SBP2SampleDriver class does most of its ORB-handling work:

- `getORBFromFreePool` gets a lock on the `fFreePoolLock` mutex and waits for a free ORB which it removes from the pool and returns.
- `addORBToFreePool` gets a lock on the `fFreePoolLock` mutex, appends the passed-in ORB to the free pool, and sends a signal that wakes up threads that are waiting for free ORBs.
- `appendORBToInProgressQueue` uses a Core Foundation function to add the passed-in ORB to the queue of in-progress ORBs.
- `removeORBFromInProgressQueue` uses Core Foundation functions to find the index of the passed-in ORB in the queue of in-progress ORBs and removes it.

The status of the ORBs is tracked by methods that send reports between the protocol and transport layers. The sample driver uses the transport layer’s `submitORB` method to send an ORB to the device. The transport layer responds by calling one of the following SBP2SampleDriver class methods:

- `completeORB` if the device received the ORB
- `suspendORBs` when a bus reset occurs or if the device is unplugged
- `resumeORBs` if the device is again logged in
- `loginLost` if the connection to the device is lost

The transport layer of the SBP2SampleProject is responsible for acquiring the appropriate IOFireWireSBP2Lib interfaces that allow direct communication with the device and using those interfaces to send ORBs and manage the login status of the device.

The transport layer comprises four classes, listed in order of proximity to the device object:

- SBP2SampleSBP2LibGlue
- SBP2SampleLoginController
- SBP2SampleORB
- SBP2SampleORBTransport

When the protocol layer starts the transport layer, the `start` method of the SBP2SampleSBP2LibGlue class executes, acquiring an IOFireWireSBP2LibLUNInterface. Using this interface, the SBP2SampleSBP2LibGlue instance opens the LUN and gets the IOFireWireSBP2LibLoginInterface. The IOFireWireSBP2LibLoginInterface supplies APIs for login maintenance and command execution.

The SBP2SampleSBP2LibGlue class uses the IOFireWireSBP2LibLoginInterface to register status callbacks that the in-kernel SBP-2 services use to notify the driver, such as `setLoginCallback` and `setStatusNotify`. In addition, the class uses this interface to create an IOFireWireSBP2LibMgmtORBInterface object that gives you access to an SBP-2 management ORB. This object allows you to execute commands such as `QueryLogin`, `AbortTask`, and `LogicalUnitReset`. In this project, the SBP2SampleSBP2LibGlue class uses the IOFireWireSBP2LibMgmtORBInterface object functions to set the command to be managed by the management ORB (with `setManageeLogin`), set the function of the management ORB (with `setCommandFunction`), and set the ORB completion routine (with `setORBCompleteCallback`).

The SBP2SampleLoginController class uses the IOFireWireSBP2LibLoginInterface to send `login` and `logout` commands to the device. The `loginCompletion` method checks status parameters and tries to log in again if necessary. You can add code here to check for status values specific to your device. The SBP2SampleLoginController class also handles callback messages from the device describing the status of the device’s connection. You can subclass the methods that handle the login states (lost, suspended, and resumed) to perform device-specific tasks.

The SBP2SampleORB class implementation is responsible for the ORB object itself. Methods in this class initialize a new SBP2SampleORB object that represents the ORB and provide access to various fields in the IOFireWireSBP2LibORBInterface objects, such as the transaction identification and the maximum ORB payload size.

The SBP2SampleORBTransport class abstracts the transport of ORBs from the protocol layer to the lowest levels of the transport layer. When the SBP2SampleDriver class initiates the transport layer, it calls the factory method of the SBP2SampleORBTransport class. In its `start` method, the SBP2SampleORBTransport class instantiates the SBP2SampleSBP2LibGlue class which acquires the IOFireWireSBP2Lib interfaces it needs to communicate with the device. The SBP2SampleORBTransport class also implements the `submitORB` method for the protocol layer, using the IOFireWireSBP2LibLoginInterface function `submitORB`.

The SBP2SampleORBTransport class notifies the protocol layer of ORB status with a method called `statusNotify`. [Listing 3-7](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnrzfvbuqmrqgmwugq2iireugq2k) shows the `statusNotify` method. It does not show the method `parseStatus` that interprets the ORB’s status and returns one of the values enumerated at the beginning of the SBP2SampleORBTransport class implementation, or the messages `statusNotify` sends to `FWLog` (a macro defined in `FWDebugging.h`).

__Listing 3-7__  The statusNotify method of the SBP2SampleORBTransport class

```swift
void SBP2SampleORBTransport::statusNotify( FWSBP2NotifyParams * params )
{
    SBP2SampleORB * orb = ( SBP2SampleORB *)params->refCon;
    UInt32 event = parseStatus( params );

    switch( event )
    {
        case kStatusDeadBitSet:
            //Suspend protocol layer.
            fDriverLayer->suspendORBs();
            //Complete this ORB.
            completeORB( orb, kIOReturnError );
            //Reset the fetch agent.
            (*fSBP2LoginInterface)->submitFetchAgentReset(
                fSBP2LoginInterface );
            break;
        case kStatusDummyORBComplete:
            if ( orb == fDummyORB ) {
                // All is initialized so resume protocol layer.
                fDriverLayer->resumeORBs();
            }
            else {
                //This must be an aborted ORB.
                completeORB( orb, kIOReturnError );
            }
            break;
            case kStatusORBComplete:
                // Complete the protocol layer’s ORBs.
                completeORB( orb, kIOReturnSuccess );
                break;
            case kStatusORBError:
                completeORB( orb, kIOReturnIOError );
                break;
            case kStatusORBReset:
                //This is a command reset so tell the protocol layer (it
                //should already be suspended at this point).
                completeORB( orb, kIOReturnNotReady );
                break;
            case kStatusORBTimeout:
                //Suspend the protocol layer.
                fDriverLayer->suspendORBs();
                //Complete this ORB.
                completeORB( orb, kIOReturnError );
                //Reset the LUN.
                (*fLUNResetORBInterface)->submitORB( fLUNResetORBInterface
                    );
                break;
        }
}
```

In [Listing 3-7](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnrzfvbuqmrqgmwugq2iireugq2k), the `completeORB` method refers to a method of the SBP2SampleORBTransport class only if the ORB in question is the dummy ORB (described in [Handling Device Configuration and Reconfiguration](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnrzfvbuqmrqgmwugq2iineuurse)); otherwise, it refers to a method of the SBP2SampleDriver class.

Both the transport and protocol layers must perform some configuration before they can accept commands from the application. This occurs when the application starts up and after bus resets. The transport layer appends a dummy ORB (an ORB with no command) to a special register on the SBP-2 device called the fetch agent which holds the address of the ORB the device is currently working on. At login or after a bus reset, you must write the address of the first ORB directly to the fetch agent register. You can then chain all subsequent ORBs onto that first ORB. In this case, the dummy ORB’s function is to always be the first ORB executed at login or after a bus reset.

Because the project is written to access a mass storage device, the protocol layer reconfigures the device when the application starts up and after every bus reset. The protocol layer sends a `TEST_UNIT_READY` ORB because the device is a hard disk—your device might require another type of ORB. The protocol layer must wait until the transport layer has executed the dummy ORB before it can send the `TEST_UNIT_READY` ORB. The application must wait until both these ORBs have executed before it can start sending its own ORBs.

When the project first starts up, an instance of the LUNController class calls the `loginToDevice` method of the SBP2SampleDriver class in response to user input. The protocol and transport layers then perform the following steps to initialize the device and ready it to accept ORBs from the application:

- The SBP2SampleDriver instance calls the `loginToDevice` method of the SBP2SampleLoginController class.
- The SBP2SampleLoginController instance uses the IOFireWireSBP2LibLoginInterface function `submitLogin` to log in to the device.
- When the login is complete, it triggers the SBP2SampleLoginController callback method `loginCompletion` which calls the SBP2SampleORBTransport class’s `loginResumed` method.
- The SBP2SampleORBTransport instance submits a dummy ORB.
- When the dummy ORB completes, the `statusNotify` method of the SBP2SampleORBTransport calls the SBP2SampleDriver’s `resumeORBs` method which sets the `fSuspended` flag to `false` and submits a `TEST_UNIT_READY` ORB to the transport layer.
- The SBP2SampleORBTransport instance submits the `TEST_UNIT_READY` ORB.
- When the `TEST_UNIT_READY` ORB completes, the SBP2SampleORBTransport `statusNotify` method calls the `completeORB` method of the SBP2SampleDriver class.
- The SBP2SampleDriver `completeORB` method checks if the ORB just completed is a `TEST_UNIT_READY` ORB and, if it is, it sets the flag `fDeviceReady` to `true` and proceeds to submit ORBs from the application.

After bus resets, the steps are similar:

- The SBP2SampleLoginController instance receives a `kIOMessageServiceIsSuspended` message and, if it is currently logged in to the device, it sets the `fLoggedIn` flag to `false`.
- The SBP2SampleDriver instance executes its `suspendORBs` method which sets the `fSuspended` flag to `true` and the `fDeviceReady` flag to `false`.
- When the device successfully reconnects, the SBP2SampleLoginController instance receives a `kIOMessageFWSBP2ReconnectComplete` message and sets the `fLoggedIn` flag to `true`.
- The SBP2SampleORBTransport instance then calls the SBP2SampleLoginController class’s `loginResumed` method (which you can modify to perform device-specific operations) and submits a dummy ORB.
- When the dummy ORB completes, the `statusNotify` method of the SBP2SampleORBTransport calls the SBP2SampleDriver’s `resumeORBs` method which sets the `fSuspended` flag to `false` and submits a `TEST_UNIT_READY` ORB to the transport layer.
- The SBP2SampleORBTransport instance submits the `TEST_UNIT_READY` ORB.
- When the `TEST_UNIT_READY` ORB completes, the SBP2SampleORBTransport `statusNotify` method calls the `completeORB` method of the SBP2SampleDriver class.
- The SBP2SampleDriver `completeORB` method checks if the ORB just completed is a `TEST_UNIT_READY` ORB and, if it is, it sets the flag `fDeviceReady` to `true` and proceeds to submit ORBs from the application.

The IOFireWireAVCLib provides two interfaces that you can use independently of each other. The IOFireWireAVCLibProtocolInterface allows you to treat the Macintosh as an AV/C unit, setting up local plugs and receiving AV/C requests. The IOFireWireAVCLibUnitInterface supplies methods that send AV/C commands to an external AV/C unit. The IOFireWireAVCLibUnitInterface also provides a method to get the session reference so you can simultaneously get the IOFireWireLibDeviceInterface to access an external device and read its plug control registers.

The AVCBrowser project shows how to use both interfaces. First, it uses the IOFireWireAVCLibProtocolInterface to allocate and read input and output plugs on the Macintosh and receive AV/C requests. Then, it finds all AV/C units currently in the I/O Registry and gets an IOFireWireAVCLibUnitInterface for each. With this interface, the project opens the unit and sends it commands. Finally, the project gets an IOFireWireDeviceInterface for the device object underlying the IOFireWireAVCUnit object and reads its plug control registers.

AVCBrowser is written in Objective-C using the Cocoa framework and, as such, contains several methods that handle the user interface. For the sake of brevity, this document focuses on only those methods that acquire and use the IOFireWireAVCLib interfaces.

AVCBrowser contains four classes:

- DevicesController implements a DevicesController object that contains an array of AV/C units it finds in the I/O Registry and includes an instance method to open the device and display information about its input and output plugs.
- AVCDevice implements an AVCDevice object that contains information about an IOFireWireAVCUnit object, including a handle to its IOFireWireAVCLibUnitInterface and an IOFireWireDeviceInterface for its underlying IOFireWireDevice object.
- PlugBrowserController implements a PlugBrowserController object that responds to user requests for information about a particular AV/C unit’s input and output plugs.
- Plug implements a Plug object for each plug on an AV/C unit that includes information on its broadcast status and channel.

The implementation of the DevicesController `init` method uses standard I/O Kit functions to get a Mach port and to search the I/O Registry for IOFireWireLocalNode objects (if there is more than one FireWire bus, there is more than one IOFireWireLocalNode object representing the Macintosh). For each object it finds, the `init` method gets an IOFireWireAVCLibProtocolInterface and it uses the interface function `setMessageCallback` to receive bus reset and reconnect messages. It also sets up a routine to handle requests sent to the Macintosh from an AV/C device (in this sample, a video camera), using the interface function `setAVCRequestCallback` .

The DevicesController `init` method then sets up input and output plugs on the local node and reads their values using IOFireWireAVCLibProtocolInterface functions, as [Listing 3-8](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnrzfvbuqmrqgmwugq2iizeucrcj) shows.

__Listing 3-8__  Setting up plugs on the local node

```swift
IOFireWireAVCLibProtocolInterface ** avcInterface;
UInt32 inputPlug, outputPlug;
kern_return_t result;

//Not shown in this listing: acquisition of ‘avcInterface’ and error
//checking using the value of ‘result’.
if ( (*avcInterface)->allocateInputPlug )
    //In the call to allocateInputPlug, writePlug is the callback function
    //called when a successful lock transition plug has been performed
    //and inputPlug is set to the plug number upon successful allocation.
    result = (*avcInterface)->allocateInputPlug( avcInterface, self,
        writePlug, &inputPlug )

if ( (*avcInterface)->readInputPlug ) {
    UInt32 val;
    val = (*avcInterface)->readInputPlug( avcInterface, inputPlug );
    if ( (*avcInterface)->updateInputPlug )
        (*avcInterface)->updateInputPlug( avcInterface, inputPlug, val,
            val+1 );
    val = (*avcInterface)->readInputPlug( avcInterface, inputPlug );
}

if ( (*avcInterface)->freeInputPlug )
    (*avcInterface)->freeInputPlug( avcInterface, inputPlug );

if ( (*avcInterface)->allocateOutputPlug )
    (*avcInterface)->allocateOutputPlug( avcInterface, self, writePlug,
        &outputPlug );

if ( (*avcInterface)->readOutputPlug )
    (*avcInterface)->readOutputPlug( avcInterface, outputPlug );
```

To set up a dispatcher for kernel messages to the program, the `init` method uses the IOFireWireAVCLibProtocolInterface function `addCallbackDispatcherToRunLoop`, as in this example:

```swift
(*avcInterface)->addCallbackDispatcherToRunLoop( avcInterface,
    CFRunLoopGetCurrent() );
```

After setting up the IOFireWireAVCLibProtocolInterface for the local node, the `init` method then registers for notification of new IOFireWireAVCUnit objects in the I/O Registry, using the functions described in [Finding FireWire Devices](Accessing%20FireWire%20Devices%20From%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnrzfvbuqmrqgiwugq2iineuercc). To find all IOFireWireAVCUnit objects already present in the I/O Registry and arm the notification, the DevicesController class calls its function `serviceMatchingCallback`. This function instantiates an AVCDevice object (declared in `AVCDevice.h`) for each IOFireWireAVCUnit object it finds.

The implementation of the AVCDevice class method `withIOService:` uses I/O Kit and Core Foundation functions to extract the IOFireWireAVCUnit object’s `GUID` (globally unique identifier), `Unit_Type`, and `FireWire Product Name` properties. You can use these properties (or any of the properties of the IOFireWireAVCUnit object listed in [Table 2-2](Accessing%20FireWire%20Devices%20From%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnrzfvbuqmrqgiwugq2ijbfeqrkh)) to create a more specific matching dictionary. The `withIOService:` method calls the private function `findPluginForDevice` to create a dictionary that matches on IOFireWireAVCUnit objects with the passed-in GUID and to create an interface of type IOCFPlugInInterface for it.

The `withIOService:` method queries the IOCFPlugInInterface from `findPluginForDevice` to get the IOFireWireAVCLibUnitInterface. It then uses IOFireWireAVCLibUnitInterface functions to open the unit, set up a callback routine and dispatcher, and send a command to the unit, as [Listing 3-9](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnrzfvbuqmrqgmwugq2ii5auirch) shows.

__Listing 3-9__  Communicating with an external AV/C device

```swift
IOReturn    result;
IOFireWireAVCLibUnitInterface   **avcInterface;
AVCDevice   *theDevice;
UInt32      size;
UInt8       cmd[8], response[8];

cmd[kAVCCommandResponse] = kAVCStatusInquiryCommand;
cmd[kAVCAddress] = kAVCUnitAddress;
cmd[kAVCOpcode] = kAVCUnitInfoOpcode;
cmd[3] = cmd[4] = cmd[5] = cmd[6] = cmd[7] = 0xff;
size = 8;

//Error-checking by examining ‘result’ is not shown here.

result = (*avcInterface)->open( avcInterface );

//In the call to setMessageCallback, avcMessage is the completion routine
//that forwards AV/C bus status messages from the I/O Kit.
(*avcInterface)->setMessageCallback( avcInterface, theDevice, avcMessage );
(*avcInterface)->addCallbackDispatcherToRunLoop( avcInterface,
    CFRunLoopGetCurrent() );
result = (*avcInterface)->AVCCommand( avcInterface, cmd, 8, response, &size
    );
```

Next, the `withIOService:` method passes the IOFireWireAVCUnit object’s GUID property and the IOFireWireDevice service type to the `findPluginForDevice` function to get an IOCFPlugInInterface for the corresponding device object. It then gets an IOFireWireDeviceInterface for the device object and uses interface functions to add a callback dispatcher to the current run loop and open the device, as in this example:

```swift
IOFireWireLibDeviceRef  resultInterface;
(*resultInterface)->AddCallbackDispatcherToRunLoop( resultInterface,
    CFRunLoopGetCurrent() );
(*resultInterface)->Open( resultInterface );
```

Finally, the `withIOService:` method uses the instance method `readQuad:` to call the IOFireWireDeviceInterface function `ReadQuadlet` with the addresses of the master output and input plugs, as [Listing 3-10](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnrzfvbuqmrqgmwugq2iirfeiq2i) shows.

__Listing 3-10__  Reading the plug control registers of an external AV/C device

```objc
//...
AVCDevice *theDevice = [[self alloc] init];
//...
FWAddress addr;
UInt32 master;
addr.addressHi = 0xffff;
addr.addressLo = 0xf0000900;

//Read the master output plug.
master = [theDevice readQuad:addr];

//Place results in the AVCDevice object ‘theDevice’.
[theDevice setOutMax: [NSNumber numberWithUnsignedInt:(1 << (master >> 30))
    * 100]];
[theDevice setOutBase: [NSNumber numberWithUnsignedInt:(master >> 24 &
    0x3f)]];
[theDevice setOutNum: [NSNumber numberWithUnsignedInt:master & 0x1f]];

addr.addressLo = 0xf0000980;

//Read the master input plug.
master = [theDevice readQuad:addr];

//Place results in the AVCDevice object ‘theDevice’.
[theDevice setInMax: [NSNumber numberWithUnsignedInt:(1 << (master >> 30)) *
    100]];
[theDevice setInMax: [NSNumber numberWithUnsignedInt:(master >> 24 & 0x3f)]];
[theDevice setInMax: [NSNumber numberWithUnsignedInt:master & 0x1f]];

//...

//The readQuad: instance method.
-(UInt32)readQuad:(FWAddress)addr
{
    UInt32 val = 0xdeadbeef;
    IOReturn status;
    status = (*_interface)->ReadQuadlet( _interface, _device, &addr, &val,
        kFWDontFailOnReset, 0 );
    return val;
}
```

When the AVCBrowser project runs, the user can choose to open a particular AV/C device and view its type, packet speed, and number of input and output plugs. For each plug, the user can view information about it, such as if it is online and broadcasting.

[Next](FireWire%20Device%20Access%20in%20an%20Intel-Based%20Macintosh.md)[Previous](Accessing%20FireWire%20Devices%20From%20Applications.md)

