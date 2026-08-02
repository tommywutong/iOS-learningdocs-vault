---
title: Xcode Overview
apple_id: TP40010215
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/ToolsLanguages/Conceptual/Xcode_Overview/SimulatingProblems.html
archived_at: '2026-07-27T06:57:08.149478Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Overview](index.md)


[Next](CustomizingYourWorkflow.md)[Previous](MeasuringPerformance.md)

## Simulating Problems

Simulator helps you find major problems in your app during design and early testing. For example, the Debug menu in Simulator offers tools that help you:

- Slow an animation to spot any problems
- Change the graphics quality
- Trigger iCloud sync
- Identify blended view layers that harm app performance
- Identify images whose source pixels aren’t aligned to the destination pixels
- See what content is rendered offscreen
- Simulate different locations

（原归档配图获取待重试：`SimulatorDebug_2x.png`）

In every simulated environment in Simulator, the Home screen provides access to apps—such as Settings, Contacts, Maps, and Passbook—that are included with an iOS or watchOS device. You can perform preliminary testing of your app’s interaction with these apps in Simulator. For example, if you are testing a game, use Simulator to test that the game uses Game Center correctly.

The Accessibility inspector in Simulator helps you test the usability of your app regardless of a person’s limitations or disabilities by displaying information about each accessible element in your app. The inspector also enables you to simulate VoiceOver interaction with those elements. To start the Accessibility inspector, click the Home button in Simulator. Click Settings and go to General > Accessibility. Slide the Accessibility Inspector switch to On.

You can test your app’s localizations in Simulator by changing the language. In Settings, go to General > International > Language.

Although you can test your app’s basic behavior in Simulator, the simulator is limited as a test platform for multiple reasons. For example:

- Because Simulator is an app running on a Mac, Simulator has access to the computer’s memory, which is much greater than the memory found on a device.
- Simulator runs on the Mac CPU rather than the processor of an iOS or watch OS device.
- Simulator doesn’t run all threads that run on devices.
- Simulator can’t simulate hardware features like the accelerometer, gyroscope, camera, or proximity sensor.

While developing your app, run and test it on all of the devices and OS versions that you intend to support.

For more detailed information, see [Testing and Debugging in Simulator](../../IDEs/Simulator%20User%20Guide/Testing%20and%20Debugging%20in%20Simulator.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdqnbyfvbuqna).

[Measuring Performance](MeasuringPerformance.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqnrqfvjvomi)

[Customizing Your Workflow](CustomizingYourWorkflow.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqnrsfvjvomi)

Copyright © 2018 Apple Inc. All rights reserved.
[Terms of Use](http://www.apple.com/legal/terms/site.html) |
[Privacy Policy](http://www.apple.com/privacy/) |
[Updated: 2016-10-27](RevisionHistory.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqmrsfvjvomi)

[Next](CustomizingYourWorkflow.md)[Previous](MeasuringPerformance.md)
