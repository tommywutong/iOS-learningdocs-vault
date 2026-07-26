---
title: 'setContentOffset(_:animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiscrollview/setcontentoffset(_:animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollview/setcontentoffset(_:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollview/setcontentoffset%28_%3Aanimated%3A%29.json'
content_hash: 'sha256:ec5716610246deb7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScrollView](../uiscrollview.md)

# setContentOffset(_:animated:)

<sub>Instance Method</sub>

Sets the offset from the content view’s origin that corresponds to the scroll view’s origin.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setContentOffset(_ contentOffset: CGPoint, animated: Bool)
```

## Parameters

- `contentOffset` — A point (expressed in points) that’s offset from the content view’s origin.

- `animated` — [true](../../swift/true.md) to animate the transition at a constant velocity to the new offset, [false](../../swift/false.md) to make the transition immediate.

## See Also

### Managing the content size and offset

- [contentSize](contentsize.md) — The size of the content view.
- [contentOffset](contentoffset.md) — The point at which the origin of the content view is offset from the origin of the scroll view.
