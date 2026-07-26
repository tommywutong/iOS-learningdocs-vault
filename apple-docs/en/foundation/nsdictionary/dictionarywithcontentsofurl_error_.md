---
title: 'dictionaryWithContentsOfURL:error:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdictionary/dictionarywithcontentsofurl:error:'
source_url: 'https://developer.apple.com/documentation/foundation/nsdictionary/dictionarywithcontentsofurl:error:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdictionary/dictionarywithcontentsofurl%3Aerror%3A.json'
content_hash: 'sha256:8dc2108868466733'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDictionary](../nsdictionary.md)

# dictionaryWithContentsOfURL:error:

<sub>Type Method</sub>

Creates a dictionary using the keys and values found in a resource specified by a given URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (NSDictionary<NSString *,id> *) dictionaryWithContentsOfURL:(NSURL *) url error:(NSError **) error;
```

## Parameters

- `url` — A URL that identifies a resource containing a string representation of a property list whose root object is a dictionary.

## Return Value

A new dictionary that contains the dictionary at `url`, or `nil` if there is an error or if the contents of the resource are an invalid representation of a dictionary.

## Discussion

The dictionary representation in the file identified by path must contain only property list objects ([NSString](../nsstring.md), [NSData](../nsdata.md), [NSDate](../nsdate.md), [NSNumber](../nsnumber.md), [NSArray](../nsarray.md), or [NSDictionary](../nsdictionary.md) objects). For more details, see [Property List Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/Introduction/Introduction.html#//apple_ref/doc/uid/10000048i). The objects contained by this dictionary are immutable, even if the dictionary is mutable.

## See Also

### Creating a Dictionary from an External Source

- [dictionaryWithContentsOfFile:](dictionarywithcontentsoffile_.md) — Creates a dictionary using the keys and values found in a file specified by a given path. _(deprecated)_
- [- initWithContentsOfFile:](<init(contentsoffile_).md>) — Initializes a newly allocated dictionary using the keys and values found in a file at a given path. _(deprecated)_
