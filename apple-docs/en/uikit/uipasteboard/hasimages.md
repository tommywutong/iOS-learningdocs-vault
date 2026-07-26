---
title: hasImages
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipasteboard/hasimages
source_url: 'https://developer.apple.com/documentation/uikit/uipasteboard/hasimages'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipasteboard/hasimages.json'
content_hash: 'sha256:ae98b86587ab473e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPasteboard](../uipasteboard.md)

# hasImages

<sub>Instance Property</sub>

A Boolean value that indicates whether the pasteboard contains a nonempty array of images.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var hasImages: Bool { get }
```

## Discussion

Employ this property to determine if a pasteboard contains image data.

Do not use the [image](image.md) or [images](images.md) properties to determine whether a pasteboard contains image data, because doing so consumes resources needlessly.

## See Also

### Checking for data types on a pasteboard

- [hasColors](hascolors.md) — A Boolean value that indicates whether the pasteboard contains contains a nonempty array of colors.
- [hasStrings](hasstrings.md) — A Boolean value that indicates whether the pasteboard contains a nonempty array of strings.
- [hasURLs](hasurls.md) — A Boolean value that indicates whether the pasteboard contains a nonempty array of URLs.
