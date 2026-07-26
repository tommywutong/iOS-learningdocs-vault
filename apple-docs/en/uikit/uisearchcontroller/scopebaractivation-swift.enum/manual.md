---
title: UISearchController.ScopeBarActivation.manual
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisearchcontroller/scopebaractivation-swift.enum/manual
source_url: 'https://developer.apple.com/documentation/uikit/uisearchcontroller/scopebaractivation-swift.enum/manual'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchcontroller/scopebaractivation-swift.enum/manual.json'
content_hash: 'sha256:da6fdaac511491dc'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UISearchController](../../uisearchcontroller.md) · [ScopeBarActivation](../scopebaractivation-swift.enum.md)

# UISearchController.ScopeBarActivation.manual

<sub>Case</sub>

A mode that gives you manual control over when to show and hide the scope bar.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
case manual
```

## Discussion

When you use this mode, you control when to show and hide the scope bar through the [showsScopeBar](../../uisearchbar/showsscopebar.md) property on the [searchBar](../searchbar.md) of the [UISearchController](../../uisearchcontroller.md).

## See Also

### Constants

- [UISearchControllerScopeBarActivationAutomatic](automatic.md) — A mode in which the system automatically determines when to show and hide the scope bar.
- [UISearchControllerScopeBarActivationOnTextEntry](ontextentry.md) — A mode in which the search controller shows the scope bar when typing begins in the search field, and hides it after search cancellation.
- [UISearchControllerScopeBarActivationOnSearchActivation](onsearchactivation.md) — A mode in which the search controller shows the scope bar when search becomes active, and hides it after search cancellation.
