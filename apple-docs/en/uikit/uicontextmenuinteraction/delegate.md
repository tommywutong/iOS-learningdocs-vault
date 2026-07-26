---
title: delegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicontextmenuinteraction/delegate
source_url: 'https://developer.apple.com/documentation/uikit/uicontextmenuinteraction/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontextmenuinteraction/delegate.json'
content_hash: 'sha256:00a971deaa6826b2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIContextMenuInteraction](../uicontextmenuinteraction.md)

# delegate

<sub>Instance Property</sub>

The object that provides the preview and contextual menu for your content and responds to interaction-related events.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
weak var delegate: (any UIContextMenuInteractionDelegate)? { get }
```

## See Also

### Previewing and managing the content

- [UIContextMenuInteractionDelegate](../uicontextmenuinteractiondelegate.md) — The methods for providing the set of actions to perform on your content, and for customizing the preview of that content.
