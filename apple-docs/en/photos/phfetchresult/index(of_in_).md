---
title: 'index(of:in:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phfetchresult/index(of:in:)'
source_url: 'https://developer.apple.com/documentation/photos/phfetchresult/index(of:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phfetchresult/index%28of%3Ain%3A%29.json'
content_hash: 'sha256:6d6de8b0fa3993cc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHFetchResult](../phfetchresult.md)

# index(of:in:)

<sub>Instance Method</sub>

Returns the lowest index within the specified range whose corresponding object in the fetch result is equal to the specified object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func index(of anObject: ObjectType, in range: NSRange) -> Int
```

## Parameters

- `anObject` — An object.

- `range` — The range of indexes in the fetch result within which to search for `anObject`.

## Return Value

The lowest index within `range` whose corresponding object in the fetch result is equal to `anObject`, or `NSNotFound` if no such object is in the fetch result.

## Discussion

Starting at `range.location`, this method sends an `==` message to each object in the fetch result until it finds a match or reaches the end of the fetch result. This method passes the `anObject` parameter to each `==` message.

Raises a range exception if the `range` parameter represents a range that doesn’t exist in the fetch result.

## See Also

### Finding Objects in a Fetch Result

- [- indexOfObject:](<index(of_).md>) — Returns the lowest index whose corresponding object in the fetch result is equal to the specified object.
