---
title: UITextSelectionHandleView
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextselectionhandleview
source_url: 'https://developer.apple.com/documentation/uikit/uitextselectionhandleview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextselectionhandleview.json'
content_hash: 'sha256:cbf0ea60ffac1255'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITextSelectionHandleView

<sub>Protocol</sub>

An interface you use to draw custom the selection handles for ranges of text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UITextSelectionHandleView : UICoordinateSpace
```

## Overview

Adopt the [UITextSelectionHandleView](uitextselectionhandleview.md) protocol in a custom view you use to draw text-selection handles in one of your text views. Use your custom view in conjunction with a [UITextSelectionDisplayInteraction](uitextselectiondisplayinteraction.md) object to apply your custom selection UI to one of your text views. This protocol provides the preferred frame for the selection handle, and you provide details about the handle back to the system. Use [CALayer](../quartzcore/calayer.md) objects or your view’s [- drawRect:](<uiview/draw(__).md>) method to draw the handles.

After adopting this protocol in your custom view, create exactly two instances and assign them to the [handleViews](uitextselectiondisplayinteraction/handleviews.md) property of the interaction object you attached to your text view. Configure one instance as the leading selection handle, and configure the other instance as the trailing selection handle.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [UICoordinateSpace](uicoordinatespace.md)

## Topics

### Providing the preferred frame rectangle

- [- preferredFrameForRect:](<uitextselectionhandleview/preferredframe(for_).md>) — Provides a preferred frame given @c rect based on the current appearance configuration.

### Specifying the handle details

- [direction](uitextselectionhandleview/direction.md) — The orientation of the selection handle.
- [customShape](uitextselectionhandleview/customshape.md) — The custom shape to draw for the stem of the selection handle.
- [vertical](uitextselectionhandleview/isvertical.md) — Convenience accessor for @c direction calculations.

## See Also

### Custom text selection

- [Adopting system selection UI in custom text views](adopting-system-selection-ui-in-custom-text-views.md) — Incorporate the system text-selection experience into your custom text UI in UIKit.
- [UITextSelectionDisplayInteraction](uitextselectiondisplayinteraction.md) — An object that provides the system UI for displaying text selection.
- [UITextSelectionHighlightView](uitextselectionhighlightview.md) — An interface you use to provide a custom highlight UI behind the selected text.
- [UITextCursorView](uitextcursorview.md) — An interface you use to draw the insertion point in a piece of text.
- [UIStandardTextCursorView](uistandardtextcursorview.md) — A view that draws the standard system insertion point in a piece of text.
- [UITextCursorDropPositionAnimator](uitextcursordroppositionanimator.md)
- [UITextLoupeSession](uitextloupesession.md) — An object that manages the presentation of the system magnifier at the location you specify.
