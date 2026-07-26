---
title: Handling text interactions in custom keyboards
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/handling-text-interactions-in-custom-keyboards
source_url: 'https://developer.apple.com/documentation/uikit/handling-text-interactions-in-custom-keyboards'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/handling-text-interactions-in-custom-keyboards.json'
content_hash: 'sha256:d0840d42fa583132'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md) · [Keyboards and input](keyboards-and-input.md) · [Creating a custom keyboard](creating-a-custom-keyboard.md)

# Handling text interactions in custom keyboards

<sub>Article</sub>

Insert, delete, and manipulate text by using a proxy to a text input view.

## Overview

Custom keyboards execute in a separate process that doesn’t have direct access to the text a user is editing. A proxy object, [UITextDocumentProxy](uitextdocumentproxy.md), provides access to the input text view. Through the text document proxy you can insert or delete text, manipulate the insertion point, and access additional textual context around the insertion point.

![](../../../attachments/5d24d830be3383436ad7ed079165abfc/media-3570308@2x.png)

<sub>Diagram showing the relationship of a custom keyboard extension process to the text input object. In the keyboard extension process the input view controller uses the text document proxy to insert a string into the text input view.</sub>

### Insert and delete text

The text document proxy conforms to the [UIKeyInput](uikeyinput.md) protocol, providing methods for inserting and deleting text. To insert a character or string into the current input view:

```swift
textDocumentProxy.insertText("Hello world.")
```

To delete the character preceding the current insertion point:

```swift
textDocumentProxy.deleteBackward()
```

You can determine if the input view has any text at all using the [hasText](uikeyinput/hastext.md) property:

```swift
if textDocumentProxy.hasText {
    // Do something with the text
}

```

### Adjust the insertion point

To move the insertion point in the text input view, use the [- adjustTextPositionByCharacterOffset:](<uitextdocumentproxy/adjusttextposition(bycharacteroffset_).md>) method. For example, if you want to implement a forward delete action, move the insertion position forward by one character then delete backwards:

```swift
// Move the text insertion position forward 1 character
textDocumentProxy.adjustTextPosition(byCharacterOffset: 1)

// Delete the previous character
textDocumentProxy.deleteBackward()
```

You might choose to enable this capability only when the insertion point isn’t at the end of the text being input by checking the context after the insertion point. See [Get context around the insertion point](handling-text-interactions-in-custom-keyboards.md#Get-context-around-the-insertion-point) for more details.

### Respond to changes while the user is editing

While your keyboard is active, the user may perform operations that change the text or selection. Your custom keyboard controller, a subclass of [UIInputViewController](uiinputviewcontroller.md) that conforms to the [UITextInputDelegate](uitextinputdelegate.md) protocol, can automatically be informed of these text and selection changes. You can override two sets of methods in this delegate protocol to receive these notifications. The first set is called when text is changing, and the second is called when the selection is changing. Because your keyboard extension doesn’t have direct access to the text input field, the argument is `nil`.

```swift
func textWillChange(_ textInput: UITextInput?)
func textDidChange(_ textInput: UITextInput?)

func selectionWillChange(_ textInput: UITextInput?)
func selectionDidChange(_ textInput: UITextInput?)
```

### Get context around the insertion point

To perform certain operations like autocomplete or autocapitalization, you may need additional context of the text surrounding what the user is typing. You can access the context before and after the insertion point as follows:

```swift
let precedingText = textDocumentProxy.documentContextBeforeInput ?? ""
let followingText = textDocumentProxy.documentContextAfterInput ?? ""
let selectedText = textDocumentProxy.selectedText ?? ""
let fullText = "\(precedingText)\(selectedText)\(followingText)"
```

Use [CFStringTokenizer](../corefoundation/cfstringtokenizer.md) to better understand the context by breaking the surrounding text (or combined text) into words, paragraphs, or sentences. This information enables you to implement autocapitalization.

1. Call [documentContextBeforeInput](uitextdocumentproxy/documentcontextbeforeinput.md) to get the text preceding the insertion point.
2. Use [CFStringTokenizer](../corefoundation/cfstringtokenizer.md) to locate the beginning of the current word.
3. Move the insertion point after the first character of the word.
4. Call [- deleteBackward](<uikeyinput/deletebackward().md>).
5. Call [- insertText:](<uikeyinput/inserttext(__).md>) and pass the appropriate capitalized letter.
6. Move the insertion point back to its original position.

### Mark text while the user is editing

Some text input operations require multiple actions in order to complete a single character or word. For example, your keyboard might support a language that requires multiple keystrokes to compose a single character. [UITextDocumentProxy](uitextdocumentproxy.md) allows you to insert text and mark some or all of it for subsequent editing operations. The following code shows how you could insert a combining accent character as marked text using [- setMarkedText:selectedRange:](<uitextdocumentproxy/setmarkedtext(__selectedrange_).md>):

```swift
let accentCharacter = " \u{0301}"
let range = NSRange(location: 0, length: accentCharacter.count)
textDocumentProxy.setMarkedText(accentCharacter, selectedRange: range)
```

Calling `setMarkedText` selects the text specified by `range`. Subsequent insertions replace the characters selected in the range. In the example above, a space with a combining acute accent is shown. If the next character input by the user is an `a`, you could then insert a combined `á`.

```swift
textDocumentProxy.insertText("a\u{0301}")
```

If the range passed to [- setMarkedText:selectedRange:](<uitextdocumentproxy/setmarkedtext(__selectedrange_).md>) only covers a portion of the string passed in, the nonselected portion is marked with a background color. You could use this to display autocompleted content. For example, if you supported autocompletion of names and the user had typed “Anth”, you might display “Anthony” as the autocompletion:

```swift
let text = "Anthony"
let range = NSRange(location: 4, length: 3)
textDocumentProxy.setMarkedText(text, selectedRange: range)
```

The above would display the text as:

![](../../../attachments/2b0de0baa7f34b710e5edbc57971968a/media-3570318@2x.png)

<sub>Screenshot showing text showing marked text. The beginning of the word is marked to indicate that it’s being autocompleted, and the end of the word is selected to indicate that subsequent keystrokes will replace that portion of the text.</sub>

As the user continues to type, you can update the marked text with subsequent calls to [- setMarkedText:selectedRange:](<uitextdocumentproxy/setmarkedtext(__selectedrange_).md>).

Call [- unmarkText](<uitextdocumentproxy/unmarktext().md>) to clear the marked text indication, leaving the text in the input view.
