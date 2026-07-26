---
title: 'newObjectID(for:referenceObject:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsincrementalstore/newobjectid(for:referenceobject:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsincrementalstore/newobjectid(for:referenceobject:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsincrementalstore/newobjectid%28for%3Areferenceobject%3A%29.json'
content_hash: 'sha256:191c4b17ec93226a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSIncrementalStore](../nsincrementalstore.md)

# newObjectID(for:referenceObject:)

<sub>Instance Method</sub>

Returns a new object ID that uses given data as the key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func newObjectID(for entity: NSEntityDescription, referenceObject data: Any) -> NSManagedObjectID
```

## Parameters

- `entity` — The entity for the new object ID.

- `data` — An object of type [NSString](../../foundation/nsstring.md) or [NSNumber](../../foundation/nsnumber.md) to use as the key.

## Return Value

A new object ID for an instance of the entity specified by `entity` and that uses `data` as the key.

## Discussion

You should not override this method.

## See Also

### Manipulating Managed Objects

- [- executeRequest:withContext:error:](<execute(__with_).md>) — Returns a value as appropriate for the given request, or nil if the request cannot be completed.
- [- newValuesForObjectWithID:withContext:error:](<newvaluesforobject(with_with_).md>) — Returns an incremental store node encapsulating the persistent external values of the object with a given object ID.
- [- newValueForRelationship:forObjectWithID:withContext:error:](<newvalue(forrelationship_forobjectwith_with_).md>) — Returns the relationship for the given relationship of the object with a given object ID.
- [- obtainPermanentIDsForObjects:error:](<obtainpermanentids(for_).md>) — Returns an array containing the object IDs for a given array of newly-inserted objects.
- [- referenceObjectForObjectID:](<referenceobject(for_).md>) — Returns the reference data used to construct a given object ID.
