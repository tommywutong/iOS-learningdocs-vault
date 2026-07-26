---
title: 'init(format:locale:arguments:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstring/init(format:locale:arguments:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/init(format:locale:arguments:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/init%28format%3Alocale%3Aarguments%3A%29.json'
content_hash: 'sha256:00a9b7b8404b99c2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# init(format:locale:arguments:)

<sub>Initializer</sub>

Returns an `NSString` object initialized by using a given format string as a template into which the remaining argument values are substituted according to given locale information. This method is meant to be called from within a variadic function, where the argument list will be available.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(format: String, locale: Any?, arguments argList: CVaListPointer)
```

## Parameters

- `format` — A format string. See [Formatting String Objects](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/Articles/FormatStrings.html#//apple_ref/doc/uid/20000943) for examples of how to use this method, and [String Format Specifiers](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFStrings/formatSpecifiers.html#//apple_ref/doc/uid/TP40004265) for a list of format specifiers. This value must not be `nil`. > [!important] Important > Raises an `NSInvalidArgumentException` if `format` is `nil`.

- `locale` — An [NSLocale](../nslocale.md) object specifying the locale to use. To use the current locale (specified by user preferences), pass [[NSLocale](../nslocale.md) [currentLocale](../nslocale/current.md)]. To use the system locale, pass `nil`. For legacy support, this may be an instance of `NSDictionary` containing locale information.

- `argList` — A list of arguments to substitute into `format`.

## Return Value

An `NSString` object initialized by using `format` as a template into which values in `argList` are substituted according the locale information in `locale`. The returned object may be different from the original receiver.

## Discussion

The following Objective-C code fragment illustrates how to create a string from `myArgs`, which is derived from a string object with the value “Cost:” and an int with the value 32:

```objc
va_list myArgs;
 
NSString *myString = [[NSString alloc] initWithFormat:@"%@: %d\n"
                                               locale:[NSLocale currentLocale]
                                            arguments:myArgs];
```

The resulting string has the value “`Cost: 32\n`”.

See [String Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/introStrings.html#//apple_ref/doc/uid/10000035i) for more information.

## See Also

### Creating and Initializing Strings

- [- init](<init().md>) — Returns an initialized `NSString` object that contains no characters.
- [- initWithBytes:length:encoding:](<init(bytes_length_encoding_).md>) — Returns an initialized `NSString` object containing a given number of bytes from a given buffer of bytes interpreted in a given encoding.
- [- initWithBytesNoCopy:length:encoding:freeWhenDone:](<init(bytesnocopy_length_encoding_freewhendone_).md>) — Returns an initialized `NSString` object that contains a given number of bytes from a given buffer of bytes interpreted in a given encoding, and optionally frees the buffer.
- [- initWithCharacters:length:](<init(characters_length_).md>) — Returns an initialized `NSString` object that contains a given number of characters from a given C array of UTF-16 code units.
- [- initWithCharactersNoCopy:length:freeWhenDone:](<init(charactersnocopy_length_freewhendone_).md>) — Returns an initialized `NSString` object that contains a given number of characters from a given C array of UTF-16 code units.
- [- initWithString:](<init(string_)-210xa.md>) — Returns an `NSString` object initialized by copying the characters from another given string.
- [- initWithFormat:arguments:](<init(format_arguments_).md>) — Returns an `NSString` object initialized by using a given format string as a template into which the remaining argument values are substituted without any localization.
- [- initWithData:encoding:](<init(data_encoding_).md>) — Returns an `NSString` object initialized by converting given data into UTF-16 code units using a given encoding.
- [+ localizedUserNotificationStringForKey:arguments:](<localizedusernotificationstring(forkey_arguments_).md>) — Returns a localized string intended for display in a notification alert.
- [localizedStringWithFormat(_:_:)](<localizedstringwithformat(____).md>)
- [unichar](../unichar.md) — Type for UTF-16 code units.
