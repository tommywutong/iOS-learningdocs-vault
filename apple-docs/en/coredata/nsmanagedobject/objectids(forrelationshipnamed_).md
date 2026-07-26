---
title: 'objectIDs(forRelationshipNamed:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.3+, iPadOS 8.3+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsmanagedobject/objectids(forrelationshipnamed:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobject/objectids(forrelationshipnamed:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobject/objectids%28forrelationshipnamed%3A%29.json'
content_hash: 'sha256:47cbd40eb8615be1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObject](../nsmanagedobject.md)

# objectIDs(forRelationshipNamed:)

<sub>Instance Method</sub>

Returns the object IDs for all of the managed objects that are in the named relationship.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func objectIDs(forRelationshipNamed key: String) -> [NSManagedObjectID]
```

## See Also

### Supporting Key-Value Coding

- [- valueForKey:](<value(forkey_).md>) — Returns the value for the property specified by `key`.
- [- setValue:forKey:](<setvalue(__forkey_).md>) — Sets the specified property of the managed object to the specified value.
- [- primitiveValueForKey:](<primitivevalue(forkey_).md>) — Returns the value for the specified property from the managed object’s private internal storage .
- [- setPrimitiveValue:forKey:](<setprimitivevalue(__forkey_).md>) — Sets the value of a given property in the managed object’s private internal storage.
