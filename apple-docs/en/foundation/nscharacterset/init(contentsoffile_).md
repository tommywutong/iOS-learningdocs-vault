---
title: 'init(contentsOfFile:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscharacterset/init(contentsoffile:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscharacterset/init(contentsoffile:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscharacterset/init%28contentsoffile%3A%29.json'
content_hash: 'sha256:f01c3927cc1cd725'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCharacterSet](../nscharacterset.md)

# init(contentsOfFile:)

<sub>Initializer</sub>

Returns a character set read from the bitmap representation stored in the file a given path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(contentsOfFile fName: String)
```

## Parameters

- `fName` — A path to a file containing a bitmap representation of a character set. The path name must end with the extension `.bitmap`.

## Return Value

A character set read from the bitmap representation stored in the file at `path`.

## Discussion

This method doesn’t use filenames to check for the uniqueness of the character sets it creates. To prevent duplication of character sets in memory, cache them and make them available through an API that checks whether the requested set has already been loaded.

To read a bitmap representation from any file, use the `NSData` method[dataWithContentsOfFile:options:error:](../nsdata/datawithcontentsoffile_options_error_.md) and pass the result to [+ characterSetWithBitmapRepresentation:](<init(bitmaprepresentation_).md>).

## See Also

### Creating and Managing Character Sets as Bitmap Representations

- [+ characterSetWithBitmapRepresentation:](<init(bitmaprepresentation_).md>) — Returns a character set containing characters determined by a given bitmap representation.
- [bitmapRepresentation](bitmaprepresentation.md) — An `NSData` object encoding the receiver in binary format.
