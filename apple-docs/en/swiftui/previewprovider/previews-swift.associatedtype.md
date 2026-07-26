---
title: Previews
framework: SwiftUI
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, tvOS 13.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 6.0+（27.0 起废弃）]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: /documentation/swiftui/previewprovider/previews-swift.associatedtype
source_url: 'https://developer.apple.com/documentation/swiftui/previewprovider/previews-swift.associatedtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/previewprovider/previews-swift.associatedtype.json'
content_hash: 'sha256:be0a04f8db33f6ac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [PreviewProvider](../previewprovider.md)

# Previews

<sub>Associated Type</sub>

The type to preview.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
associatedtype Previews : View
```

## Discussion

When you create a preview, Swift infers this type from your implementation of the required [previews](previews-swift.type.property.md) property.

## See Also

### Creating a preview

- [previews](previews-swift.type.property.md) — A collection of views to preview. _(deprecated)_
