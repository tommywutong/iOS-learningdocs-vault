---
title: HomeKit Developer Guide
apple_id: TP40015050
resource_type: Guide
platform: watchOS|iOS
topic: null
technology: HomeKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/HomeKitDeveloperGuide/EnablingHomeKit/EnablingHomeKit.html
archived_at: '2026-07-27T06:57:09.401191Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [HomeKit Developer Guide](Introduction%20to%20HomeKit.md)


[Next](Getting%20the%20Home%20Layout.md)[Previous](Introduction%20to%20HomeKit.md)

# Enabling HomeKit

HomeKit is an app service available only to apps distributed through the App Store. HomeKit requires additional configuration in your Xcode project. Your app must be provisioned and code signed to use HomeKit. To avoid code signing issues, enable HomeKit in the Xcode Capabilities pane. You don’t need to edit entitlements directly in Xcode or Member Center.

## Setup

To perform all the steps in this document, you need:

- A Mac computer with Xcode 6 or later installed
- For the best experience, the latest OS X and Xcode releases installed on your Mac
- Membership in the iOS Developer Program
- Permission to create code signing and provisioning assets in Member Center

Verify that you have performed these tasks before you begin using HomeKit. To create your team provisioning profile, read _App Distribution Quick Start_.

|  | Task |
| --- | --- |
| ../Art/checkbox_checked_2x.png | Join the iOS Developer Program. |
| ../Art/checkbox_checked_2x.png | Create an Xcode project that builds and runs. |
| ../Art/checkbox_checked_2x.png | Add your Apple ID to Accounts preferences. |
| ../Art/checkbox_checked_2x.png | In the General pane, create your team provisioning profile:   - Choose your team from the Team pop-up menu. - Click Fix Issue. |

When you successfully complete the preceding tasks, the error message and the Fix Issue button below the Team pop-up menu in the General pane disappear. The screenshot below shows the General pane when the code signing assets are successfully created.

（原归档配图获取待重试：`2_create_teamprofile_2x.png`）

To troubleshoot code signing and provisioning, read Troubleshooting in _App Distribution Guide_.

## Enable HomeKit

To use HomeKit, you first enable it. Xcode will add the HomeKit entitlement to your entitlements file in the project and App ID in Member Center. Xcode also adds the HomeKit framework to your project. HomeKit requires an explicit App ID, which is created for you when you complete these steps.

__To enable HomeKit__

1. In Xcode, choose View > Navigators > Show Project Navigator.
2. Choose the target from the Project/Targets pop-up menu (or in the Product/Targets sidebar if it appears).
3. Click Capabilities to view app services that you can add to your app.
4. Scroll down to the HomeKit row and select the switch.

__Important:__ An iOS app linked on or after iOS 10.0 must include in its `Info.plist` file the usage description keys for the types of data it needs to access or it will crash. To access HomeKit data specifically, it must include `NSHomeKitUsageDescription`.

## Download HomeKit Accessory Simulator

You don’t need to buy accessories to develop your HomeKit app. You can use HomeKit Accessory Simulator to test the communication of your HomeKit app with simulated accessories. HomeKit Accessory Simulator is not distributed with Xcode.

__To download HomeKit Accessory Simulator__

1. In the HomeKit section of the Capabilities pane, click Download HomeKit Accessory Simulator.

   Alternatively, choose Xcode > Open Developer Tool > More Developer Tools.
2. In a browser, search for and download the “Hardware IO Tools for Xcode” `.dmg` file.
3. In the Finder, double-click the `.dmg` file in `~/Downloads`.
4. Drag HomeKit Accessory Simulator to the `/Applications` folder.

Later, you’ll test your app using HomeKit Accessory Simulator, as described in [Testing Your HomeKit App](Testing%20Your%20HomeKit%20App.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tanjqfvbuqnznknltc).

[Next](Getting%20the%20Home%20Layout.md)[Previous](Introduction%20to%20HomeKit.md)
