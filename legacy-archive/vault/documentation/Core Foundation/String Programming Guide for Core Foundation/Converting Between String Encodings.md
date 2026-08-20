---
title: String Programming Guide for Core Foundation
apple_id: 10000131i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreFoundation
published: '2014-02-11'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFStrings/Articles/Converting.html
archived_at: '2026-07-15T07:22:53.454497Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [String Programming Guide for Core Foundation](Introduction%20to%20Strings%20Programming%20Guide%20for%20Core%20Foundation.md)


[Next](Handling%20External%20Representations%20of%20Strings.md)[Previous](Manipulating%20Mutable%20String%20Objects.md)

# Converting Between String Encodings

String objects give you a number of tools for converting between string encodings. Some routines do the actual conversions while others show which encodings are available and help you chose the best encoding for the current situation.

If you want to convert between any two non-Unicode encodings, you can use a `CFString` object as an intermediary. Say you have a string encoded as Windows Latin 1 and you want to encode it as Mac OS Roman. Just convert the string to Unicode first (the `CFString` object), then convert the string’s contents to the desired encoding.

Many of the creation and content-accessing functions described in earlier sections of this document include an encoding parameter typed `CFStringEncoding`. These functions are listed in [Table 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge4doljrgaydsojsfvbuqrcdjfbeksi). To specify the encoding of the source or destination string (depending on whether you’re creating a `CFString` object or accessing its contents), specify the `enum` value for the desired encoding in this parameter when you call one of these functions. Use the `CFStringIsEncodingAvailable` function to test for the availability of an “external” encoding on your system before you call a conversion function.

__Table 1__  Encoding-conversion functions

| Converts to CFString (Unicode) |
| `CFStringCreateWithCString` |
| `CFStringCreateWithCStringNoCopy` |
| `CFStringCreateWithBytes` |
| `CFStringCreateFromExternalRepresentation` |

| Converts from CFString (Unicode) |
| --- |
| `CFStringGetCString` |
| `CFStringGetCStringPtr` |
| `CFStringGetBytes` |
| `CFStringCreateExternalRepresentation` |

A word of caution: not all conversions are guaranteed to be successful. This is particularly true if you are trying to convert a `CFString` object with characters that map to a variety of character sets. For example, let’s say you have a Unicode string that includes ASCII characters and accented Latin characters. You could convert this string to Mac OS Roman but not to Mac OS Japanese. In these cases, you can specify “lossy” conversion using the `CFStringGetBytes` function; this kind of conversion substitutes a “loss” character for each character that cannot be converted. The `CFStringGetBytes` function is described in the next section

Among the string object functions that convert the encodings of characters in `CFString` objects are the two low-level conversion functions, `CFStringGetBytes` and `CFStringCreateWithBytes`. As their names suggest, these functions operate on byte buffers of a known size. In addition to performing encoding conversions, they also handle any special characters in a string (such as a BOM) that makes the string suitable for external representation.

However, the `CFStringGetBytes` function is particularly useful for encoding conversions because it allows the specification of a _loss_ byte. If you specify a character for the loss byte, the function substitutes that character when it cannot convert the Unicode value to the proper character. If you specify 0 for the loss byte, this “lossy conversion” is not allowed and the function returns (indirectly) an partial set of characters when it encounters the first character it cannot convert. All other content-accessing functions of `CFString` disallow lossy conversion.

[Listing 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge4doljrgaytcnryfvbuqrceiffeury) illustrates how `CFStringGetBytes` might be used to convert a string from the system encoding to Windows Latin 1. Note one other feature of the function: it allows you to convert a string into a fixed-size buffer one segment at a time.

__Listing 1__  Converting to a different encoding with CFStringGetBytes

```
CFStringRef str;
CFRange rangeToProcess;

str = CFStringCreateWithCString(NULL, "Hello World", kCFStringEncodingMacRoman);

rangeToProcess = CFRangeMake(0, CFStringGetLength(str));
while (rangeToProcess.length > 0) {
    UInt8 localBuffer[100];
    CFIndex usedBufferLength;
    CFIndex numChars = CFStringGetBytes(str, rangeToProcess, kCFStringEncodingWindowsLatin1, '?', FALSE, (UInt8 *)localBuffer, 100, &usedBufferLength);
    if (numChars == 0) break;   // Failed to convert anything...
    processCharacters(localBuffer, usedBufferLength);
    rangeToProcess.location += numChars;
    rangeToProcess.length -= numChars;
}
```

If the size of the string to convert is relatively small, you can take a different approach with the `CFStringGetBytes` function. With the buffer parameter set to `NULL` you can call the function to find out two things. If the function result is greater than 0 conversion is possible. And, if conversion is possible, the last parameter (_usedBufLen_) will contain the number of bytes required for the conversion. With this information you can allocate a buffer of the needed size and convert the string at one shot into the desired encoding. However, if the string is large this technique has its drawbacks; asking for the length could be expensive and the allocation could require a lot of memory.

Besides the functions that convert between encodings, string objects offer a number of functions that can help you to find out which encodings are available and, of these, which are the best to use in your code.

The `CFStringGetSmallestEncoding` function determines the smallest encoding that can be used on a particular system (smallest in terms of bytes needed to represent one character). The `CFStringGetFastestEncoding` function gets the encoding on the current system with the fastest conversion time from Unicode. The `CFStringGetSystemEncoding` function obtains the encoding used by strings generated by the operating system.

Use the `CFStringIsEncodingAvailable` and `CFStringGetListOfAvailableEncodings` functions to obtain information about encodings available on your system.

You can use the `CFStringConvertEncodingToWindowsCodepage` and `CFStringConvertWindowsCodepageToEncoding` functions to convert between Windows codepage numbers and `CFStringEncoding` values. Similar sets of functions exist for Cocoa NSString encoding constants and IANA “charset” identifiers used by MIME encodings.

Core Foundation string objects supports conversions between Unicode encodings of CFString objects and a wide range of international, national, and industry encodings. Supported encodings come in two sets, an “internal” set defined in `CFString.h` by the `CFStringBuiltInEncodings``enum`, and an “external” set defined in `CFStringEncodingExt.h` by the `CFStringEncodings``enum`. The encodings in the internal set are guaranteed to be available on all platforms for conversions to and from CFString objects. The built-in encodings (as designated by the constant names in `CFStringBuiltInEncodings`) include:

- `kCFStringEncodingMacRoman`
- `kCFStringEncodingWindowsLatin1`
- `kCFStringEncodingISOLatin1`
- `kCFStringEncodingNextStepLatin`
- `kCFStringEncodingASCII`
- `kCFStringEncodingUnicode`
- `kCFStringEncodingUTF8`
- `kCFStringEncodingNonLossyASCII`
- `kCFStringEncodingUTF16`
- `kCFStringEncodingUTF16BE`
- `kCFStringEncodingUTF32`

Conversions using the encodings in the external set are possible only if the underlying system supports the encodings.

[Next](Handling%20External%20Representations%20of%20Strings.md)[Previous](Manipulating%20Mutable%20String%20Objects.md)

