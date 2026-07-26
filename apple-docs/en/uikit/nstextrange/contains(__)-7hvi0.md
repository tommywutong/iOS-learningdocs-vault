---
title: 'contains(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextrange/contains(_:)-7hvi0'
source_url: 'https://developer.apple.com/documentation/uikit/nstextrange/contains(_:)-7hvi0'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextrange/contains%28_%3A%29-7hvi0.json'
content_hash: 'sha256:dac249908e42a4ca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextRange](../nstextrange.md)

# contains(_:)

<sub>Instance Method</sub>

Determines if the text location you specify is in the current text range.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func contains(_ location: any NSTextLocation) -> Bool
```

## Parameters

- `location` — An [NSTextLocation](../nstextlocation.md).

## Return Value

Returns `true` if the location is in the range otherwise `false` .

## See Also

### Finding text within the text range

- [- containsRange:](<contains(__)-5j4y2.md>) — Determines if the text range you specify is in the current text range.
