---
title: delegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.2+, iPadOS 18.2+, Mac Catalyst 18.2+, visionOS 2.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwritingtoolscoordinator/delegate-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/delegate-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolscoordinator/delegate-swift.property.json'
content_hash: 'sha256:9c31b852ec09928f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWritingToolsCoordinator](../uiwritingtoolscoordinator.md)

# delegate

<sub>Instance Property</sub>

The object that handles Writing Tools interactions for your view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
weak var delegate: (any UIWritingToolsCoordinator.Delegate)? { get }
```

## Discussion

Specify this object at initialization time when creating your `UIWritingToolsCoordinator` object. The object must adopt the [Delegate](delegate-swift.protocol.md) protocol, and be capable of modifying your view’s text storage and refreshing the view’s layout and appearance.

## See Also

### Managing Writing Tools interactions

- [Delegate](delegate-swift.protocol.md) — An interface that you use to manage interactions between Writing Tools and your custom text view.
