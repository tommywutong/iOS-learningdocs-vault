---
title: 'init(wrappedValue:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/observedobject/init(wrappedvalue:)'
source_url: 'https://developer.apple.com/documentation/swiftui/observedobject/init(wrappedvalue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/observedobject/init%28wrappedvalue%3A%29.json'
content_hash: 'sha256:419bbb3e1c5093d8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ObservedObject](../observedobject.md)

# init(wrappedValue:)

<sub>Initializer</sub>

Creates an observed object with an initial wrapped value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency init(wrappedValue: ObjectType)
```

## Parameters

- `wrappedValue` — An initial value for the observable object.

## Discussion

Don’t call this initializer directly. Instead, declare an input to a view with the `@ObservedObject` attribute, and pass a value to this input when you instantiate the view. Unlike a [StateObject](../stateobject.md) which manages data storage, you use an observed object to refer to storage that you manage elsewhere, as in the following example:

```swift
class DataModel: ObservableObject {
    @Published var name = "Some Name"
    @Published var isEnabled = false
}

struct MyView: View {
    @StateObject private var model = DataModel()

    var body: some View {
        Text(model.name)
        MySubView(model: model)
    }
}

struct MySubView: View {
    @ObservedObject var model: DataModel

    var body: some View {
        Toggle("Enabled", isOn: $model.isEnabled)
    }
}
```

Explicitly calling the observed object initializer in `MySubView` would behave correctly, but would needlessly recreate the same observed object instance every time SwiftUI calls the view’s initializer to redraw the view.

## See Also

### Creating an observed object

- [init(initialValue:)](<init(initialvalue_).md>) — Creates an observed object with an initial value.
