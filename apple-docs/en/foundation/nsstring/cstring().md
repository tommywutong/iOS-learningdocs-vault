---
title: cString()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（2.0 起废弃）, iPadOS 2.0+（2.0 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsstring/cstring()
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/cstring()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/cstring%28%29.json'
content_hash: 'sha256:80fb4cd9c8560906'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# cString()

<sub>Instance Method</sub>

Returns a representation of the receiver as a C string in the default C-string encoding.

> [!warning] Deprecated
> Use [- cStringUsingEncoding:](<cstring(using_).md>) or [UTF8String](utf8string.md) instead.

<sub>tvOS, visionOS, watchOS</sub>

```swift
func cString() -> UnsafePointer<CChar>?
```

## Discussion

The returned C string will be automatically freed just as a returned object would be released; your code should copy the C string or use [- getCString:](<getcstring(__).md>) if it needs to store the C string outside of the autorelease context in which the C string is created.

Raises an `NSCharacterConversionException` if the receiver can’t be represented in the default C-string encoding without loss of information. Use [- canBeConvertedToEncoding:](<canbeconverted(to_).md>) if necessary to check whether a string can be losslessly converted to the default C-string encoding. If it can’t, use [- lossyCString](<lossycstring().md>) or [- dataUsingEncoding:allowLossyConversion:](<data(using_allowlossyconversion_).md>) to get a C-string representation with some loss of information.

## See Also

### Related Documentation

- [- cStringUsingEncoding:](<cstring(using_).md>) — Returns a representation of the string as a C string using a given encoding.
- [UTF8String](utf8string.md) — A null-terminated UTF8 representation of the string.
- [- getCString:maxLength:encoding:](<getcstring(__maxlength_encoding_).md>) — Converts the string to a given encoding and stores it in a buffer.

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
- [- lossyCString](<lossycstring().md>) — Returns a representation of the receiver as a C string in the default C-string encoding, possibly losing information in converting to that encoding. _(deprecated)_
- [- cStringLength](<cstringlength().md>) — Returns the length in char-sized units of the receiver’s C-string representation in the default C-string encoding. _(deprecated)_
- [- getCString:](<getcstring(__).md>) — Invokes [- getCString:maxLength:range:remainingRange:](<getcstring(__maxlength_range_remaining_).md>) with `NSMaximumStringLength` as the maximum length, the receiver’s entire extent as the range, and `NULL` for the remaining range. _(deprecated)_
