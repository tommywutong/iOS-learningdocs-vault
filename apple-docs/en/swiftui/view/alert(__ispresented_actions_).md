---
title: 'alert(_:isPresented:actions:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/alert(_:ispresented:actions:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/alert(_:ispresented:actions:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/alert%28_%3Aispresented%3Aactions%3A%29.json'
content_hash: 'sha256:6c63b4c311ee74c3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# alert(_:isPresented:actions:)

<sub>Instance Method</sub>

Presents an alert when a given condition is true, using a localized string resource for the title.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated func alert<A>(_ titleResource: LocalizedStringResource, isPresented: Binding<Bool>, @ContentBuilder actions: () -> A) -> some View where A : View

```

## Parameters

- `titleResource` — Text resource for the localized string that describes the title of the alert.

- `isPresented` — A binding to a Boolean value that determines whether to present the alert. When the user presses or taps one of the alert’s actions, the system sets this value to `false` and dismisses.

- `actions` — A [ContentBuilder](../contentbuilder.md) returning the alert’s actions.

## Discussion

In the example below, a login form conditionally presents an alert by setting the `didFail` state variable. When the form sets the value to to `true`, the system displays an alert with an “OK” action.

```swift
struct Login: View {
    @State private var didFail = false

    var body: some View {
        LoginForm(didFail: $didFail)
            .alert(
                "Login failed.",
                isPresented: $didFail
            ) {
                Button("OK") {
                    // Handle the acknowledgement.
                }
            }
    }
}
```

All actions in an alert dismiss the alert after the action runs. The default button is shown with greater prominence. You can influence the default button by assigning it the [defaultAction](../keyboardshortcut/defaultaction.md) keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

If no actions are present, the system includes a standard “OK” action. No default cancel action is provided. If you want to show a cancel action, use a button with a role of [cancel](../buttonrole/cancel.md).

On iOS, tvOS, and watchOS, alerts only support controls with labels that are [Text](../text.md). Passing any other type of view results in the content being omitted.

This modifier creates a [Text](../text.md) view for the title on your behalf. See [Text](../text.md) for more information about localizing strings.

## See Also

### Presenting an alert

- [AlertScene](../alertscene.md) — A scene that renders itself as a standalone alert dialog.
- [alert(_:isPresented:presenting:actions:)](<alert(__ispresented_presenting_actions_).md>) — Presents an alert using the given data to produce the alert’s content and a localized string resource for a title.
- [alert(_:item:actions:)](<alert(__item_actions_).md>) — Presents an alert using the given data to produce the alert’s content and a text view as a title.
- [alert(error:actions:)](<alert(error_actions_).md>) — Presents an alert when an error is present.
- [alert(isPresented:error:actions:)](<alert(ispresented_error_actions_).md>) — Presents an alert when an error is present.
- [alert(_:isPresented:actions:message:)](<alert(__ispresented_actions_message_).md>) — Presents an alert with a message when a given condition is true, using a localized string resource for a title.
- [alert(_:isPresented:presenting:actions:message:)](<alert(__ispresented_presenting_actions_message_).md>) — Presents an alert with a message using the given data to produce the alert’s content and a localized string resource for a title.
- [alert(_:item:actions:message:)](<alert(__item_actions_message_).md>) — Presents an alert with a message using the given data to produce the alert’s content and a localized string key for a title.
- [alert(error:actions:message:)](<alert(error_actions_message_).md>) — Presents an alert with a message when an error is present.
- [alert(isPresented:error:actions:message:)](<alert(ispresented_error_actions_message_).md>) — Presents an alert with a message when an error is present.
