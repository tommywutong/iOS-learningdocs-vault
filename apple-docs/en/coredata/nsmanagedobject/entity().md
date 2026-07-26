---
title: entity()
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobject/entity()
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobject/entity()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobject/entity%28%29.json'
content_hash: 'sha256:a86d28bb68ab7bfd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObject](../nsmanagedobject.md)

# entity()

<sub>Type Method</sub>

Returns the entity description that is associated with this subclass.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func entity() -> NSEntityDescription
```

## Discussion

This method is only legal to call on subclasses of `NSManagedObject` that represent a single entity in the model.

## See Also

### Getting a Managed Object’s Identity

- [entity](entity-swift.property.md) — The entity description of the managed object.
- [objectID](objectid.md) — The object ID of the managed object.
