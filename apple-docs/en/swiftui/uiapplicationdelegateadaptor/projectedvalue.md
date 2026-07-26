---
title: projectedValue
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/uiapplicationdelegateadaptor/projectedvalue
source_url: 'https://developer.apple.com/documentation/swiftui/uiapplicationdelegateadaptor/projectedvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/uiapplicationdelegateadaptor/projectedvalue.json'
content_hash: 'sha256:fa059849c17007e2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [UIApplicationDelegateAdaptor](../uiapplicationdelegateadaptor.md)

# projectedValue

<sub>Instance Property</sub>

A projection of the observed object that provides bindings to its properties.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency var projectedValue: ObservedObject<DelegateType>.Wrapper { get }
```

## Discussion

Use the projected value to get a binding to a value that the delegate publishes. Access the projected value by prefixing the name of the delegate instance with a dollar sign (`$`). For example, you might publish a Boolean value in your application delegate:

```swift
class MyAppDelegate: NSObject, UIApplicationDelegate, ObservableObject {
    @Published var isEnabled = false

    // ...
}
```

If you declare the delegate in your [App](../app.md) using the [UIApplicationDelegateAdaptor](../uiapplicationdelegateadaptor.md) property wrapper, you can get the delegate that SwiftUI instantiates from the environment and access a binding to its published values from any view in your app:

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

- [wrappedValue](wrappedvalue.md) — The underlying app delegate.
