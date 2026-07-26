---
title: 'contains(_:)'
framework: AppKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（10.11 起废弃）]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/appkit/nstextcontainer/contains(_:)'
source_url: 'https://developer.apple.com/documentation/appkit/nstextcontainer/contains(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nstextcontainer/contains%28_%3A%29.json'
content_hash: 'sha256:d8ae1d816102c93b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSTextContainer](../nstextcontainer.md)

# contains(_:)

<sub>Instance Method</sub>

Queries whether a point lies within the text container’s region or on the region’s edge—not simply within its bounding rectangle.

<sub>macOS</sub>

```swift
func contains(_ point: NSPoint) -> Bool
```

## Parameters

- `point` — The point in question.

## Return Value

[true](../../swift/true.md) if `aPoint` lies within the receiver’s region or on the region’s edge—not simply within its bounding rectangle—[false](../../swift/false.md) otherwise.

## Discussion

For example, if the receiver defines a donut shape and `aPoint` lies in the hole, this method returns [false](../../swift/false.md). This method can be used for hit testing of mouse events.

The default [NSTextContainer](../nstextcontainer.md) implementation merely checks that `aPoint` lies within its bounding rectangle.

## See Also

### Deprecated

- [- initWithContainerSize:](<init(containersize_).md>) — Initializes a text container with a specified bounding rectangle. _(deprecated)_
- [- lineFragmentRectForProposedRect:sweepDirection:movementDirection:remainingRect:](<linefragmentrect(forproposedrect_sweepdirection_movementdirection_remaining_).md>) — Calculates and returns the longest rectangle available in the proposed rectangle for displaying text. _(deprecated)_
- [containerSize](containersize.md) — The size of the text container’s bounding rectangle. _(deprecated)_
