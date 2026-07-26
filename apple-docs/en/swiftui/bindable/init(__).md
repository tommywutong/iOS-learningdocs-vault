---
title: 'init(_:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/bindable/init(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/bindable/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/bindable/init%28_%3A%29.json'
content_hash: 'sha256:990bcebf1929fcb4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Bindable](../bindable.md)

# init(_:)

<sub>Initializer</sub>

Creates a bindable object from an observable object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ wrappedValue: Value)
```

## Discussion

This initializer is equivalent to [init(wrappedValue:)](<init(wrappedvalue_).md>), but is more succinct when when creating bindable objects nested within other expressions. For example, you can use the initializer to create a bindable object inline with code that declares a view that takes a binding as a parameter:

```swift
struct TitleEditView: View {
    @Environment(Book.self) private var book

    var body: some View {
        TextField("Title", text: Bindable(book).title)
    }
}
```

## See Also

### Creating a bindable value

- [init(wrappedValue:)](<init(wrappedvalue_).md>) — Creates a bindable object from an observable object.
- [init(projectedValue:)](<init(projectedvalue_).md>) — Creates a bindable from the value of another bindable.
