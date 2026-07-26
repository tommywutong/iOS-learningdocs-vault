---
title: 'confirmationDialog(_:isPresented:titleVisibility:actions:message:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/confirmationdialog(_:ispresented:titlevisibility:actions:message:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/confirmationdialog(_:ispresented:titlevisibility:actions:message:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/confirmationdialog%28_%3Aispresented%3Atitlevisibility%3Aactions%3Amessage%3A%29.json'
content_hash: 'sha256:a8de04a92e5723eb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# confirmationDialog(_:isPresented:titleVisibility:actions:message:)

<sub>Instance Method</sub>

Presents a confirmation dialog with a message when a given condition is true, using a localized string resource for the title.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated func confirmationDialog<A, M>(_ titleResource: LocalizedStringResource, isPresented: Binding<Bool>, titleVisibility: Visibility = .automatic, @ContentBuilder actions: () -> A, @ContentBuilder message: () -> M) -> some View where A : View, M : View

```

## Parameters

- `titleResource` — Text resource for the localized string that describes the title of the dialog.

- `isPresented` — A binding to a Boolean value that determines whether to present the dialog. When the user presses or taps the dialog’s default action button, the system sets this value to `false`, dismissing the dialog.

- `titleVisibility` — The visibility of the dialog’s title. The default value is [Visibility.automatic](../visibility/automatic.md).

- `actions` — A [ContentBuilder](../contentbuilder.md) returning the dialog’s actions.

- `message` — A [ContentBuilder](../contentbuilder.md) returning the message for the dialog.

## Discussion

In the example below, a button conditionally presents a confirmation dialog depending upon the value of a bound Boolean variable. When the Boolean value is set to `true`, the system displays a confirmation dialog with a cancel action and a destructive action.

```swift
struct ConfirmEraseItems: View {
    @State private var isShowingDialog = false
    var body: some View {
        Button("Empty Trash") {
            isShowingDialog = true
        }
        .confirmationDialog(
            "Permanently erase the items in the Trash?",
            isPresented: $isShowingDialog
        ) {
            Button("Empty Trash", role: .destructive) {
                // Handle empty trash action.
            }
        } message: {
            Text("You cannot undo this action.")
        }
    }
}
```

All actions in a confirmation dialog will dismiss the dialog after the action runs. The default button will be shown with greater prominence. You can influence the default button by assigning it the [defaultAction](../keyboardshortcut/defaultaction.md) keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

Dialogs include a standard dismiss action by default. If you provide a button with a role of [cancel](../buttonrole/cancel.md), that button takes the place of the default dismiss action. You don’t have to dismiss the presentation with the cancel button’s action.

> [!note] Note
> In regular size classes in iOS, the system renders confirmation dialogs as a popover that the user dismisses by tapping anywhere outside the popover, rather than displaying the standard dismiss action.

On iOS, tvOS, and watchOS, confirmation dialogs only support controls with labels that are `Text`. Passing any other type of view results in the content being omitted.

This modifier creates a [Text](../text.md) view for the title on your behalf. See [Text](../text.md) for more information about localizing strings.

## See Also

### Showing a confirmation dialog with a message

- [confirmationDialog(_:isPresented:titleVisibility:presenting:actions:message:)](<confirmationdialog(__ispresented_titlevisibility_presenting_actions_message_).md>) — Presents a confirmation dialog with a message using data to produce the dialog’s content and a localized string resource for the title.
- [dismissalConfirmationDialog(_:shouldPresent:actions:message:)](<dismissalconfirmationdialog(__shouldpresent_actions_message_).md>) — Presents a confirmation dialog when a dismiss action has been triggered.
