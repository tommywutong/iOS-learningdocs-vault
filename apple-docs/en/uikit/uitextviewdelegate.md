---
title: UITextViewDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextviewdelegate
source_url: 'https://developer.apple.com/documentation/uikit/uitextviewdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextviewdelegate.json'
content_hash: 'sha256:eb45c51f5d99326a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITextViewDelegate

<sub>Protocol</sub>

The methods for receiving editing-related messages for text view objects.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UITextViewDelegate : UIScrollViewDelegate
```

## Overview

All of the methods in this protocol are optional. You can use them in situations where you might want to adjust the text a user is editing (such as in the case of a spell-checker program) or to modify the intended insertion point.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [UIScrollViewDelegate](uiscrollviewdelegate.md)

## Topics

### Responding to editing notifications

- [- textViewShouldBeginEditing:](<uitextviewdelegate/textviewshouldbeginediting(__).md>) — Asks the delegate whether to begin editing in the specified text view.
- [- textViewDidBeginEditing:](<uitextviewdelegate/textviewdidbeginediting(__).md>) — Tells the delegate when editing of the specified text view begins.
- [- textViewShouldEndEditing:](<uitextviewdelegate/textviewshouldendediting(__).md>) — Asks the delegate whether to stop editing in the specified text view.
- [- textViewDidEndEditing:](<uitextviewdelegate/textviewdidendediting(__).md>) — Tells the delegate when editing of the specified text view ends.

### Responding to text changes

- [- textView:shouldChangeTextInRange:replacementText:](<uitextviewdelegate/textview(__shouldchangetextin_replacementtext_).md>) — Asks the delegate whether to replace the specified text in the text view. _(deprecated)_
- [- textViewDidChange:](<uitextviewdelegate/textviewdidchange(__).md>) — Tells the delegate when the user changes the text or attributes in the specified text view.

### Responding to selection changes

- [- textViewDidChangeSelection:](<uitextviewdelegate/textviewdidchangeselection(__).md>) — Tells the delegate when the text selection changes in the specified text view.

### Interacting with text data

- [- textView:menuConfigurationForTextItem:defaultMenu:](<uitextviewdelegate/textview(__menuconfigurationfor_defaultmenu_).md>) — Asks the delegate for the menu configuration to be performed when interacting with a text item.
- [- textView:primaryActionForTextItem:defaultAction:](<uitextviewdelegate/textview(__primaryactionfor_defaultaction_).md>) — Asks the delegate for the action to be performed when interacting with a text item. If a nil action is provided, the text view will request a menu to be presented on primary action if possible.
- [- textView:textItemMenuWillDisplayForTextItem:animator:](<uitextviewdelegate/textview(__textitemmenuwilldisplayfor_animator_).md>) — Informs the delegate that a text item menu is about to be presented with the specified animator.
- [- textView:textItemMenuWillEndForTextItem:animator:](<uitextviewdelegate/textview(__textitemmenuwillendfor_animator_).md>) — Informs the delegate that a text item menu is about to be dismissed with the specified animator.

### Providing a context menu

- [- textView:editMenuForTextInRange:suggestedActions:](<uitextviewdelegate/textview(__editmenufortextin_suggestedactions_).md>) — Asks the delegate for the menu to display in the text view, based on the text range and actions the system provides. _(deprecated)_

### Customizing an edit menu

- [- textView:willDismissEditMenuWithAnimator:](<uitextviewdelegate/textview(__willdismisseditmenuwith_).md>)
- [- textView:willPresentEditMenuWithAnimator:](<uitextviewdelegate/textview(__willpresenteditmenuwith_).md>)

### Responding to writing tools interactions

- [- textViewWritingToolsWillBegin:](<uitextviewdelegate/textviewwritingtoolswillbegin(__).md>) — Tells the delegate that an interaction with the writing tools interface is about to begin.
- [- textViewWritingToolsDidEnd:](<uitextviewdelegate/textviewwritingtoolsdidend(__).md>) — Tells the delegate that the current writing tools session ended.
- [- textView:writingToolsIgnoredRangesInEnclosingRange:](<uitextviewdelegate/textview(__writingtoolsignoredrangesinenclosingrange_).md>) — Asks the delegate to specify any ranges of text you want the writing tools to ignore.

### Inserting a Smart Reply suggestion

- [- textView:insertInputSuggestion:](<uitextviewdelegate/textview(__insertinputsuggestion_).md>) — Tells the delegate when the keyboard delivers an input suggestion.

### Deprecated

- [- textView:shouldInteractWithTextAttachment:inRange:interaction:](<uitextviewdelegate/textview(__shouldinteractwith_in_interaction_)-5qha9.md>) — Asks the delegate whether the specified text view allows the specified type of user interaction with the provided text attachment in the specified range of text. _(deprecated)_
- [- textView:shouldInteractWithURL:inRange:interaction:](<uitextviewdelegate/textview(__shouldinteractwith_in_interaction_)-622ub.md>) — Asks the delegate whether the specified text view allows the specified type of user interaction with the specified URL in the specified range of text. _(deprecated)_
- [- textView:shouldInteractWithTextAttachment:inRange:](<uitextviewdelegate/textview(__shouldinteractwith_in_)-97zx6.md>) — Asks the delegate whether the specified text view allows user interaction with the provided text attachment in the specified range of text. _(deprecated)_
- [- textView:shouldInteractWithURL:inRange:](<uitextviewdelegate/textview(__shouldinteractwith_in_)-98tho.md>) — Asks the delegate whether the specified text view allows user interaction with the specified URL in the specified range of text. _(deprecated)_
- [UITextItemInteraction](uitextiteminteraction.md) — Constants that indicate the type of interaction the user expects to have with a URL or text attachment. _(deprecated)_

### Instance Methods

- [- textView:didBeginFormattingWithViewController:](<uitextviewdelegate/textview(__didbeginformattingwith_).md>)
- [- textView:didEndFormattingWithViewController:](<uitextviewdelegate/textview(__didendformattingwith_).md>)
- [- textView:editMenuForTextInRanges:suggestedActions:](<uitextviewdelegate/textview(__editmenufortextinranges_suggestedactions_).md>)
- [- textView:shouldChangeTextInRanges:replacementText:](<uitextviewdelegate/textview(__shouldchangetextinranges_replacementtext_).md>)
- [- textView:willBeginFormattingWithViewController:](<uitextviewdelegate/textview(__willbeginformattingwith_).md>)
- [- textView:willEndFormattingWithViewController:](<uitextviewdelegate/textview(__willendformattingwith_).md>)

## See Also

### Text actions and menus

- [UITextItem](uitextitem.md) — An object for attaching custom actions and menus to links, text attachments, or other specific text in a text view.
- [MenuConfiguration](uitextitem/menuconfiguration.md) — An object that describes what type of menu and preview to show for a text item.
