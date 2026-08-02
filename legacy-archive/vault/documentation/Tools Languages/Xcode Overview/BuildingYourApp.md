---
title: Xcode Overview
apple_id: TP40010215
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/ToolsLanguages/Conceptual/Xcode_Overview/BuildingYourApp.html
archived_at: '2026-07-27T06:57:08.089651Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Overview](index.md)


[Next](RunningintheSimulator.md)[Previous](AddingWatchComplications.md)

## Building Your App

To build and run your iOS, watchOS, or OS X app, choose a scheme and a run destination in the workspace toolbar, and click the Run button. Clicking the Stop button causes your app to quit.

（原归档配图未能恢复：`XC_O_SchemeMenuWithCallouts_2x.png`）

If you are running an iOS or watchOS app, Xcode launches it either in Simulator or on a device connected to your Mac. If you are running an OS X app, Xcode launches it directly on your Mac.

Xcode displays any errors or warnings it encounters in the issue navigator, available by clicking （原归档配图获取待重试：`XG_NavArea_Issue_icon_2x.png`） in the navigator bar. If there are errors during the compilation or link phase, Xcode doesn’t run your code.

### Choosing a Scheme to Build Your App

A __scheme__ is a collection of settings that specify the targets to build for a project, the build configuration to use, and the executable environment to use when the product is launched. When you open an existing project (or create a new one), Xcode automatically creates a scheme for each target. The default scheme is named after your project and includes settings to perform five actions:

- Run the app.
- Run unit tests against the target.
- Profile the app’s performance characteristics.
- Perform static analysis on the code.
- Archive the app for distribution, such as sending to testers or submitting to the App Store.

Each action includes building the app as an executable product. To choose the scheme, use the __Scheme menu__ in the Xcode workspace toolbar. (You’ll use the Scheme menu to choose a destination, too.)

### Choosing a Destination to Run Your App

When you build an app, the __destination__ determines where the app runs after it’s built. For OS X apps, the destination is the Mac on which the app is built. For iOS or watchOS apps, the destination can be a provisioned device connected to the Mac, or Simulator. Installed as part of the Xcode tools, __Simulator__ runs on your Mac and simulates an iPhone, iPad, or Apple Watch environment.

（原归档配图未能恢复：`SchemeMenu_2x.png`）

The Scheme menu lets you select a combination of scheme and destination, but the two settings are distinct. A scheme does not include a destination. In the screenshot above, Adventure iOS is selected as the scheme, and the iPhone Retina (4-inch) simulation environment is selected as the destination. As a result, the Adventure iOS scheme builds an iOS executable that runs on a simulated iPhone in OS Simulator. As shown below, the same scheme could be used to run the app on a different destination, such as a simulated iPad or a connected iOS device.

（原归档配图获取待重试：`NewRunDestination_2x.png`）

[Adding Watch Complications](AddingWatchComplications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqnztfvjvomi)

[Running in Simulator](RunningintheSimulator.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqnjufvjvomi)

Copyright © 2018 Apple Inc. All rights reserved.
[Terms of Use](http://www.apple.com/legal/terms/site.html) |
[Privacy Policy](http://www.apple.com/privacy/) |
[Updated: 2016-10-27](RevisionHistory.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqmrsfvjvomi)

[Next](RunningintheSimulator.md)[Previous](AddingWatchComplications.md)
