---
title: NSString
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsstring
source_url: 'https://developer.apple.com/documentation/foundation/nsstring'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring.json'
content_hash: 'sha256:54ab99c374fc2a89'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSString

<sub>Class</sub>

A static, plain-text Unicode string object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSString
```

## Overview

You can use this type in Swift when you need reference semantics or other Foundation-specific behavior.

The [NSString](nsstring.md) class and its mutable subclass, [NSMutableString](nsmutablestring.md), provide an extensive set of APIs for working with strings, including methods for comparing, searching, and modifying strings. [NSString](nsstring.md) objects are used throughout Foundation and other Cocoa frameworks, serving as the basis for all textual and linguistic functionality on the platform.

[NSString](nsstring.md) is _toll-free bridged_ with its Core Foundation counterpart, [CFString](../corefoundation/cfstring.md). See [Toll-Free Bridging](https://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2) for more information.

### String Objects

An [NSString](nsstring.md) object encodes a Unicode-compliant text string, represented as a sequence of UTF–16 code units. All lengths, character indexes, and ranges are expressed in terms of 16-bit platform-endian values, with index values starting at `0`.

An [NSString](nsstring.md) object can be initialized from or written to a C buffer, an [NSData](nsdata.md) object, or the contents of an [NSURL](nsurl.md). It can also be encoded and decoded to and from ASCII, UTF–8, UTF–16, UTF–32, or any other string encoding represented by [NSStringEncoding](nsstringencoding.md).

> [!note] Note
> An immutable string is a text string that is defined when it is created and subsequently cannot be changed. An immutable string is implemented as an array of UTF–16 code units (in other words, a text string). To create and manage an immutable string, use the [NSString](nsstring.md) class. To construct and manage a string that can be changed after it has been created, use [NSMutableString](nsmutablestring.md).

The objects you create using [NSString](nsstring.md) and [NSMutableString](nsmutablestring.md) are referred to as string objects (or, when no confusion will result, merely as strings). The term C string refers to the standard `char *` type.

Because of the nature of class clusters, string objects aren’t actual instances of the [NSString](nsstring.md) or [NSMutableString](nsmutablestring.md) classes but of one of their private subclasses. Although a string object’s class is private, its interface is public, as declared by these abstract superclasses, [NSString](nsstring.md) and [NSMutableString](nsmutablestring.md). The string classes adopt the [NSCopying](nscopying.md) and [NSMutableCopying](nsmutablecopying.md) protocols, making it convenient to convert a string of one type to the other.

#### Understanding Characters

A string object presents itself as a sequence of UTF–16 code units. You can determine how many UTF-16 code units a string object contains with the [length](nsstring/length.md) method and can retrieve a specific UTF-16 code unit with the [- characterAtIndex:](<nsstring/character(at_).md>) method. These two “primitive” methods provide basic access to a string object.

Most use of strings, however, is at a higher level, with the strings being treated as single entities: You compare strings against one another, search them for substrings, combine them into new strings, and so on. If you need to access string objects character by character, you must understand the Unicode character encoding, specifically issues related to composed character sequences. For details see _The Unicode Standard, Version 4.0_ (The Unicode Consortium, Boston: Addison-Wesley, 2003, ISBN 0-321-18578-1) and the Unicode Consortium web site: [http://www.unicode.org/](http://www.unicode.org/). See also [Characters and Grapheme Clusters](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/Articles/stringsClusters.html#//apple_ref/doc/uid/TP40008025) in [String Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/introStrings.html#//apple_ref/doc/uid/10000035i).

Localized string comparisons are based on the Unicode Collation Algorithm, as tailored for different languages by CLDR (Common Locale Data Repository). Both are projects of the Unicode Consortium. Unicode is a registered trademark of Unicode, Inc.

#### Interpreting UTF-16-Encoded Data

When creating an `NSString` object from a UTF-16-encoded string (or a byte stream interpreted as UTF-16), if the byte order is not otherwise specified, `NSString` assumes that the UTF-16 characters are big-endian, unless there is a BOM (byte-order mark), in which case the BOM dictates the byte order. When creating an `NSString` object from an array of `unichar` values, the returned string is always native-endian, since the array always contains UTF–16 code units in native byte order.

### Subclassing Notes

It is possible to subclass [NSString](nsstring.md) (and [NSMutableString](nsmutablestring.md)), but doing so requires providing storage facilities for the string (which is not inherited by subclasses) and implementing two primitive methods. The abstract [NSString](nsstring.md) and [NSMutableString](nsmutablestring.md) classes are the public interface of a class cluster consisting mostly of private, concrete classes that create and return a string object appropriate for a given situation. Making your own concrete subclass of this cluster imposes certain requirements (discussed in [Methods to Override](nsstring.md#Methods-to-Override)).

Make sure your reasons for subclassing [NSString](nsstring.md) are valid. Instances of your subclass should represent a string and not something else. Thus the only attributes the subclass should have are the length of the character buffer it’s managing and access to individual characters in the buffer. Valid reasons for making a subclass of [NSString](nsstring.md) include providing a different backing store (perhaps for better performance) or implementing some aspect of object behavior differently, such as memory management. If your purpose is to add non-essential attributes or metadata to your subclass of [NSString](nsstring.md), a better alternative would be object composition (see [Alternatives to Subclassing](nsstring.md#Alternatives-to-Subclassing)). Cocoa already provides an example of this with the [NSAttributedString](nsattributedstring.md) class.

#### Methods to Override

Any subclass of `NSString`   _must_ override the primitive instance methods [length](nsstring/length.md) and [- characterAtIndex:](<nsstring/character(at_).md>). These methods must operate on the backing store that you provide for the characters of the string. For this backing store you can use a static array, a dynamically allocated buffer, a standard `NSString` object, or some other data type or mechanism. You may also choose to override, partially or fully, any other `NSString` method for which you want to provide an alternative implementation. For example, for better performance it is recommended that you override [- getCharacters:range:](<nsstring/getcharacters(__range_).md>) and give it a faster implementation.

You might want to implement an initializer for your subclass that is suited to the backing store that the subclass is managing. The `NSString` class does not have a designated initializer, so your initializer need only invoke the [init()](<../objectivec/nsobject-swift.class/init().md>) method of `super`. The `NSString` class adopts the [NSCopying](nscopying.md), [NSMutableCopying](nsmutablecopying.md), and [NSCoding](nscoding.md) protocols; if you want instances of your own custom subclass created from copying or coding, override the methods in these protocols.

#### Alternatives to Subclassing

Often a better and easier alternative to making a subclass of `NSString`—or of any other abstract, public class of a class cluster, for that matter—is object composition. This is especially the case when your intent is to add to the subclass metadata or some other attribute that is not essential to a string object. In object composition, you would have an `NSString` object as one instance variable of your custom class (typically a subclass of `NSObject`) and one or more instance variables that store the metadata that you want for the custom object. Then just design your subclass interface to include accessor methods for the embedded string object and the metadata.

If the behavior you want to add supplements that of the existing class, you could write a category on `NSString`. Keep in mind, however, that this category will be in effect for all instances of `NSString` that you use, and this might have unintended consequences.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [NSMutableString](nsmutablestring.md)

- **Conforms To**: [CKRecordValue](../cloudkit/ckrecordvalue-c.protocol.md), [CKRecordValueProtocol](../cloudkit/ckrecordvalueprotocol.md), [CNKeyDescriptor](../contacts/cnkeydescriptor.md), [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [ExpressibleByExtendedGraphemeClusterLiteral](../swift/expressiblebyextendedgraphemeclusterliteral.md), [ExpressibleByStringLiteral](../swift/expressiblebystringliteral.md), [ExpressibleByUnicodeScalarLiteral](../swift/expressiblebyunicodescalarliteral.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSItemProviderReading](nsitemproviderreading.md), [NSItemProviderWriting](nsitemproviderwriting.md), [NSMutableCopying](nsmutablecopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSPasteboardReading](../appkit/nspasteboardreading.md), [NSPasteboardWriting](../appkit/nspasteboardwriting.md), [NSSecureCoding](nssecurecoding.md)

## Topics

### Creating and Initializing Strings

- [- init](<nsstring/init().md>) — Returns an initialized `NSString` object that contains no characters.
- [- initWithBytes:length:encoding:](<nsstring/init(bytes_length_encoding_).md>) — Returns an initialized `NSString` object containing a given number of bytes from a given buffer of bytes interpreted in a given encoding.
- [- initWithBytesNoCopy:length:encoding:freeWhenDone:](<nsstring/init(bytesnocopy_length_encoding_freewhendone_).md>) — Returns an initialized `NSString` object that contains a given number of bytes from a given buffer of bytes interpreted in a given encoding, and optionally frees the buffer.
- [- initWithCharacters:length:](<nsstring/init(characters_length_).md>) — Returns an initialized `NSString` object that contains a given number of characters from a given C array of UTF-16 code units.
- [- initWithCharactersNoCopy:length:freeWhenDone:](<nsstring/init(charactersnocopy_length_freewhendone_).md>) — Returns an initialized `NSString` object that contains a given number of characters from a given C array of UTF-16 code units.
- [- initWithString:](<nsstring/init(string_)-210xa.md>) — Returns an `NSString` object initialized by copying the characters from another given string.
- [- initWithFormat:arguments:](<nsstring/init(format_arguments_).md>) — Returns an `NSString` object initialized by using a given format string as a template into which the remaining argument values are substituted without any localization.
- [- initWithFormat:locale:arguments:](<nsstring/init(format_locale_arguments_).md>) — Returns an `NSString` object initialized by using a given format string as a template into which the remaining argument values are substituted according to given locale information. This method is meant to be called from within a variadic function, where the argument list will be available.
- [- initWithData:encoding:](<nsstring/init(data_encoding_).md>) — Returns an `NSString` object initialized by converting given data into UTF-16 code units using a given encoding.
- [+ localizedUserNotificationStringForKey:arguments:](<nsstring/localizedusernotificationstring(forkey_arguments_).md>) — Returns a localized string intended for display in a notification alert.
- [localizedStringWithFormat(_:_:)](<nsstring/localizedstringwithformat(____).md>)
- [unichar](unichar.md) — Type for UTF-16 code units.

### Creating and Initializing a String from a File

- [- initWithContentsOfFile:encoding:error:](<nsstring/init(contentsoffile_encoding_).md>) — Returns an `NSString` object initialized by reading data from the file at a given path using a given encoding.
- [- initWithContentsOfFile:usedEncoding:error:](<nsstring/init(contentsoffile_usedencoding_).md>) — Returns an `NSString` object initialized by reading data from the file at a given path and returns by reference the encoding used to interpret the characters.

### Getting a String’s Length

- [length](nsstring/length.md) — The number of UTF-16 code units in the receiver.
- [- lengthOfBytesUsingEncoding:](<nsstring/lengthofbytes(using_).md>) — Returns the number of bytes required to store the receiver in a given encoding.
- [- maximumLengthOfBytesUsingEncoding:](<nsstring/maximumlengthofbytes(using_).md>) — Returns the maximum number of bytes needed to store the receiver in a given encoding.

### Getting Characters and Bytes

- [- characterAtIndex:](<nsstring/character(at_).md>) — Returns the character at a given UTF-16 code unit index.
- [- getCharacters:range:](<nsstring/getcharacters(__range_).md>) — Copies characters from a given range in the receiver into a given buffer.
- [- getBytes:maxLength:usedLength:encoding:options:range:remainingRange:](<nsstring/getbytes(__maxlength_usedlength_encoding_options_range_remaining_).md>) — Gets a given range of characters as bytes in a specified encoding.

### Getting C Strings

- [- cStringUsingEncoding:](<nsstring/cstring(using_).md>) — Returns a representation of the string as a C string using a given encoding.
- [- getCString:maxLength:encoding:](<nsstring/getcstring(__maxlength_encoding_).md>) — Converts the string to a given encoding and stores it in a buffer.
- [UTF8String](nsstring/utf8string.md) — A null-terminated UTF8 representation of the string.

### Identifying and Comparing Strings

- [- caseInsensitiveCompare:](<nsstring/caseinsensitivecompare(__).md>) — Returns the result of invoking [- compare:options:](<nsstring/compare(__options_).md>) with `NSCaseInsensitiveSearch` as the only option.
- [- localizedCaseInsensitiveCompare:](<nsstring/localizedcaseinsensitivecompare(__).md>) — Compares the string with a given string using a case-insensitive, localized, comparison.
- [- compare:](<nsstring/compare(__).md>) — Returns the result of invoking [- compare:options:range:](<nsstring/compare(__options_range_).md>) with no options and the receiver’s full extent as the range.
- [- localizedCompare:](<nsstring/localizedcompare(__).md>) — Compares the string and a given string using a localized comparison.
- [- compare:options:](<nsstring/compare(__options_).md>) — Compares the string with the specified string using the given options.
- [- compare:options:range:](<nsstring/compare(__options_range_).md>) — Returns the result of invoking [- compare:options:range:locale:](<nsstring/compare(__options_range_locale_).md>) with a `nil` locale.
- [- compare:options:range:locale:](<nsstring/compare(__options_range_locale_).md>) — Compares the string using the specified options and returns the lexical ordering for the range.
- [- localizedStandardCompare:](<nsstring/localizedstandardcompare(__).md>) — Compares strings as sorted by the Finder.
- [- hasPrefix:](<nsstring/hasprefix(__).md>) — Returns a Boolean value that indicates whether a given string matches the beginning characters of the receiver.
- [- hasSuffix:](<nsstring/hassuffix(__).md>) — Returns a Boolean value that indicates whether a given string matches the ending characters of the receiver.
- [- isEqualToString:](<nsstring/isequal(to_).md>) — Returns a Boolean value that indicates whether a given string is equal to the receiver using a literal Unicode-based comparison.
- [hash](nsstring/hash.md) — An unsigned integer that can be used as a hash table address.
- [CompareOptions](nsstring/compareoptions.md) — These values represent the options available to many of the string classes’ search and comparison methods.
- [EncodingConversionOptions](nsstring/encodingconversionoptions.md) — Options for converting string encodings.

### Combining Strings

- [appendingFormat(_:_:)](<nsstring/appendingformat(____).md>)
- [- stringByAppendingString:](<nsstring/appending(__).md>) — Returns a new string made by appending a given string to the receiver.
- [- stringByPaddingToLength:withString:startingAtIndex:](<nsstring/padding(tolength_withpad_startingat_).md>) — Returns a new string formed from the receiver by either removing characters from the end, or by appending as many occurrences as necessary of a given pad string.

### Changing Case

- [lowercaseString](nsstring/lowercased.md) — A lowercase representation of the string.
- [localizedLowercaseString](nsstring/localizedlowercase.md) — Returns a version of the string with all letters converted to lowercase, taking into account the current locale.
- [- lowercaseStringWithLocale:](<nsstring/lowercased(with_).md>) — Returns a version of the string with all letters converted to lowercase, taking into account the specified locale.
- [uppercaseString](nsstring/uppercased.md) — An uppercase representation of the string.
- [localizedUppercaseString](nsstring/localizeduppercase.md) — Returns a version of the string with all letters converted to uppercase, taking into account the current locale.
- [- uppercaseStringWithLocale:](<nsstring/uppercased(with_).md>) — Returns a version of the string with all letters converted to uppercase, taking into account the specified locale.
- [capitalizedString](nsstring/capitalized.md) — A capitalized representation of the string.
- [localizedCapitalizedString](nsstring/localizedcapitalized.md) — Returns a capitalized representation of the receiver using the current locale.
- [- capitalizedStringWithLocale:](<nsstring/capitalized(with_).md>) — Returns a capitalized representation of the receiver using the specified locale.

### Dividing Strings

- [- componentsSeparatedByString:](<nsstring/components(separatedby_)-238fy.md>) — Returns an array containing substrings from the receiver that have been divided by a given separator.
- [- componentsSeparatedByCharactersInSet:](<nsstring/components(separatedby_)-27x9g.md>) — Returns an array containing substrings from the receiver that have been divided by characters in a given set.
- [- stringByTrimmingCharactersInSet:](<nsstring/trimmingcharacters(in_).md>) — Returns a new string made by removing from both ends of the receiver characters contained in a given character set.
- [- substringFromIndex:](<nsstring/substring(from_).md>) — Returns a new string containing the characters of the receiver from the one at a given index to the end.
- [- substringWithRange:](<nsstring/substring(with_).md>) — Returns a string object containing the characters of the receiver that lie within a given range.
- [- substringToIndex:](<nsstring/substring(to_).md>) — Returns a new string containing the characters of the receiver up to, but not including, the one at a given index.

### Normalizing Strings

- [decomposedStringWithCanonicalMapping](nsstring/decomposedstringwithcanonicalmapping.md) — A string made by normalizing the string’s contents using the Unicode Normalization Form D.
- [decomposedStringWithCompatibilityMapping](nsstring/decomposedstringwithcompatibilitymapping.md) — A string made by normalizing the receiver’s contents using the Unicode Normalization Form KD.
- [precomposedStringWithCanonicalMapping](nsstring/precomposedstringwithcanonicalmapping.md) — A string made by normalizing the string’s contents using the Unicode Normalization Form C.
- [precomposedStringWithCompatibilityMapping](nsstring/precomposedstringwithcompatibilitymapping.md) — A string made by normalizing the receiver’s contents using the Unicode Normalization Form KC.

### Folding Strings

- [- stringByFoldingWithOptions:locale:](<nsstring/folding(options_locale_).md>) — Creates a string suitable for comparison by removing the specified character distinctions from a string.

### Transforming Strings

- [- stringByApplyingTransform:reverse:](<nsstring/applyingtransform(__reverse_).md>) — Returns a new string by applying a specified transform to the string.
- [StringTransform](stringtransform.md) — Constants representing an ICU string transform.

### Finding Characters and Substrings

- [- containsString:](<nsstring/contains(__).md>) — Returns a Boolean value indicating whether the string contains a given string by performing a case-sensitive, locale-unaware search.
- [- localizedCaseInsensitiveContainsString:](<nsstring/localizedcaseinsensitivecontains(__).md>) — Returns a Boolean value indicating whether the string contains a given string by performing a case-insensitive, locale-aware search.
- [- localizedStandardContainsString:](<nsstring/localizedstandardcontains(__).md>) — Returns a Boolean value indicating whether the string contains a given string by performing a case and diacritic insensitive, locale-aware search.
- [- rangeOfCharacterFromSet:](<nsstring/rangeofcharacter(from_).md>) — Finds and returns the range in the string of the first character from a given character set.
- [- rangeOfCharacterFromSet:options:](<nsstring/rangeofcharacter(from_options_).md>) — Finds and returns the range in the string of the first character, using given options, from a given character set.
- [- rangeOfCharacterFromSet:options:range:](<nsstring/rangeofcharacter(from_options_range_).md>) — Finds and returns the range in the string of the first character from a given character set found in a given range with given options.
- [- rangeOfString:](<nsstring/range(of_).md>) — Finds and returns the range of the first occurrence of a given string within the string.
- [- rangeOfString:options:](<nsstring/range(of_options_).md>) — Finds and returns the range of the first occurrence of a given string within the string, subject to given options.
- [- rangeOfString:options:range:](<nsstring/range(of_options_range_).md>) — Finds and returns the range of the first occurrence of a given string, within the given range of the string, subject to given options.
- [- rangeOfString:options:range:locale:](<nsstring/range(of_options_range_locale_).md>) — Finds and returns the range of the first occurrence of a given string within a given range of the string, subject to given options, using the specified locale, if any.
- [- localizedStandardRangeOfString:](<nsstring/localizedstandardrange(of_).md>) — Finds and returns the range of the first occurrence of a given string within the string by performing a case and diacritic insensitive, locale-aware search.
- [- enumerateLinesUsingBlock:](<nsstring/enumeratelines(__).md>) — Enumerates all the lines in the string.
- [- enumerateSubstringsInRange:options:usingBlock:](<nsstring/enumeratesubstrings(in_options_using_).md>) — Enumerates the substrings of the specified type in the specified range of the string.

### Replacing Substrings

- [- stringByReplacingOccurrencesOfString:withString:](<nsstring/replacingoccurrences(of_with_).md>) — Returns a new string in which all occurrences of a target string in the receiver are replaced by another given string.
- [- stringByReplacingOccurrencesOfString:withString:options:range:](<nsstring/replacingoccurrences(of_with_options_range_).md>) — Returns a new string in which all occurrences of a target string in a specified range of the receiver are replaced by another given string.
- [- stringByReplacingCharactersInRange:withString:](<nsstring/replacingcharacters(in_with_).md>) — Returns a new string in which the characters in a specified range of the receiver are replaced by a given string.

### Getting a Shared Prefix

- [- commonPrefixWithString:options:](<nsstring/commonprefix(with_options_).md>) — Returns a string containing characters the receiver and a given string have in common, starting from the beginning of each up to the first characters that aren’t equivalent.

### Performing Linguistic Analysis

- [- enumerateLinguisticTagsInRange:scheme:options:orthography:usingBlock:](<nsstring/enumeratelinguistictags(in_scheme_options_orthography_using_).md>) — Performs linguistic analysis on the specified string by enumerating the specific range of the string, providing the Block with the located tags. _(deprecated)_
- [- linguisticTagsInRange:scheme:options:orthography:tokenRanges:](<nsstring/linguistictags(in_scheme_options_orthography_tokenranges_).md>) — Returns an array of linguistic tags for the specified range and requested tags within the receiving string. _(deprecated)_
- [EnumerationOptions](nsstring/enumerationoptions.md) — Constants to specify kinds of substrings and styles of enumeration.

### Determining Line and Paragraph Ranges

- [- getLineStart:end:contentsEnd:forRange:](<nsstring/getlinestart(__end_contentsend_for_).md>) — Returns by reference the beginning of the first line and the end of the last line touched by the given range.
- [- lineRangeForRange:](<nsstring/linerange(for_).md>) — Returns the range of characters representing the line or lines containing a given range.
- [- getParagraphStart:end:contentsEnd:forRange:](<nsstring/getparagraphstart(__end_contentsend_for_).md>) — Returns by reference the beginning of the first paragraph and the end of the last paragraph touched by the given range.
- [- paragraphRangeForRange:](<nsstring/paragraphrange(for_).md>) — Returns the range of characters representing the paragraph or paragraphs containing a given range.

### Determining Composed Character Sequences

- [- rangeOfComposedCharacterSequenceAtIndex:](<nsstring/rangeofcomposedcharactersequence(at_).md>) — Returns the range in the receiver of the composed character sequence located at a given index.
- [- rangeOfComposedCharacterSequencesForRange:](<nsstring/rangeofcomposedcharactersequences(for_).md>) — Returns the range in the string of the composed character sequences for a given range.

### Writing to a File or URL

- [- writeToFile:atomically:encoding:error:](<nsstring/write(tofile_atomically_encoding_).md>) — Writes the contents of the receiver to a file at a given path using a given encoding.
- [- writeToURL:atomically:encoding:error:](<nsstring/write(to_atomically_encoding_).md>) — Writes the contents of the receiver to the URL specified by `url` using the specified encoding.

### Converting String Contents Into a Property List

- [- propertyList](<nsstring/propertylist().md>) — Parses the receiver as a text representation of a property list, returning an `NSString`, `NSData`, `NSArray`, or `NSDictionary` object, according to the topmost element.
- [- propertyListFromStringsFileFormat](<nsstring/propertylistfromstringsfileformat().md>) — Returns a dictionary object initialized with the keys and values found in the receiver.

### Sizing and Drawing Strings

- [- drawAtPoint:withAttributes:](<nsstring/draw(at_withattributes_).md>) — Draws the receiver with the font and other display characteristics of the given attributes, at the specified point in the current graphics context.
- [- drawInRect:withAttributes:](<nsstring/draw(in_withattributes_).md>) — Draws the attributed string inside the specified bounding rectangle.
- [- drawWithRect:options:attributes:context:](<nsstring/draw(with_options_attributes_context_).md>) — Draws the attributed string in the specified bounding rectangle using the provided options.
- [- boundingRectWithSize:options:attributes:context:](<nsstring/boundingrect(with_options_attributes_context_).md>) — Calculates and returns the bounding rect for the receiver drawn using the given options and display characteristics, within the specified rectangle in the current graphics context.
- [- sizeWithAttributes:](<nsstring/size(withattributes_).md>) — Returns the bounding box size the receiver occupies when drawn with the given attributes.
- [- variantFittingPresentationWidth:](<nsstring/variantfittingpresentationwidth(__).md>) — Returns a string variation suitable for the specified presentation width.
- [NSStringDrawingOptions](../uikit/nsstringdrawingoptions.md) — Constants that specify the rendering options for drawing a string.

### Getting Numeric Values

- [doubleValue](nsstring/doublevalue.md) — The floating-point value of the string as a `double`.
- [floatValue](nsstring/floatvalue.md) — The floating-point value of the string as a `float`.
- [intValue](nsstring/intvalue.md) — The integer value of the string.
- [integerValue](nsstring/integervalue.md) — The `NSInteger` value of the string.
- [longLongValue](nsstring/longlongvalue.md) — The `long long` value of the string.
- [boolValue](nsstring/boolvalue.md) — The Boolean value of the string.

### Working with Encodings

- [availableStringEncodings](nsstring/availablestringencodings.md) — Returns a zero-terminated list of the encodings string objects support in the application’s environment.
- [defaultCStringEncoding](nsstring/defaultcstringencoding.md) — Returns the C-string encoding assumed for any method accepting a C string as an argument.
- [+ stringEncodingForData:encodingOptions:convertedString:usedLossyConversion:](<nsstring/stringencoding(for_encodingoptions_convertedstring_usedlossyconversion_).md>) — Returns the string encoding for the given data as detected by attempting to create a string according to the specified encoding options.
- [+ localizedNameOfStringEncoding:](<nsstring/localizedname(of_).md>) — Returns a human-readable string giving the name of a given encoding.
- [- canBeConvertedToEncoding:](<nsstring/canbeconverted(to_).md>) — Returns a Boolean value that indicates whether the receiver can be converted to a given encoding without loss of information.
- [- dataUsingEncoding:](<nsstring/data(using_).md>) — Returns an `NSData` object containing a representation of the receiver encoded using a given encoding.
- [- dataUsingEncoding:allowLossyConversion:](<nsstring/data(using_allowlossyconversion_).md>) — Returns an `NSData` object containing a representation of the receiver encoded using a given encoding.
- [description](nsstring/description.md)
- [fastestEncoding](nsstring/fastestencoding.md) — The fastest encoding to which the receiver may be converted without loss of information.
- [smallestEncoding](nsstring/smallestencoding.md) — The smallest encoding to which the receiver can be converted without loss of information.
- [StringEncodingDetectionOptionsKey](stringencodingdetectionoptionskey.md)
- [NSString Handling Exception Names](nsstring-handling-exception-names.md) — These constants define the names of exceptions raised if `NSString` cannot represent a string in a given encoding, or parse a string as a property list.

### Working with Paths

- [+ pathWithComponents:](<nsstring/path(withcomponents_).md>) — Returns a string built from the strings in a given array by concatenating them with a path separator between each pair.
- [pathComponents](nsstring/pathcomponents.md) — The file-system path components of the receiver.
- [- completePathIntoString:caseSensitive:matchesIntoArray:filterTypes:](<nsstring/completepath(into_casesensitive_matchesinto_filtertypes_).md>) — Interprets the receiver as a path in the file system and attempts to perform filename completion, returning a numeric value that indicates whether a match was possible, and by reference the longest path that matches the receiver.
- [fileSystemRepresentation](nsstring/filesystemrepresentation.md) — A file system-specific representation of the receiver.
- [- getFileSystemRepresentation:maxLength:](<nsstring/getfilesystemrepresentation(__maxlength_).md>) — Interprets the receiver as a system-independent path and fills a buffer with a C-string in a format and encoding suitable for use with file-system calls.
- [absolutePath](nsstring/isabsolutepath.md) — A Boolean value that indicates whether the receiver represents an absolute path.
- [lastPathComponent](nsstring/lastpathcomponent.md) — The last path component of the receiver.
- [pathExtension](nsstring/pathextension.md) — The path extension, if any, of the string as interpreted as a path.
- [stringByAbbreviatingWithTildeInPath](nsstring/abbreviatingwithtildeinpath.md) — A new string that replaces the current home directory portion of the current path with a tilde (`~`) character.
- [- stringByAppendingPathComponent:](<nsstring/appendingpathcomponent(__).md>) — Returns a new string made by appending to the receiver a given string.
- [- stringByAppendingPathExtension:](<nsstring/appendingpathextension(__).md>) — Returns a new string made by appending to the receiver an extension separator followed by a given extension.
- [stringByDeletingLastPathComponent](nsstring/deletinglastpathcomponent.md) — A new string made by deleting the last path component from the receiver, along with any final path separator.
- [stringByDeletingPathExtension](nsstring/deletingpathextension.md) — A new string made by deleting the extension (if any, and only the last) from the receiver.
- [stringByExpandingTildeInPath](nsstring/expandingtildeinpath.md) — A new string made by expanding the initial component of the receiver to its full path value.
- [stringByResolvingSymlinksInPath](nsstring/resolvingsymlinksinpath.md) — A new string made from the receiver by resolving all symbolic links and standardizing path.
- [stringByStandardizingPath](nsstring/standardizingpath.md) — A new string made by removing extraneous path components from the receiver.
- [- stringsByAppendingPaths:](<nsstring/strings(byappendingpaths_).md>) — Returns an array of strings made by separately appending to the receiver each string in a given array.

### Working with URL Strings

- [- stringByAddingPercentEncodingWithAllowedCharacters:](<nsstring/addingpercentencoding(withallowedcharacters_).md>) — Returns a new string made from the receiver by replacing all characters not in the specified set with percent-encoded characters.
- [stringByRemovingPercentEncoding](nsstring/removingpercentencoding.md) — Returns a new string made from the receiver by replacing all percent encoded sequences with the matching UTF-8 characters.

### Deprecated

- [+ stringWithCString:](<nsstring/string(withcstring_).md>) — Creates a new string using a given C-string. _(deprecated)_
- [init(CString:)](<nsstring/init(cstring_)-vkuo.md>) — Initializes the receiver, a newly allocated `NSString` object, by converting the data in a given C-string from the default C-string encoding into the Unicode character encoding. _(deprecated)_
- [+ stringWithCString:length:](<nsstring/string(withcstring_length_).md>) — Returns a string containing the characters in a given C-string. _(deprecated)_
- [init(CString:length:)](<nsstring/init(cstring_length_)-5ure3.md>) — Initializes the receiver, a newly allocated `NSString` object, by converting the data in a given C-string from the default C-string encoding into the Unicode character encoding. _(deprecated)_
- [init(CStringNoCopy:length:freeWhenDone:)](<nsstring/init(cstringnocopy_length_freewhendone_)-86dm2.md>) — Initializes the receiver, a newly allocated `NSString` object, by converting the data in a given C-string from the default C-string encoding into the Unicode character encoding. _(deprecated)_
- [+ stringWithContentsOfFile:](<nsstring/string(withcontentsoffile_).md>) — Returns a string created by reading data from the file named by a given path. _(deprecated)_
- [- initWithContentsOfFile:](<nsstring/init(contentsoffile_).md>) — Initializes the receiver, a newly allocated `NSString` object, by reading data from the file named by `path`. _(deprecated)_
- [+ stringWithContentsOfURL:](<nsstring/string(withcontentsof_).md>) — Returns a string created by reading data from the file named by a given URL. _(deprecated)_
- [init(contentsOfURL:)](<nsstring/init(contentsofurl_).md>) — Initializes the receiver, a newly allocated `NSString` object, by reading data from the location named by a given URL. _(deprecated)_
- [- writeToFile:atomically:](<nsstring/write(tofile_atomically_).md>) — Writes the contents of the receiver to the file specified by a given path. _(deprecated)_
- [- writeToURL:atomically:](<nsstring/write(to_atomically_).md>) — Writes the contents of the receiver to the location specified by a given URL. _(deprecated)_
- [- getCharacters:](<nsstring/getcharacters(__).md>) — Copies all characters from the receiver into a given buffer. _(deprecated)_
- [- cString](<nsstring/cstring().md>) — Returns a representation of the receiver as a C string in the default C-string encoding. _(deprecated)_
- [- lossyCString](<nsstring/lossycstring().md>) — Returns a representation of the receiver as a C string in the default C-string encoding, possibly losing information in converting to that encoding. _(deprecated)_
- [- cStringLength](<nsstring/cstringlength().md>) — Returns the length in char-sized units of the receiver’s C-string representation in the default C-string encoding. _(deprecated)_
- [- getCString:](<nsstring/getcstring(__).md>) — Invokes [- getCString:maxLength:range:remainingRange:](<nsstring/getcstring(__maxlength_range_remaining_).md>) with `NSMaximumStringLength` as the maximum length, the receiver’s entire extent as the range, and `NULL` for the remaining range. _(deprecated)_
- [- getCString:maxLength:](<nsstring/getcstring(__maxlength_).md>) — Invokes [- getCString:maxLength:range:remainingRange:](<nsstring/getcstring(__maxlength_range_remaining_).md>) with `maxLength` as the maximum length in char-sized units, the receiver’s entire extent as the range, and `NULL` for the remaining range. _(deprecated)_
- [- getCString:maxLength:range:remainingRange:](<nsstring/getcstring(__maxlength_range_remaining_).md>) — Converts the receiver’s content to the default C-string encoding and stores them in a given buffer. _(deprecated)_
- [- stringByAddingPercentEscapesUsingEncoding:](<nsstring/addingpercentescapes(using_).md>) — Returns a representation of the receiver using a given encoding to determine the percent escapes necessary to convert the receiver into a legal URL string. _(deprecated)_
- [- stringByReplacingPercentEscapesUsingEncoding:](<nsstring/replacingpercentescapes(using_).md>) — Returns a new string made by replacing in the receiver all percent escapes with the matching characters as determined by a given encoding. _(deprecated)_
- [- drawWithRect:options:attributes:](<nsstring/draw(with_options_attributes_).md>) — Draws the receiver with the specified options and other display characteristics of the given attributes, within the specified rectangle in the current graphics context. _(deprecated)_
- [- boundingRectWithSize:options:attributes:](<nsstring/boundingrect(with_options_attributes_).md>) — Calculates and returns the bounding rect for the receiver drawn using the given options and display characteristics, within the specified rectangle in the current graphics context. _(deprecated)_

### Structures

- [DrawingOptions](nsstring/drawingoptions.md)

### Initializers

- [- initWithBytesNoCopy:length:encoding:deallocator:](<nsstring/init(bytesnocopy_length_encoding_deallocator_).md>)
- [- initWithCString:](<nsstring/init(cstring_)-5mpk8.md>) _(deprecated)_
- [- initWithCString:encoding:](<nsstring/init(cstring_encoding_)-20f9h.md>) — Returns an @c NSString object initialized using the characters in a given C array, interpreted according to a given encoding.
- [- initWithCString:length:](<nsstring/init(cstring_length_)-4bbpi.md>) _(deprecated)_
- [- initWithCStringNoCopy:length:freeWhenDone:](<nsstring/init(cstringnocopy_length_freewhendone_)-7ssxw.md>) _(deprecated)_
- [- initWithCharactersNoCopy:length:deallocator:](<nsstring/init(charactersnocopy_length_deallocator_).md>)
- [- initWithCoder:](<nsstring/init(coder_).md>)
- [- initWithContentsOfURL:](<nsstring/init(contentsof_).md>) — Returns an @c NSString object initialized by reading data from the URL named by @c url. _(deprecated)_
- [- initWithContentsOfURL:encoding:error:](<nsstring/init(contentsof_encoding_).md>) — Returns an @c NSString object initialized by reading data from a given URL interpreted using a given encoding.
- [- initWithContentsOfURL:usedEncoding:error:](<nsstring/init(contentsof_usedencoding_).md>) — Returns an @c NSString object initialized by reading data from a given URL and returns by reference the encoding used to interpret the data.
- [init(format:_:)](<nsstring/init(format___).md>)
- [init(format:locale:_:)](<nsstring/init(format_locale___).md>)
- [init(string:)](<nsstring/init(string_)-7xgq7.md>) — Returns an `NSString` object initialized by copying the characters from another given string.
- [- initWithUTF8String:](<nsstring/init(utf8string_)-vg2b.md>) — Returns an @c NSString object initialized by copying the characters from a given C array of UTF8-encoded bytes.

### Instance Properties

- [customPlaygroundQuickLook](nsstring/customplaygroundquicklook.md) — A custom playground Quick Look for this instance. _(deprecated)_

### Instance Methods

- [- stringByAppendingPathComponent:conformingToType:](<nsstring/appendingpathcomponent(__conformingto_).md>)
- [- stringByAppendingPathExtensionForType:](<nsstring/appendingpathextension(for_).md>)
- [- sr_sensorForDeletionRecordsFromSensor](<nsstring/sr_sensorfordeletionrecordsfromsensor().md>) _(deprecated)_

### Type Methods

- [deferredLocalizedIntentsString(with:_:)](<nsstring/deferredlocalizedintentsstring(with___).md>)
- [deferredLocalizedIntentsString(with:table:_:)](<nsstring/deferredlocalizedintentsstring(with_table___).md>)
- [deferredLocalizedIntentsString(with:table:arguments:)](<nsstring/deferredlocalizedintentsstring(with_table_arguments_).md>)

### Default Implementations

- [ExpressibleByStringLiteral Implementations](nsstring/expressiblebystringliteral-implementations.md)
- [NSString Implementations](nsstring/nsstring-implementations.md)
