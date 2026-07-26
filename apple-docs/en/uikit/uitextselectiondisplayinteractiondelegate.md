---
title: UITextSelectionDisplayInteractionDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextselectiondisplayinteractiondelegate
source_url: 'https://developer.apple.com/documentation/uikit/uitextselectiondisplayinteractiondelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextselectiondisplayinteractiondelegate.json'
content_hash: 'sha256:6f12aa0e53db1d17'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITextSelectionDisplayInteractionDelegate

<sub>Protocol</sub>

An object you use to customize the presentation of text selections in your interface.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UITextSelectionDisplayInteractionDelegate : NSObjectProtocol
```

## Overview

Adopt the [UITextSelectionDisplayInteractionDelegate](uitextselectiondisplayinteractiondelegate.md) protocol in a custom type that you use to customize the selection UI implementation. The [UITextSelectionDisplayInteraction](uitextselectiondisplayinteraction.md) object manages separate views to draw the text selection, the handles for the selected text range, and the insertion-point caret. Use this protocol if you use a custom view to manage these views instead of the text input view. For example, provide a container view if you draw the selection UI behind your text view’s content.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Providing a container view

- [- selectionContainerViewBelowTextForSelectionDisplayInteraction:](<uitextselectiondisplayinteractiondelegate/selectioncontainerviewbelowtext(for_).md>) — Returns the container view to hold the selection-related highlight and detail views.

## See Also

### Managing the drawing view

- [delegate](uitextselectiondisplayinteraction/delegate.md) — A delegate that provides a container view to manage the system-supplied selection views.
