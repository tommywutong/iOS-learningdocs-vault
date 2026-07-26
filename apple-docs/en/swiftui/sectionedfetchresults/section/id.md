---
title: id
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/sectionedfetchresults/section/id
source_url: 'https://developer.apple.com/documentation/swiftui/sectionedfetchresults/section/id'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/sectionedfetchresults/section/id.json'
content_hash: 'sha256:6fa374a0d87a3499'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [SectionedFetchResults](../../sectionedfetchresults.md) · [Section](../section.md)

# id

<sub>Instance Property</sub>

The value that all entities in the section share for a specified key path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency let id: SectionIdentifier
```

## Discussion

Specify the key path that the entities share this value with by setting the [SectionedFetchRequest](../../sectionedfetchrequest.md) instance’s `sectionIdentifier` parameter during initialization, or by modifying the corresponding [SectionedFetchResults](../../sectionedfetchresults.md) instance’s [sectionIdentifier](../sectionidentifier.md) property.
