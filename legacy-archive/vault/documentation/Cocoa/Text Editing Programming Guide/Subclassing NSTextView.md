---
title: Text Editing Programming Guide
apple_id: 10000157i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AppKit
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TextEditing/Tasks/Subclassing.html
archived_at: '2026-07-15T07:20:16.476188Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Text Editing Programming Guide](Introduction%20to%20Text%20Editing%20Programming%20Guide%20for%20Cocoa.md)


[Next](Creating%20Custom%20Views.md)[Previous](Delegate%20Messages%20and%20Notifications.md)

# Subclassing NSTextView

This article explains how to subclass `NSTextView`. It describes the major areas where a subclass has obligations and where it can expect help in implementing new features.

The text system requires `NSTextView` subclasses to abide by certain rules of behavior, and `NSTextView` provides many methods to help subclasses do so. Some of these methods are meant to be overridden to add information and behavior into the basic infrastructure. Some are meant to be invoked as part of that infrastructure when the subclass defines its own behavior.

`NSTextView` automatically updates the Fonts window and ruler as its selection changes. If you add any new font or paragraph attributes to your subclass of `NSTextView`, you’ll need to override the methods that perform this updating to account for the added information. The `updateFontPanel` method makes the Fonts window display the font of the first character in the selection. You could override this method to update the display of an accessory view in the Fonts window. Similarly, `updateRuler` causes the ruler to display the paragraph attributes for the first paragraph in the selection. You can also override this method to customize display of items in the ruler. Be sure to invoke the `super` implementation in your override to have the basic updating performed as well.

`NSTextView` supports pasteboard operations and the dragging of files and colors into its text. If you customize the ability of your subclass to handle pasteboard operations for new data types, you should override the `readablePasteboardTypes` and `writablePasteboardTypes` methods to reflect those types. Similarly, to support new types of data for dragging operations, you should override the `acceptableDragTypes` method. Your implementation of these methods should invoke the superclass implementation, add the new data types to the array returned from `super`, and return the modified array.

To read and write custom pasteboard types, you must override the `readSelectionFromPasteboard:type:` and `writeSelectionToPasteboard:type:` methods. In your implementation of these methods, you should read the new data types your subclass supports and let the superclass handle any other types.

For dragging operations, if your subclass’s ability to accept your custom dragging types varies over time, you can override `updateDragTypeRegistration` to register or unregister the custom types according to the text view’s current status. By default this method enables dragging of all acceptable types if the receiver is editable and a rich text view.

Your subclass of `NSTextView` can customize the way selections are made for the various granularities (such as character, word, and paragraph) described in[Setting Focus and Selection Programmatically](Setting%20Focus%20and%20Selection%20Programmatically.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqheztglkdjjbeoqsjijba). While tracking user changes to the selection, whether by the mouse or keyboard, an `NSTextView` object repeatedly invokes `selectionRangeForProposedRange:granularity:` to determine what range to actually select. When finished tracking changes, it sends the delegate a `textView:willChangeSelectionFromCharacterRange:toCharacterRange:` message. By overriding the `NSTextView` method or implementing the delegate method, you can alter the way the selection is extended or reduced. For example, in a code editor you can provide a delegate that extends a double click on a brace or parenthesis character to its matching delimiter.

These mechanisms aren’t meant for changing language word definitions (such as what’s selected by a double click). That detail of selection is handled at a lower (and currently private) level of the text system.

If you create a subclass of `NSTextView` to add new capabilities that will change the text in response to user actions, you may need to modify the range selected by the user before actually applying the change. For example, if the user is making a change to the ruler, the change must apply to whole paragraphs, so the selection may have to be extended to paragraph boundaries. Three methods calculate the range to which certain kinds of change should apply. The `rangeForUserTextChange` method returns the range to which any change to characters themselves—insertions and deletions—should apply. The `rangeForUserCharacterAttributeChange` method returns the range to which a character attribute change, such as a new font or color, should apply. Finally, `rangeForUserParagraphAttributeChange` returns the range for a paragraph-level change, such as a new or moved tab stop or indent. These methods all return a range whose location is `NSNotFound` if a change isn’t possible; you should check the returned range and abandon the change in this case.

In actually making changes to the text, you must ensure that the changes are properly performed and recorded by different parts of the text system. You do this by bracketing each batch of potential changes with `shouldChangeTextInRange:replacementString:` and `didChangeText` messages. These methods ensure that the appropriate delegate messages are sent and notifications posted. The first method asks the delegate for permission to begin editing with a `textShouldBeginEditing:` message. If the delegate returns `NO`, `shouldChangeTextInRange:replacementString:` in turn returns `NO`, in which case your subclass should disallow the change. If the delegate returns `YES`, the text view posts an `NSTextDidBeginEditingNotification`, and `shouldChangeTextInRange:replacementString:` in turn returns `YES`. In this case you can make your changes to the text, and follow up by invoking `didChangeText`. This method concludes the changes by posting an `NSTextDidChangeNotification`, which results in the delegate receiving a `textDidChange:` message.

The `textShouldBeginEditing:` and `textDidBeginEditing:` messages are sent only once during an editing session. More precisely, they’re sent upon the first user input since the `NSTextView` became the first responder. Thereafter, these messages—and the `NSTextDidBeginEditingNotification`—are skipped in the sequence. The `textView:shouldChangeTextInRange:replacementString:` method, however, must be invoked for each individual change.

`NSTextView` defines several methods to aid in “smart” insertion and deletion of text, so that spacing and punctuation are preserved after a change. Smart insertion and deletion typically applies when the user has selected whole words or other significant units of text. A smart deletion of a word before a comma, for example, also deletes the space that would otherwise be left before the comma (though not placing it on the pasteboard in a Cut operation). A smart insertion of a word between another word and a comma adds a space between the two words to protect that boundary. `NSTextView` automatically uses smart insertion and deletion by default; you can turn this behavior off using `setSmartInsertDeleteEnabled:`. Doing so causes only the selected text to be deleted, and inserted text to be added, with no addition of white space.

If your subclass of `NSTextView` defines any methods that insert or delete text, you can make them smart by taking advantage of two `NSTextView` methods. The `smartDeleteRangeForProposedRange:` method expands a proposed deletion range to include any white space that should also be deleted. If you need to save the deleted text, however, it’s typically best to save only the text from the original range. For smart insertion, `smartInsertForString:replacingRange:beforeString:afterString:` returns by reference two strings that you can insert before and after a given string to preserve spacing and punctuation. See the method descriptions for more information.

[Next](Creating%20Custom%20Views.md)[Previous](Delegate%20Messages%20and%20Notifications.md)

