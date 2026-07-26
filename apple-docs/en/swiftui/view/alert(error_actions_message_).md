---
title: 'alert(error:actions:message:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/alert(error:actions:message:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/alert(error:actions:message:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/alert%28error%3Aactions%3Amessage%3A%29.json'
content_hash: 'sha256:ed441bb256f36a1d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# alert(error:actions:message:)

<sub>Instance Method</sub>

Presents an alert with a message when an error is present.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated func alert<E, A, M>(error: Binding<E?>, @ContentBuilder actions: (E) -> A, @ContentBuilder message: (E) -> M) -> some View where E : LocalizedError, A : View, M : View

```

## Parameters

- `error` — A binding to an optional localized Error. The system presents the alert when the binding’s value is non-nil, and uses the error to generate the alert’s title. When the user presses or taps one of the alert’s actions, the system sets this value to `nil` and dismisses. The system passes the error to the modifier’s closures. You use this data to populate the fields of an alert that the system displays to the user. The error’s `errorDescription` will be used as the title.

- `actions` — A [ContentBuilder](../contentbuilder.md) returning the alert’s actions.

- `message` — A [ContentBuilder](../contentbuilder.md) returning the message for the alert given the current error.

## Discussion

In the example below, a form conditionally presents an alert depending upon the value of an error. When the error value isn’t `nil`, the system presents an alert with an “OK” action.

The title of the alert is inferred from the error’s `errorDescription`.

```swift
struct TicketPurchase: View {
    @State private var error: TicketPurchaseError? = nil

    var body: some View {
        TicketForm(error: $error)
            .alert(error: $error) { _ in
                Button("OK") {
                    // Handle acknowledgement.
                }
            } message: { error in
                Text(error.recoverySuggestion ?? "Try again later.")
            }
    }
}
```

All actions in an alert dismiss the alert after the action runs. The default button is shown with greater prominence. You can influence the default button by assigning it the [defaultAction](../keyboardshortcut/defaultaction.md) keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

If no actions are present, the system includes a standard “OK” action. No default cancel action is provided. If you want to show a cancel action, use a button with a role of [cancel](../buttonrole/cancel.md).

On iOS, tvOS, and watchOS, alerts only support controls with labels that are [Text](../text.md). Passing any other type of view results in the content being omitted.

This modifier creates a [Text](../text.md) view for the title on your behalf, and treats the localized key similar to [init(_:tableName:bundle:comment:)](<../text/init(__tablename_bundle_comment_).md>). See [Text](../text.md) for more information about localizing strings.

## See Also

### Presenting an alert

- [AlertScene](../alertscene.md) — A scene that renders itself as a standalone alert dialog.
- [alert(_:isPresented:actions:)](<alert(__ispresented_actions_).md>) — Presents an alert when a given condition is true, using a localized string resource for the title.
- [alert(_:isPresented:presenting:actions:)](<alert(__ispresented_presenting_actions_).md>) — Presents an alert using the given data to produce the alert’s content and a localized string resource for a title.
- [alert(_:item:actions:)](<alert(__item_actions_).md>) — Presents an alert using the given data to produce the alert’s content and a text view as a title.
- [alert(error:actions:)](<alert(error_actions_).md>) — Presents an alert when an error is present.
- [alert(isPresented:error:actions:)](<alert(ispresented_error_actions_).md>) — Presents an alert when an error is present.
- [alert(_:isPresented:actions:message:)](<alert(__ispresented_actions_message_).md>) — Presents an alert with a message when a given condition is true, using a localized string resource for a title.
- [alert(_:isPresented:presenting:actions:message:)](<alert(__ispresented_presenting_actions_message_).md>) — Presents an alert with a message using the given data to produce the alert’s content and a localized string resource for a title.
- [alert(_:item:actions:message:)](<alert(__item_actions_message_).md>) — Presents an alert with a message using the given data to produce the alert’s content and a localized string key for a title.
- [alert(isPresented:error:actions:message:)](<alert(ispresented_error_actions_message_).md>) — Presents an alert with a message when an error is present.
