---
title: iOS 7.0 Release Notes
apple_id: TP40013202
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2013-10-22'
source_url: https://developer.apple.com/library/archive/releasenotes/General/RN-iOSSDK-7.0/index.html
archived_at: '2026-07-18T02:54:42.068404Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# iOS SDK Release Notes for iOS 7 GM

#### Contents:

- [Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztembsfvbuqmjnknlte)
- [Bug Reporting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztembsfvbuqmjnknltg)
- [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztembsfvbuqmjnknlti)

### Introduction

iOS SDK 7.0.3 provides support for developing iOS apps, and it includes the complete set of Xcode tools, compilers, and frameworks for creating apps for iOS and OS X. These tools include the Xcode IDE and the Instruments analysis tool, among many others.

With this software you can develop apps for iPhone, iPad, or iPod touch running iOS 7. You can also test your apps using the included iOS Simulator, which supports iOS 7. iOS SDK 7.0.3 requires a Mac computer running OS X v10.8.4 (Mountain Lion) or later.

This version of iOS is intended for installation only on devices registered with the Apple Developer Program. Attempting to install this version of iOS in an unauthorized manner could put your device in an unusable state.

For more information and additional support resources, visit [http://developer.apple.com/programs/ios/](https://developer.apple.com/programs/ios/).

### Bug Reporting

To report any bugs not mentioned in the [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztembsfvbuqmjnknlti) section, use the Apple Bug Reporter on the Apple Developer website ([http://developer.apple.com/bugreporter/](https://developer.apple.com/bugreporter/)). Additionally, you may discuss these issues and iOS SDK 7.0.3 in the Apple Developer Forums: [http://devforums.apple.com](http://devforums.apple.com/). To get more information about iCloud for Developers, go to [http://developer.apple.com/icloud](https://developer.apple.com/icloud).

### Notes and Known Issues

The following issues relate to using iOS SDK 7.0.3 to develop code.

### 64-Bit Runtime

### Notes

Applications can now target iOS 5.1.1 and later while building for 64-bit using the “Standard architecture (including 64-bit)” build setting. This produces an Archive for the App Store with a single binary containing both 32-bit and 64-bit components. During development and testing, you must build only 32-bit when targeting an iOS 5.1.1 device (this is the default in Xcode).

### Accessibility

### Notes

The callback for `UIAccessibilityRequestGuidedAccessSession()` is executed on the global queue. Therefore, if you intend to performing any main-queue work in the callback provided, you must ensure to synchronize that work back to the main queue.

### Address Book

### Notes

The classes in the `AddressBookUI` framework now explicitly disallow subclassing. For apps linked against the iOS 7 SDK, attempting to initialize a subclass of one of these classes returns nil. For apps linked against older SDKs, the only behavior change is a warning logged to the console.

### App Deployment

### Notes

Comparing `[[[UIDevice currentDevice] identifierForVendor] UUIDString]` on multiple Enterprise applications or applications installed via Xcode (not the App Store), where the bundleIDs differ only in the last component, will result in identical strings. If the bundleID has 3 or less components, this behavior is unchanged from iOS 6.

This is due to a change in behavior between iOS 6 and iOS 7 where `-[UIDevice identifierForVendor]` takes into account the bundleID if there is no Vendor ID. Vendor ID is only assigned to apps on the App Store.

### AV Foundation

### Notes

- [AVCaptureSession](https://developer.apple.com/documentation/avfoundation/avcapturesession) now uses your app’s [AVAudioSession](https://developer.apple.com/documentation/avfoundation/avaudiosession) by default.
- `+[AVPlayer playerWithPlayerItem:]` returns an [AVPlayer](https://developer.apple.com/documentation/avfoundation/avplayer) object, but the current item will return nil if the player was created on another thread.

### Bluetooth

### Known Issue

32-bit apps running on a 64-bit device cannot attach to BTServer.

### Contacts

### Known Issue

If you created birthdays using a beta version of iOS 7, the birthday information may have been saved incorrectly. To correct such a birthday that displays incorrectly, edit the contact and change the date.

### Core Animation

### Notes

When the `[UIViewGroupOpacity](../../../documentation/General/Reference/InfoPlistKeyReference/Articles/iPhoneOSKeys.md#apple-f4xwc4dqnrsv64tfmyxwi33df5ygy2ltoqxws3tgn4xvkskwnfsxor3sn52xat3qmfrws5dz)` key is not present, the default value is now YES. The default was previously NO.

This means that subviews of a transparent view will first be composited onto that transparent view, then the precomposited subtree will be drawn as a whole onto the background. A NO setting results in less expensive, but also less accurate, compositing: each view in the transparent subtree is composited onto what’s underneath it, according to the parent’s opacity, in the normal painter’s algorithm order.

### Foundation

### Notes

- An `NSMetadataQuery` with ubiquitous scope can now use `kMDItemContentTypeTree` in predicates. For example:

```
NSPredicate *p = [NSComparisonPredicate                predicateWithLeftExpression:[NSExpression expressionForKeyPath:@"kMDItemContentTypeTree"]                            rightExpression:[NSExpression expressionForConstantValue:@"public.rtf"]                                   modifier: NSAnyPredicateModifier                                       type:NSLikePredicateOperatorType                                    options:0];
```
- When called on results returned by queries with ubiquitous scopes, `-[NSMetadataItem valueForAttribute:NSMetadataItemDisplayNameKey]` now produces the same value as `-[NSURL getResourceValue: forKey: NSURLLocalizedNameKey]`, matching nonubiquitous queries.

### GLKit

### Known Issue

If loaded with [GLKTextureLoader](https://developer.apple.com/documentation/glkit/glktextureloader), pngcrush images that have alpha are unpremultiplied.

__Workaround:__ You can either use a format other than PNG or turn off Xcode’s pngcrush option. To turn off Xcode’s pngcrush option, set Compress PNG Files to No in Xcode’s Build Settings. If you turn off pngcrush in Xcode, also set the [GLKTextureLoaderApplyPremultiplication](https://developer.apple.com/documentation/glkit/glktextureloaderapplypremultiplication) flag to true.

### High Precision Timers

### Known Issue

When sleeping or waiting for extremely precise time intervals, timers may be delayed by up to 1 millisecond.

### iCloud

### Notes

- The `kSecAttrSynchronizable` APIs that were available in the Beta seeds are not available in the GM Seed.
- Activation Lock, a new feature of Find My iPhone, is turned on automatically when Find My iPhone is enabled on any device running iOS 7. Activation Lock requires users to enter their Apple ID and password to turn off Find My iPhone, sign out of iCloud, erase the device, or reactivate the device after an erase. It’s important to do one of the following before transferring a device to a new user:

  - Sign out of iCloud.
  - Turn off Activation Lock in Settings > iCloud > Find My iPhone.

### iTunes Radio

### Notes

If you used iTunes Radio in seeds prior to the GM Seed, you need to sign out of your account and sign back in. Otherwise, your stations won’t update. To do this, go to Settings > iTunes & App Store. Select your Apple ID and then Sign Out. Then, enter your Apple ID and password, and Sign In.

### MapKit

### Notes

If the calls to `renderInContext` on the layer backing an [MKMapView](https://developer.apple.com/documentation/mapkit/mkmapview) are made off the main thread, they should be eliminated or moved to the main thread. Failure to do so can cause an app crash. Instead of using `renderInContext`, use the new [MKMapSnapshotter](https://developer.apple.com/documentation/mapkit/mkmapsnapshotter) APIs.

### Media

### Notes

iOS now remembers the last used media app across reboot and app crashes. Media apps that can receive remote control events should be prepared to be launched in the background and potentially receive a remote control event to begin playback. Additionally, it’s important that media apps monitor and handle the media server reset event, since the media app may receive a remote request to resume playback after a reset. Notifications to monitor these media server events are available in [AVAudioSession](https://developer.apple.com/documentation/avfoundation/avaudiosession), and proper handling is described in _[AVAudioSession - General recommendations for handling AVAudioSessionMediaServicesWereResetNotification](https://developer.apple.com/library/archive/qa/qa1749/_index.html#//apple_ref/doc/uid/DTS40011192)_.

### Multipeer Connectivity

### Notes

- The following new method on [MCSession](https://developer.apple.com/documentation/multipeerconnectivity/mcsession) has been implemented:

```objc
- (NSOutputStream *)startStreamWithName:(NSString *)streamName toPeer:(MCPeerID *)peerID error:(NSError **)error
```

  This delegate method has been implemented:

```objc
- (void)session:(MCSession *)session didReceiveStream:(NSInputStream *)stream withName:(NSString *)streamName fromPeer:(MCPeerID *)peerID
```
- The following new method on [MCSession](https://developer.apple.com/documentation/multipeerconnectivity/mcsession) has been implemented:

```objc
- (NSProgress *)sendResourceAtURL:(NSURL *)resourceURL withName:(NSString *)resourceName toPeer:(MCPeerID *)peerID withCompletionHandler:(void(^)(NSError *error))completionHandler
```

  The delegate method to start receiving a resource from remote peer has been implemented as:

```objc
- (void)session:(MCSession *)session didStartReceivingResourceWithName:(NSString *)resourceName fromPeer:(MCPeerID *)peerID withProgress:(NSProgress *)progress
```

  The delegate method to finish receiving a resource from remote peer and save the content in a temporary location is implemented as:

```objc
- (void)session:(MCSession *)session didFinishReceivingResourceWithName:(NSString *)resourceName fromPeer:(MCPeerID *)peerID atURL:(NSURL *)localURL withError:(NSError *)error
```

  > [!NOTE]
  > 
- [MCAdvertiserAssistant](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistant) is a convenience class for implementing an Advertiser, which handles invitations and connections to an [MCSession](https://developer.apple.com/documentation/multipeerconnectivity/mcsession).
- [MCSession](https://developer.apple.com/documentation/multipeerconnectivity/mcsession) has a new [initWithPeer:](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/1407000-initwithpeer) method.
- `sendResource` has added “with” to the `completionHandler`.
- The timeout has been removed from `connectPeer:withNearbyConnectionData`.

For more information on these APIs, watch _WWDC 2013: Nearby Networking with Multipeer Connectivity_.

### Multitasking

### Notes

- [AVAudioSession](https://developer.apple.com/documentation/avfoundation/avaudiosession) can no longer become active by apps in the background that wake due to Background Fetch, Background Transfers, and Remote Notification events.
- The time limit for task completion has decreased from the 10 minutes it was in iOS 6.

### Networking

### Notes

Two low-level networking APIs that used to return a MAC address now return the fixed value _02:00:00:00:00:00_. The APIs in question are `sysctl (NET_RT_IFLIST)` and `ioctl (SIOCGIFCONF)`. Developers using the value of the MAC address should migrate to identifiers such as `-[UIDevice identifierForVendor]`. This change affects all apps running on iOS 7.

### Objective-C Runtime

### Notes

Due to changes in how the `isa` field is implemented, `*self` may change during enumeration (for example, if the container is retained).

__Workaround:__ When implementing `countByEnumeratingWithState`, do not set `state->mutationsPtr = self`.

### Passbook

### Notes

- Passbook has added support for the major and minor fields to better match the rest of the iBeacon ecosystem. The new `major` and `minor` keys are independently variable options alongside `proximityUUID` (required) in each dictionary in the `beacons` array.
- In previous versions of the iOS SDK, Passbook did not validate the back fields on passes completely. The validation rules have not changed, but validation is now including back fields. Please check the console log for additional logs.
- [PKPassLibraryDidCancelAddPasses](https://developer.apple.com/documentation/passkit/pkpasslibraryaddpassesstatus/pkpasslibrarydidcanceladdpasses) is a new status code in the [PKPassLibraryAddPassesStatus](https://developer.apple.com/documentation/passkit/pkpasslibraryaddpassesstatus) enum. It signifies that the user tapped Cancel in an add-passes alert.

### Photos

### Notes

Upon upgrading from an earlier seed, photo thumbnails in the Photos app will not appear for a short while.

### Safari

### Known Issue

If upgrading to the GM Seed from an earlier seed, Safari preferences may be lost.

__Workaround:__ Disable passcode lock before you upgrade.

### Security

### Notes

- `-[UIDevice uniqueIdentifier]` is no longer accepted in submissions to the App Store. In iOS 7, apps that are already on the store or on users’ devices that call this removed API will no longer be returned the UDID. Instead, `-[UIDevice uniqueIdentifier]` will return a 40-character string starting with _FFFFFFFF_, followed by the hex value of `-[UIDevice identifierForVendor]`. It is important to consider how this will affect existing apps. Consider submitting updates that no longer access the UDID.
- iOS now requests user consent for apps to use audio input on all iOS 7 devices. For devices sold in China, iOS will also request user consent for apps to use the camera hardware. The operating system will present the consent alert when you set the category of the instantiated [AVAudioSession](https://developer.apple.com/documentation/avfoundation/avaudiosession). The [AVAudioSession](https://developer.apple.com/documentation/avfoundation/avaudiosession) categories that will present the alert are [AVAudioSessionCategoryRecord](https://developer.apple.com/documentation/avfoundation/avaudiosession/category/1616451-record) and [AVAudioSessionCategoryPlayAndRecord](https://developer.apple.com/documentation/avfoundation/avaudiosession/category/1616568-playandrecord).

  If the user doesn’t allow access, the audio session data will be all zeros (silence). For devices where camera access is requested and denied by the user, the video capture session is a black screen.
- The API `gethostuuid()` has been removed and will not be accepted for submission to the store, regardless of the targeted OS. For existing apps running on iOS 7, the function will return a _uuid_t_ representation of the vendor identifier (`-[UIDevice identifierForVendor]`).

### Social

### Notes

- Through iOS 6, when using `TWTweetComposeViewController` and [SLComposeViewController](https://developer.apple.com/documentation/social/slcomposeviewcontroller) (the latter only for Twitter and Weibo, but not Facebook), if the caller supplies a `completionHandler`, the supplied `completionHandler` is responsible for dismissing the view controller. As of iOS 7, if the app links against the iOS 7 SDK, the view controller will dismiss itself, even if the caller supplies a `completionHandler`. To avoid this, the caller’s `completionHandler` should not dismiss the view controller.
- When using the iOS 6.1 SDK on OS X v10.8 Mountain Lion, if you use the iOS 5.0 or iOS 5.1 Legacy SDK in iOS Simulator, you will not be able to use Twitter features: attempting to sign in to Twitter via the Settings pane will fail, and `Twitter.framework` will not work correctly. If you need to test Twitter features, you will need to choose either an iOS 6.1 or iOS 6.0 Simulator run destination, or you can test with iOS 5.x on a device.

### Springboard

### Notes

- Active touches are no longer canceled when the user takes a screenshot.
- Dynamic wallpaper is not available on iPhone 4.

### Stores

### Fixed in GM Seed

App downloads no longer get stuck in the “Waiting” state.

### UIKit

### Fixed in GM Seed

Password fields were not displayed in alert views for apps in landscape (for example, Game Center authentication or In-App Purchase).

### Known Issues

- If a [UITextField](https://developer.apple.com/documentation/uikit/uitextfield) or a [UILabel](https://developer.apple.com/documentation/uikit/uilabel) that is baseline-aligned with constraints has attributes that change after the constraints have been added, the layout may be incorrect. The exception to this is `-setFont:` on [UILabel](https://developer.apple.com/documentation/uikit/uilabel), which should work as expected.

  __Workaround:__ Avoid making changes in [UITextField](https://developer.apple.com/documentation/uikit/uitextfield) or [UILabel](https://developer.apple.com/documentation/uikit/uilabel) after adding baseline-alignment constraints. If you must make changes, you should remove the constraints and then reapply them afterward. Note that this is a performance hit, so don’t do it unless it is necessary.
- The `backIndicatorTransitionMask` from a storyboard or a xib will not be interpreted correctly at runtime.

  __Workaround:__ Set the `backIndicatorTransitionMask` in code.

### Notes

- When there isn’t enough room in the navigation bar layout for the full text of the back button title, the navigation bar will substitute a generic short back title (in English, “Back”). If even that string is too long, the bar will show the back indicator chevron with no title.
- `+[UIPasteboard pasteboardWithName:create:]` and `+[UIPasteboard pasteboardWithUniqueName]` now unique the given name to allow only those apps in the same application group to access the pasteboard. If the developer attempts to create a pasteboard with a name that already exists and they are not part of the same app suite, they will get their own unique and private pasteboard. Note that this does not affect the system provided pasteboards, general, and find.
- Apps default to using the new view controller-based status bar management system. To opt out of this, add a value of NO for the `UIViewControllerBasedStatusBarAppearance` key to your Info.plist.
- When using Auto Layout to position a [UIButton](https://developer.apple.com/documentation/uikit/uibutton), if you set the content compression resistance or content hugging priority to minimum, the button will have ambiguous layout.

  __Workaround:__ Don’t use a content compression resistance or content hugging priority of less than 2 for [UIButton](https://developer.apple.com/documentation/uikit/uibutton).
- [UIScreenEdgePanGestureRecognizer](https://developer.apple.com/documentation/uikit/uiscreenedgepangesturerecognizer) allows you to perform actions in response to swipes over the edge of the screen using the same heuristics that the system uses for its own gestures. Use this if you have a navigation semantic of your own that doesn’t use [UINavigationController](https://developer.apple.com/documentation/uikit/uinavigationcontroller), but that should include this gesture (e.g., Safari).

  This gesture recognizer has a property that describes the edges on which it’s active. [UIRectEdge](https://developer.apple.com/documentation/uikit/uirectedge) is a new enum type that this property and `-[UIViewController edgesForExtendedLayout]` can share. [UIRectEdge](https://developer.apple.com/documentation/uikit/uirectedge) replaces `UIExtendedEdge`, which will be removed. The members of both have the same values. Use Xcode to replace all instances of “UIExtendedEdge” in your project with “UIRectEdge”.
- [UIButtonTypeInfoLight](https://developer.apple.com/documentation/uikit/uibuttontype/uibuttontypeinfolight), [UIButtonTypeInfoDark](https://developer.apple.com/documentation/uikit/uibuttontype/uibuttontypeinfodark), and [UIButtonTypeDetailDisclosure](https://developer.apple.com/documentation/uikit/uibuttontype/uibuttontypedetaildisclosure) buttons all look the same.
- Blurred layers are not available on iPhone 4.
- Parallax is not available on iPhone 4.
- Letterpress text is not available on iPhone 4.

### Weather

### Notes

Weather conditions are not animated on iPhone 4.

### WebKit

### Notes

- Previously, when the viewport parameters were modified, the old parameters were never discarded. This caused the viewport parameters to be additive.

  For example, if you started with _width=device-width_ and then changed it to _initial-scale=1.0_, you ended up with a computed viewport of _width=device-width, initial-scale=1.0_.

  In iOS 7, this has been addressed. Now you end up with with a computed viewport of _initial-scale=1.0_.
- Previously, when using _<meta name="viewport" content="initial-scale=1.0, user-scalable=1">_, the scale could be incorrect after rotation.

  Now, if a user has not scaled the page explicitly, the page is restored to its initial scale. Also, the current scale is now correctly restricted within the `min-scale`, `max-scale` bounds.
- In accordance with the CSS spec, the `background` CSS shorthand property now resets the value of the `background-size` property to `auto` when background size is not specified.

  Images larger than their containers and styled with the `background` property after the `background-size` property or the `-webkit-background-size` property will therefore appear twice the intended size on Retina display devices.

  You should now specify the `background-size` property or the `-webkit-background-size` property after the `background` shorthand property in the CSS stylesheet for the web content being displayed.

  The legacy behavior is available only for apps linked to an SDK prior to iOS 7.0 when running on iOS 7 or later.

  This issue affects both native apps that display web content and web pages viewed in Safari for iPhone.

### Known Issue

- Web apps and web clips created prior to Seed 4 will not stay in folders across reboot.

  __Workaround:__ Delete the old web app or web clip and recreate it in this seed by loading the content in Safari, tapping the Action button, and then “Add to Home Screen.”
