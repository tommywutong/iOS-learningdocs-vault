---
title: watchOS 3.0 Release Notes
apple_id: TP40017541
resource_type: Release Note
platform: watchOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/RN-watchOSSDK-3.0/index.html
archived_at: '2026-07-18T02:54:43.714040Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# Release Notes

#### Contents:

- [Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tknbrfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mi)
- [Bug Reporting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tknbrfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mq)
- [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tknbrfvbuqmjnknltc)

### Introduction

watchOS SDK 3.0 provides support for developing watchOS apps. It is packaged with a complete set of Xcode tools, compilers, and frameworks for creating apps for watchOS. These tools include the Xcode IDE and the Instruments analysis tool, among many others.

This version of watchOS is intended for installation only on devices registered with the Apple Developer Program. Attempting to install this version of watchOS in an unauthorized manner could put your device in an unusable state.

For more information and additional support resources, visit [http://developer.apple.com/programs/](https://developer.apple.com/programs/).

### Bug Reporting

For issues not mentioned in [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tknbrfvbuqmjnknltc), please file bugs through the Apple Developer website [https://developer.apple.com/bug-reporting/](https://developer.apple.com/bug-reporting/). Additionally, you may discuss these issues and watchOS SDK 3.0 in the Apple Developer Forums at [http://devforums.apple.com](http://devforums.apple.com/).

### Notes and Known Issues

The following items relate to using watchOS 3.0 SDK to develop code.

### Activity

For Activity Sharing to properly function, ensure that every paired Apple Watch is running watchOS 3.

### Apple Pay

A payment card may show as unavailable when attempting to use Apple Pay after restarting Apple Watch.

__Workaround:__ Dismiss and double-tap the side button again to make the payment.

### Background Refresh

Violations of system resources will result in a crash report for your application. The exception code provides context about the nature of the violation:

|  |  |
| --- | --- |
| **0xc51bad01** | : The app used too much CPU time. |
| **0xc51bad02** | : The app took too much wall time. |
| **0xc51bad03** | : The app may not have had sufficient runtime to complete the task. |

### Watch Connectivity

- Apple Watch may get into a state that fails to receive watch connectivity transmission.

  __Workaround:__ Reboot Apple Watch.
- In some first deploy scenarios, `isComplicationEnabled == NO` for watch connectivity after a complication is configured on the clock face.

  __Workaround:__ Reboot Apple Watch.
- A file received by watch connectivity might have an additional suffix after the filename.

### HomeKit

Using [enableNotification:completionHandler:](https://developer.apple.com/documentation/homekit/hmcharacteristic/1624189-enablenotification) on Apple Watch causes `homed` to hang.

__Workaround:__ Use [enableNotification:completionHandler:](https://developer.apple.com/documentation/homekit/hmcharacteristic/1624189-enablenotification) on the iOS device instead.

### Networking

To improve customer privacy, HTTPS URLs, NSURLSession, and NSURLConnection no longer support RC4 cipher suites during the TLS handshake. Affected apps and services should upgrade web servers to use more modern cipher suites.

In Console, your app will show `-1200` and `-98xx` errors that did not appear in the previous release (that is, `NSURLError` `secureConnectionFailed` and `SecureTransport` errors, respectively).

- (CFNetwork) `HTTP load failed (error code: –1200 [3:-9824])`
- (CFNetwork) `NSURLConnection finished with error code –1200`

To determine if a particular URL is affected by this change, on macOS use `nscurl <url>`. If the load fails, and `nscurl --enable-rc4 <url>` succeeds, then the web server supports only RC4 cipher suites and needs to be upgraded.

Note that another reason you may see identical errors is because of a change where App Transport Security `NSExceptionMinimumTLSVersion` or `NSThirdPartyExceptionMinimumTLSVersion` is now being respected for [NSURLConnection](https://developer.apple.com/documentation/foundation/nsurlconnection). To learn more about ATS keys, see [NSAppTransportSecurity](../../documentation/General/Information%20Property%20List%20Key%20Reference/Cocoa%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvomzt).

### NSURLConnection

[NSURLConnection](https://developer.apple.com/documentation/foundation/nsurlconnection) disallows connections that use TLS protocol versions lower than the protocol version specified by an ATS policy via the `NSExceptionMinimumTLSVersion` or `NSThirdPartyExceptionMinimumTLSVersion` keys. To learn more about ATS keys, see [NSAppTransportSecurity](../../documentation/General/Information%20Property%20List%20Key%20Reference/Cocoa%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvomzt).

__Workaround:__ This is now being enforced as of the WWDC 2016 seed. Affected apps and services should upgrade web servers to use more modern TLS protocol versions.

### NSURLSession

The [NSMutableURLRequest](https://developer.apple.com/documentation/foundation/nsmutableurlrequest) class requires that the [HTTPBodyStream](https://developer.apple.com/documentation/foundation/nsurlrequest/1407341-httpbodystream) property be an unopened stream. The [NSURLConnection](https://developer.apple.com/documentation/foundation/nsurlconnection) and [NSURLSession](https://developer.apple.com/documentation/foundation/urlsession) classes now strictly enforce this unopened stream requirement. Affected apps should ensure that any [NSInputStream](https://developer.apple.com/documentation/foundation/inputstream) that is provided has not yet been opened.

### Snapshot

Periodic updates have been disabled for WatchKit apps that have not adopted the new [handleBackgroundTasks:](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/1650877-handlebackgroundtasks) API available in watchOS 3. Adopt this new method to ensure that your app is given periodic updates.

### WatchKit

### Notes

- SpriteKit and SceneKit scenes are paused when an app goes to the Dock.
- When a WatchKit app is in an active debug session and in the background, you can send background tasks to the app through the Debug menu. “Simulate Background Refresh” sends a [WKApplicationRefreshBackgroundTask](https://developer.apple.com/documentation/watchkit/wkapplicationrefreshbackgroundtask) and “Simulate UI Snapshot” sends a [WKSnapshotRefreshBackgroundTask](https://developer.apple.com/documentation/watchkit/wksnapshotrefreshbackgroundtask). Note that these tasks do not have any user info data that may have been registered from a previous request from the app. Also note that these tasks are not sent if the app is in the foreground.
- T[WKInterfaceController](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller) methods [handleActionWithIdentifier:forRemoteNotification:](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/1619530-handleactionwithidentifier) and [handleActionWithIdentifier:forLocalNotification:](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/1619516-handleactionwithidentifier) are unavailable for watchOS 3. This API should only be called via iOS.
- You need to manually resume your [SCNScene](https://developer.apple.com/documentation/scenekit/scnscene) objects when the interface controller that holds them is activated after the app comes to the foreground.

### Known Issues

- The determination of whether a WatchKit app implements [handleBackgroundTasks:](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/1650877-handlebackgroundtasks) in its [WKExtensionDelegate](https://developer.apple.com/documentation/watchkit/wkextensiondelegate) is made at launch time and never updated. If your WatchKit app sets `[WKExtension sharedExtension].delegate` after being launched, it will not properly be checked.

  __Workaround:__ Use the [WKExtensionDelegate](https://developer.apple.com/documentation/watchkit/wkextensiondelegate) that is designated in your `Info.plist` file.
- watchOS Simulator can enter a state in which updating app context and transferring user info and files to iOS Simulator fails. Sending message and message data also takes longer than expected.
- `SecAccessControlCreateWithFlags` does not work in watchOS 3.
- watchOS apps that link against `AVFoundation.framework` will not build for the Simulator.
- Attempting to reload an interface controller object that contains a SpriteKit or SceneKit control while in the background causes a crash.

  __Workaround:__ Mark SpriteKit and SceneKit controls as paused in Interface Builder, and resume them only when the extension is marked as being in the foreground.
- At simulator first launch, watch connectivity communication could be clogged or slowed down for several minutes.

  __Workaround:__ Wait for all watch-to-phone communications to come through.
- `NSLog()` messages are not printed in Xcode’s debug console when running on watch

  __Workaround:__ Install the `sysdiagnose` logging profile on Apple Watch to reinstate logging.
