---
title: UIPhotoSearchSuggestion
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/uikit/uiphotosearchsuggestion
source_url: 'https://developer.apple.com/documentation/uikit/uiphotosearchsuggestion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiphotosearchsuggestion.json'
content_hash: 'sha256:c3392bad3c58c625'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIPhotoSearchSuggestion

<sub>Class</sub>

An input suggestion that carries photo search metadata for people, subjects, locations, and time periods.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
class UIPhotoSearchSuggestion
```

## Discussion

When someone types text that could match a photo library search, such as “photos from Paris last summer,” the system recognizes the input as a photo library search and delivers a `UIPhotoSearchSuggestion` through the [- textField:insertInputSuggestion:](<uitextfielddelegate/textfield(__insertinputsuggestion_).md>) or [- textView:insertInputSuggestion:](<uitextviewdelegate/textview(__insertinputsuggestion_).md>) delegate method. Use `as? UIPhotoSearchSuggestion` to check whether the incoming [UIInputSuggestion](uiinputsuggestion.md) is a photo search suggestion and access its metadata.

After receiving a suggestion, you have two options: Pass the object directly to the [Photos](../photos.md) framework to present a pre-populated photo picker, or read the `whoValues`, `whatValues`, `whereValues`, and `whenValues` arrays to build a custom search experience.

You can’t create a `UIPhotoSearchSuggestion` directly. The system creates and delivers instances through the input suggestion system.

### Presenting a photo picker

Pass the suggestion to `PHPickerSearchText(photoSearchSuggestion:)` to pre-populate a `PHPickerViewController` with photos matching the person’s search.

```swift
class SearchViewController: UIViewController, UITextFieldDelegate, PHPickerViewControllerDelegate {
    @IBOutlet var searchField: UITextField!

    func textField(_ textField: UITextField,
                   insertInputSuggestion inputSuggestion: UIInputSuggestion) {
        if let photoSuggestion = inputSuggestion as? UIPhotoSearchSuggestion {
            presentPhotosPicker(with: photoSuggestion)
        }
    }

    func presentPhotosPicker(with suggestion: UIPhotoSearchSuggestion) {
        var configuration = PHPickerConfiguration()
        configuration.searchText = PHPickerSearchText(photoSearchSuggestion: suggestion)
        let picker = PHPickerViewController(configuration: configuration)
        picker.delegate = self
        present(picker, animated: true)
    }

    func picker(_ picker: PHPickerViewController,
                didFinishPicking results: [PHPickerResult]) {
        dismiss(animated: true)
        // Handle selected photos.
    }
}
```

### Building a custom search

If your app has its own photo search UI, read the filter arrays and construct your own query.

```swift
func textField(_ textField: UITextField,
               insertInputSuggestion inputSuggestion: UIInputSuggestion) {
    guard let suggestion = inputSuggestion as? UIPhotoSearchSuggestion else { return }

    // Build a custom query from the individual filter values.
    let who = suggestion.whoValues        // e.g., ["John"]
    let what = suggestion.whatValues      // e.g., ["hiking"]
    let locations = suggestion.whereValues // e.g., ["Paris"]
    let timeframes = suggestion.whenValues // e.g., ["last summer"]

    performCustomPhotoSearch(people: who, subjects: what, locations: locations, timeframes: timeframes)
}
```

## Relationships

- **Inherits From**: [UIInputSuggestion](uiinputsuggestion.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Instance Properties

- [whatValues](uiphotosearchsuggestion/whatvalues.md) — Subjects or topics mentioned in the text that can be used to filter photos. _(beta)_
- [whenValues](uiphotosearchsuggestion/whenvalues.md) — Time periods mentioned in the text that can be used to filter photos. _(beta)_
- [whereValues](uiphotosearchsuggestion/wherevalues.md) — Locations mentioned in the text that can be used to filter photos. _(beta)_
- [whoValues](uiphotosearchsuggestion/whovalues.md) — People mentioned in the text that can be used to filter photos. _(beta)_

## See Also

### Smart Reply for messaging

- [Adopting Smart Reply in your messaging or email app](adopting-smart-reply-in-your-messaging-or-email-app.md) — Generate reply suggestions by using Apple Intelligence and put selected text into your text UI.
- [UIConversationContext](uiconversationcontext.md) — A base class that represents a conversation between participants, such as in an email or messaging app.
- [Entry](uiconversationcontext/entry.md) — A base class that represents a message in a conversation.
- [UIMailConversationContext](uimailconversationcontext.md) — A class that represents an email conversation.
- [MailEntry](uimailconversationcontext/mailentry.md) — A class that represents a specific email in an email thread.
- [UIMessageConversationContext](uimessageconversationcontext.md) — A class that represents a message conversation.
- [MessageEntry](uimessageconversationcontext/messageentry.md) — A class that represents a message in a message conversation.
- [UIInputSuggestion](uiinputsuggestion.md) — A base class you use to handle suggestions from the keyboard or system.
- [UISmartReplySuggestion](uismartreplysuggestion.md) — A class you use to handle a Smart Reply suggestion.
