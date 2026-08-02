---
title: Core Bluetooth Programming Guide
apple_id: TP40013257
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Networking, Internet, & Web
technology: CoreBluetooth
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternetWeb/Conceptual/CoreBluetooth_concepts/PerformingCommonPeripheralRoleTasks/PerformingCommonPeripheralRoleTasks.html
archived_at: '2026-07-18T01:33:56.227679Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Core Bluetooth Programming Guide](About%20Core%20Bluetooth.md)


[Next](Core%20Bluetooth%20Background%20Processing%20for%20iOS%20Apps.md)[Previous](Performing%20Common%20Central%20Role%20Tasks.md)

# Performing Common Peripheral Role Tasks

In the last chapter, you learned how to perform the most common types of Bluetooth low energy tasks from the central side. In this chapter, you learn how to use the Core Bluetooth framework to perform the most common types of Bluetooth low energy tasks from the peripheral side. The code-based examples that follow will assist you in developing your app to implement the peripheral role on your local device. Specifically, you will learn how to:

- Start up a peripheral manager object
- Set up services and characteristics on your local peripheral
- Publish your services and characteristics to your device’s local database
- Advertise your services
- Respond to read and write requests from a connected central
- Send updated characteristic values to subscribed centrals

The code examples that you find in this chapter are simple and abstract; you may need to make appropriate changes to incorporate them into your real-world app. More advanced topics related to implementing the peripheral role on your local device—including tips, tricks, and best practices—are covered in the later chapters, [Core Bluetooth Background Processing for iOS Apps](Core%20Bluetooth%20Background%20Processing%20for%20iOS%20Apps.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztenjxfvbuqnznknltc) and [Best Practices for Setting Up Your Local Device as a Peripheral](Best%20Practices%20for%20Setting%20Up%20Your%20Local%20Device%20as%20a%20Peripheral.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztenjxfvbuqnjnknltc).

The first step in implementing the peripheral role on your local device is to allocate and initialize a peripheral manager instance (represented by a [CBPeripheralManager](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager) object). Start up your peripheral manager by calling the [initWithDelegate:queue:options:](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1393295-init) method of the [CBPeripheralManager](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager) class, like this:

```
    myPeripheralManager =
        [[CBPeripheralManager alloc] initWithDelegate:self queue:nil options:nil];
```

In this example, `self` is set as the delegate to receive any peripheral role events. When you specify the dispatch queue as `nil`, the peripheral manager dispatches peripheral role events using the main queue.

When you create a peripheral manager, the peripheral manager calls the [peripheralManagerDidUpdateState:](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/1393271-peripheralmanagerdidupdatestate) method of its delegate object. You must implement this delegate method to ensure that Bluetooth low energy is supported and available to use on the local peripheral device. For more information about how to implement this delegate method, see _[CBPeripheralManagerDelegate Protocol Reference](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate)_.

As shown in [Figure 1-7](Core%20Bluetooth%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztenjxfvbuqmrnknltcoa), a local peripheral’s database of services and characteristics is organized in a tree-like manner. You must organize them in this tree-like manner to set up your services and characteristics on your local peripheral. Your first step in carrying out these tasks is understanding how services and characteristics are identified.

The services and characteristics of a peripheral are identified by 128-bit Bluetooth-specific UUIDs, which are represented in the Core Bluetooth framework by [CBUUID](https://developer.apple.com/documentation/corebluetooth/cbuuid) objects. Though not all UUIDs that identify a service or characteristic are predefined by the Bluetooth Special Interest Group (SIG), Bluetooth SIG has defined and published a number of commonly used UUIDs that have been shortened to 16-bits for convenience. For example, Bluetooth SIG has predefined the 16-bit UUID that identifies a heart rate service as 180D. This UUID is shortened from its equivalent 128-bit UUID, 0000180D-0000-1000-8000-00805F9B34FB, which is based on the Bluetooth base UUID that is defined in the Bluetooth 4.0 specification, Volume 3, Part F, Section 3.2.1.

The [CBUUID](https://developer.apple.com/documentation/corebluetooth/cbuuid) class provides factory methods that make it much easier to deal with long UUIDs when developing your app. For example, instead of passing around the string representation of the heart rate service’s 128-bit UUID in your code, you can simply use the `UUIDWithString` method to create a [CBUUID](https://developer.apple.com/documentation/corebluetooth/cbuuid) object from the service’s predefined 16-bit UUID, like this:

```
    CBUUID *heartRateServiceUUID = [CBUUID UUIDWithString: @"180D"];
```

When you create a [CBUUID](https://developer.apple.com/documentation/corebluetooth/cbuuid) object from a predefined 16-bit UUID, Core Bluetooth pre-fills the rest of 128-bit UUID with the Bluetooth base UUID.

You may have services and characteristics that are not identified by predefined Bluetooth UUIDs. If you do, you need to generate your own 128-bit UUIDs to identify them.

Use the command-line utility `uuidgen` to easily generate 128-bit UUIDs. To get started, open a window in Terminal. Next, for each service and characteristic that you need to identify with a UUID, type `uuidgen` on the command line to receive a unique 128-bit value in the form of an ASCII string that is punctuated by hyphens, as in the following example:

```
$ uuidgen
71DA3FD1-7E10-41C1-B16F-4430B506CDE7
```

You can then use this UUID to create a [CBUUID](https://developer.apple.com/documentation/corebluetooth/cbuuid) object using the `UUIDWithString` method, like this:

```
    CBUUID *myCustomServiceUUID =
        [CBUUID UUIDWithString:@"71DA3FD1-7E10-41C1-B16F-4430B506CDE7"];
```


After you have the UUIDs of your services and characteristics (represented by [CBUUID](https://developer.apple.com/documentation/corebluetooth/cbuuid) objects), you can create mutable services and characteristics and organize them in the tree-like manner described above. For example, if you have the UUID of a characteristic, you can create a mutable characteristic by calling the [initWithType:properties:value:permissions:](https://developer.apple.com/documentation/corebluetooth/cbmutablecharacteristic/1519073-init) method of the [CBMutableCharacteristic](https://developer.apple.com/documentation/corebluetooth/cbmutablecharacteristic) class, like this:

```
    myCharacteristic =
        [[CBMutableCharacteristic alloc] initWithType:myCharacteristicUUID
         properties:CBCharacteristicPropertyRead
         value:myValue permissions:CBAttributePermissionsReadable];
```

When you create a mutable characteristic, you set its properties, value, and permissions. The properties and permissions you set determine, among other things, whether the value of the characteristic is readable or writeable, and whether a connected central can subscribe to the characteristic’s value. In this example, the value of the characteristic is set to be readable by a connected central. For more information about the range of supported properties and permissions of mutable characteristics, see _[CBMutableCharacteristic Class Reference](https://developer.apple.com/documentation/corebluetooth/cbmutablecharacteristic)_.

Now that you have created a mutable characteristic, you can create a mutable service to associate the characteristic with. To do so, call the [initWithType:primary:](https://developer.apple.com/documentation/corebluetooth/cbmutableservice/1434330-init) method of the [CBMutableService](https://developer.apple.com/documentation/corebluetooth/cbmutableservice) class, as shown here:

```
    myService = [[CBMutableService alloc] initWithType:myServiceUUID primary:YES];
```

In this example, the second parameter is set to `YES`, indicating that the service is primary as opposed to secondary. A _primary service_ describes the primary functionality of a device and can be included (referenced) by another service. A _secondary service_ describes a service that is relevant only in the context of another service that has referenced it. For example, the primary service of a heart rate monitor may be to expose heart rate data from the monitor’s heart rate sensor, whereas a secondary service may be to expose the sensor’s battery data.

After you create a service, you can associate the characteristic with it by setting the service’s array of characteristics, like this:

```
    myService.characteristics = @[myCharacteristic];
```


After you have built your tree of services and characteristics, the next step in implementing the peripheral role on your local device is publishing them to the device’s database of services and characteristics. This task is easy to perform using the Core Bluetooth framework. You call the [addService:](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1393255-add) method of the [CBPeripheralManager](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager) class, like this:

```
    [myPeripheralManager addService:myService];
```

When you call this method to publish your services, the peripheral manager calls the [peripheralManager:didAddService:error:](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/1393279-peripheralmanager) method of its delegate object. If an error occurs and your services can’t be published, implement this delegate method to access the cause of the error, as the following example shows:

```objc
- (void)peripheralManager:(CBPeripheralManager *)peripheral
            didAddService:(CBService *)service
                    error:(NSError *)error {

    if (error) {
        NSLog(@"Error publishing service: %@", [error localizedDescription]);
    }
    ...
```


When you have published your services and characteristics to your device’s database of services and characteristics, you are ready to start advertising some of them to any centrals that may be listening. As the following example shows, you can advertise some of your services by calling the [startAdvertising:](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1393252-startadvertising) method of the [CBPeripheralManager](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager) class, passing in a dictionary (an instance of [NSDictionary](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/cl/NSDictionary)) of advertisement data:

```
    [myPeripheralManager startAdvertising:@{ CBAdvertisementDataServiceUUIDsKey :
        @[myFirstService.UUID, mySecondService.UUID] }];
```

In this example, the only key in the dictionary, [CBAdvertisementDataServiceUUIDsKey](https://developer.apple.com/documentation/corebluetooth/cbadvertisementdataserviceuuidskey), expects as a value an array (an instance of [NSArray](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/cl/NSArray)) of [CBUUID](https://developer.apple.com/documentation/corebluetooth/cbuuid) objects that represent the UUIDs of the services you want to advertise. The possible keys that you may specify in a dictionary of advertisement data are detailed in the constants described in `Advertisement Data Retrieval Keys` in _[CBCentralManagerDelegate Protocol Reference](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate)_. That said, only two of the keys are supported for peripheral manager objects: [CBAdvertisementDataLocalNameKey](https://developer.apple.com/documentation/corebluetooth/cbadvertisementdatalocalnamekey) and [CBAdvertisementDataServiceUUIDsKey](https://developer.apple.com/documentation/corebluetooth/cbadvertisementdataserviceuuidskey).

When you start advertising some of the data on your local peripheral, the peripheral manager calls the [peripheralManagerDidStartAdvertising:error:](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/1393321-peripheralmanagerdidstartadverti) method of its delegate object. If an error occurs and your services can’t be advertised, implement this delegate method to access the cause of the error, like this:

```objc
- (void)peripheralManagerDidStartAdvertising:(CBPeripheralManager *)peripheral
                                       error:(NSError *)error {

    if (error) {
        NSLog(@"Error advertising: %@", [error localizedDescription]);
    }
    ...
```

Once you begin advertising data, remote centrals can discover and initiate a connection with you.

After you are connected to one or more remote centrals, you may begin receiving read or write requests from them. When you do, be sure to respond to those requests in an appropriate manner. The following examples describe how to handle such requests.

When a connected central requests to read the value of one of your characteristics, the peripheral manager calls the [peripheralManager:didReceiveReadRequest:](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/1393257-peripheralmanager) method of its delegate object. The delegate method delivers the request to you in the form of a [CBATTRequest](https://developer.apple.com/documentation/corebluetooth/cbattrequest) object, which has a number of properties that you can use to fulfill the request.

For example, when you receive a simple request to read the value of a characteristic, the properties of the [CBATTRequest](https://developer.apple.com/documentation/corebluetooth/cbattrequest) object you receive from the delegate method can be used to make sure that the characteristic in your device’s database matches the one that the remote central specified in the original read request. You can begin to implement this delegate method, like this:

```objc
- (void)peripheralManager:(CBPeripheralManager *)peripheral
    didReceiveReadRequest:(CBATTRequest *)request {

    if ([request.characteristic.UUID isEqual:myCharacteristic.UUID]) {
        ...
```

If the characteristics’ UUIDs match, the next step is to make sure that the read request isn’t asking to read from an index position that is outside the bounds of your characteristic’s value. As the following example shows, you can use a [CBATTRequest](https://developer.apple.com/documentation/corebluetooth/cbattrequest) object’s [offset](https://developer.apple.com/documentation/corebluetooth/cbattrequest/1518857-offset) property to ensure the read request isn’t attempting to read outside the proper bounds:

```
    if (request.offset > myCharacteristic.value.length) {
        [myPeripheralManager respondToRequest:request
            withResult:CBATTErrorInvalidOffset];
        return;
    }
```

Assuming the request’s offset is verified, now set the value of the request’s characteristic property (whose value by default is `nil`) to the value of the characteristic you created on your local peripheral, taking into account the offset of the read request:

```
    request.value = [myCharacteristic.value
        subdataWithRange:NSMakeRange(request.offset,
        myCharacteristic.value.length - request.offset)];
```

After you set the value, respond to the remote central to indicate that the request was successfully fulfilled. Do so by calling the [respondToRequest:withResult:](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1393293-respond) method of the [CBPeripheralManager](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager) class, passing back the request (whose value you updated) and the result of the request, like this:

```
    [myPeripheralManager respondToRequest:request withResult:CBATTErrorSuccess];
    ...
```

Call the [respondToRequest:withResult:](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1393293-respond) method exactly once each time the [peripheralManager:didReceiveReadRequest:](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/1393257-peripheralmanager) delegate method is called.

Handling write requests from a connected central is also straightforward. When a connected central sends a request to write the value of one or more of your characteristics, the peripheral manager calls the [peripheralManager:didReceiveWriteRequests:](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/1393315-peripheralmanager) method of its delegate object. This time, the delegate method delivers the requests to you in the form of an array containing one or more [CBATTRequest](https://developer.apple.com/documentation/corebluetooth/cbattrequest) objects, each representing a write request. After you have ensured that a write request can be fulfilled, you can write the characteristic’s value, like this:

```
    myCharacteristic.value = request.value;
```

Although the above example does not demonstrate this, be sure to take into account the request’s offset property when writing the value of your characteristic.

Just as you respond to a read request, call the [respondToRequest:withResult:](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1393293-respond) method exactly once each time the [peripheralManager:didReceiveWriteRequests:](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/1393315-peripheralmanager) delegate method is called. That said, the first parameter of the [respondToRequest:withResult:](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1393293-respond) method expects a single [CBATTRequest](https://developer.apple.com/documentation/corebluetooth/cbattrequest) object, even though you may have received an array containing more than one of them from the [peripheralManager:didReceiveWriteRequests:](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/1393315-peripheralmanager) delegate method. You should pass in the first request of the array, like this:

```
    [myPeripheralManager respondToRequest:[requests objectAtIndex:0]
        withResult:CBATTErrorSuccess];
```


Often, connected centrals will subscribe to one or more of your characteristic values, as described in [Subscribing to a Characteristic’s Value](Performing%20Common%20Central%20Role%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztenjxfvbuqmznknltcnq). When they do, you are responsible for sending them notifications when the value of characteristic they subscribed to changes. The following examples describe how.

When a connected central subscribes to the value of one of your characteristics, the peripheral manager calls the [peripheralManager:central:didSubscribeToCharacteristic:](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/1393261-peripheralmanager) method of its delegate object:

```objc
- (void)peripheralManager:(CBPeripheralManager *)peripheral
                  central:(CBCentral *)central
didSubscribeToCharacteristic:(CBCharacteristic *)characteristic {

    NSLog(@"Central subscribed to characteristic %@", characteristic);
    ...
```

Use the above delegate method as a cue to start sending the central updated values.

Next, get the updated value of the characteristic and send it to the central by calling the [updateValue:forCharacteristic:onSubscribedCentrals:](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1393281-updatevalue) method of the [CBPeripheralManager](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager) class.

```
    NSData *updatedValue = // fetch the characteristic's new value
    BOOL didSendValue = [myPeripheralManager updateValue:updatedValue
        forCharacteristic:characteristic onSubscribedCentrals:nil];
```

When you call this method to send updated characteristic values to subscribed centrals, you can specify which centrals you want to update in the last parameter. As in the above example, if you specify `nil`, all connected and subscribed centrals are updated (and any connected centrals that have not subscribed are ignored).

The [updateValue:forCharacteristic:onSubscribedCentrals:](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1393281-updatevalue) method returns a Boolean value that indicates whether the update was successfully sent to the subscribed centrals. If the underlying queue that is used to transmit the updated value is full, the method returns `NO`. The peripheral manager then calls the [peripheralManagerIsReadyToUpdateSubscribers:](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/1393248-peripheralmanagerisreadytoupdate) method of its delegate object when more space in the transmit queue becomes available. You can then implement this delegate method to resend the value, again using the [updateValue:forCharacteristic:onSubscribedCentrals:](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1393281-updatevalue) method.

[Next](Core%20Bluetooth%20Background%20Processing%20for%20iOS%20Apps.md)[Previous](Performing%20Common%20Central%20Role%20Tasks.md)

