---
title: 'init(objects:count:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsarray/init(objects:count:)-7dct1'
source_url: 'https://developer.apple.com/documentation/foundation/nsarray/init(objects:count:)-7dct1'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarray/init%28objects%3Acount%3A%29-7dct1.json'
content_hash: 'sha256:8ff2abf7514c5a74'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArray](../nsarray.md)

# init(objects:count:)

<sub>Initializer</sub>

Creates and returns an array that includes a given number of objects from a given C array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(objects: UnsafePointer<AnyObject>, count cnt: Int)
```

## Parameters

- `objects` — A C array of objects.

- `cnt` — The number of values from the `objects` C array to include in the new array. This number will be the count of the new array—it must not be negative or greater than the number of elements in `objects`.

## Return Value

A new array including the first `count` objects from `objects`.

## Discussion

Elements are added to the new array in the same order they appear in `objects`, up to but not including index `count`. For example:

```objc
NSString *strings[3];
strings[0] = @"First";
strings[1] = @"Second";
strings[2] = @"Third";
 
NSArray *stringsArray = [NSArray arrayWithObjects:strings count:2];
// strings array contains { @"First", @"Second" }
```

## See Also

### Creating an Array

- [+ arrayWithObject:](<init(object_).md>) — Creates and returns an array containing a given object.
