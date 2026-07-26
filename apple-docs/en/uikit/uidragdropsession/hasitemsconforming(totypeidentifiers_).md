---
title: 'hasItemsConforming(toTypeIdentifiers:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidragdropsession/hasitemsconforming(totypeidentifiers:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidragdropsession/hasitemsconforming(totypeidentifiers:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidragdropsession/hasitemsconforming%28totypeidentifiers%3A%29.json'
content_hash: 'sha256:44dbcdf331d471ef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDragDropSession](../uidragdropsession.md)

# hasItemsConforming(toTypeIdentifiers:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether at least one drag item in the session conforms to at least one of the specified UTIs.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func hasItemsConforming(toTypeIdentifiers typeIdentifiers: [String]) -> Bool
```

## Parameters

- `typeIdentifiers` — An array of uniform type identifier (UTI) strings.

## Return Value

[true](../../swift/true.md) if a drag item in the session conforms to any UTI in the specified array; otherwise, [false](../../swift/false.md).

## See Also

### Checking for drag items

- [- canLoadObjectsOfClass:](<canloadobjects(ofclass_).md>) — Returns a Boolean value that indicates whether at least one drag item in the session can create an instance of the specified class.
- [items](items.md) — An array of drag items in the drag session or drop session.
