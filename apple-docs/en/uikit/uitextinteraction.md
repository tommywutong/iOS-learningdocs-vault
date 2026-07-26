---
title: UITextInteraction
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextinteraction
source_url: 'https://developer.apple.com/documentation/uikit/uitextinteraction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinteraction.json'
content_hash: 'sha256:668e83260689bb45'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITextInteraction

<sub>Class</sub>

An interaction that provides text selection gestures and UI to custom text views.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UITextInteraction
```

## Overview

Use [UITextInteraction](uitextinteraction.md) to provide your custom text views the same text selection gestures and UI available in native text views like [UITextView](uitextview.md) and [UITextField](uitextfield.md). When creating a text interaction, choose a mode that matches the state of the text, [UITextInteractionModeEditable](uitextinteractionmode/editable.md) or [UITextInteractionModeNonEditable](uitextinteractionmode/noneditable.md). Then set the [textInput](uitextinteraction/textinput.md) property to an object that conforms to [UITextInput](uitextinput.md), and add the interaction to a view.

```swift
// Create a selection interaction for non-editable content.
let selectionInteraction = UITextInteraction(for: .nonEditable)

// Assign `textInput` to your view that implements the `UITextInput` protocol
// to get more control over the selection behavior and the text input system.
selectionInteraction.textInput = customTextView

// Add the interaction to the view.
customTextView.addInteraction(selectionInteraction)
```

If your custom text view supports editable and non-editable text, create two interactions — one for each mode — and add the interaction that matches the state of text to the view while removing the other interaction.

```swift
override func becomeFirstResponder() -> Bool {
    let isFirstResponder = self.isFirstResponder
    let result = super.becomeFirstResponder()
    
    if isFirstResponder == false && self.isFirstResponder == true {
        customTextView.removeInteraction(nonEditableTextInteraction)
        customTextView.addInteraction(editableTextInteraction)
    }
    
    return result
}

override func resignFirstResponder() -> Bool {
    let isFirstResponder = self.isFirstResponder
    let result = super.resignFirstResponder()
    
    if isFirstResponder == true && self.isFirstResponder == false {
        customTextView.removeInteraction(editableTextInteraction)
        customTextView.addInteraction(nonEditableTextInteraction)
    }
    
    return result
}
```

If your app provides other gestures in the same view hierarchy, you can use the [- requireGestureRecognizerToFail:](<uigesturerecognizer/require(tofail_).md>) method to set up failure requirements between your app’s gestures and the text interaction gestures listed in the [gesturesForFailureRequirements](uitextinteraction/gesturesforfailurerequirements.md) property.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [UIInteraction](uiinteraction.md)

## Topics

### Creating text interactions

- [+ textInteractionForMode:](<uitextinteraction/init(for_).md>) — Creates a text interaction with the specified mode.

### Handling text input and interaction events

- [textInput](uitextinteraction/textinput.md) — The object that interacts with the text input system.
- [delegate](uitextinteraction/delegate.md) — The object that receives events from the text interaction.
- [UITextInteractionDelegate](uitextinteractiondelegate.md) — An interface that an object implements to receive information about text interaction events.

### Getting interaction information

- [gesturesForFailureRequirements](uitextinteraction/gesturesforfailurerequirements.md) — The list of gestures that the text interaction adds to the view hierarchy.
- [textInteractionMode](uitextinteraction/textinteractionmode.md) — The mode of the text interaction.
- [UITextInteractionMode](uitextinteractionmode.md) — Modes that determine the selection behaviors that a text interaction provides.

### Initializers

- [init(forMode:)](<uitextinteraction/init(formode_).md>)

## See Also

### Text interactions

- [UITextInteractionDelegate](uitextinteractiondelegate.md) — An interface that an object implements to receive information about text interaction events.
- [UITextInteractionMode](uitextinteractionmode.md) — Modes that determine the selection behaviors that a text interaction provides.
