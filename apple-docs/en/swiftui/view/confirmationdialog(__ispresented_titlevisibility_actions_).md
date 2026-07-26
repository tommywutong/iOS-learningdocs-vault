---
title: 'confirmationDialog(_:isPresented:titleVisibility:actions:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/confirmationdialog(_:ispresented:titlevisibility:actions:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/confirmationdialog(_:ispresented:titlevisibility:actions:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/confirmationdialog%28_%3Aispresented%3Atitlevisibility%3Aactions%3A%29.json'
content_hash: 'sha256:84e121fd0b2c88c8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# confirmationDialog(_:isPresented:titleVisibility:actions:)

<sub>Instance Method</sub>

Presents a confirmation dialog when a given condition is true, using a localized string resource for the title.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated func confirmationDialog<A>(_ titleResource: LocalizedStringResource, isPresented: Binding<Bool>, titleVisibility: Visibility = .automatic, @ContentBuilder actions: () -> A) -> some View where A : View

```

## Parameters

- `titleResource` — Text resource for the localized string that describes the title of the dialog.

- `isPresented` — A binding to a Boolean value that determines whether to present the dialog. When the user presses or taps the dialog’s default action button, the system sets this value to `false`, dismissing the dialog.

- `titleVisibility` — The visibility of the dialog’s title. The default value is [Visibility.automatic](../visibility/automatic.md).

- `actions` — A [ContentBuilder](../contentbuilder.md) returning the dialog’s actions.

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
        }
    }
}
```

All actions in a confirmation dialog will dismiss the dialog after the action runs. The default button will be shown with greater prominence. You can influence the default button by assigning it the [defaultAction](../keyboardshortcut/defaultaction.md) keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

Dialogs include a standard dismiss action by default. If you provide a button with a role of [cancel](../buttonrole/cancel.md), that button takes the place of the default dismiss action. You don’t have to dismiss the presentation with the cancel button’s action.

> [!note] Note
> In regular size classes in iOS, the system renders confirmation dialogs as a popover that the user dismisses by tapping anywhere outside the popover, rather than displaying the standard dismiss action.

On iOS, tvOS, and watchOS, confirmation dialogs only support controls with labels that are [Text](../text.md). Passing any other type of view results in the content being omitted.

This modifier creates a [Text](../text.md) view for the title on your behalf. See [Text](../text.md) for more information about localizing strings.

## See Also

### Getting confirmation for an action

- [confirmationDialog(_:isPresented:titleVisibility:presenting:actions:)](<confirmationdialog(__ispresented_titlevisibility_presenting_actions_).md>) — Presents a confirmation dialog using data to produce the dialog’s content and a localized string resource for the title.
- [dismissalConfirmationDialog(_:shouldPresent:actions:)](<dismissalconfirmationdialog(__shouldpresent_actions_).md>) — Presents a confirmation dialog when a dismiss action has been triggered.
