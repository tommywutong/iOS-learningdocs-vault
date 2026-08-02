---
title: IOKit Device Driver Design Guidelines
apple_id: TP30000694
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2009-08-14'
source_url: https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/WritingDeviceDriver/IOService/IOService.html
archived_at: '2026-07-15T07:31:49.306969Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [IOKit Device Driver Design Guidelines](Introduction%20to%20I-O%20Kit%20Device%20Driver%20Design%20Guidelines.md)


[Next](Making%20Hardware%20Accessible%20to%20Applications.md)[Previous](libkern%20Collection%20and%20Container%20Classes.md)

# The IOService API

Even though the IOService class inherits directly from IORegistryEntry and, by extension, from OSObject, you can think of IOService as the root class of nearly every object in the I/O Registry and, at least indirectly, of every driver. The methods of the IOService API are numerous and wide-ranging, providing services for most aspects of device management, from driver matching and loading to device interrupts and power management.

The majority of these methods are for internal (IOService) and I/O Kit family use. Many IOService methods are helper methods that IOService uses to implement other methods. Many more are meant for the I/O Kit families to implement. As a driver developer for a family-supported device, you will implement or call only a small fraction of the methods in IOService. If you are developing a driver for a familyless device, such as a PCI device, you may need to implement some of the IOService methods that families typically implement.

This chapter explores the public IOService methods that are available for external use in each of the following categories:

- Driver life cycle, including matching
- Notifications and messaging
- Accessing objects
- Power management
- Memory mapping
- Interrupt handling

In the dynamic I/O Kit environment, a driver can be loaded and unloaded, or activated and deactivated, at any time. The constant in this flurry of activity is the set of IOService and IORegistryEntry methods that define every driver’s life cycle.

With the exception of `init` and `free`, which OSObject defines, the remaining driver life-cycle methods are IOService methods. Because these methods are well-documented elsewhere (see_[IOKit Fundamentals](../IOKit%20Fundamentals/Introduction%20to%20I-O%20Kit%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridambqgaydcmi)_), this chapter does not cover them again. Instead, the following sections present the less well-known IOService methods related to the driver life cycle.

IOService includes a number of methods used in the driver-matching process, but unless you are developing a family or writing a familyless driver, you do not need to implement any of them. It is important, however, to understand the driver-matching process and how the I/O Kit uses IOService’s matching methods so you can successfully define your driver’s personality dictionary.

[Table 3-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmojxfvbucq2djjeecrq) shows the IOService matching methods and briefly describes how the I/O Kit uses them.

__Table 3-1__  IOService matching methods

| IOService method | Usage |
| `compareProperties` | Helper function used in implementing `matchPropertyTable` |
| `compareProperty` | Helper function used in implementing `matchPropertyTable` |
| `getMatchingServices` | In-kernel counterpart of the user-space function `IOServiceGetMatchingServices` |
| `matchPropertyTable` | Optionally implemented by families (or familyless drivers) to examine family-specific match properties |
| `nameMatching` | In-kernel counterpart of the user-space function `IOServiceNameMatching` |
| `resourceMatching` | In-kernel matching function to create a dictionary to search for `IOResources` objects |
| `serviceMatching` | In-kernel counterpart of the user-space function `IOServiceMatching` |

For more information on the user-space functions `IOServiceGetMatchingServices`, `IOServiceNameMatching`, and `IOServiceMatching`, see _[Accessing Hardware From Applications](../Accessing%20Hardware%20From%20Applications/Introduction%20to%20Accessing%20Hardware%20From%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgnzw)_ or the HeaderDoc documentation for `IOKitLib.h` in `/Developer/ADC Reference Library/documentation/Darwin/Reference/IOKit`.

Understanding how the I/O Kit uses your driver’s personality in the driver-matching process is an important prerequisite to crafting successful personality dictionaries. As described in _[IOKit Fundamentals](../IOKit%20Fundamentals/Introduction%20to%20I-O%20Kit%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridambqgaydcmi)_, the I/O Kit uses the driver’s required `IOProviderClass` key during the class-matching step to eliminate all drivers with the wrong provider type. Usually, this step eliminates the majority of drivers, leaving only those that attach to the correct nub type.

In the passive-matching phase, the I/O Kit examines the remaining keys in a driver’s personality dictionary and compares them to the provider–class specific information in the device nub. It is during this phase that the family can implement the `matchPropertyTable` method to more closely inspect the match candidate.

When a family implements `matchPropertyTable`, it can interpret the match candidate’s property values in any way it chooses, without interference from the I/O Kit. Additionally, if a driver includes a family-defined property in its `Info.plist` file, the I/O Kit ignores it if the family does not implement the `matchPropertyTable` method. As a driver writer, you should be familiar with the properties your driver’s family uses. For example, the IOSCSIPeripheralDeviceNub class (in the IOSCSIArchitectureModel family) implements `matchPropertyTable` to rank a match candidate according to how many family-specific properties it has. [Listing 3-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmojxfvbucq2hincumra) shows a fragment of IOSCSIPeripheralDeviceNub’s `matchPropertyTable` implementation.

__Listing 3-1__  A `matchPropertyTable` implementation


```
bool IOSCSIPeripheralDeviceNub::matchPropertyTable ( OSDictionary * table,
                                    SInt32 * score )
{
    bool returnValue = true;
    bool isMatch = false;
    SInt32 propertyScore = * score;
    /* Adjust a driver's initial score to avoid "promoting" it too far. */
    /* ... */
    /* Use IOSCSIPeripheralDeviceNub's sCompareProperty method to compare */
    /* the driver's properties with family-specific properties. */
    if ( sCompareProperty ( this,table, kIOPropertySCSIPeripheralDeviceType,
                            &isMatch ) )
    {
        if ( isMatch ) {
            *score = kDefaultProbeRanking;
        }
        else {
            *score = kPeripheralDeviceTypeNoMatch;
            returnValue = false;
        }
        if ( sCompareProperty ( this, table,
                                kIOPropertySCSIVendorIdentification,
                                &isMatch ) ) {
            if ( isMatch ) {
                *score = kFirstOrderRanking;
                /* Continue to test for additional properties, */
                /* promoting the driver to the next rank with each */
                /* property found. */
            }
        }
    } else {
        /* Take care of SCSITaskUserClient "driver" here. */
    }
    if ( *score != 0 )
        *score += propertyScore;
    return returnValue;
}
```


In addition to the family-specific keys the family may require, there are several passive-matching keys the I/O Kit defines:

- `IOProviderClass`
- `IOPropertyMatch`
- `IONameMatch`
- `IOResourceMatch`
- `IOParentMatch`
- `IOPathMatch`

`IOProviderClass` is required for all driver personalities because it declares the name of the nub class the driver attaches to. The provider class name also determines the remaining match keys.

The `IOPropertyMatch` key represents a specific list of properties that must match exactly in order for the I/O Kit to load the driver. For example, the IOBlockStorageDriver defines the following personality:

```
<key>IOProviderClass</key>
<string>IOBlockStorageDevice</string>
<key>IOClass</key>
<string>IOBlockStorageDriver</string>
<key>IOPropertyMatch</key>
<dict>
    <key>device-type</key>
    <string>Generic</string>
</dict>
```

After the I/O Kit determines that the IOBlockStorageDriver is a match candidate for a nub of class IOBlockStorageDevice, it examines the value of the `IOPropertyMatch` key. If the nub has a `device-type` key with the value `Generic`, the I/O Kit loads this personality of the IOBlockStorageDriver.

The utility of the `IOPropertyMatch` key lies in the fact that the I/O Kit uses its value in the matching process regardless of whether the family implements the `matchPropertyTable` method. Unlike the `matchPropertyTable` method, however, the `IOPropertyMatch` key does not allow the family to interpret its value—if the `IOPropertyMatch` value does not match the nub’s corresponding property exactly, the I/O Kit removes the driver from the pool of match candidates.

The `IONameMatch` key matches on the `compatible`, `name`, or `device-type` properties of a provider. The value of the `IONameMatch` key can be an array of strings representing a list of all such properties your driver can match on. After the I/O Kit has matched and loaded your driver, it places the `IONameMatched` property and the value of the actual property value your driver matched on in your driver’s I/O Registry property table.

[Listing 3-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmojxfvbucq2fi5demsa) shows part of one of the personalities of the GossamerPE (a Platform Expert for the Blue and White G3 computer):

__Listing 3-2__  A personality of the GossamerPE

```
<key>GossamerPE</key>
<dict>
    <key>IOClass</key>
    <string>GossamerPE</string>
    <key>IONameMatch</key>
    <array>
        <string>AAPL,Gossamer</string>
        <string>AAPL,PowerMac G3</string>
        <string>AAPL,PowerBook1998</string>
        <string>iMac,1</string>
        <string>PowerMac1,1</string>
        <string>PowerMac1,2</string>
        <string>PowerBook1,1</string>
    </array>
    <key>IOProviderClass</key>
    <string>IOPlatformExpertDevice</string>
</dict>
```

The `IONameMatch` key contains an array of several possible names. Note that there is no `IONameMatched` key in this personality. [Listing 3-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmojxfvbucq2hinbuosq) shows part of the I/O Registry entry for the GossamerPE after the I/O Kit matched and loaded it for a particular device:

__Listing 3-3__  Partial I/O Registry entry for GossamerPE

```
GossamerPE  <class GossamerPE>
{
    "IOClass" = "GossamerPE"
    "IOProviderClass" = "IOPlatformExpertDevice"
    "IONameMatched" = "PowerMac1,1"
}
```

The `IOResourceMatch` key declares a dependency or connection between your driver and a specific resource, such as the BSD kernel or a particular resource on a device, like an audio-video jack. If you add the key-value pair

```
<key>IOResourceMatch</key>
<string>IOBSD</string>
```

to your driver’s personality, for example, your driver will not load until the resource, in this case the BSD kernel, is available. In this way, you can effectively stall the loading of your driver until its required resource is available. You can examine the available resources in IOResources on a running OS X system using the I/O Registry Explorer application (available in `/Developer/Applications`). In the IOService plane (I/O Registry Explorer’s default plane), click Root, click the platform expert device for your machine (such as PowerMac3,3), and then click IOResources.

The remaining passive-matching keys, `IOParentMatch` and `IOPathMatch`, are useful for user-space driver-client matching and are very rarely used in in-kernel driver personalities. These keys depend on information about the location of an object or service in the I/O Registry rather than on the device-specific or service-specific information a nub publishes. An application developer can examine the I/O Registry to determine the location of a specific object and create a matching dictionary using that information. This is much more difficult for an in-kernel driver developer, however, because accurate I/O Registry location of objects may not be available at development time.

IOService provides some methods that give you information about an IOService object’s state which is described in the IOService private instance variable `state`. You can view the states of objects currently attached in the I/O Registry by typing `ioreg -s` on the command line.

When a driver is in the midst of registration, matching, or termination, its busy state is set to one. When these activities conclude, the busy state is reduced to zero. Any change in an IOService object’s busy state causes an identical change in its provider’s busy state, so that a driver or other IOService object is considered busy when any of its clients is busy.

A driver may need to wait for a change in another IOService object’s state. The `waitQuiet`method allows a driver to block until the specified IOService object’s busy state is zero.

A driver can call the `adjustBusy` method to mark itself busy if, for example, it wishes to asynchronously probe a device after exiting from its `start` method.

Two IOService methods return information about a driver’s stage in its life cycle. The `isOpen` method determines if a specified client has an IOService object open. If you pass zero instead of a pointer to a particular client object, `isOpen` returns the open state for all clients of an object.

The second method, `isInactive`, indicates that an IOService object has been terminated. An inactive object does not support matching, attachments, or notifications.

The I/O Kit’s resource service uses the matching and notification methods usually used for driver objects to make resources available system-wide through IOResources, an instance of IOService attached to the root of the I/O Registry. A resource might be an audio-output jack on a device or a service, such as the BSD kernel. The I/O Kit itself appears as a resource.

A driver, or other IOService object, can publish a resource in IOResources using the IOService method `publishResource`. The publication of a resource triggers any notifications set on its presence, and the objects holding those notifications can then access the resource.

The IOKernelDebugger (in the IONetworking family) publishes its presence as a resource in this way:

```
publishResource ( "kdp" );
```

A driver can request a notification about the resource, make the resource a matching condition (as described in[Passive-Matching Keys](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmojxfvbucq2ijbceqqq)), or, as in the AppleUSBCDCDriver, call the `waitForService` method to wait until a particular resource appears:

```
waitForService ( resourceMatching ( "kdp" ) );
```

The `waitForService` method allows an IOService object to block until the object matching the specified matching dictionary is registered. Optionally, a driver can also specify a maximum time to wait.

IOService provides the `newUserClient` method for families that support user clients. A family that provides user clients implements the `newUserClient` method to create a connection between a user-space client application and an in-kernel user-client object.

The default implementation of `newUserClient` looks up the `IOUserClientClass` key in the given IOService object’s properties. If the key is found, IOService creates an instance of the class given in the value. Then, it calls the methods `initWithTask`, `attach`, and `start` on the newly instantiated user-client class object. If, on the other hand, there is no `IOUserClientClass` key (or its value is invalid) or any of the initialization methods fail, IOService returns `kIOReturnUnsupported`.

For more information on implementing a user-client object, see [Making Hardware Accessible to Applications](Making%20Hardware%20Accessible%20to%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmojyfvbeeq2djjceksa).

In addition to the `probe` method your driver can choose to implement to examine a device during the matching process (described in detail in _[IOKit Fundamentals](../IOKit%20Fundamentals/Introduction%20to%20I-O%20Kit%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridambqgaydcmi)_), IOService provides the `requestProbe` method for discovering newly added or removed devices. The `requestProbe` method gives the families that do not automatically detect device addition and removal a way to rescan the bus and publish new devices and detach removed devices.

A family, or perhaps a bus-controller driver, implements `requestProbe` and passes it a set of options contained in an object of type IOOptionBits, which is not interpreted by IOService.

A driver frequently communicates with other entities in the I/O Registry to perform its functions. During the course of its life, a driver must be prepared to receive status and other types of messages from its provider, register for and receive notifications of various events, and send messages to its clients. IOService provides a small number of methods to handle these tasks.

The `addNotification` method expects a pointer to a notification handler that IOService calls when the specified IOService object attains the specified state. For example, a driver might need to know when a particular IOService object is published. [Listing 3-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmojxfvbucq2iifeucri) shows how an instance of IOBSDConsole requests notification of the appearance of an IOHIKeyboard object:

__Listing 3-4__  Using the `addNotification` method

```
OSObject * notify;
notify = addNotification( gIOPublishNotification,
    serviceMatching( "IOHIKeyboard" ),
    ( IOServiceNotificationHandler )
        &IOBSDConsole::publishNotificationHandler,
    this, 0 );
assert( notify );
```

The first parameter `addNotification` expects is of class OSSymbol; it defines the type of event or status change. IOService delivers the notification types shown in [Table 3-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmojxfvbucq2firceera).

__Table 3-2__  Notification types and events

| Notification type | Event type |
| `gIOPublishNotification` | An IOService object is newly registered. |
| `gIOFirstPublishNotification` | Similar to `gIOPublishNotification`, but delivered only once for each IOService instance, even if the object is reregistered when its state changes. |
| `gIOMatchedNotification` | An IOService object is matched with all client objects, which have all been started. |
| `gIOFirstMatchNotification` | Similar to `gIOMatchedNotification`, but delivered only once for each IOService instance, even if the object is reregistered when its state changes. |
| `gIOTerminatedNotification` | An IOService object is terminated during its `finalize` stage. |

The second parameter is a dictionary describing the IOService object to match on. In [Listing 3-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmojxfvbucq2iifeucri), the IOBSDConsole object uses the IOService method `serviceMatching` (introduced in [Driver Matching](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmojxfvbucq2gizceqra)) to create a dictionary with the class name IOHIKeyboard. When a matching object is published in the I/O Registry, IOService calls the notification-handling method passed to `addNotification` in the third parameter.

IOService calls the notification handler with a reference to each of the matching IOService objects that attain the specified state, beginning with the objects already in that state. The notification handler code can then use that reference in any way it chooses. Often, as in the case of the IOBSDConsole object, the notification handler examines one of the properties of the matching IOService object to update its own object’s properties. [Listing 3-5](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmojxfvbucq2dizaukra) shows a fragment of the IOBSDConsole’s notification-handler code.

__Listing 3-5__  Implementing a notification-handling method

```swift
bool IOBSDConsole::publishNotificationHandler( IOBSDConsole * self,
    void * ref, IOService * newService ) {
    IOHIKeyboard * keyboard = 0;
    IOService * audio = 0;

    if ( ref ) {
        audio = OSDynamicCast( IOService,
            newService->metaCast( "IOAudioStream" ) );
        if ( audio != 0 ) {
            OSNumber * out;
            out = OSDynamicCast( OSNumber, newService->getProperty( "Out" );
            if ( out ) {
                if ( out->unsigned8BitValue == 1 ) {
                    self->fAudioOut = newService;
                }
            }
        }
    }
    else { /* Handle other case here */ }
}
```

The `installNotification` method is very similar to the `addNotification` method, except that you pass it an object of class OSIterator into which the method places an iterator over the set of matching IOService objects currently in the specified state.

The primary lines of communication between a driver and its provider and clients are the messaging methods. In order to receive messages from its provider, your driver must implement the `message` method. To send messages to its clients, your driver must implement the `messageClient` or `messageClients` method.

Frequently, your driver will receive messages defined by the I/O Kit in `IOMessage.h` (available in `/System/Library/Frameworks/Kernel.framework/Headers/IOKit`), but your driver’s family may also define its own messages. The IOUSBDevice class, for example, implements the `message` method to handle a number of USB family-specific messages, in addition to messages defined in `IOMessage.h`. [Listing 3-6](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmojxfvbucq2kjjbuksq) shows a fragment of IOUSBDevice’s implementation of the `message` method.

__Listing 3-6__  Implementing the `message` method

```
IOReturn IOUSBDevice::message( UInt32 type, IOService * provider, void
     *argument ) {

    /* local variable declarations */

    switch ( type ) {
        case kIOUSBMessagePortHasBeenReset:
            /* handle this case */
        case kIOUSBMessageHubIsDeviceConnected:
            /* handle this case */
        case kIOUSBMessagePortHasBeenResumed:
            /* handle this case */
        /* handle messages defined in IOMessage.h */
        /* ... */
    }
}
```

A provider uses the `messageClient` and `messageClients` methods to send messages to its clients. Although you can override the `messageClient` method, you rarely need to do so unless, for example, you’re writing a framework. IOService implements the `messageClients` method by applying the `messageClient` method to each client in turn. Referring again to the IOUSBDevice implementation of `message` (shown in [Listing 3-6](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmojxfvbucq2kjjbuksq)), an instance of IOUSBDevice calls `messageClients` on its clients to forward the messages it received from its provider, as in the following code fragment:

```
/* Previous cases of the switch statement handled here. */
case kIOUSBMessagePortHasBeenResumed:
    // Forward the message to our clients.
    messageClients( kIOUSBMessagePortHasBeenResumed, this, _portNumber );
    break;
/* Following cases of the switch statement handled here. */
```


IOService provides a number of methods you can use to access your driver’s provider, clients, and various other objects in the I/O Registry. A few of these methods are for internal use only, but most are available for your driver to call when it needs to access other objects currently in the I/O Registry.

Perhaps the most widely used IOService access method is `getWorkLoop`. Any time you need to ensure single-threaded access to data structures or handle asynchronous events, such as timer events or I/O commands driver clients issue to their providers, you should use a work loop. For extensive information on the architecture and use of work loops, see _[IOKit Fundamentals](../IOKit%20Fundamentals/Introduction%20to%20I-O%20Kit%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridambqgaydcmi)_.

Many drivers can successfully share their provider’s work loop to protect sensitive data and handle events. A call to `getWorkLoop` returns your provider’s work loop or, if you provider does not have one, the work loop of the object below your provider in the driver stack. At the root of the I/O Registry, the IOPlatformExpertDevice object holds a system-wide work loop your driver can share, even if your providers do not have work loops.

The ApplePCCardSample driver gets the PCCard family work loop with the following lines of code:

```
IOWorkLoop * workLoop;
workLoop = getWorkLoop();
if ( !workLoop ) {
    /* Handle error. */
}
```

Although most drivers do not need to create their own work loops, a driver for a PCI controller or PCI device or any driver that interacts directly with an interrupt controller should create its own, dedicated work loop. For an example of how to do this, see _[IOKit Fundamentals](../IOKit%20Fundamentals/Introduction%20to%20I-O%20Kit%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridambqgaydcmi)_.

The methods for accessing providers and clients fall into two categories: Those that return the provider or client object itself and those that return an iterator over a set of providers or clients. The methods in the first category, `getClient` and `getProvider`, return an IOService object’s primary client and primary provider, respectively. IOService defines the primary client as the first client to attach to the IOService object and the primary provider as the provider to which the IOService object first attached. Most often, your driver will have only one provider and one client, so these methods provide a convenient way to access them without having to further specify the provider or client you want.

The IOService objects returned by the `getClient` and `getProvider` methods should not be released by the caller. The client object is retained as long as it is attached and the provider object is retained as long as the client is attached to it. It is unlikely you will need to override these methods, but one possibility is implementing them to narrow down the type of IOService object returned. For example, as a convenience to subclass developers, the IOCDMedia object overrides its superclass’s `getProvider` method to return IOCDBlockStorageDriver rather than the more generic IOService:

```
IOCDBlockStorageDriver * IOCDMedia::getProvider() const
{
    return (IOCDBlockStorageDriver *) IOService::getProvider();
}
```

The methods `getClientIterator`, `getOpenClientIterator`, `getProviderIterator`, and `getOpenProviderIterator` comprise the set of IOService client-provider access methods that return iterators. When you use `getClientIterator` or `getProviderIterator` to access your driver’s clients or providers, each object the iterator returns is retained as long as the iterator is valid, although it is possible that the object may detach itself from the I/O Registry during the iteration. In addition, you must release the iterator when you are finished with the iteration. [Listing 3-7](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmojxfvbucq2cifcegqi) shows how the IOFireWireAVCUnit object uses `getClientIterator` to check for existing subunits before creating a new one.

__Listing 3-7__  `getClientIterator` example

```swift
/* Create propTable property table with the subunit type property. */
OSIterator * childIterator;
IOFireWireAVCSubUnit * found = NULL;
childIterator = getClientIterator();
if ( childIterator ) {
    OSObject * child;
    while ( ( child = childIterator->getNextObject() ) ) {
        found = OSDynamicCast( IOFireWireAVCSubUnit, child );
        if ( found && found->matchPropertyTable( propTable ) ) {
            break;
        }
        else
            found = NULL;
    }
    childIterator->release();
    if ( found )
        /* Continue searching for existing subunits. */
}
```

The `getOpenClientIterator` and `getOpenProviderIterator` methods differ from the `getClientIterator` and `getProviderIterator` methods in two important ways. First, as their names suggest, `getOpenClientIterator` and `getOpenProviderIterator` return iterators for only the open clients and providers. For `getOpenClientIterator`, this means an iterator for a provider’s clients that have opened the provider, and for `getOpenProviderIterator`, it means an iterator for a client’s providers that the client currently has open. Second, IOService uses the `lockForArbitration` method to lock the current object in the iteration so that its state does not change while you are accessing it.

The `getOpenClientIterator` and `getOpenProviderIterator` methods mirror the `getClientIterator` and `getProviderIterator` methods in that the objects the iterator returns are retained as long as the iterator is valid and in that you must release the iterator when you no longer need it.

The remaining IOService access methods are:

- `getPlatform`
- `getResources`
- `getState`

Of these three, two are used almost exclusively by the I/O Kit and IOService. The `getResources` method allows for lazy allocation of resources during the registration process for an IOService object by deferring the allocation until a matching driver is found for the object. The `getState` method returns the IOService state for an IOService object and is not typically used outside of IOService’s internal implementations.

In the unlikely event that your driver needs to find out which platform it is running on, it can call the `getPlatform` method, as in this example that determines the platform’s computer type:

```swift
if ( getPlatform()->getMachineType() == kGossamerTypeYosemite )
    /* Do something here. */
```

The `getPlatform` method gives you a reference to the platform expert instance for the computer you’re currently running on. With this reference, you can then call platform expert methods, such as `getModelName` and `getMachineName` to get specific information about it (for more information on platform expert methods, see `/System/Library/Frameworks/Kernel.framework/Headers/IOKit/IOPlatformExpert.h`).

On an OS X system, changes in power state can happen at any time. Whether it is due to the hot-unplugging of a device or system sleep, your driver must be prepared to handle a change in its power state whenever it happens.

The IOService class includes a large number of methods related to power management but unless your driver serves as a policy maker or as the power controller for your device, you will probably not need to implement or call any of them.

This section briefly introduces policy makers and power controllers and how they can interact with your driver to give context for the IOService power management methods. For more information on power management in general and how to implement policy makers and power controllers in particular, see_[IOKit Fundamentals](../IOKit%20Fundamentals/Introduction%20to%20I-O%20Kit%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridambqgaydcmi)_.

The power-management subsystem of an OS X system is responsible for providing enough power to function at the required level while at the same time prolonging display life and conserving power. To do this, power management keeps track of the power needs and states of all devices and subsystems, and uses that information to make power-supply decisions.

A power domain is a switchable source of power in the system that provides power for one or more devices considered to be members of the domain. The root power domain represents the main power of the OS X system itself and contains all other power domains. You can view the (current) hierarchical structure of the root power domain and all its dependent domains in the I/O Registry’s IOPower plane by entering `ioreg -p IOPower` at the command line.

Each entity in power management, such as a power domain or device, is represented by an object that inherits from the IOService class. The power management methods IOService provides allow all power-management objects to communicate with each other to manage the power usage of the system.

Two types of power-management objects perform most of the power-related tasks for the system: policy makers and power controllers. A policy maker is usually an instance of an I/O Kit family class, but it can be any object at an appropriate level in a driver stack. The policy maker for a device (or domain) considers factors such as aggressiveness (a measure of how urgently a device should conserve power) when making decisions that affect the power level of that device or domain.

As its name suggests, the power controller for a device is the expert on that device’s power capabilities and carries out the decisions of the policy maker. The communication between policy maker and power controller flows in both directions: The policy maker decides to change the power state of a device and tells the power controller and the power controller gives the policy maker information about the device that helps the policy maker make its decisions.

Because a policy maker needs to know about the type of device being controlled, including its power-usage patterns, it is usually implemented as an instance of an I/O Kit family class. For the same reasons, an I/O Kit family class may also choose to implement a power controller for its devices, although it is more common for the driver that actually controls a device’s I/O to be that device’s power controller. It's important to read the documentation for the family to which your driver belongs, because each family may apportion power management tasks a little differently.

If you are implementing a driver that represents physical hardware, such as a PCI device, or a physical subsystem, such as an Ethernet driver, you may be responsible for being both policy maker and power controller for your device. At minimum, you should be familiar with the following subset of IOService power management methods:

- `PMinit`
- `PMstop`
- `joinPMTree`
- `registerPowerDriver`
- `changePowerStateTo`
- `setAggressiveness`
- `setPowerState`
- `activityTickle`
- `setIdleTimerPeriod`
- `acknowledgePowerChange`
- `acknowledgeSetPowerState`

If your driver is serving as the power controller for your device, it should first create an array of structures that describe your device’s power requirements and capabilities. Each structure is of type `IOPMPowerState` (declared in `IOPMpowerState.h` available at `/System/Library/Frameworks/Kernel.framework/Headers/IOKit/pwr_mgt`). For example, the ApplePCCardSample driver defines the following array:

```
static const IOPMPowerState myPowerStates[ kIOPCCard16DevicePowerStateCount ]
{
    { 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 },
    { 1, 0, IOPMSoftSleep, IOPMSoftSleep, 0, 0, 0, 0, 0, 0, 0, 0 },
    { 1, IOPMPowerOn, IOPMPowerOn, IOPMPowerOn, 0, 0, 0, 0, 0, 0, 0, 0 }
};
```

In order for a policy maker or a power controller to participate in the power-management subsystem, it must first initialize the protected power-management instance variables in the IOPMpriv and IOPMprot objects (for more information on these objects, see_[IOKit Fundamentals](../IOKit%20Fundamentals/Introduction%20to%20I-O%20Kit%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridambqgaydcmi)_). A driver does this by calling the `PMinit` method, typically in its `start` method. At the end of a driver’s life span, usually in its `stop` method, a driver resigns its power-management responsibilities and disables its power-management participation by calling the `PMstop` method, which erases the IOPMpriv and IOPMprot objects and serves to de-register the driver.

Not surprisingly, different I/O Kit families can handle the exact distribution of power-management responsibilities in different ways. For example, in its `stop` method, the IOFramebuffer superclass calls `PMstop` automatically for all its subclasses, so an IOFramebuffer subclass should not call `PMstop` itself. Before implementing power management in your driver, therefore, be sure to find out how your driver’s I/O Kit family assigns power-management responsibilities.

After creating the array of power states, your driver can then volunteer as the power controller for your device by calling the method `registerPowerDriver`, passing it a pointer to itself, the power state array, and the number of states in the array, as in this example from ApplePCCardSample’s `start` method:

```
registerPowerDriver ( this, (IOPMPowerState *) myPowerStates,
                    kIOPCCard16DevicePowerStateCount );
```

Although the `PMinit` method initializes the power-management variables, it does not attach the calling driver to the power-management hierarchy, or tree. Therefore, after registering as the power controller, the ApplePCCardSample then becomes a member of the power-management tree by calling the `joinPMTree` method on its provider:

```swift
provider->joinPMtree ( this );
```

When a power-controller driver needs to change its power state, it calls the `changePowerStateTo` method, passing in the ordinal value of the desired power state in the power state array. Conversely, when a policy maker needs to tell a power controller to change its power state, the policy maker calls the `setPowerState` method. It passes in the ordinal value of the desired power state in the power state array and a pointer to the particular IOService object whose power state the power controller should change.

Aggressiveness is a measure of how aggressive the power-management subsystem should be in conserving power. Policy makers need to be aware of the current aggressiveness in order to appropriately determine when a device or domain is idle. In general, a policy maker should implement the `setAggressiveness` method to receive information about changes in aggressiveness, but it should be sure to invoke its superclass’s `setAggressiveness` method, as well.

The IODisplayWrangler, for example, is the policy maker for displays. It senses when a display is idle or active and adjusts the power accordingly. The IODisplayWrangler uses aggressiveness levels from its power domain parent in its calculation of an idle-timer period. When the timer expires and no user activity has occurred since the last timer expiration, the IODisplayWrangler lowers the power state of the display. [Listing 3-8](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmojxfvbucq2jjfduury) shows IODisplayWrangler’s implementation of the `setAggressiveness` method.

__Listing 3-8__  The IODisplayWrangler `setAggressiveness` method

```swift
IOReturn IODisplayWrangler::setAggressiveness( unsigned long type, unsigned
                                             long newLevel )
{
    if( type == kPMMinutesToDim) {
        // Minutes to dim received.
        if( newLevel == 0) {
            // Power management turned off while idle?
            if( pm_vars->myCurrentState < kIODisplayWranglerMaxPowerState) {
                // Yes, bring displays up again.
                changePowerStateToPriv( kIODisplayWranglerMaxPowerState );
            }
        }
        fMinutesToDim = newLevel;
        fUseGeneralAggressiveness = false;
        // No. Currently in emergency level?
        if( pm_vars->aggressiveness < kIOPowerEmergencyLevel) {
            // No, set new timeout.
            setIdleTimerPeriod( newLevel*60 / 2);
        }

    // general factor received.
    } else if( type == kPMGeneralAggressiveness) {
        // Emergency level?
        if( newLevel >= kIOPowerEmergencyLevel ) {
            // Yes.
            setIdleTimerPeriod( 5 );
        }
        else {
            // No. Coming out of emergency level?
            if( pm_vars->aggressiveness >= kIOPowerEmergencyLevel ) {
                if( fUseGeneralAggressiveness) {
                    // Yes, set new timer period.
                    setIdleTimerPeriod( (333 - (newLevel/3)) / 2 );
                }
                else {
                    setIdleTimerPeriod( fMinutesToDim * 60 / 2);
                }
            }
            else {
                if( fUseGeneralAggressiveness) {
                    // No, maybe set period.
                    setIdleTimerPeriod( (333 - (newLevel/3)) / 2 );
                }
            }
        }
    }
    super::setAggressiveness(type, newLevel);
    return( IOPMNoErr );
}
```

A policy maker uses the `activityTickle` method to help it determine when a device is idle. If the policy maker is solely responsible for determining idleness, it should implement the `activityTickle` method to intercept any calls by other driver objects and use its own methods to determine idleness periods. In this situation, power-controller drivers call the `activityTickle` method when there is device activity or for any other reason the device needs to be fully powered, with the `kIOPMSubclassPolicy` parameter.

A policy maker that determines idleness in cooperation with IOService, on the other hand, should first call `setIdleTimerPeriod` on its superclass, passing in the number of seconds for the timer interval. If the policy maker needs other objects to inform it of device activity, it should implement `activityTickle` as described above. When it becomes aware of activity, the policy maker should call `activityTickle` on its superclass, passing in the `kIOPMSubclassPolicy1` parameter. Then, when the idle timer expires, the IOService superclass checks to see if `activityTickle(kIOPMSubclassPolicy1)` has been called on it. If it has, then there has been activity and the IOService superclass restarts the idleness timer. If it hasn’t, and there has been no activity, the IOService superclass calls `setPowerState` on the power controller to tell it to lower the device’s power state to the next lower level.

A policy maker tells interested IOService objects when a device’s power state is changing. In return, such an object can tell the policy maker that it is either prepared for the change or needs time to prepare by calling the `acknowledgePowerChange` method on the policy maker.

When a policy maker tells a power controller to change a device’s power state, the power controller uses the `acknowledgeSetPowerState` method to tell the policy maker either that it has made the change or that it needs time to make the change.

IOService provides a number of methods for low-level access of device memory and interrupt-handling. Most driver writers will not need to use these because the I/O Kit families generally take care of such low-level access. In addition, unless you are implementing an interrupt controller, you should use the interrupt-handling facilities IOInterruptEventSource provides or, for PCI devices, IOFilterInterruptEventSource (both available in `/System/Library/Frameworks/Kernel.framework/Headers/IOKit`.)

If you’re writing a device driver for a familyless device, however, you may need to gain direct access to your device’s memory or implement an interrupt-controller driver. This section describes the IOService methods that can help you.

The IOService methods for accessing device memory handle IODeviceMemory objects. IODeviceMemory is a simple subclass of IOMemoryDescriptor, the abstract base class that defines common methods for describing physical or virtual memory. An IODeviceMemory object describes a single range of physical memory on a device and implements a handful of factory methods to create instances with particular memory ranges or subranges.

You can think of the memory-access methods in IOService as wrappers for IOMemoryDescriptor methods. If your device’s provider is a memory-mapped device, IOService provides it with its own array of memory descriptors (IODeviceMemory objects). The first member of the array might be the IODeviceMemory object that represents the `vram` and the second might represent the device’s registers. The IOService memory-access methods allow you to specify a member of this array so that you can then create a mapping for it and access the memory it represents.

IOService defines three methods you can use to get information about and access your device’s array of physical memory ranges:

- `getDeviceMemory`
- `getDeviceMemoryCount`
- `getDeviceMemoryWithIndex`

The `getDeviceMemory` method returns the array of IODeviceMemory objects that represent a device’s memory-mapped ranges. It is most likely that you will need to access specific members of this array using the other two methods, but a nub might call `getDeviceMemory` on its provider and use the returned array in its `start` method to set up a corresponding array of IODeviceMemory objects.

The `getDeviceMemoryCount` method returns the number of physical memory ranges available for a device; in effect, it returns a value you can use as an index into the IODeviceMemory array. As its name suggests, `getDeviceMemoryWithIndex` returns the IODeviceMemory object representing a memory-mapped range at the specified index.

In its `start` method, the AppleSamplePCI driver uses the `getDeviceMemoryCount` and `getDeviceMemoryWithIndex` methods to display all the device’s memory ranges, as shown in [Listing 3-9](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmojxfvbucq2cijdusri).

__Listing 3-9__  Using `getDeviceMemoryCount` and `getDeviceMemoryWithIndex`

```swift
bool AppleSamplePCI::start( IOService * provider )
{
    IOMemoryDescriptor * mem;
    /* Other code here */
    fPCIDevice = ( IOPCIDevice * ) provider;
    /* Use IOPCIDevice API to enable memory response from the device */
    fPCIDevice->setMemoryEnable( true );

    /* Use IOLog (defined in IOLib.h) to display the device's memory
        ranges. */
    for ( UInt32 index = 0;
        index < fPCIDevice->getDeviceMemoryCount();
        index++ ) {

        mem = fPCIDevice->getDeviceMemoryWithIndex( index );
        /* Use assert (defined in IOKit/assert.h) for debugging purposes */
        IOLog( "Range[%ld] %081x\n", index,
                mem->getPhysicalAddress(), mem->getLength() );
    }
    /* Work with a range based on the device's config BAR (base
     address register) here */
}
```

AppleSamplePCI’s `start` method uses an IOMemoryDescriptor object instead of an IODeviceMemory object to contain the object returned by `getDeviceMemoryWithIndex` because it uses IOMemoryDescriptor’s `getPhysicalAddress` and `getLength` methods.

IOService provides one device memory–mapping method, `mapDeviceMemoryWithIndex`, that maps a physical memory range of a device at the given index (passed in the first parameter). The second parameter of the `mapDeviceMemoryWithIndex` method contains the same options IOMemoryDescriptor’s `map` method uses (defined in `/System/Library/Frameworks/IOKit.framwork/Headers/IOTypes.h`), as shown in [Table 3-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmojxfvbucq2ii5cekrq):

__Table 3-3__  Memory-mapping options for `mapDeviceMemoryWithIndex`

| Option name | Description |
| `kIOMapAnywhere` | Create the mapping anywhere. |
| `kIOMapInhibitCache`, `kIOMapDefaultCache`, `kIOMapCopybackCache`, `kIOMapWriteThruCache` | Set the appropriate caching. |
| `kIOMapReadOnly` | Allow only read-only access to the mapped memory. |
| `kIOMapReference` | Create a new reference to a preexisting mapping. |

If you choose to specify a combination of these options, you use a variable of type `IOOptionsBits` and perform a logical `OR` on the options you want.

Further along in its `start` method, the ApplePCCardSample driver calls the `mapDeviceMemoryWithIndex` method on its nub, using the number of windows (or mappings) the nub has created as the index, as [Listing 3-10](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmojxfvbucq2jivbeori) shows.

__Listing 3-10__  Part of the ApplePCCardSample class declaration

```swift
/* From ApplePCCardSample class declaration: */
unsigned windowCount;
IOMemoryMap * windowMap[10];

/* Other initialization and configuration performed here. */
/* ... */
/* Find out how many windows we have configured. */
windowCount = nub->getWindowCount();

/* Map in the windows. */
for ( unsigned i = 0; i < windowCount; i++ ) {
    UInt32 attributes;
    if ( !nub->getWindowAttributes( i, &attributes ))
        /* Log error. */
    windowMap[i] = nub->mapDeviceMemoryWithIndex( i );
    if ( !windowMap[i] )
        /* Log error, call stop on provider, and return false from start. */
}
```


The vast majority of drivers should use the interrupt-handling facilities the IOInterruptEventSource class provides. The work-loop mechanism provides a safe, easy way to handle all types of asynchronous events, including interrupts.

For interrupt-controller or PCI device driver developers, however, IOService provides a handful of methods for low-level interrupt handling, outside the work-loop mechanism:

- `getInterruptType`
- `causeInterrupt`
- `disableInterrupt`
- `enableInterrupt`
- `registerInterrupt`
- `unregisterInterrupt`

The first task in implementing an interrupt controller is to determine which type of interrupt the device uses, edge-triggered or level-sensitive. Most PCI devices use level-sensitive interrupts by specification. The `getInterruptType` method is valid even before you register your interrupt handler so you can choose which handler to register based on the type of the interrupt. The implementation of IOInterruptEventSource does just this in its `init` method, as [Listing 3-11](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmojxfvbucq2gizduiqq) shows.

__Listing 3-11__  Determining interrupt type with `getInterruptType`

```swift
bool IOInterruptEventSource::init( OSObject *inOwner,
                                    Action inAction = 0,
                                    IOService *inProvider = 0,
                                    int inIntIndex = 0 )
{
    bool res = true;
    if ( !super::init( inOwner, ( IOEventSourceAction) inAction ) )
            return false;

    provider = inProvider;
    autoDisable = false;
    intIndex = -1;

    if ( inProvider ) {
        int intType;
        res = ( kIOReturnSuccess ==
            inProvider->getInterruptType( intIntIndex, &intType ) );
        if ( res ) {
            IOInterruptAction intHandler;
            autoDisable = ( intType == kIOInterruptTypeLevel );
            if ( autoDisable ) {
                intHandler = ( IOInterruptAction )
                    &IOInterruptEventSource::disableInterruptOccurred;
            }
            else
                intHandler = ( IOInterruptAction )
                    &IOInterruptEventSource::normalInterruptOccurred;

            res = ( kIOReturnSuccess == inProvider->registerInterrupt
                    ( inIntIndex, this, intHandler ) );
            if ( res )
                intIndex = inIntIndex;
        }
    }
    return res;
}
```

After you’ve determined which type of interrupt is valid for your device, you should register an interrupt handler for the device’s interrupt source. The `registerInterrupt` method requires an integer giving the index of the interrupt source in the device, a reference to the interrupt controller class (often the `this` pointer), a reference to the interrupt-handling routine, and an optional reference constant for the interrupt handler’s use. [Listing 3-11](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmojxfvbucq2gizduiqq) shows how IOInterruptEventSource registers the appropriate interrupt handler.

When you call `registerInterrupt` on an interrupt source, that interrupt source always starts disabled. It does not take interrupts until you enable it with the `enableInterrupt` method.

The `disableInterrupt` method disables the physical interrupt source, disabling it for all consumers of the interrupt if it is shared. You should call the `disableInterrupt` method sparingly and only for very short periods of time. If, for some reason, you need to disable an interrupt source for a longer time, you should instead use the `unregisterInterrupt` method to unregister the interrupt handler for a particular source and then reregister it later.

Internal services and top-level interrupt handlers sometimes use the `causeInterrupt` method to ensure that certain interrupts behave in an expected manner. Interrupt controllers are not required to implement this method so you should check before calling `causeInterrupt` to tickle your interrupt controller.

By using these methods instead of the IOInterruptEventSource and work-loop mechanism, you are responsible for keeping track of the state of your own interrupts. If, for example, your interrupt source is not registered, you must make sure that your device does not assert that interrupt, otherwise it could adversely affect other sources sharing that interrupt.

The remaining IOService methods do not fall neatly into any single, functional category. This section describes the following methods:

- `errnoFromReturn`
- `stringFromReturn`
- `callPlatformFunction`
- `lockForArbitration`
- `unlockForArbitration`

The `errnoFromReturn` and `stringFromReturn` methods are utilities that translate the error codes in `IOReturn.h` (available in `/System/Library/Frameworks/IOKit.framework/Headers`) into more usable formats. The `errnoFromReturn` method translates an `IOReturn` error code into the error codes BSD defines for its functions in `errno.h` (available in `/System/Library/Frameworks/Kernel.framework/Headers/sys`). The IOCDMediaBSDClient class, for example, uses `errnoFromReturn` to return a BSD error code when it encounters errors while processing an `ioctl` system call, as [Listing 3-12](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmojxfvbucq2jjjbuera) shows.

__Listing 3-12__  Using `errnoFromReturn`

```swift
int IOCDMediaBSDClient::ioctl ( dev_t dev, u_long cmd, caddr_t data,
                                int flags, struct proc * proc )
{
    /* Process a CD-specific ioctl. */
    int error = 0;

    switch ( cmd )
    {
        /* Switch cases not shown. */
    }
    return error ? error : getProvider()->errnoFromReturn ( status );
}
```

The `stringFromReturn` method translates the `IOReturn` error code into an easier-to-read string. For example, IOService translates the error code `kIOReturnLockedRead` into the string “device is read locked”.

You can override either `errnoFromReturn` or `stringFromReturn` to interpret family-dependent return codes or if you choose to support other `IOReturn` codes in addition to the ones IOService translates. If you do implement one of these methods, however, you should call the corresponding class in your superclass if you cannot translate the given error code.

The `callPlatformFunction` method is an internal method that routes requests to other I/O Registry objects or resources. There is no need for your driver to call this method.

The `lockForArbitration` and `unlockForArbitration` methods protect an IOService object from changes in its state or ownership. Most drivers do not need to use these methods because they get called when their state should change so they can then synchronize their internal state. Internally, IOService uses these methods extensively in its implementation of the driver life-cycle methods, such as `attach`, `detach`, `open`, and `close`.

Some I/O Kit families also use these methods to prevent changes in an IOService object’s state or ownership while accessing it. For example, [Listing 3-13](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmojxfvbucq2jineuery) shows a fragment of the IOBlockStorageDriver’s `mediaStateHasChanged` method, which determines a course of action based on a media’s new state.

__Listing 3-13__  Using `lockForArbitration` and `unlockForArbitration`

```
IOReturn IOBlockStorageDriver::mediaStateHasChanged( IOMediaState state )
{
    IOReturn result;
    /* Determine if media has been inserted or removed. */
    if ( state == kIOMediaStateOnline ) /* Media is now present. */
    {
        /* Allow a subclass to decide whether to accept or reject the
            media depending on tests like password protection. */
        /* ... */
        /* Get new media's parameters. */
        /* ... */
        /* Now make new media show in system. */
        lockForArbitration();
        result = acceptNewMedia(); /* Instantiate new media object */
                                 /* and attach to I/O Registry. */
        if ( result != kIOReturnSuccess )
        {
            /* Deal with error. */
        }
        unlockForArbitration();
        return ( result );
    }
    else { /* Deal with removed media. */
}
```

[Next](Making%20Hardware%20Accessible%20to%20Applications.md)[Previous](libkern%20Collection%20and%20Container%20Classes.md)

