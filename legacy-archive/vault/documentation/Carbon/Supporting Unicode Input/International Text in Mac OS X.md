---
title: Supporting Unicode Input
apple_id: TP40000951
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2008-10-01'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/Supporting_Unicode_Input/sui_concepts/sui_concepts.html
archived_at: '2026-07-15T05:24:41.741532Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Supporting Unicode Input](Introduction%20to%20Supporting%20Unicode%20Input.md)


[Next](Supporting%20Unicode%20Input%20in%20Applications%20and%20Input%20Methods.md)[Previous](Introduction%20to%20Supporting%20Unicode%20Input.md)

# International Text in Mac OS X

This section contains an overview of international
text handling on the Mac OS and a more specific introduction to
some of the Unicode facilities available with Mac OS X. If you would
like more information on converting between text encodings, see _[Programming With the Text Encoding Conversion Manager](../Programming%20With%20the%20Text%20Encoding%20Conversion%20Manager/Introduction%20to%20Programming%20With%20the%20Text%20Encoding%20Conversion%20Manager.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzs)_.

Written representation of a spoken language relies on a writing
system. A _writing system_ is an artificial construct
used to record language in written form. It can be viewed as having
three main components—language, scripts, and orthography—with well-defined
relations to one another.

A _script_ comprises a set of symbols that
represent the components of a language. A writing system uses one
or more scripts for the symbols required to represent linguistic elements,
which include sound, meaning, syntax and so forth. A script can
be coupled with one language, or it can represent and be used by
many languages. Moreover, a language can have more than one script
associated with it. For example, the Japanese language uses the
Japanese script, while the French, Italian, and Spanish languages
all use parts of the Latin script.

A script exists apart from both the languages it represents
and the writing systems for which it is used. (A small number of
scripts, less than 100, are used by writing systems despite the
large number of existing modern and archaic languages.) A special
category of scripts, called pseudoscripts, exists for use with other
scripts. These pseudoscripts include symbols, numbers, and punctuation.

Writing systems can use different scripts at the same time.
A writing system uses at least one script and typically one or more
pseudoscripts. In this sense, it is best to refer to the characters
a writing system includes as a repertoire of characters, rather
than a character set, because these characters can belong to different
scripts.

The writing system for a language entails an _orthography_ which
defines the relationship between the written language and one or
more scripts. Among the rules an orthography specifies are rules
of directionality, level of discreteness, and units of representation.
For example, for mixed-directional text, the direction of a paragraph
is important. For writing systems based in European languages, a
paragraph is considered a unit of representation, as is a word.
Word division and paragraph identification are easily determined
for these languages, but this is not necessarily the case for other
writing systems, such as those based in Japanese or Indic languages.

Traditionally, in the Mac OS, a _script system_ has
been understood to be a collection of software facilities that provides
for the representation of a specific writing system. This usage
of the term “script” in the phrase “script system” should
not be confused with the more current, linguistics-derived notion
of scripts that is used in the Mac OS and described in [Languages, Writing Systems, Scripts, and Orthographies](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydcojtfvbecssjjbcuuqq).

Types of Mac OS script systems include the following:

- single-byte
  simple: small character set, non-contextual, not bidirectional (example: English)
- single-byte complex: small character set, but with contextual
  or bidirectional text (example: Devanagari)
- double-byte: large character set (examples: Japanese, Korean,
  Chinese, and Simplified Chinese)

At minimum, a script system consists of the following items:

- keyboard
  resources, which provide for text input in any language from any
  keyboard; these allow for convenient switching from one input language
  to another on a single keyboard
- international resources, which contain information specific
  to a particular language, such as its date and time formats, sorting
  order, and word-break rules
- fonts, that is, sets of glyphs that are associated with specified
  characters

A _script code_ is a numeric value indicating
a particular Mac OS script system. Constants are defined for each
of the script codes recognized by the Mac OS.

A writing system’s alphabet, numbers, punctuation, and other
writing marks consist of characters. A _character_ is
a symbolic representation of an element of a writing system; it is
the concept of, for example, “lowercase a” or “number 3”.

In memory, text is stored as character codes, where each code
is a numeric value that defines a particular character. A _character
encoding_ is the organization of the set of numeric codes
that represent all the meaningful characters of a script system
in memory. There are two fundamental classes of Mac OS character
encodings: single-byte and double-byte.

_Unicode_ is an international standard that
combines the characters for all commonly used writing systems into
a single, coded character set, based upon a 16-bit character encoding
standard. With a universal character encoding such as Unicode, the
character sets of separate writing systems do not overlap. Furthermore,
Unicode resolves the issue of conflicting character encodings within
a single writing system; for example, in Unicode, there is no overlap
between Roman character codes and the Symbol font’s character codes.

By means of keyboard input, the user can create text that
your application stores as character codes. The system reports the
user’s key-down, key-up, and auto-key events to your application
through events. Key-down and key-up events report that the user pressed
or released a key, respectively. Auto-key events report that the
user has held a key down for a certain amount of time. For keyboard-related
events, the application receives both the virtual key code and the
character code for the key that is pressed, as well as the state
of any modifier keys (Shift, Caps Lock, Command, Option, and Control)
at the time of the event.

To obtain this information for your application, the Mac OS
uses keyboard resources to convert key presses into the correct
character codes for the current writing system, taking into account
the type of keyboard being used.

_Key translation_ is the process by which
character codes are generated. Each keyboard has a particular physical
arrangement of keys, and each keypress generates a value called a
raw key code, which indicates which key was pressed. The keyboard
driver that handles the keypress maps these raw key codes to keyboard-independent
virtual key codes.

Any given script system has one or more keyboard-layout resources.
The keyboard-layout resources provide script-specific maps for converting
a virtual key code into the character code that is passed to your
application. As part of the key-translation process, the keyboard-layout
resources must take into account the current dead-key state. A _dead
key_ is a keypress or modifier-plus-keypress combination
that produces no immediate character output, but instead affects
the character(s) that are ultimately produced by the following key
press(es).

A keyboard layout is what the Key Caps application shows.
For the purposes of this document, a keyboard-layout resource is
the critical item in determining keyboard layout; changing the keyboard
layout means changing the keyboard-layout resource. Because keyboard
layouts are independent of the physical keyboard attached to the
computer, your application has the flexibility of changing text
input from one writing system to another by simply using a different
keyboard-layout resource.

For languages with large character sets, it is impractical
to manufacture keyboards with keys for every possible character.
In such a case, it is usually the job of an input method, working
in conjunction with a keyboard, to handle text input. An _input
method_ is a software module, often independent of the
application it serves, that performs complex processing of text
input, prior to the application’s processing of the text. A typical
example of an input method is a translation service that converts
character codes that can be entered from the keyboard into character
codes that cannot; text input in Japanese, Chinese, and Korean usually
requires an input method.

The set of Mac OS script codes that identify particular script
systems includes Unicode, which is handled as a special Mac OS script
code. The Text Encoding Converter and other Mac OS facilities use
the constant `kTextEncodingUnicodeDefault` (0x0100)
to designate Unicode. However, because some components have only
7 bits available for a script code, rather than the typical 16 bits,
the value `smUnicodeScript` (0x7E)
can also be used to indicate Unicode. For example, the Text Encoding
Converter handles the `smUnicodeScript` value
similar to `kTextEncodingUnicodeDefault`.

Similar to the (pre-Unicode) keyboard-layout resource (`'KCHR'`),
the Unicode keyboard-layout resource (`'uchr'`)
contains the data necessary to map virtual key codes to character
codes for various keyboard layouts. However, the `'uchr'` resource
specifies Unicode keyboard layouts—that is, keyboard layouts which
produce Unicode character codes, rather than characters in a Mac
OS encoding.

Because some Unicode character codes can be mapped to Mac
OS encoded character codes (while some cannot), for the purposes
of key translation there are considered to be two categories of
Unicode keyboard-layout resources. The first category of `'uchr'` resources
is one that produces Unicode character codes that are all within
the range of a single Mac OS encoding. That is, these partial Unicode `'uchr'` resources
contain only Unicode characters that can be mapped to characters
belonging to the Mac OS encoding associated with its ID range.

The second category of `'uchr'` resources
may produce any Unicode characters. That is, these full Unicode `'uchr'` resources
contain Unicode characters that are either not all within the range
of a single Mac OS encoding or are not within the range of any Mac
OS encoding. Table
2-1 shows the relationships of keyboard-layout
resources to differing types of text input.

__Table 1-1__  Text input types and keyboard layouts

| Input Type | Keyboard Layout (resource type, ID) |
| Produces Mac OS encoded characters | KCHR, >= 0 |
| Produces partial Unicode characters | uchr, >= 0 |
| Produces full Unicode characters | uchr < 0 |

The function `UCKeyTranslate` uses
the `'uchr'` resource to
produce Unicode character codes. However, unlike its non-Unicode
counterpart (the `KeyTranslate` function), `UCKeyTranslate` also
does the following:

1. Outputs multiple
   character codes. A single keycode (or a dead-key sequence) can produce
   a string of up to 255 Unicode characters. This facility is useful
   both for some international script systems and for the production
   of macros. As an example of the former, the Devanagari keyboard
   in the Indian Language Kit must be able to produce up to three characters
   from a single keypress to support the keyboard standards of India.
2. Allows multiple dead keys. The keyboard standards for some
   countries require double dead keys. For example, Greek keyboards
   use two dead keys for adding diacritical marks.
3. Handles virtual key codes with a range greater than 0-127.
   While this requirement is currently uncommon in the Mac OS, some
   types of keyboards—for example, older Kanji keyboards and keyboards
   for some other operating systems—may use a larger key code range.
4. Allows virtual key code mapping to depend on keyboard type.
   While the use of virtual key codes should theoretically remove all
   dependencies on particular physical keyboards, in some cases key
   translation does depend on the keyboard type (due to certain scripts,
   languages, and regions needing subtle differences in layout for
   specific keyboards). The `UCKeyTranslate` function
   accommodates this need by requesting keyboard type information and
   using the `'uchr'` resource
   to access the proper keyboard’s mapping tables in cases where
   there is a keyboard-specific dependency, thus eliminating the need
   to use the `'itlk'` resource.

The Keyboard menu in Mac OS X appears on the menu bar when
more than one script system is enabled. It permits the user to choose
among keyboard layouts, input methods, and script systems, for text
input.

If there are input methods for any of the Mac OS double-byte
script systems that are enabled, the Keyboard menu shows only the
input methods; otherwise, in the absence of input methods, it shows
the keyboard layouts. For all other enabled script systems, including
Unicode, the keyboard menu shows keyboard layouts and input methods.

To display a full Unicode script system in the Keyboard menu,
the System must include an international bundle resource (`'itlb'`)
with a resource ID of `smUnicodeScript` (0x7E) and
one or more full Unicode keyboard layouts or input methods.

Full Unicode keyboard layouts and input methods (that is,
for input sources that produce Unicode characters that are not within
the range of a single Mac encoding), if enabled, are shown in their
own section of the menu, after all of those for Mac OS script systems.

[Next](Supporting%20Unicode%20Input%20in%20Applications%20and%20Input%20Methods.md)[Previous](Introduction%20to%20Supporting%20Unicode%20Input.md)

