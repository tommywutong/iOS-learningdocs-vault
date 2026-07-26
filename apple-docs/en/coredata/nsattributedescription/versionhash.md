---
title: versionHash
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsattributedescription/versionhash
source_url: 'https://developer.apple.com/documentation/coredata/nsattributedescription/versionhash'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsattributedescription/versionhash.json'
content_hash: 'sha256:f861af4ba09a7311'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSAttributeDescription](../nsattributedescription.md)

# versionHash

<sub>Instance Property</sub>

The version hash for the attribute.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var versionHash: Data { get }
```

## Discussion

The version hash is used to uniquely identify an attribute based on its configuration. This value includes the [versionHash](../nspropertydescription/versionhash.md) information from [NSPropertyDescription](../nspropertydescription.md) and the attribute type.

## See Also

### Related Documentation

- [versionHash](../nspropertydescription/versionhash.md) — The version hash for the receiver.
