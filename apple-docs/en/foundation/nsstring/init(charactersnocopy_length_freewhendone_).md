---
title: 'init(charactersNoCopy:length:freeWhenDone:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstring/init(charactersnocopy:length:freewhendone:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/init(charactersnocopy:length:freewhendone:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/init%28charactersnocopy%3Alength%3Afreewhendone%3A%29.json'
content_hash: 'sha256:b3eb33318310710c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# init(charactersNoCopy:length:freeWhenDone:)

<sub>Initializer</sub>

Returns an initialized `NSString` object that contains a given number of characters from a given C array of UTF-16 code units.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(charactersNoCopy characters: UnsafeMutablePointer<unichar>, length: Int, freeWhenDone freeBuffer: Bool)
```

## Parameters

- `characters` — A C array of UTF-16 code units.

- `length` — The number of characters to use from `characters`.

- `freeBuffer` — If [true](../../swift/true.md), the receiver releases the memory with `free()` when it no longer needs the data; if [false](../../swift/false.md) it won’t.

## Return Value

An initialized `NSString` object that contains `length` characters from `characters`. The returned object may be different from the original receiver.

## Discussion

If an error occurs during the creation of the string, then `bytes` is not freed even if `flag` is [true](../../swift/true.md). In this case, the caller is responsible for freeing the buffer. This allows the caller to continue trying to create a string with the buffer, without having the buffer deallocated.

## See Also

### Creating and Initializing Strings

- [- init](<init().md>) — Returns an initialized `NSString` object that contains no characters.
- [- initWithBytes:length:encoding:](<init(bytes_length_encoding_).md>) — Returns an initialized `NSString` object containing a given number of bytes from a given buffer of bytes interpreted in a given encoding.
- [- initWithBytesNoCopy:length:encoding:freeWhenDone:](<init(bytesnocopy_length_encoding_freewhendone_).md>) — Returns an initialized `NSString` object that contains a given number of bytes from a given buffer of bytes interpreted in a given encoding, and optionally frees the buffer.
- [- initWithCharacters:length:](<init(characters_length_).md>) — Returns an initialized `NSString` object that contains a given number of characters from a given C array of UTF-16 code units.
- [- initWithString:](<init(string_)-210xa.md>) — Returns an `NSString` object initialized by copying the characters from another given string.
- [- initWithFormat:arguments:](<init(format_arguments_).md>) — Returns an `NSString` object initialized by using a given format string as a template into which the remaining argument values are substituted without any localization.
- [- initWithFormat:locale:arguments:](<init(format_locale_arguments_).md>) — Returns an `NSString` object initialized by using a given format string as a template into which the remaining argument values are substituted according to given locale information. This method is meant to be called from within a variadic function, where the argument list will be available.
- [- initWithData:encoding:](<init(data_encoding_).md>) — Returns an `NSString` object initialized by converting given data into UTF-16 code units using a given encoding.
- [+ localizedUserNotificationStringForKey:arguments:](<localizedusernotificationstring(forkey_arguments_).md>) — Returns a localized string intended for display in a notification alert.
- [localizedStringWithFormat(_:_:)](<localizedstringwithformat(____).md>)
- [unichar](../unichar.md) — Type for UTF-16 code units.
