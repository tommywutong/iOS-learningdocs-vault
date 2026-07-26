---
title: 'subscript(_:)'
framework: Photos
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phfetchresult/subscript(_:)'
source_url: 'https://developer.apple.com/documentation/photos/phfetchresult/subscript(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phfetchresult/subscript%28_%3A%29.json'
content_hash: 'sha256:1efac9dd6e8d94ba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHFetchResult](../phfetchresult.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Returns the object located at the specified index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
subscript(idx: Int) -> ObjectType { get }
```

## Parameters

- `idx` — An index within the bounds of the fetch result.

## Return Value

The object located at `index` in the fetch result.

## Discussion

Raises a range exception if `idx` is beyond the end of the fetch result (that is, greater than or equal to the value of the [count](count.md) property).

This method behaves identically to the [- objectAtIndex:](<object(at_).md>) method and allows you to access a fetch result using subscript syntax. That is, the two statements below produce the same result.

**Swift**

```swift
print("First object \(fetchResult[0])")
print("First object \(fetchResult.object(at: 0))")
```

**Objective-C**

```objc
NSLog(@"First object: %@", [fetchResult objectAtIndex:0]);
NSLog(@"First object: %@", fetchResult[0]);
```

## See Also

### Querying a Fetch Result

- [- containsObject:](<contains(__).md>) — Returns whether the specified object is present in the fetch result.
- [count](count.md) — The number of objects in the fetch result.
- [- countOfAssetsWithMediaType:](<countofassets(with_).md>) — Returns the number of assets in the fetch result of a specified type.
- [firstObject](firstobject.md) — The first object in the fetch result.
- [lastObject](lastobject.md) — The last object in the fetch result.
- [- objectAtIndex:](<object(at_).md>) — Returns the object located at the specified index.
- [- objectsAtIndexes:](<objects(at_).md>) — Returns an array containing the objects in the fetch result at the indexes in the specified index set.
