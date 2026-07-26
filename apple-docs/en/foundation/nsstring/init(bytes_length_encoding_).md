---
title: 'init(bytes:length:encoding:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstring/init(bytes:length:encoding:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/init(bytes:length:encoding:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/init%28bytes%3Alength%3Aencoding%3A%29.json'
content_hash: 'sha256:6499eecc0b008c0f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# init(bytes:length:encoding:)

<sub>Initializer</sub>

Returns an initialized `NSString` object containing a given number of bytes from a given buffer of bytes interpreted in a given encoding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init?(bytes: UnsafeRawPointer, length len: Int, encoding: UInt)
```

## Parameters

- `bytes` — A buffer of bytes interpreted in the encoding specified by `encoding`.

- `len` — The number of bytes to use from `bytes`.

- `encoding` — The character encoding applied to `bytes`. For possible values, see [NSStringEncoding](../nsstringencoding.md).

## Return Value

An initialized `NSString` object containing `length` bytes from `bytes` interpreted using the encoding `encoding`. The returned object may be different from the original receiver. The return byte strings are allowed to be unterminated. If the length of the byte string is greater than the specified length a `nil` value is returned.

## See Also

### Creating and Initializing Strings

- [- init](<init().md>) — Returns an initialized `NSString` object that contains no characters.
- [- initWithBytesNoCopy:length:encoding:freeWhenDone:](<init(bytesnocopy_length_encoding_freewhendone_).md>) — Returns an initialized `NSString` object that contains a given number of bytes from a given buffer of bytes interpreted in a given encoding, and optionally frees the buffer.
- [- initWithCharacters:length:](<init(characters_length_).md>) — Returns an initialized `NSString` object that contains a given number of characters from a given C array of UTF-16 code units.
- [- initWithCharactersNoCopy:length:freeWhenDone:](<init(charactersnocopy_length_freewhendone_).md>) — Returns an initialized `NSString` object that contains a given number of characters from a given C array of UTF-16 code units.
- [- initWithString:](<init(string_)-210xa.md>) — Returns an `NSString` object initialized by copying the characters from another given string.
- [- initWithFormat:arguments:](<init(format_arguments_).md>) — Returns an `NSString` object initialized by using a given format string as a template into which the remaining argument values are substituted without any localization.
- [- initWithFormat:locale:arguments:](<init(format_locale_arguments_).md>) — Returns an `NSString` object initialized by using a given format string as a template into which the remaining argument values are substituted according to given locale information. This method is meant to be called from within a variadic function, where the argument list will be available.
- [- initWithData:encoding:](<init(data_encoding_).md>) — Returns an `NSString` object initialized by converting given data into UTF-16 code units using a given encoding.
- [+ localizedUserNotificationStringForKey:arguments:](<localizedusernotificationstring(forkey_arguments_).md>) — Returns a localized string intended for display in a notification alert.
- [localizedStringWithFormat(_:_:)](<localizedstringwithformat(____).md>)
- [unichar](../unichar.md) — Type for UTF-16 code units.
