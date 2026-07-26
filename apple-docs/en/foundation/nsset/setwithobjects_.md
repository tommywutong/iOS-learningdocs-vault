---
title: 'setWithObjects:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsset/setwithobjects:'
source_url: 'https://developer.apple.com/documentation/foundation/nsset/setwithobjects:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsset/setwithobjects%3A.json'
content_hash: 'sha256:7abbab3f51282c64'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSet](../nsset.md)

# setWithObjects:

<sub>Type Method</sub>

Creates and returns a set containing the objects in a given argument list.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) setWithObjects:(ObjectType) firstObj;
```

## Parameters

- `firstObj` — The first object to add to the new set.

## Return Value

A new set containing the objects in the argument list.

## Discussion

To add additional objects to the new set, pass a comma-separated list of trailing variadic arguments, ending with `nil`.  If the same object appears more than once in the list of objects, it is added only once to the returned set. Each object receives a [retain](../../objectivec/nsobject-c.protocol/retain.md) message as it is added to the set.

As an example, the following code excerpt creates a set containing three different types of elements (assuming `aPath` exits):

```objc
NSSet *mySet;
NSData *someData = [NSData dataWithContentsOfFile:aPath];
NSValue *aValue = [NSNumber numberWithInteger:5];
NSString *aString = @"a string";
 
mySet = [NSSet setWithObjects:someData, aValue, aString, nil];
```

## See Also

### Creating a Set

- [set](set.md) — Creates and returns an empty set.
- [setWithArray:](setwitharray_.md) — Creates and returns a set containing a uniqued collection of the objects contained in a given array.
- [+ setWithObject:](<init(object_).md>) — Creates and returns a set that contains a single given object.
- [+ setWithObjects:count:](<init(objects_count_)-65ni4.md>) — Creates and returns a set containing a specified number of objects from a given C array of objects.
- [setWithSet:](setwithset_.md) — Creates and returns a set containing the objects from another set.
- [- setByAddingObject:](<adding(__).md>) — Returns a new set formed by adding a given object to the receiving set.
- [- setByAddingObjectsFromSet:](<addingobjects(from_)-2i31h.md>) — Returns a new set formed by adding the objects in a given set to the receiving set.
- [- setByAddingObjectsFromArray:](<addingobjects(from_)-544m9.md>) — Returns a new set formed by adding the objects in a given array to the receiving set.
