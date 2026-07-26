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
doc_path: '/documentation/swiftui/state/init(wrappedvalue:)'
source_url: 'https://developer.apple.com/documentation/swiftui/state/init(wrappedvalue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/state/init%28wrappedvalue%3A%29.json'
content_hash: 'sha256:37dda8de7449a76a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [State](../state.md)

# init(wrappedValue:)

<sub>Initializer</sub>

Creates a state property that stores an initial wrapped value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(wrappedValue value: Value)
```

## Parameters

- `value` — An initial value to store in the state property.

## Discussion

You don’t call this initializer directly. Instead, SwiftUI calls it for you when you declare a property with the `@State` attribute and provide an initial value:

```swift
struct MyView: View {
    @State private var isPlaying: Bool = false

    // ...
}
```

SwiftUI initializes the state’s storage only once for each container instance that you declare. In the above code, SwiftUI creates `isPlaying` only the first time it initializes a particular instance of `MyView`. On the other hand, each instance of `MyView` creates a distinct instance of the state. For example, each of the views in the following [VStack](../vstack.md) has its own `isPlaying` value:

```swift
var body: some View {
    VStack {
        MyView()
        MyView()
    }
}
```

## See Also

### Creating a state

- [init(initialValue:)](<init(initialvalue_).md>) — Creates a state property that stores an initial value.
- [init()](<init().md>) — Creates a state property without an initial value.
