---
title: isIndexedBySpotlight
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspropertydescription/isindexedbyspotlight
source_url: 'https://developer.apple.com/documentation/coredata/nspropertydescription/isindexedbyspotlight'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspropertydescription/isindexedbyspotlight.json'
content_hash: 'sha256:22cc4962b1979503'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPropertyDescription](../nspropertydescription.md)

# isIndexedBySpotlight

<sub>Instance Property</sub>

A Boolean value that indicates whether Core Data adds the property’s value to the Core Spotlight index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isIndexedBySpotlight: Bool { get set }
```

## Discussion

> [!important] Important
> If you set this property to [true](../../swift/true.md) for a property description that describes a relationship, you must override [- attributeSetForObject:](<../nscoredatacorespotlightdelegate/attributeset(for_).md>) in your Core Spotlight delegate and return the necessary set of attributes. Core Data doesn’t automatically infer indexable information for relationships.

You can also set this property using the Index in Spotlight attribute in the Attributes inspector of the Core Data model editor.

## See Also

### Specifying Spotlight Support

- [storedInExternalRecord](isstoredinexternalrecord.md) — A Boolean value that indicates whether to write the property’s data in an external record file that corresponds to the managed object. _(deprecated)_
