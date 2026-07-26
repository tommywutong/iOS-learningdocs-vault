---
title: LSMinimumSystemVersion
framework: Bundle Resources
symbol_kind: typealias
role: symbol
role_heading: Property List Key
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/bundleresources/information-property-list/lsminimumsystemversion
source_url: 'https://developer.apple.com/documentation/bundleresources/information-property-list/lsminimumsystemversion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/bundleresources/information-property-list/lsminimumsystemversion.json'
content_hash: 'sha256:103d20fa40ec623f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Bundle Resources](../../bundleresources.md) · [Information Property List](../information-property-list.md)

# LSMinimumSystemVersion

<sub>Property List Key</sub>

The minimum version of the operating system required for the app to run in macOS.

## Discussion

Use this key to indicate the minimum macOS release that your app supports. The App Store uses this key to indicate the macOS releases on which your app can run, and to show compatibility with a person’s Mac.

Starting with macOS 11.4, the lowest version number you can specify as the value for the [LSMinimumSystemVersion](lsminimumsystemversion.md) key is:

- `10` if your app links against the macOS SDK.
- `10.15` if your app links against the iOS 14.3 SDK (or later) and builds using Mac Catalyst.
- `11` if your iPad or iPhone app links against the iOS 14.3 SDK (or later) and can run on a Mac with Apple silicon.

To specify the minimum version of iOS, iPadOS, tvOS, or watchOS that your app supports, use [MinimumOSVersion](minimumosversion.md).

## See Also

### Operating system version

- [LSMinimumSystemVersionByArchitecture](lsminimumsystemversionbyarchitecture.md) — The minimum version of macOS required for the app to run on a set of architectures.
- [MinimumOSVersion](minimumosversion.md) — The minimum version of the operating system required for the app to run in iOS, iPadOS, tvOS, and watchOS.
- [LSRequiresIPhoneOS](lsrequiresiphoneos.md) — A Boolean value indicating whether the app must run in iOS.
- [WKApplication](wkapplication.md)
- [WKWatchKitApp](wkwatchkitapp.md) — A Boolean value that indicates whether the bundle is a watchOS app.
