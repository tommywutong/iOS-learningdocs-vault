---
title: 'itemProviders(for:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/dropinfo/itemproviders(for:)-93409'
source_url: 'https://developer.apple.com/documentation/swiftui/dropinfo/itemproviders(for:)-93409'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/dropinfo/itemproviders%28for%3A%29-93409.json'
content_hash: 'sha256:c6814f4d1420a9ac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DropInfo](../dropinfo.md)

# itemProviders(for:)

<sub>Instance Method</sub>

Finds item providers that conform to at least one of the specified uniform type identifiers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
func itemProviders(for contentTypes: [UTType]) -> [NSItemProvider]
```

## Parameters

- `contentTypes` — The uniform type identifiers to query for.

## Return Value

The item providers that conforms to `contentTypes`.

## Discussion

This function is only valid during the `performDrop()` action.

## See Also

### Checking for items

- [hasItemsConforming(to:)](<hasitemsconforming(to_)-47irh.md>) — Indicates whether at least one item conforms to at least one of the specified uniform type identifiers.
