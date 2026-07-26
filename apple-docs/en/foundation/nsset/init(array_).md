---
title: 'init(array:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsset/init(array:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsset/init(array:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsset/init%28array%3A%29.json'
content_hash: 'sha256:9e14c82c4958fa79'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSet](../nsset.md)

# init(array:)

<sub>Initializer</sub>

Initializes a newly allocated set with the objects that are contained in a given array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(array: [Any])
```

## Parameters

- `array` — An array of objects to add to the new set. If the same object appears more than once in `array`, it is represented only once in the returned set. Each object receives a [retain](../../objectivec/nsobject-c.protocol/retain.md) message as it is added to the set.

## Return Value

An initialized set with the contents of `array`. The returned set might be different than the original receiver.

## See Also

### Initializing a Set

- [- initWithObjects:count:](<init(objects_count_)-7kift.md>) — Initializes a newly allocated set with a specified number of objects from a given C array of objects.
- [- initWithSet:](<init(set_)-1xovx.md>) — Initializes a newly allocated set and adds to it objects from another given set.
- [- initWithSet:copyItems:](<init(set_copyitems_).md>) — Initializes a newly allocated set and adds to it members of another given set.
- [- init](<init().md>) — Initializes a newly allocated set.
