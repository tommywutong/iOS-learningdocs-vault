---
title: 'write(to:atomically:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（2.0 起废弃）, iPadOS 2.0+（2.0 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsstring/write(to:atomically:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/write(to:atomically:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/write%28to%3Aatomically%3A%29.json'
content_hash: 'sha256:bb7917036fb64d54'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# write(to:atomically:)

<sub>Instance Method</sub>

Writes the contents of the receiver to the location specified by a given URL.

> [!warning] Deprecated
> Use [- writeToURL:atomically:encoding:error:](<write(to_atomically_encoding_).md>) instead.

<sub>tvOS, visionOS, watchOS</sub>

```swift
func write(to url: URL, atomically: Bool) -> Bool
```

## Return Value

[true](../../swift/true.md) if the location is written successfully, otherwise [false](../../swift/false.md).

## Discussion

If `atomically` is [true](../../swift/true.md), the receiver is written to an auxiliary location, and then the auxiliary location is renamed to `aURL`. If `atomically` is [false](../../swift/false.md), the receiver is written directly to `aURL`. The [true](../../swift/true.md) option guarantees that `aURL`, if it exists at all, won’t be corrupted even if the system should crash during writing.

The `atomically` parameter is ignored if `aURL` is not of a type that can be accessed atomically.

## See Also

### Related Documentation

- [- writeToURL:atomically:encoding:error:](<write(to_atomically_encoding_).md>) — Writes the contents of the receiver to the URL specified by `url` using the specified encoding.

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
- [- writeToFile:atomically:](<write(tofile_atomically_).md>) — Writes the contents of the receiver to the file specified by a given path. _(deprecated)_
- [- getCharacters:](<getcharacters(__).md>) — Copies all characters from the receiver into a given buffer. _(deprecated)_
- [- cString](<cstring().md>) — Returns a representation of the receiver as a C string in the default C-string encoding. _(deprecated)_
- [- lossyCString](<lossycstring().md>) — Returns a representation of the receiver as a C string in the default C-string encoding, possibly losing information in converting to that encoding. _(deprecated)_
- [- cStringLength](<cstringlength().md>) — Returns the length in char-sized units of the receiver’s C-string representation in the default C-string encoding. _(deprecated)_
- [- getCString:](<getcstring(__).md>) — Invokes [- getCString:maxLength:range:remainingRange:](<getcstring(__maxlength_range_remaining_).md>) with `NSMaximumStringLength` as the maximum length, the receiver’s entire extent as the range, and `NULL` for the remaining range. _(deprecated)_
