---
title: hasURLs
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipasteboard/hasurls
source_url: 'https://developer.apple.com/documentation/uikit/uipasteboard/hasurls'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipasteboard/hasurls.json'
content_hash: 'sha256:822a8768e7d4eb99'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPasteboard](../uipasteboard.md)

# hasURLs

<sub>Instance Property</sub>

A Boolean value that indicates whether the pasteboard contains a nonempty array of URLs.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var hasURLs: Bool { get }
```

## Discussion

Employ this property to determine if a pasteboard contains URL data.

Do not use the [URL](url.md) or [URLs](urls.md) properties to determine whether a pasteboard contains URL data, because doing so consumes resources needlessly.

## See Also

### Checking for data types on a pasteboard

- [hasColors](hascolors.md) — A Boolean value that indicates whether the pasteboard contains contains a nonempty array of colors.
- [hasImages](hasimages.md) — A Boolean value that indicates whether the pasteboard contains a nonempty array of images.
- [hasStrings](hasstrings.md) — A Boolean value that indicates whether the pasteboard contains a nonempty array of strings.
