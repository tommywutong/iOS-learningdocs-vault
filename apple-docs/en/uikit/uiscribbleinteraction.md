---
title: UIScribbleInteraction
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscribbleinteraction
source_url: 'https://developer.apple.com/documentation/uikit/uiscribbleinteraction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscribbleinteraction.json'
content_hash: 'sha256:557c589884a623a4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIScribbleInteraction

<sub>Class</sub>

An interaction for customizing the behavior of Scribble on text input views, or for suppressing it entirely in specific cases.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor class UIScribbleInteraction
```

## Overview

By default, Scribble lets users enter text by writing directly into any editable view that implements [UITextInput](uitextinput.md).

In apps with customized text fields, you can use the [UIScribbleInteractionDelegate](uiscribbleinteractiondelegate.md) callbacks to optimize the UI for a better writing experience. For example, you can hide custom placeholders when the user starts writing, or delay focusing on the field if it moves while gaining focus.

With text views that support drawing with Apple Pencil, you’ll need to suppress Scribble on nearby text fields to keep them from taking over the Pencil events for writing.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [UIInteraction](uiinteraction.md)

## Topics

### Creating a Scribble interaction

- [- initWithDelegate:](<uiscribbleinteraction/init(delegate_).md>) — Creates a Scribble interaction that allows customizing the behavior of Scribble on text input views with the delegate you provide.

### Managing Scribble interactions

- [delegate](uiscribbleinteraction/delegate.md) — The object that acts as the delegate for this interaction and responds to Scribble events for text input views.

### Detecting writing

- [handlingWriting](uiscribbleinteraction/ishandlingwriting.md) — A Boolean value that indicates whether the user is actively writing in a text view.

### Expecting input from Apple Pencil

- [pencilInputExpected](uiscribbleinteraction/ispencilinputexpected.md) — A Boolean value that indicates the user is likely to use Apple Pencil and handwriting instead of the keyboard to enter text.

## See Also

### Text fields

- [UIScribbleInteractionDelegate](uiscribbleinteractiondelegate.md) — Methods for customizing or suppressing Scribble behavior within text input views.
