---
title: 'stringWithString:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstring/stringwithstring:'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/stringwithstring:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/stringwithstring%3A.json'
content_hash: 'sha256:627513947c1390c2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# stringWithString:

<sub>Type Method</sub>

Returns a string created by copying the characters from another given string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) stringWithString:(NSString *) string;
```

## Parameters

- `string` — The string from which to copy characters. This value must not be `nil`. > [!important] Important > Raises an `NSInvalidArgumentException` if `aString` is `nil`.

## Return Value

A string created by copying the characters from `aString`.

## See Also

### Creating and Initializing Strings

- [string](string.md) — Returns an empty string.
- [- init](<init().md>) — Returns an initialized `NSString` object that contains no characters.
- [- initWithBytes:length:encoding:](<init(bytes_length_encoding_).md>) — Returns an initialized `NSString` object containing a given number of bytes from a given buffer of bytes interpreted in a given encoding.
- [- initWithBytesNoCopy:length:encoding:freeWhenDone:](<init(bytesnocopy_length_encoding_freewhendone_).md>) — Returns an initialized `NSString` object that contains a given number of bytes from a given buffer of bytes interpreted in a given encoding, and optionally frees the buffer.
- [- initWithCharacters:length:](<init(characters_length_).md>) — Returns an initialized `NSString` object that contains a given number of characters from a given C array of UTF-16 code units.
- [- initWithCharactersNoCopy:length:freeWhenDone:](<init(charactersnocopy_length_freewhendone_).md>) — Returns an initialized `NSString` object that contains a given number of characters from a given C array of UTF-16 code units.
- [- initWithString:](<init(string_)-210xa.md>) — Returns an `NSString` object initialized by copying the characters from another given string.
- [initWithFormat:](initwithformat_.md) — Returns an `NSString` object initialized by using a given format string as a template into which the remaining argument values are substituted.
- [- initWithFormat:arguments:](<init(format_arguments_).md>) — Returns an `NSString` object initialized by using a given format string as a template into which the remaining argument values are substituted without any localization.
- [initWithFormat:locale:](initwithformat_locale_.md) — Returns an `NSString` object initialized by using a given format string as a template into which the remaining argument values are substituted according to given locale.
- [- initWithFormat:locale:arguments:](<init(format_locale_arguments_).md>) — Returns an `NSString` object initialized by using a given format string as a template into which the remaining argument values are substituted according to given locale information. This method is meant to be called from within a variadic function, where the argument list will be available.
- [- initWithData:encoding:](<init(data_encoding_).md>) — Returns an `NSString` object initialized by converting given data into UTF-16 code units using a given encoding.
- [stringWithFormat:](stringwithformat_.md) — Returns a string created by using a given format string as a template into which the remaining argument values are substituted.
- [localizedStringWithFormat:](localizedstringwithformat_.md) — Returns a string created by using a given format string as a template into which the remaining argument values are substituted according to the current locale.
- [+ localizedUserNotificationStringForKey:arguments:](<localizedusernotificationstring(forkey_arguments_).md>) — Returns a localized string intended for display in a notification alert.
