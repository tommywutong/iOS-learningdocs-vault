---
title: MKAddressRepresentations.ContextStyle.full
framework: MapKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkaddressrepresentations/contextstyle/full
source_url: 'https://developer.apple.com/documentation/mapkit/mkaddressrepresentations/contextstyle/full'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkaddressrepresentations/contextstyle/full.json'
content_hash: 'sha256:81a24fb283fb0033'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [MapKit](../../../mapkit.md) · [MKAddressRepresentations](../../mkaddressrepresentations.md) · [ContextStyle](../contextstyle.md)

# MKAddressRepresentations.ContextStyle.full

<sub>Case</sub>

The value that represents the full context style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case full
```

## Discussion

The value that tells the framework to include all relevant context. For example, when used with [- cityWithContextUsingStyle:](<../citywithcontext(__).md>) MapKit always includes the region name if the device is in that region.

## See Also

### Available context styles

- [MKAddressRepresentationsContextStyleAutomatic](automatic.md) — The value that represents the automatic context style.
- [MKAddressRepresentationsContextStyleShort](short.md) — The value that represents the short context style.
