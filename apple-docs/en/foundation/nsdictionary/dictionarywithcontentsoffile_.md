---
title: 'dictionaryWithContentsOfFile:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+（27.0 起废弃）, iPadOS 2.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.0+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsdictionary/dictionarywithcontentsoffile:'
source_url: 'https://developer.apple.com/documentation/foundation/nsdictionary/dictionarywithcontentsoffile:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdictionary/dictionarywithcontentsoffile%3A.json'
content_hash: 'sha256:8846e57f4d95cc45'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDictionary](../nsdictionary.md)

# dictionaryWithContentsOfFile:

<sub>Type Method</sub>

Creates a dictionary using the keys and values found in a file specified by a given path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (NSDictionary<id,id> *) dictionaryWithContentsOfFile:(NSString *) path;
```

## Parameters

- `path` — A full or relative pathname. The file identified by `path` must contain a string representation of a property list whose root object is a dictionary.

## Return Value

A new dictionary that contains the dictionary at `path`, or `nil` if there is a file error or if the contents of the file are an invalid representation of a dictionary.

## Discussion

The dictionary representation in the file identified by `path` must contain only property list objects (`NSString`, `NSData`, `NSDate`, `NSNumber`, `NSArray`, or `NSDictionary` objects). For more details, see [Property List Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/Introduction/Introduction.html#//apple_ref/doc/uid/10000048i). The objects contained by this dictionary are immutable, even if the dictionary is mutable.

## See Also

### Creating a Dictionary from an External Source

- [dictionaryWithContentsOfURL:error:](dictionarywithcontentsofurl_error_.md) — Creates a dictionary using the keys and values found in a resource specified by a given URL.
- [- initWithContentsOfFile:](<init(contentsoffile_).md>) — Initializes a newly allocated dictionary using the keys and values found in a file at a given path. _(deprecated)_
