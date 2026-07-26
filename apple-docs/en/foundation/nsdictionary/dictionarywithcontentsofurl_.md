---
title: 'dictionaryWithContentsOfURL:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+（27.0 起废弃）, iPadOS 2.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.0+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsdictionary/dictionarywithcontentsofurl:'
source_url: 'https://developer.apple.com/documentation/foundation/nsdictionary/dictionarywithcontentsofurl:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdictionary/dictionarywithcontentsofurl%3A.json'
content_hash: 'sha256:b50524bb92f06ed2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDictionary](../nsdictionary.md)

# dictionaryWithContentsOfURL:

<sub>Type Method</sub>

Creates a dictionary using the keys and values found in a resource specified by a given URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (NSDictionary<id,id> *) dictionaryWithContentsOfURL:(NSURL *) url;
```

## Parameters

- `url` — An URL that identifies a resource containing a string representation of a property list whose root object is a dictionary.

## Return Value

A new dictionary that contains the dictionary at `aURL`, or `nil` if there is an error or if the contents of the resource are an invalid representation of a dictionary.

## Discussion

The dictionary representation in the file identified by `aURL` must contain only property list objects (`NSString`, `NSData`, `NSDate`, `NSNumber`, `NSArray`, or `NSDictionary` objects). For more details, see [Property List Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/Introduction/Introduction.html#//apple_ref/doc/uid/10000048i). The objects contained by this dictionary are immutable, even if the dictionary is mutable.

> [!warning] Deprecated
> Use [dictionaryWithContentsOfURL:error:](dictionarywithcontentsofurl_error_.md) instead.
