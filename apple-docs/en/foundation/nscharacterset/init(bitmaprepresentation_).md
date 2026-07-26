---
title: 'init(bitmapRepresentation:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscharacterset/init(bitmaprepresentation:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscharacterset/init(bitmaprepresentation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscharacterset/init%28bitmaprepresentation%3A%29.json'
content_hash: 'sha256:83021d85437ddcc9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCharacterSet](../nscharacterset.md)

# init(bitmapRepresentation:)

<sub>Initializer</sub>

Returns a character set containing characters determined by a given bitmap representation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(bitmapRepresentation data: Data)
```

## Parameters

- `data` — A bitmap representation of a character set.

## Return Value

A character set containing characters determined by `data`.

## Discussion

This method is useful for creating a character set object with data from a file or other external data source.

A raw bitmap representation of a character set is a byte array with the first 2^16 bits (that is, 8192 bytes) representing the code point range of the the Basic Multilingual Plane (BMP), such that the value of the bit at position n represents the presence in the character set of the character with decimal Unicode value n. A bitmap representation may contain zero to sixteen additional 8192 byte segments to for each additional Unicode plane containing a character in a character set, with each 8192 byte segment prepended with a single plane index byte.

To add a character in the Basic Multilingual Plane (BMP) with decimal Unicode value n to a raw bitmap representation, you might do the following:

```objc
unsigned char bitmapRep[8192];
bitmapRep[n >> 3] |= (((unsigned int)1) << (n & 7));
```

To remove that character:

```objc
bitmapRep[n >> 3] &= ~(((unsigned int)1) << (n & 7));
```

## See Also

### Creating and Managing Character Sets as Bitmap Representations

- [+ characterSetWithContentsOfFile:](<init(contentsoffile_).md>) — Returns a character set read from the bitmap representation stored in the file a given path.
- [bitmapRepresentation](bitmaprepresentation.md) — An `NSData` object encoding the receiver in binary format.
