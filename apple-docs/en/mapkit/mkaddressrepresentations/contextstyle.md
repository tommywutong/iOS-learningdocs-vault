---
title: MKAddressRepresentations.ContextStyle
framework: MapKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkaddressrepresentations/contextstyle
source_url: 'https://developer.apple.com/documentation/mapkit/mkaddressrepresentations/contextstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkaddressrepresentations/contextstyle.json'
content_hash: 'sha256:d16896d14caeb8bb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKAddressRepresentations](../mkaddressrepresentations.md)

# MKAddressRepresentations.ContextStyle

<sub>Enumeration</sub>

Values that describe the degree of disambiguation context to include in an address representation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum ContextStyle
```

## Discussion

Use the [ContextStyle](contextstyle.md) to configure the degree of disambiguation context to include in an address representation from [MKAddressRepresentations](../mkaddressrepresentations.md), such as including the region name with the city.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating a context style

- [init(rawValue:)](<contextstyle/init(rawvalue_).md>) — Initializes a context style with the raw value you provide.

### Available context styles

- [MKAddressRepresentationsContextStyleAutomatic](contextstyle/automatic.md) — The value that represents the automatic context style.
- [MKAddressRepresentationsContextStyleShort](contextstyle/short.md) — The value that represents the short context style.
- [MKAddressRepresentationsContextStyleFull](contextstyle/full.md) — The value that represents the full context style.
