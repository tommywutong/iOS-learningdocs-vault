---
title: Xcode Overview
apple_id: TP40010215
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/ToolsLanguages/Conceptual/Xcode_Overview/RunningonaDevice.html
archived_at: '2026-07-27T06:57:08.103587Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Overview](index.md)


[Next](ManagingSchemes.md)[Previous](RunningintheSimulator.md)

## Running on a Device

Xcode will launch an OS X app on your development Mac.

（原归档配图获取待重试：`AdventureLaunchedMac_2x.png`）

To run your iOS and watchOS apps on a device (an iPad, iPhone, iPod touch, or Apple Watch) during development, four things are required:

- The device is connected to your Mac.
- You are a member of an Apple developer program.
- You have a valid signing identity for the developer program.
- The device is provisioned for development use by that developer program.

Xcode guides you through any missing parts of these requirements and can usually do the work of obtaining a signing identity and device provisioning profile.

To run your iOS app on a device (an iPad, iPhone, or iPod touch) during development, the device must be connected to your Mac, and the device must be provisioned for development by Apple. If your Mac app uses certain Apple technologies—such as iCloud, Game Center, and In-App Purchase—your Mac must be provisioned.

Apple implements an underlying security model to protect user data and to protect your app from being modified and distributed without your knowledge. Throughout the development process, you create assets and enter information that Apple uses to verify the identify of you, your devices, and your apps. These assets include provisioning profiles, which identify your development devices.

To obtain a provisioning profile for a device, you need an Apple Developer Program membership and associated signing identity. For detailed information on doing this, see _App Distribution Quick Start_.

### Choosing Your Device for the Run Destination

When you plug the device into your Mac, the device’s name and the iOS release it is running appear as a destination in the Scheme menu. Choose your device as the destination, and then click the Run button to build and run your app on the device.

[Running in Simulator](RunningintheSimulator.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqnjufvjvomi)

[Managing Schemes](ManagingSchemes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqnjwfvjvomi)

Copyright © 2018 Apple Inc. All rights reserved.
[Terms of Use](http://www.apple.com/legal/terms/site.html) |
[Privacy Policy](http://www.apple.com/privacy/) |
[Updated: 2016-10-27](RevisionHistory.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqmrsfvjvomi)

[Next](ManagingSchemes.md)[Previous](RunningintheSimulator.md)
