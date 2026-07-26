---
title: delegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextselectiondisplayinteraction/delegate
source_url: 'https://developer.apple.com/documentation/uikit/uitextselectiondisplayinteraction/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextselectiondisplayinteraction/delegate.json'
content_hash: 'sha256:c6a766c84866eb05'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextSelectionDisplayInteraction](../uitextselectiondisplayinteraction.md)

# delegate

<sub>Instance Property</sub>

A delegate that provides a container view to manage the system-supplied selection views.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
weak var delegate: (any UITextSelectionDisplayInteractionDelegate)? { get }
```

## Discussion

Provide a delegate object if your UI displays selection highlights below your text input view. The delegate provides the container view for the system to use when adding the selection-related views.

## See Also

### Managing the drawing view

- [UITextSelectionDisplayInteractionDelegate](../uitextselectiondisplayinteractiondelegate.md) — An object you use to customize the presentation of text selections in your interface.
