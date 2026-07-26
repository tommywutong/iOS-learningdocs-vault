---
title: 'init(wrappedValue:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/stateobject/init(wrappedvalue:)'
source_url: 'https://developer.apple.com/documentation/swiftui/stateobject/init(wrappedvalue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/stateobject/init%28wrappedvalue%3A%29.json'
content_hash: 'sha256:9f8ab74372b6424d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [StateObject](../stateobject.md)

# init(wrappedValue:)

<sub>Initializer</sub>

Creates a new state object with an initial wrapped value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(wrappedValue thunk: @autoclosure @escaping () -> ObjectType)
```

## Parameters

- `thunk` — An initial value for the state object.

## Discussion

You typically don’t call this initializer directly. Instead, SwiftUI calls it for you when you declare a property with the `@StateObject` attribute in an [App](../app.md), [Scene](../scene.md), or [View](../view.md) and provide an initial value:

```swift
struct MyView: View {
    @StateObject private var model = DataModel()

    // ...
}
```

SwiftUI creates only one instance of the state object for each container instance that you declare. In the above code, SwiftUI creates `model` only the first time it initializes a particular instance of `MyView`. On the other hand, each instance of `MyView` creates a distinct instance of the data model. For example, each of the views in the following [VStack](../vstack.md) has its own model storage:

```swift
var body: some View {
    VStack {
        MyView()
        MyView()
    }
}
```

### Initialize using external data

If the initial state of a state object depends on external data, you can call this initializer directly. However, use caution when doing this, because SwiftUI only initializes the object once during the lifetime of the view — even if you call the state object initializer more than once — which might result in unexpected behavior. For more information and an example, see [StateObject](../stateobject.md).
