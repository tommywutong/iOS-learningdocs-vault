---
title: 'hasTag(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/containervalues/hastag(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/containervalues/hastag(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/containervalues/hastag%28_%3A%29.json'
content_hash: 'sha256:bc4ef6860a3ede14'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ContainerValues](../containervalues.md)

# hasTag(_:)

<sub>Instance Method</sub>

Returns true if the container values contain a tag matching a given value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func hasTag<V>(_ tag: V) -> Bool where V : Hashable
```

## Parameters

- `tag` — The tag value to check for.

## Return Value

If the container values has a tag matching the given value.

## Discussion

Tag values are set using the `View/tag` modifier.
