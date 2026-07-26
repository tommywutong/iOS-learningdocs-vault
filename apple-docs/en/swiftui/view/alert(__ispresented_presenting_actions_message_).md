---
title: 'alert(_:isPresented:presenting:actions:message:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/alert(_:ispresented:presenting:actions:message:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/alert(_:ispresented:presenting:actions:message:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/alert%28_%3Aispresented%3Apresenting%3Aactions%3Amessage%3A%29.json'
content_hash: 'sha256:eda176e8d6be9717'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# alert(_:isPresented:presenting:actions:message:)

<sub>Instance Method</sub>

Presents an alert with a message using the given data to produce the alert’s content and a localized string resource for a title.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated func alert<A, M, T>(_ titleResource: LocalizedStringResource, isPresented: Binding<Bool>, presenting data: T?, @ContentBuilder actions: (T) -> A, @ContentBuilder message: (T) -> M) -> some View where A : View, M : View

```

## Parameters

- `titleResource` — Text resource for the localized string that describes the title.

- `isPresented` — A binding to a Boolean value that determines whether to present the alert. When the user presses or taps one of the alert’s actions, the system sets this value to `false` and dismisses.

- `data` — An optional source of truth for the alert. The system passes the contents to the modifier’s closures. You use this data to populate the fields of an alert that you create that the system displays to the user.

- `actions` — A [ContentBuilder](../contentbuilder.md) returning the alert’s actions given the currently available data.

- `message` — A [ContentBuilder](../contentbuilder.md) returning the message for the alert given the currently available data.

## Discussion

For the alert to appear, both `isPresented` must be `true` and `data` must not be `nil`. The data should not change after the presentation occurs. Any changes that you make after the presentation occurs are ignored.

Use this method when you need to populate the fields of an alert with content from a data source. The example below shows a custom data source, `SaveDetails`, that provides data to populate the alert:

```swift
struct SaveDetails: Identifiable {
    let name: String
    let error: String
    let id = UUID()
}

struct SaveButton: View {
    @State private var didError = false
    @State private var details: SaveDetails?

    var body: some View {
        Button("Save") {
            details = model.save(didError: $didError)
        }
        .alert(
            "Save failed.",
            isPresented: $didError,
            presenting: details
        ) { details in
            Button(role: .destructive) {
                // Handle the deletion.
            } label: {
                Text("Delete \(details.name)")
            }
            Button("Retry") {
                // Handle the retry action.
            }
        } message: { details in
            Text(details.error)
        }
    }
}
```

This modifier creates a [Text](../text.md) view for the title on your behalf. See [Text](../text.md) for more information about localizing strings.

All actions in an alert dismiss the alert after the action runs. The default button is shown with greater prominence. You can influence the default button by assigning it the [defaultAction](../keyboardshortcut/defaultaction.md) keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

If no actions are present, the system includes a standard “OK” action. No default cancel action is provided. If you want to show a cancel action, use a button with a role of [cancel](../buttonrole/cancel.md).

On iOS, tvOS, and watchOS, alerts only support controls with labels that are [Text](../text.md). Passing any other type of view results in the content being omitted.

Only unstyled text is supported for the message.

## See Also

### Presenting an alert

- [AlertScene](../alertscene.md) — A scene that renders itself as a standalone alert dialog.
- [alert(_:isPresented:actions:)](<alert(__ispresented_actions_).md>) — Presents an alert when a given condition is true, using a localized string resource for the title.
- [alert(_:isPresented:presenting:actions:)](<alert(__ispresented_presenting_actions_).md>) — Presents an alert using the given data to produce the alert’s content and a localized string resource for a title.
- [alert(_:item:actions:)](<alert(__item_actions_).md>) — Presents an alert using the given data to produce the alert’s content and a text view as a title.
- [alert(error:actions:)](<alert(error_actions_).md>) — Presents an alert when an error is present.
- [alert(isPresented:error:actions:)](<alert(ispresented_error_actions_).md>) — Presents an alert when an error is present.
- [alert(_:isPresented:actions:message:)](<alert(__ispresented_actions_message_).md>) — Presents an alert with a message when a given condition is true, using a localized string resource for a title.
- [alert(_:item:actions:message:)](<alert(__item_actions_message_).md>) — Presents an alert with a message using the given data to produce the alert’s content and a localized string key for a title.
- [alert(error:actions:message:)](<alert(error_actions_message_).md>) — Presents an alert with a message when an error is present.
- [alert(isPresented:error:actions:message:)](<alert(ispresented_error_actions_message_).md>) — Presents an alert with a message when an error is present.
