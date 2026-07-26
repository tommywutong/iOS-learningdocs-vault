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
doc_path: /documentation/uikit/uinavigationbar/delegate
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationbar/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationbar/delegate.json'
content_hash: 'sha256:e8760be5cafdbef0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationBar](../uinavigationbar.md)

# delegate

<sub>Instance Property</sub>

The navigation bar’s delegate object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
weak var delegate: (any UINavigationBarDelegate)? { get set }
```

## Discussion

The delegate must conform to the [UINavigationBarDelegate](../uinavigationbardelegate.md) protocol. The default value is `nil`.

If the navigation bar was created by a navigation controller and is being managed by that object, you must not change the value of this property. A navigation controller acts as the delegate for the navigation bar it creates.

## See Also

### Responding to navigation bar changes

- [UINavigationBarDelegate](../uinavigationbardelegate.md) — Methods that a navigation bar calls before and after it modifies its stack of navigation items.
