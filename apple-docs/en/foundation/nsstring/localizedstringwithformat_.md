---
title: 'localizedStringWithFormat:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstring/localizedstringwithformat:'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/localizedstringwithformat:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/localizedstringwithformat%3A.json'
content_hash: 'sha256:24cf0c33dc9667ed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# localizedStringWithFormat:

<sub>Type Method</sub>

Returns a string created by using a given format string as a template into which the remaining argument values are substituted according to the current locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) localizedStringWithFormat:(NSString *) format;
```

## Parameters

- `format` — A format string. See [Formatting String Objects](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/Articles/FormatStrings.html#//apple_ref/doc/uid/20000943) for examples of how to use this method, and [String Format Specifiers](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFStrings/formatSpecifiers.html#//apple_ref/doc/uid/TP40004265) for a list of format specifiers. This value must not be `nil`. Raises an `NSInvalidArgumentException` if `format` is `nil`.

## Return Value

A string created by using `format` as a template into which the following argument values are substituted according to the formatting information in the current locale.

## Discussion

Pass a comma-separated list of variadic arguments to substitute into `format`.

This method is equivalent to using [initWithFormat:locale:](initwithformat_locale_.md) and passing the current locale as the locale argument.

As an example of formatting, this method replaces the decimal according to the locale in `%f` and `%d` substitutions, and calls [- descriptionWithLocale:](<../nsnumber/description(withlocale_).md>) instead of [description()](<../../objectivec/nsobject-swift.class/description().md>) where necessary.

This code excerpt creates a string from another string and a float:

```objc
NSString *myString = [NSString localizedStringWithFormat:@"%@:  %f\n", @"Cost", 1234.56];
```

The resulting string has the value “`Cost: 1234.560000\n`” if the locale is `en_US`, and “`Cost: 1234,560000\n`” if the locale is `fr_FR`.

See [Formatting String Objects](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/Articles/FormatStrings.html#//apple_ref/doc/uid/20000943) for more information.

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
- [+ localizedUserNotificationStringForKey:arguments:](<localizedusernotificationstring(forkey_arguments_).md>) — Returns a localized string intended for display in a notification alert.
- [stringWithCharacters:length:](stringwithcharacters_length_.md) — Returns a string containing a given number of characters taken from a given C array of UTF-16 code units.
