---
title: Xcode Overview
apple_id: TP40010215
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/ToolsLanguages/Conceptual/Xcode_Overview/AddingImages.html
archived_at: '2026-07-27T06:57:08.057240Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Overview](index.md)


[Next](AddingParticleEmitterEffects.md)[Previous](FindingHelpforInterfaceBuilder.md)

## Adding Images

To help you create and manage user interface elements for your app, Xcode offers several tools in addition to Interface Builder.

You create many images for your app, including icons, custom artwork, and the launch screens for different iOS devices. Some of these images are required for App Store submission. The asset catalog helps you manage them.

（原归档配图获取待重试：`AssetCatMac_2x.png`）

With the particle emitter editor, you can enhance your app by adding animation effects involving moving particles such as snow, sparks, and smoke. These effects are especially useful in games for iOS and Mac.

（原归档配图未能恢复：`LeafParticles_2x.png`）

### Adding App Icons and Launch Images

Create app icons for all of the operating system versions and devices that your app supports. iOS, watchOS, and OS X apps require different types of icons. For any platform, add the required versions of your app icons to an asset catalog in Xcode.

For an iOS app, create an icon to be displayed on a device’s Home screen and in the App Store. Xcode doesn’t include graphics tools for creating icons; use a graphic design app. Create several different versions of the icon for use in different situations. Your iOS app can include a small icon (to use when displaying search results) and a high-resolution icon (for devices with Retina displays). If your iOS app’s target is universal, you also create versions of the icon for iPad and iPhone devices.

For a watchOS app, create icons for the home screen and any other interfaces you support such as notifications or long looks.

For an OS X app, create a set of icons, consisting of pairs of icons (standard and high resolution) for each icon size, in pixels: 16 x 16, 32 x 32, 128 x 128, 256 x 256, and 512 x 512. The Finder uses these icons to represent your app to the user.

### Work with Image Assets in the Asset Catalog

When you create a new project, Xcode creates an asset catalog named `Assets.xcassets`. Select the asset catalog from the project navigator, and Xcode opens the catalog in the editor area.

The asset catalog contains a list of image sets. Each image set, such as AppIcon in the screenshot, contains all the versions of an image that are necessary to support various devices and scale factors. You can add icon images to your app by dragging them to the appropriate cell in the icon set grid.

（原归档配图获取待重试：`iOSAppIcon_2x.png`）

You can create additional image sets, such as for buttons and other controls in your app. To create an empty image set or to import images into a new set, click the Add button (+) at the bottom of the image set list. You can add folders to organize the items in the catalog. Asset catalogs also support other types such as Sprite Atlases, Watch Complications, and Data files.

### Create and Set the iOS Launch Screen File

A launch screen is displayed while your app is launching on an iOS device. The launch screen is displayed as soon as the user taps your app icon, and it stays on the screen until your main interface is displayed. If your app is running on iOS 8 or later, the system uses a launch screen from a storyboard file and sizes it appropriately for the screen. For deployment targets prior to iOS 8, you add a set of launch images to an asset catalog for each of the possible screen sizes.

New projects are created with a launch screen storyboard file called `LaunchScreen.storyboard`. Alternatively, you can create a new launch screen file using File > New, selecting the User Interface category, and choosing a file type of Launch Screen. The launch screen uses size classes to adapt to different screen sizes and orientations; see [Building for Multiple Screen Sizes](BuildingforMultipleScreenSizes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqnbvfvjvomi) for more information.

Because the launch screen is shown before your app is running, you can only use a single root view of type UIView or UIViewController. You are also limited to UIKit classes that do not require updating. For more information, see Creating a Launch Screen File.

To set the launch screen, open the General information tab for your target, and select the launch screen file from the pop-up menu.

For more help icons, launch images, and the asset catalog, see [Xcode Help](https://help.apple.com/xcode).

### Create and Set iOS Launch Images for iOS 7 and Earlier

You can easily capture screenshots for launch images on a device. On the device, configure the screen the way you want it to appear. Then press the device Lock and Home buttons simultaneously. Your screenshot is saved in the Saved Photos album in the Photos app. Copy the screenshot from the device to your Mac. You can use the iPhoto app, for example, to import the screenshot from the device and then export the screenshot to your Mac as a PNG file.

To set the screenshot as a launch image, select the asset catalog file in the project navigator, and select the LaunchImage set. Drag your screenshot to the appropriate cell in the grid.

For more information on help icons, launch images, and the asset catalog, see [Xcode Help](https://help.apple.com/xcode).

[Finding Help for Interface Builder](FindingHelpforInterfaceBuilder.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqnbzfvjvomi)

[Adding Particle Emitter Effects](AddingParticleEmitterEffects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqnjrfvjvomi)

Copyright © 2018 Apple Inc. All rights reserved.
[Terms of Use](http://www.apple.com/legal/terms/site.html) |
[Privacy Policy](http://www.apple.com/privacy/) |
[Updated: 2016-10-27](RevisionHistory.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqmrsfvjvomi)

[Next](AddingParticleEmitterEffects.md)[Previous](FindingHelpforInterfaceBuilder.md)
