---
title: projectedValue
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [watchOS 7.0+（9.2 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/swiftui/wkextensiondelegateadaptor/projectedvalue
source_url: 'https://developer.apple.com/documentation/swiftui/wkextensiondelegateadaptor/projectedvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/wkextensiondelegateadaptor/projectedvalue.json'
content_hash: 'sha256:3ada8da92e97b283'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WKExtensionDelegateAdaptor](../wkextensiondelegateadaptor.md)

# projectedValue

<sub>Instance Property</sub>

A projection of the observed object that provides bindings to its properties.

> [!warning] Deprecated
> Use WKApplicationDelegateAdaptor with a WKApplicationDelegate instead.

<sub>watchOS</sub>

```swift
@MainActor @preconcurrency var projectedValue: ObservedObject<DelegateType>.Wrapper { get }
```

## Discussion

Use the projected value to get a binding to a value that the delegate publishes. Access the projected value by prefixing the name of the delegate instance with a dollar sign (`$`). For example, you might publish a Boolean value in your extension delegate:

```swift
class MyExtensionDelegate: NSObject, WKExtensionDelegate, ObservableObject {
    @Published var isEnabled = false

    // ...
}
```

If you declare the delegate in your [App](../app.md) using the [WKExtensionDelegateAdaptor](../wkextensiondelegateadaptor.md) property wrapper, you can get the delegate that SwiftUI instantiates from the environment and access a binding to its published values from any view in your extension:

```swift
struct MyView: View {
    @EnvironmentObject private var extensionDelegate: MyExtensionDelegate

    var body: some View {
        Toggle("Enabled", isOn: $extensionDelegate.isEnabled)
    }
}
```

## See Also

### Getting the delegate adaptor

- [wrappedValue](wrappedvalue.md) — The underlying delegate. _(deprecated)_
