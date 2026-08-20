---
title: Adopting 3D Touch on iPhone
apple_id: TP40016543
resource_type: Guide
platform: Safari (Mobile)|iOS
topic: User Experience
technology: UIKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/Adopting3DTouchOniPhone/3DTouchAPIs.html
archived_at: '2026-07-18T02:09:46.462536Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Adopting 3D Touch on iPhone](index.md)



## 3D Touch APIs

iOS 9 provides the following 3D Touch APIs:

- The __Home screen quick action API__ is for adding shortcuts to your app icon that anticipate and accelerate a user’s interaction with your app.
- The __UIKit peek and pop API__ lets you provide easy access, within your app, to additional content while maintaining the user’s context. Use the peek quick actions API to provide a press-enabled replacement to your app’s touch-and-hold actions.
- The __Web view peek and pop API__ lets you enable system-mediated previews of HTML link destinations.
- The __UITouch force properties__ let you add customized force-based user interaction to your app.

No matter which of these APIs you adopt, your app must check the availability of 3D Touch at runtime.

### Checking for 3D Touch Availability

To check at runtime whether a device supports 3D Touch, read the value of the [forceTouchCapability](https://developer.apple.com/documentation/uikit/uitraitcollection/1623515-forcetouchcapability) property on the trait collection for any object that has a trait environment (see_[UITraitEnvironment Protocol Reference](https://developer.apple.com/documentation/uikit/uitraitenvironment)_). A user can turn off 3D Touch while your app is running, so read this property as part of your implementation of the [traitCollectionDidChange:](https://developer.apple.com/documentation/uikit/uitraitenvironment/1623516-traitcollectiondidchange) delegate method.

To ensure that all your users can access your app’s features, branch your code depending on whether 3D Touch is available. When it is available, take advantage of 3D Touch capabilities. When it is not available, provide alternatives such as by employing touch and hold, implemented with the [UILongPressGestureRecognizer](https://developer.apple.com/documentation/uikit/uilongpressgesturerecognizer) class.

Refer to _iOS Human Interface Guidelines_ for ideas on how to enhance your app’s interactions for users with 3D Touch-capable devices while not leaving your other users behind.

### Home Screen Quick Actions

iOS 9 supports Home screen _static_ and _dynamic_ quick actions.

- __Static quick actions__ are available to the user immediately upon app installation. Define Home screen static quick actions in your app’s `Info.plist` file in the [UIApplicationShortcutItems](../../General/Information%20Property%20List%20Key%20Reference/iOS%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjsfvjvomzw) array.
- __Dynamic quick actions__ are available to the user after first launch. Define Home screen dynamic quick actions with the [UIApplicationShortcutItem](https://developer.apple.com/documentation/uikit/uiapplicationshortcutitem), [UIMutableApplicationShortcutItem](https://developer.apple.com/documentation/uikit/uimutableapplicationshortcutitem), and [UIApplicationShortcutIcon](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticon) classes. Add dynamic quick actions to your app’s shared [UIApplication](https://developer.apple.com/documentation/uikit/uiapplication) object using the [shortcutItems](https://developer.apple.com/documentation/uikit/uiapplication/1623033-shortcutitems) property.

iOS 9 displays up to four Home screen quick actions for your app. Within this limit, the system shows your static quick actions first, starting at the topmost position in the menu. If your static items do not exhaust the limit and you have also defined dynamic quick actions, then one or more of your dynamic quick actions is displayed.

Home screen static and dynamic quick action can each display up to two lines of text along with an icon. The system formats the text, wrapping it, aligning it, and adding ellipses as appropriate. For the icon of a quick action, use one of the system template icons available via the [iconWithType:](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticon/1623389-init) class method of the [UIApplicationShortcutIcon](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticon) class. If you want to instead use a custom icon, it must be a template (that is, stencil-like) image, which you can create using that class’s [iconWithTemplateImageName:](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticon/1623367-init) class method.

The Home screen Quick Actions feature supports Voice Over.

For details on implementing Home screen quick actions, read the following material:

- Home Screen Quick Actions and Template Icons in _iOS Human Interface Guidelines_
- _[ApplicationShortcuts: Using UIApplicationShortcutItems](https://developer.apple.com/library/archive/samplecode/ApplicationShortcuts/Introduction/Intro.html#//apple_ref/doc/uid/TP40016545)_ (sample code)
- [UIApplicationShortcutItems](../../General/Information%20Property%20List%20Key%20Reference/iOS%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjsfvjvomzw) in _[Information Property List Key Reference](../../General/Information%20Property%20List%20Key%20Reference/About%20Info.plist%20Keys%20and%20Values.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenbx)_
- _[UIApplicationShortcutItem Class Reference](https://developer.apple.com/documentation/uikit/uiapplicationshortcutitem)_
- _[UIMutableApplicationShortcutItem Class Reference](https://developer.apple.com/documentation/uikit/uimutableapplicationshortcutitem)_
- _[UIApplicationShortcutIcon Class Reference](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticon)_

### UIKit Peek and Pop

iOS 9 lets you configure view controllers for the user features of _peek_, which provides a preview of additional content when a user presses on a specified view, and _pop_, which commits to viewing that content and navigates to it.

To support peek and pop on 3D Touch-capable devices, the iOS 9 SDK includes:

- New methods in the [UIViewController](https://developer.apple.com/documentation/uikit/uiviewcontroller) class for registering and unregistering a view controller for participation in 3D Touch
- New view controller protocols to support 3D Touch

You can optionally configure a preview view controller to include a set of _peek quick actions_, or deep links into your app. A user can obtain peek quick actions by swiping a peek upward.

To support peek quick actions, the iOS 9 SDK includes:

- The new [UIPreviewAction](https://developer.apple.com/documentation/uikit/uipreviewaction) and [UIPreviewActionGroup](https://developer.apple.com/documentation/uikit/uipreviewactiongroup) classes
- The new [UIPreviewActionItem](https://developer.apple.com/documentation/uikit/uipreviewactionitem) protocol

For details on implementing peek and pop and for implementing peek quick actions, read the following material:

- 3D Touch in _iOS Human Interface Guidelines_
- The descriptions for the [registerForPreviewingWithDelegate:sourceView:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621463-registerforpreviewingwithdelegat) and [unregisterForPreviewingWithContext:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621395-unregisterforpreviewingwithconte) methods in _[UIViewController Class Reference](https://developer.apple.com/documentation/uikit/uiviewcontroller)_
- _[UIViewControllerPreviewing Protocol Reference](https://developer.apple.com/documentation/uikit/uiviewcontrollerpreviewing)_, which describes the interface adopted by the context object for a 3D Touch-enabled view controller
- _[UIViewControllerPreviewingDelegate Protocol Reference](https://developer.apple.com/documentation/uikit/uiviewcontrollerpreviewingdelegate)_, which describes the interface for providing a preview view controller (_peek_, in user terminology) in response to a user force touch, and for providing a commit view controller (_pop_, in user terminology) in response to a deeper press on the preview
- _[UIPreviewAction Class Reference](https://developer.apple.com/documentation/uikit/uipreviewaction)_, which describes a peek quick action
- _[UIPreviewActionGroup Class Reference](https://developer.apple.com/documentation/uikit/uipreviewactiongroup)_, which describes submenu-like grouping of peek quick actions
- _[UIPreviewActionItem Protocol Reference](https://developer.apple.com/documentation/uikit/uipreviewactionitem)_, which describes the interface adopted by peek quick actions and groups
- _[ViewControllerPreviews: Using the UIViewController previewing APIs](../../../samplecode/ViewControllerPreviews-%20Using%20the%20UIViewController%20previewing%20APIs/ViewControllerPreviews-%20Using%20the%20UIViewController%20previewing%20APIs.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dknbw)_ (sample code)

### Web View Peek and Pop

In web views, you can enable peek and pop for links and for detected data using the new `allowsLinkPreview` property. In iOS 9, this property is available in the recommended [WKWebView](https://developer.apple.com/documentation/webkit/wkwebview) class (in the WebKit framework) and in the older [UIWebView](https://developer.apple.com/documentation/uikit/uiwebview) class (in the UIKit framework).

Peek and pop for links and detected data work automatically with the [SFSafariViewController](https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller) (Safari view controller) class in the Safari Services framework.

### Force Properties in UITouch Objects

The [UITouch](https://developer.apple.com/documentation/uikit/uitouch) class has two new properties to support custom implementation of 3D Touch in your app: [force](https://developer.apple.com/documentation/uikit/uitouch/1618110-force) and [maximumPossibleForce](https://developer.apple.com/documentation/uikit/uitouch/1618121-maximumpossibleforce). For the first time on iOS devices, these properties let you detect and respond to touch pressure in the [UIEvent](https://developer.apple.com/documentation/uikit/uievent) objects your app receives.

On iPhone, the force of a touch has a high dynamic range, available as a floating point value to your app.

For details on providing a custom implementation of 3D Touch using force values, read the following material:

- The descriptions for the [force](https://developer.apple.com/documentation/uikit/uitouch/1618110-force) and [maximumPossibleForce](https://developer.apple.com/documentation/uikit/uitouch/1618121-maximumpossibleforce) properties in _[UITouch Class Reference](https://developer.apple.com/documentation/uikit/uitouch)_
- _[TouchCanvas: Using UITouch efficiently and effectively](https://developer.apple.com/library/archive/samplecode/TouchCanvas/Introduction/Intro.html#//apple_ref/doc/uid/TP40016561)_ (sample code)

[Getting Started with 3D Touch](index.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dknbtfvbuqmjnknltc)
