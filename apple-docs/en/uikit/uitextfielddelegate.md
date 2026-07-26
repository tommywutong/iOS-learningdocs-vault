---
title: UITextFieldDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextfielddelegate
source_url: 'https://developer.apple.com/documentation/uikit/uitextfielddelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextfielddelegate.json'
content_hash: 'sha256:c4a6b8084a7f1dbe'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITextFieldDelegate

<sub>Protocol</sub>

A set of optional methods to manage editing and validating text in a text field object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UITextFieldDelegate : NSObjectProtocol
```

## Overview

A text field calls the methods of its delegate in response to important changes. You use these methods to validate text that was typed by the user, to respond to specific interactions with the keyboard, and to control the overall editing process. Editing begins shortly before the text field becomes the first responder and displays the keyboard (or its assigned input view). The flow of the editing process is as follows:

1. Before becoming the first responder, the text field calls its delegate’s [- textFieldShouldBeginEditing:](<uitextfielddelegate/textfieldshouldbeginediting(__).md>) method. Use that method to allow or prevent the editing of the text field’s contents.
2. The text field becomes the first responder.

In response, the system displays the keyboard (or the text field’s input view) and posts the [UIKeyboardWillShowNotification](uiresponder/keyboardwillshownotification.md) and [UIKeyboardDidShowNotification](uiresponder/keyboarddidshownotification.md) notifications as needed. If the keyboard or another input view was already visible, the system posts the [UIKeyboardWillChangeFrameNotification](uiresponder/keyboardwillchangeframenotification.md) and [UIKeyboardDidChangeFrameNotification](uiresponder/keyboarddidchangeframenotification.md) notifications instead. 3. The text field calls its delegate’s [- textFieldDidBeginEditing:](<uitextfielddelegate/textfielddidbeginediting(__).md>) method and posts a [UITextFieldTextDidBeginEditingNotification](uitextfield/textdidbegineditingnotification.md) notification. 4. The text field calls various delegate methods during editing:

- Whenever the current text changes, it calls the [- textField:shouldChangeCharactersInRange:replacementString:](<uitextfielddelegate/textfield(__shouldchangecharactersin_replacementstring_).md>) method and posts the [UITextFieldTextDidChangeNotification](uitextfield/textdidchangenotification.md) notification.
- It calls the [- textFieldShouldClear:](<uitextfielddelegate/textfieldshouldclear(__).md>) method when the user taps the built-in button to clear the text.
- It calls the [- textFieldShouldReturn:](<uitextfielddelegate/textfieldshouldreturn(__).md>) method when the user taps the keyboard’s return button.

1. Before resigning as first responder, the text field calls its delegate’s [- textFieldShouldEndEditing:](<uitextfielddelegate/textfieldshouldendediting(__).md>) method. Use that method to validate the current text.
2. The text field resigns as first responder.

In response, the system hides or adjusts the keyboard as needed. When hiding the keyboard, the system posts the [UIKeyboardWillHideNotification](uiresponder/keyboardwillhidenotification.md) and [UIKeyboardDidHideNotification](uiresponder/keyboarddidhidenotification.md) notifications. 7. The text field calls its delegate’s [- textFieldDidEndEditing:](<uitextfielddelegate/textfielddidendediting(__).md>) method and posts a [UITextFieldTextDidEndEditingNotification](uitextfield/textdidendeditingnotification.md) notification.

For more information about the features of a text field, see [UITextField](uitextfield.md).

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Inherited By**: [UISearchTextFieldDelegate](uisearchtextfielddelegate.md)

## Topics

### Managing editing

- [- textFieldShouldBeginEditing:](<uitextfielddelegate/textfieldshouldbeginediting(__).md>) — Asks the delegate whether to begin editing in the specified text field.
- [- textFieldDidBeginEditing:](<uitextfielddelegate/textfielddidbeginediting(__).md>) — Tells the delegate when editing begins in the specified text field.
- [- textFieldShouldEndEditing:](<uitextfielddelegate/textfieldshouldendediting(__).md>) — Asks the delegate whether to stop editing in the specified text field.
- [- textFieldDidEndEditing:reason:](<uitextfielddelegate/textfielddidendediting(__reason_).md>) — Tells the delegate when editing stops for the specified text field, and the reason it stopped.
- [- textFieldDidEndEditing:](<uitextfielddelegate/textfielddidendediting(__).md>) — Tells the delegate when editing stops for the specified text field.
- [DidEndEditingReason](uitextfield/didendeditingreason.md) — Constants that indicate the reason for ending editing in a text field.

### Editing the text field’s text

- [- textField:shouldChangeCharactersInRange:replacementString:](<uitextfielddelegate/textfield(__shouldchangecharactersin_replacementstring_).md>) — Asks the delegate whether to change the specified text. _(deprecated)_
- [- textFieldShouldClear:](<uitextfielddelegate/textfieldshouldclear(__).md>) — Asks the delegate whether to remove the text field’s current contents.
- [- textFieldShouldReturn:](<uitextfielddelegate/textfieldshouldreturn(__).md>) — Asks the delegate whether to process the pressing of the Return button for the text field.

### Managing text selection

- [- textFieldDidChangeSelection:](<uitextfielddelegate/textfielddidchangeselection(__).md>) — Tells the delegate when the text selection changes in the specified text field.

### Providing a context menu

- [- textField:editMenuForCharactersInRange:suggestedActions:](<uitextfielddelegate/textfield(__editmenuforcharactersin_suggestedactions_).md>) — Asks the delegate for the menu to display in the text field, based on the text range and actions the system provides. _(deprecated)_

### Customizing an edit menu

- [- textField:willPresentEditMenuWithAnimator:](<uitextfielddelegate/textfield(__willpresenteditmenuwith_).md>) — Tells the delegate that the system is about to present an edit menu with an animator.
- [- textField:willDismissEditMenuWithAnimator:](<uitextfielddelegate/textfield(__willdismisseditmenuwith_).md>) — Tells the delegate that the system is about to dismiss an edit menu with an animator.

### Inserting a Smart Reply suggestion

- [- textField:insertInputSuggestion:](<uitextfielddelegate/textfield(__insertinputsuggestion_).md>) — Tells the delegate when the keyboard delivers an input suggestion.

### Instance Methods

- [- textField:editMenuForCharactersInRanges:suggestedActions:](<uitextfielddelegate/textfield(__editmenuforcharactersinranges_suggestedactions_).md>)
- [- textField:shouldChangeCharactersInRanges:replacementString:](<uitextfielddelegate/textfield(__shouldchangecharactersinranges_replacementstring_).md>)

## See Also

### Validating and handling edits

- [delegate](uitextfield/delegate.md) — The text field’s delegate.
