---
title: 'init(contentsOfFile:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+（2.0 起废弃）, iPadOS 2.0+（2.0 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsstring/init(contentsoffile:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/init(contentsoffile:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/init%28contentsoffile%3A%29.json'
content_hash: 'sha256:9d58103a922adda0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# init(contentsOfFile:)

<sub>Initializer</sub>

Initializes the receiver, a newly allocated `NSString` object, by reading data from the file named by `path`.

> [!warning] Deprecated
> Use [- initWithContentsOfFile:encoding:error:](<init(contentsoffile_encoding_).md>) or [- initWithContentsOfFile:usedEncoding:error:](<init(contentsoffile_usedencoding_).md>) instead.

<sub>tvOS, visionOS, watchOS</sub>

```swift
convenience init?(contentsOfFile path: String)
```

## Discussion

Initializes the receiver, a newly allocated `NSString` object, by reading data from the file named by `path`. If the contents begin with a byte-order mark (`U+FEFF` or `U+FFFE`), interprets the contents as UTF-16 code units; otherwise interprets the contents as data in the default C string encoding. Returns an initialized object, which might be different from the original receiver, or `nil` if the file can’t be opened.

## See Also

### Related Documentation

- [- initWithContentsOfFile:encoding:error:](<init(contentsoffile_encoding_).md>) — Returns an `NSString` object initialized by reading data from the file at a given path using a given encoding.
- [- initWithContentsOfFile:usedEncoding:error:](<init(contentsoffile_usedencoding_).md>) — Returns an `NSString` object initialized by reading data from the file at a given path and returns by reference the encoding used to interpret the characters.

### Deprecated

- [+ stringWithCString:](<string(withcstring_).md>) — Creates a new string using a given C-string. _(deprecated)_
- [init(CString:)](<init(cstring_)-vkuo.md>) — Initializes the receiver, a newly allocated `NSString` object, by converting the data in a given C-string from the default C-string encoding into the Unicode character encoding. _(deprecated)_
- [+ stringWithCString:length:](<string(withcstring_length_).md>) — Returns a string containing the characters in a given C-string. _(deprecated)_
- [init(CString:length:)](<init(cstring_length_)-5ure3.md>) — Initializes the receiver, a newly allocated `NSString` object, by converting the data in a given C-string from the default C-string encoding into the Unicode character encoding. _(deprecated)_
- [init(CStringNoCopy:length:freeWhenDone:)](<init(cstringnocopy_length_freewhendone_)-86dm2.md>) — Initializes the receiver, a newly allocated `NSString` object, by converting the data in a given C-string from the default C-string encoding into the Unicode character encoding. _(deprecated)_
- [+ stringWithContentsOfFile:](<string(withcontentsoffile_).md>) — Returns a string created by reading data from the file named by a given path. _(deprecated)_
- [+ stringWithContentsOfURL:](<string(withcontentsof_).md>) — Returns a string created by reading data from the file named by a given URL. _(deprecated)_
- [init(contentsOfURL:)](<init(contentsofurl_).md>) — Initializes the receiver, a newly allocated `NSString` object, by reading data from the location named by a given URL. _(deprecated)_
- [- writeToFile:atomically:](<write(tofile_atomically_).md>) — Writes the contents of the receiver to the file specified by a given path. _(deprecated)_
- [- writeToURL:atomically:](<write(to_atomically_).md>) — Writes the contents of the receiver to the location specified by a given URL. _(deprecated)_
- [- getCharacters:](<getcharacters(__).md>) — Copies all characters from the receiver into a given buffer. _(deprecated)_
- [- cString](<cstring().md>) — Returns a representation of the receiver as a C string in the default C-string encoding. _(deprecated)_
- [- lossyCString](<lossycstring().md>) — Returns a representation of the receiver as a C string in the default C-string encoding, possibly losing information in converting to that encoding. _(deprecated)_
- [- cStringLength](<cstringlength().md>) — Returns the length in char-sized units of the receiver’s C-string representation in the default C-string encoding. _(deprecated)_
- [- getCString:](<getcstring(__).md>) — Invokes [- getCString:maxLength:range:remainingRange:](<getcstring(__maxlength_range_remaining_).md>) with `NSMaximumStringLength` as the maximum length, the receiver’s entire extent as the range, and `NULL` for the remaining range. _(deprecated)_
