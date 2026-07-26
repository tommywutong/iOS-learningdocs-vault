---
title: relationshipKeyPathsForPrefetching
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsfetchrequest/relationshipkeypathsforprefetching
source_url: 'https://developer.apple.com/documentation/coredata/nsfetchrequest/relationshipkeypathsforprefetching'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsfetchrequest/relationshipkeypathsforprefetching.json'
content_hash: 'sha256:d8b755f067cc96c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSFetchRequest](../nsfetchrequest.md)

# relationshipKeyPathsForPrefetching

<sub>Instance Property</sub>

The relationship key paths to prefetch along with the entity for the request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var relationshipKeyPathsForPrefetching: [String]? { get set }
```

## Discussion

This property is an array of relationship key-path strings in NSKeyValueCoding notation (as you typically use with [value(forKeyPath:)](<../../objectivec/nsobject-swift.class/value(forkeypath_).md>)). The default value is an empty array (no prefetching).

Prefetching allows Core Data to obtain related objects in a single fetch (per entity), rather than incurring subsequent access to the store for each individual record as their faults are tripped. For example, given an Employee entity with a relationship to a Department entity, suppose you fetch all the employees, and then for each print out their name and the name of the department to which they belong. In this case, a fault might be fired for each individual Department object. This can represent a significant overhead. You can avoid this by prefetching the department relationship in the Employee fetch, as illustrated in Listing 1.

(For more details, see Core Data Performance in Core Data Programming Guide)

**Swift**

```swift
let request = NSFetchRequest(entityName: "Employee") as NSFetchRequest<NSManagedObject>
request.relationshipKeyPathsForPrefetching = ["department"]
```

**Objective-C**

```objc
NSFetchRequest *request = [NSFetchRequest fetchRequestWithEntityName:@"Employee"];
[request setRelationshipKeyPathsForPrefetching:@[@"department"]];
```
