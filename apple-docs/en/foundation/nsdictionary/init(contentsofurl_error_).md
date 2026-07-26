---
title: 'init(contentsOfURL:error:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdictionary/init(contentsofurl:error:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdictionary/init(contentsofurl:error:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdictionary/init%28contentsofurl%3Aerror%3A%29.json'
content_hash: 'sha256:90920f6863cefd21'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDictionary](../nsdictionary.md)

# init(contentsOfURL:error:)

<sub>Initializer</sub>

Initializes a newly allocated dictionary using the keys and values found at a given URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(contentsOfURL url: URL, error: ()) throws
```

## Parameters

- `url` — A URL that identifies a resource containing a string representation of a property list whose root object is a dictionary.

- `error` — On failure, a reference to the error that occurred.

## Return Value

An initialized dictionary that contains the dictionary at `url`, or `nil` if there is an error or if the contents of the resource are an invalid representation of a dictionary.

## Discussion

The dictionary representation in the file identified by `url` must contain only property list objects ([NSString](../nsstring.md), [NSData](../nsdata.md), [NSDate](../nsdate.md), [NSNumber](../nsnumber.md), [NSArray](../nsarray.md), or [NSDictionary](../nsdictionary.md) objects). For more details, see [Property List Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/Introduction/Introduction.html#//apple_ref/doc/uid/10000048i). The objects contained by this dictionary are immutable, even if the dictionary is mutable.

In Swift, this initializer throws if there is an error loading the URL, or if the contents of the resource are an invalid representation of a dictionary.

## See Also

### Creating a Dictionary from an External Source

- [- initWithContentsOfFile:](<init(contentsoffile_).md>) — Initializes a newly allocated dictionary using the keys and values found in a file at a given path. _(deprecated)_
