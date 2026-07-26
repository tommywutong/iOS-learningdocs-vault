---
title: projectedValue
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/nsapplicationdelegateadaptor/projectedvalue
source_url: 'https://developer.apple.com/documentation/swiftui/nsapplicationdelegateadaptor/projectedvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nsapplicationdelegateadaptor/projectedvalue.json'
content_hash: 'sha256:aa26499ead17c433'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NSApplicationDelegateAdaptor](../nsapplicationdelegateadaptor.md)

# projectedValue

<sub>Instance Property</sub>

A projection of the observed object that provides bindings to its properties.

<sub>macOS</sub>

```swift
@MainActor @preconcurrency var projectedValue: ObservedObject<DelegateType>.Wrapper { get }
```

## Discussion

Use the projected value to get a binding to a value that the delegate publishes. Access the projected value by prefixing the name of the delegate instance with a dollar sign (`$`). For example, you might publish a Boolean value in your application delegate:

```swift
class MyAppDelegate: NSObject, NSApplicationDelegate, ObservableObject {
    @Published var isEnabled = false

    // ...
}
```

If you declare the delegate in your [App](../app.md) using the [NSApplicationDelegateAdaptor](../nsapplicationdelegateadaptor.md) property wrapper, you can get the delegate that SwiftUI instantiates from the environment and access a binding to its published values from any view in your app:

```swift
struct MyView: View {
    @EnvironmentObject private var appDelegate: MyAppDelegate

    var body: some View {
        Toggle("Enabled", isOn: $appDelegate.isEnabled)
    }
}
```

## See Also

### Getting the delegate adaptor

- [wrappedValue](wrappedvalue.md) — The underlying delegate.
