---
title: UIDragDropSession
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidragdropsession
source_url: 'https://developer.apple.com/documentation/uikit/uidragdropsession'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidragdropsession.json'
content_hash: 'sha256:7456c09979ebd432'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIDragDropSession

<sub>Protocol</sub>

The common interface for querying the state of both drag sessions and drop sessions.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor protocol UIDragDropSession : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Inherited By**: [UIDragSession](uidragsession.md), [UIDropSession](uidropsession.md)

## Topics

### Checking for drag items

- [- canLoadObjectsOfClass:](<uidragdropsession/canloadobjects(ofclass_).md>) — Returns a Boolean value that indicates whether at least one drag item in the session can create an instance of the specified class.
- [- hasItemsConformingToTypeIdentifiers:](<uidragdropsession/hasitemsconforming(totypeidentifiers_).md>) — Returns a Boolean value that indicates whether at least one drag item in the session conforms to at least one of the specified UTIs.
- [items](uidragdropsession/items.md) — An array of drag items in the drag session or drop session.

### Checking for drag and drop session restrictions

- [allowsMoveOperation](uidragdropsession/allowsmoveoperation.md) — A Boolean value that indicates whether the drag session permits moving drag items within the same app.
- [restrictedToDraggingApplication](uidragdropsession/isrestrictedtodraggingapplication.md) — A Boolean value that indicates whether the drag session is confined to the app that started the drag activity.

### Getting the location of a drag activity

- [- locationInView:](<uidragdropsession/location(in_).md>) — Returns the geometrical location of the user’s drag activity within the specified view.

## See Also

### Drag sources

- [UIDragItem](uidragitem.md) — A representation of an underlying data item as a person drags it from one location to another.
- [UIDragSession](uidragsession.md) — The interface for configuring a drag session.
- [UIDragAnimating](uidraganimating.md) — The interface for providing custom animation alongside the system’s lift, drop, and cancellation animations.
