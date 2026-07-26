---
title: 'init(projectedValue:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/binding/init(projectedvalue:)'
source_url: 'https://developer.apple.com/documentation/swiftui/binding/init(projectedvalue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/binding/init%28projectedvalue%3A%29.json'
content_hash: 'sha256:e42a2b167f836b0c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Binding](../binding.md)

# init(projectedValue:)

<sub>Initializer</sub>

Creates a binding from the value of another binding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) init(projectedValue: Binding<Value>)
```

## See Also

### Creating a binding

- [init(_:)](<init(__).md>) — Creates a binding by projecting the base value to a hashable value.
- [init(get:set:)](<init(get_set_).md>) — Creates a binding with closures that read and write the binding value.
- [constant(_:)](<constant(__).md>) — Creates a binding with an immutable value.
