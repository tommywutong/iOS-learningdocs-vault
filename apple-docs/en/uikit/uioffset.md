---
title: UIOffset
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uioffset
source_url: 'https://developer.apple.com/documentation/uikit/uioffset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uioffset.json'
content_hash: 'sha256:d7f55dd0df748f81'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIOffset

<sub>Structure</sub>

A structure that specifies an amount to offset a position.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
struct UIOffset
```

## Overview

The components are positive for right or down, negative for left or up.

See also [Initializing offsets](uioffset.md#Initializing-offsets) and [UIOffsetZero](uioffset/zero.md).

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Copyable](../swift/copyable.md), [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializing offsets

- [init(horizontal:vertical:)](<uioffset/init(horizontal_vertical_)-9wl8x.md>) — Creates an offset structure from the given components.
- [init()](<uioffset/init().md>) — Creates an offset structure.

### Getting the offset values

- [horizontal](uioffset/horizontal.md) — The amount of horizontal offset from a position.
- [vertical](uioffset/vertical.md) — The amount of vertical offset from a position.

### Comparing offsets

- [UIOffsetEqualToOffset(_:_:)](<uioffsetequaltooffset(____).md>) — Returns a Boolean value that indicates whether two offsets are equal. _(deprecated)_

### Converting to and from strings

- [string(for:)](<../foundation/nscoder/string(for_)-454dj.md>) — Returns a string formatted to contain the data from an offset structure.
- [uiOffset(for:)](<../foundation/nscoder/uioffset(for_).md>) — Returns a UIKit offset structure corresponding to the data in a given string.

### Getting the empty offset value

- [UIOffsetZero](uioffset/zero.md) — An offset structure with no offset in the horizontal and vertical directions.

## See Also

### Related types

- [UIAxis](uiaxis.md) — A structure that specifies the layout axes.
- [UIEdgeInsets](uiedgeinsets.md) — The inset distances for views.
- [NSDirectionalEdgeInsets](nsdirectionaledgeinsets.md) — The inset distances for views, taking the user interface layout direction into account.
- [NSDirectionalRectEdge](nsdirectionalrectedge.md) — Constants that specify an edge or a set of edges, taking the user interface layout direction into account.
- [NSRectAlignment](nsrectalignment.md) — Constants that specify alignment to an edge or a set of edges depending on the user interface layout direction.
- [UIKit macros](uikit-macros.md) — Macros that UIKit defines.
