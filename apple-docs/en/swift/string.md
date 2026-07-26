---
title: String
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/string
source_url: 'https://developer.apple.com/documentation/swift/string'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string.json'
content_hash: 'sha256:a93af11fb9fd0a81'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# String

<sub>Structure</sub>

A Unicode string value that is a collection of characters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct String
```

## Overview

A string is a series of characters, such as `"Swift"`, that forms a collection. Strings in Swift are Unicode correct and locale insensitive, and are designed to be efficient. The `String` type bridges with the Objective-C class `NSString` and offers interoperability with C functions that work with strings.

You can create new strings using string literals or string interpolations. A _string literal_ is a series of characters enclosed in quotes.

```swift
let greeting = "Welcome!"
```

_String interpolations_ are string literals that evaluate any included expressions and convert the results to string form. String interpolations give you an easy way to build a string from multiple pieces. Wrap each expression in a string interpolation in parentheses, prefixed by a backslash.

```swift
let name = "Rosa"
let personalizedGreeting = "Welcome, \(name)!"
// personalizedGreeting == "Welcome, Rosa!"

let price = 2
let number = 3
let cookiePrice = "\(number) cookies: $\(price * number)."
// cookiePrice == "3 cookies: $6."
```

Combine strings using the concatenation operator (`+`).

```swift
let longerGreeting = greeting + " We're glad you're here!"
// longerGreeting == "Welcome! We're glad you're here!"
```

Multiline string literals are enclosed in three double quotation marks (`"""`), with each delimiter on its own line. Indentation is stripped from each line of a multiline string literal to match the indentation of the closing delimiter.

```swift
let banner = """
          __,
         (           o  /) _/_
          `.  , , , ,  //  /
        (___)(_(_/_(_ //_ (__
                     /)
                    (/
        """
```

## Modifying and Comparing Strings

Strings always have value semantics. Modifying a copy of a string leaves the original unaffected.

```swift
var otherGreeting = greeting
otherGreeting += " Have a nice time!"
// otherGreeting == "Welcome! Have a nice time!"

print(greeting)
// Prints "Welcome!"
```

Comparing strings for equality using the equal-to operator (`==`) or a relational operator (like `<` or `>=`) is always performed using Unicode canonical representation. As a result, different representations of a string compare as being equal.

```swift
let cafe1 = "Cafe\u{301}"
let cafe2 = "Café"
print(cafe1 == cafe2)
// Prints "true"
```

The Unicode scalar value `"\u{301}"` modifies the preceding character to include an accent, so `"e\u{301}"` has the same canonical representation as the single Unicode scalar value `"é"`.

Basic string operations are not sensitive to locale settings, ensuring that string comparisons and other operations always have a single, stable result, allowing strings to be used as keys in `Dictionary` instances and for other purposes.

## Accessing String Elements

A string is a collection of _extended grapheme clusters_, which approximate human-readable characters. Many individual characters, such as “é”, “김”, and “🇮🇳”, can be made up of multiple Unicode scalar values. These scalar values are combined by Unicode’s boundary algorithms into extended grapheme clusters, represented by the Swift `Character` type. Each element of a string is represented by a `Character` instance.

For example, to retrieve the first word of a longer string, you can search for a space and then create a substring from a prefix of the string up to that point:

```swift
let name = "Marie Curie"
let firstSpace = name.firstIndex(of: " ") ?? name.endIndex
let firstName = name[..<firstSpace]
// firstName == "Marie"
```

The `firstName` constant is an instance of the `Substring` type—a type that represents substrings of a string while sharing the original string’s storage. Substrings present the same interface as strings.

```swift
print("\(name)'s first name has \(firstName.count) letters.")
// Prints "Marie Curie's first name has 5 letters."
```

## Accessing a String’s Unicode Representation

If you need to access the contents of a string as encoded in different Unicode encodings, use one of the string’s `unicodeScalars`, `utf16`, or `utf8` properties. Each property provides access to a view of the string as a series of code units, each encoded in a different Unicode encoding.

To demonstrate the different views available for every string, the following examples use this `String` instance:

```swift
let cafe = "Cafe\u{301} du 🌍"
print(cafe)
// Prints "Café du 🌍"
```

The `cafe` string is a collection of the nine characters that are visible when the string is displayed.

```swift
print(cafe.count)
// Prints "9"
print(Array(cafe))
// Prints "["C", "a", "f", "é", " ", "d", "u", " ", "🌍"]"
```

## Unicode Scalar View

A string’s `unicodeScalars` property is a collection of Unicode scalar values, the 21-bit codes that are the basic unit of Unicode. Each scalar value is represented by a `Unicode.Scalar` instance and is equivalent to a UTF-32 code unit.

```swift
print(cafe.unicodeScalars.count)
// Prints "10"
print(Array(cafe.unicodeScalars))
// Prints "["C", "a", "f", "e", "\u{0301}", " ", "d", "u", " ", "\u{0001F30D}"]"
print(cafe.unicodeScalars.map { $0.value })
// Prints "[67, 97, 102, 101, 769, 32, 100, 117, 32, 127757]"
```

The `unicodeScalars` view’s elements comprise each Unicode scalar value in the `cafe` string. In particular, because `cafe` was declared using the decomposed form of the `"é"` character, `unicodeScalars` contains the scalar values for both the letter `"e"` (101) and the accent character `"´"` (769).

## UTF-16 View

A string’s `utf16` property is a collection of UTF-16 code units, the 16-bit encoding form of the string’s Unicode scalar values. Each code unit is stored as a `UInt16` instance.

```swift
print(cafe.utf16.count)
// Prints "11"
print(Array(cafe.utf16))
// Prints "[67, 97, 102, 101, 769, 32, 100, 117, 32, 55356, 57101]"
```

The elements of the `utf16` view are the code units for the string when encoded in UTF-16. These elements match those accessed through indexed `NSString` APIs.

```swift
let nscafe = cafe as NSString
print(nscafe.length)
// Prints "11"
print(nscafe.character(at: 3))
// Prints "101"
```

## UTF-8 View

A string’s `utf8` property is a collection of UTF-8 code units, the 8-bit encoding form of the string’s Unicode scalar values. Each code unit is stored as a `UInt8` instance.

```swift
print(cafe.utf8.count)
// Prints "14"
print(Array(cafe.utf8))
// Prints "[67, 97, 102, 101, 204, 129, 32, 100, 117, 32, 240, 159, 140, 141]"
```

The elements of the `utf8` view are the code units for the string when encoded in UTF-8. This representation matches the one used when `String` instances are passed to C APIs.

```swift
let cLength = strlen(cafe)
print(cLength)
// Prints "14"
```

## Measuring the Length of a String

When you need to know the length of a string, you must first consider what you’ll use the length for. Are you measuring the number of characters that will be displayed on the screen, or are you measuring the amount of storage needed for the string in a particular encoding? A single string can have greatly differing lengths when measured by its different views.

For example, an ASCII character like the capital letter _A_ is represented by a single element in each of its four views. The Unicode scalar value of _A_ is `65`, which is small enough to fit in a single code unit in both UTF-16 and UTF-8.

```swift
let capitalA = "A"
print(capitalA.count)
// Prints "1"
print(capitalA.unicodeScalars.count)
// Prints "1"
print(capitalA.utf16.count)
// Prints "1"
print(capitalA.utf8.count)
// Prints "1"
```

On the other hand, an emoji flag character is constructed from a pair of Unicode scalar values, like `"\u{1F1F5}"` and `"\u{1F1F7}"`. Each of these scalar values, in turn, is too large to fit into a single UTF-16 or UTF-8 code unit. As a result, each view of the string `"🇵🇷"` reports a different length.

```swift
let flag = "🇵🇷"
print(flag.count)
// Prints "1"
print(flag.unicodeScalars.count)
// Prints "2"
print(flag.utf16.count)
// Prints "4"
print(flag.utf8.count)
// Prints "8"
```

To check whether a string is empty, use its `isEmpty` property instead of comparing the length of one of the views to `0`. Unlike with `isEmpty`, calculating a view’s `count` property requires iterating through the elements of the string.

## Accessing String View Elements

To find individual elements of a string, use the appropriate view for your task. For example, to retrieve the first word of a longer string, you can search the string for a space and then create a new string from a prefix of the string up to that point.

```swift
let name = "Marie Curie"
let firstSpace = name.firstIndex(of: " ") ?? name.endIndex
let firstName = name[..<firstSpace]
print(firstName)
// Prints "Marie"
```

Strings and their views share indices, so you can access the UTF-8 view of the `name` string using the same `firstSpace` index.

```swift
print(Array(name.utf8[..<firstSpace]))
// Prints "[77, 97, 114, 105, 101]"
```

Note that an index into one view may not have an exact corresponding position in another view. For example, the `flag` string declared above comprises a single character, but is composed of eight code units when encoded as UTF-8. The following code creates constants for the first and second positions in the `flag.utf8` view. Accessing the `utf8` view with these indices yields the first and second code UTF-8 units.

```swift
let firstCodeUnit = flag.startIndex
let secondCodeUnit = flag.utf8.index(after: firstCodeUnit)
// flag.utf8[firstCodeUnit] == 240
// flag.utf8[secondCodeUnit] == 159
```

When used to access the elements of the `flag` string itself, however, the `secondCodeUnit` index does not correspond to the position of a specific character. Instead of only accessing the specific UTF-8 code unit, that index is treated as the position of the character at the index’s encoded offset. In the case of `secondCodeUnit`, that character is still the flag itself.

```swift
// flag[firstCodeUnit] == "🇵🇷"
// flag[secondCodeUnit] == "🇵🇷"
```

If you need to validate that an index from one string’s view corresponds with an exact position in another view, use the index’s `samePosition(in:)` method or the `init(_:within:)` initializer.

```swift
if let exactIndex = secondCodeUnit.samePosition(in: flag) {
    print(flag[exactIndex])
} else {
    print("No exact match for this position.")
}
// Prints "No exact match for this position."
```

## Performance Optimizations

Although strings in Swift have value semantics, strings use a copy-on-write strategy to store their data in a buffer. This buffer can then be shared by different copies of a string. A string’s data is only copied lazily, upon mutation, when more than one string instance is using the same buffer. Therefore, the first in any sequence of mutating operations may cost O(_n_) time and space.

When a string’s contiguous storage fills up, a new buffer must be allocated and data must be moved to the new storage. String buffers use an exponential growth strategy that makes appending to a string a constant time operation when averaged over many append operations.

## Bridging Between String and NSString

Any `String` instance can be bridged to `NSString` using the type-cast operator (`as`), and any `String` instance that originates in Objective-C may use an `NSString` instance as its storage. Because any arbitrary subclass of `NSString` can become a `String` instance, there are no guarantees about representation or efficiency when a `String` instance is backed by `NSString` storage. Because `NSString` is immutable, it is just as though the storage was shared by a copy. The first in any sequence of mutating operations causes elements to be copied into unique, contiguous storage which may cost O(_n_) time and space, where _n_ is the length of the string’s encoded representation (or more, if the underlying `NSString` has unusual performance characteristics).

For more information about the Unicode terms used in this discussion, see the [Unicode.org glossary](http://www.unicode.org/glossary/). In particular, this discussion mentions [extended grapheme clusters](http://www.unicode.org/glossary/#extended_grapheme_cluster), [Unicode scalar values](http://www.unicode.org/glossary/#unicode_scalar_value), and [canonical equivalence](http://www.unicode.org/glossary/#canonical_equivalent).

## Relationships

- **Conforms To**: [Attachable](../testing/attachable.md), [BidirectionalCollection](bidirectionalcollection.md), [BindableData](../realitykit/bindabledata.md), [CKRecordValueProtocol](../cloudkit/ckrecordvalueprotocol.md), [CVAttachmentValueRepresentable](../corevideo/cvattachmentvaluerepresentable.md), [CVarArg](cvararg.md), [CodingKeyRepresentable](codingkeyrepresentable.md), [Collection](collection.md), [Comparable](comparable.md), [ConvertibleFromGeneratedContent](../foundationmodels/convertiblefromgeneratedcontent.md), [ConvertibleToGeneratedContent](../foundationmodels/convertibletogeneratedcontent.md), [Copyable](copyable.md), [CustomDebugStringConvertible](customdebugstringconvertible.md), [CustomReflectable](customreflectable.md), [CustomStringConvertible](customstringconvertible.md), [CustomTestStringConvertible](../testing/customteststringconvertible.md), [CustomURLRepresentationParameterConvertible](../appintents/customurlrepresentationparameterconvertible.md), [Decodable](decodable.md), [Encodable](encodable.md), [EntityIdentifierConvertible](../appintents/entityidentifierconvertible.md), [Equatable](equatable.md), [Escapable](escapable.md), [ExpressibleByExtendedGraphemeClusterLiteral](expressiblebyextendedgraphemeclusterliteral.md), [ExpressibleByStringInterpolation](expressiblebystringinterpolation.md), [ExpressibleByStringLiteral](expressiblebystringliteral.md), [ExpressibleByUnicodeScalarLiteral](expressiblebyunicodescalarliteral.md), [Generable](../foundationmodels/generable.md), [Hashable](hashable.md), [InstructionsRepresentable](../foundationmodels/instructionsrepresentable.md), [IntentValueConvertible](../appintents/intentvalueconvertible.md), [IntentValueExpressing](../appintents/intentvalueexpressing.md), [LosslessStringConvertible](losslessstringconvertible.md), [MLDataValueConvertible](../createml/mldatavalueconvertible.md), [MLIdentifier](../createml/mlidentifier.md), [MirrorPath](mirrorpath.md), [MusicLibraryRequestFilterValueEquatable](../musickit/musiclibraryrequestfiltervalueequatable.md), [Plottable](../charts/plottable.md), [PrimitivePlottableProtocol](../charts/primitiveplottableprotocol.md), [PromptRepresentable](../foundationmodels/promptrepresentable.md), [RangeReplaceableCollection](rangereplaceablecollection.md), [RegexComponent](regexcomponent.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md), [Sequence](sequence.md), [StringProtocol](stringprotocol.md), [TextOutputStream](textoutputstream.md), [TextOutputStreamable](textoutputstreamable.md), [Transferable](../coretransferable/transferable.md), [USDPrim.Attribute.MetadataValue](../usdkit/usdprim/attribute/metadatavalue.md), [USDPrim.Attribute.Value](../usdkit/usdprim/attribute/value.md), [USDValueProtocol](../usdkit/usdvalueprotocol.md)

## Topics

### Creating a String

- [init(decoding:)](<string/init(decoding_)-nm7v.md>) — Creates a string by interpreting the file path’s content as UTF-8 on Unix and UTF-16 on Windows.
- [init()](<string/init().md>) — Creates an empty string.
- [init(_:)](<string/init(__)-8v3fo.md>) — Creates a string containing the given character.
- [init(_:)](<string/init(__)-8og6g.md>) — Creates a new string containing the characters in the given sequence.
- [init(_:)](<string/init(__)-1ip93.md>) — Creates a new instance of a collection containing the elements of a sequence.
- [init(_:)](<string/init(__)-50pwi.md>) — Creates a new string containing the characters in the given sequence.
- [init(_:)](<string/init(__)-14lv5.md>) — Creates a new string from the given substring.
- [init(repeating:count:)](<string/init(repeating_count_)-23xjt.md>) — Creates a new string representing the given string repeated the specified number of times.
- [init(repeating:count:)](<string/init(repeating_count_)-11bpi.md>) — Creates a string representing the given character repeated the specified number of times.
- [init(unsafeUninitializedCapacity:initializingUTF8With:)](<string/init(unsafeuninitializedcapacity_initializingutf8with_).md>)

### Inspecting a String

- [isEmpty](string/isempty.md) — A Boolean value indicating whether a string has no characters.
- [count](string/count.md) — The number of characters in a string.

### Creating a String from Unicode Data

- [init(_:)](<string/init(__)-8ay23.md>)
- [init(data:encoding:)](<string/init(data_encoding_).md>) — Returns a `String` initialized by converting given `data` into Unicode characters using a given `encoding`.
- [init(validatingUTF8:)](<string/init(validatingutf8_)-208fn.md>) — Creates a new string by copying and validating the null-terminated UTF-8 data referenced by the given pointer.
- [init(validating:as:)](<string/init(validating_as_)-84qr9.md>) — Creates a new string by copying and validating the sequence of code units passed in, according to the specified encoding.
- [init(validating:as:)](<string/init(validating_as_)-5cw2c.md>) — Creates a new string by copying and validating the sequence of code units passed in, according to the specified encoding.
- [init(utf8String:)](<string/init(utf8string_)-8qmaq.md>) — Creates a string by copying the data from a given null-terminated array of UTF8-encoded bytes.
- [init(utf8String:)](<string/init(utf8string_)-3mcco.md>) — Creates a string by copying the data from a given null-terminated C array of UTF8-encoded bytes.
- [init(utf16CodeUnits:count:)](<string/init(utf16codeunits_count_).md>) — Creates a new string that contains the specified number of characters from the given C array of Unicode characters.
- [init(utf16CodeUnitsNoCopy:count:freeWhenDone:)](<string/init(utf16codeunitsnocopy_count_freewhendone_).md>) — Creates a new string that contains the specified number of characters from the given C array of UTF-16 code units. _(deprecated)_
- [init(decoding:as:)](<string/init(decoding_as_).md>) — Creates a string from the given Unicode code units in the specified encoding.

### Creating a String Using Formats

- [init(format:_:)](<string/init(format___).md>) — Returns a `String` object initialized by using a given format string as a template into which the remaining argument values are substituted.
- [init(format:arguments:)](<string/init(format_arguments_).md>) — Returns a `String` object initialized by using a given format string as a template into which the remaining argument values are substituted according to the user’s default locale.
- [init(format:locale:_:)](<string/init(format_locale___).md>) — Returns a `String` object initialized by using a given format string as a template into which the remaining argument values are substituted according to given locale information.
- [init(format:locale:arguments:)](<string/init(format_locale_arguments_).md>) — Returns a `String` object initialized by using a given format string as a template into which the remaining argument values are substituted according to given locale information.
- [localizedStringWithFormat(_:_:)](<string/localizedstringwithformat(____).md>) — Returns a string created by using a given format string as a template into which the remaining argument values are substituted according to the user’s default locale.

### Creating a Localized String

- [init(localized:table:bundle:locale:comment:)](<string/init(localized_table_bundle_locale_comment_).md>) — Creates a localized string from an interpolated string.
- [init(localized:options:table:bundle:locale:comment:)](<string/init(localized_options_table_bundle_locale_comment_).md>) — Creates a localized string from an interpolated string, applying the specified options.
- [LocalizationValue](string/localizationvalue.md) — A reference to a localizable string, with optional string interpolation.
- [LocalizationOptions](string/localizationoptions.md) — Options to apply when initializing a localized string.
- [init(localized:defaultValue:table:bundle:locale:comment:)](<string/init(localized_defaultvalue_table_bundle_locale_comment_).md>) — Creates a localized string from an arbitrary static string key.
- [init(localized:defaultValue:options:table:bundle:locale:comment:)](<string/init(localized_defaultvalue_options_table_bundle_locale_comment_).md>) — Creates a localized string from an arbitrary static string key, applying the specified options.
- [init(localized:)](<string/init(localized_).md>) — Creates a localized string from a localized string resource.
- [init(localized:options:)](<string/init(localized_options_).md>) — Creates a localized string from a localized string resource, applying the specified options.

### Converting Numeric Values

- [init(_:radix:uppercase:)](<string/init(__radix_uppercase_).md>) — Creates a string representing the given value in base 10, or some other specified base.

### Converting a C String

- [init(bytes:encoding:)](<string/init(bytes_encoding_).md>) — Creates a new string equivalent to the given bytes interpreted in the specified encoding. Note: This API does not interpret embedded nulls as termination of the string. Use `String?(validatingCString:)` instead for null-terminated C strings.
- [init(bytesNoCopy:length:encoding:freeWhenDone:)](<string/init(bytesnocopy_length_encoding_freewhendone_).md>) — Creates a new string that contains the specified number of bytes from the given buffer, interpreted in the specified encoding, and optionally frees the buffer. _(deprecated)_
- [init(validatingCString:)](<string/init(validatingcstring_)-992vo.md>) — Creates a new string by copying and validating the null-terminated UTF-8 data referenced by the given pointer.
- [init(validatingCString:)](<string/init(validatingcstring_)-98wra.md>) — Creates a new string by copying and validating the null-terminated UTF-8 data referenced by the given array.
- [init(cString:)](<string/init(cstring_)-2p84k.md>) — Creates a new string by copying the null-terminated UTF-8 data referenced by the given pointer.
- [init(cString:)](<string/init(cstring_)-6kr8s.md>) — Creates a new string by copying the null-terminated UTF-8 data referenced by the given pointer.
- [init(cString:encoding:)](<string/init(cstring_encoding_)-3h7bc.md>) — Produces a string by copying the null-terminated bytes in a given array, interpreted according to a given encoding.
- [init(cString:encoding:)](<string/init(cstring_encoding_)-3qgzd.md>) — Produces a string by copying the null-terminated bytes in a given C array, interpreted according to a given encoding.
- [init(decodingCString:as:)](<string/init(decodingcstring_as_)-8way7.md>) — Creates a new string by copying the null-terminated sequence of code units referenced by the given array.
- [decodeCString(_:as:repairingInvalidCodeUnits:)](<string/decodecstring(__as_repairinginvalidcodeunits_)-46n2p.md>) — Creates a new string by copying the null-terminated data referenced by the given pointer using the specified encoding.

### Converting Other Types to Strings

- [init(_:)](<string/init(__)-1ywfq.md>) — Creates an instance from the description of a given `LosslessStringConvertible` instance.
- [init(describing:)](<string/init(describing_)-588wb.md>) — Creates a string representing the given value.
- [init(describing:)](<string/init(describing_)-hsqw.md>) — Creates a string representing the given value.
- [init(describing:)](<string/init(describing_)-6ttci.md>) — Creates a string representing the given value.
- [init(describing:)](<string/init(describing_)-67ncf.md>) — Creates a string representing the given value.
- [init(reflecting:)](<string/init(reflecting_).md>) — Creates a string with a detailed representation of the given value, suitable for debugging.

### Creating a String from a File or URL

- [init(contentsOf:)](<string/init(contentsof_).md>) _(deprecated)_
- [init(contentsOf:encoding:)](<string/init(contentsof_encoding_).md>) — Produces a string created by reading data from a given URL interpreted using a given encoding.
- [init(contentsOf:usedEncoding:)](<string/init(contentsof_usedencoding_).md>) — Produces a string created by reading data from a given URL and returns by reference the encoding used to interpret the data.
- [init(contentsOfFile:)](<string/init(contentsoffile_).md>) _(deprecated)_
- [init(contentsOfFile:encoding:)](<string/init(contentsoffile_encoding_).md>) — Produces a string created by reading data from the file at a given path interpreted using a given encoding.
- [init(contentsOfFile:usedEncoding:)](<string/init(contentsoffile_usedencoding_).md>) — Produces a string created by reading data from the file at a given path and returns by reference the encoding used to interpret the file.

### Writing to a File or URL

- [write(_:)](<string/write(__).md>) — Appends the given string to this string.
- [write(to:)](<string/write(to_).md>) — Writes the string into the given output stream.

### Appending Strings and Characters

- [append(_:)](<string/append(__)-4xa8f.md>) — Appends the given string to this string.
- [append(_:)](<string/append(__)-4xi3j.md>) — Appends the given character to the string.
- [append(contentsOf:)](<string/append(contentsof_)-oxek.md>)
- [append(contentsOf:)](<string/append(contentsof_)-9vb4t.md>)
- [append(contentsOf:)](<string/append(contentsof_)-7est5.md>) — Appends the characters in the given sequence to the string.
- [append(contentsOf:)](<string/append(contentsof_)-9foms.md>) — Adds the elements of a sequence or collection to the end of this collection.
- [reserveCapacity(_:)](<string/reservecapacity(__).md>) — Reserves enough space in the string’s underlying storage to store the specified number of ASCII characters.
- [+(_:_:)](<string/+(____).md>)
- [+=(_:_:)](<string/+=(____).md>)
- [+(_:_:)](<string/+(____)-6h59y.md>) — Creates a new collection by concatenating the elements of a sequence and a collection.
- [+(_:_:)](<string/+(____)-n329.md>) — Creates a new collection by concatenating the elements of a collection and a sequence.
- [+(_:_:)](<string/+(____)-9fm57.md>) — Creates a new collection by concatenating the elements of two collections.
- [+=(_:_:)](<string/+=(____)-676gx.md>) — Appends the elements of a sequence to a range-replaceable collection.

### Inserting Characters

- [insert(_:at:)](<string/insert(__at_).md>) — Inserts a new character at the specified position.
- [insert(_:at:)](<string/insert(__at_)-88yqh.md>) — Inserts a new element into the collection at the specified position.
- [insert(contentsOf:at:)](<string/insert(contentsof_at_)-rdu9.md>) — Inserts the elements of a sequence into the collection at the specified position.
- [insert(contentsOf:at:)](<string/insert(contentsof_at_).md>) — Inserts a collection of characters at the specified position.

### Replacing Substrings

- [replaceSubrange(_:with:)](<string/replacesubrange(__with_).md>) — Replaces the text within the specified bounds with the given characters.
- [replaceSubrange(_:with:)](<string/replacesubrange(__with_)-72947.md>) — Replaces the specified subrange of elements with the given collection.

### Removing Substrings

- [remove(at:)](<string/remove(at_).md>) — Removes and returns the character at the specified position.
- [remove(at:)](<string/remove(at_)-5g0wm.md>) — Removes and returns the element at the specified position.
- [removeAll(keepingCapacity:)](<string/removeall(keepingcapacity_).md>) — Replaces this string with the empty string.
- [removeAll(where:)](<string/removeall(where_).md>) — Removes all the elements that satisfy the given predicate.
- [removeFirst()](<string/removefirst().md>) — Removes and returns the first element of the collection.
- [removeFirst(_:)](<string/removefirst(__).md>) — Removes the specified number of elements from the beginning of the collection.
- [removeLast()](<string/removelast().md>) — Removes and returns the last element of the collection.
- [removeLast(_:)](<string/removelast(__).md>) — Removes the specified number of elements from the end of the collection.
- [removeSubrange(_:)](<string/removesubrange(__).md>) — Removes the characters in the given range.
- [removeSubrange(_:)](<string/removesubrange(__)-8maxn.md>) — Removes the elements in the specified subrange from the collection.
- [removeSubrange(_:)](<string/removesubrange(__)-9twng.md>) — Removes the elements in the specified subrange from the collection.
- [drop(while:)](<string/drop(while_).md>) — Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
- [dropFirst(_:)](<string/dropfirst(__).md>) — Returns a subsequence containing all but the given number of initial elements.
- [dropLast(_:)](<string/droplast(__).md>) — Returns a subsequence containing all but the specified number of final elements.
- [popLast()](<string/poplast().md>) — Removes and returns the last element of the collection.

### Changing Case

- [lowercased()](<string/lowercased().md>) — Returns a lowercase version of the string.
- [uppercased()](<string/uppercased().md>) — Returns an uppercase version of the string.

### Comparing Strings Using Operators

- [==(_:_:)](<string/==(____).md>) — Returns a Boolean value indicating whether two values are equal.
- [==(_:_:)](<string/==(____)-8kzxf.md>)
- [!=(_:_:)](<string/!=(____)-frzf.md>)
- [~=(_:_:)](<string/~=(____).md>)

### Comparing Characters

- [elementsEqual(_:)](<string/elementsequal(__).md>) — Returns a Boolean value indicating whether this sequence and another sequence contain the same elements in the same order.
- [elementsEqual(_:by:)](<string/elementsequal(__by_).md>) — Returns a Boolean value indicating whether this sequence and another sequence contain equivalent elements in the same order, using the given predicate as the equivalence test.
- [starts(with:)](<string/starts(with_).md>) — Returns a Boolean value indicating whether the initial elements of the sequence are the same as the elements in another sequence.
- [starts(with:by:)](<string/starts(with_by_).md>) — Returns a Boolean value indicating whether the initial elements of the sequence are equivalent to the elements in another sequence, using the given predicate as the equivalence test.
- [lexicographicallyPrecedes(_:)](<string/lexicographicallyprecedes(__).md>) — Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the less-than operator (`<`) to compare elements.
- [lexicographicallyPrecedes(_:by:)](<string/lexicographicallyprecedes(__by_).md>) — Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the given predicate to compare elements.

### Creating and Applying Differences

- [applying(_:)](<string/applying(__).md>) — Applies the given difference to this collection.
- [difference(from:)](<string/difference(from_).md>) — Returns the difference needed to produce this collection’s ordered elements from the given collection.
- [difference(from:by:)](<string/difference(from_by_).md>) — Returns the difference needed to produce this collection’s ordered elements from the given collection, using the given predicate as an equivalence test.

### Finding Substrings

- [hasPrefix(_:)](<string/hasprefix(__).md>)
- [hasSuffix(_:)](<string/hassuffix(__).md>)

### Finding Characters

- [contains(_:)](<string/contains(__).md>) — Returns a Boolean value indicating whether the sequence contains the given element.
- [allSatisfy(_:)](<string/allsatisfy(__).md>) — Returns a Boolean value indicating whether every element of a sequence satisfies a given predicate.
- [contains(where:)](<string/contains(where_).md>) — Returns a Boolean value indicating whether the sequence contains an element that satisfies the given predicate.
- [first(where:)](<string/first(where_).md>) — Returns the first element of the sequence that satisfies the given predicate.
- [firstIndex(of:)](<string/firstindex(of_).md>) — Returns the first index where the specified value appears in the collection.
- [firstIndex(where:)](<string/firstindex(where_).md>) — Returns the first index in which an element of the collection satisfies the given predicate.
- [last(where:)](<string/last(where_).md>) — Returns the last element of the sequence that satisfies the given predicate.
- [lastIndex(of:)](<string/lastindex(of_).md>) — Returns the last index where the specified value appears in the collection.
- [lastIndex(where:)](<string/lastindex(where_).md>) — Returns the index of the last element in the collection that matches the given predicate.
- [max()](<string/max().md>) — Returns the maximum element in the sequence.
- [max(_:_:)](<string/max(____).md>)
- [max(by:)](<string/max(by_).md>) — Returns the maximum element in the sequence, using the given predicate as the comparison between elements.
- [min()](<string/min().md>) — Returns the minimum element in the sequence.
- [min(_:_:)](<string/min(____).md>)
- [min(by:)](<string/min(by_).md>) — Returns the minimum element in the sequence, using the given predicate as the comparison between elements.

### Getting Substrings

- [subscript(_:)](<string/subscript(__)-2so14.md>) — Accesses a contiguous subrange of the collection’s elements.
- [subscript(_:)](<string/subscript(__)-4h7s3.md>) — Accesses the contiguous subrange of the collection’s elements specified by a range expression.
- [subscript(_:)](<string/subscript(__)-4al9c.md>)
- [prefix(_:)](<string/prefix(__).md>) — Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
- [prefix(through:)](<string/prefix(through_).md>) — Returns a subsequence from the start of the collection through the specified position.
- [prefix(upTo:)](<string/prefix(upto_).md>) — Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [prefix(while:)](<string/prefix(while_).md>) — Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.
- [suffix(_:)](<string/suffix(__).md>) — Returns a subsequence, up to the given maximum length, containing the final elements of the collection.
- [suffix(from:)](<string/suffix(from_).md>) — Returns a subsequence from the specified position to the end of the collection.

### Splitting a String

- [split(separator:maxSplits:omittingEmptySubsequences:)](<string/split(separator_maxsplits_omittingemptysubsequences_).md>) — Returns the longest possible subsequences of the collection, in order, around elements equal to the given element.
- [split(maxSplits:omittingEmptySubsequences:whereSeparator:)](<string/split(maxsplits_omittingemptysubsequences_whereseparator_).md>) — Returns the longest possible subsequences of the collection, in order, that don’t contain elements satisfying the given predicate.

### Getting Characters and Bytes

- [subscript(_:)](<string/subscript(__)-lc0v.md>) — Accesses the character at the given position.
- [first](string/first.md) — The first element of the collection.
- [last](string/last.md) — The last element of the collection.
- [randomElement()](<string/randomelement().md>) — Returns a random element of the collection.
- [randomElement(using:)](<string/randomelement(using_).md>) — Returns a random element of the collection, using the given generator as a source for randomness.

### Working with Encodings

- [availableStringEncodings](string/availablestringencodings.md) — An array of the encodings that strings support in the application’s environment.
- [defaultCStringEncoding](string/defaultcstringencoding.md) — The C-string encoding assumed for any method accepting a C string as an argument.
- [localizedName(of:)](<string/localizedname(of_).md>) — Returns a human-readable string giving the name of the specified encoding.
- [isContiguousUTF8](string/iscontiguousutf8.md) — Returns whether this string’s storage contains validly-encoded UTF-8 contents in contiguous memory.
- [makeContiguousUTF8()](<string/makecontiguousutf8().md>) — If this string is not contiguous, make it so. If this mutates the string, it will invalidate any pre-existing indices.
- [withUTF8(_:)](<string/withutf8(__).md>) — Runs `body` over the content of this string in contiguous memory. If this string is not contiguous, this will first make it contiguous, which will also speed up subsequent access. If this mutates the string, it will invalidate any pre-existing indices.

### Working with String Views

- [unicodeScalars](string/unicodescalars.md) — The string’s value represented as a collection of Unicode scalar values.
- [init(_:)](<string/init(__)-2t931.md>) — Creates a string corresponding to the given collection of Unicode scalars.
- [init(_:)](<string/init(__)-11jx3.md>) — Creates a String having the given content.
- [utf16](string/utf16.md) — A UTF-16 encoding of `self`.
- [init(_:)](<string/init(__)-wbcx.md>) — Creates a string corresponding to the given sequence of UTF-16 code units.
- [init(_:)](<string/init(__)-expd.md>) — Creates a String having the given content.
- [utf8](string/utf8.md) — A UTF-8 encoding of `self`.
- [init(_:)](<string/init(__)-6sprj.md>) — Creates a string corresponding to the given sequence of UTF-8 code units.
- [init(_:)](<string/init(__)-83bub.md>) — Creates a String having the given content.

### Transforming a String’s Characters

- [compactMap(_:)](<string/compactmap(__).md>) — Returns an array containing the non-`nil` results of calling the given transformation with each element of this sequence.
- [flatMap(_:)](<string/flatmap(__)-i3m9.md>) — Returns an array containing the concatenated results of calling the given transformation with each element of this sequence.
- [flatMap(_:)](<string/flatmap(__)-6chuq.md>)
- [reduce(_:_:)](<string/reduce(____).md>) — Returns the result of combining the elements of the sequence using the given closure.
- [reduce(into:_:)](<string/reduce(into___).md>) — Returns the result of combining the elements of the sequence using the given closure.
- [lazy](string/lazy.md) — A sequence containing the same elements as this sequence, but on which some operations, such as `map` and `filter`, are implemented lazily.

### Iterating over a String’s Characters

- [forEach(_:)](<string/foreach(__).md>) — Calls the given closure on each element in the sequence in the same order as a `for`-`in` loop.
- [enumerated()](<string/enumerated().md>) — Returns a sequence of pairs (_n_, _x_), where _n_ represents a consecutive integer starting at zero and _x_ represents an element of the sequence.
- [makeIterator()](<string/makeiterator().md>) — Returns an iterator over the elements of the collection.
- [underestimatedCount](string/underestimatedcount.md) — A value less than or equal to the number of elements in the collection.

### Reordering a String’s Characters

- [sorted()](<string/sorted().md>) — Returns the elements of the sequence, sorted.
- [sorted(by:)](<string/sorted(by_).md>) — Returns the elements of the sequence, sorted using the given predicate as the comparison between elements.
- [reversed()](<string/reversed().md>) — Returns a view presenting the elements of the collection in reverse order.
- [shuffled()](<string/shuffled().md>) — Returns the elements of the sequence, shuffled.
- [shuffled(using:)](<string/shuffled(using_).md>) — Returns the elements of the sequence, shuffled using the given generator as a source for randomness.

### Getting C Strings

- [utf8CString](string/utf8cstring.md) — A contiguously stored null-terminated UTF-8 representation of the string.
- [withCString(_:)](<string/withcstring(__).md>) — Calls the given closure with a pointer to the contents of the string, represented as a null-terminated sequence of UTF-8 code units.
- [withCString(encodedAs:_:)](<string/withcstring(encodedas___).md>) — Calls the given closure with a pointer to the contents of the string, represented as a null-terminated sequence of code units.

### Working with Paths

- [init(_:)](<string/init(__)-3a5mh.md>) _(deprecated)_
- [init(validatingUTF8:)](<string/init(validatingutf8_)-6i0in.md>) _(deprecated)_

### Manipulating Indices

- [startIndex](string/startindex.md) — The position of the first character in a nonempty string.
- [endIndex](string/endindex.md) — A string’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [index(after:)](<string/index(after_).md>) — Returns the position immediately after the given index.
- [formIndex(after:)](<string/formindex(after_).md>) — Replaces the given index with its successor.
- [index(before:)](<string/index(before_).md>) — Returns the position immediately before the given index.
- [formIndex(before:)](<string/formindex(before_).md>) — Replaces the given index with its predecessor.
- [index(_:offsetBy:)](<string/index(__offsetby_).md>) — Returns an index that is the specified distance from the given index.
- [index(_:offsetBy:limitedBy:)](<string/index(__offsetby_limitedby_).md>) — Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [formIndex(_:offsetBy:)](<string/formindex(__offsetby_).md>) — Offsets the given index by the specified distance.
- [formIndex(_:offsetBy:limitedBy:)](<string/formindex(__offsetby_limitedby_).md>) — Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [distance(from:to:)](<string/distance(from_to_).md>) — Returns the distance between two indices.
- [indices](string/indices-swift.property.md) — The indices that are valid for subscripting the collection, in ascending order.

### Creating a Range Expression

- [...(_:_:)](<string/'...(____).md>) — Returns a closed range that contains both of its bounds.
- [...(_:)](<string/'...(__)-4mm4o.md>) — Returns a partial range up to, and including, its upper bound.
- [...(_:)](<string/'...(__)-6ct5g.md>) — Returns a partial range extending upward from a lower bound.

### Encoding and Decoding

- [encode(to:)](<string/encode(to_).md>) — Encodes this value into the given encoder.
- [init(from:)](<string/init(from_).md>) — Creates a new instance by decoding from the given decoder.

### Describing a String

- [description](string/description.md) — The value of this string.
- [debugDescription](string/debugdescription.md) — A representation of the string that is suitable for debugging.
- [customMirror](string/custommirror.md) — A mirror that reflects the `String` instance.
- [hashValue](string/hashvalue.md) — The hash value.
- [hash(into:)](<string/hash(into_).md>) — Hashes the essential components of this value by feeding them into the given hasher.

### Infrequently Used Functionality

- [index(of:)](<string/index(of_).md>) — Returns the first index where the specified value appears in the collection.
- [init(_:)](<string/init(__)-5a5lw.md>)
- [init(stringInterpolation:)](<string/init(stringinterpolation_).md>) — Creates a new instance from an interpolated string literal.
- [init(stringLiteral:)](<string/init(stringliteral_).md>) — Creates an instance initialized to the given string value.
- [init(unicodeScalarLiteral:)](<string/init(unicodescalarliteral_).md>)
- [init(extendedGraphemeClusterLiteral:)](<string/init(extendedgraphemeclusterliteral_).md>)
- [customPlaygroundQuickLook](string/customplaygroundquicklook.md) — A custom playground Quick Look for the `String` instance. _(deprecated)_
- [withContiguousStorageIfAvailable(_:)](<string/withcontiguousstorageifavailable(__).md>) — Executes a closure on the sequence’s contiguous storage.

### Reference Types

- [NSString](../foundation/nsstring.md) — A static, plain-text Unicode string object.
- [NSMutableString](../foundation/nsmutablestring.md) — A dynamic plain-text Unicode string object.

### Related String Types

- [Substring](substring.md) — A slice of a string.
- [StringProtocol](stringprotocol.md) — A type that can represent a string as a collection of characters.
- [Index](string/index.md) — A position of a character or code unit in a string.
- [UnicodeScalarView](string/unicodescalarview.md) — A view of a string’s contents as a collection of Unicode scalar values.
- [UTF16View](string/utf16view.md) — A view of a string’s contents as a collection of UTF-16 code units.
- [UTF8View](string/utf8view.md) — A view of a string’s contents as a collection of UTF-8 code units.
- [Iterator](string/iterator.md) — A type that provides the collection’s iteration interface and encapsulates its iteration state.
- [Encoding](string/encoding.md)

### Structures

- [Comparator](string/comparator.md) — A `String` comparison performed using the given comparison options and locale.
- [IntentInputOptions](string/intentinputoptions.md)
- [StandardComparator](string/standardcomparator.md) — Compares `String`s using one of a fixed set of standard comparison algorithms.

### Initializers

- [init(_:)](<string/init(__)-1oup7.md>)
- [init(_:)](<string/init(__)-2cuu.md>)
- [init(_:)](<string/init(__)-5ruqx.md>)
- [init(cString:)](<string/init(cstring_)-1gatt.md>) _(deprecated)_
- [init(cString:)](<string/init(cstring_)-295hy.md>) _(deprecated)_
- [init(cString:)](<string/init(cstring_)-472zs.md>) — Creates a new string by copying the null-terminated UTF-8 data referenced by the given array.
- [init(cString:)](<string/init(cstring_)-54awj.md>) — Creates a new string by copying the null-terminated UTF-8 data referenced by the given array.
- [init(cString:)](<string/init(cstring_)-cgw2.md>) _(deprecated)_
- [init(cString:encoding:)](<string/init(cstring_encoding_)-358mb.md>) _(deprecated)_
- [init(cString:encoding:)](<string/init(cstring_encoding_)-4ydt6.md>) _(deprecated)_
- [init(copying:)](<string/init(copying_).md>) — Creates a new string, copying the specified code units.
- [init(decoding:)](<string/init(decoding_)-364r2.md>) — On Unix, creates the string `"/"`
- [init(decoding:)](<string/init(decoding_)-9xh58.md>) — Creates a string by interpreting the path component’s content as UTF-8 on Unix and UTF-16 on Windows.
- [init(decodingCString:as:)](<string/init(decodingcstring_as_)-2zmjc.md>) _(deprecated)_
- [init(decodingCString:as:)](<string/init(decodingcstring_as_)-534rp.md>) _(deprecated)_
- [init(describingForTest:)](<string/init(describingfortest_).md>) — Initialize this instance so that it can be presented in a test’s output.
- [init(platformString:)](<string/init(platformstring_)-341sr.md>) _(deprecated)_
- [init(platformString:)](<string/init(platformstring_)-36ydz.md>) _(deprecated)_
- [init(platformString:)](<string/init(platformstring_)-5j2y3.md>) — Creates a string by interpreting the null-terminated platform string as UTF-8 on Unix and UTF-16 on Windows.
- [init(platformString:)](<string/init(platformstring_)-7hjry.md>) — Creates a string by interpreting the null-terminated platform string as UTF-8 on Unix and UTF-16 on Windows.
- [init(utf8String:)](<string/init(utf8string_)-5v4k8.md>) _(deprecated)_
- [init(utf8String:)](<string/init(utf8string_)-7t980.md>) _(deprecated)_
- [init(validating:)](<string/init(validating_)-6r2j9.md>) — On Unix, creates the string `"/"`
- [init(validating:)](<string/init(validating_)-95n8b.md>) — Creates a string from a path component, validating its contents as UTF-8 on Unix and UTF-16 on Windows.
- [init(validating:)](<string/init(validating_)-9dx2b.md>) — Creates a string from a file path, validating its contents as UTF-8 on Unix and UTF-16 on Windows.
- [init(validatingCString:)](<string/init(validatingcstring_)-1x5p0.md>) _(deprecated)_
- [init(validatingCString:)](<string/init(validatingcstring_)-7gjlg.md>) _(deprecated)_
- [init(validatingPlatformString:)](<string/init(validatingplatformstring_)-2920w.md>) — Creates a string by interpreting the null-terminated platform string as UTF-8 on Unix and UTF-16 on Windows.
- [init(validatingPlatformString:)](<string/init(validatingplatformstring_)-8x1kn.md>) _(deprecated)_
- [init(validatingPlatformString:)](<string/init(validatingplatformstring_)-91z6f.md>) — Creates a string by interpreting the null-terminated platform string as UTF-8 on Unix and UTF-16 on Windows.
- [init(validatingPlatformString:)](<string/init(validatingplatformstring_)-go44.md>) _(deprecated)_
- [init(validatingUTF8:)](<string/init(validatingutf8_)-2m5lb.md>) — Creates a new string by copying and validating the null-terminated UTF-8 data referenced by the given array.
- [init(validatingUTF8:)](<string/init(validatingutf8_)-2o7g5.md>) _(deprecated)_
- [init(validatingUTF8:)](<string/init(validatingutf8_)-8awk3.md>) _(deprecated)_

### Instance Properties

- [characters](string/characters.md) — A view of the string’s contents as a collection of characters.
- [utf8Span](string/utf8span.md) — A UTF-8 span over the code units that make up this string.

### Instance Methods

- [data(using:allowLossyConversion:)](<string/data(using_allowlossyconversion_).md>)
- [isTriviallyIdentical(to:)](<string/istriviallyidentical(to_).md>) — Returns a boolean value indicating whether this string is identical to `other`. _(beta)_
- [withMutableCharacters(_:)](<string/withmutablecharacters(__).md>) — Applies the given closure to a mutable view of the string’s characters.
- [withPlatformString(_:)](<string/withplatformstring(__).md>) — Calls the given closure with a pointer to the contents of the string, represented as a null-terminated platform string.

### Type Aliases

- [CharacterView](string/characterview.md) — A view of a string’s contents as a collection of characters.
- [CompareOptions](string/compareoptions.md)
- [EncodingConversionOptions](string/encodingconversionoptions.md)
- [EnumerationOptions](string/enumerationoptions.md)
- [IndexDistance](string/indexdistance.md) — A type that represents the number of steps between two `String.Index` values, where one value is reachable from the other. _(deprecated)_
- [Output](string/output.md)
- [Specification](string/specification.md)
- [UnicodeScalarIndex](string/unicodescalarindex.md) — The index type for a string’s `unicodeScalars` view.
- [UnwrappedType](string/unwrappedtype.md)
- [ValueType](string/valuetype.md)

### Type Properties

- [defaultResolverSpecification](string/defaultresolverspecification.md)

### Type Methods

- [decodeCString(_:as:repairingInvalidCodeUnits:)](<string/decodecstring(__as_repairinginvalidcodeunits_)-2l7u6.md>) _(deprecated)_
- [decodeCString(_:as:repairingInvalidCodeUnits:)](<string/decodecstring(__as_repairinginvalidcodeunits_)-3mvvy.md>)
- [decodeCString(_:as:repairingInvalidCodeUnits:)](<string/decodecstring(__as_repairinginvalidcodeunits_)-9pdmv.md>) _(deprecated)_

### Default Implementations

- [Attachable Implementations](string/attachable-implementations.md)
- [BidirectionalCollection Implementations](string/bidirectionalcollection-implementations.md)
- [CodingKeyRepresentable Implementations](string/codingkeyrepresentable-implementations.md)
- [Collection Implementations](string/collection-implementations.md)
- [Comparable Implementations](string/comparable-implementations.md)
- [CustomDebugStringConvertible Implementations](string/customdebugstringconvertible-implementations.md)
- [CustomReflectable Implementations](string/customreflectable-implementations.md)
- [CustomStringConvertible Implementations](string/customstringconvertible-implementations.md)
- [Decodable Implementations](string/decodable-implementations.md)
- [Encodable Implementations](string/encodable-implementations.md)
- [Equatable Implementations](string/equatable-implementations.md)
- [ExpressibleByExtendedGraphemeClusterLiteral Implementations](string/expressiblebyextendedgraphemeclusterliteral-implementations.md)
- [ExpressibleByStringInterpolation Implementations](string/expressiblebystringinterpolation-implementations.md)
- [ExpressibleByStringLiteral Implementations](string/expressiblebystringliteral-implementations.md)
- [ExpressibleByUnicodeScalarLiteral Implementations](string/expressiblebyunicodescalarliteral-implementations.md)
- [Hashable Implementations](string/hashable-implementations.md)
- [LosslessStringConvertible Implementations](string/losslessstringconvertible-implementations.md)
- [RangeReplaceableCollection Implementations](string/rangereplaceablecollection-implementations.md)
- [Sequence Implementations](string/sequence-implementations.md)
- [StringProtocol Implementations](string/stringprotocol-implementations.md)
- [TextOutputStream Implementations](string/textoutputstream-implementations.md)
- [TextOutputStreamable Implementations](string/textoutputstreamable-implementations.md)

## See Also

### Standard Library

- [Int](int.md) — A signed integer value type.
- [Double](double.md) — A double-precision (64-bit), floating-point value type.
- [Array](array.md) — An ordered, random-access collection.
- [Dictionary](dictionary.md) — A collection whose elements are key-value pairs.
- [Swift Standard Library](swift-standard-library.md) — Solve complex problems and write high-performance, readable code.
