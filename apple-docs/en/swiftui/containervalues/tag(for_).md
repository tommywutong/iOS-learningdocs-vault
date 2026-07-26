---
title: 'tag(for:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/containervalues/tag(for:)'
source_url: 'https://developer.apple.com/documentation/swiftui/containervalues/tag(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/containervalues/tag%28for%3A%29.json'
content_hash: 'sha256:49ed5bb35c0ea685'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ContainerValues](../containervalues.md)

# tag(for:)

<sub>Instance Method</sub>

The tag value for the given type if the container values contains one.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func tag<V>(for type: V.Type) -> V? where V : Hashable
```

## Parameters

- `type` — The type to get the tag value for.

## Return Value

The tag value for the given type if the subview has one, otherwise `nil`.

## Discussion

Tag values are set using the `View/tag` modifier.
