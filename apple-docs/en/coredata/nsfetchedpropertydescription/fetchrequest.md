---
title: fetchRequest
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsfetchedpropertydescription/fetchrequest
source_url: 'https://developer.apple.com/documentation/coredata/nsfetchedpropertydescription/fetchrequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsfetchedpropertydescription/fetchrequest.json'
content_hash: 'sha256:6ad6c7ce2d476249'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSFetchedPropertyDescription](../nsfetchedpropertydescription.md)

# fetchRequest

<sub>Instance Property</sub>

The fetch request of the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var fetchRequest: NSFetchRequest<any NSFetchRequestResult>? { get set }
```

## Discussion

Setting the fetch request raises an exception if the receiver’s model has been used by an object graph manager.

## See Also

### Related Documentation

- [Core Data Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075)
- [Predicate Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Predicates/AdditionalChapters/Introduction.html#//apple_ref/doc/uid/TP40001789)
