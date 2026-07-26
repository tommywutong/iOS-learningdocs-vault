---
title: UIDragItem
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidragitem
source_url: 'https://developer.apple.com/documentation/uikit/uidragitem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidragitem.json'
content_hash: 'sha256:d2f853775c99aa88'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIDragItem

<sub>Class</sub>

A representation of an underlying data item as a person drags it from one location to another.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UIDragItem
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Initializing a drag item

- [- initWithItemProvider:](<uidragitem/init(itemprovider_).md>) — Initializes a new drag item with a specified item provider.

### Accessing the drag item’s data

- [itemProvider](uidragitem/itemprovider.md) — The item provider associated with the drag item.
- [localObject](uidragitem/localobject.md) — A custom object associated with the drag item.

### Changing the drag item preview

- [previewProvider](uidragitem/previewprovider.md) — A visual preview of the drag item, displayed while the user drags the item across the screen.
- [- setNeedsDropPreviewUpdate](<uidragitem/setneedsdroppreviewupdate().md>) — Notifies the operating system that an updated drop preview is available for the item.

## See Also

### Drag sources

- [UIDragDropSession](uidragdropsession.md) — The common interface for querying the state of both drag sessions and drop sessions.
- [UIDragSession](uidragsession.md) — The interface for configuring a drag session.
- [UIDragAnimating](uidraganimating.md) — The interface for providing custom animation alongside the system’s lift, drop, and cancellation animations.
