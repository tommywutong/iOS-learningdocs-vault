---
title: HomeKit Developer Guide
apple_id: TP40015050
resource_type: Guide
platform: watchOS|iOS
topic: null
technology: HomeKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/HomeKitDeveloperGuide/RespondingtoHomeKitDatabaseChanges/RespondingtoHomeKitDatabaseChanges.html
archived_at: '2026-07-27T06:57:09.437814Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [HomeKit Developer Guide](Introduction%20to%20HomeKit.md)


[Next](Accessing%20Services%20and%20Characteristics.md)[Previous](Creating%20Homes%20and%20Adding%20Accessories.md)

# Observing HomeKit Database Changes

There is one HomeKit database per home. As shown in the figure below, the database is securely synchronized with a user’s iOS devices and potentially with guest user iOS devices that are granted access to the home. In order to show the most current data to the user, your app needs to observe changes to this database.

（原归档配图获取待重试：`architecture_2x.png`）

## About HomeKit Delegation Methods

HomeKit uses the [delegation design pattern](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14-SW2) to notify your app of changes to HomeKit objects. In general, if your app invokes a HomeKit method with a completion handler parameter and the method is successful, the associated delegate message is sent to other HomeKit apps running on the same or remote iOS devices. The apps can even be run by guest users on their iOS devices. If your app initiates the change, the delegate message is not sent to your app. Therefore, add code to both the completion handler and the associated delegate method to reload data and update views as needed. If a home layout changes significantly, reload all the information about that home. In the case of the completion handler, check whether the method is successful before updating the app. HomeKit also invokes delegate methods to notify your app of changes to the state of the home network.

For example, if (1) in response to a user action, (2) your app invokes [addRoomWithName:completionHandler:](https://developer.apple.com/documentation/homekit/hmhome/1620236-addroomwithname) and no error occurs, (3) the completion handler should (4) update the views of the home. If successful, HomeKit (5) sends the [home:didAddRoom:](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620244-home) message to delegates of the home in other apps. Therefore, your implementation of the [home:didAddRoom:](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620244-home) method should also (6) update the views of the home.

（原归档配图获取待重试：`changeflow_2x.png`）

The apps need to be in the foreground to receive these delegate messages. Changes are not batched while your app is in the background. If your app is in the background while another app successfully adds a room to a home, your app doesn’t receive a [home:didAddRoom:](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620244-home) message. When your app comes to the foreground, your app receives a [homeManagerDidUpdateHomes:](https://developer.apple.com/documentation/homekit/hmhomemanagerdelegate/1616756-homemanagerdidupdatehomes) message, which signals your app to reload all its data.

## Observing Changes to the Collection of Homes

To receive delegate messages when the primary home or collection of homes changes, set the home manager’s delegate and implement the [HMHomeManagerDelegate](https://developer.apple.com/documentation/homekit/hmhomemanagerdelegate) protocol.

All apps need to implement the [homeManagerDidUpdateHomes:](https://developer.apple.com/documentation/homekit/hmhomemanagerdelegate/1616756-homemanagerdidupdatehomes) method, which is invoked after HomeKit finishes the initial fetch of homes. Until this method is invoked, for a newly created home manager, the [primaryHome](https://developer.apple.com/documentation/homekit/hmhomemanager/1616745-primaryhome) property is `nil` and the [homes](https://developer.apple.com/documentation/homekit/hmhomemanager/1616751-homes) property is an empty array. The [homeManagerDidUpdateHomes:](https://developer.apple.com/documentation/homekit/hmhomemanagerdelegate/1616756-homemanagerdidupdatehomes) method is also invoked when the app comes to the foreground, and changes occurred while it was in the background. The [homeManagerDidUpdateHomes:](https://developer.apple.com/documentation/homekit/hmhomemanagerdelegate/1616756-homemanagerdidupdatehomes) method should reload all data associated with the homes.

__To observe changes to homes__

1. Add the home manager delegate protocol and home manager property to your class interface.

   ```objc
   @interface AppDelegate () <HMHomeManagerDelegate>

   @property (strong, nonatomic) HMHomeManager *homeManager;

   @end
   ```
2. Create the home manager object and set its delegate.

   ```objc
   - (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
       self.homeManager = [[HMHomeManager alloc] init];
       self.homeManager.delegate = self;

       return YES;
   ```
3. Implement the delegate methods that are invoked when a home changes.

   For example, if multiple view controllers display information about homes, you can post a notification that a change occurred to update all the views.

   ```objc
   - (void)homeManagerDidUpdateHomes:(HMHomeManager *)manager {
       // Send a notification to the other objects
       [[NSNotificationCenter defaultCenter] postNotificationName:@"UpdateHomesNotification" object:self];
   }

   - (void)homeManagerDidUpdatePrimaryHome:(HMHomeManager *)manager {
       // Send a notification to the other objects
       [[NSNotificationCenter defaultCenter] postNotificationName:@"UpdatePrimaryHomeNotification" object:self];
   }
   ```

   View controllers register for the change notification and implement the appropriate action.

   ```
   [[NSNotificationCenter defaultCenter] addObserver:self selector:@selector(updateHomes:) name:@"UpdateHomesNotification" object:nil];
   [[NSNotificationCenter defaultCenter] addObserver:self selector:@selector(updatePrimaryHome:) name:@"UpdatePrimaryHomeNotification"  object:nil];
   ```

## Observing Changes to Individual Homes

The view controller that displays information about a home should be the delegate for the home object and update its views when the home changes.

__To observe changes to a specific home__

1. Add the home delegate protocol to your class interface.

   ```objc
   @interface HomeViewController () <HMHomeDelegate>

   @end
   ```
2. Set the delegate of the accessory.

   ```
   home.delegate = self;
   ```
3. Implement the [HMHomeDelegate](https://developer.apple.com/documentation/homekit/hmhomedelegate) protocol.

   For example, implement the [home:didAddAccessory:](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620215-home) and [home:didRemoveAccessory:](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620263-home) methods to update views that display accessories. To get the room that the accessory belongs to, use the [room](https://developer.apple.com/documentation/homekit/hmaccessory/1615282-room) property in the [HMAccessory](https://developer.apple.com/documentation/homekit/hmaccessory) class. (The default room for an accessory is returned by the [roomForEntireHome](https://developer.apple.com/documentation/homekit/hmhome/1620227-roomforentirehome) method.)

__Bridge Note:__ When you add a bridge to a home, the accessories behind the bridge are automatically added to the home. Your delegate receives a [home:didAddAccessory:](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620215-home) message for each accessory behind the bridge, but your delegate doesn’t receive a [home:didAddAccessory:](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620215-home) message for the bridge.

## Observing Changes to Accessories

The state of an accessory can change at any time. An accessory may not be reachable, can be out of range, or may be turned off. Update the user interface accordingly to reflect the current state of accessories, especially if your app allows the user to control an accessory.

In these steps it is assumed that you already retrieved an accessory object from the HomeKit database, as described in [Getting the Accessories in a Room](Getting%20the%20Home%20Layout.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tanjqfvbuqmznknltk).

__To observe changes to a specific accessory__

1. Add the accessory delegate protocol to your class interface.

   ```objc
   @interface AccessoryViewController () <HMAccessoryDelegate>

   @end
   ```
2. Set the delegate of the accessory.

   ```
   accessory.delegate = self;
   ```
3. Implement the [HMAccessoryDelegate](https://developer.apple.com/documentation/homekit/hmaccessorydelegate) protocol.

   For example, implement the [accessoryDidUpdateReachability:](https://developer.apple.com/documentation/homekit/hmaccessorydelegate/1615273-accessorydidupdatereachability) method to enable or disable accessory controls.

   ```objc
   - (void)accessoryDidUpdateReachability:(HMAccessory *)accessory {
       if (accessory.reachable == YES) {
          // Can communicate with the accessory
       } else {
          // The accessory is out of range, turned off, etc
       }
   }
   ```

If you display the state of services and their characteristics, implement the following delegate methods to update views accordingly:

- [accessoryDidUpdateServices:](https://developer.apple.com/documentation/homekit/hmaccessorydelegate/1615269-accessorydidupdateservices)
- [accessory:service:didUpdateValueForCharacteristic:](https://developer.apple.com/documentation/homekit/hmaccessorydelegate/1615286-accessory)

To access the services of an accessory, read [Accessing Services and Their Characteristics](Accessing%20Services%20and%20Characteristics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tanjqfvbuqnrnknltc).

[Next](Accessing%20Services%20and%20Characteristics.md)[Previous](Creating%20Homes%20and%20Adding%20Accessories.md)
