---
title: 'point(inside:with:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiview/point(inside:with:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiview/point(inside:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/point%28inside%3Awith%3A%29.json'
content_hash: 'sha256:858d8a8e9a7752fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# point(inside:with:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether the receiver contains the specified point.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func point(inside point: CGPoint, with event: UIEvent?) -> Bool
```

## Parameters

- `point` — A point that is in the receiver’s local coordinate system (bounds).

- `event` — The event that warranted a call to this method. If you are calling this method from outside your event-handling code, you may specify `nil`.

## Return Value

[true](../../swift/true.md) if `point` is inside the receiver’s bounds; otherwise, [false](../../swift/false.md).

## See Also

### Hit-testing in a view

- [- hitTest:withEvent:](<hittest(__with_).md>) — Returns the farthest descendant in the view hierarchy of the current view, including itself, that contains the specified point.
