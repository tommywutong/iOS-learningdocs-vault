---
title: 'getCharacters(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsstring/getcharacters(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/getcharacters(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/getcharacters%28_%3A%29.json'
content_hash: 'sha256:fd0f110bc183b272'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# getCharacters(_:)

<sub>Instance Method</sub>

Copies all characters from the receiver into a given buffer.

> [!warning] Deprecated
> This method is unsafe because it could potentially cause buffer overruns. Use [- getCharacters:range:](<getcharacters(__range_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func getCharacters(_ buffer: UnsafeMutablePointer<unichar>)
```

## Parameters

- `buffer` — Upon return, contains the characters from the receiver. `buffer` must be large enough to contain all characters in the string (`[string length]*sizeof(unichar)`).

## Discussion

Invokes [- getCharacters:range:](<getcharacters(__range_).md>) with `buffer` and the entire extent of the receiver as the range.

## See Also

### Related Documentation

- [length](length.md) — The number of UTF-16 code units in the receiver.

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
- [- cString](<cstring().md>) — Returns a representation of the receiver as a C string in the default C-string encoding. _(deprecated)_
- [- lossyCString](<lossycstring().md>) — Returns a representation of the receiver as a C string in the default C-string encoding, possibly losing information in converting to that encoding. _(deprecated)_
- [- cStringLength](<cstringlength().md>) — Returns the length in char-sized units of the receiver’s C-string representation in the default C-string encoding. _(deprecated)_
- [- getCString:](<getcstring(__).md>) — Invokes [- getCString:maxLength:range:remainingRange:](<getcstring(__maxlength_range_remaining_).md>) with `NSMaximumStringLength` as the maximum length, the receiver’s entire extent as the range, and `NULL` for the remaining range. _(deprecated)_
