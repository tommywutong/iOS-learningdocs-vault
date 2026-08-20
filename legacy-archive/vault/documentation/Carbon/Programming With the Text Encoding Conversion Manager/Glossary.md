---
title: Programming With the Text Encoding Conversion Manager
apple_id: TP40000932
resource_type: Guide
platform: macOS
topic: Data Management
technology: CoreServices
published: '2005-07-07'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/ProgWithTECM/tecmgr_glossary/tecmgr_glossary.html
archived_at: '2026-07-15T05:24:12.146942Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Programming With the Text Encoding Conversion Manager](Introduction%20to%20Programming%20With%20the%20Text%20Encoding%20Conversion%20Manager.md)


[Previous](Document%20Revision%20History.md)

# Glossary

- __character__

  An atomic unit of content for text data. A character is an abstract entity without any particular appearance; characters include letters, digits, punctuation, and symbols.

- __character encoding scheme__

  A text encoding that maps a sequence of characters (from one or more coded character sets) to a sequence of bytes, in order to combine characters from multiple coded character sets or to permit easier handling of some coded character sets. Compare coded character set.

- __code fragment__

  See [fragment](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzsfvbuqmrqg4wugsscijbusqsc).

- __Code Fragment Manager (CFM)__

  In Mac OS 9 and earlier, refers to the part of the Macintosh system software that prepares fragments for execution.

- __code point__

  An integer value that represents (or can represent) a character.

- __coded character__

  A character together with its numeric representation in a particular coded character set.

- __coded character set__

  A text encoding that maps each character in a set of characters to a particular integer from a set of integers. Compare character encoding scheme.

- __code-switching scheme__

  A character encoding scheme that allows switching between different coded character sets, usually signaled by escape or other special sequences. See also character coding scheme.

- __content transfer encoding__

  See transfer encoding syntax.

- __converter object__

  An instance of data that tells a text converter how to convert text from a particular source encoding to a particular destination encoding, and maintains any necessary state information that applies to the conversion of a particular stream of text.

- __destination encoding__

  The text encoding that describes the desired encoding of the text after conversion. Compare source encoding.

- __direct conversion__

  A text conversion by the Text Encoding Converter that can be handled in one step (that is, by one call to a single plug-in). Compare indirect conversion.

- __Extended UNIX Code (EUC)__

  A type of packing scheme that is used as the text encoding for UNIX workstations that handle East Asian languages. See also packing scheme.

- __fallback mapping__

  A character or sequence of characters used to replace a character that has no direct equivalent in the destination encoding. For example, if the target encoding does not contain “å,” a possible fallback mapping would be “aa.”

- __fragment__

  In Mac OS 9 and earlier, a fragment refers to a block of executable code or data. Fragments are handled by the Code Fragment Manager. See also Code Fragment Manager.

- __glyph image__

  A visual element used to represent one or more characters.

- __indirect conversion__

  A text conversion by the Text Encoding Converter that requires stepping through one or more intermediate conversions before reaching the desired destination encoding. Compare direct conversion.

- __Internet__

  The name given to the world-wide network of computers.

- __loose mapping__

  A mapping between text encodings that preserves the information content of text but does not permit round-trip fidelity.

- __Multipurpose Internet Mail Extensions (MIME)__

  Mechanisms for specifying and describing the format of Internet message bodies.

- __packing scheme__

  A type of character encoding scheme where characters are encoded using a variable number of bytes. Typically certain bytes signal the beginning of a character and how many additional bytes are used to encode the character. Character sets with a large number of elements are often stored using a packing scheme. See also character encoding scheme.

- __perfect round-trip conversion__

  This occurs when mapping a character from a particular source encoding to a particular destination encoding (usually Unicode) and then back to the source encoding again yields the original character.

- __plug in__

  See text encoding conversion plug-in.

- __presentation form__

  An abstraction of a range of glyph images, which represents a standard way to display a particular character or group of characters in a particular context as specified by a particular writing system. See also glyph image.

- __script__

  A collection of related characters, subsets of which are required to write a particular language. Some examples of scripts are Latin, Greek, Hiragana, Katakana, and Han.

- __sniffer__

  A function included with a text conversion plug-in that scans text for features that identify a particular text encoding.

- __source encoding__

  The text encoding that describes the encoding of the text before conversion. Compare destination encoding.

- __strict mapping__

  A mapping between text encodings that preserves the information content of text and permits round-trip fidelity.

- __text element__

  A group of one or more characters that is treated as a single entity for a particular process such as collation, display, or transcoding.

- __text encoding__

  The coded character set or character encoding scheme used to represent a particular piece of text. See also coded character set, character encoding scheme.

- __text encoding base__

  The primary specification of a text encoding, and one component of a text encoding specification. See also text encoding specification, text encoding variant, text encoding format.

- __text encoding conversion plug-in__

  A code fragment that provides conversion services between pairs of encodings. A text encoding conversion plug-in informs the Text Encoding Conversion Manager about its conversion and encoding analysis capabilities

- __text encoding format__

  A subset of the text encoding specification that specifies the byte format of the encoding. For example, a format might specify that the encoding take up only 7-bits for transmission over 7-bit channels. See also text encoding specification, universal transformation format.

- __text encoding specification__

  A scalar value that defines a text encoding to be used in a conversion. It includes information about the text encoding base, the text encoding variant, and the text encoding format.

- __text encoding variant__

  A specification of one among possibly several minor variants or subsets of a particular text encoding base. See also text encoding specification, text encoding base.

- __Text Encoding Conversion Manager__

  A pair of shared library extensions—namely, the Text Encoding Converter and the Unicode Converter—that facilitate text encoding conversion on Mac OS–based computers

- __Text Encoding Converter__

  A shared library extension that provides the services for general and algorithmic encoding conversions or multi-encoding streams. The Text Encoding Converter sometimes uses the Unicode Converter.

- __transfer encoding syntax__

  A transformation applied to text encoded using a character encoding scheme to allow it to be transmitted by a specific protocol or set of protocols. This is normally used to permit 8-bit data to be sent through channels that can only handle 7-bit values. Also called content transfer encoding. Compare character encoding scheme, [universal transformation format](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzsfvbuqmrqg4wugsscjfeuurki).

- __Unicode__

  A universal character set that includes tens of thousands of characters covering the world’s major written languages along with many symbols.

- __Unicode Converter__

  A shared library extension that provides table-based conversion between no-subset variants of Unicode, in either UTF-16 or UTF-8, and many other encodings.

- __universal transformation format__

  Special formats that allow transmission of Unicode characters over 7-bit (UTF-7) and 8-bit (UTF-8) channels. See also transfer encoding syntax.

- __writing system__

  A set of characters from one or more scripts that are used to write a particular language and the rules that govern the presentation of those characters.

[Previous](Document%20Revision%20History.md)

