---
title: 'canOpenURL(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+（27.0 起废弃）, iPadOS 3.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiapplication/canopenurl(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/canopenurl(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/canopenurl%28_%3A%29.json'
content_hash: 'sha256:a60e25e01c4e0d35'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# canOpenURL(_:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether an app is available to handle a URL scheme.

> [!warning] Deprecated
> Attempt to open the URL and handle any failure instead of validating it first. Using universal links instead of custom URL schemes removes the need for this validation entirely.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
nonisolated func canOpenURL(_ url: URL) -> Bool
```

## Parameters

- `url` — A URL (Universal Resource Locator). At runtime, the system determines if the device has an installed app registered to handle the URL’s scheme. The device can have more than one app registered to handle a scheme. The URL can have a common scheme such as `http`, `https`, `tel`, or `facetime`, or a custom scheme. For information about supported schemes, see [Apple URL Scheme Reference](https://developer.apple.com/library/archive/featuredarticles/iPhoneURLScheme_Reference/Introduction/Introduction.html#//apple_ref/doc/uid/TP40007899).

## Return Value

[false](../../swift/false.md) if the device doesn’t have an installed app registered to handle the URL’s scheme, or if you haven’t declared the URL’s scheme in your `Info.plist` file; otherwise, [true](../../swift/true.md).

## Discussion

When this method returns [true](../../swift/true.md), iOS guarantees subsequent calls to the [- openURL:options:completionHandler:](<open(__options_completionhandler_).md>) method with the same URL will successfully launch an app that can handle the URL. The return value doesn’t indicate the validity of the URL, whether the specified resource exists, or, in the case of a universal link, whether the device has an installed app registered to respond to the universal link.

You can call this method safely on a thread that isn’t the main thread.

> [!important] Important
> If you link your app on or after iOS 9.0, you must declare the URL schemes you pass to this method by adding the `LSApplicationQueriesSchemes` key to your app’s `Info.plist` file. This method always returns [false](../../swift/false.md) for undeclared schemes, even if the device doesn’t have a registered app installed. Apps linked on or after iOS 15 are limited to a maximum of 50 entries in the `LSApplicationQueriesSchemes` key. Apps linked on or after iOS 27 are limited to a maximum of 25 entries in the `LSApplicationQueriesSchemes` key. To learn more about the key, see [LSApplicationQueriesSchemes](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/LaunchServicesKeys.html#//apple_ref/doc/plist/info/LSApplicationQueriesSchemes).

If you link your app against an earlier version of iOS but it is running in iOS 9.0 or later, you can call this method up to 50 times. After reaching that limit, subsequent calls always return [false](../../swift/false.md). If the user reinstalls or upgrades the app, iOS resets the limit.

Unlike this method, the [- openURL:options:completionHandler:](<open(__options_completionhandler_).md>) method isn’t constrained by the `LSApplicationQueriesSchemes` requirement. If an app is available to handle the URL, the system will launch it, even if you haven’t declared the scheme.

Using universal links instead of custom URL schemes removes the need to use this method to validate target links; if no app is available to handle a universal link, iOS routes it to the person’s default browser, allowing the associated website to respond. For more information on universal links, see [Allowing apps and websites to link to your content](../../xcode/allowing-apps-and-websites-to-link-to-your-content.md).

## See Also

### Related Documentation

- [- openURL:](<openurl(__).md>) — Attempts to open the resource at the specified URL. _(deprecated)_

### Opening a URL resource

- [- openURL:options:completionHandler:](<open(__options_completionhandler_).md>) — Attempts to asynchronously open the resource at the specified URL.
- [OpenExternalURLOptionsKey](openexternalurloptionskey.md) — Options for opening a URL.
