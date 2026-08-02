---
title: HomeKit Developer Guide
apple_id: TP40015050
resource_type: Guide
platform: watchOS|iOS
topic: null
technology: HomeKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/HomeKitDeveloperGuide/FindingandAddingAccessories/FindingandAddingAccessories.html
archived_at: '2026-07-27T06:57:09.409404Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [HomeKit Developer Guide](Introduction%20to%20HomeKit.md)


[Next](Creating%20Homes%20and%20Adding%20Accessories.md)[Previous](Enabling%20HomeKit.md)

# Getting the Home Layout

HomeKit allows users to create a layout for one or more of their homes. A home ([HMHome](https://developer.apple.com/documentation/homekit/hmhome)) represents a single dwelling that has a network of accessories. A home’s data is owned by the user and can be accessed from any of the user’s iOS devices. A user can also share a home with a guest who has more limited access. One home is designated as the primary home and is the default home for Siri commands that don’t specify a home.

Each home may have multiple rooms and accessories added to each room. A room ([HMRoom](https://developer.apple.com/documentation/homekit/hmroom)) represents an individual room in the home. It has a meaningful name, such as “living room” or “kitchen," which can be used in Siri commands. An accessory ([HMAccessory](https://developer.apple.com/documentation/homekit/hmaccessory)) is a physical home automation device, such as a garage door opener. A service ([HMService](https://developer.apple.com/documentation/homekit/hmservice)) is an actual service provided by an accessory, such as opening and closing a garage door or the light on the garage door opener.

（原归档配图获取待重试：`homes_2x.png`）

If your app caches information about a home’s layout, it needs to update that information when the home layout changes. Use a [HMHomeManager](https://developer.apple.com/documentation/homekit/hmhomemanager) object to fetch [HMHome](https://developer.apple.com/documentation/homekit/hmhome) and related objects from the HomeKit database. After fetching objects using the APIs described in this chapter, keep your objects synchronized with the database through delegate callbacks, as described in [Observing HomeKit Database Changes](Observing%20HomeKit%20Database%20Changes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tanjqfvbuqnjnknlte).

## Getting the Home Manager Object

Use the home manager, an [HMHomeManager](https://developer.apple.com/documentation/homekit/hmhomemanager) object, to access home, room, accessory, service, and other HomeKit objects. Immediately after creating the home manager, set its delegate so that you are notified when the initial fetch of these objects is complete.

```
self.homeManager = [[HMHomeManager alloc] init];
self.homeManager.delegate = self;
```

When you create a home manager object, HomeKit begins fetching the homes and associated objects—for example, room and accessory objects—from the HomeKit database. While HomeKit is fetching these objects, the value for the home manager [primaryHome](https://developer.apple.com/documentation/homekit/hmhomemanager/1616745-primaryhome) property is `nil`, and [homes](https://developer.apple.com/documentation/homekit/hmhomemanager/1616751-homes) property is an empty array. Your app should handle the case in which the user hasn’t created a home yet, but the app should not behave as if there are no homes until HomeKit completes the initial fetch. HomeKit sends the [homeManagerDidUpdateHomes:](https://developer.apple.com/documentation/homekit/hmhomemanagerdelegate/1616756-homemanagerdidupdatehomes) message to the home manager’s delegate when the fetch is complete.

__Note:__ The [homeManagerDidUpdateHomes:](https://developer.apple.com/documentation/homekit/hmhomemanagerdelegate/1616756-homemanagerdidupdatehomes) method is also invoked when the app comes to the foreground and changes occurred while it was in the background, as described in [Observing Changes to the Collection of Homes](Observing%20HomeKit%20Database%20Changes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tanjqfvbuqnjnknltg).

## Getting the Primary Home and Collection of Homes

To get the primary home, use the [primaryHome](https://developer.apple.com/documentation/homekit/hmhomemanager/1616745-primaryhome) property of the home manager.

```
HMHome *home = self.homeManager.primaryHome;
```

Use the home manager [homes](https://developer.apple.com/documentation/homekit/hmhomemanager/1616751-homes) property to get all of the user’s homes; for example, a primary residence, a vacation home, and an office. Each home is represented by a separate home object.

```
HMHome *home;
for (home in self.homeManager.homes){
    …
}
```

## Getting the Rooms in a Home

Rooms define physical locations of accessories within a home. To enumerate the rooms in a home, use the home’s [rooms](https://developer.apple.com/documentation/homekit/hmhome/1620276-rooms) property.

```
HMHome *home = self.homeManager.primaryHome;
HMRoom *room;
for (room in home.rooms){
    …
}
```

## Getting the Accessories in a Room

Accessories belong to a home but are assigned to a room in a home. If the user doesn’t assign an accessory to a room, the accessory is assigned to the default room returned by the [roomForEntireHome](https://developer.apple.com/documentation/homekit/hmhome/1620227-roomforentirehome) method. To enumerate the accessories in a room, use the room’s [accessories](https://developer.apple.com/documentation/homekit/hmroom/1618288-accessories) property.

```
HMAccessory *accessory;
for (accessory in room.accessories){
    …
}
```

If you display information about an accessory or allow the user to control an accessory, set the accessory’s delegate and implement accessory delegate methods, as described in [Observing Changes to Accessories](Observing%20HomeKit%20Database%20Changes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tanjqfvbuqnjnknltc).

Once you have an accessory object, you can access its services and their characteristics, as described in [Accessing Services and Characteristics](Accessing%20Services%20and%20Characteristics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tanjqfvbuqnrnknltc).

## Getting Accessories in a Home

To get all accessories directly from the home object without enumerating rooms in a home (as described in [Getting the Accessories in a Room](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tanjqfvbuqmznknltk)), use the [accessories](https://developer.apple.com/documentation/homekit/hmhome/1620275-accessories) method in the [HMHome](https://developer.apple.com/documentation/homekit/hmhome) class.

[Next](Creating%20Homes%20and%20Adding%20Accessories.md)[Previous](Enabling%20HomeKit.md)
