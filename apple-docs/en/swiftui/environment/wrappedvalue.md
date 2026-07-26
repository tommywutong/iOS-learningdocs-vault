---
title: wrappedValue
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environment/wrappedvalue
source_url: 'https://developer.apple.com/documentation/swiftui/environment/wrappedvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environment/wrappedvalue.json'
content_hash: 'sha256:629624cd4d88ebbf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Environment](../environment.md)

# wrappedValue

<sub>Instance Property</sub>

The current value of the environment property.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var wrappedValue: Value { get }
```

## Discussion

The wrapped value property provides primary access to the value’s data. However, you don’t access `wrappedValue` directly. Instead, you read the property variable created with the [Environment](../environment.md) property wrapper:

```swift
@Environment(\.colorScheme) var colorScheme: ColorScheme

var body: some View {
    if colorScheme == .dark {
        DarkContent()
    } else {
        LightContent()
    }
}
```
