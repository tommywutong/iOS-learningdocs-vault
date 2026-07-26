---
title: 'translationTask(source:target:action:)'
framework: Translation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 26.0+, macOS 15.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/translationtask(source:target:action:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/translationtask(source:target:action:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/translationtask%28source%3Atarget%3Aaction%3A%29.json'
content_hash: 'sha256:5068ebacb1150d10'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# translationTask(source:target:action:)

<sub>Instance Method</sub>

Adds a task to perform before this view appears or when the specified source or target languages change.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
nonisolated func translationTask(source: Locale.Language? = nil, target: Locale.Language? = nil, action: @escaping (TranslationSession) async -> Void) -> some View

```

## Parameters

- `source` — The language the source content is in. If this is `nil`, the session tries to identify the language and prompts the person to pick the source language if it’s unclear. All text translated within the session should be in the same source language. Changing this value cancels previous tasks and creates a new session to perform translations again.

- `target` — The language to translate content into. A `nil` value means the session picks a target according to the person’s `Locale.preferredLanguages` and the `source`. Changing this value cancels previous tasks and creates a new one to perform translations again.

- `action` — A closure that runs when the view first appears and when `source` or `target` change.  It provides a [TranslationSession](../../translation/translationsession.md) instance to perform one or multiple translations.

## Discussion

This task provides an instance of [TranslationSession](../../translation/translationsession.md)  to use to perform translations.

To perform new translations with the same `source` and `target` language, use [translationTask(_:action:)](<translationtask(__action_).md>) and call [invalidate()](<../../translation/translationsession/configuration/invalidate().md>).

For example, you can translate when content appears:

```swift
 struct ContentView: View {
     var sourceText = "Hallo, Welt!"
     var sourceLanguage: Locale.Language?
     var targetLanguage: Locale.Language?

     @State private var targetText: String?

     var body: some View {
         Text(targetText ?? sourceText)
             .translationTask(
                 source: sourceLanguage,
                 target: targetLanguage
             ) { session in
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
```

The system throws a `fatalError` if you use a [TranslationSession](../../translation/translationsession.md) instance after the attached view disappears or if you use it after changing the `source` or `target` parameters. This causes the `action` closure to provide a new instance.

## See Also

### Showing a translation

- [translationPresentation(isPresented:text:attachmentAnchor:arrowEdge:replacementAction:)](<translationpresentation(ispresented_text_attachmentanchor_arrowedge_replacementaction_).md>) — Presents a translation popover when a given condition is true.
- [translationTask(_:action:)](<translationtask(__action_).md>) — Adds a task to perform before this view appears or when the translation configuration changes.
- [translationTask(source:target:preferredStrategy:action:)](<translationtask(source_target_preferredstrategy_action_).md>) — Adds a task to perform before this view appears or when the specified source or target languages change.
