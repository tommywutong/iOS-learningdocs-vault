---
title: identifier
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilayoutguide/identifier
source_url: 'https://developer.apple.com/documentation/uikit/uilayoutguide/identifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilayoutguide/identifier.json'
content_hash: 'sha256:b66bea3c9120f55c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILayoutGuide](../uilayoutguide.md)

# identifier

<sub>Instance Property</sub>

A string used to identify the layout guide.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var identifier: String { get set }
```

## Discussion

By default, the `identifier` property is an empty string. Assign a nonempty string to identify this layout guide. This string appears as part of the guide’s description when the guide is printed to the console. You can also use the identifier to find a particular layout guide from among the guides owned by a view.

Identifiers starting with “NS” or “UI” are reserved by the system. The system may assign these identifiers to the guides it creates.

## See Also

### Working with layout guides

- [layoutFrame](layoutframe.md) — The layout guide’s frame in its owning view’s coordinate system.
- [owningView](owningview.md) — The view that owns this layout guide.
