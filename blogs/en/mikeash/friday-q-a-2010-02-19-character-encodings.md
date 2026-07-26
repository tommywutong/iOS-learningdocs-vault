---
title: 'Friday Q&A 2010-02-19: Character Encodings'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2010-02-19-character-encodings.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:ab889530371b40d9'
translated: false
---

> 原文：[Friday Q&A 2010-02-19: Character Encodings](https://www.mikeash.com/pyblog/friday-qa-2010-02-19-character-encodings.html)　·　mikeash.com Friday Q&A

Posted at 2010-02-19 22:15 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2010-02-26: Futures](https://www.mikeash.com/pyblog/friday-qa-2010-02-26-futures.html)  
Previous article: [Friday Q&A 2010-02-12: Trampolining Blocks with Mutable Code](https://www.mikeash.com/pyblog/friday-qa-2010-02-12-trampolining-blocks-with-mutable-code.html)  
Tags: [encoding](https://www.mikeash.com/pyblog/?tag=encoding) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [text](https://www.mikeash.com/pyblog/?tag=text) [unicode](https://www.mikeash.com/pyblog/?tag=unicode)

Friday Q&A 2010-02-19: Character Encodings

by [Mike Ash](https://www.mikeash.com/)

**What's a Character Encoding?**  
 To define a character encoding, I first need to define a character. This is probably intuitively obvious to most of you, but there is great value in a more formal definition, especially since intuitive ideas will vary.

The trouble is that the formal definition is vague. Essentially, a **character** is the fundamental conceptual unit of textual information. Letters and numbers are characters, but that's not all characters are. Symbols are characters, but there are non-symbolic characters, such as the space character.

Now that we (sort of) know what a character is, a **character encoding** is some technique for mapping conceptual sequences of characters into actual sequences of bytes, and for mapping a sequence of bytes back to a sequence of characters.

There are many different kinds of encodings, but there are two basic kinds that are of primary interest here:

- **8-bit encodings:** These encodings maintain a one-to-one mapping between a byte and a character. Each character gets encoded to a single byte, and each byte represents one character. For obvious reasons, 8-bit encodings can't represent more than 256 characters.
- **Variable-length encodings:** These encodings can map a single character to multiple bytes, and the number of bytes varies depending on the character. This allows the encoding to represent more than 256 characters, essential if you're dealing with languages such as Chinese which have far more than this.

**ASCII**  
 The most common and fundamental character encoding used today is ASCII. ASCII is a small and simple 7-bit character encoding, which means that it defines 128 characters and maps them to the byte values 0-127. As used on modern systems, ASCII can be thought of as an 8-bit encoding where the values 128-255 go unused.

ASCII encodes all of the letters used in English, as well as common punctuation and other symbols. ASCII also encodes various control characters. Some of these, like newline and tab, are commonly used in text for formatting purposes. Some, like Record Separator and Start of Header, are basically obsolete. A full listing of all ASCII characters can be seen by typing `man ascii` into your local Terminal window.

ASCII works great for most English writing, but is inadequate for the vast majority of other languages in the world.

**ASCII compatibility**  
 The notion of ASCII compatibility is a key concept when discussing other encodings. Because of ASCII's early dominance, and the fact that it left half of the values unused on computers with 8-bit bytes, many other encodings sprouted up which maintained compatibility with ASCII, taking advantage of the unused values in order to represent more characters. Being ASCII compatible makes it much easier to use old code with a new encoding, and ensures that software will have a common denominator for communication even if they disagree on encodings.

There are two different kinds of ASCII compatibility. The first kind is full ASCII compatibility. This means that if you take a sequence of ASCII bytes and decode them using the encoding in question, the result is still the ASCII characters that they represent. It also means that if you encode a sequence of characters using this encoding, any ASCII bytes in the output represent the corresponding ASCII character. In short, ASCII gets encoded to ASCII, and anything that looks like ASCII is ASCII.

There's also partial compatibility. Some encodings will correctly read an ASCII string, but can produce bytes in the range 0-127 for non-ASCII characters which take up more than one byte. Any sort of text processing with such encodings requires a strong understanding of how the encoding works, because, for example, searching for the letter Z within the text using a raw byte-by-byte search could end up finding the byte 0x5A that just happens to be part of a multi-byte character. For this sort of encoding, it will interpret ASCII strings correctly, but may produce ASCII-looking byte sequences where no such thing is intended.

Some encodings are simply not ASCII-compatible at all. These assign different meanings to byte values 0-127 in all contexts.

**Latin-1**  
 Latin-1, is perhaps the most common 8-bit encoding, so it deserves special mention. Latin-1 is a mostly ASCII compatible encoding whose purpose is to work better with common Western European languages. As such, it uses many of the values left unused by ASCII to represent accented characters and certain letters not in ASCII, as this is the major thing lacking from ASCII for these languages. It also includes other characters useful to these languages, such as currency symbols and punctuation, and some symbols that are just useful in general, like copyright/trademark symbols.

There are actually three somewhat different encodings which can all be described as "Latin-1", which is wonderfully confusing. There's ISO 8859-1, Windows-1252, and ISO-8859-1 (the first and last names are identical except for a single hyphen). ISO 8859-1 is not ASCII compatible because it does not define characters for the ranges occupied by ASCII control characters. It does leave ASCII values intact for the rest of that range, and the other two are fully ASCII compatible. ISO-8859-1 is so frequently confused with Windows-1252 (which encodes additional human-readable characters in a space that ISO-8859-1 uses for control characters) that many documents state their encoding as ISO-8859-1 when they actually use Windows-1252. As best I can tell, in Cocoa, the `NSISOLatin1StringEncoding` constant refers to ISO-8859-1, but this is by no means clear. (The documentation doesn't say precisely what it is. When passed through `CFStringConvertNSStringEncodingToEncoding`, it comes out as `kCFStringEncodingISOLatin1`. The documentation says that encoding is ISO 8859-1. However, `CFStringConvertEncodingToIANACharSetName` returns `iso-8859-1` and that's probably the one to believe.)

**MacRoman**  
 Since this is a Mac-centric blog, MacRoman deserves special mention as well. It's roughly the Mac-specific equivalent of Latin-1. Like Latin-1, MacRoman is ASCII-compatible and fills in a lot of useful letters and symbols for Western European languages. However, the code points that it uses and the characters that it covers don't match Latin-1.

MacRoman has one nice property (which is shared by ISO-8859-1 but not the other two "Latin-1" encodings) that it defines a unique character for every possible byte value. This means that any sequence of bytes is a valid MacRoman string, and that roundtripping through MacRoman (decoding with MacRoman, then re-encoding) will always preserve the data with no changes.

**Unicode**  
 Unicode is a fantastically large and complicated system of character encodings whose full nature is too involved to explain here. However, there are a few relevant points which are valuable to know.

Unicode defines a large range of characters (in Unicode terminology, "code points") which encompass virtually every character defined in other character encodings, and thus virtually every character in use for written communication. All in all, Unicode defines about a million characters. Unicode is able to represent nearly any written text without having to worry about different encodings. This is really handy.

Once you reach the level of Unicode, an important distinction makes itself obvious. The distinction is the difference between a _character_ and a _glyph_. A _character_ is a logical semantic unit, and a _glyph_ is a visual unit that you actually see on screen. Although many English speakers (and plenty of non-English speakers) consider these ideas to be the same, they are not. It is possible to have a character which has no glyph (for example, the space character), two characters which combine to a single glyph (Unicode defines "combining marks", like accent marks, which modify a plain letter), and it's even possible for a single character to produce multiple glyphs (like an accented character transforming into a plain letter plus a separate, appropriately positioned accent mark glyph).

All of this means that you can't just slice up Unicode text in arbitrary places without really understanding how Unicode works, or at least knowing that your text only contains characters that behave nicely. The `NSString` method `-rangeOfComposedCharacterSequenceAtIndex:` can help a lot with this.

Unicode defines characters, but does not define a single character _encoding_ to map those characters to sequences of bytes. Instead, it defines several different encodings, which all have different tradeoffs and different uses.

The original Unicode was a 16-bit encoding where every character occupied exactly two bytes. This encoding is now referred to as UCS-2. UCS-2 was later expanded to be able to work with more than 65,535 characters, and this new encoding became UTF-16. UTF-16 uses two-byte code units, but uses two such code units (four bytes in total) to represent characters which don't fit into the original two bytes. (UTF-16 code units are what `NSString` puts into the `unichar` type, for things like `-characterAtIndex:`.)

Another encoding is called UTF-32, which as the name suggests uses four bytes per character. Every Unicode character fits into four bytes, so this is a fixed-length encoding, but tends to waste a lot of space so it doesn't get much use.

**UTF-8**  
 The trouble with these Unicode encodings is that they are completely incompatible with all software which works with individual bytes and assumes that ASCII is king. This, plus the fact that UCS-2 and UTF-16 double the size of plain ASCII text, with little perceived benefit for English speakers, hurt Unicode's adoption.

UTF-8 was created to solve these problems. As the name suggests, the basic code unit in UTF-8 is a single byte. These bytes are chained together in sequences up to four bytes long to encode each Unicode character.

The most important property of UTF-8 is that it's _fully ASCII compatible_. Put ASCII in, get ASCII out, every time. All non-ASCII characters are encoded using a sequence of bytes in the range 128-255. This means that software which expects ASCII but can leave the top half of the byte value range alone will generally work pretty well with UTF-8.

For non-ASCII characters, UTF-8 uses a clever variable-length encoding scheme that's very easy to work with. Any byte in a UTF-8-encoded byte stream wil fall into one of five categories:

| **bit pattern** (`x` is wildcard) | **meaning** |
|---|---|
| `0xxxxxxx` | single ASCII character |
| `110xxxxx` | lead byte of two-character sequence |
| `1110xxxx` | lead byte of three-character sequence |
| `11110xxx` | lead byte of four-character sequence |
| `10xxxxxx` | trailing byte in multi-character sequence |

As you can see, the byte stream is self-describing. For any given character, you can see which category it falls into. If it's a trailing byte, then you can read forward (or backwards) in the stream until you come to the next lead byte. From there, you can easily tell how many trailing bytes that will have, which characters are ASCII, etc. While Unicode is complicated and UTF-8 can't hide that fact, UTF-8 does make it relatively easy to pass arbitrary text around while still being able to parse the ASCII bits. And if you need to deal with the Unicode bits as well, it's easy to convert UTF-8 into something more useful, like an `NSString`, which knows more about Unicode.

Because of all of the useful properties that UTF-8 has, I want to leave you with this piece of advice: **when storing or transmitting text, always use UTF-8 for your character encoding**.

This obviously doesn't apply if you're writing for a protocol or format which already exists and which mandates a different encoding, but any time you have a choice, your choice should be UTF-8.

**Fallbacks**  
 Sometimes you receive textual data and you don't know in advance what the encoding is. This is ultimately a problem that's impossible to solve with complete accuracy. However, it's possible to make some useful guesses which will be right much of the time, in most contexts.

When this happens to me, I like to use code like this:

```
    NSString *string = [[NSString alloc] initWithData: data encoding: NSUTF8StringEncoding];
    if(!string)
        string = [[NSString alloc] initWithData: data encoding: NSISOLatin1StringEncoding];
    if(!string)
        string = [[NSString alloc] initWithData: data encoding: NSMacOSRomanStringEncoding];
```

The first attempt is with UTF-8. This is not just because it's a useful and common encoding, but also because UTF-8 has a rigid syntactical structure which is extremely unlikely to be reproduced by accident. In other words, if your data is a valid UTF-8 string, the odds are extremely high that it was actually intended to be UTF-8. It's difficult to find meaningful text that can be encoded with a different encoding and still produce a valid UTF-8 string.

If it's not UTF-8, then the next attempt is with Latin-1, because it's so common. If that fails (depending on which version of Latin-1 Cocoa means by this constant, it might not define characters for all possible byte values), then the final fallback is MacRoman. Since MacRoman defines characters for every byte value, this last attempt will always work, although it may not produce the correct output. And because MacRoman is ASCII-compatible, and most other encodings are at least somewhat ASCII-compatible, this step is likely to give you the correct values for any ASCII characters in the string, even if you get bad characters for the rest.

Note that there is no case for `NSASCIIStringEncoding`. It's not necessary, because any ASCII text will be correctly decoded by the `NSUTF8StringEncoding` step.

Depending on your context, you may want to try a different sequence of encodings. For example, if you expect to see mostly Japanese text, then you may want to try `NSJapaneseEUCStringEncoding` or `NSShiftJISStringEncoding` instead of, or perhaps before, `NSISOLatin1StringEncoding`.

The key elements are to first try UTF-8, because it has an extremely low false positive rate, then try any specific encodings which make sense for your scenario, and finally, if necessary, fall back to an encoding like MacRoman which will always produce some kind of sensible output.

**Conclusion**  
 That's it for this week. I hope that now you understand a little more about character encodings, what they are, how they work, and how to use them. If you learn only one lesson from this post, let it be this: use UTF-8!

Come back in another week for another post. Until then, [send in your suggestions for topics](mailto:mike@mikeash.com). Friday Q&A is driven by user ideas, so if you want to see something discussed here, please submit your idea.

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2010-02-19-character-encodings.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
