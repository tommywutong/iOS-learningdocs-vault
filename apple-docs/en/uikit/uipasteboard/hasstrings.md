---
title: hasStrings
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipasteboard/hasstrings
source_url: 'https://developer.apple.com/documentation/uikit/uipasteboard/hasstrings'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipasteboard/hasstrings.json'
content_hash: 'sha256:b50299c1aaf16bc4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPasteboard](../uipasteboard.md)

# hasStrings

<sub>Instance Property</sub>

A Boolean value that indicates whether the pasteboard contains a nonempty array of strings.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var hasStrings: Bool { get }
```

## Discussion

Employ this property to determine if a pasteboard contains string data.

Do not use the [string](string.md) or [strings](strings.md) properties to determine whether a pasteboard contains string data, because doing so consumes resources needlessly.

## See Also

### Checking for data types on a pasteboard

- [hasColors](hascolors.md) — A Boolean value that indicates whether the pasteboard contains contains a nonempty array of colors.
- [hasImages](hasimages.md) — A Boolean value that indicates whether the pasteboard contains a nonempty array of images.
- [hasURLs](hasurls.md) — A Boolean value that indicates whether the pasteboard contains a nonempty array of URLs.
