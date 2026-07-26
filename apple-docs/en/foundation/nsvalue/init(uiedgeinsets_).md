---
title: 'init(UIEdgeInsets:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsvalue/init(uiedgeinsets:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsvalue/init(uiedgeinsets:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsvalue/init%28uiedgeinsets%3A%29.json'
content_hash: 'sha256:11fa0af124567ee6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSValue](../nsvalue.md)

# init(UIEdgeInsets:)

<sub>Initializer</sub>

Creates a new value object containing the specified UIKit edge insets structure.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
init(UIEdgeInsets insets: UIEdgeInsets)
```

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
init(uiEdgeInsets insets: UIEdgeInsets)
```

## Parameters

- `insets` — The value for the new object.

## Return Value

A new value object that contains the edge inset information.

## See Also

### Related Documentation

- [UIEdgeInsets](../../uikit/uiedgeinsets.md) — The inset distances for views.

### Working with UIKit Geometry Values

- [+ valueWithUIOffset:](<init(uioffset_).md>) — Creates a new value object containing the specified UIKit offset structure.
- [UIEdgeInsetsValue](uiedgeinsetsvalue.md) — Returns the UIKit edge insets structure representation of the value.
- [UIOffsetValue](uioffsetvalue.md) — Returns the UIKit offset structure representation of the value.
