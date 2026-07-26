---
title: totalBounds
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsstringdrawingcontext/totalbounds
source_url: 'https://developer.apple.com/documentation/uikit/nsstringdrawingcontext/totalbounds'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsstringdrawingcontext/totalbounds.json'
content_hash: 'sha256:ee177af061beeae9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSStringDrawingContext](../nsstringdrawingcontext.md)

# totalBounds

<sub>Instance Property</sub>

The most recent bounding rectangle that the system used to draw the string.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var totalBounds: CGRect { get }
```

## Discussion

This property contains the bounding rectangle that was last used when calling the [draw(with:options:context:)](<../../foundation/nsattributedstring/draw(with_options_context_).md>) method. The rectangle is specified in the coordinate system of the drawn string. (The origin of the bounds corresponds to neither a view the string might have been drawn into nor the origin of a possible [draw(in:)](<../../foundation/nsattributedstring/draw(in_).md>) call.)
