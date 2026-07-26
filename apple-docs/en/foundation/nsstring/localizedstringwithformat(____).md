---
title: 'localizedStringWithFormat(_:_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstring/localizedstringwithformat(_:_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/localizedstringwithformat(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/localizedstringwithformat%28_%3A_%3A%29.json'
content_hash: 'sha256:0f63a0ffefe4c69e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# localizedStringWithFormat(_:_:)

<sub>Type Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func localizedStringWithFormat(_ format: NSString, _ args: any CVarArg...) -> Self
```

## See Also

### Creating and Initializing Strings

- [- init](<init().md>) — Returns an initialized `NSString` object that contains no characters.
- [- initWithBytes:length:encoding:](<init(bytes_length_encoding_).md>) — Returns an initialized `NSString` object containing a given number of bytes from a given buffer of bytes interpreted in a given encoding.
- [- initWithBytesNoCopy:length:encoding:freeWhenDone:](<init(bytesnocopy_length_encoding_freewhendone_).md>) — Returns an initialized `NSString` object that contains a given number of bytes from a given buffer of bytes interpreted in a given encoding, and optionally frees the buffer.
- [- initWithCharacters:length:](<init(characters_length_).md>) — Returns an initialized `NSString` object that contains a given number of characters from a given C array of UTF-16 code units.
- [- initWithCharactersNoCopy:length:freeWhenDone:](<init(charactersnocopy_length_freewhendone_).md>) — Returns an initialized `NSString` object that contains a given number of characters from a given C array of UTF-16 code units.
- [- initWithString:](<init(string_)-210xa.md>) — Returns an `NSString` object initialized by copying the characters from another given string.
- [- initWithFormat:arguments:](<init(format_arguments_).md>) — Returns an `NSString` object initialized by using a given format string as a template into which the remaining argument values are substituted without any localization.
- [- initWithFormat:locale:arguments:](<init(format_locale_arguments_).md>) — Returns an `NSString` object initialized by using a given format string as a template into which the remaining argument values are substituted according to given locale information. This method is meant to be called from within a variadic function, where the argument list will be available.
- [- initWithData:encoding:](<init(data_encoding_).md>) — Returns an `NSString` object initialized by converting given data into UTF-16 code units using a given encoding.
- [+ localizedUserNotificationStringForKey:arguments:](<localizedusernotificationstring(forkey_arguments_).md>) — Returns a localized string intended for display in a notification alert.
- [unichar](../unichar.md) — Type for UTF-16 code units.
