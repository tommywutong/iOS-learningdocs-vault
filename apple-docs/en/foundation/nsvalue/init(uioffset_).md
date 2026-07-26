---
title: 'init(UIOffset:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsvalue/init(uioffset:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsvalue/init(uioffset:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsvalue/init%28uioffset%3A%29.json'
content_hash: 'sha256:f5704b6f219813b6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSValue](../nsvalue.md)

# init(UIOffset:)

<sub>Initializer</sub>

Creates a new value object containing the specified UIKit offset structure.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
init(UIOffset insets: UIOffset)
```

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
init(uiOffset insets: UIOffset)
```

## Parameters

- `insets` — The value for the new object.

## Return Value

A new value object that contains the offset information.

## See Also

### Related Documentation

- [UIOffset](../../uikit/uioffset.md) — A structure that specifies an amount to offset a position.

### Working with UIKit Geometry Values

- [+ valueWithUIEdgeInsets:](<init(uiedgeinsets_).md>) — Creates a new value object containing the specified UIKit edge insets structure.
- [UIEdgeInsetsValue](uiedgeinsetsvalue.md) — Returns the UIKit edge insets structure representation of the value.
- [UIOffsetValue](uioffsetvalue.md) — Returns the UIKit offset structure representation of the value.
