---
title: coordinateSpace
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifocusitemcontainer/coordinatespace
source_url: 'https://developer.apple.com/documentation/uikit/uifocusitemcontainer/coordinatespace'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocusitemcontainer/coordinatespace.json'
content_hash: 'sha256:7a0caa9580415031'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFocusItemContainer](../uifocusitemcontainer.md)

# coordinateSpace

<sub>Instance Property</sub>

The coordinate space of the focus items contained in the focus item container.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var coordinateSpace: any UICoordinateSpace { get }
```

## Discussion

The focus items returned by [- focusItemsInRect:](<focusitems(in_).md>) should report their frames in this coordinate space.

## See Also

### Retrieving focus items

- [- focusItemsInRect:](<focusitems(in_).md>) — Retrieves all of the focus items within this container that intersect with the provided rectangle.
