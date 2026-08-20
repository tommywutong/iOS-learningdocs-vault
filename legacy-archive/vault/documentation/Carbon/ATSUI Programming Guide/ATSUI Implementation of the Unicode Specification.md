---
title: ATSUI Programming Guide
apple_id: TP30000984
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2008-09-30'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/ATSUI_Concepts/atsui_app_unicode/atsui_appendixA.html
archived_at: '2026-07-15T05:21:48.073974Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [ATSUI Programming Guide](Introduction%20to%20ATSUI%20Programming%20Guide.md)


[Next](Font%20Features.md)[Previous](Direct-Access%20Tasks-%20Working%20With%20Glyph%20Data.md)

# ATSUI Implementation of the Unicode Specification

This appendix provides additional details about the implementation of the Unicode specification in ATSUI. ATSUI provides full layout support for Unicode 3.2 and supports text rendering for all the features required by scripts included with version 2.1 of the Unicode standard or later. It does not provide other Unicode-related text processing services such as date and time formatting, collation, or string matching. The ability of ATSUI to render Unicode text is limited only by the available fonts the user has installed.

The correct handling of many Unicode characters requires that the current font supports those characters properly. For example, correct ligature formation requires that the font supports those features using Apple Advanced Typography (AAT) tables. If there is more than one equivalent combining character sequence for a given glyph, the font is responsible for mapping all such sequences to the correct glyph. For example, ATSUI does not automatically support conjoining Jamo in a Korean font that specifies precomposed glyphs only. For more details on the required AAT font tables and tools for creating them, see the description of Apple Advanced Typography at [http://developer.apple.com/fonts/](https://developer.apple.com/fonts/).

ATSUI version 1.1 and later does not support the following control characters:

- U+00AD (soft hyphen)
- U+206A (inhibit symmetric swapping)
- U+206B (activate symmetric swapping)
- U+206C (inhibit Arabic form shaping)
- U+206D (activate Arabic form shaping)
- U+206E (national digit shapes)
- U+206F (normal digit shapes)
- Use of U+005F (spacing underscore or low line) to underline other characters

You can, however, achieve similar effects achieved by these control characters by setting certain style attributes. (See [ATSUI Style and Text Layout Objects](ATSUI%20Style%20and%20Text%20Layout%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydamrzfvkfami) for information on style objects and style attributes.) In addition, ATSUI currently treats the following characters as hard line breaks:

- U+000A (line feed)
- U+000C (form feed)
- U+000D (carriage return)
- U+2028 (line separator)
- U+2029 (paragraph separator)

ATSUI fully renders nonspacing marks, though correct font tables are required to render and process nonspacing marks correctly. To locate text element boundaries, ATSUI defines a cluster as a run consisting of a base character plus zero or more nonbase characters, where a base character is defined as one whose combining class is 0 and whose glyph is not deleted. Whether or not a set of characters is a cluster is also dependent upon the behavior of the specific font you are using with those characters.

ATSUI uses the Unicode Utilities function `UCFindTextBreak` to determine the boundaries of text elements such as character clusters, words, and lines. For example, character clusters as determined by `UCFindTextBreak` include the following:

- a run consisting of a base character plus zero or more combining characters
- a sequence of conjoining Jamo that would normally be displayed as a single composed Hangul character

However, ATSUI extends the `UCFindTextBreak` function’s notion of text boundaries so that they may also be affected by rendering behavior, and may thus be dependent on the behavior of the specific font that is being used to render the text.

ATSUI fully supports the Unicode bidirectional algorithm, including the bidirectional ordering codes. Correct bidirectional processing requires that the font have the correct glyph properties set (for example, mirrored punctuation). Other characters that require font support for correct processing include invisible characters such as U+FEFF (zero-width no-break space). There are some characters that ATSUI maps to either a zero-width glyph or a nonmarking return.

Unicode code points, or scalar values, range from 0 to U+10FFFF (excluding the surrogate range 0xD800 to 0xDFFF and certain disallowed values such as 0xFFFF). There are three encoding forms for Unicode: UTF-32, UTF-16, and UTF-8. UTF-32 uses 32-bit code units, and it can represent Unicode scalar values directly. UTF-16 uses 16-bit code units, and it is the encoding form used by ATSUI. Unicode scalar values in the range 0 to U+FFFF, the Basic Multilingual Plane (BMP), are represented in UTF-16 by a single code unit with the same numeric value.

Unicode values in the range U+10000 to U+10FFFF are represented in UTF-16 by a pair of UTF-16 code units: A high surrogate in the range 0xD800 to 0xDBFF followed by a low surrogate in the range 0xDC00 to 0xDFFF (the mapping between Unicode scalar values above U+FFFF and surrogate pairs is described in the Unicode Standard).

A surrogate pair should generally be treated as a single character for such editing operations as text insertion, deletion, selection, hit-testing, and cursor movement. In other areas such as ligatures or accented letters, you may treat surrogates as a single or multiple entities.

Until version 3.1 of the Unicode Standard, there were no characters encoded outside the BMP—that is, no characters with scalar values above U+FFFF, and thus no characters that required surrogate pairs in UTF-16. However, Unicode 3.1 encodes a number of characters that require surrogates, including many CJK ideographs that are in the Hiragino Japanese fonts included with Mac OS X. ATSUI and the Unicode Utilities provide support for handling such non-BMP characters as surrogate pairs in UTF-16.

The character properties used by ATSUI support the standard characters in Unicode 3.2 plus the characters that Apple has defined in the corporate private use zone. ATSUI requires that white space and symmetric swapping-related properties be correctly set in the font. Characters not defined in the standard are assumed to be direction-neutral.

[Next](Font%20Features.md)[Previous](Direct-Access%20Tasks-%20Working%20With%20Glyph%20Data.md)

