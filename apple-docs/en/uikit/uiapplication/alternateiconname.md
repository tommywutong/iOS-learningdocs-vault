---
title: alternateIconName
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.3+, iPadOS 10.3+, Mac Catalyst 13.1+, tvOS 10.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiapplication/alternateiconname
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/alternateiconname'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/alternateiconname.json'
content_hash: 'sha256:337ff072e43b98e8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# alternateIconName

<sub>Instance Property</sub>

The name of the icon the system displays for the app.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var alternateIconName: String? { get }
```

## Discussion

When the system is displaying one of your app’s alternate icons, the value of this property is the name of the alternate icon (from your app’s `Info.plist` file). When the system is displaying your app’s primary icon, the value of this property is `nil`.

## See Also

### Managing the app’s icon

- [supportsAlternateIcons](supportsalternateicons.md) — A Boolean value that indicates whether the app is allowed to change its icon.
- [- setAlternateIconName:completionHandler:](<setalternateiconname(__completionhandler_).md>) — Changes the icon the system displays for the app.
