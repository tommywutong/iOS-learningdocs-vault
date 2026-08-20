---
title: tvOS SDK Release Notes for tvOS 10.0
apple_id: TP40017542
resource_type: Release Note
platform: tvOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/RN-tvOSSDK-10.0/index.html
archived_at: '2026-07-18T02:54:43.119581Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# tvOS SDK Release Notes for tvOS 10.0

#### Contents:

- [Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tknbsfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mi)
- [Bug Reporting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tknbsfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mq)
- [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tknbsfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6my)

### Introduction

The tvOS SDK leverages many of the same frameworks and technologies that you’re already using for iOS development. However, please note that all libraries and frameworks used in your tvOS apps must be built for tvOS, including any 3rd-party libraries. Do not link your tvOS app against frameworks or libraries that are not built with tvOS. Attempting to do so will result in a build failure. Furthermore, bitcode is required for all tvOS apps. All apps and frameworks in the app bundle must include bitcode.

tvOS 10 SDK provides support for developing tvOS apps. It’s packaged with a complete set of Xcode tools, compilers, and frameworks for creating apps for tvOS. These tools include the Xcode IDE and the Instruments analysis tool, among many others.

This version of tvOS is intended for installation only on devices registered with the Apple Developer Program. Attempting to install this version of tvOS in an unauthorized manner could put your device in an unusable state.

### Bug Reporting

For issues not mentioned in the Notes and Known Issues section, please file bugs through the Apple Developer website ([https://developer.apple.com/bug-reporting/](https://developer.apple.com/bugreporter/)). Additionally, you may discuss these issues and tvOS SDK 10.0 in the Apple Developer Forums: [https://forums.developer.apple.com/](https://forums.developer.apple.com/).

### Notes and Known Issues

### CFNetwork HTTPProtocol

The [NSMutableURLRequest](https://developer.apple.com/documentation/foundation/nsmutableurlrequest) class requires that the [HTTPBodyStream](https://developer.apple.com/documentation/foundation/nsmutableurlrequest/1409529-httpbodystream) property be an unopened stream, and the [NSURLConnection](https://developer.apple.com/documentation/foundation/nsurlconnection) and [NSURLSession](https://developer.apple.com/documentation/foundation/urlsession) classes now strictly enforce this unopened stream requirement. Affected apps should ensure that any [NSInputStream](https://developer.apple.com/documentation/foundation/inputstream) that is provided has not yet been opened.

### libstdc++

Support for libstdc++ has been removed from the tvOS SDK beginning with tvOS 9.2.

> [!NOTE]
> 

### SSL/TLS

__Notes__:

- [NSURLConnection](https://developer.apple.com/documentation/foundation/nsurlconnection) disallows connections that use TLS protocol versions lower than the protocol version specified by an ATS policy via the `NSExceptionMinimumTLSVersion` or `NSThirdPartyExceptionMinimumTLSVersion` keys.
This is now being enforced as of tvOS 10. Affected apps and services should upgrade web servers to use more modern TLS protocol versions.
- To improve customer privacy, when an HTTPS URL is specified, [NSURLSession](https://developer.apple.com/documentation/foundation/urlsession) and [NSURLConnection](https://developer.apple.com/documentation/foundation/nsurlconnection) no longer support RC4 cipher suites during the TLS handshake. Affected apps and services should upgrade web servers to use more modern cipher suites.

  In Console, your app will show -1200 and -98xx errors that did not appear in the previous release ([NSURLErrorSecureConnectionFailed](https://developer.apple.com/documentation/foundation/1508628-url_loading_system_error_codes/nsurlerrorsecureconnectionfailed) and SecureTransport errors, respectively).

  (CFNetwork) HTTP load failed (error code: -1200 [3:-9824]

  (CFNetwork) NSURLConnection finished with error - code -1200

  To determine if a particular URL is affected by this change, on OS X, use nscurl <url>. If the load fails, and nscurl --enable-rc4 <url> succeeds, then the web server only supports RC4 cipher suites and will need to be upgraded.

  Please note that another reason you may see identical errors is because of a change where App Transport Security `NSExceptionMinimumTLSVersion` or `NSThirdPartyExceptionMinimumTLSVersion` is now being respected for [NSURLConnection](https://developer.apple.com/documentation/foundation/nsurlconnection).

### Simulator

Switching between Light and Dark appearance can be done in the Simulator by using the “Shift + Command + d” keyboard shortcut.

### UIKit

### Known Issue

When a search keyboard is configured to be explicitly dark, The “Hold to dictate search” text may appear in a dark color.

### Note

On tvOS 9, a [UITableView](https://developer.apple.com/documentation/uikit/uitableview) object’s contentInset would modify the fading mask applied to the top and bottom of the table. Content scrolled off the top of the UITableView would begin fading out a short distance from the top of the contentInset, and be completely obscured at the top of the contentInset.

This behavior has changed for apps built with tvOS 10 or later. The fading effect now always happens at the top and bottom of the [UITableView](https://developer.apple.com/documentation/uikit/uitableview)’s frame, and the contentInset only affects scrolling margin, as it does on iOS. There is one exception; a [UITableView](https://developer.apple.com/documentation/uikit/uitableview) object inside of a [UINavigationController](https://developer.apple.com/documentation/uikit/uinavigationcontroller) object will have the top of the mask inset to leave room for the [UINavigationBar](https://developer.apple.com/documentation/uikit/uinavigationbar).

To achieve the previous behavior, it may be necessary to adjust the frame of a `UITableView`. If the system-provided mask does not meet your needs, you can provide your own masking view using the `UITableView`’s [maskView](https://developer.apple.com/documentation/uikit/uiview/1622557-maskview) property.
