---
title: 'applyingContentHeadroom(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicolor/applyingcontentheadroom(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicolor/applyingcontentheadroom(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicolor/applyingcontentheadroom%28_%3A%29.json'
content_hash: 'sha256:8388162c3daaba5b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIColor](../uicolor.md)

# applyingContentHeadroom(_:)

<sub>Instance Method</sub>

Reinterpret the color by applying a new `contentHeadroom` without changing the color components. Changing the `contentHeadroom` redefines the color relative to a different peak white, changing its behavior under tone mapping and the result of calling `standardDynamicRangeColor`. The new color will have a `contentHeadroom` \>= 1.0.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func applyingContentHeadroom(_ contentHeadroom: CGFloat) -> UIColor
```

## See Also

### Working with high dynamic range (HDR) colors

- [standardDynamicRangeColor](standarddynamicrange.md) — In some cases it is useful to recover the color that was base SDR color that was exposed to generate the given HDR color. If a color’s `linearExposure` is \>1, then this will return the base SDR color.
