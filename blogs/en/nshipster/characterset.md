---
title: CharacterSet
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/characterset/'
original_language: en
published: 2012-09-17
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:22420d17edc601d3'
translated: false
---

> 原文：[CharacterSet](https://nshipster.com/characterset/)　·　NSHipster (Mattt)

# [Character​Set](https://nshipster.com/characterset/)

Written by  [Mattt](https://nshipster.com/authors/mattt/)  December 12^th, 2018 ([revised](https://github.com/nshipster/articles/commits/master/2012-09-17-characterset.md))

In Japan, there’s a comedy tradition known as [Manzai (漫才)](https://en.wikipedia.org/wiki/Manzai). It’s kind of a cross between stand up and vaudeville, with a straight man and a funny man delivering rapid-fire jokes that revolve around miscommunication and wordplay.

As it were, we’ve been working on a new routine as a way to introduce the subject for this week’s article, `CharacterSet`, and wanted to see what you thought:

Is `CharacterSet` a `Set<Character>`?  キャラクターセットではないキャラクターセット？    Of course not!  もちろん違います！    What about `NSCharacterSet`?  何エンエスキャラクタセットは？    That's an old reference.  それは古いリファレンスです。    Then what do you call a collection of characters?  何と呼ばれる文字の集合ですか？    That would be a `String`!  それは文字列でしょ！    (╯° 益 °)╯ 彡 ┻━┻  無駄無駄無駄無駄無駄無駄無駄

_(Yeah, we might need to workshop this one a bit more.)_

All kidding aside, `CharacterSet` is indeed ripe for miscommunication and wordplay (so to speak): it doesn’t store `Character` values, and it’s not a `Set` in the literal sense.

So what is `CharacterSet` and how can we use it? Let’s find out! (行きましょう！)

---

`CharacterSet` (and its reference type counterpart, `NSCharacterSet`) is a Foundation type used to trim, filter, and search for characters in text.

In Swift, a `Character` is an extended grapheme cluster (really just a `String` with a length of 1) that comprises one or more scalar values. `CharacterSet` stores those underlying `Unicode.Scalar` values, rather than `Character` values, as the name might imply.

The “set” part of `CharacterSet` refers not to `Set` from the Swift standard library, but instead to the `SetAlgebra` protocol, which bestows the type with the same interface: `contains(_:)`, `insert(_:)`, `union(_:)`, `intersection(_:)`, and so on.

## Predefined Character Sets

`CharacterSet` defines constants for sets of characters that you’re likely to work with, such as letters, numbers, punctuation, and whitespace. Most of them are self-explanatory and, with only a few exceptions, correspond to one or more [Unicode General Categories](https://unicode.org/reports/tr44/#General_Category_Values).

| Type Property | Unicode General Categories & Code Points |
|---|---|
| `alphanumerics` | L*, M*, N* |
| `letters` | L*, M* |
| `capitalizedLetters`^* | Lt |
| `lowercaseLetters` | Ll |
| `uppercaseLetters` | Lu, Lt |
| `nonBaseCharacters` | M* |
| `decimalDigits` | Nd |
| `punctuationCharacters` | P* |
| `symbols` | S* |
| `whitespaces` | Zs, U+0009 |
| `newlines` | U+000A – U+000D, U+0085, U+2028, U+2029 |
| `whitespacesAndNewlines` | Z*, U+000A – U+000D, U+0085 |
| `controlCharacters` | Cc, Cf |
| `illegalCharacters` | Cn |

The remaining predefined character set, `decomposables`, is derived from the [decomposition type and mapping](https://unicode.org/reports/tr44/#Character_Decomposition_Mappings) of characters.

### Trimming Leading and Trailing Whitespace

Perhaps the most common use for `CharacterSet` is to remove leading and trailing whitespace from text.

```
"""

    😴

""".trimmingCharacters(in: .whitespacesAndNewlines) // "😴"
```

You can use this, for example, when sanitizing user input or preprocessing text.

## Predefined URL Component Character Sets

In addition to the aforementioned constants, `CharacterSet` provides predefined values that correspond to the characters allowed in various [components of a URL](https://nshipster.com/nsurl/):

- `urlUserAllowed`
- `urlPasswordAllowed`
- `urlHostAllowed`
- `urlPathAllowed`
- `urlQueryAllowed`
- `urlFragmentAllowed`

### Escaping Special Characters in URLs

Only certain characters are allowed in certain parts of a URL without first being escaped. For example, spaces must be percent-encoded as `%20` (or `+`) when part of a query string like `https://nshipster.com/search/?q=character%20set`.

`URLComponents` takes care of percent-encoding components automatically, but you can replicate this functionality yourself using the `addingPercentEncoding(withAllowedCharacters:)` method and passing the appropriate character set:

```
let query = "character set"
query.addingPercentEncoding(withAllowedCharacters: .urlQueryAllowed)
// "character%20set"
```

## Building Your Own

In addition to these predefined character sets, you can create your own. Build them up character by character, inserting multiple characters at a time by passing a string, or by mixing and matching any of the predefined sets.

### Validating User Input

You might create a `CharacterSet` to validate some user input to, for example, allow only lowercase and uppercase letters, digits, and certain punctuation.

```
var allowed = CharacterSet()
allowed.formUnion(.lowercaseLetters)
allowed.formUnion(.uppercaseLetters)
allowed.formUnion(.decimalDigits)
allowed.insert(charactersIn: "!@#$%&")

func validate(_ input: String) -> Bool {
    return input.unicodeScalars.allSatisfy { allowed.contains($0) }
}
```

Depending on your use case, you might find it easier to think in terms of what shouldn’t be allowed, in which case you can compute the inverse character set using the `inverted` property:

```
let disallowed = allowed.inverted
func validate(_ input: String) -> Bool {
    return input.rangeOfCharacter(from: disallowed) == nil
}
```

### Caching Character Sets

If a `CharacterSet` is created as the result of an expensive operation, you may consider caching its `bitmapRepresentation` for later reuse.

For example, if you wanted to create `CharacterSet` for Emoji, you might do so by enumerating over the Unicode code space (U+0000 – U+1F0000) and inserting the scalar values for any characters with [Emoji properties](https://www.unicode.org/reports/tr51/#Emoji_Properties) using the `properties` property added in Swift 5 by [SE-0221 “Character Properties”](https://github.com/apple/swift-evolution/blob/master/proposals/0221-character-properties.md):

```
import Foundation

var emoji = CharacterSet()

for codePoint in 0x0000...0x1F0000 {
    guard let scalarValue = Unicode.Scalar(codePoint) else {
        continue
    }

    // Implemented in Swift 5 (SE-0221)
    // https://github.com/apple/swift-evolution/blob/master/proposals/0221-character-properties.md
    if scalarValue.properties.isEmoji {
        emoji.insert(scalarValue)
    }
}
```

The resulting `bitmapRepresentation` is a 16KB `Data` object.

```
emoji.bitmapRepresentation // 16385 bytes
```

You could store that in a file somewhere in your app bundle, or embed its [Base64 encoding](https://en.wikipedia.org/wiki/Base64) as a string literal directly in the source code itself.

```
extension CharacterSet {
    static var emoji: CharacterSet {
        let base64Encoded = """
        AAAAAAgE/wMAAAAAAAAAAAAAAAAA...
        """
        let data = Data(base64Encoded: base64Encoded)!

        return CharacterSet(bitmapRepresentation: data)
    }
}

CharacterSet.emoji.contains("👺") // true
```

---

Much like our attempt at a Manzai routine at the top of the article, some of the meaning behind `CharacterSet` is lost in translation.

`NSCharacterSet` was designed for `NSString` at a time when characters were equivalent to 16-bit UCS-2 code units and text rarely had occasion to leave the Basic Multilingual Plane. But with Swift’s modern, Unicode-compliant implementations of `String` and `Character`, the definition of terms has drifted slightly; along with its `NS` prefix, `CharacterSet` lost some essential understanding along the way.

Nevertheless, `CharacterSet` remains a performant, specialized container type for working with collections of scalar values.

FIN  おしまい。
