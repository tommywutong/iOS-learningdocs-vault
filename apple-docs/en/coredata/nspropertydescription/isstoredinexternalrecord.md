---
title: isStoredInExternalRecord
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+（11.0 起废弃）, iPadOS 3.0+（11.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.6+（10.13 起废弃）, tvOS（11.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（4.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/coredata/nspropertydescription/isstoredinexternalrecord
source_url: 'https://developer.apple.com/documentation/coredata/nspropertydescription/isstoredinexternalrecord'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspropertydescription/isstoredinexternalrecord.json'
content_hash: 'sha256:e6b2126b4367bee4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPropertyDescription](../nspropertydescription.md)

# isStoredInExternalRecord

<sub>Instance Property</sub>

A Boolean value that indicates whether to write the property’s data in an external record file that corresponds to the managed object.

> [!warning] Deprecated
> Spotlight integration is deprecated. Use CoreSpotlight integration instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isStoredInExternalRecord: Bool { get set }
```

## Discussion

[true](../../swift/true.md) if the property data should be written out in an external record file corresponding to the managed object, otherwise [false](../../swift/false.md). For additional information, see [Core Data Spotlight Integration Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/SpotlightCoreData/Introduction/introSpotlightCoreData.html#//apple_ref/doc/uid/TP40008065).

### Special Considerations

This property has no effect on iOS.

## See Also

### Specifying Spotlight Support

- [indexedBySpotlight](isindexedbyspotlight.md) — A Boolean value that indicates whether Core Data adds the property’s value to the Core Spotlight index.
