---
title: Strings in Swift 1
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2014/07/swift-strings/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:df423ad64cba8a4d'
translated: false
---

> 原文：[Strings in Swift 1](https://oleb.net/blog/2014/07/swift-strings/)　·　Ole Begemann

# Strings in Swift 1

**Note:** This article describes the situation in Swift 1.0. Please check out [Strings in Swift 4](https://oleb.net/blog/2017/11/swift-4-strings) for an updated version.

In this article, I want to take a closer look at how strings are handled in Swift. I see this as a follow-up to a piece titled [NSString and Unicode](http://www.objc.io/issue-9/unicode.html) that I wrote for [objc.io](http://www.objc.io/) a while ago. Please refer to that article for a more thorough explanation of the Unicode features I mention below. I also assume that you have read the [chapter on Strings and Characters](https://developer.apple.com/library/prerelease/ios/documentation/Swift/Conceptual/Swift_Programming_Language/StringsAndCharacters.html#//apple_ref/doc/uid/TP40014097-CH7-XID_368) in Apple’s Swift book.

[Download this article as a playground](https://oleb.net/media/swift-strings.playground.zip) for Xcode 6 to experiment directly with the code samples. The text is identical to the blog post (except for the footnotes). Feedback welcome. Made with [Swift Playground Builder](https://github.com/jas/swift-playground-builder) by [Jason Sandmeyer](http://jasonsandmeyer.com).

# The String Type in Swift

Strings in Swift are represented by the [`String`](https://developer.apple.com/library/prerelease/ios/documentation/Swift/Conceptual/Swift_Programming_Language/StringsAndCharacters.html) type. A `String` is a collection of `Character` values. A Swift `Character` represents one _perceived_ character (what a person thinks of as a single character, called a _grapheme_). Since Unicode often uses two or more [code points](https://en.wikipedia.org/wiki/Unicode#Architecture_and_terminology) (called a _grapheme cluster_) to form one perceived character, this implies that a `Character` can be composed of _multiple_ [Unicode scalar values](http://www.unicode.org/glossary/#unicode_scalar_value) _if_ they form a single grapheme cluster. (_Unicode scalar_ is the term for any Unicode code point except surrogate pair characters, which are used to encode [UTF-16](https://en.wikipedia.org/wiki/UTF-16).)

```
// This is a single Character composed of 2 Unicode scalars
let encircledLetter: Character = "i\u{20DD}" // "i⃝" U+20DD COMBINING ENCLOSING CIRCLE
```

This change has the potential to prevent many common errors when dealing with string lengths or substrings. It is a huge difference to most^[1](#fn:1) other Unicode-aware string libraries (including `NSString`) where the building blocks of a string are usually UTF-16 code units or single Unicode scalars.

# String and Character Literals

Both `String` and `Character` literals use double quotes. If you want a `Character`, you have to make the type explicit.

```
let a = "A"            // a: String
let b: Character = "B" // b: Character
```

# Counting Characters

Swift strings do not have a `length` property. You can use the global `count()` function (which works on any `CollectionType`, not just strings) to count the number of `Character`s in a string. In the following example, `count()` counts an emoji correctly as one character whereas `NSString` would return a length of 2. The equivalent to `NSString`’s `length` property for Swift strings is to count the elements in the string’s `utf16` representation.

```
let globe = "🌍" // U+1F30D EARTH GLOBE EUROPE-AFRICA
count(globe)     // -> 1

// The equivalent of NSString.length is counting the elements in the string's UTF-16 representation
count(globe.utf16) // -> 2
```

Note that computing the length of a `String` requires iterating over all characters and is therefore an [O(N)](http://rob-bell.net/2009/06/a-beginners-guide-to-big-o-notation/) operation. The reason for this is that different `Character`s require variable amounts of memory to store. While most commonly used characters fit into 16 or even 8 bits, others like emoji need 32 bits^[2](#fn:2), and the storage required for a grapheme cluster is theoretically unbounded since a base character can have unlimited combining marks. In my testing, I also found that a string does not cache its length once it has calculated it — it always takes the same time to compute.

# Grapheme Clusters

Let’s look at some examples how Swift handles grapheme clusters.

## Combining Marks

Certain accented characters (like é) can be represented either as a single code point or as a sequence of two or more code points (e + ​ ́). These are called [canonically equivalent](https://en.wikipedia.org/wiki/Unicode_equivalence) and look identical when rendered. Unlike `NSString`, Swift treats both variants as a single character and counts their length correctly.

```
let precomposedCafe = "caf\u{E9}"       // Using U+00E9 LATIN SMALL LETTER E WITH ACUTE
let decomposedCafe = "cafe" + "\u{301}" // Using e + U+0301 COMBINING ACUTE ACCENT
count(precomposedCafe)                  // -> 4
count(decomposedCafe)                   // -> 4
```

Here is another example using Hangul syllables from the Korean alphabet, taken from Apple’s Swift book. Both variants qualify as a single `Character` value.

```
let precomposedSyllable: Character = "\u{D55C}"                // "한"
let decomposedSyllable: Character = "\u{1112}\u{1161}\u{11AB}" // "한", composed of ᄒ, ᅡ, ᆫ
```

## Variation Sequences

Some fonts provide multiple glyph variants for a single character. Variation selectors are code points that are used to select a specific appearance for the preceding character. What looks like one character to a person can be composed of multiple code points, but Swift correctly treats it as a single character.

```
let umbrella = "☔️"                           // U+2614 UMBRELLA WITH RAIN DROPS
count(umbrella)                               // -> 1
let umbrellaVariation = umbrella + "\u{FE0E}" // Adding a variation selector ☔︎
count(umbrellaVariation)                      // -> 1
```

### Emoji Modifiers

Note that the [custom skin tones](http://blog.emojipedia.org/apple-2015-emoji-changelog-ios-os-x) for emoji that Apple introduced with iOS 8.3 and OS X 10.10.3 are not yet handled correctly in Swift 1.2. You select a custom skin tone by adding one of [five modifier characters](http://www.unicode.org/reports/tr51/tr51-2.html#Diversity) immediately after the emoji character. Swift currently interprets such a sequence as two separate characters. Chris Lattner [confirmed this is a bug](https://devforums.apple.com/message/1126558#1126558).

```
let defaultSkinColor = "👩"                   // U+1F469 WOMAN
count(defaultSkinColor)                       // -> 1 (correct)
let customSkinColor = "👩🏻"                  // U+1F469 + U+1F3FB EMOJI MODIFIER FITZPATRICK TYPE-1-2
count(customSkinColor)                        // -> 2 (wrong)
```

## Regional Indicator Symbols

Unicode does not define code points for national flag symbols. Instead, the standard defines a [method to compose a flag symbol](https://en.wikipedia.org/wiki/Regional_Indicator_Symbol) from two code points that represent an ISO two-letter country code. Again, things that appear as a single character are treated as such:

```
let germany = "🇩🇪" // German flag ("DE") U+1F1E9 U+1F1EA
count(germany)     // -> 1
```

Whether a combination of regional indicator symbols is actually displayed as a flag on your device depends on font support. Currently, most emoji fonts only provide glyphs for ten country flags. (Update April 13, 2015: Apple recently [added 198 new flags](http://blog.emojipedia.org/apple-2015-emoji-changelog-ios-os-x) to its emoji collection with the iOS 8.3 and OS X 10.10.3 updates.) If you use a combination of regional indicator symbols for which no glyph exists, it will be displayed as multiple letters. Now we have a situation where the user sees two separate characters but Swift still treats it as one unit. Semantically, this is plausible since a two-letter country code really represents a single entity; it wouldn’t make sense to separate it in the middle. Moreover, something as basic as computing the length of a string should not depend on the fonts that are installed on the machine that executes the code.

```
let imaginaryCountryCode = "\u{1F1FD}\u{1F1FD}" // U+1F1FD U+1F1FD ("XX")
count(imaginaryCountryCode)                     // -> 1
```

Note that [the Unicode standard does not say that grapheme clusters composed of regional indicators have to be limited to two code points](http://www.unicode.org/reports/tr29/#Grapheme_Cluster_Boundary_Rules). In fact, you can add as many as you want and it will still be treated as a single character:

```
// This is a single Character (!!!)
let multipleFlags: Character = "🇩🇪🇺🇸🇫🇷🇮🇹🇬🇧🇪🇸🇯🇵🇷🇺🇨🇳" // DE US FR IT GB ES JP RU CN
```

Be aware of this, especially if your code combines multiple flags into a single string without any separators between them. Use a non-printing character like `U+200B ZERO WIDTH SPACE` to separate the flags in such a case.

```
let separatedFlags = "🇩🇪\u{200B}🇺🇸\u{200B}🇫🇷\u{200B}🇮🇹\u{200B}🇬🇧\u{200B}🇪🇸\u{200B}🇯🇵\u{200B}🇷🇺\u{200B}🇨🇳"
count(separatedFlags) // -> 17
```

## Ligatures

Another example where Swift’s string library may not do what you expect is ligatures. Some common ligatures (like `"ﬃ"` or `"ĳ"`) exist as single code points in Unicode, and `String` will treat those as a single character despite their appearance. Like precomposed accented characters, code points for these ligatures exist mainly for legacy and compatibility reasons. Since ligatures are more of a font feature than something that should be encoded in a string, anyway, it is probably best to avoid them if you can. In fact, their use [is officially discouraged](http://www.unicode.org/faq/ligature_digraph.html).

```
let ligature = "ﬃ"
count(ligature) // -> 1
```

# Comparing Strings

## Equality

The equality operator `==` treats canonically equivalent strings as equal:

```
decomposedCafe == precomposedCafe // -> true
```

Depending on your requirements, this may or may not be what you want, but it is certainly consistent with the overall design of the `String` type to abstract away as many Unicode details as possible. Rule of thumb: if two strings look equal to the user, they will be equal in your code.

Contrast this with Foundation: `-[NSString isEqualToString:]` uses byte-for-byte comparison to determine equality, so two different normalization forms of the same string are not equal, whereas `-[NSString compare:]` (and its localized/case-insensitive variants) works like Swift’s `==` operator.

```
// -[NSString isEqualToString:] returns not equal
(precomposedCafe as NSString).isEqualToString(decomposedCafe) // -> false

// -[NSString compare] returns equal
precomposedCafe.compare(decomposedCafe) // -> .OrderedSame
```

## Ordered Comparison

Ordering strings with the `<` and `>` operators uses the default [Unicode collation algorithm](http://www.unicode.org/reports/tr10/). In the example below, `"é"` is smaller than `i` because the collation algorithm specifies that characters with combining marks follow right after their base character.

```
"résumé" < "risotto" // -> true
```

The `String` type does not (yet?) come with a method to specify the language to use for collation. You should continue to use `-[NSString compare:options:range:locale:]` or `-[NSString localizedCompare:]` if you need to sort strings that are shown to the user.

In this example, specifying a locale that uses the German phonebook collation yields a different result than the default string ordering:

```
let muffe = "Muffe"
let müller = "Müller"
muffe < müller // -> true

// Comparison using an US English locale yields the same result
let muffeRange = muffe.startIndex..<muffe.endIndex
let en_US = NSLocale(localeIdentifier: "en_US")
muffe.compare(müller, options: nil, range: muffeRange, locale: en_US) // -> .OrderedAscending

// Germany phonebook ordering treats "ü" as "ue".
// Thus, "Müller" < "Muffe"
let de_DE_phonebook = NSLocale(localeIdentifier: "de_DE@collation=phonebook")
muffe.compare(müller, options: nil, range: muffeRange, locale: de_DE_phonebook) // -> .OrderedDescending
```

# String Normalization

The Swift standard library does not include methods for performing [string normalization](http://www.unicode.org/faq/normalization.html). You can use the existing `NSString` API for that:

```
let normalizedCafe = decomposedCafe.precomposedStringWithCanonicalMapping
count(normalizedCafe)
precomposedCafe == normalizedCafe // -> true
```

# Character Indices and Ranges

Because of the way Swift strings are stored, the `String` type does not support random access to its `Character`s via an integer index — there is no direct equivalent to `NSString`’s `characterAtIndex:` method. Conceptually, a `String` can be seen as a doubly linked list of characters rather than an array.

```
let digits = "0123456789"

// The subscript operator [] does not accept an Int argument.
let someDigit = digits[5] // -> error: cannot subscript String with an Int
```

Character and range indices are based on the opaque `String.Index` type, which implements the `BidirectionalIndex` protocol (an extension of the `ForwardIndex` protocol). To construct an index for a specific position, you have to first ask the string for its `startIndex` and then use the global `advance()` function^[3](#fn:3) to iterate over all characters between the beginning of the string and the target position (again, an O(N) operation; `advance()` will simply call `successor()` several times):

```
let position = 3
let index = advance(digits.startIndex, position)
let character = digits[index] // -> "3"
```

(As an alternative, you can begin at `endIndex` and `advance()` by a negative value from there.)

Another implication of this design is that `String.Index` values are not freely interchangeable between strings. For example, the following code yields a bad result because the string we operate on uses different amounts of storage for its characters than the string we created the `index` for.

```
let clockFaces = "🕛🕐🕑🕒🕓🕔🕕🕖🕗🕘🕙🕚" // Clock faces emoji
let threeOClock = clockFaces[index]          // bad result
```

Use the `distance()` function to convert a `String.Index` into an integer representation:

```
let characterToFind: Character = "7"
if let characterIndex = find(digits, characterToFind) {
    let characterPosition = distance(digits.startIndex, characterIndex) // -> 7
} else {
    "'\(characterToFind)' not found"
}
```

String ranges also have to be constructed from `String.Index` values and not from plain integers:

```
let startIndex = advance(digits.startIndex, 3)
let endIndex = advance(startIndex, 4)
let range = startIndex..<endIndex   // same as let range = Range(start: startIndex, end: endIndex)
let someDigits = digits[range]      // -> "3456"
```

## Extending String to Work with Integer Indices

It is easy to write an extension for `String` that makes the subscript operator compatible with `Int`-based indices and ranges. But keep in mind that these are still O(N) operations, even though they may look like simple random access operations on a plain array of characters. [You should probably not do this in your code](https://devforums.apple.com/message/1009537#1009537).

```
extension String
{
    subscript(integerIndex: Int) -> Character
    {
        let index = advance(startIndex, integerIndex)
            return self[index]
    }

    subscript(integerRange: Range<Int>) -> String
    {
        let start = advance(startIndex, integerRange.startIndex)
        let end = advance(startIndex, integerRange.endIndex)
        let range = start..<end
        return self[range]
    }
}

digits[5]     // works now
digits[4...6] // works now
```

# Interoperability with NSString

In [Using Swift with Cocoa and Objective-C](https://developer.apple.com/library/prerelease/ios/documentation/Swift/Conceptual/BuildingCocoaApps/WorkingWithCocoaDataTypes.html#//apple_ref/doc/uid/TP40014216-CH6-XID_40), Apple says this:

> Swift automatically bridges between the `String` type and the `NSString` class. This means that anywhere you use an `NSString` object, you can use a Swift `String` type instead and gain the benefits of both types—the `String` type’s interpolation and Swift-designed APIs and the `NSString` class’s broad functionality. For this reason, you should almost never need to use the `NSString` class directly in your own code. In fact, when Swift imports Objective-C APIs, it replaces all of the `NSString` types with `String` types. When your Objective-C code uses a `Swift` class, the importer replaces all of the `String` types with `NSString` in imported API.
> 
> To enable string bridging, just import Foundation.

For example, you can call the method `-[NSString componentsSeparatedByString:]` on a Swift string. Swift bridges the `String` and the method’s argument) to `NSString` and calls the method. It also automatically bridges the return value from an `NSArray` of `NSString`s to a Swift array of Swift strings (`String[]`).

```
let commaSeparatedNames = "Cook, Ive, Cue, Ahrendts"
let names = commaSeparatedNames.componentsSeparatedByString(", ")
    // -> ["Cook", "Ive", "Cue", "Ahrendts"]
names[0] // -> "Cook"
```

The automatic bridging also applies to ranges. Any `NSString` method that takes or returns an `NSRange` expects a `Range<String.Index>` when called on a Swift string. Passing an `NSRange` causes an error.

```
let statement = "Swift is hard."
let nsRange = NSMakeRange(0, 5)
    // gets bridged to Range<Int>, not Range<String.Index>
statement.stringByReplacingCharactersInRange(nsRange, withString: "Objective-C")
    // -> error: 'NSRange' is not convertible to 'Range<String.Index>'

let swiftRange = statement.startIndex..<advance(statement.startIndex, 5)
statement.stringByReplacingCharactersInRange(swiftRange, withString: "Objective-C")
    // -> "Objective-C is hard."
```

This can be inconvenient at times, especially because it is often easier to work with the integer-based `NSRange`s. In this case, you can opt out of the automatic bridging by manually casting a `String` to `NSString` or by explicitly typing a constant or variable. A method called on an explicitly typed `NSString` expects integer-based `NSRange` values (the return value will still be bridged to `String!` unless you cast it or declare an explicit type).

```
let statementAsNSString: NSString = statement
let newStatement: NSString = statementAsNSString.stringByReplacingCharactersInRange(nsRange, withString: "Objective-C")
    // -> "Objective-C is hard."
```

Similarly, ranges returned by `NSString` methods will be bridged to `Range<String.Index>` if called on a Swift string, but will remain `NSRange` values when called on an `NSString` object.

```
let possibleRange = statement.rangeOfString("hard")  // returns Range<String.Index>?
if let range = possibleRange {
    distance(statement.startIndex, range.startIndex) // -> 9
    distance(statement.startIndex, range.endIndex)   // -> 13
}

let unbridgedRange = statementAsNSString.rangeOfString("hard") // returns NSRange
unbridgedRange.location                                        // -> 9
unbridgedRange.length                                          // -> 4
```

Finally, explicit typing to `NSString` also lets you access the `length` property and `characterAtIndex:` method under their original names:

```
statementAsNSString.length              // -> 14
statementAsNSString.characterAtIndex(0) // -> 83
statement.length              // -> error: 'String' does not have a member named 'length'
statement.characterAtIndex(0) // -> error: 'String' does not have a member named 'characterAtIndex'
```

# Conclusion

Swift’s string implemenation makes working with Unicode easier and significantly less error-prone. As a programmer, you still have to be aware of possible edge cases, but this probably cannot be avoided completely considering the characteristics of Unicode.

The automatic bridging between `String` and `NSString` is welcome but can be confusing at times, especially when dealing with ranges.

An argument could be made that the implementation of `String` as a sequence that requires iterating over characters from the beginning of the string for many operations poses a significant performance problem but I do not think so. My guess is that Apple’s engineers have considered the implications of their implementation and apps that do not deal with enormous amounts of text will be fine. Moreover, the idea that you could get away with an implementation that supports random access of characters is an illusion given the complexity of Unicode.

1. In fact, I’m not aware of any standard string library for any programming language that handles characters like Swift does. Sure, there is usually a way to iterate over a string by grapheme clusters, but the standard methods for getting a string’s length or accessing a character are mostly based on lower-level constructs. I’d love to hear from you if you know a counterexample. [↩︎](#fnref:1)
2. Actually, the maximum size of a code point is 21 bits, but using 32-bit values would be the logical choice. [↩︎](#fnref:2)
3. There is another variant of `advance()` that takes three arguments: `func advance<T : ForwardIndex>(start: T, n: T.DistanceType, end: T) -> T`. This will advance `start` by `n` positions, but not exceed the index passed in `end`. It’s a convenient way to avoid out-of-bounds errors when working with indices and ranges. [↩︎](#fnref:3)
