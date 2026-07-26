---
title: UITextInput
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextinput
source_url: 'https://developer.apple.com/documentation/uikit/uitextinput'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinput.json'
content_hash: 'sha256:bbd5fe96e813c49a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITextInput

<sub>Protocol</sub>

A set of methods for interacting with the text input system and enabling features in documents.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UITextInput : UIKeyInput
```

## Overview

Objects that adopt the [UITextInput](uitextinput.md) protocol maintain information about text input and provide that information to the text input system on demand. A [UITextInput](uitextinput.md) object interacts with the text input system by:

- Reporting text positions and text ranges
- Responding to queries layout and writing direction
- Performing hit-testing — returning text positions and ranges for a specific point
- Providing the system with rectangles for highlighting ranges of text and drawing the _caret_, a glyph that represents the insertion point during text entry

In addition, a [UITextInput](uitextinput.md) object maintains ranges for selected text and marked text. Marked text, a part of multistage text input, represents provisionally inserted text that the user has yet to confirm. The range of marked text always contains a range of selected text, which might be a range of characters or the caret. Multistage text input is a requirement when the language is ideographic and the keyboard is phonetic.

### Integrate with the text input system

The [UITextInput](uitextinput.md) protocol works with other classes and protocols to integrate text-processing apps with the text input system:

- **[UITextPosition](uitextposition.md) and [UITextRange](uitextrange.md) classes** — All [UITextInput](uitextinput.md)-conforming document classes must create custom subclasses of these classes. A [UITextPosition](uitextposition.md) object represents a position in a text container. A [UITextRange](uitextrange.md) object, which encapsulates beginning and ending [UITextPosition](uitextposition.md) objects, represents a range of characters in the text container.
- **[UITextInputTokenizer](uitextinputtokenizer.md) protocol and [UITextInputStringTokenizer](uitextinputstringtokenizer.md) class** — The [UITextInputTokenizer](uitextinputtokenizer.md) protocol defines an interface for tokenizing input text. The [UITextInputStringTokenizer](uitextinputstringtokenizer.md) class is a default implementation of this protocol.
- **[UITextInputDelegate](uitextinputdelegate.md) protocol** — The text input system automatically assigns its own text input delegate (which conforms to this protocol) to the [UITextInput](uitextinput.md)-conforming document object. This text input delegate allows document objects to inform the input system of changes in text and selection.
- **[UIKeyInput](uikeyinput.md) protocol** — Implement this protocol to allow text entry and deletion at an insertion point.

### Customize keyboard behavior

The [UITextInput](uitextinput.md) protocol also inherits the [UITextInputTraits](uitextinputtraits.md) protocol, which provides customization of the keyboard and its behaviors.

When the user chooses dictation input on a supported device, the system automatically inserts recognized phrases into the current text view. Methods in the [UITextInput](uitextinput.md) protocol allow your app to respond to the completion of dictation. You can use an object of the [UIDictationPhrase](uidictationphrase.md) class to obtain a string that represents a phrase the user dictates. In the case of ambiguous dictation results, a dictation phrase object provides an array that contains alternative strings.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [UIKeyInput](uikeyinput.md), [UITextInputTraits](uitextinputtraits.md)

- **Inherited By**: [UITextDraggable](uitextdraggable.md), [UITextDroppable](uitextdroppable.md)

- **Conforming Types**: [UISearchTextField](uisearchtextfield.md), [UITextField](uitextfield.md), [UITextView](uitextview.md)

## Topics

### Handling text input

- [inputDelegate](uitextinput/inputdelegate.md) — An input delegate that receives a notification when text changes or when the selection changes.
- [UITextInputDelegate](uitextinputdelegate.md) — An intermediary between a document and the text input system.

### Replacing and returning text

- [- textInRange:](<uitextinput/text(in_).md>) — Returns the text in the specified range.
- [- replaceRange:withText:](<uitextinput/replace(__withtext_).md>) — Replaces the text in a document that is in the specified range.
- [- shouldChangeTextInRange:replacementText:](<uitextinput/shouldchangetext(in_replacementtext_).md>) — Asks whether to replace the text in the specified range.

### Working with marked and selected text

- [selectedTextRange](uitextinput/selectedtextrange.md) — The range of selected text in a document.
- [markedTextRange](uitextinput/markedtextrange.md) — The range of currently marked text in a document.
- [markedTextStyle](uitextinput/markedtextstyle.md) — A dictionary of attributes that describes how to draw marked text.
- [- setMarkedText:selectedRange:](<uitextinput/setmarkedtext(__selectedrange_).md>) — Inserts the provided text and marks it to indicate that it is part of an active input session.
- [- setAttributedMarkedText:selectedRange:](<uitextinput/setattributedmarkedtext(__selectedrange_).md>) — Inserts the provided styled text and marks it to indicate that it is part of an active input session.
- [- unmarkText](<uitextinput/unmarktext().md>) — Unmarks the currently marked text.
- [selectionAffinity](uitextinput/selectionaffinity.md) — The desired location for the insertion point.

### Computing text ranges and text positions

- [- textRangeFromPosition:toPosition:](<uitextinput/textrange(from_to_).md>) — Returns the range between two text positions.
- [- positionFromPosition:offset:](<uitextinput/position(from_offset_).md>) — Returns the text position at a specified offset from another text position.
- [- positionFromPosition:inDirection:offset:](<uitextinput/position(from_in_offset_).md>) — Returns the text position at a specified offset in a specified direction from another text position.
- [beginningOfDocument](uitextinput/beginningofdocument.md) — The text position for the beginning of a document.
- [endOfDocument](uitextinput/endofdocument.md) — The text position for the end of a document.

### Evaluating text positions

- [- comparePosition:toPosition:](<uitextinput/compare(__to_).md>) — Returns how one text position compares to another text position.
- [- offsetFromPosition:toPosition:](<uitextinput/offset(from_to_).md>) — Returns the number of UTF-16 characters between one text position and another text position.

### Making the view non-editable

- [editable](uitextinput/iseditable.md) — A Boolean value that indicates whether the text view contains editable text.

### Determining layout and writing direction

- [- positionWithinRange:farthestInDirection:](<uitextinput/position(within_farthestin_).md>) — Returns the text position that is at the farthest extent in a specified layout direction within a range of text.
- [- characterRangeByExtendingPosition:inDirection:](<uitextinput/characterrange(byextending_in_).md>) — Returns a text range from a specified text position to its farthest extent in a certain direction of layout.
- [- baseWritingDirectionForPosition:inDirection:](<uitextinput/basewritingdirection(for_in_).md>) — Returns the base writing direction for a position in the text going in a certain direction.
- [- setBaseWritingDirection:forRange:](<uitextinput/setbasewritingdirection(__for_).md>) — Sets the base writing direction for a specified range of text in a document.

### Working with geometry and hit-testing

- [- firstRectForRange:](<uitextinput/firstrect(for_).md>) — Returns the first rectangle that encloses a range of text in a document.
- [- closestPositionToPoint:](<uitextinput/closestposition(to_).md>) — Returns the position in a document that is closest to a specified point.
- [- selectionRectsForRange:](<uitextinput/selectionrects(for_).md>) — Returns an array of selection rects corresponding to the range of text.
- [- closestPositionToPoint:withinRange:](<uitextinput/closestposition(to_within_).md>) — Returns the position in a document that is closest to a specified point in a specified range.
- [- characterRangeAtPoint:](<uitextinput/characterrange(at_).md>) — Returns the character or range of characters that is at a specified point in a document.

### Providing the caret layout information

- [- caretRectForPosition:](<uitextinput/caretrect(for_).md>) — Returns a rectangle to draw the caret at a specified insertion point.
- [- caretTransformForPosition:](<uitextinput/carettransform(for_).md>) — Returns the transform to apply to the caret prior to drawing.

### Tokenizing input text

- [tokenizer](uitextinput/tokenizer.md) — An input tokenizer that provides information about the granularity of text units.
- [UITextInputTokenizer](uitextinputtokenizer.md) — A tokenizer, which is an object that allows the text input system to evaluate text units of different granularities.

### Managing the floating cursor

- [- beginFloatingCursorAtPoint:](<uitextinput/beginfloatingcursor(at_).md>) — Tells the object when the gesture that the system uses to manipulate the cursor begins.
- [- updateFloatingCursorAtPoint:](<uitextinput/updatefloatingcursor(at_).md>) — Tells the object that the floating cursor moved to a new location.
- [- endFloatingCursor](<uitextinput/endfloatingcursor().md>) — Tells the object when the gesture that the system uses to manipulate the cursor ends.

### Using dictation

- [- dictationRecordingDidEnd](<uitextinput/dictationrecordingdidend().md>) — Tells the object when there is a pending dictation result.
- [- dictationRecognitionFailed](<uitextinput/dictationrecognitionfailed().md>) — Tells the object when dictation ends, but recognition fails.
- [- insertDictationResult:](<uitextinput/insertdictationresult(__).md>) — Tells the object when there is more than one interpretation of a spoken phrase in a dictation result.
- [insertDictationResultPlaceholder](uitextinput/insertdictationresultplaceholder.md) — Asks for the placeholder object to use while generating dictation results.
- [- frameForDictationResultPlaceholder:](<uitextinput/frame(fordictationresultplaceholder_).md>) — Asks for the rectangle for displaying the dictation placeholder animation.
- [- removeDictationResultPlaceholder:willInsertResult:](<uitextinput/removedictationresultplaceholder(__willinsertresult_).md>) — Tells the view that the specified placeholder object is unnecessary.

### Managing placeholders

- [- insertTextPlaceholderWithSize:](<uitextinput/inserttextplaceholder(with_).md>) — Inserts a placeholder object to reserve visual space during text input.
- [- removeTextPlaceholder:](<uitextinput/remove(__).md>) — Removes a placeholder object from the text input view.
- [UITextPlaceholder](uitextplaceholder.md) — A placeholder object that reserves visual space in a text input view.

### Managing the edit menu

- [- editMenuForTextRange:suggestedActions:](<uitextinput/editmenu(for_suggestedactions_).md>) — Asks for the menu to display for the given text range and actions the system provides.
- [- willPresentEditMenuWithAnimator:](<uitextinput/willpresenteditmenu(animator_).md>) — Tells the object when the system is about to present an edit menu with an animator.
- [- willDismissEditMenuWithAnimator:](<uitextinput/willdismisseditmenu(animator_).md>) — Tells the object when the system is about to dismiss an edit menu with an animator.

### Supporting text-phrase alternatives

- [- insertText:alternatives:style:](<uitextinput/inserttext(__alternatives_style_).md>)
- [UITextAlternativeStyle](uitextalternativestyle.md) — A constant that determines if the system highlights alternative phrases during text input.

### Inserting a Smart Reply suggestion

- [- insertInputSuggestion:](<uitextinput/insert(__).md>) — Inserts the user or system’s input suggestion into the document.

### Supporting adaptive images

- [supportsAdaptiveImageGlyph](uitextinput/supportsadaptiveimageglyph.md) — A Boolean value that indicates whether the document supports adaptive images in the input.
- [- insertAdaptiveImageGlyph:replacementRange:](<uitextinput/insert(__replacementrange_).md>) — Inserts an adaptive image into the text at the specifed location.

### Returning text-styling information

- [- textStylingAtPosition:inDirection:](<uitextinput/textstyling(at_in_).md>) — Returns a dictionary with properties that specify how to style the text at a certain location in a document.

### Reconciling text position and character offset

- [- positionWithinRange:atCharacterOffset:](<uitextinput/position(within_atcharacteroffset_).md>) — Returns the position within a range of a document’s text that corresponds to the character offset from the start of that range.
- [- characterOffsetOfPosition:withinRange:](<uitextinput/characteroffset(of_within_).md>) — Returns the character offset of a position in a document’s text that falls within a specified range.

### Returning the text input view

- [textInputView](uitextinput/textinputview.md) — An affiliated view that provides a coordinate system for all geometric values in the protocol.

### Constants

- [UITextDirection](uitextdirection.md) — The direction of the text.
- [UITextStorageDirection](uitextstoragedirection.md) — The direction of text storage.
- [UITextLayoutDirection](uitextlayoutdirection.md) — The direction of text layout.

### Deprecated

- [UITextWritingDirection](uitextwritingdirection.md) — The writing direction of the text for the language. _(deprecated)_
- [Style dictionary keys](style-dictionary-keys.md) — A dictionary that contains properties that define text style characteristics.

### Instance Properties

- [unobscuredContentRect](uitextinput/unobscuredcontentrect.md) — The visible content region, excluding parts covered by view-specific UI.

### Instance Methods

- [- attributedTextInRange:](<uitextinput/attributedtext(in_).md>)
- [- didDismissWritingTools](<uitextinput/diddismisswritingtools().md>)
- [- insertAttributedText:](<uitextinput/insertattributedtext(__).md>)
- [- replaceRange:withAttributedText:](<uitextinput/replace(__withattributedtext_).md>)
- [- willPresentWritingTools](<uitextinput/willpresentwritingtools().md>)

## See Also

### Text input

- [UITextInputDelegate](uitextinputdelegate.md) — An intermediary between a document and the text input system.
- [UIKeyInput](uikeyinput.md) — A set of methods a responder uses to implement simple text entry.
- [UITextInputTraits](uitextinputtraits.md) — A set of methods that defines features for keyboard input to a text object.
- [UITextInputContext](uitextinputcontext.md) — An object that reports the type of input your app receives.
- [UITextInputMode](uitextinputmode.md) — The current text input mode.
- [UITextInputAssistantItem](uitextinputassistantitem.md) — An object that manages custom bar button items that you add to the shortcuts bar above the keyboard on iPad.
- [UIDictationPhrase](uidictationphrase.md) — An object that represents the textual interpretation of a spoken phrase that the user dictates.
