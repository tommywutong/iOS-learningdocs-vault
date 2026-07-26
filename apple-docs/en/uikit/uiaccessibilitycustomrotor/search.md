---
title: UIAccessibilityCustomRotor.Search
framework: UIKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibilitycustomrotor/search
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibilitycustomrotor/search'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibilitycustomrotor/search.json'
content_hash: 'sha256:b790a8e28bd37ca7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibilityCustomRotor](../uiaccessibilitycustomrotor.md)

# UIAccessibilityCustomRotor.Search

<sub>Type Alias</sub>

The block type for retrieving the next or previous rotor.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor typealias Search = (UIAccessibilityCustomRotorSearchPredicate) -> UIAccessibilityCustomRotorItemResult?
```

## See Also

### Navigating to the next item

- [itemSearchBlock](itemsearchblock.md) — The block for retrieving the next or previous rotor.
- [Direction](direction.md) — Constants that indicate the search direction.
