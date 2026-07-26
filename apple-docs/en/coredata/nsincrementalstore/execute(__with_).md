---
title: 'execute(_:with:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsincrementalstore/execute(_:with:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsincrementalstore/execute(_:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsincrementalstore/execute%28_%3Awith%3A%29.json'
content_hash: 'sha256:aeb46d6ad2f2658d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSIncrementalStore](../nsincrementalstore.md)

# execute(_:with:)

<sub>Instance Method</sub>

Returns a value as appropriate for the given request, or nil if the request cannot be completed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func execute(_ request: NSPersistentStoreRequest, with context: NSManagedObjectContext?) throws -> Any
```

## Parameters

- `request` — A fetch request.

- `context` — The managed object context used to execute `request`.

## Return Value

A value as appropriate for `request`, or `nil` if the request cannot be completed

## Discussion

The value to return depends on the result type (see [resultType](../nsfetchrequest/resulttype.md)) of `request`:

- If it is `NSManagedObjectResultType`, `NSManagedObjectIDResultType`, or `NSDictionaryResultType`, the method should return an array containing all objects in the store matching the request.
- If it is `NSCountResultType`, the method should return an array containing an `NSNumber` whose value is the count of all objects in the store matching the request.
- If the request is a save request, the method should return an empty array.

If the save request contains nil values for the inserted/updated/deleted/locked collections; you should treat it as a request to save the store metadata.

You should implement this method conservatively, and expect that unknown request types may at some point be passed to the method. The correct behavior in these cases is to return `nil` and an error.

## See Also

### Manipulating Managed Objects

- [- newValuesForObjectWithID:withContext:error:](<newvaluesforobject(with_with_).md>) — Returns an incremental store node encapsulating the persistent external values of the object with a given object ID.
- [- newValueForRelationship:forObjectWithID:withContext:error:](<newvalue(forrelationship_forobjectwith_with_).md>) — Returns the relationship for the given relationship of the object with a given object ID.
- [- obtainPermanentIDsForObjects:error:](<obtainpermanentids(for_).md>) — Returns an array containing the object IDs for a given array of newly-inserted objects.
- [- newObjectIDForEntity:referenceObject:](<newobjectid(for_referenceobject_).md>) — Returns a new object ID that uses given data as the key.
- [- referenceObjectForObjectID:](<referenceobject(for_).md>) — Returns the reference data used to construct a given object ID.
