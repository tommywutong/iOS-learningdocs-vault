---
title: Font Handling
apple_id: 10000093i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AppKit
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/FontHandling/Concepts/CharactersAndGlyphs.html
archived_at: '2026-07-15T07:15:42.424786Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Font Handling](Introduction%20to%20Font%20Handling.md)


[Next](Calculating%20Glyph%20Layout.md)[Previous](Querying%20Aqua%20Font%20Variations.md)

# Characters and Glyphs

Characters are
conceptual entities that correspond to units of written language.
Examples of characters include the letters of the Roman alphabet,
the Kanji ideographs used in Japanese, and symbols that indicate
mathematical operations. Characters are represented as numbers in
a computer’s memory or on disk, and a character encoding defines
the mapping between a numerical value and a specific character.
For example, the ASCII and Unicode character
encodings both assign the value 97 (decimal) to the character “a”.
The Cocoa text system uses the Unicode character encoding internally,
although it can read and write other encodings on disk.

You can think of a glyph as the rendered image of a character.
The words of this sentence are made visible through glyphs. A collection
of glyphs that share certain graphic qualities is called a font.

The difference between a character and a glyph isn’t immediately
apparent in English since there’s typically a one-to-one mapping
between the two. But, in some Indic languages, for example, a single
character can map to more than one glyph. And, in many languages,
two or more characters may be needed to specify a single glyph.

To take a simple example, the glyph “ö” can be the result
of two characters, one representing the base character “o” and
the other representing the diacritical mark “¨”. A user of
a word processor can press an arrow key one time to move the insertion
point from one side of the “ö” glyph to the other; however,
the current position in the character stream must be incremented
by two to account for the two characters that make up the single glyph.

Thus, the text system must manage two related but different
streams of data: the stream of characters (and their attributes)
and the stream of glyphs that are derived from these characters.
The NSTextStorage object
stores the attributed characters, and the NSLayoutManager object stores
the derived glyphs. Finding the correspondence between these two
streams is the responsibility of the layout manager.

For a given glyph, the layout manager can find the corresponding
character or characters in the character stream. Similarly, for
a given character, the layout manager can locate the associated
glyph or glyphs. For example, when a user selects a range of text,
the layout manager must determine which range of characters corresponds
to the selection.

When characters are deleted, some glyphs may have to be redrawn. For example,
if the user deletes the characters “ee” from the word “feel”,
the “f” and “l” can be represented by the “fl” ligature rather than the two glyphs
“f” and “l”. The NSLayoutManager object directs a glyph
generator object to generate new glyphs as needed. Once the glyphs
are regenerated, the text must be laid out and displayed. Working
with the NSTextContainer object and other objects of the text system,
the layout manager determines where each glyph appears in the NSTextView.
Finally, the text view renders the text.

Because an NSLayoutManager object is central to the operation
of the text system, it also serves as the repository of information
shared by various components of the system. For more information
about NSLayoutManager, refer to its reference documentation and
to _[Text Layout Programming Guide](../Text%20Layout%20Programming%20Guide/Introduction%20to%20Text%20Layout%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge2tq2i)_.

[Next](Calculating%20Glyph%20Layout.md)[Previous](Querying%20Aqua%20Font%20Variations.md)

