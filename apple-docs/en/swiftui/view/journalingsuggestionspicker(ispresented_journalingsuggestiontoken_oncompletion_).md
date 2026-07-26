---
title: 'journalingSuggestionsPicker(isPresented:journalingSuggestionToken:onCompletion:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/journalingsuggestionspicker(ispresented:journalingsuggestiontoken:oncompletion:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/journalingsuggestionspicker(ispresented:journalingsuggestiontoken:oncompletion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/journalingsuggestionspicker%28ispresented%3Ajournalingsuggestiontoken%3Aoncompletion%3A%29.json'
content_hash: 'sha256:c349bfd8fff00e6c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# journalingSuggestionsPicker(isPresented:journalingSuggestionToken:onCompletion:)

<sub>Instance Method</sub>

Presents a visual picker interface that contains events and images that a person can select to retrieve more information.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor @preconcurrency func journalingSuggestionsPicker(isPresented: Binding<Bool>, journalingSuggestionToken: JournalingSuggestionPresentationToken?, onCompletion: @escaping (JournalingSuggestion) async -> Void) -> some View

```

## Parameters

- `isPresented` — A binding to a `Bool` value that determines whether to show the picker.

- `journalingSuggestionToken` — A `JournalingSuggestionPresentationToken` struct to determine the content shown in the picker.

- `onCompletion` — Code that you supply, which processes any suggestions that a person may choose in the picker.

## Discussion

For more information about the Journaling Suggestions picker, see: doc:presenting-the-suggestions-picker-and-processing-a-selection.

## See Also

### Presenting journaling suggestions

- [journalingSuggestionsPicker(isPresented:onCompletion:)](<journalingsuggestionspicker(ispresented_oncompletion_).md>) — Presents a visual picker interface that contains events and images that a person can select to retrieve more information.
