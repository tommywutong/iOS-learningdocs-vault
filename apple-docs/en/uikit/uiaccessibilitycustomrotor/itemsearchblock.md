---
title: itemSearchBlock
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibilitycustomrotor/itemsearchblock
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibilitycustomrotor/itemsearchblock'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibilitycustomrotor/itemsearchblock.json'
content_hash: 'sha256:d460c8541f404626'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibilityCustomRotor](../uiaccessibilitycustomrotor.md)

# itemSearchBlock

<sub>Instance Property</sub>

The block for retrieving the next or previous rotor.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var itemSearchBlock: UIAccessibilityCustomRotor.Search { get set }
```

## Discussion

Your implementation of the block facilitates navigation from the current rotor to the next or previous rotor.

## See Also

### Navigating to the next item

- [Search](search.md) — The block type for retrieving the next or previous rotor.
- [Direction](direction.md) — Constants that indicate the search direction.
