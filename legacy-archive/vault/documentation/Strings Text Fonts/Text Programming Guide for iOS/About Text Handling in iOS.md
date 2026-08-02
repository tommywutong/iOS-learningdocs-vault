---
title: Text Programming Guide for iOS
apple_id: TP40009542
resource_type: Guide
platform: tvOS|iOS
topic: Data Management
technology: UIKit
published: '2018-01-16'
source_url: https://developer.apple.com/library/archive/documentation/StringsTextFonts/Conceptual/TextAndWebiPhoneOS/Introduction/Introduction.html
archived_at: '2026-07-18T02:06:58.427777Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Displaying%20Text%20Content%20in%20iOS.md)

# About Text Handling in iOS

The iOS platform gives you many ways to display text in your apps and let users edit that text. It also lets you display formatted text and web content in your app’s views. The resources at your disposal range from [framework](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Framework.html#//apple_ref/doc/uid/TP40008195-CH56) objects—such as text views, text fields, and web views—to text layout engines that you can use directly to draw, lay out, and otherwise manage text.

![../Art/textpg_intro_2x.png](attachments/Art/textpg_intro_2x.png)

With the classes in the UIKit framework, you can manage the edit menu (including adding custom items to it), implement custom input views, and copy, cut, and paste data within and between apps.

Apps in iOS have a number of powerful technologies to handle text, both for editing text and for rendering high-quality typographically formatted text.

### The UIKit Framework Provides Your App with Text and Web Objects

You can add ready-made text views, text fields, and labels to your app’s user interface by using instances of the [UITextView](https://developer.apple.com/documentation/uikit/uitextview), [UITextField](https://developer.apple.com/documentation/uikit/uitextfield), and [UILabel](https://developer.apple.com/documentation/uikit/uilabel). You can add and configure them programmatically or by using the [Interface Builder](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/NibFile.html#//apple_ref/doc/uid/TP40008195-CH34) editor in Xcode. You can also turn a view of your app into a miniature web browser capable of understanding and displaying HTML, CSS, and JavaScript content.

### When Users Edit Text, Your App Must Manage the Keyboard

When a user taps a text field, text view, or form field in a web view, iOS animates a keyboard into view. An app can control which keyboard is presented; for example, for a numeric-value field, the app should select the numeric keypad. If the entered or edited text is obscured by the keyboard, the app should adjust the view displaying the text so that the text appears above the keyboard. The [delegate](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14) of a text view, text field, or web view is responsible for validating edited text and for accessing and storing edited text when the user dismisses the keyboard.

### Your App Can Draw and Manage Text Directly

Underlying the text views in UIKit is a powerful layout engine called Text Kit. If you need to customize the layout process or you need to intervene in that behavior, you can use Text Kit. Text Kit is a set of classes and protocols that provide high-quality typographical services which enable apps to store, lay out, and display text with all the characteristics of fine typesetting, such as kerning, ligatures, line breaking, and justification.

For most apps, you can use the high-level text display classes and Text Kit for all their text handling. For smaller amounts of text and special needs requiring custom solutions, you can use alternate, lower level technologies, such as the programmatic interfaces from the Core Text, Core Graphics, and Core Animation frameworks as well as other APIs in UIKit itself.

To communicate directly with the text-input system of iOS, implement the [UITextInput](https://developer.apple.com/documentation/uikit/uitextinput) [protocol](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Protocol.html#//apple_ref/doc/uid/TP40008195-CH45) and related protocols and classes. Your app can also make use of technologies for spell checking and regular expressions.

### Your App Has a Range of Options for the Input and Editing of Data

The UIKit framework includes programmatic interfaces for editing the data in a view and for entering data into an app. Custom input views can replace the system keyboard to permit input of special data; input accessory views are a custom view above the system keyboard (or custom input view) that enables users to affect edited data in app-specific ways. Using [UIPasteboard](https://developer.apple.com/documentation/uikit/uipasteboard) and related classes, an app can copy, cut, and paste data within different locations of itself or between itself and another app. As part of copy-cut-paste operations, the user taps a command on an contextual edit menu; your app manages this menu and can add custom commands to it.

The Core Graphics and Core Animation frameworks have some text-handling capabilities. Core Animation, for example, offers the [CATextLayer](https://developer.apple.com/documentation/quartzcore/catextlayer) class. To learn more about these capabilities, read _[Quartz 2D Programming Guide](../../Graphics%20Imaging/Quartz%202D%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrw)_ (Core Graphics) and _[Core Animation Programming Guide](../../Cocoa/Core%20Animation%20Programming%20Guide/About%20Core%20Animation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmju)_.

To find out more about the Core Text framework, which is appropriate for developing higher-level text-handling frameworks, read _[Core Text Programming Guide](../Core%20Text%20Programming%20Guide/About%20Core%20Text.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tkmzt)_ and _[Core Text Reference Collection](https://developer.apple.com/documentation/coretext)_.

[Next](Displaying%20Text%20Content%20in%20iOS.md)

