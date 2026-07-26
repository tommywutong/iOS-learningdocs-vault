---
title: UITextCursorDropPositionAnimator
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.4+, iPadOS 17.4+, Mac Catalyst 17.4+, tvOS 17.4+, visionOS 1.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextcursordroppositionanimator
source_url: 'https://developer.apple.com/documentation/uikit/uitextcursordroppositionanimator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextcursordroppositionanimator.json'
content_hash: 'sha256:f39f1d0ec01444c2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITextCursorDropPositionAnimator

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UITextCursorDropPositionAnimator
```

## Overview

Provides a mechanism for displaying and animating a temporary text cursor to indicate a drop location.

For custom text view implementations that implement drag and drop functionality, use this animator providing either your own UITextCursorView implementation or a concrete implementation to indicate at which point in your document the dropped item will be inserted. Using this animator provides you with all of the default system animations for how the text cursor would behave.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Initializers

- [- initWithTextCursorView:textInput:](<uitextcursordroppositionanimator/init(textcursorview_textinput_).md>) — Creates an animator for the given text cursor view implementation, and the document object that implements the UITextInput protocol.

### Instance Properties

- [cursorView](uitextcursordroppositionanimator/cursorview.md) — The cursor view to be animated.
- [textInput](uitextcursordroppositionanimator/textinput.md) — The object that implements the UITextInput protocol, used to query for geometry information regarding cursor placement.

### Instance Methods

- [- animateAlongsideChanges:completion:](<uitextcursordroppositionanimator/animate(alongsidechanges_completion_).md>) — Optionally, provide an animation block or completion block to run alongside cursor appearance or position update animations.
- [- placeCursorAtPosition:animated:](<uitextcursordroppositionanimator/placecursor(at_animated_).md>) — Controls the placement of the cursor, using @c textInput and @c position to compute the final frame for the cursor view.
- [- setCursorVisible:animated:](<uitextcursordroppositionanimator/setcursorvisible(__animated_).md>) — Controls the visibility of the cursor.

## See Also

### Custom text selection

- [Adopting system selection UI in custom text views](adopting-system-selection-ui-in-custom-text-views.md) — Incorporate the system text-selection experience into your custom text UI in UIKit.
- [UITextSelectionDisplayInteraction](uitextselectiondisplayinteraction.md) — An object that provides the system UI for displaying text selection.
- [UITextSelectionHighlightView](uitextselectionhighlightview.md) — An interface you use to provide a custom highlight UI behind the selected text.
- [UITextSelectionHandleView](uitextselectionhandleview.md) — An interface you use to draw custom the selection handles for ranges of text.
- [UITextCursorView](uitextcursorview.md) — An interface you use to draw the insertion point in a piece of text.
- [UIStandardTextCursorView](uistandardtextcursorview.md) — A view that draws the standard system insertion point in a piece of text.
- [UITextLoupeSession](uitextloupesession.md) — An object that manages the presentation of the system magnifier at the location you specify.
