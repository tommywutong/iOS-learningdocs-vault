---
title: supportsAlternateIcons
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.3+, iPadOS 10.3+, Mac Catalyst 13.1+, tvOS 10.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiapplication/supportsalternateicons
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/supportsalternateicons'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/supportsalternateicons.json'
content_hash: 'sha256:308a392f565e759c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# supportsAlternateIcons

<sub>Instance Property</sub>

A Boolean value that indicates whether the app is allowed to change its icon.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var supportsAlternateIcons: Bool { get }
```

## Discussion

The value of this property is [true](../../swift/true.md) only when the system allows you to change the icon of your app. To declare your app’s alternate icons, include them in the [CFBundleIcons](../../bundleresources/information-property-list/cfbundleicons.md) key of your app’s `Info.plist` file.

The value of this property is always [false](../../swift/false.md) for apps built using the visionOS SDK.

## See Also

### Managing the app’s icon

- [alternateIconName](alternateiconname.md) — The name of the icon the system displays for the app.
- [- setAlternateIconName:completionHandler:](<setalternateiconname(__completionhandler_).md>) — Changes the icon the system displays for the app.
