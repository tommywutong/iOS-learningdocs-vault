---
title: view
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibilitylocationdescriptor/view
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibilitylocationdescriptor/view'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibilitylocationdescriptor/view.json'
content_hash: 'sha256:5983b2810b224406'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibilityLocationDescriptor](../uiaccessibilitylocationdescriptor.md)

# view

<sub>Instance Property</sub>

Returns the view associated with the accessibility location descriptor.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
weak var view: UIView? { get }
```

## See Also

### Getting the descriptor information

- [name](name.md) — Returns the plaintext string representation of the name for the accessibility location descriptor.
- [attributedName](attributedname.md) — Returns the attributed string representation of the name for the accessibility location descriptor.
- [point](point.md) — Returns the geometric point of interest for the accessibility location descriptor within its associated view and in the coordinate space of the view.
