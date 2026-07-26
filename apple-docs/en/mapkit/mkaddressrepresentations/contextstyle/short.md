---
title: MKAddressRepresentations.ContextStyle.short
framework: MapKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkaddressrepresentations/contextstyle/short
source_url: 'https://developer.apple.com/documentation/mapkit/mkaddressrepresentations/contextstyle/short'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkaddressrepresentations/contextstyle/short.json'
content_hash: 'sha256:edf86d29b37ef4f3'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [MapKit](../../../mapkit.md) · [MKAddressRepresentations](../../mkaddressrepresentations.md) · [ContextStyle](../contextstyle.md)

# MKAddressRepresentations.ContextStyle.short

<sub>Case</sub>

The value that represents the short context style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case short
```

## Discussion

The value that tells the framework to exclude optional context. For example, when used with [- cityWithContextUsingStyle:](<../citywithcontext(__).md>) MapKit always excludes the region name.

## See Also

### Available context styles

- [MKAddressRepresentationsContextStyleAutomatic](automatic.md) — The value that represents the automatic context style.
- [MKAddressRepresentationsContextStyleFull](full.md) — The value that represents the full context style.
