---
title: iOS 7 UI Transition Guide
apple_id: TP40013174
resource_type: Guide
platform: iOS
topic: User Experience
technology: UIKit
published: '2016-03-22'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/TransitionGuide/Scoping.html
archived_at: '2026-07-18T02:13:54.003379Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [iOS 7 UI Transition Guide](index.md)



## Scoping the Project

Knowing your app’s compatibility requirements and customization characteristics gives you some idea of the path to take. Use the following checklists to fill in more details and to scope the project.

### Things Every App Must Do

- Update the app icon.

  In iOS 7, app icons for high-resolution iPhone and iPod touch are 120 x 120 pixels; for high-resolution iPad, app icons are 152 x 152 pixels. (To learn more about all icon sizes, see Icon and Image Sizes.)

  Note that iOS 7 doesn’t apply shine or a drop shadow to the app icon. And, although iOS 7 still applies a mask that rounds the corners of an app icon, it uses a different corner radius than earlier versions of iOS.
- Update the launch image to include the status bar area if it doesn’t already do so.
- Support Retina display and iPhone 5 in all your artwork and designs, if you’re not already doing so.

### Things Every App Should Do

- Make sure that app content is discernible through translucent UI elements—such as bars and keyboards—and the transparent status bar. In iOS 7, view controllers use full-screen layout (to learn more, see [Using View Controllers](AppearanceCustomization.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztcnzufvbuqmjvfvjvomq)).
- Redesign custom bar button icons. In iOS 7, bar button icons are lighter in weight and have a different style. For some design guidance, see Bar Button Icons.
- Prepare for borderless buttons by reassessing the utility of button background images and bezels in your layout.
- Examine your app for hard-coded UI values—such as sizes and positions—and replace them with those you derive dynamically from system-provided values. Use Auto Layout to help your app respond when layout changes are required. (If you’re new to Auto Layout, learn about it by reading _[Auto Layout Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AutolayoutPG/index.html#//apple_ref/doc/uid/TP40010853)_.)
- Examine your app for places where the metrics and style changes of UIKit controls and views affect the layout and appearance. For example, switches are wider, grouped tables are no longer inset, and progress views are thinner. For more information on specific UI elements, see [Bars and Bar Buttons](Bars.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztcnzufvbuqobnknltc), [Content Views](ContentViews.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztcnzufvbuqmjqfvjvomi), [Controls](Controls.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztcnzufvbuqojnknltc), and [Temporary Views](TempViews.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztcnzufvbuqmjrfvjvomi).
- Adopt Dynamic Type. In iOS 7, users can adjust the text size they see in apps. When you adopt Dynamic Type, you get text that responds appropriately to user-specified size changes. For more information, see [Using Fonts](AppearanceCustomization.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztcnzufvbuqmjvfvjvona).
- Expect users to swipe up from the bottom of the screen to reveal Control Center. If iOS determines that a touch that begins at the bottom of the screen should reveal Control Center, it doesn’t deliver the gesture to the currently running app. If iOS determines that the touch should not reveal Control Center, the touch may be slightly delayed before it reaches the app.
- Revisit the use of drop shadows, gradients, and bezels. Because the iOS 7 aesthetic is smooth and layered—with much less emphasis on using visual effects to make UI elements look physical—you may want to rethink these effects.
- If necessary, update your app to best practices for iOS 6—such as Auto Layout and storyboards—and ensure that the app doesn’t use deprecated APIs.

Now that you have a better idea of the types of things you need to do, learn more about changes in view controllers, tinting, and fonts by reading [Appearance and Behavior](AppearanceCustomization.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztcnzufvbuqmjvfvjvomi).

### If You Must Continue to Support iOS 6

If you must support both iOS 6 and iOS 7, you can detect which OS version the app is running in and load the appropriate resources. For more information, see [Supporting iOS 6](SupportingEarlieriOS.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztcnzufvbuqmjufvjvomi).

[Before You Start](index.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztcnzufvbuqnrnknltc)

[Supporting iOS 6](SupportingEarlieriOS.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztcnzufvbuqmjufvjvomi)
