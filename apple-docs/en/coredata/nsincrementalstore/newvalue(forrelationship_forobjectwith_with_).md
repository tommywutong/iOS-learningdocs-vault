---
title: 'newValue(forRelationship:forObjectWith:with:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsincrementalstore/newvalue(forrelationship:forobjectwith:with:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsincrementalstore/newvalue(forrelationship:forobjectwith:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsincrementalstore/newvalue%28forrelationship%3Aforobjectwith%3Awith%3A%29.json'
content_hash: 'sha256:9919ef80b4122fdc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSIncrementalStore](../nsincrementalstore.md)

# newValue(forRelationship:forObjectWith:with:)

<sub>Instance Method</sub>

Returns the relationship for the given relationship of the object with a given object ID.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func newValue(forRelationship relationship: NSRelationshipDescription, forObjectWith objectID: NSManagedObjectID, with context: NSManagedObjectContext?) throws -> Any
```

## Parameters

- `relationship` — The relationship for which values are requested.

- `objectID` — The ID of the object for which values are requested.

- `context` — The managed object context into which values will be returned.

## Return Value

The value of the relationship specified `relationship` of the object with object ID `objectID`, or `nil` if an error occurs.

## Discussion

If the relationship is a to-one, the method should return an [NSManagedObjectID](../nsmanagedobjectid.md) instance that identifies the destination, or an instance of [NSNull](../../foundation/nsnull.md) if the relationship value is `nil`.

If the relationship is a to-many, the method should return a collection object containing [NSManagedObjectID](../nsmanagedobjectid.md) instances to identify the related objects. Using an `NSArray` instance is preferred because it will be the most efficient. A store may also return an instance of `NSSet` or `NSOrderedSet`; an instance of `NSDictionary` is not acceptable.

If an object with object ID `objectID` cannot be found, the method should return `nil` and—if `error` is not `NULL`—create and return an appropriate error object in `error`.

## See Also

### Manipulating Managed Objects

- [- executeRequest:withContext:error:](<execute(__with_).md>) — Returns a value as appropriate for the given request, or nil if the request cannot be completed.
- [- newValuesForObjectWithID:withContext:error:](<newvaluesforobject(with_with_).md>) — Returns an incremental store node encapsulating the persistent external values of the object with a given object ID.
- [- obtainPermanentIDsForObjects:error:](<obtainpermanentids(for_).md>) — Returns an array containing the object IDs for a given array of newly-inserted objects.
- [- newObjectIDForEntity:referenceObject:](<newobjectid(for_referenceobject_).md>) — Returns a new object ID that uses given data as the key.
- [- referenceObjectForObjectID:](<referenceobject(for_).md>) — Returns the reference data used to construct a given object ID.
