---
title: UITextInputTraits
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextinputtraits
source_url: 'https://developer.apple.com/documentation/uikit/uitextinputtraits'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinputtraits.json'
content_hash: 'sha256:a0075cb933e1b318'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITextInputTraits

<sub>Protocol</sub>

A set of methods that defines features for keyboard input to a text object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UITextInputTraits : NSObjectProtocol
```

## Overview

For a custom text object to support keyboard input, it must adopt this protocol to interact properly with the text-input management system. The [UITextField](uitextfield.md) and [UITextView](uitextview.md) classes automatically support this protocol.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Inherited By**: [UIKeyInput](uikeyinput.md), [UITextDocumentProxy](uitextdocumentproxy.md), [UITextDraggable](uitextdraggable.md), [UITextDroppable](uitextdroppable.md), [UITextInput](uitextinput.md)

- **Conforming Types**: [UISearchBar](uisearchbar.md), [UISearchTextField](uisearchtextfield.md), [UITextField](uitextfield.md), [UITextView](uitextview.md)

## Topics

### Configuring the keyboard appearance

- [keyboardType](uitextinputtraits/keyboardtype.md) — The keyboard type for the text object.
- [UIKeyboardType](uikeyboardtype.md) — Constants that specify the type of keyboard to display for a text-based view.
- [keyboardAppearance](uitextinputtraits/keyboardappearance.md) — The appearance style of the keyboard for the text object.
- [UIKeyboardAppearance](uikeyboardappearance.md) — Constants that specify the appearance of the keyboard for a text-based view.
- [returnKeyType](uitextinputtraits/returnkeytype.md) — The visible indication of what the Return key does.
- [UIReturnKeyType](uireturnkeytype.md) — Constants that specify the type of Return key the keyboard displays.
- [textContentType](uitextinputtraits/textcontenttype.md) — The semantic meaning for a text input area.
- [UITextContentType](uitextcontenttype.md) — Constants that identify the semantic meaning for a text-entry area.

### Managing the keyboard behavior

- [secureTextEntry](uitextinputtraits/issecuretextentry.md) — A Boolean value that indicates whether a text object disables copying, and in some cases, prevents recording/broadcasting and also hides the text.
- [enablesReturnKeyAutomatically](uitextinputtraits/enablesreturnkeyautomatically.md) — A Boolean value that indicates whether the system automatically enables the Return key when the user enters text.

### Managing spelling and autocorrection

- [autocapitalizationType](uitextinputtraits/autocapitalizationtype.md) — The autocapitalization style for the text object.
- [UITextAutocapitalizationType](uitextautocapitalizationtype.md) — The autocapitalization behavior of a text-based view.
- [autocorrectionType](uitextinputtraits/autocorrectiontype.md) — The autocorrection style for the text object.
- [UITextAutocorrectionType](uitextautocorrectiontype.md) — The autocorrection behavior of a text-based view.
- [spellCheckingType](uitextinputtraits/spellcheckingtype.md) — The spell-checking style for the text object.
- [UITextSpellCheckingType](uitextspellcheckingtype.md) — The spell-checking behavior of a text-based view.
- [inlinePredictionType](uitextinputtraits/inlinepredictiontype.md) — The behavior of inline text predictions for a text-entry area.
- [UITextInlinePredictionType](uitextinlinepredictiontype.md) — Constants that identify the behavior of inline text predictions for a text-entry area.

### Configuring the autoformatting behaviors

- [smartQuotesType](uitextinputtraits/smartquotestype.md) — The configuration state for smart quotes.
- [UITextSmartQuotesType](uitextsmartquotestype.md) — Constants that indicate whether to enable or disable smart quotes.
- [smartDashesType](uitextinputtraits/smartdashestype.md) — The configuration state for smart dashes.
- [UITextSmartDashesType](uitextsmartdashestype.md) — Constants that specify the automatic conversion behavior between hyphens and en or em dashes.
- [smartInsertDeleteType](uitextinputtraits/smartinsertdeletetype.md) — The configuration state for the smart insertion and deletion of space characters.
- [UITextSmartInsertDeleteType](uitextsmartinsertdeletetype.md) — Constants that specify whether to automatically insert extra spaces after a paste operation or to delete them after a cut or delete operation.

### Configuring the writing tools experience

- [writingToolsBehavior](uitextinputtraits/writingtoolsbehavior.md) — The writing tools experience to support in the current view.
- [UIWritingToolsBehavior](uiwritingtoolsbehavior.md) — Constants that specify the writing tools experience for the underlying view.

### Configuring Smart Replies

- [conversationContext](uitextinputtraits/conversationcontext.md) — A reference to a conversation, such as a mail or messaging thread.

### Configuring Password AutoFill

- [Password AutoFill](../security/password-autofill.md) — Streamline your app’s login and onboarding procedures.
- [UITextInputPasswordRules](uitextinputpasswordrules.md) — A class that represents password rules for a text input field.

### Configuring math expression completion

- [mathExpressionCompletionType](uitextinputtraits/mathexpressioncompletiontype.md)
- [UITextMathExpressionCompletionType](uitextmathexpressioncompletiontype.md)

### Instance Properties

- [allowedWritingToolsResultOptions](uitextinputtraits/allowedwritingtoolsresultoptions.md)
- [allowsNumberPadPopover](uitextinputtraits/allowsnumberpadpopover.md)
- [grammarCheckingType](uitextinputtraits/grammarcheckingtype.md) _(beta)_
- [passwordRules](uitextinputtraits/passwordrules.md)

## See Also

### Text input

- [UITextInput](uitextinput.md) — A set of methods for interacting with the text input system and enabling features in documents.
- [UITextInputDelegate](uitextinputdelegate.md) — An intermediary between a document and the text input system.
- [UIKeyInput](uikeyinput.md) — A set of methods a responder uses to implement simple text entry.
- [UITextInputContext](uitextinputcontext.md) — An object that reports the type of input your app receives.
- [UITextInputMode](uitextinputmode.md) — The current text input mode.
- [UITextInputAssistantItem](uitextinputassistantitem.md) — An object that manages custom bar button items that you add to the shortcuts bar above the keyboard on iPad.
- [UIDictationPhrase](uidictationphrase.md) — An object that represents the textual interpretation of a spoken phrase that the user dictates.
