---
title: 'stringWithContentsOfFile:usedEncoding:error:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstring/stringwithcontentsoffile:usedencoding:error:'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/stringwithcontentsoffile:usedencoding:error:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/stringwithcontentsoffile%3Ausedencoding%3Aerror%3A.json'
content_hash: 'sha256:56b0128c99c8df17'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# stringWithContentsOfFile:usedEncoding:error:

<sub>Type Method</sub>

Returns a string created by reading data from the file at a given path and returns by reference the encoding used to interpret the file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) stringWithContentsOfFile:(NSString *) path usedEncoding:(NSStringEncoding *) enc error:(NSError **) error;
```

## Parameters

- `path` — A path to a file.

- `enc` — Upon return, if the file is read successfully, contains the encoding used to interpret the file at `path`. For possible values, see [NSStringEncoding](../nsstringencoding.md).

- `error` — If an error occurs, upon returns contains an `NSError` object that describes the problem. If you are not interested in possible errors, you may pass in `NULL`.

## Return Value

A string created by reading data from the file named by `path`. If the file can’t be opened or there is an encoding error, returns `nil`.

## Discussion

This method attempts to determine the encoding of the file at `path`.

## See Also

### Creating and Initializing a String from a File

- [stringWithContentsOfFile:encoding:error:](stringwithcontentsoffile_encoding_error_.md) — Returns a string created by reading data from the file at a given path interpreted using a given encoding.
- [- initWithContentsOfFile:encoding:error:](<init(contentsoffile_encoding_).md>) — Returns an `NSString` object initialized by reading data from the file at a given path using a given encoding.
- [- initWithContentsOfFile:usedEncoding:error:](<init(contentsoffile_usedencoding_).md>) — Returns an `NSString` object initialized by reading data from the file at a given path and returns by reference the encoding used to interpret the characters.
