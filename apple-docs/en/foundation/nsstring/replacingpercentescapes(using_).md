---
title: 'replacingPercentEscapes(using:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（9.0 起废弃）, iPadOS 2.0+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.11 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsstring/replacingpercentescapes(using:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/replacingpercentescapes(using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/replacingpercentescapes%28using%3A%29.json'
content_hash: 'sha256:73fe3c2a79fb2bfd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# replacingPercentEscapes(using:)

<sub>Instance Method</sub>

Returns a new string made by replacing in the receiver all percent escapes with the matching characters as determined by a given encoding.

> [!warning] Deprecated
> Use [stringByRemovingPercentEncoding](removingpercentencoding.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func replacingPercentEscapes(using enc: UInt) -> String?
```

## Parameters

- `enc` — The encoding to use for the returned string.

## Return Value

A new string made by replacing in the receiver all percent escapes with the matching characters as determined by the given encoding `encoding`. Returns `nil` if the transformation is not possible, for example, the percent escapes give a byte sequence not legal in `encoding`.

## Discussion

See [CFURLCreateStringByReplacingPercentEscapes(_:_:_:)](<../../corefoundation/cfurlcreatestringbyreplacingpercentescapes(______).md>) for more complex transformations.

## See Also

### Related Documentation

- [- stringByAddingPercentEncodingWithAllowedCharacters:](<addingpercentencoding(withallowedcharacters_).md>) — Returns a new string made from the receiver by replacing all characters not in the specified set with percent-encoded characters.
- [stringByRemovingPercentEncoding](removingpercentencoding.md) — Returns a new string made from the receiver by replacing all percent encoded sequences with the matching UTF-8 characters.

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
- [- cStringLength](<cstringlength().md>) — Returns the length in char-sized units of the receiver’s C-string representation in the default C-string encoding. _(deprecated)_
