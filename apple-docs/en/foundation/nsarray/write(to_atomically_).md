---
title: 'write(to:atomically:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（27.0 起废弃）, iPadOS 2.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.0+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsarray/write(to:atomically:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsarray/write(to:atomically:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarray/write%28to%3Aatomically%3A%29.json'
content_hash: 'sha256:4a8da9184d6fc557'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArray](../nsarray.md)

# write(to:atomically:)

<sub>Instance Method</sub>

Writes the contents of the array to the location specified by a given URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func write(to url: URL, atomically: Bool) -> Bool
```

## Parameters

- `url` — The location at which to write the array.

- `atomically` — If [true](../../swift/true.md), the array is written to an auxiliary location, and then the auxiliary location is renamed to `aURL`. If [false](../../swift/false.md), the array is written directly to `aURL`. The [true](../../swift/true.md) option guarantees that `aURL`, if it exists at all, won’t be corrupted even if the system should crash during writing.

## Return Value

[true](../../swift/true.md) if the location is written successfully, otherwise [false](../../swift/false.md).

## Discussion

If the array’s contents are all property list objects (`NSString`, `NSData`, `NSArray`, or `NSDictionary` objects), the location written by this method can be used to initialize a new array with the class method `NSArray/init(contentsOfURL:)-fk8x` or the instance method `NSArray/init(contentsOfURL:)-5lo2y`.

## See Also

### Storing Arrays

- [- writeToFile:atomically:](<write(tofile_atomically_).md>) — Writes the contents of the array to a file at a given path. _(deprecated)_
