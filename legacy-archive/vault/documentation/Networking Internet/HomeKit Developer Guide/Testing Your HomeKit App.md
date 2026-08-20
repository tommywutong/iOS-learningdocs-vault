---
title: HomeKit Developer Guide
apple_id: TP40015050
resource_type: Guide
platform: watchOS|iOS
topic: null
technology: HomeKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/HomeKitDeveloperGuide/TestingYourHomeKitApp/TestingYourHomeKitApp.html
archived_at: '2026-07-27T06:57:09.462035Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [HomeKit Developer Guide](Introduction%20to%20HomeKit.md)


[Next](Creating%20Action%20Sets%20and%20Triggers.md)[Previous](Accessing%20Services%20and%20Characteristics.md)

# Testing Your HomeKit App

If you don’t have physical accessories, use HomeKit Accessory Simulator to simulate accessories in a home. Each simulated accessory has services with characteristics that you can control from your app. Your app creates the objects and relationships that are stored in the HomeKit database. It creates the home layout, adds new accessories to the home in the simulated environment, and adds the accessories to rooms in a home. Then your app can control the accessories displayed in HomeKit Accessory Simulator. To test with HomeKit Accessory Simulator, run your app in iOS Simulator, or run it on an iOS device using Xcode.

HomeKit Accessory Simulator is an additional developer tool that is not installed with Xcode. To install HomeKit Accessory Simulator, follow the steps in [Download HomeKit Accessory Simulator](Enabling%20HomeKit.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tanjqfvbuqmrnknltg).

## Adding Accessories

Use HomeKit Accessory Simulator to add some accessories to the simulated network.

__To add an accessory to the network__

1. In HomeKit Accessory Simulator, click the Add button (+) at the bottom of the left column.
2. Choose Add Accessory from the pop-up menu.
3. Enter an accessory name and manufacturer.

   （原归档配图获取待重试：`add_accessory_2x.png`）
4. Click Finish.

To delete an accessory, select the accessory and enter Delete on the keyboard.

## Adding Services to Accessories

An accessory needs a service with characteristics that you can control from your app. You select a service from a predefined list and then customize the characteristics.

__To add a service to an accessory__

1. In HomeKit Accessory Simulator, select the accessory in the Accessories column.

   The services for the accessory appear in the detail view.

   （原归档配图获取待重试：`add_service_2x.png`）

   __Note:__ All accessories have an Accessory Information service that appears below all other services in the detail view. You can add characteristics to the Accessory Information service, but you cannot delete the default characteristics.
2. Click Add Service, and choose a type of service from the pop-up menu.

   The new service appears in the detail view. HomeKit Accessory Simulator creates the common characteristics for that type of service. For example, the default characteristics of a Light Bulb service are Hue, Saturation, Brightness, and On. (The On characteristic is the same as the power state characteristic type, described in [Accessing Values of Characteristics](Accessing%20Services%20and%20Characteristics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tanjqfvbuqnrnknltg).) Some characteristics are mandatory and others are optional. For example, the On characteristic is mandatory, and the Hue, Saturation, and Brightness characteristics are optional.

   （原归档配图获取待重试：`add_service_2_2x.png`）

## Adding Characteristics to Services

You add characteristics to a service using a predefined list, or you build a custom type. You can add only one characteristic of each kind.

__To add a characteristic to a service__

1. In HomeKit Accessory Simulator, under the service in the detail view, click Add Characteristic.
2. From the Characteristic Type menu, choose a type or Custom.

   （原归档配图获取待重试：`add_characteristic_2x.png`）
3. Enter other information about the characteristic in the fields, and click Finish.

   The new characteristic appears in the detail view.

To remove a characteristic, click the minus icon to the right of the characteristic. The icon doesn’t appear if the characteristic is mandatory for a service type. For example, you can remove the Hue, Saturation, and Brightness characteristics of a Light Bulb service, but you cannot remove the On characteristic.

## Adding Accessories to a Home in Your App

After you create an accessory in HomeKit Accessory Simulator, run your app and add the new accessory to a home.

__To pair an accessory with a home__

1. In Xcode, click Run and execute the code that invokes the [addAccessory:completionHandler:](https://developer.apple.com/documentation/homekit/hmhome/1620216-addaccessory) method (described in [Adding Accessories to Homes and Rooms](Creating%20Homes%20and%20Adding%20Accessories.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tanjqfvbuqnbnknltk)).
2. If an Add HomeKit Accessory dialog states that the accessory is not certified (which is allowed in HomeKit Accessory Simulator), click Add Anyway.

   （原归档配图获取待重试：`add_accessory_dialog1_2x.png`）
3. In the next Add HomeKit Accessory dialog that appears, enter the setup code for the accessory and click Add.

   In HomeKit Accessory Simulator, the setup code appears below the accessory name in the detail area.

   （原归档配图获取待重试：`add_accessory_dialog2_2x.png`）

To write the code to add an accessory to a home and room, read [Creating Homes and Adding Accessories](Creating%20Homes%20and%20Adding%20Accessories.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tanjqfvbuqnbnknltc).

## Controlling Accessories

In HomeKit Accessory Simulator, you can access an accessory’s services and set the values of the service characteristics to simulate controlling the accessory from another HomeKit app, or to simulate manually controlling the accessory.

__To control an accessory__

1. In HomeKit Accessory Simulator, select the accessory in the Accessories column.

   The services and their characteristics are displayed in the detail view.
2. Manipulate the control for a characteristic to change its value.

   For example, to change the Hue, Saturation, and Brightness of a light bulb, move the knob of a corresponding slider. To turn a light bulb off, click No on the On toggle.

   （原归档配图获取待重试：`accessory_detail_view_2x.png`）

If your app displays the characteristics of a service, such as a light bulb’s on and off state, it should update the view when you change the characteristic’s value in HomeKit Accessory Simulator.

To observe HomeKit database changes, read [Observing HomeKit Database Changes](Observing%20HomeKit%20Database%20Changes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tanjqfvbuqnjnknlte). To write the code to control an accessory from your app, read [Accessing Services and Characteristics](Accessing%20Services%20and%20Characteristics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tanjqfvbuqnrnknltc).

## Adding Bridges

To simulate accessories that don’t support HomeKit Accessory Protocol, add a bridge and then add the accessories to the bridge. Configuring an accessory behind a bridge is similar to configuring other types of accessories.

### Adding a Bridge to the Network

Add an accessory that represents the bridge.

__To add a bridge to the network__

1. In HomeKit Accessory Simulator, click the Add button (+) at the bottom of the Accessories column.
2. Choose Add Bridge from the pop-up menu.
3. Enter an accessory name and manufacturer.

   （原归档配图获取待重试：`add_bridge_2x.png`）
4. Click Finish.

### Adding Accessories Behind a Bridge

Add one or more accessories behind the bridge.

__To add an accessory to a bridge__

1. In the left column in HomeKit Accessory Simulator, select the bridge under Bridges.
2. Choose Add Accessory in the detail view.
3. Enter an accessory name and manufacturer.
4. Click Finish.

To view the details of an accessory behind a bridge, select it under the bridge in the Bridges section. If necessary, click the disclosure triangle next to the bridge to reveal its accessories. After you add services and their characteristics to the accessories, as described in [Adding Services to Accessories](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tanjqfvbuqnznknltg) and [Adding Characteristics to Services](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tanjqfvbuqnznknlts), they appear in the detail area when the bridge is selected.

（原归档配图获取待重试：`view_bridge_accessories_2x.png`）

## Adding Bridges to a Home in Your App

The steps to pair a bridge to a home are the same as the steps to pair an accessory to a home, described in [Adding Accessories to a Home in Your App](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tanjqfvbuqnznknlti). The accessories behind the bridge are also added to the home, as described in [Adding Bridges to Homes and Rooms](Creating%20Homes%20and%20Adding%20Accessories.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tanjqfvbuqnbnknlts).

## Controlling Accessories Behind a Bridge

The steps to control accessories behind a bridge are the same as the steps to control any accessory, described in [Controlling Accessories in HomeKit Accessory Simulator](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tanjqfvbuqnznknltk), except that you select the accessory under the bridge in the left column.

## Testing Multiple iOS Devices and Users

You can’t test sharing of the HomeKit database between multiple iOS devices and users using iOS Simulator. Instead, install your app on multiple iOS devices, enter the iCloud credentials on those iOS devices, and run your app. Alternatively, use ad hoc provisioning to test your app on multiple registered iOS devices, as described in Distributing Your App Using Ad Hoc Provisioning.

- To test the same user using multiple iOS devices, sign in with the same iCloud account on each iOS device.
- To test multiple users accessing the same home, sign in with different iCloud accounts on each iOS device.

  Your app should enable a user to add a guest user to the home, as described in [Managing Users](Managing%20Users.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tanjqfvbuqojnknltc).

[Next](Creating%20Action%20Sets%20and%20Triggers.md)[Previous](Accessing%20Services%20and%20Characteristics.md)
