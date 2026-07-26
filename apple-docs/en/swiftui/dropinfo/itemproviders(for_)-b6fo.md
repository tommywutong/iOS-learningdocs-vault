---
title: 'itemProviders(for:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.4+（27.0 起废弃）, iPadOS 13.4+（27.0 起废弃）, Mac Catalyst 13.4+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/dropinfo/itemproviders(for:)-b6fo'
source_url: 'https://developer.apple.com/documentation/swiftui/dropinfo/itemproviders(for:)-b6fo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/dropinfo/itemproviders%28for%3A%29-b6fo.json'
content_hash: 'sha256:e770cc1da5a7d2de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DropInfo](../dropinfo.md)

# itemProviders(for:)

<sub>Instance Method</sub>

Returns an array of items that each conform to at least one of the specified uniform type identifiers.

> [!warning] Deprecated
> Use [itemProviders(for:)](<itemproviders(for_)-93409.md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
func itemProviders(for types: [String]) -> [NSItemProvider]
```

## Discussion

This function is only valid during the `performDrop()` action.

## See Also

### Deprecated symbols

- [hasItemsConforming(to:)](<hasitemsconforming(to_)-4qeez.md>) — Returns whether at least one item conforms to at least one of the specified uniform type identifiers. _(deprecated)_
