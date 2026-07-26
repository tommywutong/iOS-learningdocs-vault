---
title: 'subscript(dynamicMember:)'
framework: SwiftUI
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/environmentobject/wrapper/subscript(dynamicmember:)'
source_url: 'https://developer.apple.com/documentation/swiftui/environmentobject/wrapper/subscript(dynamicmember:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentobject/wrapper/subscript%28dynamicmember%3A%29.json'
content_hash: 'sha256:6ba3c372f400769f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [EnvironmentObject](../../environmentobject.md) · [Wrapper](../wrapper.md)

# subscript(dynamicMember:)

<sub>Instance Subscript</sub>

Returns a binding to the resulting value of a given key path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency subscript<Subject>(dynamicMember keyPath: ReferenceWritableKeyPath<ObjectType, Subject>) -> Binding<Subject> { get }
```

## Parameters

- `keyPath` — A key path to a specific resulting value.

## Return Value

A new binding.
