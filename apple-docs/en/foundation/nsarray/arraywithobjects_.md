---
title: 'arrayWithObjects:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsarray/arraywithobjects:'
source_url: 'https://developer.apple.com/documentation/foundation/nsarray/arraywithobjects:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarray/arraywithobjects%3A.json'
content_hash: 'sha256:3683a9c79c7304cc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArray](../nsarray.md)

# arrayWithObjects:

<sub>Type Method</sub>

Creates and returns an array containing the objects in the argument list.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) arrayWithObjects:(ObjectType) firstObj;
```

## Parameters

- `firstObj` — The first object for the array.

## Return Value

An array containing the objects in the argument list.

## Discussion

Pass comma-separated list of trailing variadic arguments as additional objects, ending with `nil`.

The following code example creates an array containing three different types of element:

```objc
NSDate *aDate = [NSDate distantFuture];
NSValue *aValue = @(5);
NSString *aString = @"hello";
 
NSArray *array = [NSArray arrayWithObjects:aDate, aValue, aString, nil];
```

Alternatively, you can use array literal syntax in Objective-C or Swift to create an array containing given objects:

```objc
NSArray *array = @[@"alpha", @"bravo", @"charlie"];
```

## See Also

### Creating an Array

- [array](array.md) — Creates and returns an empty array.
- [arrayWithArray:](arraywitharray_.md) — Creates and returns an array containing the objects in another given array.
- [arrayWithContentsOfFile:](arraywithcontentsoffile_.md) — Creates and returns an array containing the contents of the file specified by a given path. _(deprecated)_
- [+ arrayWithObject:](<init(object_).md>) — Creates and returns an array containing a given object.
- [+ arrayWithObjects:count:](<init(objects_count_)-7dct1.md>) — Creates and returns an array that includes a given number of objects from a given C array.
