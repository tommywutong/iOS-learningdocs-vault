---
title: UITextDropEditability
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextdropeditability
source_url: 'https://developer.apple.com/documentation/uikit/uitextdropeditability'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextdropeditability.json'
content_hash: 'sha256:4d524f3d8c0b0ac7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITextDropEditability

<sub>Enumeration</sub>

The text-drop editability styles for noneditable text views.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
enum UITextDropEditability
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Editability styles

- [UITextDropEditabilityNo](uitextdropeditability/no.md) — A text-drop editability specifier indicating that a noneditable text view does not accept drops.
- [UITextDropEditabilityTemporary](uitextdropeditability/temporary.md) — A text-drop editability specifier indicating that a noneditable text view does accept drops but reverts to its noneditable status immediately afterward.
- [UITextDropEditabilityYes](uitextdropeditability/yes.md) — A text-drop editability specifier indicating that a noneditable text view does accept drops, and that the dropped text remains editable after the drop is finished.

### Initializers

- [init(rawValue:)](<uitextdropeditability/init(rawvalue_).md>)

## See Also

### Text view additions

- [UITextDragDelegate](uitextdragdelegate.md) — The interface for customizing the behavior of a drag activity for a text view.
- [UITextDropDelegate](uitextdropdelegate.md) — The interface for configuring a text view’s drop behavior.
- [UITextDraggable](uitextdraggable.md) — The interface that determines if a text view is a drag source.
- [UITextDragOptions](uitextdragoptions.md) — A set of options that determine the behavior of a draggable text view.
- [UITextDroppable](uitextdroppable.md) — The interface that determines if a text view is a drop destination.
