---
title: 'hasItemsConforming(to:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/dropinfo/hasitemsconforming(to:)-47irh'
source_url: 'https://developer.apple.com/documentation/swiftui/dropinfo/hasitemsconforming(to:)-47irh'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/dropinfo/hasitemsconforming%28to%3A%29-47irh.json'
content_hash: 'sha256:3a0d41285e6687e0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DropInfo](../dropinfo.md)

# hasItemsConforming(to:)

<sub>Instance Method</sub>

Indicates whether at least one item conforms to at least one of the specified uniform type identifiers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
func hasItemsConforming(to contentTypes: [UTType]) -> Bool
```

## Parameters

- `contentTypes` — The uniform type identifiers to query for.

## Return Value

Whether at least one item conforms to one of `contentTypes`.

## See Also

### Checking for items

- [itemProviders(for:)](<itemproviders(for_)-93409.md>) — Finds item providers that conform to at least one of the specified uniform type identifiers.
