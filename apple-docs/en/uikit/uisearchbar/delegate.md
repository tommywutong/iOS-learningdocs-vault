---
title: delegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisearchbar/delegate
source_url: 'https://developer.apple.com/documentation/uikit/uisearchbar/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchbar/delegate.json'
content_hash: 'sha256:9b0e849c5619e6dd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchBar](../uisearchbar.md)

# delegate

<sub>Instance Property</sub>

The search bar’s delegate object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
weak var delegate: (any UISearchBarDelegate)? { get set }
```

## Discussion

The delegate should conform to the [UISearchBarDelegate](../uisearchbardelegate.md) protocol. Set this property to further modify the behavior. The default value is `nil`.

## See Also

### Handling search bar interactions

- [UISearchBarDelegate](../uisearchbardelegate.md) — A collection of optional methods that you implement to make a search bar control functional.
