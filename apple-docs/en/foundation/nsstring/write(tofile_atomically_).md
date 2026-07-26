---
title: 'write(toFile:atomically:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（2.0 起废弃）, iPadOS 2.0+（2.0 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsstring/write(tofile:atomically:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/write(tofile:atomically:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/write%28tofile%3Aatomically%3A%29.json'
content_hash: 'sha256:d67cf5e44b88e721'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# write(toFile:atomically:)

<sub>Instance Method</sub>

Writes the contents of the receiver to the file specified by a given path.

> [!warning] Deprecated
> Use [- writeToFile:atomically:encoding:error:](<write(tofile_atomically_encoding_).md>) instead.

<sub>tvOS, visionOS, watchOS</sub>

```swift
func write(toFile path: String, atomically useAuxiliaryFile: Bool) -> Bool
```

## Return Value

[true](../../swift/true.md) if the file is written successfully, otherwise [false](../../swift/false.md).

## Discussion

Writes the contents of the receiver to the file specified by `path` (overwriting any existing file at `path`). `path` is written in the default C-string encoding if possible (that is, if no information would be lost), in the Unicode encoding otherwise.

If `flag` is [true](../../swift/true.md), the receiver is written to an auxiliary file, and then the auxiliary file is renamed to `path`. If `flag` is [false](../../swift/false.md), the receiver is written directly to `path`. The [true](../../swift/true.md) option guarantees that `path`, if it exists at all, won’t be corrupted even if the system should crash during writing.

If `path` contains a tilde (`~`) character, you must expand it with [stringByExpandingTildeInPath](expandingtildeinpath.md) before invoking this method.

## See Also

### Related Documentation

- [- writeToFile:atomically:encoding:error:](<write(tofile_atomically_encoding_).md>) — Writes the contents of the receiver to a file at a given path using a given encoding.

### Deprecated

- [+ stringWithCString:](<string(withcstring_).md>) — Creates a new string using a given C-string. _(deprecated)_
- [init(CString:)](<init(cstring_)-vkuo.md>) — Initializes the receiver, a newly allocated `NSString` object, by converting the data in a given C-string from the default C-string encoding into the Unicode character encoding. _(deprecated)_
- [+ stringWithCString:length:](<string(withcstring_length_).md>) — Returns a string containing the characters in a given C-string. _(deprecated)_
- [init(CString:length:)](<init(cstring_length_)-5ure3.md>) — Initializes the receiver, a newly allocated `NSString` object, by converting the data in a given C-string from the default C-string encoding into the Unicode character encoding. _(deprecated)_
- [init(CStringNoCopy:length:freeWhenDone:)](<init(cstringnocopy_length_freewhendone_)-86dm2.md>) — Initializes the receiver, a newly allocated `NSString` object, by converting the data in a given C-string from the default C-string encoding into the Unicode character encoding. _(deprecated)_
- [+ stringWithContentsOfFile:](<string(withcontentsoffile_).md>) — Returns a string created by reading data from the file named by a given path. _(deprecated)_
- [- initWithContentsOfFile:](<init(contentsoffile_).md>) — Initializes the receiver, a newly allocated `NSString` object, by reading data from the file named by `path`. _(deprecated)_
- [+ stringWithContentsOfURL:](<string(withcontentsof_).md>) — Returns a string created by reading data from the file named by a given URL. _(deprecated)_
- [init(contentsOfURL:)](<init(contentsofurl_).md>) — Initializes the receiver, a newly allocated `NSString` object, by reading data from the location named by a given URL. _(deprecated)_
- [- writeToURL:atomically:](<write(to_atomically_).md>) — Writes the contents of the receiver to the location specified by a given URL. _(deprecated)_
- [- getCharacters:](<getcharacters(__).md>) — Copies all characters from the receiver into a given buffer. _(deprecated)_
- [- cString](<cstring().md>) — Returns a representation of the receiver as a C string in the default C-string encoding. _(deprecated)_
- [- lossyCString](<lossycstring().md>) — Returns a representation of the receiver as a C string in the default C-string encoding, possibly losing information in converting to that encoding. _(deprecated)_
- [- cStringLength](<cstringlength().md>) — Returns the length in char-sized units of the receiver’s C-string representation in the default C-string encoding. _(deprecated)_
- [- getCString:](<getcstring(__).md>) — Invokes [- getCString:maxLength:range:remainingRange:](<getcstring(__maxlength_range_remaining_).md>) with `NSMaximumStringLength` as the maximum length, the receiver’s entire extent as the range, and `NULL` for the remaining range. _(deprecated)_
