---
title: 'dismissalConfirmationDialog(_:shouldPresent:actions:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 15.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/dismissalconfirmationdialog(_:shouldpresent:actions:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/dismissalconfirmationdialog(_:shouldpresent:actions:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/dismissalconfirmationdialog%28_%3Ashouldpresent%3Aactions%3A%29.json'
content_hash: 'sha256:ed4e0f714387a1bd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# dismissalConfirmationDialog(_:shouldPresent:actions:)

<sub>Instance Method</sub>

Presents a confirmation dialog when a dismiss action has been triggered.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
@export(implementation) nonisolated func dismissalConfirmationDialog<A>(_ titleResource: LocalizedStringResource, shouldPresent: Bool, @ContentBuilder actions: () -> A) -> some View where A : View

```

## Parameters

- `titleResource` — Text resource for the localized string that describes the title of the dialog.

- `shouldPresent` — A Boolean value that determines whether to present the dialog upon dismissal.

- `actions` — A content builder returning the dialog’s actions.

## Discussion

On macOS, the dialog will be presented when attempting to dismiss the window for this view.

For example, you could present a dialog asking to persist unsaved changes:

```swift
struct ComposeMessage: View {
    @State private var message = Message()

    var body: some View {
        MessageEditor(message: $message)
            .dismissalConfirmationDialog(
                "Save This Message As Draft?",
                shouldPresent: message.hasUnsavedChanges
            ) {
                Button("Save") {
                    message.save()
                }
                Button("Don't Save", role: .destructive) {
                    message.discard()
                }
            } message: {
                Text(
                    """
                    This message has not been sent and contains\
                    unsaved changes.
                    """)
            }
}
```

All actions in the dialog will dismiss the dialog after the action runs. The default button will be shown with greater prominence. You can influence the default button by assigning it the [defaultAction](../keyboardshortcut/defaultaction.md) keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

Dismissal dialogs include a standard cancellation action by default. If you provide a button with a role of [cancel](../buttonrole/cancel.md), that button takes the place of the default cancellation action.

The cancellation action will always prevent the dismissal, while other actions will allow the dismiss to proceed.

On iOS, in addition to the standard cancellation action, the dismissal dialog also includes a standard close action by default. If you provide a button with a role of [destructive](../buttonrole/destructive.md), that button takes the place of the default close action. This action will immediately dismiss the dialog and the view’s associated window.

## See Also

### Getting confirmation for an action

- [confirmationDialog(_:isPresented:titleVisibility:actions:)](<confirmationdialog(__ispresented_titlevisibility_actions_).md>) — Presents a confirmation dialog when a given condition is true, using a localized string resource for the title.
- [confirmationDialog(_:isPresented:titleVisibility:presenting:actions:)](<confirmationdialog(__ispresented_titlevisibility_presenting_actions_).md>) — Presents a confirmation dialog using data to produce the dialog’s content and a localized string resource for the title.
