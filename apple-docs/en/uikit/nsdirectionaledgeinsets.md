---
title: NSDirectionalEdgeInsets
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsdirectionaledgeinsets
source_url: 'https://developer.apple.com/documentation/uikit/nsdirectionaledgeinsets'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdirectionaledgeinsets.json'
content_hash: 'sha256:b1274d0d3fdbae1c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSDirectionalEdgeInsets

<sub>Structure</sub>

The inset distances for views, taking the user interface layout direction into account.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
struct NSDirectionalEdgeInsets
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Copyable](../swift/copyable.md), [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating directional edge insets

- [init(top:leading:bottom:trailing:)](<nsdirectionaledgeinsets/init(top_leading_bottom_trailing_)-6wnda.md>) — Creates a directional edge insets structure that contains the specified values.
- [init()](<nsdirectionaledgeinsets/init().md>) — Creates a directional edge insets structure that contains default values.
- [init(_:)](<nsdirectionaledgeinsets/init(__).md>) — Creates a directional edge insets structure from a SwiftUI edge insets structure.

### Getting the edge values

- [bottom](nsdirectionaledgeinsets/bottom.md) — The bottom edge inset value.
- [leading](nsdirectionaledgeinsets/leading.md) — The leading edge inset value.
- [top](nsdirectionaledgeinsets/top.md) — The top edge inset value.
- [trailing](nsdirectionaledgeinsets/trailing.md) — The trailing edge inset value.

### Converting to and from strings

- [string(for:)](<../foundation/nscoder/string(for_)-hp8b.md>) — Returns a string formatted to contain the data from a directional edge insets structure.
- [nsDirectionalEdgeInsets(for:)](<../foundation/nscoder/nsdirectionaledgeinsets(for_).md>) — Returns a directional edge insets structure based on data in the specified string.

### Getting the empty edge insets

- [NSDirectionalEdgeInsetsZero](nsdirectionaledgeinsets/zero.md) — A directional edge insets structure whose top, leading, bottom, and trailing fields all have a value of `0`.

## See Also

### Related types

- [UIOffset](uioffset.md) — A structure that specifies an amount to offset a position.
- [UIAxis](uiaxis.md) — A structure that specifies the layout axes.
- [UIEdgeInsets](uiedgeinsets.md) — The inset distances for views.
- [NSDirectionalRectEdge](nsdirectionalrectedge.md) — Constants that specify an edge or a set of edges, taking the user interface layout direction into account.
- [NSRectAlignment](nsrectalignment.md) — Constants that specify alignment to an edge or a set of edges depending on the user interface layout direction.
- [UIKit macros](uikit-macros.md) — Macros that UIKit defines.
