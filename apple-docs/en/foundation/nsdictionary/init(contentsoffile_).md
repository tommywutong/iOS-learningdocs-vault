---
title: 'init(contentsOfFile:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+（27.0 起废弃）, iPadOS 2.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.0+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsdictionary/init(contentsoffile:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdictionary/init(contentsoffile:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdictionary/init%28contentsoffile%3A%29.json'
content_hash: 'sha256:2109ff4381fd8adb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDictionary](../nsdictionary.md)

# init(contentsOfFile:)

<sub>Initializer</sub>

Initializes a newly allocated dictionary using the keys and values found in a file at a given path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init?(contentsOfFile path: String)
```

## Parameters

- `path` — A full or relative pathname. The file identified by `path` must contain a string representation of a property list whose root object is a dictionary.

## Return Value

An initialized dictionary—which might be different than the original receiver—that contains the dictionary at `path`, or `nil` if there is a file error or if the contents of the file are an invalid representation of a dictionary.

## Discussion

The dictionary representation in the file identified by `path` must contain only property list objects (`NSString`, `NSData`, `NSDate`, `NSNumber`, `NSArray`, or `NSDictionary` objects). For more details, see [Property List Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/Introduction/Introduction.html#//apple_ref/doc/uid/10000048i). The objects contained by this dictionary are immutable, even if the dictionary is mutable.

## See Also

### Creating a Dictionary from an External Source

- [init(contentsOfURL:error:)](<init(contentsofurl_error_).md>) — Initializes a newly allocated dictionary using the keys and values found at a given URL.
