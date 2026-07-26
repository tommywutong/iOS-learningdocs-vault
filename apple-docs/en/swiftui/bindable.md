---
title: Bindable
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/bindable
source_url: 'https://developer.apple.com/documentation/swiftui/bindable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/bindable.json'
content_hash: 'sha256:b6fe2f85c630bb03'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# Bindable

<sub>Structure</sub>

A property wrapper type that supports creating bindings to the mutable properties of observable objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@dynamicMemberLookup @propertyWrapper struct Bindable<Value>
```

## Overview

Use this property wrapper to create bindings to mutable properties of a data model object that conforms to the [Observable](../observation/observable.md) protocol. For example, the following code wraps the `book` input with `@Bindable`. Then it uses a [TextField](textfield.md) to change the `title` property of a book, and a [Toggle](toggle.md) to change the `isAvailable` property, using the `$` syntax to pass a binding for each property to those controls.

```swift
@Observable
class Book: Identifiable {
    var title = "Sample Book Title"
    var isAvailable = true
}

struct BookEditView: View {
    @Bindable var book: Book
    @Environment(\.dismiss) private var dismiss

    var body: some View {
        Form {
            TextField("Title", text: $book.title)

            Toggle("Book is available", isOn: $book.isAvailable)

            Button("Close") {
                dismiss()
            }
        }
    }
}
```

You can use the `Bindable` property wrapper on properties and variables to an [Observable](../observation/observable.md) object. This includes global variables, properties that exists outside of SwiftUI types, or even local variables. For example, you can create a `@Bindable` variable within a view’s [body](view/body-8kl5o.md):

```swift
struct LibraryView: View {
    @State private var books = [Book(), Book(), Book()]

    var body: some View {
        List(books) { book in
            @Bindable var book = book
            TextField("Title", text: $book.title)
        }
    }
}
```

The `@Bindable` variable `book` provides a binding that connects [TextField](textfield.md) to the `title` property of a book so that a person can make changes directly to the model data.

Use this same approach when you need a binding to a property of an observable object stored in a view’s environment. For example, the following code uses the [Environment](environment.md) property wrapper to retrieve an instance of the observable type `Book`. Then the code creates a `@Bindable` variable `book` and passes a binding for the `title` property to a [TextField](textfield.md) using the `$` syntax.

```swift
struct TitleEditView: View {
    @Environment(Book.self) private var book

    var body: some View {
        @Bindable var book = book
        TextField("Title", text: $book.title)
    }
}
```

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [Escapable](../swift/escapable.md), [Identifiable](../swift/identifiable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a bindable value

- [init(_:)](<bindable/init(__).md>) — Creates a bindable object from an observable object.
- [init(wrappedValue:)](<bindable/init(wrappedvalue_).md>) — Creates a bindable object from an observable object.
- [init(projectedValue:)](<bindable/init(projectedvalue_).md>) — Creates a bindable from the value of another bindable.

### Getting the value

- [wrappedValue](bindable/wrappedvalue.md) — The wrapped object.
- [projectedValue](bindable/projectedvalue.md) — The bindable wrapper for the object that creates bindings to its properties using dynamic member lookup.
- [subscript(dynamicMember:)](<bindable/subscript(dynamicmember_).md>) — Returns a binding to the value of a given key path.

## See Also

### Creating and sharing view state

- [Managing user interface state](managing-user-interface-state.md) — Encapsulate view-specific data within your app’s view hierarchy to make your views reusable.
- [State()](<state().md>) — Creates a property that can read and write a value managed by SwiftUI.
- [State(initialValue:)](<state(initialvalue_).md>) — Creates a property with an initial value that can read and write a value managed by SwiftUI.
- [State(wrappedValue:)](<state(wrappedvalue_).md>) — Creates a property with a wrapped value that can read and write a value managed by SwiftUI.
- [State](state.md) — A property wrapper type that can read and write a value managed by SwiftUI.
- [Binding](binding.md) — A property wrapper type that can read and write a value owned by a source of truth.
