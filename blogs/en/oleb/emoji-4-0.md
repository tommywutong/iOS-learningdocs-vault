---
title: Emoji 4.0
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2016/12/emoji-4-0/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:2fb0f42e9120d88f'
translated: false
---

> 原文：[Emoji 4.0](https://oleb.net/blog/2016/12/emoji-4-0/)　·　Ole Begemann

# Emoji 4.0

_You need to read this on a system with Unicode 9.0 support, such as Safari on iOS 10.2 or macOS 10.12.2, for all of the emoji to display as intended. Hint: you can tap on every emoji in this article to get more info and see its composition._

You’ve probably seen that the just-released iOS 10.2 and macOS 10.12.2 [include dozens of new emoji](http://emojipedia.org/apple/ios-10.2/new/). There’s more to this than just a bunch of new symbols, however.

While many of the new emoji, such as fox face [🦊](http://emojipedia.org/fox-face/) and avocado [🥑](http://emojipedia.org/avocado/), are indeed just plain old emoji consisting of a single [code point](http://unicode.org/glossary/#code_point), others are so-called _emoji ZWJ sequences_, formed by multiple code points. These primarily encompass new gendered emoji for professions, such as firefighter [👩‍🚒](http://emojipedia.org/female-firefighter/)[👨‍🚒](http://emojipedia.org/male-firefighter/), farmer [👩‍🌾](http://emojipedia.org/female-farmer/)[👨‍🌾](http://emojipedia.org/male-farmer/), and the “David Bowie memorial” singer emoji [👩‍🎤](http://emojipedia.org/female-singer/)[👨‍🎤](http://emojipedia.org/male-singer/).

# Emoji sequences

Multi-code-point [emoji sequences](http://www.unicode.org/emoji/charts/emoji-sequences.html) aren’t new. Let’s take a look at the various forms emoji sequences can take.

## Flags

[Flags](http://emojipedia.org/flags/) consist of two [regional indicator letters](https://en.wikipedia.org/wiki/Regional_Indicator_Symbol) put together to form a country code, which the operating system displays as a flag if it finds the appropriate glyph in its emoji font. The EU flag [🇪🇺](http://emojipedia.org/flag-for-european-union/) is composed of _regional indicator symbol letter E_ [🇪](http://emojipedia.org/regional-indicator-symbol-letter-e/) and _regional indicator symbol letter U_ [🇺](http://emojipedia.org/regional-indicator-symbol-letter-u/).

## Combining marks and presentation selectors

Another example is keycaps. The symbol [1️⃣](http://emojipedia.org/keycap-digit-one/) is actually a sequence of three code points: the digit one, a so-called _emoji presentation selector_ ([U+FE0F](https://codepoints.net/U+FE0F)), and a combining enclosing keycap ([U+20E3](https://codepoints.net/U+20E3)). The keycap character is a [_combining mark_](https://en.wikipedia.org/wiki/Combining_character) — it modifies the preceding character. This tells the system to render the digit on top of the keycap. The purpose of the presentation selector is to request a graphical (i.e. emoji-style) rendering of the preceding character. If we left it out (or explicitly requested a text presentation with [U+FE0E](https://codepoints.net/U+FE0E)), the keycap would look like this: 1⃣.

[Some, mostly older, emoji](http://www.unicode.org/emoji/charts/emoji-variants.html) have both text and emoji presentation variants, and the Unicode standard [prescribes the default presentation](http://www.unicode.org/reports/tr51/index.html#Presentation_Style) (when no presentation selector is present) for each symbol.

## Skin tones

Skin tones, standardized with [Unicode 8.0](http://www.unicode.org/versions/Unicode8.0.0/) in June 2015 and first introduced by Apple [a few months earlier](http://blog.emojipedia.org/apple-2015-emoji-changelog-ios-os-x/), work the same way: a base character such as [👧](http://emojipedia.org/girl/) is combined with one of five [skin tone modifiers](http://emojipedia.org/modifiers/) (e.g. [🏽](http://emojipedia.org/emoji-modifier-fitzpatrick-type-4/)) to yield the final emoji [👧🏽](http://emojipedia.org/girl-type-4/).

# Zero-width joiner sequences

## Multi-person groupings

ZWJ sequences are another class of emoji sequences. ZWJ stands for _zero-width joiner_, which is the name of the code point [U+200D](https://codepoints.net/U+200D) that’s used to form these sequences. We first saw them in use for family and couples emoji such as [👨‍👩‍👧‍👦](http://emojipedia.org/family-man-woman-girl-boy/) and [👩‍❤️‍👩](http://emojipedia.org/couple-with-heart-woman-woman/), which were also introduced in Unicode 8 under the formal name [multi-person groupings](http://unicode.org/reports/tr51/#Multi_Person_Groupings). These presented a challenge due to the countless possible combinations of genders and the number of people in a group. Combine this with a distinct skin tone for each person and it becomes infeasible to provide separate code points for every variant.

Unicode solves this by specifying that a multi-person group consists of multiple emoji that are combined with the zero-width joiner. So the family [👨‍👩‍👧‍👦](http://emojipedia.org/family-man-woman-girl-boy/) shown above is really _man_ [👨](http://emojipedia.org/man/) + ZWJ + _woman_ [👩](http://emojipedia.org/woman/) + ZWJ + _girl_ [👧](http://emojipedia.org/girl/) + ZWJ + _boy_ [👦](http://emojipedia.org/boy/). The ZWJ serves as an indicator to the operating system that it should use a single glyph if available.

You can verify in Swift that this is really what’s going on:

```
let family1 = "👨‍👩‍👧‍👦"
let family2 = "👨\u{200D}👩\u{200D}👧\u{200D}👦"
family1 == family2 // → true
```

And to check out the code points (or Unicode scalars in Swift parlance) the emoji is composed of:

```
family1.unicodeScalars.map {
    // Format scalar as string of the form U+xxxx
    "U+\(String($0.value, radix: 16, uppercase: true))"
}
// → ["U+1F468", "U+200D", "U+1F469", "U+200D", "U+1F467", "U+200D", "U+1F466"]
```

Alternatively, you can use a [string transform](https://developer.apple.com/reference/swift/string/1643133-applyingtransform) to get the official Unicode names of the code points the string contains:

```
family1.applyingTransform(.toUnicodeName, reverse: false)!
    // This step shouldn't be necessary, but in macOS 10.12.2
    // applyingTransform(.toUnicodeName) adds an extraneous "\\N"
    // per code point to its output. We remove those first.
    .replacingOccurrences(of: "\\N", with: "")
    // Convert the resulting string into an array
    .components(separatedBy: CharacterSet(charactersIn: "{}"))
    .filter { $0 != "" }
// → ["MAN", "ZERO WIDTH JOINER", "WOMAN", "ZERO WIDTH JOINER", "GIRL", "ZERO WIDTH JOINER", "BOY"]
```

(To learn more about the incredibly useful and flexible text transforms built into Foundation, check out [my article from January 2016](https://oleb.net/blog/2016/01/icu-text-transforms/).)

Your operating system’s emoji font includes glyphs for the most common variants, but it can’t (yet?) handle every possible combination. If no glyph for the requested combination is available, the system falls back to displaying separate emoji for the group. For example, macOS 10.12.2 has no glyphs for families with skin tones — such a group is displayed as four separate faces on my system, rather than a single glyph:[1](#fn:1)

```
let family3 = "👱🏾\u{200D}👩🏽\u{200D}👧🏿\u{200D}👦🏻"
// Is displayed as "👱🏾‍👩🏽‍👧🏿‍👦🏻"
```

By the way, although this can be seen as a single logical character, it takes up 41(!) bytes if encoded with UTF-8. We’ve come a long way since ASCII:

```
family3.utf8.count // → 41
```

The discrepancy between available glyphs and logical grouping can sometimes yield strange results. If we only give the man a skin tone and leave the other family members in their natural yellow, macOS renders one glyph for the man and one glyph for the remaining family because it has a glyph for a family of one woman, a girl, and a boy: 👱🏾‍👩‍👧‍👦. The same happens when we add a third child to the family:

```
let family4 = family2 + "\u{200D}👧"
// Is displayed as "👨‍👩‍👧‍👦‍👧"
```

Note that this is only a rendering issue. The wrongly displayed multi-person groups are just as valid ZWJ sequences, regardless of how they are rendered.

In practice people will probably rarely encounter these unintuitve renderings because operating systems don’t offer a convenient way to type them and the percentage of people who know how to compose them manually is negligible. However, as new emoji glyphs and features are introduced with each new OS version, users on older systems might see rendering issues more regularly when they communicate with friends who have already updated to the newest OS.

## Professions

Finally, let’s take a look at the new profession emoji in Unicode 9.0. These are also ZWJ sequences. For example, the _female firefighter_ [👩‍🚒](http://emojipedia.org/female-firefighter/) is composed of _woman_ [👩](http://emojipedia.org/woman/) + ZWJ + _fire engine_ [🚒](http://emojipedia.org/fire-engine/), and the _male health worker_ [👨‍⚕️](http://emojipedia.org/male-health-worker/) is a sequence of _man_ [👨](http://emojipedia.org/man/) + ZWJ + _staff of aesculapius_ [⚕](http://emojipedia.org/staff-of-aesculapius/).

[Here’s a full list of the ZWJ sequences](http://www.unicode.org/emoji/charts/emoji-zwj-sequences.html) defined in the Unicode standard, including the new professions. All of these should support skin tone modifiers. The profession emoji seem to consist of two groups:

1. Combinations of a person with a “thing”. These always start with _woman_ [👩](http://emojipedia.org/woman/) or _man_ [👨](http://emojipedia.org/man/) and are followed by the symbol that describes the profession, as we saw in the examples above.
2. Combinations of an existing emoji depicting a person and the _female sign_ [♀](http://emojipedia.org/female-sign/) or _male sign_ [♂](http://emojipedia.org/male-sign/). This is used for professions for which an emoji already existed but without gendered variants. The male/female sign is also followed by an [emoji presentation selector](https://codepoints.net/U+FE0F), so the entire sequence consists of four code points (including the ZWJ), plus an optional fifth for the skin tone.

  For example, _female police officer, skin type 4_ [👮🏽‍♀️](http://emojipedia.org/female-police-officer-type-4/) is composed of _police officer_ [👮](http://emojipedia.org/police-officer/) + _skin tone modifier type 4_ [🏽](http://emojipedia.org/emoji-modifier-fitzpatrick-type-4/) + ZWJ + _female sign_ [♀](http://emojipedia.org/female-sign/) + emoji presentation selector [U+FE0F](https://codepoints.net/U+FE0F). Proof:

  ```
  "👮🏽‍♀️".unicodeScalars.map {
      "U+\(String($0.value, radix: 16, uppercase: true))"
  }
  // → ["U+1F46E", "U+1F3FD", "U+200D", "U+2640", "U+FE0F"]
  ```

  Besides professions, this technique is also used to create gendered variants of other emoji that have a non-gendered variant. Example: the _face palm_ emoji [🤦‍♂️](http://emojipedia.org/man-facepalming/)[🤦‍♀️](http://emojipedia.org/woman-facepalming/).

  The latest version of the [Unicode emoji standard](http://www.unicode.org/reports/tr51/tr51-9.html) specifies that emoji should be rendered in a gender-neutral form unless requested otherwise:

  > All other emoji representing people should be depicted in a gender-neutral way, unless gender appearance is explicitly specified using some other mechanism such as an emoji ZWJ sequence with a FEMALE SIGN or MALE SIGN.

  As of iOS 10.2, Apple’s emoji font doesn’t yet follow this rule in all cases. For instance, the ungendered versions of the _police officer_ [👮](http://emojipedia.org/police-officer/) and _face palm_ emoji [🤦](http://emojipedia.org/face-palm/) both depict a man, whereas _information desk person_ [💁](http://emojipedia.org/information-desk-person/) is displayed as a woman.

# New emoji and Swift

**Update September 20, 2017:** Swift 4.0 fixes all the issues I discuss below.

Why do I talk about emoji in this much detail? Because the new emoji features in Unicode have implications for string handling in Swift.

[Swift goes to great lengths](https://oleb.net/blog/2016/08/swift-3-strings/) to handle Unicode correctly. It should treat all emoji sequences I discussed above as a single logical [`Character`](https://developer.apple.com/reference/swift/character). In other words, the following expressions should all return `1` (the actual results are from Swift 3.0.2/Xcode 8.2):

```
"🇪🇺".characters.count // → 1 ✅
"1️⃣".characters.count // → 1 ✅
"👧🏽".characters.count // → 2 ❌ (person + skin tone)
"👨‍👩‍👧‍👦".characters.count // → 4 ❌ (four members)
"👱🏾\u{200D}👩🏽\u{200D}👧🏿\u{200D}👦🏻".characters.count
// → 8 ❌ (four members + four skin tones, ZWJ isn’t counted)
"👩🏻‍🚒".characters.count
// → 3 ❌ (person + skin tone + profession, ZWJ isn’t counted)
```

We can see that as of Swift 3.0.2, Swift doesn’t handle skin tone modifiers and ZWJ sequences correctly.

## Grapheme cluster boundaries

The problem is that string handling in Swift 3 is still based on Unicode 8.0. But, you might ask, weren’t skin tones and ZWJ sequences introduced in Unicode 8? Shouldn’t this work then? Yes, they were. Unfortunately, what constitutes an emoji and how text should be segmented into grapheme clusters (i.e. logical characters) are two separate parts of the Unicode spec, and in Unicode 8 these two diverged significantly.

While [UTR #51 (the “emoji standard”)](http://www.unicode.org/reports/tr51/tr51-3-archive.html) already codified skin tones and ZWJ sequences, the [text segmentation rules in UAX #29](http://www.unicode.org/reports/tr29/tr29-27.html#Grapheme_Cluster_Boundaries) weren’t updated to reflect that.[2](#fn:2) Thus, an implementation that aimed to follow the standard to the letter had no choice but to do what Swift did and live with the inconsistencies. I don’t know if this was intentional or an oversight by the Unicode consortium.

Unicode 9.0 fixed the text segmentation rules to take the new emoji sequences into account. Specifically, [there’s a new rule](http://www.unicode.org/reports/tr29/tr29-29.html#GB10) for determining the boundaries of an extended grapheme cluster that says:

> Do not break within emoji modifier sequences or emoji zwj sequences.

## Flags

As a side note, the segmentation rule for emoji flags was also changed slightly in Unicode 9. [The old rule](http://www.unicode.org/reports/tr29/tr29-27.html#GB8a) was simply:

> Do not break between regional indicator symbols.

[Whereas it now says](http://www.unicode.org/reports/tr29/tr29-29.html#GB12):

> Do not break within emoji flag sequences. That is, do not break between regional indicator (RI) symbols if there is an odd number of RI characters before the break point.

I’m not sure if I’m interpreting this correctly, but if I am, this means that once Swift updates to Unicode 9 it will count invalid flag sequences that consist of an odd number of regional indicator symbols as two instead of one character. The current behavior in Swift 3 is this:

```
let invalidFlag = "🇮🇸🇪" // Three RI symbols
invalidFlag.characters.count // → 1
```

The new rules says nothing about sequences of mutiple flags, however. Currently, Swift counts multiple flags following each other as a single `Character`, and it seems this will still be “correct” in Unicode 9:

```
let multipleFlags = "🇨🇦🇷🇼🇮🇩"
multipleFlags.characters.count // → 1 "correct"(!)
```

The standard recommends [to separate multiple flags](http://www.unicode.org/reports/tr29/tr29-29.html#Grapheme_Cluster_Boundaries) “by other characters, such as [U+200B](https://codepoints.net/U+200B) ZERO WIDTH SPACE”. If you do that, note that Swift does count the zero-width space as a separate character:

```
let separatedFlags = "🇨🇦\u{200B}🇷🇼\u{200B}🇮🇩"
separatedFlags.characters.count // → 5 (not 3)
```

Flags illustrate another area where the emoji standard and the text segmentation rules necessary differ. From the emoji standard’s perspective, only the 258 valid two-letter codes ([as defined by the standard](http://www.unicode.org/emoji/charts/emoji-sequences.html)) constitute a valid emoji — the majority of the 676 (26×26) possible combinations, such as 🇽🇾, is not a valid flag emoji. The text segmentation algorithm handles all regional indicator sequences equally, however.

## Workarounds

I don’t know of an easy stopgap measure way to work around this issue until Swift is updated to Unicode 9.0 — short of implementing your own text segmentation algorithm, which is definitely not easy. I guess the alternative is to try to compile and link your own version of [ICU](http://site.icu-project.org) into your app and [use that directly](http://userguide.icu-project.org/boundaryanalysis).

[In this November 2015 article](http://crunchybagel.com/using-emoji-skin-tone-modifiers-in-swift/), Quentin Zervaas recommends using the [`enumerateSubstrings(in:options:body:)`](https://developer.apple.com/reference/swift/string/1643111-enumeratesubstrings) method `String` inherits from `NSString`. That works for skin tones, but it doesn’t handle ZJW sequences correctly, either.

Ask yourself whether you really need the fully correct behavior in your code or if you can live with the current situation. In most cases, the answer is probably the latter. For example, [Twitter’s character counting algorithm](https://dev.twitter.com/basics/counting-characters) is based on ([NFC-normalized](http://unicode.org/reports/tr15/#Norm_Forms)) code points, not extended grapheme clusters, and thus totally unaffected by the new emoji.

Swift will eventually get Unicode 9 support, but the implementation has proved to be [more complicated than expected](https://github.com/apple/swift/pull/3125).

# Outlook

**Update September 20, 2017:** Swift 4.0 switched from using its own internal text segmentation algorithm to relying on the operating system’s [ICU](http://site.icu-project.org) library for this task. So your Swift programs will always yield consistent results with the OS they run on.

Even when Unicode 9 support lands in Swift, you should be aware that there will always be new Unicode features on the horizon and chances are operating systems will support them (and users will use them) before Swift gets updated. So although Swift puts much more effort into a fully Unicode-friendly string implementation than other languages, your code can’t rely on it always being 100% correct if by “correct” you mean “follows current grapheme cluster boundary rules”.

## Regional flags

[Unicode 10 will probably introduce support for regional flags](http://blog.emojipedia.org/regional-flag-support-for-unicode-in-2017/) (e.g. for US states or countries within the UK). These will be implemented using newly introduced [_emoji tag sequences_](http://www.unicode.org/reports/tr51/proposed.html#def_emoji_tag_sequence) that are completely different than the current flag sequences: a regional flag would consist of a _waving white flag_ emoji [🏳](http://emojipedia.org/waving-white-flag/) followed by a sequence of [tag characters in the range U+E00xx](https://codepoints.net/tags) and terminated by [U+E007F CANCEL TAG](https://codepoints.net/U+E007F). For instance, the flag for California would be:

```
// White flag + tags for "usca" + cancel tag
let california = "🏳\u{E0075}\u{E0073}\u{E0063}\u{E0061}\u{E007F}"
california.characters.count
// → 6 (as of Swift 3.0.2; maybe 1 in the future)
```

So better expect something like this to happen again in the future.

1. It’s conceivable that this will work better in the future if the text system could dynamically draw a glyph on the fly if it has no prerendered variant. But I don’t know enough about fonts to say how realistic such a feature is.

  **Update April 23, 2017:** Windows 10 is the first major operating system that supports [single-parent and interracial families](http://blog.emojipedia.org/diverse-emoji-families-come-to-windows/), as well as [interracial couples](http://blog.emojipedia.org/windows-10-creators-update-emoji-changelog/).

  [↩︎](#fnref:1)
2. The links point to the Unicode 8.0 versions of these documents. Use these links for the Unicode 9.0 versions of [UTR-51](http://www.unicode.org/reports/tr51/tr51-7.html) and [UAX-29](http://www.unicode.org/reports/tr29/tr29-29.html#Grapheme_Cluster_Boundaries). [↩︎](#fnref:2)
