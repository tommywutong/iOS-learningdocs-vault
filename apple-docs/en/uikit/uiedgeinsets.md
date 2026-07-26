---
title: UIEdgeInsets
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiedgeinsets
source_url: 'https://developer.apple.com/documentation/uikit/uiedgeinsets'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiedgeinsets.json'
content_hash: 'sha256:311c76d1f4e49b19'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIEdgeInsets

<sub>Structure</sub>

The inset distances for views.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
struct UIEdgeInsets
```

## Overview

Edge inset values are applied to a rectangle to shrink or expand the area represented by that rectangle. Typically, edge insets are used during view layout to modify the view’s frame. Positive values cause the frame to be inset (or shrunk) by the specified amount. Negative values cause the frame to be outset (or expanded) by the specified amount.

See also [UIEdgeInsetsMake](<uiedgeinsets/init(top_left_bottom_right_)-1s1t9.md>) and [UIEdgeInsetsZero](uiedgeinsets/zero.md).

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Copyable](../swift/copyable.md), [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating edge insets

- [init(top:left:bottom:right:)](<uiedgeinsets/init(top_left_bottom_right_)-6ff7.md>) — Creates an edge insets structure with the specified edges.
- [init()](<uiedgeinsets/init().md>) — Initializes the edge insets structure to default values.

### Getting the edge values

- [bottom](uiedgeinsets/bottom.md) — The bottom edge inset value.
- [left](uiedgeinsets/left.md) — The left edge inset value.
- [right](uiedgeinsets/right.md) — The right edge inset value.
- [top](uiedgeinsets/top.md) — The top edge inset value.

### Managing edge insets

- [inset(by:)](<../corefoundation/cgrect/inset(by_).md>)

### Converting to and from strings

- [string(for:)](<../foundation/nscoder/string(for_)-26b4z.md>) — Returns a string formatted to contain the data from an edge insets structure.
- [uiEdgeInsets(for:)](<../foundation/nscoder/uiedgeinsets(for_).md>) — Returns a UIKit edge insets structure based on the data in the specified string.

### Getting the empty edge insets

- [UIEdgeInsetsZero](uiedgeinsets/zero.md) — An edge insets struct whose top, left, bottom, and right fields are all set to `0`.

### Comparing edge insets

- [UIEdgeInsetsEqualToEdgeInsets(_:_:)](<uiedgeinsetsequaltoedgeinsets(____).md>) — Returns a Boolean value indicating whether the two edge insets are the same. _(deprecated)_

## See Also

### Related types

- [UIOffset](uioffset.md) — A structure that specifies an amount to offset a position.
- [UIAxis](uiaxis.md) — A structure that specifies the layout axes.
- [NSDirectionalEdgeInsets](nsdirectionaledgeinsets.md) — The inset distances for views, taking the user interface layout direction into account.
- [NSDirectionalRectEdge](nsdirectionalrectedge.md) — Constants that specify an edge or a set of edges, taking the user interface layout direction into account.
- [NSRectAlignment](nsrectalignment.md) — Constants that specify alignment to an edge or a set of edges depending on the user interface layout direction.
- [UIKit macros](uikit-macros.md) — Macros that UIKit defines.
