---
title: UIDragAnimating
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidraganimating
source_url: 'https://developer.apple.com/documentation/uikit/uidraganimating'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidraganimating.json'
content_hash: 'sha256:eef97e98c6710d45'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIDragAnimating

<sub>Protocol</sub>

The interface for providing custom animation alongside the system’s lift, drop, and cancellation animations.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor protocol UIDragAnimating : NSObjectProtocol
```

## Overview

You can use a [UIDragAnimating](uidraganimating.md) object to animate your own changes to the preview displayed during system-provided drag and drop animations.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Inherited By**: [UICollectionViewDropPlaceholderContext](uicollectionviewdropplaceholdercontext.md), [UITableViewDropPlaceholderContext](uitableviewdropplaceholdercontext.md)

## Topics

### Adding animations

- [- addAnimations:](<uidraganimating/addanimations(__).md>) — Adds an animation block for modifying a view animation while it’s running.
- [- addCompletion:](<uidraganimating/addcompletion(__).md>) — Adds an animation completion block to run when a view animation has ended.

## See Also

### Drag sources

- [UIDragItem](uidragitem.md) — A representation of an underlying data item as a person drags it from one location to another.
- [UIDragDropSession](uidragdropsession.md) — The common interface for querying the state of both drag sessions and drop sessions.
- [UIDragSession](uidragsession.md) — The interface for configuring a drag session.
