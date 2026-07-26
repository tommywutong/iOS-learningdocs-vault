---
title: 'focusItems(in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uifocusitemcontainer/focusitems(in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uifocusitemcontainer/focusitems(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocusitemcontainer/focusitems%28in%3A%29.json'
content_hash: 'sha256:e91ce8272aa48b00'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFocusItemContainer](../uifocusitemcontainer.md)

# focusItems(in:)

<sub>Instance Method</sub>

Retrieves all of the focus items within this container that intersect with the provided rectangle.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func focusItems(in rect: CGRect) -> [any UIFocusItem]
```

## Parameters

- `rect` — The rectangle used to look for focus items that intersect the rectangle expressed in the container’s coordinate space.

## Return Value

An array of focus items that intersect the provided rectangle. The focus items are expressed in the container’s coordinate space.

## Discussion

The found focus items should report their frames in the [coordinateSpace](coordinatespace.md).

## See Also

### Retrieving focus items

- [coordinateSpace](coordinatespace.md) — The coordinate space of the focus items contained in the focus item container.
