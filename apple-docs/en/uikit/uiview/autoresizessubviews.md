---
title: autoresizesSubviews
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/autoresizessubviews
source_url: 'https://developer.apple.com/documentation/uikit/uiview/autoresizessubviews'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/autoresizessubviews.json'
content_hash: 'sha256:18ee9cf56e80cd2b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# autoresizesSubviews

<sub>Instance Property</sub>

A Boolean value that determines whether the receiver automatically resizes its subviews when its bounds change.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var autoresizesSubviews: Bool { get set }
```

## Discussion

When set to [true](../../swift/true.md), the receiver adjusts the size of its subviews when its bounds change. The default value is [true](../../swift/true.md).

## See Also

### Configuring the resizing behavior

- [contentMode](contentmode-swift.property.md) — A flag used to determine how a view lays out its content when its bounds change.
- [ContentMode](contentmode-swift.enum.md) — Options to specify how a view adjusts its content when its size changes.
- [- sizeThatFits:](<sizethatfits(__).md>) — Asks the view to calculate and return the size that best fits the specified size.
- [- sizeToFit](<sizetofit().md>) — Resizes and moves the receiver view so it just encloses its subviews.
- [autoresizingMask](autoresizingmask-swift.property.md) — An integer bit mask that determines how the receiver resizes itself when its superview’s bounds change.
