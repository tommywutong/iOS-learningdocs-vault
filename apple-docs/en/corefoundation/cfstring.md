---
title: CFString
framework: Core Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfstring
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstring'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstring.json'
content_hash: 'sha256:652f5d2ff26fc560'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFString

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CFString
```

## Overview

CFString provides a suite of efficient string-manipulation and string-conversion functions. It offers seamless Unicode support and facilitates the sharing of data between Cocoa and C-based programs. CFString objects are immutable—use [CFMutableString](cfmutablestring.md) to create and manage a string that can be changed after it has been created.

CFString has two primitive functions, [CFStringGetLength](<cfstringgetlength(__).md>) and [CFStringGetCharacterAtIndex](<cfstringgetcharacteratindex(____).md>), that provide the basis for all other functions in its interface. The `CFStringGetLength` function returns the total number (in terms of UTF-16 code pairs) of characters in the string. The `CFStringGetCharacterAtIndex` function gives access to each character in the string by index, with index values starting at `0`.

CFString provides functions for finding and comparing strings. It also provides functions for reading numeric values from strings, for combining strings in various ways, and for converting a string to different forms (such as encoding and case changes). A number of functions, for example `CFStringFindWithOptions`, allow you to specify a range over which to operate within a string. The specified range must not exceed the length of the string. Debugging options may help you to catch any errors that arise if a range does exceed a string’s length.

Like other Core Foundation types, you can hash CFStrings using the [CFHash](<cfhash(__).md>) function. You should never, though, store a hash value outside of your application and expect it to be useful if you read it back in later (hash values may change between different releases of the operating system).

CFString is “toll-free bridged” with its Cocoa Foundation counterpart, [NSString](../foundation/nsstring.md). This means that the Core Foundation type is interchangeable in function or method calls with the bridged Foundation object. Therefore, in a method where you see an `NSString *` parameter, you can pass in a `CFStringRef`, and in a function where you see a `CFStringRef` parameter, you can pass in an NSString instance. This also applies to concrete subclasses of NSString. See [Toll-Free Bridged Types](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/Articles/tollFreeBridgedTypes.html#//apple_ref/doc/uid/TP40010677) for more information on toll-free bridging.

## Relationships

- **Inherited By**: [CFMutableString](cfmutablestring.md)

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating a CFString

- [CFStringCreateArrayBySeparatingStrings](<cfstringcreatearraybyseparatingstrings(______).md>) — Creates an array of CFString objects from a single CFString object.
- [CFStringCreateByCombiningStrings](<cfstringcreatebycombiningstrings(______).md>) — Creates a single string from the individual CFString objects that comprise the elements of an array.
- [CFStringCreateCopy](<cfstringcreatecopy(____).md>) — Creates an immutable copy of a string.
- [CFStringCreateFromExternalRepresentation](<cfstringcreatefromexternalrepresentation(______).md>) — Creates a string from its “external representation.”
- [CFStringCreateWithBytes](<cfstringcreatewithbytes(__________).md>) — Creates a string from a buffer containing characters in a specified encoding.
- [CFStringCreateWithBytesNoCopy](<cfstringcreatewithbytesnocopy(____________).md>) — Creates a string from a buffer, containing characters in a specified encoding, that might serve as the backing store for the new string.
- [CFStringCreateWithCharacters](<cfstringcreatewithcharacters(______).md>) — Creates a string from a buffer of Unicode characters.
- [CFStringCreateWithCharactersNoCopy](<cfstringcreatewithcharactersnocopy(________).md>) — Creates a string from a buffer of Unicode characters that might serve as the backing store for the object.
- [CFStringCreateWithCString](<cfstringcreatewithcstring(______).md>) — Creates an immutable string from a C string.
- [CFStringCreateWithCStringNoCopy](<cfstringcreatewithcstringnocopy(________).md>) — Creates a CFString object from an external C string buffer that might serve as the backing store for the object.
- [CFStringCreateWithFormatAndArguments](<cfstringcreatewithformatandarguments(________).md>) — Creates an immutable string from a formatted string and a variable number of arguments (specified in a parameter of type `va_list`).
- [CFStringCreateWithPascalString](<cfstringcreatewithpascalstring(______).md>) — Creates an immutable CFString object from a Pascal string.
- [CFStringCreateWithPascalStringNoCopy](<cfstringcreatewithpascalstringnocopy(________).md>) — Creates a CFString object from an external Pascal string buffer that might serve as the backing store for the object.
- [CFStringCreateWithSubstring](<cfstringcreatewithsubstring(______).md>) — Creates an immutable string from a segment (substring) of an existing string.

### Searching Strings

- [CFStringCreateArrayWithFindResults](<cfstringcreatearraywithfindresults(__________).md>) — Searches a string for multiple occurrences of a substring and creates an array of ranges identifying the locations of these substrings within the target string.
- [CFStringFind](<cfstringfind(______).md>) — Searches for a substring within a string and, if it is found, yields the range of the substring within the object’s characters.
- [CFStringFindCharacterFromSet](<cfstringfindcharacterfromset(__________).md>) — Query the range of the first character contained in the specified character set.
- [CFStringFindWithOptions](<cfstringfindwithoptions(__________).md>) — Searches for a substring within a range of the characters represented by a string and, if the substring is found, returns its range within the object’s characters.
- [CFStringFindWithOptionsAndLocale](<cfstringfindwithoptionsandlocale(____________).md>) — Returns a Boolean value that indicates whether a given string was found in a given source string.
- [CFStringGetLineBounds](<cfstringgetlinebounds(__________).md>) — Given a range of characters in a string, obtains the line bounds—that is, the indexes of the first character and the final characters of the lines containing the range.

### Comparing Strings

- [CFStringCompare](<cfstringcompare(______).md>) — Compares one string with another string.
- [CFStringCompareWithOptions](<cfstringcomparewithoptions(________).md>) — Compares a range of the characters in one string with that of another string.
- [CFStringCompareWithOptionsAndLocale](<cfstringcomparewithoptionsandlocale(__________).md>) — Compares a range of the characters in one string with another string using a given locale.
- [CFStringHasPrefix](<cfstringhasprefix(____).md>) — Determines if the character data of a string begin with a specified sequence of characters.
- [CFStringHasSuffix](<cfstringhassuffix(____).md>) — Determines if a string ends with a specified sequence of characters.

### Accessing Characters

- [CFStringCreateExternalRepresentation](<cfstringcreateexternalrepresentation(________).md>) — Creates an “external representation” of a CFString object, that is, a CFData object.
- [CFStringGetBytes](<cfstringgetbytes(________________).md>) — Fetches a range of the characters from a string into a byte buffer after converting the characters to a specified encoding.
- [CFStringGetCharacterAtIndex](<cfstringgetcharacteratindex(____).md>) — Returns the Unicode character at a specified location in a string.
- [CFStringGetCharacters](<cfstringgetcharacters(______).md>) — Copies a range of the Unicode characters from a string to a user-provided buffer.
- [CFStringGetCharactersPtr](<cfstringgetcharactersptr(__).md>) — Quickly obtains a pointer to the contents of a string as a buffer of Unicode characters.
- [CFStringGetCharacterFromInlineBuffer](<cfstringgetcharacterfrominlinebuffer(____).md>) — Returns the Unicode character at a specific location in an in-line buffer.
- [CFStringGetCString](<cfstringgetcstring(________).md>) — Copies the character contents of a string to a local C string buffer after converting the characters to a given encoding.
- [CFStringGetCStringPtr](<cfstringgetcstringptr(____).md>) — Quickly obtains a pointer to a C-string buffer containing the characters of a string in a given encoding.
- [CFStringGetLength](<cfstringgetlength(__).md>) — Returns the number (in terms of UTF-16 code pairs) of Unicode characters in a string.
- [CFStringGetPascalString](<cfstringgetpascalstring(________).md>) — Copies the character contents of a CFString object to a local Pascal string buffer after converting the characters to a requested encoding.
- [CFStringGetPascalStringPtr](<cfstringgetpascalstringptr(____).md>) — Quickly obtains a pointer to a Pascal buffer containing the characters of a string in a given encoding.
- [CFStringGetRangeOfComposedCharactersAtIndex](<cfstringgetrangeofcomposedcharactersatindex(____).md>) — Returns the range of the composed character sequence at a specified index.
- [CFStringInitInlineBuffer](<cfstringinitinlinebuffer(______).md>) — Initializes an in-line buffer to use for efficient access of a CFString object’s characters.

### Working With Hyphenation

- [CFStringGetHyphenationLocationBeforeIndex](<cfstringgethyphenationlocationbeforeindex(____________).md>) — Retrieve the first potential hyphenation location found before the specified location.
- [CFStringIsHyphenationAvailableForLocale](<cfstringishyphenationavailableforlocale(__).md>) — Returns a Boolean value that indicates whether hyphenation data is available.

### Working With Encodings

- [CFStringConvertEncodingToIANACharSetName](<cfstringconvertencodingtoianacharsetname(__).md>) — Returns the name of the IANA registry “charset” that is the closest mapping to a specified string encoding.
- [CFStringConvertEncodingToNSStringEncoding](<cfstringconvertencodingtonsstringencoding(__).md>) — Returns the Cocoa encoding constant that maps most closely to a given Core Foundation encoding constant.
- [CFStringConvertEncodingToWindowsCodepage](<cfstringconvertencodingtowindowscodepage(__).md>) — Returns the Windows codepage identifier that maps most closely to a given Core Foundation encoding constant.
- [CFStringConvertIANACharSetNameToEncoding](<cfstringconvertianacharsetnametoencoding(__).md>) — Returns the Core Foundation encoding constant that is the closest mapping to a given IANA registry “charset” name.
- [CFStringConvertNSStringEncodingToEncoding](<cfstringconvertnsstringencodingtoencoding(__).md>) — Returns the Core Foundation encoding constant that is the closest mapping to a given Cocoa encoding.
- [CFStringConvertWindowsCodepageToEncoding](<cfstringconvertwindowscodepagetoencoding(__).md>) — Returns the Core Foundation encoding constant that is the closest mapping to a given Windows codepage identifier.
- [CFStringGetFastestEncoding](<cfstringgetfastestencoding(__).md>) — Returns for a CFString object the character encoding that requires the least conversion time.
- [CFStringGetListOfAvailableEncodings](<cfstringgetlistofavailableencodings().md>) — Returns a pointer to a list of string encodings supported by the current system.
- [CFStringGetMaximumSizeForEncoding](<cfstringgetmaximumsizeforencoding(____).md>) — Returns the maximum number of bytes a string of a specified length (in Unicode characters) will take up if encoded in a specified encoding.
- [CFStringGetMostCompatibleMacStringEncoding](<cfstringgetmostcompatiblemacstringencoding(__).md>) — Returns the most compatible Mac OS script value for the given input encoding.
- [CFStringGetNameOfEncoding](<cfstringgetnameofencoding(__).md>) — Returns the canonical name of a specified string encoding.
- [CFStringGetSmallestEncoding](<cfstringgetsmallestencoding(__).md>) — Returns the smallest encoding on the current system for the character contents of a string.
- [CFStringGetSystemEncoding](<cfstringgetsystemencoding().md>) — Returns the default encoding used by the operating system when it creates strings.
- [CFStringIsEncodingAvailable](<cfstringisencodingavailable(__).md>) — Determines whether a given Core Foundation string encoding is available on the current system.

### Getting Numeric Values

- [CFStringGetDoubleValue](<cfstringgetdoublevalue(__).md>) — Returns the primary `double` value represented by a string.
- [CFStringGetIntValue](<cfstringgetintvalue(__).md>) — Returns the integer value represented by a string.

### Getting String Properties

- [CFShowStr](<cfshowstr(__).md>) — Prints the attributes of a string during debugging.
- [CFStringGetTypeID](<cfstringgettypeid().md>) — Returns the type identifier for the CFString opaque type.

### String File System Representations

- [CFStringCreateWithFileSystemRepresentation](<cfstringcreatewithfilesystemrepresentation(____).md>) — Creates a CFString from a zero-terminated POSIX file system representation.
- [CFStringGetFileSystemRepresentation](<cfstringgetfilesystemrepresentation(______).md>) — Extracts the contents of a string as a `NULL`-terminated 8-bit string appropriate for passing to POSIX APIs.
- [CFStringGetMaximumSizeOfFileSystemRepresentation](<cfstringgetmaximumsizeoffilesystemrepresentation(__).md>) — Determines the upper bound on the number of bytes required to hold the file system representation of the string.

### Getting Paragraph Bounds

- [CFStringGetParagraphBounds](<cfstringgetparagraphbounds(__________).md>) — Given a range of characters in a string, obtains the paragraph bounds—that is, the indexes of the first character and the final characters of the paragraph(s) containing the range.

### Managing Surrogates

- [CFStringGetLongCharacterForSurrogatePair](<cfstringgetlongcharacterforsurrogatepair(____).md>) — Returns a UTF-32 character that corresponds to a given pair of UTF-16 surrogate characters.
- [CFStringGetSurrogatePairForLongCharacter](<cfstringgetsurrogatepairforlongcharacter(____).md>) — Maps a given UTF-32 character to a pair of UTF-16 surrogate characters.
- [CFStringIsSurrogateHighCharacter](<cfstringissurrogatehighcharacter(__).md>) — Returns a Boolean value that indicates whether a given character is a high character in a surrogate pair.
- [CFStringIsSurrogateLowCharacter](<cfstringissurrogatelowcharacter(__).md>) — Returns a Boolean value that indicates whether a given character is a low character in a surrogate pair.

### Data Types

- [CFStringEncoding](cfstringencoding.md) — An integer type for constants used to specify supported string encodings in various CFString functions.
- [CFStringEncodings](cfstringencodings.md) — Index type for constants used to specify external string encodings.
- [CFStringCompareFlags](cfstringcompareflags.md) — A [CFOptionFlags](cfoptionflags.md) type for specifying options for string comparison .
- [CFStringInlineBuffer](cfstringinlinebuffer.md) — Defines the buffer and related fields used for in-line buffer access of characters in CFString objects.

### Constants

- [String Comparison Flags](string-comparison-flags.md) — Flags that specify how string comparisons are performed.
- [CFStringBuiltInEncodings](cfstringbuiltinencodings.md) — Encodings that are built-in on all platforms on which macOS runs.
- [Invalid String Encoding Flag](invalid-string-encoding-flag.md) — Special value returned from functions to indicate a string encoding that is not supported or recognized by CFString.
- [External String Encodings](external-string-encodings.md) — `CFStringEncoding` constants for encodings that may be supported by CFString.

## See Also

### Related Documentation

- [Property List Programming Topics for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFPropertyLists/CFPropertyLists.html#//apple_ref/doc/uid/10000130i)
- [Data Formatting Guide for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDataFormatting/Articles/CFDataFormatting.html#//apple_ref/doc/uid/10000176i)
- [String Programming Guide for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFStrings/introCFStrings.html#//apple_ref/doc/uid/10000131i)

### Opaque Types

- [CFAllocator](cfallocator.md)
- [CFArray](cfarray.md)
- [CFAttributedString](cfattributedstring.md)
- [CFBag](cfbag.md)
- [CFBinaryHeap](cfbinaryheap.md)
- [CFBitVector](cfbitvector.md)
- [CFBoolean](cfboolean.md)
- [CFBundle](cfbundle.md)
- [CFCalendar](cfcalendar.md)
- [CFCharacterSet](cfcharacterset.md)
- [CFData](cfdata.md)
- [CFDate](cfdate.md)
- [CFDateFormatter](cfdateformatter.md)
- [CFDictionary](cfdictionary.md)
- [CFError](cferror.md)
