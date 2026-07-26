---
title: 'init(initialValue:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/state/init(initialvalue:)'
source_url: 'https://developer.apple.com/documentation/swiftui/state/init(initialvalue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/state/init%28initialvalue%3A%29.json'
content_hash: 'sha256:2c2a02c969fdcda5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [State](../state.md)

# init(initialValue:)

<sub>Initializer</sub>

Creates a state property that stores an initial value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) init(initialValue value: Value)
```

## Parameters

- `value` — An initial value to store in the state property.

## Discussion

This initializer has the same behavior as the [init(wrappedValue:)](<init(wrappedvalue_).md>) initializer. See that initializer for more information.

## See Also

### Creating a state

- [init(wrappedValue:)](<init(wrappedvalue_).md>) — Creates a state property that stores an initial wrapped value.
- [init()](<init().md>) — Creates a state property without an initial value.
