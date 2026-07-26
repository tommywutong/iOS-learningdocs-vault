---
title: init()
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/state/init()
source_url: 'https://developer.apple.com/documentation/swiftui/state/init()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/state/init%28%29.json'
content_hash: 'sha256:25fe490c1a11fbc9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [State](../state.md)

# init()

<sub>Initializer</sub>

Creates a state property without an initial value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init()
```

## Discussion

This initializer behaves like the [init(wrappedValue:)](<init(wrappedvalue_).md>) initializer with an input of `nil`. See that initializer for more information.

## See Also

### Creating a state

- [init(wrappedValue:)](<init(wrappedvalue_).md>) — Creates a state property that stores an initial wrapped value.
- [init(initialValue:)](<init(initialvalue_).md>) — Creates a state property that stores an initial value.
