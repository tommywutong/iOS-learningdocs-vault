---
title: Core Bluetooth Programming Guide
apple_id: TP40013257
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Networking, Internet, & Web
technology: CoreBluetooth
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternetWeb/Conceptual/CoreBluetooth_concepts/PerformingCommonCentralRoleTasks/PerformingCommonCentralRoleTasks.html
archived_at: '2026-07-18T01:33:56.147797Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Core Bluetooth Programming Guide](About%20Core%20Bluetooth.md)


[Next](Performing%20Common%20Peripheral%20Role%20Tasks.md)[Previous](Core%20Bluetooth%20Overview.md)

# Performing Common Central Role Tasks

Devices that implement the central role in Bluetooth low energy communication perform a number of common tasks—for example, discovering and connecting to available peripherals, and exploring and interacting with the data that peripherals have to offer. Devices that implement the peripheral role also perform a number of common, but different, tasks—for example, publishing and advertising services, and responding to read, write, and subscription requests from connected centrals.

In this chapter, you will learn how to use the Core Bluetooth framework to perform the most common types of Bluetooth low energy tasks from the central side. The code-based examples that follow will assist you in developing your app to implement the central role on your local device. Specifically, you will learn how to:

- Start up a central manager object
- Discover and connect to peripheral devices that are advertising
- Explore the data on a peripheral device after you’ve connected to it
- Send read and write requests to a characteristic value of a peripheral’s service
- Subscribe to a characteristic’s value to be notified when it is updated

In the next chapter, you will learn how to develop your app to implement the peripheral role on your local device.

The code examples that you find in this chapter are simple and abstract; you may need to make appropriate changes to incorporate them into your real world app. More advanced topics related to implementing the central role—including tips, tricks, and best practices—are covered in the later chapters, [Core Bluetooth Background Processing for iOS Apps](Core%20Bluetooth%20Background%20Processing%20for%20iOS%20Apps.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztenjxfvbuqnznknltc) and [Best Practices for Interacting with a Remote Peripheral Device](Best%20Practices%20for%20Interacting%20with%20a%20Remote%20Peripheral%20Device.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztenjxfvbuqnrnknltc).

Because a [CBCentralManager](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager) object is the Core Bluetooth object-oriented representation of a local central device, you allocate and initialize a central manager instance before you can perform any Bluetooth low energy transactions. You initialize your central manager by calling its [initWithDelegate:queue:options:](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1519001-init) method:

```
    myCentralManager =
        [[CBCentralManager alloc] initWithDelegate:self queue:nil options:nil];
```

In this example, `self` is set as the delegate to receive any central role events. By specifying the dispatch queue as `nil`, the central manager dispatches central role events using the main queue.

When you create a central manager, the central manager calls the [centralManagerDidUpdateState:](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate/1518888-centralmanagerdidupdatestate) method of its delegate object. You must implement this delegate method to ensure that Bluetooth low energy is supported and available to use on the central device. For more information about how to implement this delegate method, see _[CBCentralManagerDelegate Protocol Reference](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate)_.

Once initialized, the central manager’s first task is peripheral discovery. As mentioned in [Centrals Discover and Connect to Peripherals That Are Advertising](Core%20Bluetooth%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztenjxfvbuqmrnknltg), peripherals make their presence known by advertising. Your app discovers nearby peripheral devices that are advertising by calling the central manager’s [scanForPeripheralsWithServices:options:](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1518986-scanforperipheralswithservices) method:

```
    [myCentralManager scanForPeripheralsWithServices:nil options:nil];
```

Every time the central manager discovers a peripheral, it calls the [centralManager:didDiscoverPeripheral:advertisementData:RSSI:](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate/1518937-centralmanager) method of its delegate object. The newly discovered peripheral is returned as a [CBPeripheral](https://developer.apple.com/documentation/corebluetooth/cbperipheral) object. If you plan to connect to the discovered peripheral, keep a strong reference to it so the system does not deallocate it. The following example shows a scenario where you use a class property to maintain a reference to the discovered peripheral:

```objc
- (void)centralManager:(CBCentralManager *)central
 didDiscoverPeripheral:(CBPeripheral *)peripheral
     advertisementData:(NSDictionary *)advertisementData
                  RSSI:(NSNumber *)RSSI {

    NSLog(@"Discovered %@", peripheral.name);
    self.discoveredPeripheral = peripheral;
    ...
```

If you expect to connect to multiple devices, you might instead keep an `NSArray` of discovered peripherals. In any case, once you’ve found all the peripheral devices that you’re interested in connecting to, stop scanning for other devices in order to save power:

```
    [myCentralManager stopScan];
```


After you discover a peripheral device advertising services you are interested in, you request a connection to the peripheral by calling the central manager’s [connectPeripheral:options:](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1518766-connect) method, naming the discovered peripheral that you want to connect to:

```
    [myCentralManager connectPeripheral:peripheral options:nil];
```

If the connection request is successful, the central manager calls the [centralManager:didConnectPeripheral:](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate/1518969-centralmanager) method of its delegate object. Before you start interacting with the peripheral, you set its delegate to ensure that the delegate receives the appropriate callbacks:

```objc
- (void)centralManager:(CBCentralManager *)central
  didConnectPeripheral:(CBPeripheral *)peripheral {

    NSLog(@"Peripheral connected");
    peripheral.delegate = self;
    ...
```


After you have established a connection to a peripheral, you can explore its data. The first step in exploring what a peripheral has to offer is discovering its available services. Because there are size restrictions on the amount of data a peripheral can advertise, you may discover that a peripheral has more services than what it advertises (in its advertising packets). You can discover all of the services that a peripheral offers by calling the peripheral’s [discoverServices:](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518706-discoverservices) method, like this:

```
    [peripheral discoverServices:nil];
```

When the specified services are discovered, the peripheral (the [CBPeripheral](https://developer.apple.com/documentation/corebluetooth/cbperipheral) object you’re connected to) calls the [peripheral:didDiscoverServices:](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1518744-peripheral) method of its delegate object. Core Bluetooth creates an array of [CBService](https://developer.apple.com/documentation/corebluetooth/cbservice) objects—one for each service that is discovered on the peripheral. As the following shows, you can implement this delegate method to access the array of discovered services:

```objc
- (void)peripheral:(CBPeripheral *)peripheral
didDiscoverServices:(NSError *)error {

    for (CBService *service in peripheral.services) {
        NSLog(@"Discovered service %@", service);
        ...
    }
    ...
```


When you find a service that you are interested in, the next step in exploring what a peripheral has to offer is discovering all of the service’s characteristics. Discovering all of the characteristics of a service is as simple as calling the peripheral’s [discoverCharacteristics:forService:](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518797-discovercharacteristics) method, specifying the appropriate service, like this:

```
    NSLog(@"Discovering characteristics for service %@", interestingService);
    [peripheral discoverCharacteristics:nil forService:interestingService];
```

The peripheral calls the [peripheral:didDiscoverCharacteristicsForService:error:](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1518821-peripheral) method of its delegate object when the characteristics of the specified service are discovered. Core Bluetooth creates an array of [CBCharacteristic](https://developer.apple.com/documentation/corebluetooth/cbcharacteristic) objects—one for each characteristic that is discovered. The following example shows how you can implement this delegate method to simply log every characteristic that is discovered:

```objc
- (void)peripheral:(CBPeripheral *)peripheral
didDiscoverCharacteristicsForService:(CBService *)service
             error:(NSError *)error {

    for (CBCharacteristic *characteristic in service.characteristics) {
        NSLog(@"Discovered characteristic %@", characteristic);
        ...
    }
    ...
```


A characteristic contains a single value that represents information about a peripheral’s service. For example, a temperature measurement characteristic of a health thermometer service may have a value that indicates a temperature in Celsius. You can retrieve the value of a characteristic by reading it directly or by subscribing to it.

After you have found a characteristic of a service that you are interested in, you can read the characteristic’s value by calling the peripheral’s [readValueForCharacteristic:](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518759-readvalue) method, specifying the appropriate characteristic, like this:

```
    NSLog(@"Reading value for characteristic %@", interestingCharacteristic);
    [peripheral readValueForCharacteristic:interestingCharacteristic];
```

When you attempt to read the value of a characteristic, the peripheral calls the [peripheral:didUpdateValueForCharacteristic:error:](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1518708-peripheral) method of its delegate object to retrieve the value. If the value is successfully retrieved, you can access it through the characteristic’s value property, like this:

```objc
- (void)peripheral:(CBPeripheral *)peripheral
didUpdateValueForCharacteristic:(CBCharacteristic *)characteristic
             error:(NSError *)error {

    NSData *data = characteristic.value;
    // parse the data as needed
    ...
```


Though reading the value of a characteristic using the [readValueForCharacteristic:](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518759-readvalue) method can be effective for static values, it is not the most efficient way to retrieve a dynamic value. Retrieve characteristic values that change over time—for instance, your heart rate—by subscribing to them. When you subscribe to a characteristic’s value, you receive a notification from the peripheral when the value changes.

You subscribe to the value of a characteristic that you are interested in by calling the peripheral’s [setNotifyValue:forCharacteristic:](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518949-setnotifyvalue) method, specifying the first parameter as `YES`, like this:

```
    [peripheral setNotifyValue:YES forCharacteristic:interestingCharacteristic];
```

When you subscribe to (or unsubscribe from) a characteristic’s value, the peripheral calls the [peripheral:didUpdateNotificationStateForCharacteristic:error:](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1518768-peripheral) method of its delegate object. If the subscription request fails for any reason, you can implement this delegate method to access the cause of the error, as the following example shows:

```objc
- (void)peripheral:(CBPeripheral *)peripheral
didUpdateNotificationStateForCharacteristic:(CBCharacteristic *)characteristic
             error:(NSError *)error {

    if (error) {
        NSLog(@"Error changing notification state: %@",
           [error localizedDescription]);
    }
    ...
```

After you have successfully subscribed to a characteristic’s value, the peripheral device notifies your app when the value has changed. Each time the value changes, the peripheral calls the [peripheral:didUpdateValueForCharacteristic:error:](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1518708-peripheral) method of its delegate object. To retrieve the updated value, you can implement this method in the same way as described above in [Reading the Value of a Characteristic](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztenjxfvbuqmznknltcmq).

Sometimes it makes sense to write the value of a characteristic. For example, if your app interacts with a Bluetooth low energy digital thermostat, you may want to provide the thermostat with a value at which to set the room’s temperature. If a characteristic’s value is writeable, you can write its value with data (an instance of [NSData](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/cl/NSData)) by calling the peripheral’s [writeValue:forCharacteristic:type:](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518747-writevalue) method, like this:

```
    NSLog(@"Writing value for characteristic %@", interestingCharacteristic);
    [peripheral writeValue:dataToWrite forCharacteristic:interestingCharacteristic
        type:CBCharacteristicWriteWithResponse];
```

When you write the value of a characteristic, you specify what type of write you want to perform. In the example above, the write type is [CBCharacteristicWriteWithResponse](https://developer.apple.com/documentation/corebluetooth/cbcharacteristicwritetype/cbcharacteristicwritewithresponse), which instructs the peripheral to let your app know whether or not the write succeeds by calling the [peripheral:didWriteValueForCharacteristic:error:](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1518823-peripheral) method of its delegate object. You implement this delegate method to handle the error condition, as the following example shows:

```objc
- (void)peripheral:(CBPeripheral *)peripheral
didWriteValueForCharacteristic:(CBCharacteristic *)characteristic
             error:(NSError *)error {

    if (error) {
        NSLog(@"Error writing characteristic value: %@",
            [error localizedDescription]);
    }
    ...
```

If instead you specify the write type as [CBCharacteristicWriteWithoutResponse](https://developer.apple.com/documentation/corebluetooth/cbcharacteristicwritetype/withoutresponse), the write operation is performed as best-effort, and delivery is neither guaranteed nor reported. The peripheral does not call any delegate method. For more information about the write types that are supported in the Core Bluetooth framework, see the [CBCharacteristicWriteType](https://developer.apple.com/documentation/corebluetooth/cbcharacteristicwritetype) enumeration in _[CBPeripheral Class Reference](https://developer.apple.com/documentation/corebluetooth/cbperipheral)_.

[Next](Performing%20Common%20Peripheral%20Role%20Tasks.md)[Previous](Core%20Bluetooth%20Overview.md)

