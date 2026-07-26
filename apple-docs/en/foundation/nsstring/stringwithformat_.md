---
title: 'stringWithFormat:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstring/stringwithformat:'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/stringwithformat:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/stringwithformat%3A.json'
content_hash: 'sha256:79e29cecd78279a5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# stringWithFormat:

<sub>Type Method</sub>

Returns a string created by using a given format string as a template into which the remaining argument values are substituted.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) stringWithFormat:(NSString *) format;
```

## Parameters

- `format` — A format string. See [Formatting String Objects](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/Articles/FormatStrings.html#//apple_ref/doc/uid/20000943) for examples of how to use this method, and [String Format Specifiers](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFStrings/formatSpecifiers.html#//apple_ref/doc/uid/TP40004265) for a list of format specifiers. This value must not be `nil`. > [!important] Important > Raises an `NSInvalidArgumentException` if `format` is `nil`.

## Return Value

A string created by using `format` as a template into which the remaining argument values are substituted without any localization.

## Discussion

Pass a comma-separated list of trailing variadic arguments to substitute into `format`.

This method invokes [- initWithFormat:locale:arguments:](<init(format_locale_arguments_).md>) without applying any localization. This is useful, for example, when working with fixed-format representations of information that is written out and read back in at a later time.

> [!important] Important
> When working with text that’s presented to the user, use the [localizedStringWithFormat:](localizedstringwithformat_.md) method, or the [initWithFormat:locale:](initwithformat_locale_.md) or [- initWithFormat:locale:arguments:](<init(format_locale_arguments_).md>) method, passing [currentLocale](../nslocale/current.md) as the locale.

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
- [localizedStringWithFormat:](localizedstringwithformat_.md) — Returns a string created by using a given format string as a template into which the remaining argument values are substituted according to the current locale.
- [+ localizedUserNotificationStringForKey:arguments:](<localizedusernotificationstring(forkey_arguments_).md>) — Returns a localized string intended for display in a notification alert.
- [stringWithCharacters:length:](stringwithcharacters_length_.md) — Returns a string containing a given number of characters taken from a given C array of UTF-16 code units.
