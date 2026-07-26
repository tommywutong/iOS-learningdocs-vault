---
title: 'referenceObject(for:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsincrementalstore/referenceobject(for:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsincrementalstore/referenceobject(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsincrementalstore/referenceobject%28for%3A%29.json'
content_hash: 'sha256:aac60a523b5033ae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSIncrementalStore](../nsincrementalstore.md)

# referenceObject(for:)

<sub>Instance Method</sub>

Returns the reference data used to construct a given object ID.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func referenceObject(for objectID: NSManagedObjectID) -> Any
```

## Parameters

- `objectID` — An object ID created by the receiver.

## Return Value

The reference data used to construct objectID.

## Discussion

This method raises an [invalidArgumentException](../../foundation/nsexceptionname/invalidargumentexception.md) if the object ID was not created by the receiving store.

You should not override this method.

## See Also

### Manipulating Managed Objects

- [- executeRequest:withContext:error:](<execute(__with_).md>) — Returns a value as appropriate for the given request, or nil if the request cannot be completed.
- [- newValuesForObjectWithID:withContext:error:](<newvaluesforobject(with_with_).md>) — Returns an incremental store node encapsulating the persistent external values of the object with a given object ID.
- [- newValueForRelationship:forObjectWithID:withContext:error:](<newvalue(forrelationship_forobjectwith_with_).md>) — Returns the relationship for the given relationship of the object with a given object ID.
- [- obtainPermanentIDsForObjects:error:](<obtainpermanentids(for_).md>) — Returns an array containing the object IDs for a given array of newly-inserted objects.
- [- newObjectIDForEntity:referenceObject:](<newobjectid(for_referenceobject_).md>) — Returns a new object ID that uses given data as the key.
