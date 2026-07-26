---
title: Strings in Swift 4
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2017/11/swift-4-strings/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:35d1a5a0bf8254b2'
translated: false
---

> 原文：[Strings in Swift 4](https://oleb.net/blog/2017/11/swift-4-strings/)　·　Ole Begemann

# Strings in Swift 4

_This is an excerpt from the _Strings_ chapter in our book [_Advanced Swift_](https://www.objc.io/books/advanced-swift/). The new edition, revised and extended for Swift 4, is out now._

---

All modern programming languages have support for Unicode strings, but that often only means that the native string type can store Unicode data — it’s not a promise that simple operations like getting the length of a string will return “sensible” results. In fact, most languages, and in turn most string manipulation code written in those languages, exhibit a certain level of denial about Unicode’s inherent complexity. This can lead to some unpleasant bugs.

Swift’s string implementation goes to heroic efforts to be as Unicode-correct as possible. A [`String`](https://developer.apple.com/documentation/swift/string) in Swift is a collection of [`Character`](https://developer.apple.com/documentation/swift/character) values, where a `Character` is what a human reader of a text would perceive as a single character, regardless of how many Unicode code points it’s composed of. As a result, all standard `Collection` operations like [`count`](https://developer.apple.com/documentation/swift/string/2894926-count) or [`prefix(5)`](https://developer.apple.com/documentation/swift/string/2894830-prefix) work on the level of user-perceived characters.

This is great for correctness, but it comes at a price, mostly in terms of unfamiliarity; if you’re used to manipulating strings with integer indices in other languages, Swift’s design will seem unwieldy at first, leaving you wondering. Why can’t I write `str[999]` to access a string’s one-thousandth character? Why doesn’t `str[idx+1]` get the next character? Why can’t I loop over a range of `Character` values such as `"a"..."z"`?

It also has performance implications: `String` does _not_ support random access, i.e. jumping to an arbitrary character is not an _O(1)_ operation. It can’t be — when characters have variable width, the string doesn’t know where the _n_^th character is stored without looking at all characters that come before it.

In this chapter, we’ll discuss the string architecture in detail, as well as some techniques for getting the most out of Swift strings in terms of functionality and performance. But we’ll start with an overview of the required Unicode terminology.

# Unicode, Or: No More Fixed Width

Things used to be so simple. [ASCII](https://en.wikipedia.org/wiki/ASCII) strings were a sequence of integers between 0 and 127. If you stored them in an 8-bit byte, you even had a bit to spare! Since every character was of a fixed size, ASCII strings could be random access.

But ASCII wasn’t enough if you were writing in anything other than English or for a non-U.S. audience; other countries and languages needed other characters (even English-speaking Britain needed a £ sign). Most of them needed more characters than would fit into seven bits. [ISO 8859](https://en.wikipedia.org/wiki/ISO/IEC_8859) takes the extra bit and defines 16 different encodings above the ASCII range, such as Part 1 (ISO 8859-1, aka Latin-1), covering several Western European languages; and Part 5, covering languages that use the Cyrillic alphabet.

This is still limiting, though. If you want to use ISO 8859 to write in Turkish about Ancient Greek, you’re out of luck, since you’d need to pick either Part 7 (Latin/Greek) or Part 9 (Turkish). And eight bits is still not enough to encode many languages. For example, Part 6 (Latin/Arabic) doesn’t include the characters needed to write Arabic-script languages such as Urdu or Persian. Meanwhile, Vietnamese — which is based on the Latin alphabet but with a large number of diacritic combinations — only fits into eight bits by replacing a handful of ASCII characters from the lower half. And this isn’t even an option for other East Asian languages.

When you run out of room with a fixed-width encoding, you have a choice: either increase the size, or switch to variable-width encoding. Initially, [Unicode](https://en.wikipedia.org/wiki/Unicode) was defined as a 2-byte fixed-width format, now called [UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set). This was before reality set in, and it was accepted that even two bytes would not be sufficient, while four would be horribly inefficient for most purposes.

So today, Unicode is a variable-width format, and it’s variable in two different senses: in the combining of code units into Unicode scalars, and in the combining of scalars into characters.

Unicode data can be encoded with many different widths of _[code unit](https://www.unicode.org/glossary/#code_unit),_ most commonly 8 ([UTF-8](https://en.wikipedia.org/wiki/UTF-8)) or 16 ([UTF-16](https://en.wikipedia.org/wiki/UTF-16)) bits. UTF-8 has the added benefit of being backwardly compatible with 8-bit ASCII — something that’s helped it overtake ASCII as the most popular encoding on the web. Swift represents UTF-16 and UTF-8 code units as `UInt16` and `UInt8` values, respectively (aliased as [`Unicode.UTF16.CodeUnit`](https://developer.apple.com/documentation/swift/unicode.utf8/codeunit) and [`Unicode.UTF8.CodeUnit`](https://developer.apple.com/documentation/swift/unicode.utf16/codeunit)).

A [_code point_](https://www.unicode.org/glossary/#code_point) in Unicode is a single value in the Unicode code space with a possible value from `0` to `0x10FFFF` (in decimal: 1,114,111). Only about 137,000 of the 1.1 million available code points are currently in use, so there’s a lot of room for more emoji. A given code point might take a single code unit if you’re using [UTF-32](https://en.wikipedia.org/wiki/UTF-32), or it might take between one and four if you’re using UTF-8. The first 256 Unicode code points match the characters found in Latin-1.

[Unicode _scalars_](https://www.unicode.org/glossary/#unicode_scalar_value) are almost, but not quite, the same as code points. They’re all the code points _except_ the 2,048 [_surrogate code points_](https://en.wikipedia.org/wiki/UTF-16#U.2BD800_to_U.2BDFFF) in the range `0xD800–0xDFFF`, i.e. the code points used for the leading and trailing codes that indicate pairs in UTF-16 encoding. Scalars are represented in Swift string literals as `"\u{xxxx}"`, where xxxx represents hex digits. So the euro sign can be written in Swift as either `"€"` or `"\u{20AC}"`. The corresponding Swift type is [`Unicode.Scalar`](https://developer.apple.com/documentation/swift/unicode.scalar), which is a wrapper around a [`UInt32`](https://developer.apple.com/documentation/swift/uint32) value.

To represent each Unicode scalar by a single code unit, you’d need a 21-bit encoding scheme (which usually gets rounded up to 32-bit, i.e. UTF-32), but even that wouldn’t get you a fixed-width encoding: Unicode is still a variable-width format when it comes to “characters.” What a user might consider “a single character” — as displayed on the screen — might require multiple scalars composed together. The Unicode term for such a user-perceived character is _[(extended) grapheme cluster](https://www.unicode.org/glossary/#extended_grapheme_cluster)._

The rules for how scalars form grapheme clusters determine how text is segmented. For example, if you hit the backspace key on your keyboard, you expect your text editor to delete exactly one grapheme cluster, even if that “character” is composed of multiple Unicode scalars, each of which may use a varying number of code units in the text’s representation in memory. Grapheme clusters are represented in Swift by the `Character` type, which can encode an arbitrary number of scalars, as long as they form a single user-perceived character. We’ll see some examples of this in the next section.

# Grapheme Clusters and Canonical Equivalence

## Combining Marks

A quick way to see how `String` handles Unicode data is to look at the two different ways to write é. Unicode defines [U+00E9](https://codepoints.net/U+00E9), _Latin small letter e with acute,_ as a single value. But you can also write it as the [plain letter e](https://codepoints.net/U+0065), followed by [U+0301](https://codepoints.net/U+0301), _combining acute accent._ In both cases, what’s displayed is é, and a user probably has a reasonable expectation that two strings displayed as “résumé” would not only be equal to each other but also have a “length” of six characters, no matter which technique was used to produce the é in either one. They would be what the Unicode specification describes as _[canonically equivalent](https://www.unicode.org/glossary/#canonical_equivalent)._

And in Swift, this is exactly the behavior you get:

```
let single = "Pok\u{00E9}mon"
let double = "Poke\u{0301}mon"
```

They both display identically:

```
(single, double) // → ("Pokémon", "Pokémon")
```

And both have the same character count:

```
single.count // → 7
double.count // → 7
```

Consequently, they also compare equal:

```
single == double // → true
```

Only if you drop down to a view of the underlying representation can you see that they’re different:

```
single.utf16.count // → 7
double.utf16.count // → 8
```

Contrast this with [`NSString`](https://developer.apple.com/documentation/foundation/nsstring) in Foundation: the two strings aren’t equal, and the [`length`](https://developer.apple.com/documentation/foundation/nsstring/1414212-length) property — which many programmers probably use to count the number of characters to be displayed on the screen — gives different results:

```
import Foundation

let nssingle = single as NSString
nssingle.length // → 7
let nsdouble = double as NSString
nsdouble.length // → 8
nssingle == nsdouble // → false
```

Here, `==` is defined as the version for comparing two [`NSObject`](https://developer.apple.com/documentation/objectivec/nsobject)s:

```
extension NSObject: Equatable {
    static func ==(lhs: NSObject, rhs: NSObject) -> Bool {
        return lhs.isEqual(rhs)
    }
}
```

In the case of `NSString`, this will do a literal comparison on the level of UTF-16 code units, rather than one accounting for equivalent but differently composed characters. Most string APIs in other languages work this way too. If you really want to perform a canonical comparison, you must use [`NSString.compare(_:)`](https://developer.apple.com/documentation/foundation/nsstring/1414082-compare). Didn’t know that? Enjoy your future undiagnosable bugs and grumpy international user base.

Of course, there’s one big benefit to just comparing code units: it’s faster! This is an effect that can still be achieved with Swift strings, via the `utf16` view:

```
single.utf16.elementsEqual(double.utf16) // → false
```

Why does Unicode support multiple representations of the same character at all? The existence of precomposed characters is what enables the opening range of Unicode code points to be compatible with Latin-1, which already had characters like é and ñ. While they might be a pain to deal with, it makes conversion between the two encodings quick and simple.

And ditching precomposed forms wouldn’t have helped anyway, because composition doesn’t just stop at pairs; you can compose more than one diacritic together. For example, [Yoruba](https://en.wikipedia.org/wiki/Yoruba_language) has the character ọ́, which could be written three different ways: by composing ó with a dot, or by composing ọ with an acute, or by composing o with both an acute and a dot. And for that last one, the two diacritics can be in either order! So these are all equal:

```
let chars: [Character] = [
    "\u{1ECD}\u{300}",      // ọ́
    "\u{F2}\u{323}",        // ọ́
    "\u{6F}\u{323}\u{300}", // ọ́
    "\u{6F}\u{300}\u{323}"  // ọ́
]
let allEqual = chars.dropFirst()
    .all(matching: { $0 == chars.first }) // → true
```

The `all(matching:)` method checks if the condition is true for all elements in a sequence:

```
extension Sequence {
    func all(matching predicate: (Element) throws -> Bool) rethrows -> Bool {
        for element in self {
            if try !predicate(element) {
                return false
            }
        }
        return true
    }
}
```

In fact, some diacritics can be added ad infinitum. A [famous internet meme](http://knowyourmeme.com/memes/zalgo) illustrates this nicely:

```
let zalgo = "s̼̐͗͜o̠̦̤ͯͥ̒ͫ́ͅo̺̪͖̗̽ͩ̃͟ͅn̢͔͖͇͇͉̫̰ͪ͑"

zalgo.count // → 4
zalgo.utf16.count // → 36
```

In the above, `zalgo.count` (correctly) returns 4, while `zalgo.utf16.count` returns 36. And if your code doesn’t work correctly with internet memes, then what good is it, really?

Unicode’s grapheme breaking rules even affect you when all strings you deal with are pure ASCII: [CR](https://codepoints.net/U+000D)+[LF](https://codepoints.net/U+000A), the character pair of carriage return and line feed that’s commonly used as a newline on Windows, is a single grapheme:

```
// CR+LF is a single Character
let crlf = "\r\n"
crlf.count // → 1
```

## Emoji

Strings containing emoji can also be surprising in many other programming languages. Many emoji are assigned Unicode scalars that don’t fit in a single UTF-16 code unit. Languages that represent strings as collections of UTF-16 code units, such as Java or C#, would say that the string [`"😂"`](https://emojipedia.org/face-with-tears-of-joy/) is two “characters” long. Swift handles this case correctly:

```
let oneEmoji = "😂" // U+1F602
oneEmoji.count // → 1
```

Other emoji are composed of multiple scalars. An emoji flag is a combination of two [regional indicator letters](https://en.wikipedia.org/wiki/Regional_Indicator_Symbol) that correspond to an ISO country code. Swift treats it correctly as one `Character`:

```
let flags = "🇧🇷🇳🇿"
flags.count // → 2
```

To inspect the Unicode scalars a string is composed of, use the [`unicodeScalars`](https://developer.apple.com/documentation/swift/string/1539070-unicodescalars) view. Here, we format the scalar values as hex numbers in the common format for code points:

```
flags.unicodeScalars.map {
    "U+\(String($0.value, radix: 16, uppercase: true))"
}
// → ["U+1F1E7", "U+1F1F7", "U+1F1F3", "U+1F1FF"]
```

Skin tones combine a base character such as 👧 with one of five skin tone modifiers (e.g. 🏽, or the type-4 skin tone modifier) to yield the final emoji (e.g. 👧🏽). Again, Swift handles this correctly:

```
let skinTone = "👧🏽" // 👧 + 🏽
skinTone.count // → 1
```

This time, let’s use a Foundation API to apply an [ICU string transform](https://oleb.net/blog/2016/01/icu-text-transforms/) that converts Unicode scalars to their official Unicode names:

```
extension StringTransform {
    static let toUnicodeName = StringTransform(rawValue: "Any-Name")
}

extension Unicode.Scalar {
    /// The scalar’s Unicode name, e.g. "LATIN CAPITAL LETTER A".
    var unicodeName: String {
        // Force-unwrapping is safe because this transform always succeeds
        let name = String(self).applyingTransform(.toUnicodeName,
            reverse: false)!

        // The string transform returns the name wrapped in "\\N{...}". Remove those.
        let prefixPattern = "\\N{"
        let suffixPattern = "}"
        let prefixLength = name.hasPrefix(prefixPattern) ? prefixPattern.count : 0
        let suffixLength = name.hasSuffix(suffixPattern) ? suffixPattern.count : 0
        return String(name.dropFirst(prefixLength).dropLast(suffixLength))
    }
}

skinTone.unicodeScalars.map { $0.unicodeName }
// → ["GIRL", "EMOJI MODIFIER FITZPATRICK TYPE-4"]
```

The essential part of this code snippet is the `applyingTransform(.toUnicodeName, …)` call. The remaining lines clean up the name returned from the transform method by removing the wrapping braces. We code this defensively: we first check whether the string matches the expected pattern and compute the number of characters to strip from the start and end. If the format returned by the transform method changes in the future, it’s better to return the string unchanged than to remove characters we didn’t anticipate. Notice how we use the standard `Collection` methods `dropFirst` and `dropLast` to perform the stripping operation. This is a good example of how you can manipulate a string without doing manual index calculations. It’s also efficient, because `dropFirst` and `dropLast` return a `Substring`, which is a slice of the original string. No new memory allocations are needed until the final step when we create a new `String` from the substring. We’ll have more to say about substrings later in this chapter.

Emoji depicting families and couples, such as [👨‍👩‍👧‍👦](https://emojipedia.org/family-man-woman-girl-boy/) and [👩‍❤️‍👩](https://emojipedia.org/couple-with-heart-woman-woman/), present another challenge to the Unicode standards body. Due to the countless possible combinations of genders and the number of people in a group, providing a separate code point for each variation is problematic. Combine this with a distinct skin tone for each person and it becomes impossible. Unicode solves this by specifying that these emoji are actually sequences of multiple emoji, combined with the invisible [_zero-width joiner_](https://codepoints.net/U+200D) (ZWJ) character (U+200D). So the family 👨‍👩‍👧‍👦 is really [_man_ 👨](https://emojipedia.org/man/) + ZWJ + [_woman_ 👩](https://emojipedia.org/woman/) + ZWJ + [_girl_ 👧](https://emojipedia.org/girl/) + ZWJ + [_boy_ 👦](https://emojipedia.org/boy/). The ZWJ serves as an indicator to the operating system that it should use a single glyph if available.

You can verify that this is really what’s going on:

```
let family1 = "👨‍👩‍👧‍👦"
let family2 = "👨\u{200D}👩\u{200D}👧\u{200D}👦"
family1 == family2 // → true
```

And once again, Swift is smart enough to treat such a sequence as a single `Character`:

```
family1.count // → 1
family2.count // → 1
```

New emoji for professions introduced in 2016 are ZWJ sequences too. For example, the [_female firefighter_ 👩‍🚒](https://emojipedia.org/female-firefighter/) is composed of [_woman_ 👩](https://emojipedia.org/woman/) + ZWJ + [_fire engine_ 🚒](https://emojipedia.org/fire-engine/), and the [_male health worker_ 👨‍⚕️](https://emojipedia.org/male-health-worker/) is a sequence of [_man_ 👨](https://emojipedia.org/man/) + ZWJ + [_staff of aesculapius_ ⚕](https://emojipedia.org/staff-of-aesculapius/).

Rendering these sequences into a single glyph is the task of the operating system. On Apple platforms in 2017, the OS includes glyphs for the subset of sequences the Unicode standard lists as “[recommended for general interchange](https://unicode.org/emoji/charts/emoji-zwj-sequences.html)” (RGI), i.e. the ones “most likely to be widely supported across multiple platforms.” When no glyph is available for a syntactically valid sequence, the text rendering system falls back to rendering each component as a separate glyph. Notice that this can cause a mismatch “in the other direction” between user-perceived characters and what Swift sees as a grapheme cluster; all examples up until now were concerned with programming languages _overcounting_ characters, but here we see the reverse. As an example, family sequences containing skin tones are currently not part of the RGI subset. But even though most operating systems currently render such a sequence as multiple glyphs, Swift still counts it as a single `Character` because the Unicode text segmentation rules are not concerned with rendering:

```
// Family with skin tones is rendered as multiple glyphs
// on most platforms in 2017
let family3 = "👱🏾\u{200D}👩🏽\u{200D}👧🏿\u{200D}👦🏻" // → "👱🏾‍👩🏽‍👧🏿‍👦🏻"
// But Swift still counts it as a single Character
family3.count // → 1
```

[Microsoft can already render this](https://blog.emojipedia.org/diverse-emoji-families-come-to-windows/) and other variations as a single glyph, by the way, and the other OS vendors will almost certainly follow soon. But the point still stands: no matter how carefully a string API is designed, text is so complicated that it may never catch all edge cases.

In the examples we discussed in this section, we treated the length of a string as a proxy for all sorts of things that can go wrong when a language doesn’t take the full complexity of Unicode into account. Just think of the gibberish a simple task such as reversing a string can produce in a programming language that doesn’t process strings by grapheme clusters when the string contains composed character sequences. This isn’t a new problem, but the emoji explosion has made it much more likely that bugs caused by sloppy text handling will come to the surface, even if your user base is predominantly English-speaking. And the magnitude of errors has increased as well: whereas a decade ago a botched accented character would cause an off-by-one error, messing up a modern emoji can easily cause results to be off by 10 or more “characters.” For example, a four-person family emoji is 11 (UTF-16) or 25 (UTF-8) code units long:

```
family1.count // → 1
family1.utf16.count // → 11
family1.utf8.count // → 25
```

It’s not that other languages don’t have Unicode-correct APIs at all — most do. For instance, `NSString` has the [`enumerateSubstrings`](https://developer.apple.com/documentation/foundation/nsstring/1416774-enumeratesubstrings) method that can be used to walk through a string by grapheme clusters. But defaults matter; Swift’s priority is to do the correct thing by default. And if you ever need to drop down to a lower level of abstraction, `String` provides views that let you operate directly on Unicode scalars or code units. We’ll say more about those below.

# Strings and Collections

As we’ve seen, `String` is a collection of `Character` values. In Swift’s first three years of existence, `String` went back and forth between conforming and not conforming to the [`Collection`](https://developer.apple.com/documentation/swift/collection#) protocol. The argument for _not_ adding the conformance was that programmers would expect all generic collection-processing algorithms to be completely safe and Unicode-correct, which wouldn’t necessarily be true for all edge cases.

As a simple example, you might assume that if you concatenate two collections, the resulting collection’s length would be the sum of the lengths of the two source collections. But this doesn’t hold for strings if a suffix of the first string forms a grapheme cluster with a prefix of the second string:

```
let flagLetterJ = "🇯"
let flagLetterP = "🇵"
let flag = flagLetterJ + flagLetterP // → "🇯🇵"
flag.count // → 1
flag.count == flagLetterJ.count + flagLetterP.count // → false
```

To this end, `String` itself was not made a `Collection` in Swift 2 and 3; a collection-of-characters view was moved to a property, [`characters`](https://developer.apple.com/documentation/swift/string/1540072-characters), which put it on a footing similar to the other collection views: [`unicodeScalars`](https://developer.apple.com/documentation/swift/string/1539070-unicodescalars), [`utf8`](https://developer.apple.com/documentation/swift/string/1539703-utf8), and [`utf16`](https://developer.apple.com/documentation/swift/string/1541301-utf16). Picking a specific view prompted you to acknowledge you were moving into a “collection-processing” mode and that you should consider the consequences of the algorithm you were about to run.

In practice, the loss in usability and learnability caused by this change turned out to vastly outweigh the gain in correctness for a few edge cases that are rarely relevant in real code (unless you’re writing a text editor). So `String` was made a `Collection` again in Swift 4. The `characters` view still exists, but only for backward compatibility.

## Bidirectional, Not Random Access

However, for reasons that should be clear from the examples in the previous section, `String` is _not_ a random-access collection. How could it be, when knowing where the _n_^th character of a particular string is involves evaluating just how many Unicode scalars precede that character? For this reason, `String` conforms only to [`BidirectionalCollection`](https://developer.apple.com/documentation/swift/bidirectionalcollection). You can start at either end of the string, moving forward or backward, and the code will look at the composition of the adjacent characters and skip over the correct number of bytes. However, you need to iterate up and down one character at a time.

Keep the performance implications of this in mind when writing string-processing code. Algorithms that depend on random access to maintain their performance guarantees aren’t a good match for Unicode strings. Consider this `String` extension for generating a list of a string’s prefixes, which works by generating an integer range from zero to the string’s length and then mapping over the range to create the prefix for each length:

```
extension String {
    var allPrefixes1: [Substring] {
        return (0...self.count).map(self.prefix)
    }
}

let hello = "Hello"
hello.allPrefixes1 // → ["", "H", "He", "Hel", "Hell", "Hello"]
```

As simple as this code looks, it’s very inefficient. It first walks over the string once to calculate the length, which is fine. But then each of the n + 1 calls to [`prefix`](https://developer.apple.com/documentation/swift/substring/2893985-prefix) is another _O(n)_ operation because `prefix` always starts at the beginning and has to work its way through the string to count the desired number of characters. Running a linear process inside another linear loop means this algorithm is accidentally _O(n^2)_ — as the length of the string increases, the time this algorithm takes increases quadratically.

If possible, an efficient string algorithm should walk over a string only once and then operate on string indices to denote the substrings it’s interested in. Here’s another version of the same algorithm:

```
extension String {
    var allPrefixes2: [Substring] {
        return [""] + self.indices.map { index in self[...index] }
    }
}

hello.allPrefixes2 // → ["", "H", "He", "Hel", "Hell", "Hello"]
```

This code also has to iterate over the string once to generate the [`indices`](https://developer.apple.com/documentation/swift/string/2894806-indices) collection. But once that’s done, the subscripting operation inside `map` is _O(1)_. This makes the whole algorithm _O(n)_.

## Range-Replaceable, Not Mutable

`String` also conforms to [`RangeReplaceableCollection`](https://developer.apple.com/documentation/swift/rangereplaceablecollection). Here’s an example of how you’d replace part of a string by first identifying the appropriate range in terms of string indices and then calling [`replaceSubrange`](https://developer.apple.com/documentation/swift/string/1641462-replacesubrange). The replacement string can have a different length or could even be empty (which would be equivalent to calling [`removeSubrange`](https://developer.apple.com/documentation/swift/string/2893740-removesubrange)):

```
var greeting = "Hello, world!"
if let comma = greeting.index(of: ",") {
    greeting[..<comma] // → "Hello"
    greeting.replaceSubrange(comma..., with: " again.")
}
greeting // → "Hello again."
```

As always, keep in mind that results may be surprising if parts of the replacement string form new grapheme clusters with adjacent characters in the original string.

One collection-like feature strings do _not_ provide is that of [`MutableCollection`](https://developer.apple.com/documentation/swift/mutablecollection). This protocol adds one feature to a collection — that of the single-element [subscript `set`](https://developer.apple.com/documentation/swift/mutablecollection/1640969-subscript) — in addition to `get`. This isn’t to say strings aren’t mutable — as we’ve just seen, they have several mutation methods. But what you can’t do is replace a single character using the subscript operator. The reason comes back to variable-length characters. Most people can probably intuit that a single-element subscript update would happen in constant time, as it does for [`Array`](https://developer.apple.com/documentation/swift/array). But since a character in a string may be of variable width, updating a single character could take linear time in proportion to the length of the string: changing the width of a single element would require shuffling all the later elements up or down in memory. Moreover, indices that come after the replaced index would become invalid through the shuffling, which is equally unintuitive. For these reasons, you have to use `replaceSubrange`, even if the range you pass in is only a single element.

# String Indices

Most programming languages use integers for subscripting strings, e.g. `str[5]` would return the sixth “character” of `str` (for whatever that language’s idea of a “character” is). Swift doesn’t allow this. Why? The answer should sound familiar to you by now: subscripting is supposed to take constant time (intuitively as well as per the requirements of the `Collection` protocol), and looking up the _n_^th `Character` is impossible without looking at all bytes that come before it.

[`String.Index`](https://developer.apple.com/documentation/swift/string.index), the index type used by `String` and its views, is an opaque value that essentially stores a byte offset from the beginning of the string. It’s still an _O(n)_ operation if you want to compute the index for the _n_^th character and have to start at the beginning of the string, but once you have a valid index, subscripting the string with it now only takes _O(1)_ time. And crucially, finding the next index after an existing index is also fast because you can start at the existing index’s byte offset — you don’t need to go back to the beginning again. This is why iterating over the characters in a string in order (forward or backward) is efficient.

String index manipulation is based on the same `Collection` APIs you’d use with any other collection. It’s easy to miss this equivalence since the collections we use by far the most — arrays — use integer indices, and we usually use simple arithmetic to manipulate those. The [`index(after:)`](https://developer.apple.com/documentation/swift/string/1782583-index) method returns the index of the next character:

```
let s = "abcdef"
let second = s.index(after: s.startIndex)
s[second] // → "b"
```

You can automate iterating over multiple characters in one go via the [`index(_:offsetBy:)`](https://developer.apple.com/documentation/swift/string/1786175-index) method:

```
// Advance 4 more characters
let sixth = s.index(second, offsetBy: 4)
s[sixth] // → "f"
```

If there’s a risk of advancing past the end of the string, you can add a [`limitedBy:`](https://developer.apple.com/documentation/swift/anybidirectionalcollection/1781464-index) parameter. The method returns `nil` if it hits the limit before reaching the target index:

```
let safeIdx = s.index(s.startIndex, offsetBy: 400, limitedBy: s.endIndex)
safeIdx // → nil
```

This is undoubtedly more code than simple integer indices would require, but again, that’s the point. If Swift allowed integer subscripting of strings, the temptation to accidentally write horribly inefficient code (e.g. by using integer subscripting inside a loop) would be too big.

Nevertheless, to someone used to dealing with fixed-width characters, working with strings in Swift seems challenging at first — how will you navigate without integer indices? And indeed, some seemingly simple tasks like extracting the first four characters of a string can turn into monstrosities like this one:

```
s[..<s.index(s.startIndex, offsetBy: 4)] // → "abcd"
```

But thankfully, being able to access the string via the `Collection` interface also means you have several helpful techniques at your disposal. Many of the methods that operate on `Array` also work on `String`. Using the `prefix` method, the same thing looks much clearer:

```
s.prefix(4) // → "abcd"
```

(Note that either expression returns a [`Substring`](https://developer.apple.com/documentation/swift/substring); you can convert it back into a `String` by wrapping it in a `String.init`. We’ll talk more about substrings in the next section.)

Iterating over characters in a string is easy without integer indices; just use a `for` loop. If you want to number each character in turn, use [`enumerated()`](https://developer.apple.com/documentation/swift/sequence/1641222-enumerated):

```
for (i, c) in s.enumerated() {
    print("\(i): \(c)")
}
```

Or say you want to find a specific character. In that case, you can use [`index(of:)`](https://developer.apple.com/documentation/swift/string/2893264-index):

```
var hello = "Hello!"
if let idx = hello.index(of: "!") {
    hello.insert(contentsOf: ", world", at: idx)
}
hello // → "Hello, world!"
```

The [`insert(contentsOf:at:)`](https://developer.apple.com/documentation/swift/string/2893571-insert) method inserts another collection of the same element type (e.g. `Character` for strings) before a given index. This doesn’t have to be another `String`; you could insert an array of characters into a string just as easily.

# Substrings

Like all collections, `String` has a specific slice or [`SubSequence`](https://developer.apple.com/documentation/swift/collection/1641276-subsequence) type named [`Substring`](https://developer.apple.com/documentation/swift/substring). A substring is much like an [`ArraySlice`](https://developer.apple.com/documentation/swift/arrayslice): it’s a view of a base string with different start and end indices. Substrings share the text storage of their base strings. This has the huge benefit that slicing a string is a very cheap operation. Creating the `firstWord` variable in the following example requires no expensive copies or memory allocations:

```
let sentence = "The quick brown fox jumped over the lazy dog."
let firstSpace = sentence.index(of: " ") ?? sentence.endIndex
let firstWord = sentence[..<firstSpace] // → "The"
type(of: firstWord) // → Substring.Type
```

Slicing being cheap is especially important in loops where you iterate over the entire (potentially long) string to extract its components. Tasks like finding all occurrences of a word in a text or parsing a CSV file come to mind. A very useful string processing operation in this context is splitting. The [`split`](https://developer.apple.com/documentation/swift/string/2894564-split) method is defined on `Collection` and returns an array of subsequences (i.e. `[Substring]`). Its most common variant is defined like so:

```
extension Collection where Element: Equatable {
    public func split(separator: Element, maxSplits: Int = Int.max,
        omittingEmptySubsequences: Bool = true) -> [SubSequence]
}
```

You can use it like this:

```
let poem = """
    Over the wintry
    forest, winds howl in rage
    with no leaves to blow.
    """
let lines = poem.split(separator: "\n")
// → ["Over the wintry", "forest, winds howl in rage", "with no leaves to blow."]
type(of: lines) // → Array<Substring>.Type
```

This can serve a function similar to the [`components(separatedBy:)`](https://developer.apple.com/documentation/swift/stringprotocol/2923413-components) method `String` inherits from `NSString`, with added configurations for whether or not to drop empty components. Again, no copies of the input string are made. And since there’s another variant of `split` that takes a closure, it can do more than just compare characters. Here’s an example of a primitive word wrap algorithm, where the closure captures a count of the length of the line thus far:

```
extension String {
    func wrapped(after: Int = 70) -> String {
        var i = 0
        let lines = self.split(omittingEmptySubsequences: false) {
            character in
            switch character {
            case "\n", " " where i >= after:
                i = 0
                return true
            default:
                i += 1
                return false
            }
        }
        return lines.joined(separator: "\n")
    }
}

sentence.wrapped(after: 15)
// → "The quick brown\nfox jumped over\nthe lazy dog."
```

Or, consider writing a version that takes a sequence of multiple separators:

```
extension Collection where Element: Equatable {
    func split<S: Sequence>(separators: S) -> [SubSequence]
        where Element == S.Element
    {
        return split { separators.contains($0) }
    }
}
```

This way, you can write the following:

```
"Hello, world!".split(separators: ",! ") // → ["Hello", "world"]
```

## `StringProtocol`

`Substring` has almost the same interface as `String`. This is achieved through a common protocol named [`StringProtocol`](https://developer.apple.com/documentation/swift/stringprotocol), which both types conform to. Since almost the entire string API is defined on `StringProtocol`, you can mostly work with a `Substring` as you would with a `String`. At some point, though, you’ll have to turn your substrings back into `String` instances; like all slices, substrings are only intended for short-term storage, in order to avoid expensive copies during an operation. When the operation is complete and you want to store the results or pass them on to another subsystem, you should create a new `String`. You can do this by initializing a `String` with a `Substring`, as we do in this example:

```
func lastWord(in input: String) -> String? {
    // Process the input, working on substrings
    let words = input.split(separators: [",", " "])
    guard let lastWord = words.last else { return nil }
    // Convert to String for return
    return String(lastWord)
}

lastWord(in: "one, two, three, four, five") // → "five"
```

The rationale for discouraging long-term storage of substrings is that a substring always holds on to the entire original string. A substring representing a single character of a huge string will hold the entire string in memory, even after the original string’s lifetime would normally have ended. Long-term storage of substrings would therefore effectively cause memory leaks because the original strings have to be kept in memory even when they’re no longer accessible.

By working with substrings during an operation and only creating new strings at the end, we defer copies until the last moment and make sure to only incur the cost of those copies that are actually necessary. In the example above, we split the entire (potentially long) string into substrings, but only pay the cost for a single copy of one short substring at the end. (Ignore for a moment that this algorithm isn’t efficient anyway; iterating backward from the end until we find the first separator would be the better approach.)

Encountering a function that only accepts a `Substring` when you want to pass a `String` is less common — most functions should either take a `String` or any `StringProtocol`-conforming type. But if you do need to pass a `String`, the quickest way is to subscript the string with the range operator `...` without specifying any bounds:

```
// Substring with identical start and end index as the base string
let substring = sentence[...]
```

You may be tempted to take full advantage of the existence of `StringProtocol` and convert all your APIs to take `StringProtocol` instances rather than plain `String`s. But the advice of the Swift team is [not to do that](https://forums.swift.org/t/pitch-substring-performance-affordances/6217/5):

> Our general advice is to stick with `String`. Most APIs would be simpler and clearer just using `String` rather than being made generic (which itself can come at a cost), and user conversion on the way in on the few occasions that’s needed isn’t much of a burden.

APIs that are extremely likely to be used with substrings, and at the same time aren’t further generalizable to the `Sequence` or `Collection` level, are an exception to this rule. An example of this in the standard library is the [`joined`](https://developer.apple.com/documentation/swift/sequence/1641243-joined) method. Swift 4 added an overload for sequences with `StringProtocol`-conforming elements:

```
extension Sequence where Element: StringProtocol {
    /// Returns a new string by concatenating the elements of the sequence,
    /// adding the given separator between each element.
    public func joined(separator: String = "") -> String
}
```

This lets you call `joined` directly on an array of substrings (which you got from a call to `split`, for example) without having to map over the array and copy every substring into a new string. This is more convenient and much faster.

The number type initializers that take a string and convert it into a number also take `StringProtocol` values in Swift 4. Again, this is especially handy if you want to process an array of substrings:

```
let commaSeparatedNumbers = "1,2,3,4,5"
let numbers = commaSeparatedNumbers
    .split(separator: ",").flatMap { Int($0) }
// → [1, 2, 3, 4, 5]
```

Since substrings are intended to be short-lived, it’s generally not advisable to return one from a function unless we’re talking about `Sequence` or `Collection` APIs that return slices. If you write a similar function that only makes sense for strings, having it return a substring tells readers that it doesn’t make a copy. Functions that create new strings requiring memory allocations, such as [`uppercased()`](https://developer.apple.com/documentation/swift/stringprotocol/2908613-uppercased), should always return `String` instances.

If you want to extend `String` with new functionality, placing the extension on `StringProtocol` is a good idea to keep the API surface between `String` and `Substring` consistent. `StringProtocol` is explicitly designed to be used whenever you would’ve previously extended `String`. If you want to move existing extensions from `String` to `StringProtocol`, the only change you should have to make is to replace any passing of `self` into an API that takes a concrete `String` with `String(self)`.

Keep in mind, though, that as of Swift 4, `StringProtocol` is not yet intended as a conformance target for your own custom string types. The documentation explicitly warns against it:

> Do not declare new conformances to `StringProtocol`. Only the `String` and `Substring` types of the standard library are valid conforming types.

Allowing developers to write their own string types (with special storage or performance optimizations, for instance) is the eventual goal, but the protocol design hasn’t yet been finalized, so adopting it now may break your code in Swift 5.

_… \<SNIP\> …_

# Recap

Strings in Swift are very different than their counterparts in almost all other mainstream programming languages. When you’re used to strings effectively being arrays of code units, it’ll take a while to switch your mindset to Swift’s approach of prioritizing Unicode correctness over simplicity.

Ultimately, we think Swift makes the right choice. Unicode text is much more complicated than what those other languages pretend it is. In the long run, the time savings from avoided bugs you’d otherwise have written will probably outweigh the time it takes to unlearn integer indexing.

We’re so used to random “character” access that we may not realize how rarely this feature is really needed in string processing code. We hope the examples in this chapter convince you that simple in-order traversal is perfectly fine for most common operations. Forcing you to be explicit about which representation of a string you want to work on — grapheme clusters, Unicode scalars, UTF-16 or UTF-8 code units — is another safety measure; readers of your code will be grateful for it.

When Chris Lattner outlined [the goals for Swift’s string implementation](https://forums.swift.org/t/looking-back-on-swift-3-and-ahead-to-swift-4/3610) in July 2016, he ended with this:

> Our goal is to be better at string processing than Perl!

Swift 4 isn’t quite there yet — too many desirable features are missing, including moving more string APIs from Foundation into the standard library, native language support for regular expressions, string formatting and parsing APIs, and more powerful string interpolation. The good news it that the Swift team has expressed interest in [tackling all these topics in the future](https://github.com/apple/swift/blob/master/docs/StringManifesto.md).

---

_If you liked this excerpt, consider [purchasing the full book](hhttps://www.objc.io/books/advanced-swift/). Thanks!_

_The full chapter in the book is more than twice as long as this article. Additional topics covered in the book include how (and when) to use `String`’s code unit views, and interoperating with Foundation APIs that use strings, such as [`NSRegularExpression`](https://developer.apple.com/documentation/foundation/nsregularexpression) or [`NSAttributedString`](https://developer.apple.com/documentation/foundation/nsattributedstring). Especially the latter can be quite difficult and error-prone. We also discuss other standard library APIs that are based on strings, such as [text output streams](https://developer.apple.com/documentation/swift/textoutputstream) and [`CustomStringConvertible`](https://developer.apple.com/documentation/swift/customstringconvertible)._
