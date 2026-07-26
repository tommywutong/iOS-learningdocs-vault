---
title: 'setValue(_:forKey:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsmanagedobject/setvalue(_:forkey:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobject/setvalue(_:forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobject/setvalue%28_%3Aforkey%3A%29.json'
content_hash: 'sha256:c25cfdfb1476c209'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObject](../nsmanagedobject.md)

# setValue(_:forKey:)

<sub>Instance Method</sub>

Sets the specified property of the managed object to the specified value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setValue(_ value: Any?, forKey key: String)
```

## Parameters

- `value` — The new value for the property specified by `key`.

- `key` — The name of one of the receiver’s properties.

## Discussion

If `key` is not a property defined by the model, the method raises an exception. If `key` identifies a to-one relationship, relates the object specified by `value` to the receiver, unrelating the previously related object if there was one. Given a collection object and a key that identifies a to-many relationship, relates the objects contained in the collection to the receiver, unrelating previously related objects if there were any.

This method is overridden by `NSManagedObject` to access the managed object’s generic dictionary storage unless the receiver’s class explicitly provides key-value coding compliant accessor methods for `key`.

> [!important] Important
> You must not override this method.

## See Also

### Related Documentation

- [- setObservationInfo:](<setobservationinfo(__).md>) — Sets the observation info of the managed object.

### Supporting Key-Value Coding

- [- valueForKey:](<value(forkey_).md>) — Returns the value for the property specified by `key`.
- [- primitiveValueForKey:](<primitivevalue(forkey_).md>) — Returns the value for the specified property from the managed object’s private internal storage .
- [- setPrimitiveValue:forKey:](<setprimitivevalue(__forkey_).md>) — Sets the value of a given property in the managed object’s private internal storage.
- [- objectIDsForRelationshipNamed:](<objectids(forrelationshipnamed_).md>) — Returns the object IDs for all of the managed objects that are in the named relationship.
