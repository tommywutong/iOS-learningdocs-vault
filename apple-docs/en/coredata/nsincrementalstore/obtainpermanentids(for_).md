---
title: 'obtainPermanentIDs(for:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsincrementalstore/obtainpermanentids(for:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsincrementalstore/obtainpermanentids(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsincrementalstore/obtainpermanentids%28for%3A%29.json'
content_hash: 'sha256:cbe8698bb75d480f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSIncrementalStore](../nsincrementalstore.md)

# obtainPermanentIDs(for:)

<sub>Instance Method</sub>

Returns an array containing the object IDs for a given array of newly-inserted objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func obtainPermanentIDs(for array: [NSManagedObject]) throws -> [NSManagedObjectID]
```

## Parameters

- `array` — An array of newly-inserted objects.

## Return Value

An array containing the object IDs for the objects in `array`.

## Discussion

The returned array must return the object IDs in the same order as the objects appear in `array`.

## Discussion

This method is called before [- executeRequest:withContext:error:](<execute(__with_).md>) with a save request, to assign permanent IDs to newly-inserted objects.

## See Also

### Manipulating Managed Objects

- [- executeRequest:withContext:error:](<execute(__with_).md>) — Returns a value as appropriate for the given request, or nil if the request cannot be completed.
- [- newValuesForObjectWithID:withContext:error:](<newvaluesforobject(with_with_).md>) — Returns an incremental store node encapsulating the persistent external values of the object with a given object ID.
- [- newValueForRelationship:forObjectWithID:withContext:error:](<newvalue(forrelationship_forobjectwith_with_).md>) — Returns the relationship for the given relationship of the object with a given object ID.
- [- newObjectIDForEntity:referenceObject:](<newobjectid(for_referenceobject_).md>) — Returns a new object ID that uses given data as the key.
- [- referenceObjectForObjectID:](<referenceobject(for_).md>) — Returns the reference data used to construct a given object ID.
