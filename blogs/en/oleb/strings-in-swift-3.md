---
title: Strings in Swift 3
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2016/08/swift-3-strings/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:e0722dc84bfdf85a'
translated: false
---

> 原文：[Strings in Swift 3](https://oleb.net/blog/2016/08/swift-3-strings/)　·　Ole Begemann

# Strings in Swift 3

**Note:** This article describes the situation in Swift 3.0. Please check out [Strings in Swift 4](https://oleb.net/blog/2017/11/swift-4-strings) for an updated version.

_This is an excerpt from the Strings chapter in [_Advanced Swift_](https://www.objc.io/books/advanced-swift/). [Chris Eidhof](http://chris.eidhof.nl) and I are currently updating the book for Swift 3 (and improving it in the process). This section on strings was originally written by [Airspeed Velocity](https://airspeedvelocity.net) for the first edition of the book, and Chris and myself updated it for the [upcoming edition](https://www.objc.io/blog/2016/08/22/announcements/)._

_I first wrote about [Strings in Swift 1](https://oleb.net/blog/2014/07/swift-strings/) two years ago (and about [Unicode in general](https://www.objc.io/issues/9-strings/unicode/) before that), and I kind of see this article as the spiritual successor to those earlier versions. Many thanks to Airspeed Velocity for allowing me to post it here._

# No More Fixed Width

Things used to be so simple. [ASCII](https://en.wikipedia.org/wiki/ASCII) strings were a sequence of integers between 0 and 127. If you stored them in an 8-bit byte, you even had a bit to spare! Since every character was of a fixed size, ASCII strings could be random access.

But this is only if you were writing in English for a U.S. audience; other countries and languages needed other characters (even English-speaking Britain needed a £ sign). Most of them needed more characters than would fit into seven bits. [ISO/IEC 8859](https://en.wikipedia.org/wiki/ISO/IEC_8859) takes the extra bit and defines 16 different encodings above the ASCII range, such as Part 1 (ISO/IEC 8859-1, aka Latin-1), covering several Western European languages, and Part 5, covering languages that use the Cyrillic alphabet.

But this is still limiting. If you want to use ISO/IEC 8859 to write in Turkish about Ancient Greek, you are out of luck, since you would need to pick either Part 7 (Latin/Greek) or Part 9 (Turkish). And eight bits is still not enough to encode many languages. For example, Part 6 (Latin/Arabic) does not include the characters needed to write Arabic-script languages such as Urdu or Persian. Meanwhile, Vietnamese — which is based on the Latin alphabet but with a large number of diacritic combinations — only fits into eight bits by replacing a handful of ASCII characters from the lower half. And this isn’t even an option for other East Asian languages.

When you run out of room with a fixed-width encoding, you have a choice: either increase the size, or switch to variable-width encoding. Initially, Unicode was defined as a 2-byte fixed-width format, now called [UCS-2](http://justsolve.archiveteam.org/wiki/UCS-2). This was before reality set in, and it was accepted that even two bytes would not be sufficient, while four would be horribly inefficient for most purposes.

So today, Unicode is a variable-width format, and it’s variable in two different senses: in the combining of code units into code points, and in the combining of code points into characters.

Unicode data can be encoded with many different widths of “code unit”, most commonly 8 ([UTF-8](https://en.wikipedia.org/wiki/UTF-8)) or 16 ([UTF-16](https://en.wikipedia.org/wiki/UTF-16)) bits. UTF-8 has the added benefit of being backwardly compatible with 8-bit ASCII — something that has helped it overtake ASCII as the most popular encoding on the web.

A “code point” in Unicode is a single value in the Unicode code space with a possible value from `0` to `0x10FFFF`. Only about 128,000 of the 1.1 million code points possible are currently in use, so there is a lot of room for more emoji. A given code point might take a single code unit if you are using [UTF-32](https://en.wikipedia.org/wiki/UTF-32), or it might take between one and four if you are using UTF-8. The first 256 Unicode code points match the characters found in Latin-1.

Unicode “scalars” are another unit. They are all the code points _except_ the “surrogate” code points, i.e. the code points used for the leading and trailing codes that indicate pairs in UTF-16 encoding. Scalars are represented in Swift string literals as `"\u{xxxx}"`, where xxxx represents hex digits. So the [euro sign](http://www.fileformat.info/info/unicode/char/20ac/index.htm), €, can be written in Swift as `"\u{20AC}"`.

But even when encoded using 32-bit code units, what a user might consider “a single character” — as displayed on the screen — might require multiple code points composed together. Most string manipulation code exhibits a certain level of denial about Unicode’s variable-width nature. This can lead to some unpleasant bugs.

Swift’s string implementation goes to heroic efforts to be as Unicode-correct as possible, or at least when it’s not, to make sure you acknowledge the fact. This comes at a price. [`String`](https://developer.apple.com/reference/swift/string) in Swift is _not_ a collection. Instead, it is a type that presents multiple ways of viewing the string: as a collection of `Character` values; or as a collection of UTF-8, UTF-16, or Unicode scalars.

The Swift [`Character`](https://developer.apple.com/reference/swift/character) type is unlike the other views, in that it can encode an arbitrary number of code points, composed together into a single [“grapheme cluster.”](http://unicode.org/glossary/#grapheme_cluster) We’ll see some examples of this shortly.

For all but the UTF-16 view, these views do _not_ support random access, i.e. measuring the distance between two indices or advancing an index by some number of steps is generally not an [_O(1)_](https://en.wikipedia.org/wiki/Big_O_notation) operation. Even the UTF-16 view is only random access when you import Foundation, more on that below. Some of the views can also be slower than others when performing heavy text processing. In this chapter, we’ll look at the reasons behind this, as well as some techniques for dealing with both functionality and performance.

## Grapheme Clusters and Canonical Equivalence

A quick way to see the difference between `Swift.String` and [`NSString`](https://developer.apple.com/reference/foundation/nsstring) from the Foundation framework in handling Unicode data is to look at the two different ways to write “é”. Unicode defines [U+00E9](http://www.fileformat.info/info/unicode/char/e9/index.htm), “LATIN SMALL LETTER E WITH ACUTE”, as a single value. But you can also write it as the plain letter “e”, followed by [U+0301](http://www.fileformat.info/info/unicode/char/0301/index.htm), “COMBINING ACUTE ACCENT.” In both cases, what is displayed is é, and a user probably has a reasonable expectation that two strings displayed as “résumé” would not only be equal to each other but also have a “length” of six characters, no matter which technique was used to produce the “é” in either one. They would be what the Unicode specification describes as [“canonically equivalent”](https://en.wikipedia.org/wiki/Unicode_equivalence).

And in Swift, this is exactly the behavior you get:

```
let single = "Pok\u{00E9}mon"
let double = "Pok\u{0065}\u{0301}mon"
```

They both display identically:

```
(single, double) // → (.0 "Pokémon", .1 "Pokémon")
```

And both have the same character count:

```
single.characters.count // → 7
double.characters.count // → 7
```

Only if you drop down to a view of the underlying representation can you see that they are different:

```
single.utf16.count // → 7
double.utf16.count // → 8
```

Contrast this with `NSString`: the two strings are not equal, and the `length` property — which many programmers probably use to count the number of characters to be displayed on the screen — gives different results:

```
let nssingle = NSString(characters: [0x0065,0x0301], length: 2)
nssingle.length // → 2
let nsdouble = NSString(characters: [0x00e9], length: 1)
nsdouble.length // → 1
nssingle == nsdouble // → false
```

Here, `==` is defined as the version for comparing two `NSObject`s:

```
extension NSObject: Equatable {
    static func ==(lhs: NSObject, rhs: NSObject) -> Bool {
        return lhs.isEqual(rhs)
    }
}
```

In the case of `NSString`, this will do a literal comparison, rather than one accounting for equivalent but differently composed characters. `NSString.isEqualToString` will do the same, and most string APIs in other languages work this way, too. If you really want to perform a canonical comparison, you must use `NSString.compare`. Didn’t know that? Enjoy your future undiagnosable bugs and grumpy international user base.

Of course, there’s one big benefit to just comparing code units: it’s a lot faster! This is an effect that can still be achieved with Swift strings, via the [`utf16`](https://developer.apple.com/reference/swift/string/1541301-utf16) view:

```
single.utf16.elementsEqual(double.utf16) // → false
```

Why does Unicode support multiple representations at all? The existence of precomposed characters is what enables the opening range of Unicode code points to be compatible with Latin-1, which already had characters like “é” and “ñ”. While they might be a pain to deal with, it makes conversion between the two quick and simple.

Ditching them wouldn’t have helped, because composition doesn’t just stop at pairs; you can compose more than one diacritic together. For example, [Yoruba](https://en.wikipedia.org/wiki/Yoruba_language) has the character “ọ́”, which could be written three different ways: by composing ó with a dot, or by composing ọ with an acute, or by composing o with both an acute and a dot. And for that last one, the two diacritics can be in either order! So these are all equal:

```
let chars: [Character] = [
    "\u{1ECD}\u{300}",      // ọ́
    "\u{F2}\u{323}",        // ọ́
    "\u{6F}\u{323}\u{300}", // ọ́
    "\u{6F}\u{300}\u{323}", // ọ́
]

chars.dropFirst().all { $0 == chars.first }
// → true
```

The `all` method checks if the condition is true for all elements in a sequence and is defined in the chapter on Collections:

```
extension Sequence {
    func all(f: (Iterator.Element) throws -> Bool) rethrows -> Bool {
        for x in self where try !f(x) {
            return false
        }
        return true
    }
}
```

In fact, some diacritics can be added ad infinitum:

```
//
let zalgo = "s̼̐͗͜o̠̦̤ͯͥ̒ͫ́ͅo̺̪͖̗̽ͩ̃͟ͅn̢͔͖͇͇͉̫̰ͪ͑"

zalgo.characters.count // → 4
zalgo.utf16.count      // → 36
```

In the above, `zalgo.characters.count` returns 4, while `zalgo.utf16.count` returns 36. And if your code doesn’t work correctly with [Internet memes](http://knowyourmeme.com/memes/zalgo), then what good is it, really?

Strings containing emoji can also be a little surprising. For example, a row of emoji flags is considered a single character:

```
let flags = "🇳🇱🇬🇧"
flags.characters.count // → 1

// The scalars are the underlying ISO country codes:
flags.unicodeScalars.map { String($0) }.joined(separator: ",")
// → "🇳,🇱,🇬,🇧"
```

On the other hand, `"👩🏾".characters.count` returns 2 (one for the generic character, one for the skin tone) and `"👨‍👨‍👧‍👧".characters.count` returns 4 in Swift 3.0, as the multi-person groupings are composed from individual member emoji joined with the zero-width joiner:

```
"👩🏾".characters.count // → 2
"👨‍👨‍👧‍👧".characters.count // → 4
"👩\u{200D}👩\u{200D}👦\u{200D}👦" == "👩‍👩‍👦‍👦" // → true
```

While the concatenated flags counting as one character is weird but expected behavior, these emoji should really be treated as a single character. [Expect these results to change](https://bugs.swift.org/browse/SR-2413) as soon as Swift updates its rules for grapheme cluster boundaries to [Unicode 9.0](http://www.unicode.org/versions/Unicode9.0.0/), which was released in June 2016.

# Strings and Collections

Strings in Swift have an [`Index`](https://developer.apple.com/reference/swift/string/index) associated type, [`startIndex`](https://developer.apple.com/reference/swift/string/1540930-startindex) and [`endIndex`](https://developer.apple.com/reference/swift/string/1539571-endindex) properties, a [`subscript`](https://developer.apple.com/reference/swift/string/1540052-subscript) that takes the index to fetch a specific character, and an [`index(after:)`](https://developer.apple.com/reference/swift/string/1782583-index) method that advances an index by one.

This means that `String` meets all the criteria needed to qualify as conforming to [`Collection`](https://developer.apple.com/reference/swift/collection). Yet `String` is _not_ a collection. You cannot use it with `for...in`, nor does it inherit all the protocol extensions of `Collection` or [`Sequence`](https://developer.apple.com/reference/swift/sequence).

In theory, you can change this yourself by extending `String`:

```
extension String: Collection {
    // Nothing needed here – it already has the necessary implementations
}

var greeting = "Hello, world!"
greeting.dropFirst(7) // → "world!"
```

However, this is probably not wise. Strings are not collections for a reason — it isn’t just because the Swift team forgot. When Swift 2.0 introduced protocol extensions, this had the huge benefit of granting all collections and sequences method-like access to dozens of useful algorithms. But this also led to some concerns that collection-processing algorithms presenting themselves as methods on strings would give the implicit indication that these methods are completely safe and Unicode-correct, which wouldn’t necessarily be true. Even though `Character` does its best to present combining character sequences as single values, as seen above, there are still some cases where processing a string character by character can result in incorrect results.

To this end, the collection-of-characters view of strings was moved to a property, [`characters`](https://developer.apple.com/reference/swift/string/1540072-characters), which put it on a footing similar to the other collection views: [`unicodeScalars`](https://developer.apple.com/reference/swift/string/1539070-unicodescalars), [`utf8`](https://developer.apple.com/reference/swift/string/1539703-utf8), and [`utf16`](https://developer.apple.com/reference/swift/string/1541301-utf16). Picking a specific view prompts you to acknowledge that you’re moving into a “collection-processing” mode and that you should consider the consequences of the algorithm you’re about to run.

[`CharacterView`](https://developer.apple.com/reference/swift/string.characterview), however, has a special place amongst those views. `String.Index` is actually just a type alias for `CharacterView.Index`. This means that once you have found an index into the character view, you can then index directly into the string with it.

But for reasons that should be clear from the examples in the previous section, the characters view is not a random-access collection. How could it be, when knowing where the _n_^th character of a particular string is involves evaluating just how many code points precede that character?

For this reason, `CharacterView` conforms only to [`BidirectionalCollection`](https://developer.apple.com/reference/swift/bidirectionalcollection). You can start at either end of the string, moving forward or backward, and the code will look at the composition of the adjacent characters and skip over the correct number of bytes. However, you need to iterate up and down one character at a time.

Like all collection indices, String indices do conform to [`Comparable`](https://developer.apple.com/reference/swift/comparable). You might not know how many characters lie between two indices, but you do at least know that one lies before the other.

You can automate iterating over multiple characters in one go via the [`index(_:offsetBy:)`](https://developer.apple.com/reference/swift/string) method:

```
let s = "abcdef"
// Advance 5 from the start
let idx = s.index(s.startIndex, offsetBy: 5)
s[idx] // → "f" (the Character, not the String)
```

If there’s a risk of advancing past the end of the string, you can add a `limitedBy:` parameter. The method returns `nil` if it would need to advance beyond the limit:

```
let safeIdx = s.index(s.startIndex, offsetBy: 400, limitedBy: s.endIndex)
safeIdx // → nil
```

This behavior is new in Swift 3.0. The corresponding method in Swift 2.2, [`advancedBy(_:limit:)`](http://swiftdoc.org/v2.2/protocol/BidirectionalIndexType/#comment-func--advancedby_limit_), did not make a difference between hitting the limit and going beyond it — it returned the end value in both situations. The new API, by returning an optional, is more expressive.

Now, you might look at this and think, “I know! I can use this to give strings integer subscripting!” So you might do something like this:

```
extension String {
    subscript(idx: Int) -> Character {
        guard let strIdx = index(startIndex, offsetBy: idx, limitedBy: endIndex)
            else { fatalError("String index out of bounds") }
        return self[strIdx]
    }
}

s[5] // → "f"
```

However, just as with extending `String` to make it a collection, this kind of extension is best avoided. You might otherwise be tempted to start writing code like this:

```
for i in 0..<5 {
    print(s[i])
}
```

But as simple as this code looks, it’s horribly inefficient. Every time `s` is accessed with an integer, an _O(n)_ function to advance its starting index is run. Running a linear loop inside another linear loop means this `for` loop is accidentally _O(n²)_ — as the length of the string increases, the time this loop takes increases quadratically.

To someone used to dealing with fixed-width characters, this seems challenging at first — how will you navigate without integer indices? And indeed, some seemingly simple tasks like extracting the first four characters of a string can turn into monstrosities like this one:

```
s[s.startIndex..<s.index(s.startIndex, offsetBy: 4)] // → "abcd"
```

But thankfully, `String` providing access to characters via a collection also means you have several helpful techniques at your disposal. Many of the methods that operate on `Array` also work on `String.characters`. Using the [`prefix`](https://developer.apple.com/reference/swift/sequence/1641743-prefix) method, the same thing looks much clearer (note that this returns a `CharacterView`; if you need a `String`, you’ll need to wrap it in a `String.init`):

```
s.characters.prefix(4)
```

Iterating over characters in a string is easy without integer indices; just use a `for` loop. If you want to number each character in turn, use [`enumerated()`](https://developer.apple.com/reference/swift/sequence/1641222-enumerated):

```
for (i, c) in "hello".characters.enumerated() {
    print("\(i): \(c)")
}
/* Prints:
0: h
1: e
2: l
3: l
4: o
*/
```

Or say you want to find a specific character. In that case, you can use `index(of:)`:

```
var hello = "Hello!"
if let idx = hello.characters.index(of: "!") {
    hello.insert(contentsOf: ", world".characters, at: idx)
}
// → "Hello, world!"
```

Note here that while the index was found using [`characters.index(of:)`](https://developer.apple.com/reference/swift/collection/1641318-index), the [`insert(contentsOf:)`](https://developer.apple.com/reference/swift/string/1641538-insert) method is called directly on the string, because `String.Index` is just an alias for `Character.Index`. The `insert(contentsOf:)` method inserts another collection of the same element type (e.g. `Character` for strings) after a given index. Note that this doesn’t have to be another `String`; you could insert an array of characters into a string just as easily.

Just like `Array`, `String` supports all the methods of [`RangeReplaceableCollection`](https://developer.apple.com/reference/swift/rangereplaceablecollection) — but again, it doesn’t conform to it. You could add the conformance manually, but we once more advise against it because it falsely implies that all collection operations are Unicode-safe in every situation:

```
extension String: RangeReplaceableCollection { }

if let comma = greeting.index(of: ",") {
    print(greeting[greeting.startIndex..<comma])
    greeting.replaceSubrange(greeting.startIndex..<greeting.endIndex,
        with: "How about some original example strings?")
}
```

One collection-like feature strings do _not_ provide is that of [`MutableCollection`](https://developer.apple.com/reference/swift/mutablecollection). This protocol adds one feature to a collection — that of the single-element subscript `set`, in addition to `get`. This is not to say strings aren’t mutable — they have several mutating methods. But what you can’t do is replace a single character using the subscript operator. The reason comes back to variable-length characters. Most people probably can intuit that a single-element subscript update would happen in constant time, as it does for `Array`. But since a character in a string may be of variable width, updating a single character could take linear time in proportion to the length of the string, because changing the width of a single element might require shuffling all the later elements up or down in memory. For this reason, you have to use [`replaceSubrange`](https://developer.apple.com/reference/swift/string.characterview/1641691-replacesubrange), even if that range is only a single element.

## Strings and Slicing

A good sign that a collection function will work well with strings is if the result is a `SubSequence` of the input. Performing slicing operations on arrays is a bit awkward, as the value you get back is not an [`Array`](https://developer.apple.com/reference/swift/array), but rather an [`ArraySlice`](https://developer.apple.com/reference/swift/arrayslice). This makes writing recursive functions that slice up their input especially painful.

`String`’s collection views have no such trouble. They define their `SubSequence` to be an instance of `Self`, so the generic functions that take a sliceable type and return a subsequence work very well with strings. For example, `world` here will be of type `String.CharacterView`:

```
let world = "Hello, world!".characters.suffix(6).dropLast()
String(world) // → "world"
```

[`split`](https://developer.apple.com/reference/swift/collection/2297966-split), which returns an array of subsequences, is also useful for string processing. It’s defined like so:

```
extension Collection {
    func split(maxSplits: Int = default,
        omittingEmptySubsequences: Bool = default,
        whereSeparator isSeparator: (Self.Iterator.Element) throws -> Bool) rethrows
        -> [AnySequence<Self.Iterator.Element>]
}
```

You can use its simplest form like this:

```
let commaSeparatedArray = "a,b,c".characters.split { $0 == "," }
commaSeparatedArray.map(String.init) // → ["a", "b", "c"]
```

This can serve a similar function to the [`components(separatedBy:)`](https://developer.apple.com/reference/foundation/nsstring/1413214-components) method `String` inherits from `NSString`, but with added configurations for whether or not to drop empty components. But since it takes a closure, it can do more than just compare characters. Here is an example of a primitive word wrap, where the closure captures a count of the length of the line thus far:

```
extension String {
    func wrapped(after: Int = 70) -> String {
        var i = 0
        let lines = self.characters.split(omittingEmptySubsequences: false) { character in
            switch character {
            case "\n", 
                 " " where i >= after:
                i = 0
                return true
            default:
                i += 1
                return false
            }
        }.map(String.init)
        return lines.joined(separator: "\n")
    }
}

let paragraph = "The quick brown fox jumped over the lazy dog."
paragraph.wrapped(after: 15)
// → "The quick brown\nfox jumped over\nthe lazy dog."
```

The [`map`](https://developer.apple.com/reference/swift/sequence/1641748-map) on the end of the `split` is necessary because we want an array of `String`, not an array of `String.CharacterView`.

That said, chances are that you’ll want to split things by character most of the time, so you might find it convenient to use the variant of [`split`](https://developer.apple.com/reference/swift/sequence/1641352-split) that takes a single separator:

```
extension Collection where Iterator.Element: Equatable {
    public func split(separator: Self.Iterator.Element,
        maxSplits: Int = default,
        omittingEmptySubsequences: Bool = default)
        -> [Self.SubSequence]
}

"1,2,3".characters.split(separator: ",").map(String.init)
// → ["1", "2", "3"]
```

Or, consider writing a version that takes a sequence of multiple separators:

```
extension Collection where Iterator.Element: Equatable {
    func split<S: Sequence>(separators: S) -> [SubSequence]
        where Iterator.Element == S.Iterator.Element
    {
        return split { separators.contains($0) }
    }
}
```

This way, you can write the following:

```
"Hello, world!".characters.split(separators: ",! ".characters).map(String.init)
// → ["Hello", "world"]
```

# Code Unit Views

Sometimes it’s necessary to drop down to a lower level of abstraction and operate directly on Unicode code units instead of characters. There are a few common reasons for this.

Firstly, maybe you actually need the code units, perhaps for rendering into a UTF-8-encoded webpage, or for interoperating with a non-Swift API that takes them.

For an example of an API that requires code units, let’s look at using [`CharacterSet`](https://developer.apple.com/reference/foundation/nscharacterset) from the Foundation framework in combination with Swift strings. The `CharacterSet` API is mostly defined in terms of Unicode scalars. So if you wanted to use `CharacterSet` to split up a string, you could do it via the `unicodeScalars` view:

```
extension String {
    func words(with charset: CharacterSet = .alphanumerics) -> [String] {
        return self.unicodeScalars.split {
            !charset.contains($0)
        }.map(String.init)
    }
}

let s = "Wow! This contains _all_ kinds of things like 123 and \"quotes\"?"
s.words()
// → ["Wow", "This", "contains", "all", "kinds", "of", "things", "like", "123", "and", "quotes"]
```

This will break the string apart at every non-alphanumeric character, giving you an array of `String.UnicodeScalarView` slices. Those can be turned back into strings via `map` with the `String` initializer that takes a `UnicodeScalarView`.

The good news is, even after going through this fairly extensive pipeline, the string slices in `words` will _still_ just be views onto the original string; this property isn’t lost by going via the `UnicodeScalarView` and back again.

A second reason for using these views is that operating on code units rather than fully composed characters can be much faster. This is because to compose grapheme clusters, you must look ahead of every character to see if it’s followed by combining characters. To see just how much faster these views can be, take a look at the performance section later on _[that section is in the book, but not part of this article]_.

Finally, the UTF-16 view has one benefit the other views do not have: it can be random access. This is possible for just this view type because, as we’ve seen, this is how strings are held internally within the `String` type. What this means is the _n_^th UTF-16 code unit is always at the _n_^th position in the buffer (even if the string is in “ASCII buffer mode” – it’s just a question of the width of the entries to advance over).

The Swift team made the decision _not_ to conform `String.UTF16View` to `RandomAccessCollection` in the standard library, though. Instead, they moved the conformance into Foundation, so you need to `import Foundation` to take advantage of it. A comment [in the Foundation source code](https://github.com/apple/swift/blob/master/stdlib/public/SDK/Foundation/ExtraStringAPIs.swift) explains why:

```
// Random access for String.UTF16View, only when Foundation is
// imported.  Making this API dependent on Foundation decouples the
// Swift core from a UTF16 representation.
...
extension String.UTF16View : RandomAccessCollection {}
```

So nothing would break if a future `String` implementation used a different internal representation. Existing code that relied on the random access conformance could take advantage of the option for a `String` to be backed by an `NSString` we discussed above. `NSString` also uses UTF-16 internally.

That said, it’s probably rarer than you think to need random access. Most practical string use cases just need serial access. But some processing algorithms rely on random access for efficiency. For example, the [Boyer-Moore search algorithm](https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_string_search_algorithm) relies on the ability to skip along the text in jumps of multiple characters.

So you could use the UTF-16 view with algorithms that require such a characteristic. Another example is the search algorithm that we define in the Generics chapter:

```
extension Collection
    where Iterator.Element: Equatable,
    SubSequence.Iterator.Element == Iterator.Element,
    Indices.Iterator.Element == Index
{
    func search<S: Sequence>(_ pattern: S) -> Index?
        where S.Iterator.Element == Iterator.Element
    {
        return indices.first { idx in
            self[idx..<endIndex].starts(with: pattern)
        }
    }
}

let helloWorld = "Hello, world!"
if let idx = helloWorld.utf16.search("world".utf16)?
    .samePosition(in: helloWorld)
{
    print(helloWorld[idx..<helloWorld.endIndex])
}
// Prints "world!"
```

But beware! These convenience or efficiency benefits come at a price, which is that your code may no longer be completely Unicode-correct. So unfortunately, the following search will fail:

```
let text = "Look up your Pok\u{0065}\u{0301}mon in a Pokédex."
text.utf16.search("Pokémon".utf16) // → nil
```

Unicode defines diacritics that are used to combine with alphabetic characters as being alphanumeric, so this fares a little better:

```
let nonAlphas = CharacterSet.alphanumerics.inverted
text.unicodeScalars.split(whereSeparator: nonAlphas.contains)
// → ["Look", "up", "your", "Pokémon", "in", "a", "Pokédex"]
```

# Outlook

When Chris Lattner outlined [the goals for Swift 4](https://forums.swift.org/t/looking-back-on-swift-3-and-ahead-to-swift-4/3610) in July 2016, improvements to string handling were among the handful of primary objectives:

> `String` is one of the most important fundamental types in the language. The standard library leads have numerous ideas of how to improve the programming model for it, without jeopardizing the goals of providing a unicode-correct-by-default model. Our goal is to be better at string processing than Perl!

The Swift team has also expressed their desire to provide native language support for regular expressions on numerous occasions, though it remains to be seen if there is time for such an additive feature in the Swift 4 timeframe. Whatever the case may be, expect string handling to change in the future.
