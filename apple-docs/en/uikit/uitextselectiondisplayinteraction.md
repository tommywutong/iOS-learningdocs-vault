---
title: UITextSelectionDisplayInteraction
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextselectiondisplayinteraction
source_url: 'https://developer.apple.com/documentation/uikit/uitextselectiondisplayinteraction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextselectiondisplayinteraction.json'
content_hash: 'sha256:b06591d330c721a3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITextSelectionDisplayInteraction

<sub>Class</sub>

An object that provides the system UI for displaying text selection.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UITextSelectionDisplayInteraction
```

## Overview

> [!note] Related sessions from WWDC23
> Session 10058: [What’s new with text and text interactions](https://developer.apple.com/videos/play/wwdc2023/10058/)

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [UIInteraction](uiinteraction.md)

## Topics

### Creating a text selection display interaction

- [- initWithTextInput:delegate:](<uitextselectiondisplayinteraction/init(textinput_delegate_).md>) — Creates a new text selection display interaction object for the specified text view.

### Managing the drawing view

- [delegate](uitextselectiondisplayinteraction/delegate.md) — A delegate that provides a container view to manage the system-supplied selection views.
- [UITextSelectionDisplayInteractionDelegate](uitextselectiondisplayinteractiondelegate.md) — An object you use to customize the presentation of text selections in your interface.

### Activating the selection UI

- [activated](uitextselectiondisplayinteraction/isactivated.md) — A Boolean value that indicates whether to display the system selection UI.

### Reporting changes to the selection

- [- setNeedsSelectionUpdate](<uitextselectiondisplayinteraction/setneedsselectionupdate().md>) — Tells the system to update the selection UI to match the current selection state.
- [- layoutManagedSubviews](<uitextselectiondisplayinteraction/layoutmanagedsubviews().md>) — Loads the selection from the text input view and lays out the selection-related views.

### Getting the text input view

- [textInput](uitextselectiondisplayinteraction/textinput.md) — The text input object that manages the selection.

### Getting the system selection views

- [highlightView](uitextselectiondisplayinteraction/highlightview.md) — The view that draws the selection highlight behind the rendered text.
- [handleViews](uitextselectiondisplayinteraction/handleviews.md) — The view that draws the selection handles for the selected text.
- [cursorView](uitextselectiondisplayinteraction/cursorview.md) — The view that draws the caret at the text insertion point.

## See Also

### Custom text selection

- [Adopting system selection UI in custom text views](adopting-system-selection-ui-in-custom-text-views.md) — Incorporate the system text-selection experience into your custom text UI in UIKit.
- [UITextSelectionHighlightView](uitextselectionhighlightview.md) — An interface you use to provide a custom highlight UI behind the selected text.
- [UITextSelectionHandleView](uitextselectionhandleview.md) — An interface you use to draw custom the selection handles for ranges of text.
- [UITextCursorView](uitextcursorview.md) — An interface you use to draw the insertion point in a piece of text.
- [UIStandardTextCursorView](uistandardtextcursorview.md) — A view that draws the standard system insertion point in a piece of text.
- [UITextCursorDropPositionAnimator](uitextcursordroppositionanimator.md)
- [UITextLoupeSession](uitextloupesession.md) — An object that manages the presentation of the system magnifier at the location you specify.
