---
title: macOS Character Viewer
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/character-viewer/'
original_language: en
published: 2018-12-10
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:01326e0064ab9335'
translated: false
---

> 原文：[macOS Character Viewer](https://nshipster.com/character-viewer/)　·　NSHipster (Mattt)

# [macOS Character Viewer](https://nshipster.com/character-viewer/)

Written by  [Mattt](https://nshipster.com/authors/mattt/)  December 10^th, 2018

Emoji is a conspiracy by the Unicode® Consortium to make Americans care about internationalization.

For a time, many developers operated under the assumption that user-input would be _primarily_ Latin-1-compatible. Or at least they could feel reasonably assured that everything would fall within the Basic Multilingual Plane — fitting comfortably into a single UTF-16 code unit.

But nowadays, with Emoji emerging as the _lingua franca_ of these troubled times, text is presumed international until proven otherwise. Everyone should be ready for when the U+1F4A9 hits the fan.

So whatever you think about those colorful harbingers of societal collapse, at _least_ they managed to break us of our ASCII-only information diets.

This week on NSHipster, we’ll be looking at a relatively obscure part of macOS that will prove essential for developers in today’s linguistic landscape: Character Viewer

---

From any macOS app, you can select the Edit menu and find an item at the very bottom called “Emoji & Symbols” (tellingly renamed from “Special Characters” in OS X Mavericks).

By default, this opens a panel that looks something like this:

![](https://nshipster.com/assets/character-viewer-collapsed-3c0822f5a5f449e964ed400c6cec759c27bc9cb0d7756df5668d78b34740ae76c3786930db82f7d640d2c79776f622eddd6abf9879df624bba0ff9f242949955.png)

You may have discovered this on your own and found it to be a convenient alternative to searching for Emoji online.

_But this isn’t even its final form!_ Click the icon on the top right to see its _true_ power:

![](https://nshipster.com/assets/character-viewer-expanded-8953f4788781cae959ca58e0feaeca3a14b84b00cacc3dea243d58856d2db534827435ed50468b46e18ab15fb7385a564972f4d34c352e2ae45ca6ed0e662571.png)

Go ahead and memorize the global shortcut if you haven’t already: ⌃⌘Space. If you do any serious work with text, you’ll be using Character Viewer frequently.

Let’s take a quick tour of Character Viewer and see what it can do for us:

## A Quick Tour of Character Viewer

The sidebar on the left provides quick access to your favorite and frequently-used characters, as well as a customizable list of named categories like Emoji, Latin, Punctuation, and Bullets/Stars.

The center column displays a grid of characters. Some categories, including Emoji, provide special views that make it easier to browse through the characters in that collection.

Selecting a character populates the inspector pane on the right with a larger, isolated rendering of the character, the character name, code point, and UTF-8 encoding. The inspector may also show alternate glyph renderings provided by other fonts as well as related characters, as applicable.

### Copying Character Information

You can control-click a character and choose “Copy Character Info” from the shortcut menu to copy the information found in the inspector. For example:

😂  
 face with tears of joy  
 Unicode: U+1F602, UTF-8: F0 9F 98 82

Let’s take a look at what all of this means and how to use it in Swift code:

#### Character Literal

The first line of the copied character information is the character itself.

Swift source code fully supports Unicode, so you can copy-paste any character into a string literal and have it work as expected:

```
"😂" // 😂
```

All characters found in Character Viewer are valid string and character literals. However, not all entries are valid Unicode scalar literals. For example, the character 👩🏻‍🦰 is a [named sequence](https://unicode.org/reports/tr34/) consisting of four individual code points:

- 👩‍ WOMAN (U+1F469)
- 🏻 EMOJI MODIFIER FITZPATRICK TYPE-1-2 (U+1F3FB)
- ␣ ZERO WIDTH JOINER (U+200D)
- 🦰 EMOJI COMPONENT RED HAIR (U+1F9B0)

Attempting to initialize a `Unicode.Scalar` value from a string literal with this character results in an error.

```
("👩🏻‍🦰" as Unicode.Scalar) // error
```

#### Unicode Code Point

Each Unicode character is assigned a unique name and number, known as a code point. By convention, Unicode code points are formatted as 4 – 6 hexadecimal digits (0–9, A–F) with the prefix “U+”.

In Swift, string literals have the `\u{n}` escape sequence which takes a 1 – 6 hexadecimal number corresponding to a Unicode scalar value (essentially, the numerical value of any code point that isn’t a [surrogate](https://unicode.org/faq/utf_bom.html#utf16-2)).

The character 😂 has a scalar value equal to 1F602₁₆ (128514 in decimal). You can plug that number into a `\u{}` escape sequence in a string literal to have it replaced by the character in the resulting string.

```
"\u{1F602}" // "😂"
```

Unicode scalar value escape sequences are especially useful when working with nonprinting control characters like [directional formatting characters](http://unicode.org/reports/tr9/).

#### UTF-8 Code Units

The pairs of hexadecimal digits labeled “UTF8” correspond to the code points for the [UTF-8](https://unicode.org/faq/utf_bom.html#utf8-1) encoded form of the character.

The UTF-8 code unit is a byte (8 bits), which is represented by two hexadecimal digits.

In Swift, you can use the `String(decoding:as:)` initializer to create a string from an array of `UInt8` values corresponding to the values copied from Character Viewer.

```
String(decoding: [0xF0, 0x9F, 0x98, 0x82], as: UTF8.self) // 😂
```

#### Unicode Character Name

The last piece of information provided by Character Viewer is the name of the character “face with tears of joy”.

The Swift standard library doesn’t currently provide a way to initialize Unicode scalar values or named sequences. However, you can use the `String` method [`applyingTransform(_:reverse:)`](https://developer.apple.com/documentation/foundation/nsstring/1407787-applyingtransform) provided by the Foundation framework to get a character by name:

```
import Foundation

"\\N{FACE WITH TEARS OF JOY}".applyingTransform(.toUnicodeName,
                                                reverse: true)
// "😂"
```

Perhaps more usefully, you can apply the `.toUnicodeName` transform in the non-reverse direction to get the Unicode names for each character in a string:

```
"🥳✨".applyingTransform(.toUnicodeName, reverse: false)
// \\N{FACE WITH PARTY HORN AND PARTY HAT}\\N{SPARKLES}
```

## Things to Do with Character Viewer

Now that you’re more familiar with Character Viewer, here are some ideas for what to do with it:

### Add Keyboard Shortcut Characters to Favorites

All developers should take responsibility for writing documentation about the software they work on and the processes they use in their organization.

When providing instructions for using a Mac app, it’s often helpful to include the keyboard shortcuts corresponding to menu items. The symbols for modifier keys like Shift (⇧) are difficult to type, so it’s often more convenient to pick them from Character Viewer. You can make it even easier for yourself by adding them to your Favorites list.

Click on the Action button at the top left corner of the Character Viewer panel and select the Customize List… menu item. In the displayed sheet, scroll to the bottom of the categories listed under Symbols and check the box next to Technical Symbols.

| ⌃ | Control | UP ARROWHEAD (U+2303) |
|---|---|---|
| ⌥ | Alt / Option | OPTION KEY (U+2325) |
| ⇧ | Shift | UPWARDS WHITE ARROW (U+21E7) |
| ⌘ | Command | PLACE OF INTEREST SIGN (U+2318) |

Dismiss the sheet and select Technical Symbols in the sidebar, and you’ll notice some familiar keyboard shortcut characters. Add them to your Favorites list by selecting each individually and clicking the Add to Favorites button in the inspector.

![](https://nshipster.com/assets/character-viewer-add-to-favorites-a4db0aeb0bbc0f4d16b17c66bdda2a6482f14c676aaf9154b4dba90b3553b18d9dbf8577ce9e6b4fdb917c3c005375e89792bacf343a57c63ddc438b50f16447.png)

### Demystify Unknown Characters

Ever see a character and wonder what it was? Simply copy-paste it into the search field of Character Viewer to get its name and number.

For example, have you ever wondered about the  character you get by typing ⌥⇧K? Like, how did Apple get its logo into the Unicode Standard when that goes against their [criteria for encoding symbols](http://www.unicode.org/pending/symbol-guidelines.html)?

By copy-pasting into the Character Viewer, you can learn that, in fact, the Apple logo _isn’t_ an encoded Unicode character. Rather, it’s a glyph associated with the code point U+F8FF from the [Private-Use Area block](http://www.unicode.org/faq/private_use.html).

![](https://nshipster.com/assets/character-viewer-apple-logo-34cad3f4cc14a2f8a9c9701495b45b6a9ff96b8b156da12f62f392b7172eaea6fa5f8ee7ffa37dfe0318f977589f2cd007041f209aa976aec135be633ed41089.png)

The next time you have a question about what’s in your pasteboard, consider asking Character Viewer instead of Safari.

### Divest Your Cryptocurrency

Given the current economic outlook for Bitcoin (₿) and other cryptocurrencies, you may be looking to divest your holdings in favor of something more stable and valuable. Look no further than the Currency Symbols category for some exciting investment opportunities, including [French francs (₣)](https://en.wikipedia.org/wiki/French_franc) and [Italian lira (₤)](https://en.wikipedia.org/wiki/Italian_lira).

![](https://nshipster.com/assets/character-viewer-currency-symbols-e0d6a44a275140771811626a469d6aeaa8396360c0cf088aa434b07384ce006837f376413b2270ffcc08c3657e0b05477315b4b6f05c4709d144435fdd50321d.png)

### Explore the Unicode Code Table

At the bottom of the Customize List sheet, you’ll find a section titled Code Tables.

Go ahead and check the box next to Unicode.

![](https://nshipster.com/assets/character-viewer-unicode-code-chart-c231eaca8bdd4c8dc4eeecb62f99742a03ebe120bbd66a3b4314ae7a9a4444728ed2071195c49e12d5c05c584845def03be2ac1911336c63ae93568cdf996982.png)

This is arguably the best interface available to you for browsing the Unicode Standard. No web page comes close to matching the speed and convenience of what’s available here in the macOS Character Viewer.

The top panel shows a sortable table of [Unicode blocks](https://en.wikipedia.org/wiki/Unicode_block), with their code point offset, name, and category. Clicking on any of these entries navigates to the corresponding offset in the bottom panel, where characters are displayed in a 16-column grid.

_Brilliant._

---

Character Viewer is an indispensable tool for working with text on computers — _a hidden gem in macOS if ever there was one._

But even more than that, Character Viewer offers a look into our collective linguistic and cultural heritage as encoded into the Unicode Standard. Etchings made thousands of years ago by Phoenician merchants and Qin dynasty bureaucrats and Ancient Egyptian priests and Lycian school children — they’re all preserved here digitally, just waiting to be discovered.

_Seriously, how amazing is that?_

So if ever you grow weary of the awfulness of software… take a scroll through the multitude of scripts and symbols in the Unicode code table, and take solace that we managed to get a _few_ things right along the way.
