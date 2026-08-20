---
title: iOS 10.1 Release Notes
apple_id: TP40017562
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/releasenotes/General/RN-iOSSDK-10.1/index.html
archived_at: '2026-07-18T02:54:41.547889Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# iOS SDK Release Notes for iOS 10.1

#### Contents:

- [Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tknrsfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mi)
- [Bug Reporting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tknrsfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mq)
- [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tknrsfvbuqmjnknltc)

### Introduction

iOS 10.1 SDK provides support for developing iOS apps. It’s packaged with a complete set of Xcode tools, compilers, and frameworks for creating apps for iOS and macOS. These tools include the Xcode IDE and the Instruments analysis tool, among many others.

With this software you can develop apps for iPhone, iPad, or iPod touch running iOS 10.1. You can also test your apps using the included iOS Simulator, which supports iOS 10.1. iOS 10.1 SDK requires a Mac computer running macOS 10.10.3 (Yosemite) or later.

This version of iOS is intended for installation only on devices registered with the Apple Developer Program. Attempting to install this version of iOS in an unauthorized manner could put your device in an unusable state.

For more information and additional support resources, visit [http://developer.apple.com/programs/ios/](https://developer.apple.com/programs/ios/).

### Bug Reporting

For issues not mentioned in [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tknrsfvbuqmjnknltc), please file bugs through the Apple Developer website [https://developer.apple.com/bug-reporting/](https://developer.apple.com/bug-reporting/). Additionally, you may discuss these issues and iOS 10.1 SDK in the Apple Developer Forums: [http://devforums.apple.com](http://devforums.apple.com/). To get more information about iCloud for Developers, go to [http://developer.apple.com/icloud](https://developer.apple.com/icloud).

### Notes and Known Issues

The following items relate to using iOS 10.1 SDK to develop code.

### Binary Compatibility

- Apple reserves two-letter prefixes for use in framework classes. When naming your own classes, please use a three-letter prefix. The guidelines can be reviewed at [Conventions](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/Conventions/Conventions.html#//apple_ref/doc/uid/TP40011210-CH10).

  Failure to follow these guidelines could result in your app crashing during beta software releases.
- Upon recompiling with iOS 10, calling [valueForKey:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/EOF/EOControl/Classes/NSObjectAdditions/Description.html#//apple_ref/occ/instm/NSObject/valueForKey:) with a `nil` key throws an exception. Previously, this led to undefined behavior; now, it causes your app to crash.
- Referencing a system font by name in a call to [fontWithName:size:](https://developer.apple.com/documentation/uikit/uifont/1619041-init) causes a crash. For more information, see [https://developer.apple.com/videos/play/wwdc2015/804/](https://developer.apple.com/videos/play/wwdc2015/804/).
- To improve customer privacy, HTTPS URLs, [NSURLSession](https://developer.apple.com/documentation/foundation/urlsession), and [NSURLConnection](https://developer.apple.com/documentation/foundation/nsurlconnection) no longer support RC4 cipher suites during the TLS handshake. Affected apps and services should upgrade web servers to use more modern cipher suites.
- Apps may hang if they change a superview’s geometry in [viewWillLayoutSubviews](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621437-viewwilllayoutsubviews) or [layoutSubviews](https://developer.apple.com/documentation/uikit/uiview/1622482-layoutsubviews).
- [NSURLConnection](https://developer.apple.com/documentation/foundation/nsurlconnection) disallows connections that use TLS protocol versions lower than the protocol version specified by an ATS policy via the `NSExceptionMinimumTLSVersion` or `NSThirdPartyExceptionMinimumTLSVersion` keys. Affected apps and services should upgrade web servers to use more modern TLS protocol versions. To learn more about ATS keys and values, see [App Transport Security](https://developer.apple.com/library/archive/releasenotes/General/WhatsNewIniOS/Articles/iOS9.html#//apple_ref/doc/uid/TP40016198-SW14).

### CFNetwork HTTP Protocol

The [NSMutableURLRequest](https://developer.apple.com/documentation/foundation/nsmutableurlrequest) class requires that the [HTTPBodyStream](https://developer.apple.com/documentation/foundation/nsmutableurlrequest/1409529-httpbodystream) property be an unopened stream, and the [NSURLConnection](https://developer.apple.com/documentation/foundation/nsurlconnection) and [NSURLSession](https://developer.apple.com/documentation/foundation/urlsession) classes now strictly enforce this unopened stream requirement. Affected apps should ensure that any [NSInputStream](https://developer.apple.com/documentation/foundation/inputstream) that is provided has not yet been opened.

### CloudKit

When building and running from Xcode repeatedly, long-lived operations can fail with a "You don’t have permission to save the file” error because the container path is changing repeatedly.

### HomeKit

Adding WAC HomeKit accessories might fail using the Home app if the network credentials are not first provided using the Settings > Wi-Fi > Set Up New Device option.

__Workaround:__ If adding such a HomeKit accessory fails, provide the network credentials using Settings > Wi-Fi > Set Up New Device. After the accessory has joined the network, the accessory can be added using the Home app.

### libdispatch

Libdispatch asserts if there is a hang detected due to a deadlock in `dispatch_barrier_sync`.

### Messages

- When [UISearchController](https://developer.apple.com/documentation/uikit/uisearchcontroller) and [UITableViewController](https://developer.apple.com/documentation/uikit/uitableviewcontroller) are used in Messages extensions, their content can be hidden below the top bar.

  __Workaround:__ Use insets of about 80 px on top and 40px on the bottom.
- In iOS Simulator only, when `localizedChangeDescription` in the `insertMessage:localizedChangeDescription:completionHandler:` method is set to `$localParticipantIdentifier.UUIDString`, the `$localParticipantIdentifier.UUIDString` is not replaced with the user’s Messages ID, and the [UUIDString](https://developer.apple.com/documentation/collaboration/cbidentity/1423879-uuidstring) is printed as-is.
- When the Messages app in the simulator is force quit, message history is lost.
- When a [UIAlertController](https://developer.apple.com/documentation/uikit/uialertcontroller) object is presented in a Messages extension, it is truncated by the bottom bar of the extension.
- If a sign-in dialog is displayed while performing an in-app purchase or attempting to buy content from the store, or the store or the extension will be dismissed.
- The local participant UUID is the same for both conversation participants in the simulator only.

  __Workaround:__ Use a device to test UUID comparisons.

### NSUserActivity

An [NSUserActivity](https://developer.apple.com/documentation/foundation/nsuseractivity) object may not have any `userInfo` content after handoff.

__Workaround:__ Explicitly call [becomeCurrent](https://developer.apple.com/documentation/foundation/nsuseractivity/1413665-becomecurrent) on the activity object.

### Photos

- People syncing is not enabled via iCloud Photo Library in iOS 10.
- Memories, Related, People, and Scene are not supported on 32-bit devices.

### Safari

- Web geolocation now requires a secure (HTTPS) website to work on both iOS and macOS to prevent malicious use of location data.
- [WKWebView](https://developer.apple.com/documentation/webkit/wkwebview) now defaults to respecting `user-scalable = no` from a viewport. Clients of `WKWebView` can improve accessibility and allow users to pinch-to-zoom on all pages by setting the [WKWebViewConfiguration](https://developer.apple.com/documentation/webkit/wkwebviewconfiguration) property [ignoresViewportScaleLimits](https://developer.apple.com/documentation/webkit/wkwebviewconfiguration/2274633-ignoresviewportscalelimits) to `YES`.
- The [SFSafariViewControllerConfiguration](https://developer.apple.com/documentation/safariservices/sfsafariviewcontrollerconfiguration) and [initWithURL:configuration:](https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller/1649141-initwithurl) APIs have been removed, and [initWithURL:entersReaderIfAvailable:](https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller/1621221-initwithurl) is no longer marked as deprecated. The [preferredBarTintColor](https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller/2274394-preferredbartintcolor) property has been moved to [SFSafariViewController](https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller), along with the new [preferredControlTintColor](https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller/2274393-preferredcontroltintcolor) property, which clients should use instead of setting `tintColor` directly on the view. Apps linked on iOS 10 or later will no longer forward their view's tint color to [SFSafariViewController](https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller).

### Setup Assistant

Customers using iPhone 7 or 7+ devices running iOS 10.0, 10.0.1, or 10.0.2 may be prompted twice with the iCloud Restore option when upgrading the device to iOS 10.1.

### UIKit

### Notes

- Prior to iOS 10, it was possible to override [initWithArrangedSubviews:](https://developer.apple.com/documentation/uikit/uistackview/1616240-initwitharrangedsubviews), but this was intended as a convenience initializer and implemented as such. We have now enforced this in the headers. As a result, Swift clients can no longer override this method, because Swift initializer rules prevent the override of a convenience initializer.
- In iOS 10, UIKit has updated and unified background management for [UINavigationBar](https://developer.apple.com/documentation/uikit/uinavigationbar), [UITabBar](https://developer.apple.com/documentation/uikit/uitabbar), and [UIToolbar](https://developer.apple.com/documentation/uikit/uitoolbar). In particular, changes to background properties of these views (such as background or shadow images, or setting the bar style) may kick off a layout pass for the bar to resolve the new background appearance.

  In particular, this means that attempts to change the background appearance of these bars inside of [layoutSubviews](https://developer.apple.com/documentation/uikit/uiview/1622482-layoutsubviews), -[UIView updateConstraints], [viewWillLayoutSubviews](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621437-viewwilllayoutsubviews), [viewDidLayoutSubviews](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621398-viewdidlayoutsubviews), [updateViewConstraints](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621379-updateviewconstraints), or any other method that is called in response to layout may result in a layout loop.

  In some cases you can break these layout loops by ensuring that you always use the same object instance when objects (such as [UIImage](https://developer.apple.com/documentation/uikit/uiimage) or [UIColor](https://developer.apple.com/documentation/uikit/uicolor)) are required. But in general you should avoid doing this.

  Because all appearance parameters are now resolved at one time, there may be some cases where your bar's appearance has changed. In general, best results are obtained by specifying as little as possible for customizing your bar. For example, if you are specifying a `barTintColor` value and specifying an empty [UIImage](https://developer.apple.com/documentation/uikit/uiimage) object for the `backgroundImage` property (as is the case when you call `[UIImage new]`, for example) then you should get better results by specifying only the `barTintColor`. Any changes you make to resolve these issues in iOS 10 should also work correctly in iOS 9—if this is not the case, please report bugs with a sample project and a screenshot indicating what the bars should look like.
- In iOS 10, there is a slight [UIGestureRecognizer](https://developer.apple.com/documentation/uikit/uigesturerecognizer) behavior change when removing a currently recognizing (that is, midflight) gesture recognizer from its view. Previously, removing the gesture recognizer midflight would not explicitly cancel the gesture recognizer, allowing you to re-add the gesture recognizer back to the same view or to a different view. In iOS 10, calling [removeGestureRecognizer:](https://developer.apple.com/documentation/uikit/uiview/1622413-removegesturerecognizer) on the view of a midflight gesture recognizer explicitly cancels the gesture recognizer. If a user desires to change the view of a midflight gesture recognizer, you can simply call [addGestureRecognizer:](https://developer.apple.com/documentation/uikit/uiview/1622496-addgesturerecognizer) on the view you wish to move the gesture recognizer to.
- Presented view controllers can now affect the status bar appearance even if they were presented from a view controller that did not affect the status bar (for example, a popover). By default, custom view controller presentations are assumed to not affect the status bar; use the [modalPresentationCapturesStatusBarAppearance](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621453-modalpresentationcapturesstatusb) property to allow a presented view controller to participate in status bar appearance.
- It has always been a requirement that [UIViewController](https://developer.apple.com/documentation/uikit/uiviewcontroller) subclasses call super’s implementation of [awakeFromNib](https://developer.apple.com/documentation/objectivec/nsobject/1402907-awakefromnib) from their own overrides. Starting in iOS 10, `awakeFromNib` is correctly annotated with the `NS_REQUIRES_SUPER` attribute to detect implementations that fail to obey this requirement. To fix this warning, ensure that all code paths of your override call `awakeFromNib`.
- When running on iPad, the background color set for a [UITableViewCell](https://developer.apple.com/documentation/uikit/uitableviewcell) in a Storyboard is now respected.
- Starting in iOS 10, [UITableViewHeaderFooterView](https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview) supports [NSCoding](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSCoding/Description.html#//apple_ref/occ/intf/NSCoding) so if a view with this class is in a XIB, it now decodes correctly. The consequence is that apps may exhibit some extra content for these views which did not appear before due to the bug that was fixed.
- For very wide table views where cell layout margins have been automatically increased to follow the readable width, separator insets are now interpreted relative to these left and right margins instead of from the edges of the table view.
- The coalescing of [UITouch](https://developer.apple.com/documentation/uikit/uitouch) delivery has been significantly improved, especially in cases where users would both touch the screen and use Apple Pencil at the same time on iPad Pro and the app wasn’t able to process them at the incoming rate. In certain scenarios, events still can come in at a higher rate than the display refreshes. This is expected, and your app should anticipate this and handle accordingly.
- In iOS 10, windows that are not full screen do not affect status bar appearance.
- Sending [layoutIfNeeded](https://developer.apple.com/documentation/uikit/uiview/1622507-layoutifneeded) to a view is not expected to move the view, but in earlier releases, if the view had [translatesAutoresizingMaskIntoConstraints](https://developer.apple.com/documentation/uikit/uiview/1622572-translatesautoresizingmaskintoco) set to `NO`, and if it was being positioned by constraints, `layoutIfNeeded` would move the view to match the layout engine before sending layout to the subtree.

  These changes correct this behavior, and the receiver’s position and usually its size won’t be affected by `layoutIfNeeded`.

  Some existing code may be relying on this incorrect behavior that is now corrected. There is no behavior change for binaries linked before iOS 10, but when building on iOS 10 you may need to correct some situations by sending -`layoutIfNeeded` to a superview of the [translatesAutoresizingMaskIntoConstraints](https://developer.apple.com/documentation/uikit/uiview/1622572-translatesautoresizingmaskintoco) view that was the previous receiver, or else positioning and sizing it before (or after, depending on your desired behavior) `layoutIfNeeded`.
- Third party apps with custom [UIView](https://developer.apple.com/documentation/uikit/uiview) subclasses using Auto Layout that override [layoutSubviews](https://developer.apple.com/documentation/uikit/uiview/1622482-layoutsubviews) and dirty layout on `self` before calling super are at risk of triggering a layout feedback loop when they rebuild on iOS 10. When they are correctly sent subsequent `layoutSubviews` calls they must be sure to stop dirtying layout on self at some point (note that this call was skipped in release prior to iOS 10).
- Flippable images work by having two images in an asset, each with a different directionality trait. When you create a derived [UIImage](https://developer.apple.com/documentation/uikit/uiimage) object using the `imageWith…` methods, it is no longer associated with the image asset it came from. To create a flippable template image at runtime, use [UIImageAsset](https://developer.apple.com/documentation/uikit/uiimageasset).
- The source of the `UIContentSizeCategoryDidChangeNotification` notification is now `UIScreen.main()` instead of `UIApplication.shared()`.
- There are two properties in the [UIViewPropertyAnimator](https://developer.apple.com/documentation/uikit/uiviewpropertyanimator) class and one method in the [UIViewAnimating](https://developer.apple.com/documentation/uikit/uiviewanimating) protocol that are unavailable in iOS 10 beta 2.

  - `UIViewPropertyAnimator`:

    [manualHitTestingEnabled](https://developer.apple.com/documentation/uikit/uiviewpropertyanimator/2097548-manualhittestingenabled)

    [delay](https://developer.apple.com/documentation/uikit/uiviewpropertyanimator/2097549-delay)
  - `UIViewAnimating`:

    [startAnimationAfterDelay:](https://developer.apple.com/documentation/uikit/uiviewanimating/2097540-startanimation)

### Known Issue

For [UIImage](https://developer.apple.com/documentation/uikit/uiimage) objects that are created from [CIImage](https://developer.apple.com/documentation/coreimage/ciimage) objects, the drawing methods [drawInRect:](https://developer.apple.com/documentation/uikit/uiimage/1624092-drawinrect) and [drawAtPoint:](https://developer.apple.com/documentation/uikit/uiimage/1624132-draw) always convert to the `DeviceRGB` color space before drawing. This results in loss of extended color information when drawing into a wide-color graphics context.

__Workaround:__ You can retrieve the underlying [CIImage](https://developer.apple.com/documentation/coreimage/ciimage) via the [CIImage](https://developer.apple.com/documentation/uikit/uiimage/1624129-ciimage) property and render it using a [CIContext](https://developer.apple.com/documentation/coreimage/cicontext) created with the appropriate color space (Extended sRGB) and pixel format (full-float).

A [UIImage](https://developer.apple.com/documentation/uikit/uiimage) object that is created from `CGImageRef` is not affected, and will draw correctly without loss of color information.

### Widgets

The first time you debug a widget on a device, it does not show as a possible app extension.

__Workaround:__ Debug again for the widget to show up.

### Xcode

- Occasionally, using Command-Shift-HH from the Home screen does not invoke the app switcher.

  __Workaround:__ Launch any app before using Command-Shift-HH.
- Protocol methods in the Intents framework require `@objc` annotation to be properly bridged between Obj-C and Swift 2.3.
