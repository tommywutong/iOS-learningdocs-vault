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
doc_path: '/documentation/swiftui/observedobject/init(initialvalue:)'
source_url: 'https://developer.apple.com/documentation/swiftui/observedobject/init(initialvalue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/observedobject/init%28initialvalue%3A%29.json'
content_hash: 'sha256:b9a83187c4153a52'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ObservedObject](../observedobject.md)

# init(initialValue:)

<sub>Initializer</sub>

Creates an observed object with an initial value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @export(implementation) @preconcurrency init(initialValue: ObjectType)
```

## Parameters

- `initialValue` — An initial value.

## Discussion

This initializer has the same behavior as the [init(wrappedValue:)](<init(wrappedvalue_).md>) initializer. See that initializer for more information.

## See Also

### Creating an observed object

- [init(wrappedValue:)](<init(wrappedvalue_).md>) — Creates an observed object with an initial wrapped value.
