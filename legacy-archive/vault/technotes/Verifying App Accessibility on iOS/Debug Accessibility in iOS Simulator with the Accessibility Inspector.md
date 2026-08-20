---
title: Verifying App Accessibility on iOS
apple_id: TP40012619
resource_type: Guide
platform: iOS
topic: User Experience
technology: null
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/technotes/TestingAccessibilityOfiOSApps/TestAccessibilityiniOSSimulatorwithAccessibilityInspector/TestAccessibilityiniOSSimulatorwithAccessibilityInspector.html
archived_at: '2026-07-27T06:57:08.756956Z'
---
> 导航：[总目录](../../README.md) · [technotes](../../_indexes/technotes.md) · [Verifying App Accessibility on iOS](About%20Accessibility%20Verification%20on%20iOS.md)



# Debug Accessibility in iOS Simulator with the Accessibility Inspector

The Accessibility Inspector displays accessibility information about each accessible element in an app. You can use the Accessibility Inspector to simulate VoiceOver interaction with the accessible elements in your app to examine the information they provide.

__Note:__ The Accessibility Inspector is helpful for testing the accessibility of your app during development, but it is no substitute for testing your app with VoiceOver on a physical device. For one thing, the Accessibility Inspector does not speak accessibility information, so you can’t hear how your element descriptions will sound. Even though the Accessibility Inspector is ideal for quickly verifying that elements supply appropriate accessibility information, you should test your app on a device, with VoiceOver turned on, to make sure that it behaves as users expect. See [Test Accessibility on Your Device with VoiceOver](Test%20Accessibility%20on%20Your%20Device%20with%20VoiceOver.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdmmjzfvbuqmznknltc) for some tips on how to do this.

The Accessibility Inspector runs in iOS Simulator and lets you see at a glance the accessibility label, value, hint (if applicable), traits, and frame coordinates for each element onscreen. You are also presented with a list of recently dispatched accessibility notifications.

![bullet](attachments/Resources/1282/Images/task_2x.png)To start Accessibility Inspector

1. Run your app in iOS Simulator (for more information on how to do this, see _[Simulator User Guide](../../documentation/IDEs/Simulator%20User%20Guide/About%20Simulator.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdqnby)_).
2. In the simulated device environment, press the Home button to reveal the Home screen.
3. Open Settings and go to General > Accessibility.
4. Slide the Accessibility Inspector switch control to On. The Accessibility Inspector remains active until you turn it off, even if you quit and restart iOS Simulator.

When you run your app in iOS Simulator, a single-click simulates a single-tap, and scrolling with the mouse or keyboard simulates flicking or dragging with the finger. But when the Accessibility Inspector is active, a single-click focuses the inspector on an element; it does not simulate a tap on the element. To simulate a tap on an element while the Accessibility Inspector is active, double-click the element. When the Accessibility Inspector focuses on an element, it draws a shaded box around it (similar to the VoiceOver cursor), as shown in Figure 2-1.

__Figure 2-1__  The Accessibility Inspector draws a shaded rectangle around the selected element

（原归档配图获取待重试：`accessibility_inspector_focus_2x.png`）

To scroll, you must first deactivate the Accessibility Inspector. Then scroll as needed by dragging the mouse, and reactivate the inspector when you’ve reached the location you want in your app. To deactivate or reactivate the Accessibility Inspector, click the close control in the upper-left corner of the panel (the close control looks like a circle with an “X” in it). Clicking this control does not turn off the Accessibility Inspector; to turn it off, go to General > Accessibility > Accessibility Inspector and change the setting to Off.

When the Accessibility Inspector is not active, it appears as it does in Figure 2-2 and does not affect the way you interact with any simulated app features in iOS Simulator.

__Figure 2-2__  The inactive appearance of the Accessibility Inspector

（原归档配图获取待重试：`accessibility_inspector_disabled_2x.png`）
