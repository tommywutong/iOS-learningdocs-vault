---
title: Text Programming Guide for iOS
apple_id: TP40009542
resource_type: Guide
platform: tvOS|iOS
topic: Data Management
technology: UIKit
published: '2018-01-16'
source_url: https://developer.apple.com/library/archive/documentation/StringsTextFonts/Conceptual/TextAndWebiPhoneOS/InputViews/InputViews.html
archived_at: '2026-07-18T02:06:58.382828Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Text Programming Guide for iOS](About%20Text%20Handling%20in%20iOS.md)


[Next](Displaying%20and%20Managing%20the%20Edit%20Menu.md)[Previous](Copy%2C%20Cut%2C%20and%20Paste%20Operations.md)

# Custom Views for Data Input

UIKit allows apps to substitute custom input views for the system keyboard. It also enables apps to have an accessory view above the system keyboard or custom input view. Additionally, it enables apps to play key-click sounds when users tap on a controls of an input view or input accessory view.

The UIKit [framework](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Framework.html#//apple_ref/doc/uid/TP40008195-CH56) includes support for custom input [views](https://developer.apple.com/library/archive/documentation/General/Conceptual/Devpedia-CocoaApp/ViewObject.html#//apple_ref/doc/uid/TP40009071-CH5) and input accessory views. Your app can substitute its own input view for the system keyboard when users edit text or other forms of data in a view. For example, an app could use a custom input view to enter characters from a runic alphabet. You may also attach an input accessory view to the system keyboard or to a custom input view; this accessory view runs along the top of the main input view and can contain, for example, [controls](https://developer.apple.com/library/archive/documentation/General/Conceptual/Devpedia-CocoaApp/Control.html#//apple_ref/doc/uid/TP40009071-CH7) that affect the text in some way or labels that display some information about the text.

To get this feature if your app is using [UITextView](https://developer.apple.com/documentation/uikit/uitextview) and [UITextField](https://developer.apple.com/documentation/uikit/uitextfield) objects for text editing, simply assign custom views to the [inputView](https://developer.apple.com/documentation/uikit/uitextfield/1619620-inputview) and [inputAccessoryView](https://developer.apple.com/documentation/uikit/uitextfield/1619627-inputaccessoryview) properties. Those custom views are shown when the text object becomes [first responder](https://developer.apple.com/library/archive/documentation/General/Conceptual/Devpedia-CocoaApp/Responder.html#//apple_ref/doc/uid/TP40009071-CH1).

You are not limited to input views and input accessory views in framework-supplied text objects. Any class inheriting directly or indirectly from [UIResponder](https://developer.apple.com/documentation/uikit/uiresponder) (usually a custom view) can specify its own input view and input accessory view. The `UIResponder` class declares two [properties](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/DeclaredProperty.html#//apple_ref/doc/uid/TP40008195-CH13) for input views and input accessory views:

```objc
@property (readonly, retain) UIView *inputView;
@property (readonly, retain) UIView *inputAccessoryView;
```

When the responder object becomes the first responder and [inputView](https://developer.apple.com/documentation/uikit/uiresponder/1621092-inputview) (or [inputAccessoryView](https://developer.apple.com/documentation/uikit/uiresponder/1621119-inputaccessoryview)) is not `nil`, UIKit animates the input view into place below the parent view (or attaches the input accessory view to the top of the input view). The first responder can reload the input and accessory views by calling the [reloadInputViews](https://developer.apple.com/documentation/uikit/uiresponder/1621110-reloadinputviews) method of `UIResponder`.

The `UITextView` class redeclares the [inputView](https://developer.apple.com/documentation/uikit/uiresponder/1621092-inputview) and [inputAccessoryView](https://developer.apple.com/documentation/uikit/uiresponder/1621119-inputaccessoryview) properties as `readwrite`. Clients of `UITextView` objects need only obtain the input and input-accessory views—either by loading a [nib file](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/NibFile.html#//apple_ref/doc/uid/TP40008195-CH34) or creating the views in code—and assign them to their properties. Custom view classes (and other subclasses that inherit from `UIResponder`) should redeclare one or both of these properties and their backing instance variables and override the [getter method](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/AccessorMethod.html#//apple_ref/doc/uid/TP40008195-CH2) for the property—that is, don’t synthesize the properties’ accessor methods. In their getter-method implementations, they should return it the view, loading or creating it if it doesn’t already exist.

You have a lot of flexibility in defining the size and content of an input view or input accessory view. Although the height of these views can be what you’d like, they should be the same width as the system keyboard. If UIKit encounters an input view with a [UIViewAutoresizingFlexibleHeight](https://developer.apple.com/documentation/uikit/uiviewautoresizing/uiviewautoresizingflexibleheight) value in its autoresizing mask, it changes the height to match the keyboard. There are no restrictions on the number of subviews (such as controls) that input views and input accessory views may have. For more guidance on input views and input accessory views, see _iOS Human Interface Guidelines_.

To load a nib file at run time, first create the input view or input accessory view in Interface Builder. Then at runtime get the app’s main [bundle](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Bundle.html#//apple_ref/doc/uid/TP40008195-CH4) and call [loadNibNamed:owner:options:](https://developer.apple.com/documentation/foundation/bundle/1618147-loadnibnamed) on it, passing the name of the nib file, the File’s Owner for the nib file, and any options. This method returns an array of the top-level objects in the nib, which includes the input view or input accessory view. Assign the view to its corresponding property. For more on this subject, see [Nib Files](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/LoadingResources/CocoaNibs/CocoaNibs.html#//apple_ref/doc/uid/10000051i-CH4) in _[Resource Programming Guide](../../Cocoa/Resource%20Programming%20Guide/About%20Resources.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2tc2i)_.

Listing 6-1 illustrates a custom view class lazily creating its input accessory view in the `inputAccessoryView` getter method.

__Listing 6-1__  Creating an input accessory view programmatically

```objc
- (UIView *)inputAccessoryView {
    if (!inputAccessoryView) {
        CGRect accessFrame = CGRectMake(0.0, 0.0, 768.0, 77.0);
        inputAccessoryView = [[UIView alloc] initWithFrame:accessFrame];
        inputAccessoryView.backgroundColor = [UIColor blueColor];
        UIButton *compButton = [UIButton buttonWithType:UIButtonTypeRoundedRect];
        compButton.frame = CGRectMake(313.0, 20.0, 158.0, 37.0);
        [compButton setTitle: @"Word Completions" forState:UIControlStateNormal];
        [compButton setTitleColor:[UIColor blackColor] forState:UIControlStateNormal];
        [compButton addTarget:self action:@selector(completeCurrentWord:)
            forControlEvents:UIControlEventTouchUpInside];
        [inputAccessoryView addSubview:compButton];
    }
    return inputAccessoryView;
}
```

The subviews of an input view and input accessory view can be anything you want. If they are buttons or other controls, you need to specify [targets and actions](https://developer.apple.com/library/archive/documentation/General/Conceptual/Devpedia-CocoaApp/TargetAction.html#//apple_ref/doc/uid/TP40009071-CH3) for each control and implement the associated action methods to perform data input or manipulation.

Just as it does with the system keyboard, UIKit posts [UIKeyboardWillShowNotification](https://developer.apple.com/documentation/uikit/uiresponder/1621576-keyboardwillshownotification), [UIKeyboardDidShowNotification](https://developer.apple.com/documentation/uikit/uiresponder/1621602-keyboarddidshownotification), [UIKeyboardWillHideNotification](https://developer.apple.com/documentation/uikit/uikeyboardwillhidenotification), and [UIKeyboardDidHideNotification](https://developer.apple.com/documentation/uikit/uikeyboarddidhidenotification) notifications. The object observing these notifications can get geometry information related to the input view and input accessory view and adjust the edited view accordingly. See [Keyboards and Input Methods](https://developer.apple.com/library/archive/documentation/StringsTextFonts/Conceptual/TextAndWebiPhoneOS/KeyboardManagement/KeyboardManagement.html#//apple_ref/doc/uid/TP40009542-CH5-SW2) for examples and related information.

You can play standard system keyboard clicks when a user taps in your custom input views and keyboard accessory views. First, adopt the `UIInputViewAudioFeedback` protocol in your input view. Then, call the [playInputClick](https://developer.apple.com/documentation/uikit/uidevice/1620050-playinputclick) method when responding to a key tap in the view.

Perform the following three steps to adopt the [UIInputViewAudioFeedback](https://developer.apple.com/documentation/uikit/uiinputviewaudiofeedback) protocol:

1. In your Xcode project, create a subclass of the [UIView](https://developer.apple.com/documentation/uikit/uiview) class. In the header file, indicate that the subclass conforms to the `UIInputViewAudioFeedback` protocol, as follows:

```objc
@interface KeyboardAccessoryView : UIView <UIInputViewAudioFeedback> {
}
```
2. In the implementation file for your `UIView` subclass, implement the [enableInputClicksWhenVisible](https://developer.apple.com/documentation/uikit/uiinputviewaudiofeedback/1620038-enableinputclickswhenvisible) method, as follows:

```objc
- (BOOL) enableInputClicksWhenVisible {
    return YES;
}
```
3. Finally, in the Interface Builder document for your custom input or accessory view, select the View object. In the Identity inspector, set the class for the object to be your `UIView` subclass.

To play an input click for a key tap in a custom input or keyboard accessory view, first ensure that view adopts the [UIInputViewAudioFeedback](https://developer.apple.com/documentation/uikit/uiinputviewaudiofeedback) protocol as described in [Adopting the UIInputViewAudioFeedback Protocol](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tknbsfvbuqmjsfvjvoni). Then, for each tap that you want to provide a click sound for, call the [playInputClick](https://developer.apple.com/documentation/uikit/uidevice/1620050-playinputclick) method of the [UIDevice](https://developer.apple.com/documentation/uikit/uidevice) class, as follows:

```objc
- (void) playClickForCustomKeyTap {
   [[UIDevice currentDevice] playInputClick];
}
```

The system automatically manages the audio session for custom input clicks, including audio ducking as needed. (For information on audio sessions, see _[Audio Session Programming Guide](../../Audio/Audio%20Session%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tqnzv)_.)

[Next](Displaying%20and%20Managing%20the%20Edit%20Menu.md)[Previous](Copy%2C%20Cut%2C%20and%20Paste%20Operations.md)

