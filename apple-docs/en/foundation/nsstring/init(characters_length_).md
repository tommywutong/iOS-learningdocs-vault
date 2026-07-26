---
title: 'init(characters:length:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstring/init(characters:length:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/init(characters:length:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/init%28characters%3Alength%3A%29.json'
content_hash: 'sha256:76c814961e1b9101'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# init(characters:length:)

<sub>Initializer</sub>

Returns an initialized `NSString` object that contains a given number of characters from a given C array of UTF-16 code units.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(characters: UnsafePointer<unichar>, length: Int)
```

## Parameters

- `characters` — A C array of UTF-16 code units; the value must not be `NULL`. > [!important] Important > Raises an exception if `characters` is `NULL`, even if `length` is `0`.

- `length` — The number of characters to use from `characters`.

## Return Value

An initialized `NSString` object containing `length` characters taken from `characters`. The returned object may be different from the original receiver.

## See Also

### Creating and Initializing Strings

- [- init](<init().md>) — Returns an initialized `NSString` object that contains no characters.
- [- initWithBytes:length:encoding:](<init(bytes_length_encoding_).md>) — Returns an initialized `NSString` object containing a given number of bytes from a given buffer of bytes interpreted in a given encoding.
- [- initWithBytesNoCopy:length:encoding:freeWhenDone:](<init(bytesnocopy_length_encoding_freewhendone_).md>) — Returns an initialized `NSString` object that contains a given number of bytes from a given buffer of bytes interpreted in a given encoding, and optionally frees the buffer.
- [- initWithCharactersNoCopy:length:freeWhenDone:](<init(charactersnocopy_length_freewhendone_).md>) — Returns an initialized `NSString` object that contains a given number of characters from a given C array of UTF-16 code units.
- [- initWithString:](<init(string_)-210xa.md>) — Returns an `NSString` object initialized by copying the characters from another given string.
- [- initWithFormat:arguments:](<init(format_arguments_).md>) — Returns an `NSString` object initialized by using a given format string as a template into which the remaining argument values are substituted without any localization.
- [- initWithFormat:locale:arguments:](<init(format_locale_arguments_).md>) — Returns an `NSString` object initialized by using a given format string as a template into which the remaining argument values are substituted according to given locale information. This method is meant to be called from within a variadic function, where the argument list will be available.
- [- initWithData:encoding:](<init(data_encoding_).md>) — Returns an `NSString` object initialized by converting given data into UTF-16 code units using a given encoding.
- [+ localizedUserNotificationStringForKey:arguments:](<localizedusernotificationstring(forkey_arguments_).md>) — Returns a localized string intended for display in a notification alert.
- [localizedStringWithFormat(_:_:)](<localizedstringwithformat(____).md>)
- [unichar](../unichar.md) — Type for UTF-16 code units.
