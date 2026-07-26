---
title: 'newValuesForObject(with:with:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsincrementalstore/newvaluesforobject(with:with:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsincrementalstore/newvaluesforobject(with:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsincrementalstore/newvaluesforobject%28with%3Awith%3A%29.json'
content_hash: 'sha256:4d458c7baa59a0fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSIncrementalStore](../nsincrementalstore.md)

# newValuesForObject(with:with:)

<sub>Instance Method</sub>

Returns an incremental store node encapsulating the persistent external values of the object with a given object ID.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func newValuesForObject(with objectID: NSManagedObjectID, with context: NSManagedObjectContext) throws -> NSIncrementalStoreNode
```

## Parameters

- `objectID` — The ID of the object for which values are requested.

- `context` — The managed object context into which values will be returned.

## Return Value

An incremental store node encapsulating the persistent external values of the object with object ID `objectID`, or `nil` if the corresponding object cannot be found.

## Discussion

The returned node should include all attributes values and may include to-one relationship values as instances of [NSManagedObjectID](../nsmanagedobjectid.md).

If an object with object ID `objectID` cannot be found, the method should return `nil` and—if `error` is not `NULL`—create and return an appropriate error object in `error`.

## See Also

### Manipulating Managed Objects

- [- executeRequest:withContext:error:](<execute(__with_).md>) — Returns a value as appropriate for the given request, or nil if the request cannot be completed.
- [- newValueForRelationship:forObjectWithID:withContext:error:](<newvalue(forrelationship_forobjectwith_with_).md>) — Returns the relationship for the given relationship of the object with a given object ID.
- [- obtainPermanentIDsForObjects:error:](<obtainpermanentids(for_).md>) — Returns an array containing the object IDs for a given array of newly-inserted objects.
- [- newObjectIDForEntity:referenceObject:](<newobjectid(for_referenceobject_).md>) — Returns a new object ID that uses given data as the key.
- [- referenceObjectForObjectID:](<referenceobject(for_).md>) — Returns the reference data used to construct a given object ID.
