---
title: 'confirmationDialog(_:item:titleVisibility:actions:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/confirmationdialog(_:item:titlevisibility:actions:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/confirmationdialog(_:item:titlevisibility:actions:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/confirmationdialog%28_%3Aitem%3Atitlevisibility%3Aactions%3A%29.json'
content_hash: 'sha256:f979b217eb844f32'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# confirmationDialog(_:item:titleVisibility:actions:)

<sub>Instance Method</sub>

Presents a confirmation dialog using data to produce the dialog’s content and a text view for the title.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated func confirmationDialog<A, T>(_ title: Text, item data: Binding<T?>, titleVisibility: Visibility = .automatic, @ContentBuilder actions: (T) -> A) -> some View where A : View

```

## Parameters

- `title` — The title of the dialog.

- `data` — A binding to optional source of truth for the confirmation dialog. The system presents the dialog when the binding’s value is non-nil. When the user presses or taps the dialog’s default action button, the system sets this value to `nil` and dismisses. The system passes the contents to the modifier’s closures. You use this data to populate the fields of a confirmation dialog that you create that the system displays to the user.

- `titleVisibility` — The visibility of the dialog’s title. The default value is [Visibility.automatic](../visibility/automatic.md).

- `actions` — A [ContentBuilder](../contentbuilder.md) returning the dialog’s actions given the currently available data.

## See Also

### Confirmation dialogs

- [confirmationDialog(_:isPresented:titleVisibility:actions:)](<confirmationdialog(__ispresented_titlevisibility_actions_).md>) — Presents a confirmation dialog when a given condition is true, using a localized string resource for the title.
- [confirmationDialog(_:isPresented:titleVisibility:presenting:actions:)](<confirmationdialog(__ispresented_titlevisibility_presenting_actions_).md>) — Presents a confirmation dialog using data to produce the dialog’s content and a localized string resource for the title.
- [dismissalConfirmationDialog(_:shouldPresent:actions:)](<dismissalconfirmationdialog(__shouldpresent_actions_).md>) — Presents a confirmation dialog when a dismiss action has been triggered.
