---
title: 'subscript(_:)'
framework: Foundation
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsarray/subscript(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsarray/subscript(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarray/subscript%28_%3A%29.json'
content_hash: 'sha256:334250232d1198eb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArray](../nsarray.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Returns the object at the specified index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(idx: Int) -> Any { get }
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(idx: Int) -> Any { get set }
```

## Parameters

- `idx` — An index within the bounds of the array.

## Return Value

The object located at `idx`.

## Discussion

This method has the same behavior as the [- objectAtIndex:](<object(at_).md>) method.

If `idx` is beyond the end of the array (that is, if `idx` is greater than or equal to the value returned by `count`), an [NSRangeException](../nsexceptionname/rangeexception.md) is raised.

You shouldn’t need to call this method directly. Instead, this method is called when accessing an object by index using subscripting.

```objc
id value = array[3]; // equivalent to [array objectAtIndex:3]
```

## See Also

### Querying an Array

- [- containsObject:](<contains(__).md>) — Returns a Boolean value that indicates whether a given object is present in the array.
- [count](count.md) — The number of objects in the array.
- [firstObject](firstobject.md) — The first object in the array.
- [lastObject](lastobject.md) — The last object in the array.
- [- objectAtIndex:](<object(at_).md>) — Returns the object located at the specified index.
- [- objectsAtIndexes:](<objects(at_).md>) — Returns an array containing the objects in the array at the indexes specified by a given index set.
- [- objectEnumerator](<objectenumerator().md>) — Returns an enumerator object that lets you access each object in the array.
- [- reverseObjectEnumerator](<reverseobjectenumerator().md>) — Returns an enumerator object that lets you access each object in the array, in reverse order.
