---
title: HomeKit Developer Guide
apple_id: TP40015050
resource_type: Guide
platform: watchOS|iOS
topic: null
technology: HomeKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/HomeKitDeveloperGuide/AccessingServicesandTheirCharacteristics/AccessingServicesandTheirCharacteristics.html
archived_at: '2026-07-27T06:57:09.451196Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [HomeKit Developer Guide](Introduction%20to%20HomeKit.md)


[Next](Testing%20Your%20HomeKit%20App.md)[Previous](Observing%20HomeKit%20Database%20Changes.md)

# Accessing Services and Characteristics

A service ([HMService](https://developer.apple.com/documentation/homekit/hmservice)) represents a function of an accessory and encapsulates characteristics ([HMCharacteristic](https://developer.apple.com/documentation/homekit/hmcharacteristic)) that have read-write properties. An accessory can have multiple services, and a service can have multiple characteristics. For example, a garage opener accessory may have a light and switch service. The light service may have on/off and dimmer characteristics. Users don’t create accessories and their services—the manufacturer defines the functions of an accessory—but users may change the values of service characteristics. Some characteristics represent a physical state that has read and write properties—for example, the current temperature of a thermostat is read-only, but the target temperature is read-write. Apple provides predefined service and characteristic names that are recognized and understood by Siri.

## Getting Services and Their Properties

After you get an accessory object, as described in [Getting the Accessories in a Room](Getting%20the%20Home%20Layout.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tanjqfvbuqmznknltk), you can obtain information about its services and their characteristics. You can also get services by type directly from the home.

__Important:__ Don’t expose an unnamed service—such as a firmware update service—to the user.

To get the services of an accessory, use the [services](https://developer.apple.com/documentation/homekit/hmaccessory/1615250-services) property in the [HMAccessory](https://developer.apple.com/documentation/homekit/hmaccessory) class.

```
NSArray *services = accessory.services;
```

To get services provided by accessories in a home that match specified types, use the [servicesWithTypes:](https://developer.apple.com/documentation/homekit/hmhome/1620235-serviceswithtypes) method in the [HMHome](https://developer.apple.com/documentation/homekit/hmhome) class.

```
// Get all lights and thermostats in a home
NSArray *lightServices = [home servicesWithTypes:[HMServiceTypeLightbulb]];
NSArray *thermostatServices = [home servicesWithTypes:[HMServiceTypeThermostat]];
```

To get the name of a service, use the [name](https://developer.apple.com/documentation/homekit/hmservice/1615888-name) property in the [HMService](https://developer.apple.com/documentation/homekit/hmservice) class.

```
NSString *name = service.name;
```

To get the characteristics of a service, use the [characteristics](https://developer.apple.com/documentation/homekit/hmservice/1615893-characteristics) property.

```
NSArray *characteristics = service.characteristics;
```

To get the type of service, use the [serviceType](https://developer.apple.com/documentation/homekit/hmservice/1615885-servicetype) property.

```
NSString *serviceType = service.serviceType;
```

Apple-defined service types that are recognized by Siri include:

- Door locks
- Fans
- Garage door openers
- Lights
- Outlets
- Thermostats

## Changing Names of Services

To change the name of a service, use the [updateName:completionHandler:](https://developer.apple.com/documentation/homekit/hmservice/1615887-updatename) asynchronous method. The service name, passed as a parameter to this method, must be unique within a home. Service names are recognized by Siri.

```
[service updateName:@"Garage 1 Opener" completionHandler:^(NSError *error) {
    if (error) {
        // Failed to change the name
    } else {
        // Successfully changed the name
    }
}];
```

## Accessing Values of Characteristics

A characteristic represents a parameter of a service that is either read-only, read-write, or write-only. It provides information about the possible values of the parameter, for example, a Boolean or range. The temperature of a thermostat is read-only, and the target temperature is read-write. A command that performs an action but requires no feedback—such as playing a sound or flashing a light to confirm the identity of an accessory—may be write-only.

Apple-defined characteristic types that are recognized by Siri include:

- Brightness
- Current door state
- Current temperature
- Lock state
- Power state
- Rotation speed
- Rotation direction
- Target door state
- Target state
- Target temperature

For example, the target state for a garage door opener is open or closed. The target state for a door lock is locked or unlocked.

After you get an [HMService](https://developer.apple.com/documentation/homekit/hmservice) object, as described in [Getting Services and Their Properties](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tanjqfvbuqnrnknlte), you can access the values of the individual service characteristics. Because the values are obtained from the physical accessory, these read and write methods are asynchronous with completion handler parameters.

To read the value of a characteristic, use the [readValueWithCompletionHandler:](https://developer.apple.com/documentation/homekit/hmcharacteristic/1624188-readvaluewithcompletionhandler) asynchronous method.

```
[characteristic readValueWithCompletionHandler:^(NSError *error) {
    if (error == nil) {
       // Successfully read the value
       id value = characteristic.value;
    }
    else {
       // Unable to read the value
    }
}];
```

In the `if` clause, insert your code that updates the app’s views.

To write the value of a characteristic, use the [writeValue:completionHandler:](https://developer.apple.com/documentation/homekit/hmcharacteristic/1624191-writevalue) asynchronous method.

```
[self.characteristic writeValue:@42 withCompletionHandler:^(NSError *error) {
    if (error == nil) {
       // Successfully wrote the value
    }
    else {
       // Unable to write the value
    }
}];
```

Don’t assume the write method is successful until the completion handler is called with no error. For example, don’t change the state of a switch until the characteristic it represents changes state. In the `if` clause, insert your code that updates the app’s views.

In addition, update views when other apps change the values of characteristics, as described in [Observing Changes to Accessories](Observing%20HomeKit%20Database%20Changes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tanjqfvbuqnjnknltc).

## Creating Service Groups

A service group ([HMServiceGroup](https://developer.apple.com/documentation/homekit/hmservicegroup)) provides a convenient way to control arbitrary services belonging to different accessories—for example, controlling a subset of lights in the home when the user is away.

（原归档配图获取待重试：`servicegroups_2x.png`）

After you get a [HMHome](https://developer.apple.com/documentation/homekit/hmhome) object, as described in [Getting the Primary Home and Collection of Homes](Getting%20the%20Home%20Layout.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tanjqfvbuqmznknltg), you can create a service group within that home.

To create a service group, use the [addServiceGroupWithName:completionHandler:](https://developer.apple.com/documentation/homekit/hmhome/1620269-addservicegroupwithname) method in the [HMHome](https://developer.apple.com/documentation/homekit/hmhome) class. The service group name, a parameter to this method, must be unique within a home. Service group names are recognized by Siri.

```
[self.home addServiceGroupWithName:@"Away Lights" completionHandler:^(HMServiceGroup *serviceGroup, NSError *error) {
    if (error == nil) {
       // Successfully created the service group
    }
    else {
       // Unable to create the service group
    }];
```

To add a service to a service group, use the [addService:completionHandler:](https://developer.apple.com/documentation/homekit/hmservicegroup/1616997-addservice) method in the [HMServiceGroup](https://developer.apple.com/documentation/homekit/hmservicegroup) class. Services can be in one or more service groups.

```
[serviceGroup addService:service completionHandler:^(NSError *error) {
    if (error == nil) {
       // Successfully added service to service group
    }
       // Unable to add the service to the service group
    }];
```

To get service groups for a home, use the [serviceGroups](https://developer.apple.com/documentation/homekit/hmhome/1620266-servicegroups) property in the [HMHome](https://developer.apple.com/documentation/homekit/hmhome) class.

```
NSArray *serviceGroups = self.home.serviceGroups;
```

To get the accessory for a service, use the [accessory](https://developer.apple.com/documentation/homekit/hmservice/1615884-accessory) property in the [HMServiceGroup](https://developer.apple.com/documentation/homekit/hmservicegroup) class.

```
HMAccessory *accessory = service.accessory;
```

Similar to accessories, delegate methods are invoked when other apps change service groups. If your app uses service groups, read _[HMHomeDelegate Protocol Reference](https://developer.apple.com/documentation/homekit/hmhomedelegate)_ for the methods you should implement to observe these changes.

[Next](Testing%20Your%20HomeKit%20App.md)[Previous](Observing%20HomeKit%20Database%20Changes.md)
