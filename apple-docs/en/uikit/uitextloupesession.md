---
title: UITextLoupeSession
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextloupesession
source_url: 'https://developer.apple.com/documentation/uikit/uitextloupesession'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextloupesession.json'
content_hash: 'sha256:3680fc6d4096343b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITextLoupeSession

<sub>Class</sub>

An object that manages the presentation of the system magnifier at the location you specify.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
@MainActor class UITextLoupeSession
```

## Overview

A [UITextLoupeSession](uitextloupesession.md) object programmatically displays the system loupe in your view. You might display this view to allow someone to magnify your view’s content. Typically, you display the loupe from a [UIPanGestureRecognizer](uipangesturerecognizer.md) when someone interacts with your view. As the location in the gesture recognizer changes, use the loupe session object to update the position of the loupe.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Creating the loupe session

- [+ beginLoupeSessionAtPoint:fromSelectionWidgetView:inView:](<uitextloupesession/begin(at_fromselectionwidgetview_in_).md>) — Creates a new loupe session and displays the loupe at the specified location in your view.

### Updating the loupe during the session

- [- moveToPoint:withCaretRect:trackingCaret:](<uitextloupesession/move(to_withcaretrect_trackingcaret_).md>) — Moves the loupe to the specified point in the session’s associated view.
- [- invalidate](<uitextloupesession/invalidate().md>) — Hides the loupe and cleans up any session-related state.

## See Also

### Custom text selection

- [Adopting system selection UI in custom text views](adopting-system-selection-ui-in-custom-text-views.md) — Incorporate the system text-selection experience into your custom text UI in UIKit.
- [UITextSelectionDisplayInteraction](uitextselectiondisplayinteraction.md) — An object that provides the system UI for displaying text selection.
- [UITextSelectionHighlightView](uitextselectionhighlightview.md) — An interface you use to provide a custom highlight UI behind the selected text.
- [UITextSelectionHandleView](uitextselectionhandleview.md) — An interface you use to draw custom the selection handles for ranges of text.
- [UITextCursorView](uitextcursorview.md) — An interface you use to draw the insertion point in a piece of text.
- [UIStandardTextCursorView](uistandardtextcursorview.md) — A view that draws the standard system insertion point in a piece of text.
- [UITextCursorDropPositionAnimator](uitextcursordroppositionanimator.md)
