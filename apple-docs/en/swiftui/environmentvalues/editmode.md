---
title: editMode
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/editmode
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/editmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/editmode.json'
content_hash: 'sha256:4b817de15a289bbf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# editMode

<sub>Instance Property</sub>

An indication of whether the user can edit the contents of a view associated with this environment.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var editMode: Binding<EditMode>? { get set }
```

## Discussion

Read this environment value to receive a optional binding to the edit mode state. The binding contains an [EditMode](../editmode.md) value that indicates whether edit mode is active, and that you can use to change the mode. To learn how to read an environment value, see [EnvironmentValues](../environmentvalues.md).

Certain built-in views automatically alter their appearance and behavior in edit mode. For example, a [List](../list.md) with a [ForEach](../foreach.md) that’s configured with the [onDelete(perform:)](<../dynamicviewcontent/ondelete(perform_).md>) or [onMove(perform:)](<../dynamicviewcontent/onmove(perform_).md>) modifier provides controls to delete or move list items while in edit mode. On devices without an attached keyboard and mouse or trackpad, people can make multiple selections in lists only when edit mode is active.

You can also customize your own views to react to edit mode. The following example replaces a read-only [Text](../text.md) view with an editable [TextField](../textfield.md), checking for edit mode by testing the wrapped value’s [isEditing](../editmode/isediting.md) property:

```swift
@Environment(\.editMode) private var editMode
@State private var name = "Maria Ruiz"

var body: some View {
    Form {
        if editMode?.wrappedValue.isEditing == true {
            TextField("Name", text: $name)
        } else {
            Text(name)
        }
    }
    .animation(nil, value: editMode?.wrappedValue)
    .toolbar { // Assumes embedding this view in a NavigationView.
        EditButton()
    }
}
```

You can set the edit mode through the binding, or you can rely on an [EditButton](../editbutton.md) to do that for you, as the example above demonstrates. The button activates edit mode when the user taps the Edit button, and disables editing mode when the user taps Done.

## See Also

### Editing a list

- [moveDisabled(_:)](<../view/movedisabled(__).md>) — Adds a condition for whether the view’s view hierarchy is movable.
- [deleteDisabled(_:)](<../view/deletedisabled(__).md>) — Adds a condition for whether the view’s view hierarchy is deletable.
- [EditMode](../editmode.md) — A mode that indicates whether the user can edit a view’s content.
- [EditActions](../editactions.md) — A set of edit actions on a collection of data that a view can offer to a user.
- [EditableCollectionContent](../editablecollectioncontent.md) — An opaque wrapper view that adds editing capabilities to a row in a list.
- [IndexedIdentifierCollection](../indexedidentifiercollection.md) — A collection wrapper that iterates over the indices and identifiers of a collection together.
