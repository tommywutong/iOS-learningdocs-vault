---
title: UITextDragOptions
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextdragoptions
source_url: 'https://developer.apple.com/documentation/uikit/uitextdragoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextdragoptions.json'
content_hash: 'sha256:33ecd70f98758e93'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITextDragOptions

<sub>Structure</sub>

A set of options that determine the behavior of a draggable text view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
struct UITextDragOptions
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Text drag options

- [UITextDragOptionStripTextColorFromPreviews](uitextdragoptions/striptextcolorfrompreviews.md) — Strips the foreground and background colors for a system-provided text drag preview.

### Initializers

- [init(rawValue:)](<uitextdragoptions/init(rawvalue_).md>) — Creates a text-drag options structure with the specified raw value.

## See Also

### Text view additions

- [UITextDragDelegate](uitextdragdelegate.md) — The interface for customizing the behavior of a drag activity for a text view.
- [UITextDropDelegate](uitextdropdelegate.md) — The interface for configuring a text view’s drop behavior.
- [UITextDraggable](uitextdraggable.md) — The interface that determines if a text view is a drag source.
- [UITextDroppable](uitextdroppable.md) — The interface that determines if a text view is a drop destination.
- [UITextDropEditability](uitextdropeditability.md) — The text-drop editability styles for noneditable text views.
