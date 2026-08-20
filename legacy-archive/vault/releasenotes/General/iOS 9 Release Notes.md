---
title: iOS 9 Release Notes
apple_id: TP40016202
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-10-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/RN-iOSSDK-9.0/index.html
archived_at: '2026-07-18T02:54:42.434910Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# iOS SDK Release Notes for iOS 9

#### Contents:

- [Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dembsfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mi)
- [Bug Reporting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dembsfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mq)
- [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dembsfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6my)

### Introduction

iOS SDK 9.0 provides support for developing iOS apps. It is packaged with a complete set of Xcode tools, compilers, and frameworks for creating apps for iOS and OS X. These tools include the Xcode IDE and the Instruments analysis tool, among many others.

With this software you can develop apps for iPhone, iPad, or iPod touch running iOS 9. You can also test your apps using the included Simulator, which supports iOS 9. iOS SDK 9.0 requires a Mac computer running OS X v10.10.3 (Yosemite) or later.

This version of iOS is intended for installation only on devices registered with the Apple Developer Program. Attempting to install this version of iOS in an unauthorized manner could put your device in an unusable state.

For more information and additional support resources, visit [http://developer.apple.com/programs/ios/](https://developer.apple.com/programs/ios/).

### Bug Reporting

For issues not mentioned in the Notes and Known Issues section, please file bugs through the Apple Developer website ([https://developer.apple.com/bug-reporting/ios/](https://developer.apple.com/bugreporter/)). Additionally, you may discuss these issues and iOS SDK 9.0 in the Apple Developer Forums. To get more information about iCloud for Developers, go to [http://developer.apple.com/icloud](https://developer.apple.com/icloud).

### Notes and Known Issues

The following issues relate to using iOS SDK 9.0 to develop code.

### App Store

### Note

iOS 9 enforces the [UILaunchImages](../../documentation/General/Information%20Property%20List%20Key%20Reference/iOS%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjsfvjvomry) requirement; apps can no longer declare the same launch image to support different interface orientations.

### Known Issue

Users might be prompted twice for credentials on the first In-App Purchase.

### Apple ID

### Notes

- Some users will be offered to turn on two-factor authentication on their Apple ID. For more information about two-factor authentication see [developer.apple.com/support/two-factor-authentication](https://forums.developer.apple.com/welcome).
- If you turn on two-factor authentication on your Apple ID, iTunes purchases on Mac and Windows and store purchases on Apple TV will require you to append a six-digit verification code to the end of your password the first time you use that device. The six-digit code will display automatically on your iOS 9 or OS X El Capitan devices, or can be sent to your trusted phone number via a text message or phone call.

### Apple Pay

### Note

The format of the postal code that is returned prior to full authorization has changed from iOS 8. In some cases, it may be truncated from what was previously being returned.

### AVFoundation

### Notes

- The `canUseNetworkResourcesForLiveStreamingWhilePaused` property has been added to [AVPlayerItem](https://developer.apple.com/documentation/avfoundation/avplayeritem). The default value is `NO` for apps linked on or after iOS 9.0 or OS X 10.11, but `YES` for apps that were linked earlier.

  To minimize power usage, set this property to `NO` if you do not need playback state to stay up to date while paused.
- [AVQueuePlayer](https://developer.apple.com/documentation/avfoundation/avqueueplayer) now supports a mixture of file-based media and HTTP Live Streaming media in its queue. Prior to this, you had to ensure that all items in the queue were of the same type.
- For apps linked against iOS 9 or later, the media interruption behavior for `AV(Queue)Player` has changed.

  Before iOS 9, apps could interrupt other media-playing clients by associating or adding [AVPlayerItem](https://developer.apple.com/documentation/avfoundation/avplayeritem) to [AVPlayer](https://developer.apple.com/documentation/avfoundation/avplayer) or by modifying the time or date of the current `AVPlayerItem` (using the `seekToTime:` or `seekToDate:` methods). In iOS 9, these operations interrupt only when `AVPlayer` object’s playback rate is changed to a non-zero value through the [rate](https://developer.apple.com/documentation/avfoundation/avplayer/1388846-rate) property or `play` method.
- Picture in Picture playback might stop and the Picture in Picture button might disappear when using [AVPlayerViewController](https://developer.apple.com/documentation/avkit/avplayerviewcontroller) for video playback and replacing the underlying `AVPlayer` object’s current item using [replaceCurrentItemWithPlayerItem:](https://developer.apple.com/documentation/avfoundation/avplayer/1390806-replacecurrentitem).
- The `cancelPictureInPicture` method is deprecated.

### Bluetooth

### Known Issue

Pairing a Miura MFI accessory to an iOS 9 device will not work.

__Workaround:__ Do not remove pairing after updating to iOS 9.

### CBCentralManager

### Note

The `retrievePeripherals:` and `retrieveConnectedPeripherals` methods were deprecated in iOS 7.0 and removed in iOS 9.0. Apps that use these methods will crash on launch or upon pairing an accessory.

### Foundation

### Notes

- There is new Foundation API that can be used to detect if the device is in Low Power Mode. See the updated _[Energy Efficiency Guide for iOS Apps](https://developer.apple.com/library/archive/documentation/Performance/Conceptual/EnergyGuide-iOS/index.html#//apple_ref/doc/uid/TP40015243)_ for details.
- Horizontal location constraints should consistently reference either left/right _or_ leading/trailing attributes. For apps linked against the iOS 9 SDK, [NSLayoutConstraint](https://developer.apple.com/documentation/uikit/nslayoutconstraint) will throw an exception if you attempt to create a constraint between a leading/trailing attribute _and_ a left/right attribute.

### iCloud Drive

### Note

The `fetchAllChanges` property on [CKFetchRecordChangesOperation](https://developer.apple.com/documentation/cloudkit/ckfetchrecordchangesoperation) has been deprecated, and will be removed in iOS 9.

### Keyboards

### Note

The setting to use a third-party keyboard as the default keyboard for text input is not always respected.

### Keychain

### Note

iCloud Keychain will not sync passwords and credit cards with betas of iOS 9 and OS X El Capitan.

### Music

### Note

When users plug in headphones or connect to Bluetooth or CarPlay in their car, their favorite music app appears on the lock screen or the car display.

For your app to be eligible for this, it must publish to Now Playing upon launch and consistently maintain a Now Playing state. A common practice upon launch is to continue playing the track from when the app was last exited.

### Known Issue

Some tracks you have previously purchased won’t play.

__Workaround:__ Sign out of the Store and then sign back in.

### Networking

### Notes

- When negotiating a TLS/SSL connection with Diffie-Hellman key exchange, iOS 9 requires a 1024-bit group or larger. These connections include:

  - Secure Web (HTTPS)
  - Enterprise Wi-Fi (802.1X)
  - Secure e-mail (IMAP, POP, SMTP)
  - Printing servers (IPPS)
- DHE_RSA cipher suites are now disabled by defaults in Secure Transport for TLS clients. This may cause failure to connect to TLS servers that only support DHE_RSA cipher suites. Applications that explicitly enable cipher suites using [SSLSetEnabledCiphers](https://developer.apple.com/documentation/security/1397188-sslsetenabledciphers) are not affected and will still use DHE_RSA cipher suites if explicitly enabled.

  Safari may see a “Safari can’t establish a secure connection to the server” error page. Safari and other clients of `CFNetwork` API ([NSURLSession](https://developer.apple.com/documentation/foundation/urlsession), [NSURLConnection](https://developer.apple.com/documentation/foundation/nsurlconnection), `CFHTTPStream`, `CFSocketStream` and Cocoa equivalent) will show “CFNetwork SSLHandshake failed” error in Console.

### On-Demand Resources

### Known Issue

New or changed on-demand resource assets packs that are added or changed as part of an app update may be inaccessible to the application.

__Workaround:__ Include the new or updated asset packs directly in the application bundle.

### ReplayKit

### Known Issue

Playing a video while ReplayKit recording is ON stops the ongoing recording session and the video fails to play.

### Restore

### Known Issue

If you’ve set a region that doesn’t match your language, restores from iCloud Backup might not progress.

__Workaround:__ During restore, change your region to match your language. You can change it back after the restore is over.

### Safari

### Notes

- When Done is tapped in a [SFSafariViewController](https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller), it is automatically dismissed. You no longer need to dismiss it in the delegate method [safariViewControllerDidFinish:](https://developer.apple.com/documentation/safariservices/sfsafariviewcontrollerdelegate/1621214-safariviewcontrollerdidfinish).
- “Find on Page” is now available both from the Share sheet as well as in the Completions List.
- Request Desktop Site has moved; it’s now in the Share sheet instead of Favorites.
- Web Browser–to–Native App Handoff does not work with your app if the `apple-app-site-association` file isn’t correctly formatted and signed. For more information, see _[Handoff Programming Guide](../../documentation/User%20Experience/Handoff%20Programming%20Guide/About%20Handoff.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2dgmzy)_ and _[Shared Web Credentials Reference](https://developer.apple.com/documentation/security/shared_web_credentials)_.

### Secure Transport

### Note

DHE_RSA cipher suites are now disabled by default in Secure Transport for TLS clients. This may cause failure to connect to TLS servers that only support DHE_RSA cipher suites. Applications that explicitly enable cipher suites using [SSLSetEnabledCiphers](https://developer.apple.com/documentation/security/1397188-sslsetenabledciphers) are not affected and will still use DHE_RSA cipher suites if explicitly enabled.

### UIKit

### Notes

- If initialized with a `nil` [nibName](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621487-nibname) value, `UIViewController.nibName` has always looked for a nib with a similar name as the view controller’s class, and defaulted to that value if [loadView](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621454-loadview) is not overridden.

  Prior to iOS 9, subclasses of `UIViewController` that were written in Swift would require that their corresponding nib file name include the module prefix.

  To improve flexibility in the event of refactoring, you can omit the module name from the nib filename in code that runs in iOS 9. `UIViewController.nibName` still prefers a name that contains the module prefix, but falls back to an unqualified name if a nib with the fully-qualified name is not found.
- In iOS 9, when [layoutIfNeeded](https://developer.apple.com/documentation/uikit/uiview/1622507-layoutifneeded) is sent to a view and all of the following conditions are satisfied (which is not common), we apply fitting-size constraints (width/height = 0 at `UILayoutPriorityFittingSizeLevel`) instead of required size constraints (width/height required to match current size):

  1. The receiver is not yet in the subtree of a view that hosts a layout engine, such as window, view controller view (unless you have set [translatesAutoresizingMaskIntoConstraints](https://developer.apple.com/documentation/uikit/uiview/1622572-translatesautoresizingmaskintoco) to `NO` on that view—or created constraints that have one item in its subtree and one item outside it), table view cell content view, and so on.
  2. The final ancestor (that is, top-level view) of the receiver has [translatesAutoresizingMaskIntoConstraints](https://developer.apple.com/documentation/uikit/uiview/1622572-translatesautoresizingmaskintoco) set to `NO`.
  3. The top-level view has a subview that is not a [UIViewController](https://developer.apple.com/documentation/uikit/uiviewcontroller)-owned layout guide that also has `translatesAutoresizingMaskIntoConstraints` set to `NO`.

  Under condition 1, we create a temporary layout engine from the top-level view and add all the constraints from the subtree to it. The problem is that we need to add some constraints that make the size of the top-level view unambiguous in the layout engine. The old behavior (prior to iOS 9) was that we would add constraints to restrict the size of the top-level view to its current bounds for any situation under condition 1. This really doesn’t make sense when you add conditions 2 and 3 and can result in unsatisfiable-constraints logging and broken layout.

  So in iOS 9, for this special case only, we use fitting-size constraints instead.

  This means that if you are sending [layoutIfNeeded](https://developer.apple.com/documentation/uikit/uiview/1622507-layoutifneeded) to a view under these conditions in iOS 9, you must be sure that either you have sufficient constraints to establish a size for the top-level view (which usually, though not always, is the receiver) or you must add temporary size constraints to the top-level view of layout size you desire before sending `layoutIfNeeded`, and remove them afterward.
- For apps linked on iOS 9 or later, [UITextView](https://developer.apple.com/documentation/uikit/uitextview) will now always correctly constrict its [NSTextContainer](https://developer.apple.com/documentation/appkit/nstextcontainer) to the fit inside the view when scrolling is disabled. Overflowing lines that lie outside of an `NSTextContainer`, even partially, are not rendered.

  In previous iOS releases, the `NSTextContainer` sometimes was not constricted in size. This meant that logically overflowing lines were erroneously rendered. If you are seeing previously rendered lines at the end of your text view no longer rendered after linking your app against iOS 9, this behavior change is the likely cause. You can remedy this by making your `UITextView` larger, or perhaps by adjusting the bottom value of the text view's [textContainerInset](https://developer.apple.com/documentation/uikit/uitextview/1618619-textcontainerinset) property.
- There is a redesigned UI for printing that includes a print preview (presented from [UIPrintInteractionController](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller) or [UIActivityViewController](https://developer.apple.com/documentation/uikit/uiactivityviewcontroller)). For apps that provide printing items or use only built-in `UIPrintFormatter` objects (such as [UISimpleTextPrintFormatter](https://developer.apple.com/documentation/uikit/uisimpletextprintformatter), [UIMarkupTextPrintFormatter](https://developer.apple.com/documentation/uikit/uimarkuptextprintformatter), `UIWebViewPrintFormatter`, or the [UIViewPrintFormatter](https://developer.apple.com/documentation/uikit/uiviewprintformatter) of any system-provided view), nothing additional is needed for the print preview to display.

  Apps that subclass [UIPrintPageRenderer](https://developer.apple.com/documentation/uikit/uiprintpagerenderer) or `UIPrintFormatter` to draw content for printing must be built with the iOS 9 SDK for the preview to display. The behavior of `UIPrintPageRenderer` has been updated to call [drawPageAtIndex:inRect:](https://developer.apple.com/documentation/uikit/uiprintpagerenderer/1621636-drawpageatindex) multiple times with potentially different page sizes and margins. Various methods on `UIPrintPageRenderer` may be called from a non-main thread, but never from multiple threads concurrently.
- [UIPickerView](https://developer.apple.com/documentation/uikit/uipickerview) and [UIDatePicker](https://developer.apple.com/documentation/uikit/uidatepicker) are now resizable and adaptive—previously, these views would enforce a default size even if you attempted to resize them. These views also now default to a width of 320 points on all devices, instead of to the device width on iPhone.

  Interfaces that rely on the old enforcement of the default size will likely look wrong when compiled for iOS 9. Any problems encountered can be resolved by fully constraining or sizing picker views to the desired size instead of relying on implicit behavior.

### Webkit

### Note

The `if-domain` and `unless-domain` value strings only match the exact domain. To match the domain and any subdomains, begin the string with the asterisk character (\*).
