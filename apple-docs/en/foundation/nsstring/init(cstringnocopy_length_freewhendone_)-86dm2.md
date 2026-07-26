---
title: 'init(CStringNoCopy:length:freeWhenDone:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+（2.0 起废弃）, iPadOS 2.0+（2.0 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsstring/init(cstringnocopy:length:freewhendone:)-86dm2'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/init(cstringnocopy:length:freewhendone:)-86dm2'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/init%28cstringnocopy%3Alength%3Afreewhendone%3A%29-86dm2.json'
content_hash: 'sha256:524348f7c5a1ffd0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# init(CStringNoCopy:length:freeWhenDone:)

<sub>Initializer</sub>

Initializes the receiver, a newly allocated `NSString` object, by converting the data in a given C-string from the default C-string encoding into the Unicode character encoding.

> [!warning] Deprecated
> Use [- initWithBytesNoCopy:length:encoding:freeWhenDone:](<init(bytesnocopy_length_encoding_freewhendone_).md>) instead.

<sub>tvOS, visionOS, watchOS</sub>

```swift
convenience init?(CStringNoCopy bytes: UnsafeMutablePointer<CChar>, length: Int, freeWhenDone freeBuffer: Bool)
```

## Discussion

This method converts `length` * `sizeof(char)` bytes from `cString` and doesn’t stop short at a zero character. `cString` must contain data in the default C-string encoding and may not be `NULL`. The receiver becomes the owner of `cString`; if `flag` is [true](../../swift/true.md) it will free the memory when it no longer needs it, but if `flag` is [false](../../swift/false.md) it won’t. Returns an initialized object, which might be different from the original receiver.

You can use this method to create an immutable string from an immutable (`const char *`) C-string buffer. If you receive a warning message, you can disregard it; its purpose is simply to warn you that the C string passed as the method’s first argument may be modified. If you make certain the `freeWhenDone` argument to `initWithStringNoCopy` is [false](../../swift/false.md), the C string passed as the method’s first argument cannot be modified, so you can safely use `initWithStringNoCopy` to create an immutable string from an immutable (`const char *`) C-string buffer.

## See Also

### Deprecated

- [+ stringWithCString:](<string(withcstring_).md>) — Creates a new string using a given C-string. _(deprecated)_
- [init(CString:)](<init(cstring_)-vkuo.md>) — Initializes the receiver, a newly allocated `NSString` object, by converting the data in a given C-string from the default C-string encoding into the Unicode character encoding. _(deprecated)_
- [+ stringWithCString:length:](<string(withcstring_length_).md>) — Returns a string containing the characters in a given C-string. _(deprecated)_
- [init(CString:length:)](<init(cstring_length_)-5ure3.md>) — Initializes the receiver, a newly allocated `NSString` object, by converting the data in a given C-string from the default C-string encoding into the Unicode character encoding. _(deprecated)_
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
- [- getCString:](<getcstring(__).md>) — Invokes [- getCString:maxLength:range:remainingRange:](<getcstring(__maxlength_range_remaining_).md>) with `NSMaximumStringLength` as the maximum length, the receiver’s entire extent as the range, and `NULL` for the remaining range. _(deprecated)_
