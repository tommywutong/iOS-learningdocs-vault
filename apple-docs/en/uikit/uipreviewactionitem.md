---
title: UIPreviewActionItem
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipreviewactionitem
source_url: 'https://developer.apple.com/documentation/uikit/uipreviewactionitem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipreviewactionitem.json'
content_hash: 'sha256:06799baa4ef5388c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIPreviewActionItem

<sub>Protocol</sub>

A set of methods that defines the styles you can apply to peek quick actions and peek quick action groups, and defines a read-only accessor for the user-visible title of a peek quick action.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UIPreviewActionItem : NSObjectProtocol
```

## Overview

> [!important] Important
> Don’t adopt this protocol in custom classes.

The [UIPreviewActionItem](uipreviewactionitem.md) protocol is adopted by the [UIPreviewAction](uipreviewaction.md) and [UIPreviewActionGroup](uipreviewactiongroup.md) classes.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Conforming Types**: [UIPreviewAction](uipreviewaction.md), [UIPreviewActionGroup](uipreviewactiongroup.md)

## Topics

### Accessing peek quick action properties

- [title](uipreviewactionitem/title.md) — The peek quick action item’s title.

### Constants

- [Style](uipreviewaction/style.md) — The style for a peek quick action. _(deprecated)_

## See Also

### 3D Touch interactions

- [UIPreviewInteraction](uipreviewinteraction.md) — A class that registers a view to provide a custom user experience in response to 3D Touch interactions.
- [UIPreviewInteractionDelegate](uipreviewinteractiondelegate.md) — A set of methods for communicating the progress of a preview interaction.
