---
title: 'index(of:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phfetchresult/index(of:)'
source_url: 'https://developer.apple.com/documentation/photos/phfetchresult/index(of:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phfetchresult/index%28of%3A%29.json'
content_hash: 'sha256:87c61f578b646670'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHFetchResult](../phfetchresult.md)

# index(of:)

<sub>Instance Method</sub>

Returns the lowest index whose corresponding object in the fetch result is equal to the specified object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func index(of anObject: ObjectType) -> Int
```

## Parameters

- `anObject` — An object.

## Return Value

The lowest index whose corresponding object in the fetch result is equal to `anObject`, or `NSNotFound` if no such object is in the fetch result.

## Discussion

Starting at index `0`, this method sends an `==` message to each object in the fetch result until it finds a match or reaches the end of the fetch result. This method passes the `anObject` parameter to each `==` message.

## See Also

### Finding Objects in a Fetch Result

- [- indexOfObject:inRange:](<index(of_in_).md>) — Returns the lowest index within the specified range whose corresponding object in the fetch result is equal to the specified object.
