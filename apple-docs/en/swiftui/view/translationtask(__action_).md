---
title: 'translationTask(_:action:)'
framework: Translation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 26.0+, macOS 15.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/translationtask(_:action:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/translationtask(_:action:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/translationtask%28_%3Aaction%3A%29.json'
content_hash: 'sha256:9c4b7b42de02fe2a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# translationTask(_:action:)

<sub>Instance Method</sub>

Adds a task to perform before this view appears or when the translation configuration changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
nonisolated func translationTask(_ configuration: TranslationSession.Configuration?, action: @escaping (TranslationSession) async -> Void) -> some View

```

## Parameters

- `configuration` — A configuration for a [TranslationSession](../../translation/translationsession.md). When this configuration is non-`nil` and changes, the `action` runs providing an instance of the session to perform translations.

- `action` — This closure runs when the [TranslationSession.Configuration](../../translation/translationsession/configuration.md) is non-`nil` and changes. If the configuration is initially non-`nil`, it calls the action closure when the view appears and provides a session to perform one or more translations.

## Discussion

This task provides an instance of [TranslationSession](../../translation/translationsession.md) to use in translations. Whenever [TranslationSession.Configuration](../../translation/translationsession/configuration.md)  changes and isn’t `nil`, the closure `action` runs, providing a session instance to perform one or more translations.

For example, you can create a configuration in response to a button press to initiate the translation:

```swift
struct ContentView: View {
    @State private var sourceText = "Hallo, Welt!"
    var sourceLanguage: Locale.Language?
    var targetLanguage: Locale.Language?

    @State private var targetText: String?
    @State private var configuration: TranslationSession.Configuration?

    var body: some View {
        VStack {
            Text(targetText ?? sourceText)
            Button("Translate") {
                guard configuration == nil else {
                    configuration?.invalidate()
                    return
                }

                 configuration = TranslationSession.Configuration(
                    source: sourceLanguage,
                    target: targetLanguage)
            }
            .translationTask(configuration) { session in
                Task { @MainActor in
                    do {
                        let response = try await session.translate(sourceText)
                        targetText = response.targetText
                    } catch {
                        // Handle any errors.
                    }
                }
            }
        }
    }
}
```

The system throws a `fatalError` if you use a [TranslationSession](../../translation/translationsession.md) instance after the attached view disappears or if you use it after changing the configuration. This causes the `action` closure to provide a new session instance.

## See Also

### Showing a translation

- [translationPresentation(isPresented:text:attachmentAnchor:arrowEdge:replacementAction:)](<translationpresentation(ispresented_text_attachmentanchor_arrowedge_replacementaction_).md>) — Presents a translation popover when a given condition is true.
- [translationTask(source:target:action:)](<translationtask(source_target_action_).md>) — Adds a task to perform before this view appears or when the specified source or target languages change.
- [translationTask(source:target:preferredStrategy:action:)](<translationtask(source_target_preferredstrategy_action_).md>) — Adds a task to perform before this view appears or when the specified source or target languages change.
