---
title: 'stringWithContentsOfFile:encoding:error:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstring/stringwithcontentsoffile:encoding:error:'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/stringwithcontentsoffile:encoding:error:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/stringwithcontentsoffile%3Aencoding%3Aerror%3A.json'
content_hash: 'sha256:ee70edefa4766339'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# stringWithContentsOfFile:encoding:error:

<sub>Type Method</sub>

Returns a string created by reading data from the file at a given path interpreted using a given encoding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) stringWithContentsOfFile:(NSString *) path encoding:(NSStringEncoding) enc error:(NSError **) error;
```

## Parameters

- `path` — A path to a file.

- `enc` — The encoding of the file at `path`. For possible values, see [NSStringEncoding](../nsstringencoding.md).

- `error` — If an error occurs, upon returns contains an `NSError` object that describes the problem. If you are not interested in possible errors, pass in `NULL`.

## Return Value

A string created by reading data from the file named by `path` using the encoding, `enc`. If the file can’t be opened or there is an encoding error, returns `nil`.

## See Also

### Creating and Initializing a String from a File

- [- initWithContentsOfFile:encoding:error:](<init(contentsoffile_encoding_).md>) — Returns an `NSString` object initialized by reading data from the file at a given path using a given encoding.
- [stringWithContentsOfFile:usedEncoding:error:](stringwithcontentsoffile_usedencoding_error_.md) — Returns a string created by reading data from the file at a given path and returns by reference the encoding used to interpret the file.
- [- initWithContentsOfFile:usedEncoding:error:](<init(contentsoffile_usedencoding_).md>) — Returns an `NSString` object initialized by reading data from the file at a given path and returns by reference the encoding used to interpret the characters.
