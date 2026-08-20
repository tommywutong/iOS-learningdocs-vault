---
title: HomeKit Developer Guide
apple_id: TP40015050
resource_type: Guide
platform: watchOS|iOS
topic: null
technology: HomeKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/HomeKitDeveloperGuide/WritingtotheHomeKitDatabase/WritingtotheHomeKitDatabase.html
archived_at: '2026-07-27T06:57:09.426596Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [HomeKit Developer Guide](Introduction%20to%20HomeKit.md)


[Next](Observing%20HomeKit%20Database%20Changes.md)[Previous](Getting%20the%20Home%20Layout.md)

# Creating Homes and Adding Accessories

HomeKit objects are stored in a shared HomeKit database accessed by multiple apps through the HomeKit framework. All HomeKit method calls that write records are asynchronous and contain a completion handler parameter. If the method is successful, your app should update local objects in the completion handler. The app that initiates the change to HomeKit objects doesn’t receive delegate messages; the app only receives completion handler callbacks.

To observe changes to HomeKit objects initiated by other apps, read [Observing HomeKit Database Changes](Observing%20HomeKit%20Database%20Changes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tanjqfvbuqnjnknlte). For the error codes that may be passed to completion handlers of asynchronous messages, read _HomeKit Constants Reference_.

## Rules for Naming Objects

The names of HomeKit objects—such as home, room, and zone objects—are recognized by Siri where indicated in this document. The following rules apply to setting names of HomeKit objects:

- Names must be unique within their namespace.
- The names of homes belonging to a user are in one namespace.
- A home object and its containing objects are in another namespace.
- A name can contain only alphanumeric, space, and apostrophe characters.
- A name must start and end with an alphabetic or numeric character.
- Space and apostrophe characters are ignored in comparisons (for example, `home1` and `home 1` are the same).
- A name is not case-sensitive.

To learn about the language the user can use to interact with Siri, read “Siri Integration” in [HomeKit User Interface Guidelines](https://developer.apple.com/homekit/ui-guidelines/).

## Creating Homes

To add a home, use the [addHomeWithName:completionHandler:](https://developer.apple.com/documentation/homekit/hmhomemanager/1616747-addhome) asynchronous method in the [HMHomeManager](https://developer.apple.com/documentation/homekit/hmhomemanager) class. The home name, passed as a parameter to this method, must be unique. Home names are recognized by Siri.

```
    [self.homeManager addHomeWithName:@"My Home" completionHandler:^(HMHome *home, NSError *error) {
        if (error != nil) {
            // Failed to add a home
        } else {
            // Successfully added a home
        }
    }];
```

In the `else` clause, insert your code that updates the app’s views. To get the home manager, read [Getting the Home Manager Object](Getting%20the%20Home%20Layout.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tanjqfvbuqmznknlte).

## Adding a Room to a Home

To add a room to a home, use the [addRoomWithName:completionHandler:](https://developer.apple.com/documentation/homekit/hmhome/1620236-addroomwithname) asynchronous method. The room name, passed as a parameter to this method, must be unique within the home. Room names are recognized by Siri.

```
    NSString *roomName = @"Living Room";
    [home addRoomWithName:roomName completionHandler:^(HMRoom *room, NSError *error) {
        if (error != nil) {
            // Failed to add a room to a home
        } else {
            // Successfully added a room to a home
        }
    }];
```

In the `else` clause, insert your code that updates the app’s views.

## Discovering Accessories

Accessories encapsulate the state of a physical accessory and therefore cannot be created by the user. To allow users to add new accessories to their home, use an [HMAccessoryBrowser](https://developer.apple.com/documentation/homekit/hmaccessorybrowser) object to discover new accessories not yet associated with a home. The [HMAccessoryBrowser](https://developer.apple.com/documentation/homekit/hmaccessorybrowser) object searches for accessories in the background and uses delegation to notify your app when it finds new accessories. The [HMAccessoryBrowserDelegate](https://developer.apple.com/documentation/homekit/hmaccessorybrowserdelegate) messages are sent to the delegate only after the [startSearchingForNewAccessories](https://developer.apple.com/documentation/homekit/hmaccessorybrowser/1622405-startsearchingfornewaccessories) method is invoked and before the [stopSearchingForNewAccessories](https://developer.apple.com/documentation/homekit/hmaccessorybrowser/1622408-stopsearchingfornewaccessories) method is invoked.

__To discover accessories in a home__

1. Add the accessory browser delegate protocol, and add an accessory browser property to your class interface.

   ```objc
   @interface EditHomeViewController () <HMAccessoryBrowserDelegate>

   @property HMAccessoryBrowser *accessoryBrowser;

   @end
   ```

   Replace `EditHomeViewController` with your class name.
2. Create the accessory browser object, and set its delegate.

   ```
   self.accessoryBrowser = [[HMAccessoryBrowser alloc] init];
   self.accessoryBrowser.delegate = self;
   ```
3. Start searching for accessories.

   ```
   [self.accessoryBrowser startSearchingForNewAccessories];
   ```
4. Add found accessories to your collection.

   ```objc
   - (void)accessoryBrowser:(HMAccessoryBrowser *)browser didFindNewAccessory:(HMAccessory *)accessory {
       // Update the UI per the new accessory; for example, reload a picker view.
       [self.accessoryPicker reloadAllComponents];
   }
   ```

   Replace the above [accessoryBrowser:didFindNewAccessory:](https://developer.apple.com/documentation/homekit/hmaccessorybrowserdelegate/1622402-accessorybrowser) implementation with your code. Also, implement the [accessoryBrowser:didRemoveNewAccessory:](https://developer.apple.com/documentation/homekit/hmaccessorybrowserdelegate/1622407-accessorybrowser) method to remove an accessory that is no longer new from your collection or view.
5. Stop searching for accessories.

   If a view controller starts looking for accessories, override [viewWillDisappear:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621485-viewwilldisappear) to stop looking for accessories.

   ```objc
   - (void)viewWillDisappear:(BOOL)animated {
       [self.accessoryBrowser stopSearchingForNewAccessories];
   }
   ```

__Note:__ To get a new wireless accessory on the Wi-Fi network securely so it can be discovered by HomeKit, read _[External Accessory Framework Reference](https://developer.apple.com/documentation/externalaccessory)_.

## Adding Accessories to Homes and Rooms

Accessories belong to a home and optionally can be added to a room in a home. To add an accessory to a home, use the [addAccessory:completionHandler:](https://developer.apple.com/documentation/homekit/hmhome/1620216-addaccessory) asynchronous method. The accessory name, passed as a parameter to this method, must be unique within a home. To add an accessory to a room in a home, use the [assignAccessory:toRoom:completionHandler:](https://developer.apple.com/documentation/homekit/hmhome/1620265-assignaccessory) asynchronous method. The default room for an accessory is the room returned by the [roomForEntireHome](https://developer.apple.com/documentation/homekit/hmhome/1620227-roomforentirehome) method.

```
// Add an accesory to a home and a room
// 1. Get the home and room objects for the completion handlers.
__block HMHome *home = self.home;
__block HMRoom *room = roomInHome;

// 2. Add the accessory to the home
[home addAccessory:accessory completionHandler:^(NSError *error) {
    if (error) {
        // Failed to add accessory to home
    } else {
        if (accessory.room != room) {
            // 3. If successfully, add the accessory to the room
            [home assignAccessory:accessory toRoom:room completionHandler:^(NSError *error) {
                if (error) {
                    // Failed to add accessory to room
                }
            }];
        }
    }
}];
```

Accessories have one or more services, and services have characteristics defined by manufacturers. To get service and characteristic objects from an accessory, read [Accessing Services and Characteristics](Accessing%20Services%20and%20Characteristics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tanjqfvbuqnrnknltc).

## Changing Names of Accessories

To change the name of an accessory, use the [updateName:completionHandler:](https://developer.apple.com/documentation/homekit/hmaccessory/1615277-updatename) asynchronous method.

```
[accessory updateName:@"Kid's Night Light" completionHandler:^(NSError *error) {
    if (error) {
        // Failed to change the name
    } else {
        // Successfully changed the name
    }
}];
```

## Adding Bridges to Homes and Rooms

A bridge is a special type of accessory that allows you to communicate with accessories that can’t communicate directly with HomeKit. For example, a bridge might be a hub for multiple lights that use a communication protocol other than HomeKit Accessory Protocol. To add a bridge to a home, follow the steps for adding any other type of accessory to a home, as described in [Adding Accessories to Homes and Rooms](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tanjqfvbuqnbnknltk). When you add a bridge to a home, the accessories behind the bridge are also added to the home. Per the change notification design pattern, described in [Observing HomeKit Database Changes](Observing%20HomeKit%20Database%20Changes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tanjqfvbuqnjnknlte), the home’s delegate won’t receive a [home:didAddAccessory:](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620215-home) delegate message for the bridge, but will receive a [home:didAddAccessory:](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620215-home) delegate message for each accessory behind the bridge. Treat the accessories behind a bridge in the same way as any other accessory in a home—for example, add them to the list of configured accessories.

In contrast, when you add a bridge to a room, the accessories behind the bridge are not automatically added to the room because the bridge and its accessories can be located in different rooms.

## Creating Zones

A zone ([HMZone](https://developer.apple.com/documentation/homekit/hmzone)) is an arbitrary optional grouping of rooms; for example, upstairs, downstairs, or bedrooms. Rooms can be added to one or more zones.

（原归档配图获取待重试：`zones_2x.png`）

To create a zone, use the [addZoneWithName:completionHandler:](https://developer.apple.com/documentation/homekit/hmhome/1620212-addzone) asynchronous method. The name of the zone, passed as an argument to this method, must be unique within a home. Zone names are recognized by Siri.

```
__block HMHome *home = self.home;
NSString *zoneName = @"Upstairs";
[home addZoneWithName:zoneName completionHandler:^(HMZone *zone, NSError *error) {
    if (error) {
        // Failed to create zone
    } else {
        // Successfully created zone, now add the rooms
    }
}];
```

To add a room to a zone, use the [addRoom:completionHandler:](https://developer.apple.com/documentation/homekit/hmzone/1624764-addroom) asynchronous method.

```
__block HMRoom *room = roomInHome;
[zone addRoom:room completionHandler:^(NSError *error) {
    if (error) {
        // Failed to add room to zone
    } else {
        // Successfully added room to zone
    }
}];
```

[Next](Observing%20HomeKit%20Database%20Changes.md)[Previous](Getting%20the%20Home%20Layout.md)
