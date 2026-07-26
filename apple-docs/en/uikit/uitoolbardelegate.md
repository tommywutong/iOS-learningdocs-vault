---
title: UIToolbarDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitoolbardelegate
source_url: 'https://developer.apple.com/documentation/uikit/uitoolbardelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitoolbardelegate.json'
content_hash: 'sha256:923b248299cd44f4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIToolbarDelegate

<sub>Protocol</sub>

The interface that toolbar delegate objects implement to manage the toolbar behavior.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor protocol UIToolbarDelegate : UIBarPositioningDelegate
```

## Overview

This protocol declares no methods of its own, but conforms to the [UIBarPositioningDelegate](uibarpositioningdelegate.md) protocol to support the positioning of a toolbar when it’s moved to a window.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [UIBarPositioningDelegate](uibarpositioningdelegate.md)

## See Also

### Managing toolbar changes

- [delegate](uitoolbar/delegate.md) — The toolbar’s delegate object.
