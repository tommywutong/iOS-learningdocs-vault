---
title: EnvironmentKey
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentkey
source_url: 'https://developer.apple.com/documentation/swiftui/environmentkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentkey.json'
content_hash: 'sha256:90411705d43a3ad7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# EnvironmentKey

<sub>Protocol</sub>

A key for accessing values in the environment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol EnvironmentKey
```

## Overview

You can create custom environment values by extending the [EnvironmentValues](environmentvalues.md) structure with new properties. First declare a new environment key type and specify a value for the required [defaultValue](environmentkey/defaultvalue.md) property:

```swift
private struct MyEnvironmentKey: EnvironmentKey {
    static let defaultValue: String = "Default value"
}
```

The Swift compiler automatically infers the associated [Value](environmentkey/value.md) type as the type you specify for the default value. Then use the key to define a new environment value property:

```swift
extension EnvironmentValues {
    var myCustomValue: String {
        get { self[MyEnvironmentKey.self] }
        set { self[MyEnvironmentKey.self] = newValue }
    }
}
```

Clients of your environment value never use the key directly. Instead, they use the key path of your custom environment value property. To set the environment value for a view and all its subviews, add the [environment(_:_:)](<view/environment(____).md>) view modifier to that view:

```swift
MyView()
    .environment(\.myCustomValue, "Another string")
```

As a convenience, you can also define a dedicated view modifier to apply this environment value:

```swift
extension View {
    func myCustomValue(_ myCustomValue: String) -> some View {
        environment(\.myCustomValue, myCustomValue)
    }
}
```

This improves clarity at the call site:

```swift
MyView()
    .myCustomValue("Another string")
```

To read the value from inside `MyView` or one of its descendants, use the [Environment](environment.md) property wrapper:

```swift
struct MyView: View {
    @Environment(\.myCustomValue) var customValue: String

    var body: some View {
        Text(customValue) // Displays "Another string".
    }
}
```

## Topics

### Getting the default value

- [defaultValue](environmentkey/defaultvalue.md) — The default value for the environment key.
- [Value](environmentkey/value.md) — The associated type representing the type of the environment key’s value.

## See Also

### Creating custom environment values

- [Entry()](<entry().md>) — Creates an environment values, transaction, container values, or focused values entry.
