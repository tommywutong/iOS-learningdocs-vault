---
title: 'init(_:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextalignment/init(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextalignment/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextalignment/init%28_%3A%29.json'
content_hash: 'sha256:eebe5fae903545fb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextAlignment](../nstextalignment.md)

# init(_:)

<sub>Initializer</sub>

Converts a Core Text alignment constant value to the matching constant value in UIKit.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
init(_ ctTextAlignment: CTTextAlignment)
```

## Parameters

- `ctTextAlignment` — The Core Text alignment constant to convert.

## Return Value

The UIKit text alignment that corresponds to the value specified in `ctTextAlignment`.

## Discussion

Use this function when you need to map between the Core Text and UIKit constants for text alignment.

## See Also

### Text manipulations

- [init(_:)](<../../coretext/cttextalignment/init(__).md>) — Converts a UIKit text alignment constant value to the matching constant value that Core Text uses.
