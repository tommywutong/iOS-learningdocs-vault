---
title: ICU Text Transforms in Foundation
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2016/01/icu-text-transforms/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:5fe262264f89f826'
translated: false
---

> 原文：[ICU Text Transforms in Foundation](https://oleb.net/blog/2016/01/icu-text-transforms/)　·　Ole Begemann

# ICU Text Transforms in Foundation

[ICU string transforms](http://userguide.icu-project.org/transforms/general) are cool. The [ICU libraries](http://site.icu-project.org) provide a bunch of powerful text transformations that are very useful for processing user input, especially if your code needs to handle languages other than English and scripts other than Latin. For instance, you could transliterate a text written in Simplified Chinese to Latin characters, strip accents and other diacritical marks, delete invisible characters, and convert the input to lowercase before you feed the normalized string into your database’s search API, all in a single line of code.

On Apple platforms, string transforms have been exposed through the [`CFStringTransform`](https://developer.apple.com/reference/corefoundation/1542411-cfstringtransform) function in Core Foundation for a long time. Read Mattt Thompson’s [excellent overview on NSHipster](https://nshipster.com/cfstringtransform/) for more on this API.

With iOS 9 and OS X 10.11, string transforms have made the jump to the Foundation framework and are also exposed on Swift’s [`String`](https://developer.apple.com/reference/swift/string) type. Documentation for the new [`applyingTransform(_:reverse:)`](https://developer.apple.com/reference/swift/string/1643133-applyingtransform) method is still sparse, but the docs for `CFStringTransform` tell you what you need to know, and Nate Cook shows a few examples in [this NSHipster article](https://nshipster.com/ios9/). Here’s how you would do the conversion from Chinese to Latin:

```
import Foundation
let shanghai = "上海"
shanghai.applyingTransform(.toLatin, reverse: false)
// → "shàng hǎi"
```

So far, so good. Apple currently provides [constants for 16 possible transforms](https://developer.apple.com/reference/foundation/stringtransform). Most of these refer to script transliterations, and then there are some others that let you strip combining marks and diacritics from the input, or convert characters to their code point numbers or official Unicode names. Additionally, most transforms can be reversed via the second argument to `applyingTransform`. This is already very powerful, especially when you chain multiple transformations. For example, here we transliterate the Chinese text first, then strip combining and diacritical marks:

```
shanghai.applyingTransform(.toLatin, reverse: false)?
    .applyingTransform(.stripCombiningMarks, reverse: false)?
    .applyingTransform(.stripDiacritics, reverse: false)
// → "shang hai"
```

# Freeform Transforms

What I never realized, although it is mentioned both in the `CFStringTransform` documentation and in the NSHipster article, is that you can even go a step further. ICU defines its own syntax for specifying a transform, and if you pass a string conforming to this syntax to `applyingTransform` or `CFStringTransform`, it just works. Like this:

```
// Convert non-ASCII characters to ASCII,
// convert to lowercase, delete spaces
let toLowercaseASCIINoSpaces =
    StringTransform(rawValue: "Latin-ASCII; Lower; [:Separator:] Remove;")
"Café au lait".applyingTransform(toLowercaseASCIINoSpaces, reverse: false)
// → "cafeaulait"
```

The `CFStringTransform` API takes a normal string. With Swift 3, the loosely-typed string constants were converted to the dedicated `StringTransform` type as part of [SE-0033](https://github.com/apple/swift-evolution/blob/master/proposals/0033-import-objc-constants.md). As a consequence, you’ll have to use the `StringTransform.init(rawValue:)` initializer for your custom transform rules. If you want to use a custom transform in many places, consider defining it as an extension to `StringTransform`:

```
extension StringTransform {
    static let toLowercaseASCIINoSpaces =
        StringTransform(rawValue: "Latin-ASCII; Lower; [:Separator:] Remove;")
}

"Café au lait".applyingTransform(.toLowercaseASCIINoSpaces, reverse: false)
// → "cafeaulait"
```

The [documentation for this in the ICU User Guide](http://userguide.icu-project.org/transforms/general) is very good and includes lots of examples. I encourage you to check it out. Here are some of my own examples:

**Convert to lowercase.**

| Input | Transform | Result |
|---|---|---|
| `HELLO WORLD` | `Lower` | `hello world` |

**Convert only vowels to lowercase.** The square brackets specify a filter. The rule following the filter is only applied to characters that match the filter.

| Input | Transform | Result |
|---|---|---|
| `HELLO WORLD` | `[AEIOU] Lower` | `HeLLo WoRLD` |

**Convert to Latin, then to ASCII, then to lowercase.** Separate multiple rules with semicolons. The `Latin-ASCII` step removes diacritical marks and will also try to convert symbols and punctuation from outside the ASCII range to their nearest ASCII equivalent.

| Input | Transform | Result |
|---|---|---|
| `上海` | `Any-Latin; Latin-ASCII; Lower` | `shang hai` |
| `København` | `Any-Latin; Latin-ASCII; Lower` | `kobenhavn` |
| `กรุงเทพมหานคร` | `Any-Latin; Latin-ASCII; Lower` | `krungthephmhankhr` |
| `Αθήνα` | `Any-Latin; Latin-ASCII; Lower` | `athena` |
| `“Æ « © 1984”` | `Any-Latin; Latin-ASCII; Lower` | `"ae << (c) 1984"` |

**Delete punctuation.** The `Remove` rule can be very powerful. The filter (in brackets) can either consist of a string of characters the rule should apply to (see above), or as in this case, a named [Unicode character category](https://en.wikipedia.org/wiki/Unicode_character_property#General_Category).

| Input | Transform | Result |
|---|---|---|
| `“Make it so,” said Picard.` | `[:Punctuation:] Remove` | `Make it so said Picard` |

**Delete everything that is not a letter.** Use a caret `^` to negate a filter.

| Input | Transform | Result |
|---|---|---|
| `5 plus 6 equals 11 👍!` | `[:^Letter:] Remove` | `plusequals` |

**Convert to typographical punctuation.** The `Publishing` rule converts straight punctuation marks into their typographical equivalents.

| Input | Transform | Result |
|---|---|---|
| `"How's it going?"` | `Publishing` | `“How’s it going?”` |

**Convert to hex representation.** Several formats are supported. The default format is `Java`. Note that `Java` outputs UTF-16 code units (the emoji is encoded in two parts) while the other formats output code points.

| Input | Transform | Result |
|---|---|---|
| `😃!` | `Hex` | `\uD83D\uDE03\u0021` |
| `😃!` | `Hex/Java` | `\uD83D\uDE03\u0021` |
| `😃!` | `Hex/Unicode` | `U+1F603U+0021` |
| `😃!` | `Hex/Perl` | `\x{1F603}\x{21}` |
| `😃!` | `Hex/XML` | `&#x1F603;&#x21;` |

**Normalize to different normalization forms.**

| Input | Transform | Result |
|---|---|---|
| `é` | `NFD; Hex/Unicode` | `U+0065U+0301` |
| `é` | `NFC; Hex/Unicode` | `U+00E9` |
| `2⁸` | `NFKD` | `28` |
| `2⁸` | `NFKC` | `28` |

---

Imagine you’d have to write all this yourself.

I learned about freeform transform rules from Florian and Daniel’s [Core Data book](https://oleb.net/blog/2015/12/core-data-book/). They explain how you can use string transforms to normalize search terms the user has entered before feeding it to the database. This can vastly improve search performance and yield better search results.
