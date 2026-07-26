---
title: 'confirmationDialog(_:isPresented:titleVisibility:presenting:actions:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/confirmationdialog(_:ispresented:titlevisibility:presenting:actions:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/confirmationdialog(_:ispresented:titlevisibility:presenting:actions:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/confirmationdialog%28_%3Aispresented%3Atitlevisibility%3Apresenting%3Aactions%3A%29.json'
content_hash: 'sha256:e76965215127c956'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# confirmationDialog(_:isPresented:titleVisibility:presenting:actions:)

<sub>Instance Method</sub>

Presents a confirmation dialog using data to produce the dialog’s content and a localized string resource for the title.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated func confirmationDialog<A, T>(_ titleResource: LocalizedStringResource, isPresented: Binding<Bool>, titleVisibility: Visibility = .automatic, presenting data: T?, @ContentBuilder actions: (T) -> A) -> some View where A : View

```

## Parameters

- `titleResource` — Text resource for the localized string that describes the title of the dialog.

- `isPresented` — A binding to a Boolean value that determines whether to present the dialog. When the user presses or taps the dialog’s default action button, the system sets this value to `false`, dismissing the dialog.

- `titleVisibility` — The visibility of the dialog’s title. The default value is [Visibility.automatic](../visibility/automatic.md).

- `data` — An optional source of truth for the confirmation dialog. The system passes the contents to the modifier’s closures. You use this data to populate the fields of a confirmation dialog that you create that the system displays to the user.

- `actions` — A [ContentBuilder](../contentbuilder.md) returning the dialog’s actions given the currently available data.

## Discussion

In order for the interface to appear, both `isPresented` must be `true` and `data` must not be `nil`. `data` should not change after the presentation occurs. Any changes which occur after the presentation occurs will be ignored.

Use this method when you need to populate the fields of a confirmation dialog with content from a data source. The example below shows a custom data source, `FileDetails`, that provides data to populate the dialog:

```swift
struct FileDetails: Identifiable {
    var id: String { name }
    let name: String
    let fileType: UTType
}
struct ConfirmFileImport: View {
    @State private var isConfirming = false
    @State private var dialogDetail: FileDetails?
    var body: some View {
        Button("Import File") {
            dialogDetail = FileDetails(
                name: "MyImageFile.png", fileType: .png)
            isConfirming = true
        }
        .confirmationDialog(
            "Are you sure you want to import this file?",
            isPresented: $isConfirming, presenting: dialogDetail
        ) { detail in
            Button {
                // Handle import action.
            } label: {
                Text("""
                Import \(detail.name)
                File Type: \(detail.fileType.description)
                """)
            }
            Button("Cancel", role: .cancel) {
                dialogDetail = nil
            }
        }
    }
}
```

This modifier creates a [Text](../text.md) view for the title on your behalf. See [Text](../text.md) for more information about localizing strings.

All actions in a confirmation dialog will dismiss the dialog after the action runs. The default button will be shown with greater prominence. You can influence the default button by assigning it the [defaultAction](../keyboardshortcut/defaultaction.md) keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

Dialogs include a standard dismiss action by default. If you provide a button with a role of [cancel](../buttonrole/cancel.md), that button takes the place of the default dismiss action. You don’t have to dismiss the presentation with the cancel button’s action.

> [!note] Note
> In regular size classes in iOS, the system renders confirmation dialogs as a popover that the user dismisses by tapping anywhere outside the popover, rather than displaying the standard dismiss action.

On iOS, tvOS, and watchOS, confirmation dialogs only support controls with labels that are `Text`. Passing any other type of view results in the content being omitted.

## See Also

### Getting confirmation for an action

- [confirmationDialog(_:isPresented:titleVisibility:actions:)](<confirmationdialog(__ispresented_titlevisibility_actions_).md>) — Presents a confirmation dialog when a given condition is true, using a localized string resource for the title.
- [dismissalConfirmationDialog(_:shouldPresent:actions:)](<dismissalconfirmationdialog(__shouldpresent_actions_).md>) — Presents a confirmation dialog when a dismiss action has been triggered.
