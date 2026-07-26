---
title: 'init(top:leading:bottom:trailing:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nsdirectionaledgeinsets/init(top:leading:bottom:trailing:)-6wnda'
source_url: 'https://developer.apple.com/documentation/uikit/nsdirectionaledgeinsets/init(top:leading:bottom:trailing:)-6wnda'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdirectionaledgeinsets/init%28top%3Aleading%3Abottom%3Atrailing%3A%29-6wnda.json'
content_hash: 'sha256:0cc1623d5aee29af'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSDirectionalEdgeInsets](../nsdirectionaledgeinsets.md)

# init(top:leading:bottom:trailing:)

<sub>Initializer</sub>

Creates a directional edge insets structure that contains the specified values.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
init(top: CGFloat, leading: CGFloat, bottom: CGFloat, trailing: CGFloat)
```

## Parameters

- `top` — The inset on the top of an object.

- `leading` — The inset on the leading edge of an object. In a left-to-right system, the left edge is the leading edge. In a right-to-left system, the right edge is the leading edge.

- `bottom` — The inset on the bottom of an object.

- `trailing` — The inset on the trailing edge of an object. In a left-to-right system, the right edge is the trailing edge. In a right-to-left system, the left edge is the trailing edge.

## Return Value

An initialized inset structure.

## See Also

### Creating directional edge insets

- [init()](<init().md>) — Creates a directional edge insets structure that contains default values.
- [init(_:)](<init(__).md>) — Creates a directional edge insets structure from a SwiftUI edge insets structure.
