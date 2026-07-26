---
title: 'UIPointerShape.roundedRect(_:radius:)'
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipointershape-swift.enum/roundedrect(_:radius:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipointershape-swift.enum/roundedrect(_:radius:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipointershape-swift.enum/roundedrect%28_%3Aradius%3A%29.json'
content_hash: 'sha256:9442fcaa798a5a49'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPointerShape](../uipointershape-swift.enum.md)

# UIPointerShape.roundedRect(_:radius:)

<sub>Case</sub>

The pointer morphs into a rounded rectangle using the provided corner radius.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
case roundedRect(CGRect, radius: CGFloat = UIPointerShape.defaultCornerRadius)
```

## Discussion

If you don’t specify a radius, the rounded rectangle uses the `defaultCornerRadius`.

> [!note] Note
> If used alongside a content effect, this rectangle must be in the view coordinate space of the [preview](../uipointereffect-swift.enum/preview.md). Otherwise, it’s centered around the pointer’s current location, and the rectangle’s origin is interpreted as an offset.

## See Also

### Specifying pointer shapes

- [UIPointerShape.horizontalBeam(length:)](<horizontalbeam(length_).md>) — The pointer morphs into a horizontal beam using the specified length.
- [UIPointerShape.verticalBeam(length:)](<verticalbeam(length_).md>) — The pointer morphs into a vertical beam using the specified length.
- [UIPointerShape.path(_:)](<path(__).md>) — The pointer morphs into the given Bézier path.
