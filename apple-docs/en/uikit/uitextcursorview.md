---
title: UITextCursorView
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextcursorview
source_url: 'https://developer.apple.com/documentation/uikit/uitextcursorview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextcursorview.json'
content_hash: 'sha256:603f6b384f293dca'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITextCursorView

<sub>Protocol</sub>

An interface you use to draw the insertion point in a piece of text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UITextCursorView : UICoordinateSpace
```

## Overview

Adopt the [UITextCursorView](uitextcursorview.md) protocol in a custom view you use to draw the insertion caret in one of your text views. Use your custom view in conjunction with a [UITextSelectionDisplayInteraction](uitextselectiondisplayinteraction.md) object to apply your custom selection UI to one of your text views. This protocol provides details about when to display the blink animations. Use [CALayer](../quartzcore/calayer.md) objects or your view’s [- drawRect:](<uiview/draw(__).md>) method to draw and animate the caret.

After adopting this protocol in your custom view, assign your view to the [cursorView](uitextselectiondisplayinteraction/cursorview.md) property of the interaction object you attached to your text view.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [UICoordinateSpace](uicoordinatespace.md)

- **Conforming Types**: [UIStandardTextCursorView](uistandardtextcursorview.md)

## Topics

### Determining the animation state

- [blinking](uitextcursorview/isblinking.md) — A Boolean value that determines whether the blink animation is running.
- [- resetBlinkAnimation](<uitextcursorview/resetblinkanimation().md>) — Resets the blink animation to avoid glitches while someone is typing.

## See Also

### Custom text selection

- [Adopting system selection UI in custom text views](adopting-system-selection-ui-in-custom-text-views.md) — Incorporate the system text-selection experience into your custom text UI in UIKit.
- [UITextSelectionDisplayInteraction](uitextselectiondisplayinteraction.md) — An object that provides the system UI for displaying text selection.
- [UITextSelectionHighlightView](uitextselectionhighlightview.md) — An interface you use to provide a custom highlight UI behind the selected text.
- [UITextSelectionHandleView](uitextselectionhandleview.md) — An interface you use to draw custom the selection handles for ranges of text.
- [UIStandardTextCursorView](uistandardtextcursorview.md) — A view that draws the standard system insertion point in a piece of text.
- [UITextCursorDropPositionAnimator](uitextcursordroppositionanimator.md)
- [UITextLoupeSession](uitextloupesession.md) — An object that manages the presentation of the system magnifier at the location you specify.
