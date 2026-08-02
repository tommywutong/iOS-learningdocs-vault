---
title: Xcode Overview
apple_id: TP40010215
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/ToolsLanguages/Conceptual/Xcode_Overview/RunningintheSimulator.html
archived_at: '2026-07-27T06:57:08.096991Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Overview](index.md)


[Next](RunningonaDevice.md)[Previous](BuildingYourApp.md)

## Running in Simulator

Simulator enables you to simulate multiple iOS and watchOS devices running current and some legacy operating systems. You interact with Simulator by using the keyboard and trackpad to emulate taps, device rotation, and other actions. For example, you can use the Hardware menu in Simulator to:

- Rotate an iPhone or iPad to the left and right
- Simulate a user shaking an iPhone or iPad
- Send the frontmost app a simulated low-memory warning
- Use tools to to examine graphics rendering, simulate Touch ID, and more
- Simulate the force of a touch on a pressure sensitive display

（原归档配图未能恢复：`AdventureLaunchediPhone_2x.png`）

As a preliminary tool for use before testing your app on devices, Simulator allows you to prototype and test builds of your apps during the development process. Although you can test your app’s basic behavior in Simulator, the simulator is limited as a test platform. While developing your app, it is essential that you run and test it on connected devices.

For more detail on using the simulator, see _[Simulator User Guide](../../IDEs/Simulator%20User%20Guide/About%20Simulator.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdqnby)_.

### Create Custom Simulator Configurations

Choose Window > Devices to open the Devices organizer. Click the Add button (+) in the bottom left of the organizer window. In the dialog that appears, type a name for your custom simulator configuration, choose a device type, and then choose an iOS version. If this is for a watchOS app, add a paired Apple Watch by choosing one from the menu. Click Create and your new custom simulator configuration is added to the Simulator list. By default, the new configuration appears in the Run Destinations menu.

（原归档配图获取待重试：`XC_O_devices_add_2x.png`）

### Show Simulators or Devices in the Run Destinations Menu

Choose Window > Devices. In the Devices organizer, select the item you want to add or remove from the target menu. Click the Configuration button (（原归档配图未能恢复：`XC_O_devices_window_config_button_2x.png`）) in the bottom left of the organizer window. Choose Show in Run Destinations Menu. A checkmark next to that menu item indicates that the simulator or device will be shown in the Run Destinations menu.

（原归档配图获取待重试：`XC_O_devices_menu_2x.png`）

[Building Your App](BuildingYourApp.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqnjtfvjvomi)

[Running on a Device](RunningonaDevice.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqnjvfvjvomi)

Copyright © 2018 Apple Inc. All rights reserved.
[Terms of Use](http://www.apple.com/legal/terms/site.html) |
[Privacy Policy](http://www.apple.com/privacy/) |
[Updated: 2016-10-27](RevisionHistory.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqmrsfvjvomi)

[Next](RunningonaDevice.md)[Previous](BuildingYourApp.md)
