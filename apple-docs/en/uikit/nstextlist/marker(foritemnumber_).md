---
title: 'marker(forItemNumber:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextlist/marker(foritemnumber:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextlist/marker(foritemnumber:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlist/marker%28foritemnumber%3A%29.json'
content_hash: 'sha256:6488b8130a58b3e1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextList](../nstextlist.md)

# marker(forItemNumber:)

<sub>Instance Method</sub>

Returns the computed value for a specific ordinal position in the list.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func marker(forItemNumber itemNumber: Int) -> String
```

## Parameters

- `itemNumber` — The ordinal position in the list whose computed marker value is desired.

## Return Value

The computed maker value for `itemNumber`.

## See Also

### Working with markers

- [markerFormat](markerformat-swift.property.md) — Returns the marker format string used by the receiver.
- [MarkerFormat](markerformat-swift.struct.md) — Constants that describe marker symbols you can apply to list elements in text lists.
