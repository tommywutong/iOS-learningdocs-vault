---
title: FocusedValues
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/focusedvalues
source_url: 'https://developer.apple.com/documentation/swiftui/focusedvalues'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/focusedvalues.json'
content_hash: 'sha256:c946cac9ad3b8200'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# FocusedValues

<sub>Structure</sub>

A collection of state exported by the focused scene or view and its ancestors.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct FocusedValues
```

## Creating Custom Focused Values

Use the `Entry` macro to create custom focused values by extending `FocusedValues` with new properties:

```swift
extension FocusedValues {
    @Entry var focusedDocument: Binding<MyDocument>?
}
```

The `Entry` macro automatically generates the underlying key type and provides the getter and setter for the focused value. Since the default value for focused values is always `nil`, all focused values must be optional.

### Publishing Values in Your Views

Views publish focused values using the [focusedValue(_:_:)](<view/focusedvalue(____).md>) modifier:

```swift
struct DocumentCellView: View {
    @Binding var document: MyDocument

    var body: some View {
        Text("Document Content")
            .focusedValue(\.focusedDocument, $document)
    }
}
```

For scene-wide values that should be available depending on the focused scene, use [focusedSceneValue(_:_:)](<view/focusedscenevalue(____).md>):

```swift
struct DocumentViewer: View {
    @Binding var document: MyDocument

    var body: some View {
        Text("Document Content")
            .focusedSceneValue(\.focusedDocument, $document)
    }
}
```

### Accessing the current focused value

Use the [FocusedValue](focusedvalue.md) property wrapper in your [App](app.md) or [View](view.md) to read the current value in the `body`. The [FocusedBinding](focusedbinding.md) can be used as a convenient way to access the `wrappedValue` if the value type of the focused value is a `Binding`:

```swift
@main
struct DocumentApp: App {
    @FocusedBinding(\.focusedDocument) var currentDocument: MyDocument?

    var body: some Scene {
        DocumentGroup(newDocument: MyDocument()) { file in
            ContentView(document: file.$document)
                .focusedValue(\.focusedDocument, file.$document)
        }
        .commands {
            CommandGroup(after: .undoRedo) {
                Button("Increment") {
                    currentDocument?.value += 1
                }.disabled(currentDocument == nil)
            }
        }
    }
}
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md)

## Topics

### Getting the value for a key

- [subscript(_:)](<focusedvalues/subscript(__).md>) — Reads and writes values associated with a given focused value key.

## See Also

### Exposing value types to focused views

- [focusedValue(_:)](<view/focusedvalue(__).md>) — Sets the focused value for the given object type.
- [focusedValue(_:_:)](<view/focusedvalue(____).md>) — Modifies this view by injecting a value that you provide for use by other views whose state depends on the focused view hierarchy.
- [focusedSceneValue(_:)](<view/focusedscenevalue(__).md>) — Sets the focused value for the given object type at a scene-wide scope.
- [focusedSceneValue(_:_:)](<view/focusedscenevalue(____).md>) — Modifies this view by injecting a value that you provide for use by other views whose state depends on the focused scene.
