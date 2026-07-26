---
title: 'primitiveValue(forKey:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsmanagedobject/primitivevalue(forkey:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobject/primitivevalue(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobject/primitivevalue%28forkey%3A%29.json'
content_hash: 'sha256:e6d2f738c427bb6e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObject](../nsmanagedobject.md)

# primitiveValue(forKey:)

<sub>Instance Method</sub>

Returns the value for the specified property from the managed object’s private internal storage .

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func primitiveValue(forKey key: String) -> Any?
```

## Parameters

- `key` — The name of one of the receiver’s properties.

## Return Value

The value of the property specified by `key`. Returns `nil` if no value has been set.

## Discussion

This method does not invoke the access notification methods ([- willAccessValueForKey:](<willaccessvalue(forkey_).md>) and [- didAccessValueForKey:](<didaccessvalue(forkey_).md>)). This method is used primarily by subclasses that implement custom accessor methods that need direct access to the receiver’s private storage.

### Special Considerations

Subclasses should not override this method.

The following points also apply:

- Primitive accessor methods are only supported on _modeled_ properties. If you invoke a primitive accessor on an unmodeled property, it will instead operate upon a random modeled property. (The debug libraries and frameworks (available from [Apple Developer Website](http://developer.apple.com/)) have assertions to test for passing unmodeled keys to these methods.)
- You are strongly encouraged to use the dynamically-generated accessors rather than using this method directly (for example, `primitiveName:` instead of `primitiveValueForKey:@"name"`). The dynamic accessors are much more efficient, and allow for compile-time checking.

## See Also

### Related Documentation

- [- setObservationInfo:](<setobservationinfo(__).md>) — Sets the observation info of the managed object.

### Supporting Key-Value Coding

- [- valueForKey:](<value(forkey_).md>) — Returns the value for the property specified by `key`.
- [- setValue:forKey:](<setvalue(__forkey_).md>) — Sets the specified property of the managed object to the specified value.
- [- setPrimitiveValue:forKey:](<setprimitivevalue(__forkey_).md>) — Sets the value of a given property in the managed object’s private internal storage.
- [- objectIDsForRelationshipNamed:](<objectids(forrelationshipnamed_).md>) — Returns the object IDs for all of the managed objects that are in the named relationship.
