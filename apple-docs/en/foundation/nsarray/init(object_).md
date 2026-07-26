---
title: 'init(object:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsarray/init(object:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsarray/init(object:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarray/init%28object%3A%29.json'
content_hash: 'sha256:a590bdff79ab8102'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArray](../nsarray.md)

# init(object:)

<sub>Initializer</sub>

Creates and returns an array containing a given object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(object anObject: Any)
```

## Parameters

- `anObject` — An object.

## Return Value

An array containing the single element `anObject`.

## Discussion

Alternatively, you can use array literal syntax in Objective-C or Swift to create an array containing a given object:

**Swift**

```swift
let array: NSArray = ["Hello, world!"]
```

**Objective-C**

```objc
NSArray *array = @[@"Hello, world!"];
```

## See Also

### Creating an Array

- [+ arrayWithObjects:count:](<init(objects_count_)-7dct1.md>) — Creates and returns an array that includes a given number of objects from a given C array.
