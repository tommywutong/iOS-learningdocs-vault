---
title: hasColors
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipasteboard/hascolors
source_url: 'https://developer.apple.com/documentation/uikit/uipasteboard/hascolors'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipasteboard/hascolors.json'
content_hash: 'sha256:98b706947110ba87'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPasteboard](../uipasteboard.md)

# hasColors

<sub>Instance Property</sub>

A Boolean value that indicates whether the pasteboard contains contains a nonempty array of colors.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var hasColors: Bool { get }
```

## Discussion

Employ this property to determine if a pasteboard contains color data.

Do not use the [color](color.md) or [colors](colors.md) properties to determine whether a pasteboard contains color data, because doing so consumes resources needlessly.

## See Also

### Checking for data types on a pasteboard

- [hasImages](hasimages.md) — A Boolean value that indicates whether the pasteboard contains a nonempty array of images.
- [hasStrings](hasstrings.md) — A Boolean value that indicates whether the pasteboard contains a nonempty array of strings.
- [hasURLs](hasurls.md) — A Boolean value that indicates whether the pasteboard contains a nonempty array of URLs.
