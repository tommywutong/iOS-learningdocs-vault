---
title: 'translationPresentation(isPresented:text:attachmentAnchor:arrowEdge:replacementAction:)'
framework: Translation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.4+, iPadOS 17.4+, macOS 14.4+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/translationpresentation(ispresented:text:attachmentanchor:arrowedge:replacementaction:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/translationpresentation(ispresented:text:attachmentanchor:arrowedge:replacementaction:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/translationpresentation%28ispresented%3Atext%3Aattachmentanchor%3Aarrowedge%3Areplacementaction%3A%29.json'
content_hash: 'sha256:e0caa8fef4283755'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# translationPresentation(isPresented:text:attachmentAnchor:arrowEdge:replacementAction:)

<sub>Instance Method</sub>

Presents a translation popover when a given condition is true.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
nonisolated func translationPresentation(isPresented: Binding<Bool>, text: String, attachmentAnchor: PopoverAttachmentAnchor = .rect(.bounds), arrowEdge: Edge = .top, replacementAction: ((String) -> Void)? = nil) -> some View

```

## Parameters

- `isPresented` — A binding to a Boolean value that determines whether to present the popover.

- `text` — The text to be translated. Changing this after the popover presents has no effect.

- `attachmentAnchor` — The positioning anchor that defines the attachment point of the popover. The default is [bounds](../anchor/source/bounds.md).

- `arrowEdge` — The edge of the `attachmentAnchor` that defines the location of the popover’s arrow in macOS. The default is [Edge.top](../edge/top.md). iOS ignores this parameter.

- `replacementAction` — An optional action to perform when someone interacts with the “Replace with Translation” button. The “Replace with Translation” button appears when you provide this action.

## Discussion

Use this method to show a system UI translation popover when the `translationVisible` Boolean variable is `true`. Attach this view modifier to the containing view holding the text to translate. Then set the `isPresented` Boolean binding to `true` when you want the popover to display. When you do, a system UI translation popover appears offering a translation.

In the example below, the popover appears when the user toggles the `translationVisible` state variable by pressing the Translate button.

```swift
struct ContentView: View {
    @State private var translationVisible = false
    private var originalText = "Hallo, Welt!"

    var body: some View {
        VStack {
            Text(verbatim: originalText)
                .translationPresentation(isPresented: $translationVisible, text: originalText)
            Button("Translate") {
                translationVisible.toggle()
            }
        }
    }
}
```

To replace the original text with the translation, pass in a trailing closure to the `replacementAction` parameter. When you do, a Replace with Translation button appears in the system UI. When the user taps this button, the closure returns a translation of the text as a string. Use that string to update the original text with the translated text as shown below:

```swift
struct ReplaceTranslation: View {
    @State private var translationVisible = false
    @State private var originalText = "Hallo, Welt!"

    var body: some View {
        VStack(spacing: 20) {
            TextField("Text to translate", text: $originalText, axis: .vertical)
                .textFieldStyle(.roundedBorder)
                .translationPresentation(isPresented: $translationVisible, text: originalText) { translatedString in
                    // Update the original text with the translated result.
                    originalText = translatedString
                }
            Button("Translate") {
                translationVisible.toggle()
            }
        }
        .padding()
    }
}
```

If the system can’t detect the source language, it asks the user to select the language to translate from. For a list of supported languages see `LanguageAvailability.supportedLanguages`.

While this function does support long strings of text, it works best with short ones (no more than a couple of sentences or phrases in length).

## See Also

### Showing a translation

- [translationTask(_:action:)](<translationtask(__action_).md>) — Adds a task to perform before this view appears or when the translation configuration changes.
- [translationTask(source:target:action:)](<translationtask(source_target_action_).md>) — Adds a task to perform before this view appears or when the specified source or target languages change.
- [translationTask(source:target:preferredStrategy:action:)](<translationtask(source_target_preferredstrategy_action_).md>) — Adds a task to perform before this view appears or when the specified source or target languages change.
