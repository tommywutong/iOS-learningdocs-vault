---
title: cStringLength()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（2.0 起废弃）, iPadOS 2.0+（2.0 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsstring/cstringlength()
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/cstringlength()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/cstringlength%28%29.json'
content_hash: 'sha256:e7b599c3b25b2169'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# cStringLength()

<sub>Instance Method</sub>

Returns the length in char-sized units of the receiver’s C-string representation in the default C-string encoding.

> [!warning] Deprecated
> Use [- lengthOfBytesUsingEncoding:](<lengthofbytes(using_).md>) or [- maximumLengthOfBytesUsingEncoding:](<maximumlengthofbytes(using_).md>) instead.

<sub>tvOS, visionOS, watchOS</sub>

```swift
func cStringLength() -> Int
```

## Discussion

Raises if the receiver can’t be represented in the default C-string encoding without loss of information. You can also use [- canBeConvertedToEncoding:](<canbeconverted(to_).md>) to check whether a string can be losslessly converted to the default C-string encoding. If it can’t, use [- lossyCString](<lossycstring().md>) to get a C-string representation with some loss of information, then check its length explicitly using the ANSI function `strlen()`.

## See Also

### Related Documentation

- [UTF8String](utf8string.md) — A null-terminated UTF8 representation of the string.
- [- maximumLengthOfBytesUsingEncoding:](<maximumlengthofbytes(using_).md>) — Returns the maximum number of bytes needed to store the receiver in a given encoding.
- [- lengthOfBytesUsingEncoding:](<lengthofbytes(using_).md>) — Returns the number of bytes required to store the receiver in a given encoding.

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
- [- writeToURL:atomically:](<write(to_atomically_).md>) — Writes the contents of the receiver to the location specified by a given URL. _(deprecated)_
- [- getCharacters:](<getcharacters(__).md>) — Copies all characters from the receiver into a given buffer. _(deprecated)_
- [- cString](<cstring().md>) — Returns a representation of the receiver as a C string in the default C-string encoding. _(deprecated)_
- [- lossyCString](<lossycstring().md>) — Returns a representation of the receiver as a C string in the default C-string encoding, possibly losing information in converting to that encoding. _(deprecated)_
- [- getCString:](<getcstring(__).md>) — Invokes [- getCString:maxLength:range:remainingRange:](<getcstring(__maxlength_range_remaining_).md>) with `NSMaximumStringLength` as the maximum length, the receiver’s entire extent as the range, and `NULL` for the remaining range. _(deprecated)_
