---
title: localizationDictionary
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobjectmodel/localizationdictionary
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/localizationdictionary'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectmodel/localizationdictionary.json'
content_hash: 'sha256:5dc25c0b6c692d29'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectModel](../nsmanagedobjectmodel.md)

# localizationDictionary

<sub>Instance Property</sub>

The localization dictionary of the model.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var localizationDictionary: [String : String]? { get set }
```

## Discussion

The following table describes the key and value pattern for the localization dictionary.

| Key | Value | Note |
|---|---|---|
| “Entity/NonLocalizedEntityName” | “LocalizedEntityName” |  |
| “Property/NonLocalizedPropertyName/Entity/EntityName” | “LocalizedPropertyName” | (1) |
| “Property/NonLocalizedPropertyName” | “LocalizedPropertyName” |  |
| “ErrorString/NonLocalizedErrorString” | “LocalizedErrorString” |  |

(1) For properties in different entities with the same non-localized name but that should have different localized names.

### Special Considerations

In OS X v10.4, `localizationDictionary` may return `nil` until Core Data lazily loads the dictionary for its own purposes (for example, reporting a localized error).
