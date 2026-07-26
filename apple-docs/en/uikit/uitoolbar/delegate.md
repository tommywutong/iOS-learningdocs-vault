---
title: delegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitoolbar/delegate
source_url: 'https://developer.apple.com/documentation/uikit/uitoolbar/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitoolbar/delegate.json'
content_hash: 'sha256:3f9b0be37272f8b9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIToolbar](../uitoolbar.md)

# delegate

<sub>Instance Property</sub>

The toolbar’s delegate object.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
weak var delegate: (any UIToolbarDelegate)? { get set }
```

## Discussion

The delegate should conform to the `UIToolbarDelegate` protocol. You may not set the delegate when the toolbar is managed by a navigation controller. The default value is `nil`.

## See Also

### Managing toolbar changes

- [UIToolbarDelegate](../uitoolbardelegate.md) — The interface that toolbar delegate objects implement to manage the toolbar behavior.
