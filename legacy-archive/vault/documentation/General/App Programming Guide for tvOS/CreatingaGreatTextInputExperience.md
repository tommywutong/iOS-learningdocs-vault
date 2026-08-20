---
title: App Programming Guide for tvOS
apple_id: TP40015241
resource_type: Guide
platform: tvOS
topic: General
technology: null
published: '2017-01-12'
source_url: https://developer.apple.com/library/archive/documentation/General/Conceptual/AppleTV_PG/CreatingaGreatTextInputExperience.html
archived_at: '2026-07-15T07:33:05.433575Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [App Programming Guide for tvOS](index.md)



## Designing the Keyboard Input Experience

Keyboard input can be difficult on Apple TV, because there is no hardware keyboard. You need to take extra care to ensure that your users have an enjoyable experience. When possible, design your UI to avoid excessive text input. Apple TV has two types of keyboards: normal and inline.

### Keyboard Input

Use [UIAlertController](https://developer.apple.com/documentation/uikit/uialertcontroller) or [UITextField](https://developer.apple.com/documentation/uikit/uitextfield) to customize the keyboard experience and create keyboards specific to your app; for example, an email-specific keyboard or a numeric keyboard. Both [UIAlertController](https://developer.apple.com/documentation/uikit/uialertcontroller) and [UITextField](https://developer.apple.com/documentation/uikit/uitextfield) support all of the available options in `UIKit/UITextInputTrailts.h`. The [inputAccessoryView](https://developer.apple.com/documentation/uikit/uiresponder/1621119-inputaccessoryview) and [inputAccessoryViewController](https://developer.apple.com/documentation/uikit/uiresponder/1621124-inputaccessoryviewcontroller) APIs also allow you to customize the keyboard experience.

### Using UIAlertController

The keyboard UI is completely controlled by UIKit, but using [UIAlertController](https://developer.apple.com/documentation/uikit/uialertcontroller) allows you to add any number of text fields and buttons. You can put instructional text and a title on the top of the keyboard. This keyboard is easy to bring up and use. However, the user generally has to click the remote a number of times in order to enter information.

### Using UITextField

Use [UITextField](https://developer.apple.com/documentation/uikit/uitextfield) to place a full-screen keyboard on the screen. Users can navigate between text fields using the Next and Previous buttons built into the keyboard. This avoids the need to drop back to the text fields, focus on the next one, and click again. After all text fields have been filled, a Done button is presented to return the user to the previous page. Developers can place these keyboards wherever they are required and still get the next/previous behavior. However, setting up these keyboards requires more work than using [UIAlertController](https://developer.apple.com/documentation/uikit/uialertcontroller), because you have to create all the views and lay them out.

### Advanced UITextField Keyboards

All of the iOS first responder mechanisms work on tvOS. This allows developers to present a UI, visible or hidden, and then make one of the text fields the first responder by calling the [becomeFirstResponder](https://developer.apple.com/documentation/uikit/uiresponder/1621113-becomefirstresponder) method on it. This action causes the text field to put up the keyboard UI without the user having to navigate to a text field and click on it. When the user exits the keyboard or clicks the Done button, use first responder callbacks to see that the text fields no longer accept keyboard input.

### Inline Keyboard Input

An inline keyboard displays all of the possible inputs on a single line. Use [UISearchController](https://developer.apple.com/documentation/uikit/uisearchcontroller) to create a keyboard that can be fully integrated with third-party content. However, there are very few customization options when you use [UISearchController](https://developer.apple.com/documentation/uikit/uisearchcontroller). You can not access the text field itself, customize the traits, or add input accessories.

[Detecting Gestures and Button Presses](DetectingButtonPressesandGestures.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbrfvbuqmjwfvjvomi)

[Working with Game Controllers](WorkingwithGameControllers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbrfvbuqmjyfvjvomi)
