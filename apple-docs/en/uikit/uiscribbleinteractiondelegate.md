---
title: UIScribbleInteractionDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscribbleinteractiondelegate
source_url: 'https://developer.apple.com/documentation/uikit/uiscribbleinteractiondelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscribbleinteractiondelegate.json'
content_hash: 'sha256:9169377f201ce024'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIScribbleInteractionDelegate

<sub>Protocol</sub>

Methods for customizing or suppressing Scribble behavior within text input views.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor protocol UIScribbleInteractionDelegate : NSObjectProtocol
```

## Overview

By default, Scribble let users enter text by writing directly into any editable view that implement [UITextInput](uitextinput.md). In apps with customized text fields, you can use the [UIScribbleInteractionDelegate](uiscribbleinteractiondelegate.md) callbacks to optimize the UI for a better writing experience, including:

- Opting individual text fields in or out of Scribble interactions.
- Controlling how quickly a given text field responds to input, giving the view an opportunity to change its configuration, if necessary.
- Receiving notifications when the user writing begins and ends.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Allowing and controlling Scribble interactions

- [- scribbleInteraction:shouldBeginAtLocation:](<uiscribbleinteractiondelegate/scribbleinteraction(__shouldbeginat_).md>) — Returns a Boolean value that indicates whether the delegate should allow writing at a specific location in the view.
- [- scribbleInteractionShouldDelayFocus:](<uiscribbleinteractiondelegate/scribbleinteractionshoulddelayfocus(__).md>) — Tells the delegate to delay focusing the text input view.

### Tracking Scribble input

- [- scribbleInteractionWillBeginWriting:](<uiscribbleinteractiondelegate/scribbleinteractionwillbeginwriting(__).md>) — Informs the delegate when the user begins writing in the view.
- [- scribbleInteractionDidFinishWriting:](<uiscribbleinteractiondelegate/scribbleinteractiondidfinishwriting(__).md>) — Informs the delegate that the user stops writing in the view, after Scribble transcribes and enters the last word.

## See Also

### Text fields

- [UIScribbleInteraction](uiscribbleinteraction.md) — An interaction for customizing the behavior of Scribble on text input views, or for suppressing it entirely in specific cases.
