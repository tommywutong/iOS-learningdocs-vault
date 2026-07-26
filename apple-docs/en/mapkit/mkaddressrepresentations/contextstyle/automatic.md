---
title: MKAddressRepresentations.ContextStyle.automatic
framework: MapKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkaddressrepresentations/contextstyle/automatic
source_url: 'https://developer.apple.com/documentation/mapkit/mkaddressrepresentations/contextstyle/automatic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkaddressrepresentations/contextstyle/automatic.json'
content_hash: 'sha256:4416aba33f0b616e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [MapKit](../../../mapkit.md) · [MKAddressRepresentations](../../mkaddressrepresentations.md) · [ContextStyle](../contextstyle.md)

# MKAddressRepresentations.ContextStyle.automatic

<sub>Case</sub>

The value that represents the automatic context style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case automatic
```

## Discussion

This value tells the framework to automatically select the content style for address representations. For example, when used with [- cityWithContextUsingStyle:](<../citywithcontext(__).md>) MapKit only includes the region.

## See Also

### Available context styles

- [MKAddressRepresentationsContextStyleShort](short.md) — The value that represents the short context style.
- [MKAddressRepresentationsContextStyleFull](full.md) — The value that represents the full context style.
