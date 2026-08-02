---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/parserInternals/CompositePage.html
archived_at: '2026-07-15T07:23:27.548758Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| parserInternals.h | parserInternals.h | parserInternals.h | parserInternals.h | parserInternals.h |

|  |  |
| --- | --- |
| __Includes:__ | [<libxml/xmlversion.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/xmlversion/index.html#//apple_ref/doc/header/xmlversion.h)  [<libxml/parser.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/parser/index.html#//apple_ref/doc/header/parser.h)  [<libxml/HTMLparser.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/HTMLparser/index.html#//apple_ref/doc/header/HTMLparser.h)  [<libxml/chvalid.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/chvalid/index.html#//apple_ref/doc/header/chvalid.h) |

## Introduction

---

## Constants

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlStringText | xmlStringText | xmlStringText | xmlStringText | xmlStringText |

---

```
extern  const xmlChar xmlStringText[];
```

##### Discussion

Global variables used for predefined strings.

## Typedefs

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlEntityReferenceFunc | xmlEntityReferenceFunc | xmlEntityReferenceFunc | xmlEntityReferenceFunc | xmlEntityReferenceFunc |

---

```
typedef void (*xmlEntityReferenceFunc) (
    xmlEntityPtr ent,
    xmlNodePtr firstNode,
    xmlNodePtr lastNode);
```

##### Discussion

xmlEntityReferenceFunc:
@ent: the entity
@firstNode: the fist node in the chunk
@lastNode: the last nod in the chunk

Callback function used when one needs to be able to track back the
provenance of a chunk of nodes inherited from an entity replacement.

## Globals

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlParserMaxDepth | xmlParserMaxDepth | xmlParserMaxDepth | xmlParserMaxDepth | xmlParserMaxDepth |

---

```
extern  unsigned int xmlParserMaxDepth;
```

##### Discussion

xmlParserMaxDepth:

arbitrary depth limit for the XML documents that we allow to
process. This is not a limitation of the parser but a safety
boundary feature.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XMLPUBFUN | XMLPUBFUN | XMLPUBFUN | XMLPUBFUN | XMLPUBFUN |

---

```
 Macros which declare an exportable function */
#define XMLPUBFUN  ;
```

##### Discussion

Parser context.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XMLPUBFUN | XMLPUBFUN | XMLPUBFUN | XMLPUBFUN | XMLPUBFUN |

---

```
 Macros which declare an exportable function */
#define XMLPUBFUN  ;
```

##### Discussion

Entities

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XMLPUBFUN | XMLPUBFUN | XMLPUBFUN | XMLPUBFUN | XMLPUBFUN |

---

```
 Macros which declare an exportable function */
#define XMLPUBFUN  ;
```

##### Discussion

Input Streams.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XMLPUBFUN | XMLPUBFUN | XMLPUBFUN | XMLPUBFUN | XMLPUBFUN |

---

```
 Macros which declare an exportable function */
#define XMLPUBFUN  ;
```

##### Discussion

Namespaces.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XMLPUBFUN | XMLPUBFUN | XMLPUBFUN | XMLPUBFUN | XMLPUBFUN |

---

```
 Macros which declare an exportable function */
#define XMLPUBFUN  ;
```

##### Discussion

Generic production rules.

## #defines

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| INPUT_CHUNK | INPUT_CHUNK | INPUT_CHUNK | INPUT_CHUNK | INPUT_CHUNK |

---

```
#define INPUT_CHUNK 250
```

##### Discussion

INPUT_CHUNK:

The parser tries to always have that amount of input ready.
One of the point is providing context when reporting errors.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| IS_ASCII_DIGIT | IS_ASCII_DIGIT | IS_ASCII_DIGIT | IS_ASCII_DIGIT | IS_ASCII_DIGIT |

---

```
#define IS_ASCII_DIGIT(
    c)
```

##### Discussion

IS_ASCII_DIGIT(c)
@c: an xmlChar value

Macro to check [0-9]

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| IS_ASCII_LETTER | IS_ASCII_LETTER | IS_ASCII_LETTER | IS_ASCII_LETTER | IS_ASCII_LETTER |

---

```
#define IS_ASCII_LETTER(
    c)
```

##### Discussion

IS_ASCII_LETTER(c)
@c: an xmlChar value

Macro to check [a-zA-Z]

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| IS_BASECHAR | IS_BASECHAR | IS_BASECHAR | IS_BASECHAR | IS_BASECHAR |

---

```
#define IS_BASECHAR(
    c) xmlIsBaseCharQ(
    c)
```

##### Discussion

IS_BASECHAR:
@c: an UNICODE value (int)

Macro to check the following production in the XML spec:

[85] BaseChar ::= ... long list see REC ...

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| IS_BLANK | IS_BLANK | IS_BLANK | IS_BLANK | IS_BLANK |

---

```
#define IS_BLANK(
    c) xmlIsBlankQ(
    c)
```

##### Discussion

IS_BLANK:
@c: an UNICODE value (int)

Macro to check the following production in the XML spec:

[3] S ::= (#x20 | #x9 | #xD | #xA)+

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| IS_BLANK_CH | IS_BLANK_CH | IS_BLANK_CH | IS_BLANK_CH | IS_BLANK_CH |

---

```
#define IS_BLANK_CH(
    c) xmlIsBlank_ch(
    c)
```

##### Discussion

IS_BLANK_CH:
@c: an xmlChar value (normally unsigned char)

Behaviour same as IS_BLANK

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| IS_BYTE_CHAR | IS_BYTE_CHAR | IS_BYTE_CHAR | IS_BYTE_CHAR | IS_BYTE_CHAR |

---

```
#define IS_BYTE_CHAR(
    c) xmlIsChar_ch(
    c)
```

##### Discussion

IS_BYTE_CHAR:
@c: an byte value (int)

Macro to check the following production in the XML spec:

[2] Char ::= #x9 | #xA | #xD | [#x20...]
any byte character in the accepted range

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| IS_CHAR | IS_CHAR | IS_CHAR | IS_CHAR | IS_CHAR |

---

```
#define IS_CHAR(
    c) xmlIsCharQ(
    c)
```

##### Discussion

IS_CHAR:
@c: an UNICODE value (int)

Macro to check the following production in the XML spec:

[2] Char ::= #x9 | #xA | #xD | [#x20-#xD7FF] | [#xE000-#xFFFD]
| [#x10000-#x10FFFF]
any Unicode character, excluding the surrogate blocks, FFFE, and FFFF.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| IS_CHAR_CH | IS_CHAR_CH | IS_CHAR_CH | IS_CHAR_CH | IS_CHAR_CH |

---

```
#define IS_CHAR_CH(
    c) xmlIsChar_ch(
    c)
```

##### Discussion

IS_CHAR_CH:
@c: an xmlChar (usually an unsigned char)

Behaves like IS_CHAR on single-byte value

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| IS_COMBINING | IS_COMBINING | IS_COMBINING | IS_COMBINING | IS_COMBINING |

---

```
#define IS_COMBINING(
    c) xmlIsCombiningQ(
    c)
```

##### Discussion

IS_COMBINING:
@c: an UNICODE value (int)

Macro to check the following production in the XML spec:

[87] CombiningChar ::= ... long list see REC ...

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| IS_COMBINING_CH | IS_COMBINING_CH | IS_COMBINING_CH | IS_COMBINING_CH | IS_COMBINING_CH |

---

```
#define IS_COMBINING_CH(
    c) 0
```

##### Discussion

IS_COMBINING_CH:
@c: an xmlChar (usually an unsigned char)

Always false (all combining chars > 0xff)

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| IS_DIGIT | IS_DIGIT | IS_DIGIT | IS_DIGIT | IS_DIGIT |

---

```
#define IS_DIGIT(
    c) xmlIsDigitQ(
    c)
```

##### Discussion

IS_DIGIT:
@c: an UNICODE value (int)

Macro to check the following production in the XML spec:

[88] Digit ::= ... long list see REC ...

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| IS_DIGIT_CH | IS_DIGIT_CH | IS_DIGIT_CH | IS_DIGIT_CH | IS_DIGIT_CH |

---

```
#define IS_DIGIT_CH(
    c) xmlIsDigit_ch(
    c)
```

##### Discussion

IS_DIGIT_CH:
@c: an xmlChar value (usually an unsigned char)

Behaves like IS_DIGIT but with a single byte argument

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| IS_EXTENDER | IS_EXTENDER | IS_EXTENDER | IS_EXTENDER | IS_EXTENDER |

---

```
#define IS_EXTENDER(
    c) xmlIsExtenderQ(
    c)
```

##### Discussion

IS_EXTENDER:
@c: an UNICODE value (int)

Macro to check the following production in the XML spec:

[89] Extender ::= #x00B7 | #x02D0 | #x02D1 | #x0387 | #x0640 |
#x0E46 | #x0EC6 | #x3005 | [#x3031-#x3035] |
[#x309D-#x309E] | [#x30FC-#x30FE]

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| IS_EXTENDER_CH | IS_EXTENDER_CH | IS_EXTENDER_CH | IS_EXTENDER_CH | IS_EXTENDER_CH |

---

```
#define IS_EXTENDER_CH(
    c) xmlIsExtender_ch(
    c)
```

##### Discussion

IS_EXTENDER_CH:
@c: an xmlChar value (usually an unsigned char)

Behaves like IS_EXTENDER but with a single-byte argument

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| IS_IDEOGRAPHIC | IS_IDEOGRAPHIC | IS_IDEOGRAPHIC | IS_IDEOGRAPHIC | IS_IDEOGRAPHIC |

---

```
#define IS_IDEOGRAPHIC(
    c) xmlIsIdeographicQ(
    c)
```

##### Discussion

IS_IDEOGRAPHIC:
@c: an UNICODE value (int)

Macro to check the following production in the XML spec:

[86] Ideographic ::= [#x4E00-#x9FA5] | #x3007 | [#x3021-#x3029]

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| IS_LETTER | IS_LETTER | IS_LETTER | IS_LETTER | IS_LETTER |

---

```
#define IS_LETTER(
    c)
```

##### Discussion

IS_LETTER:
@c: an UNICODE value (int)

Macro to check the following production in the XML spec:

[84] Letter ::= BaseChar | Ideographic

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| IS_LETTER_CH | IS_LETTER_CH | IS_LETTER_CH | IS_LETTER_CH | IS_LETTER_CH |

---

```
#define IS_LETTER_CH(
    c) xmlIsBaseChar_ch(
    c)
```

##### Discussion

IS_LETTER_CH:
@c: an xmlChar value (normally unsigned char)

Macro behaves like IS_LETTER, but only check base chars

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| IS_PUBIDCHAR | IS_PUBIDCHAR | IS_PUBIDCHAR | IS_PUBIDCHAR | IS_PUBIDCHAR |

---

```
#define IS_PUBIDCHAR(
    c) xmlIsPubidCharQ(
    c)
```

##### Discussion

IS_PUBIDCHAR:
@c: an UNICODE value (int)

Macro to check the following production in the XML spec:

[13] PubidChar ::= #x20 | #xD | #xA | [a-zA-Z0-9] | [-'()+,./:=?;!\*#@$_%]

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| IS_PUBIDCHAR_CH | IS_PUBIDCHAR_CH | IS_PUBIDCHAR_CH | IS_PUBIDCHAR_CH | IS_PUBIDCHAR_CH |

---

```
#define IS_PUBIDCHAR_CH(
    c) xmlIsPubidChar_ch(
    c)
```

##### Discussion

IS_PUBIDCHAR_CH:
@c: an xmlChar value (normally unsigned char)

Same as IS_PUBIDCHAR but for single-byte value

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| MOVETO_ENDTAG | MOVETO_ENDTAG | MOVETO_ENDTAG | MOVETO_ENDTAG | MOVETO_ENDTAG |

---

```
#define MOVETO_ENDTAG(
    p) \ while ((
    *p) && (
    *(
    p) != '>')) (
    p)++
```

##### Discussion

MOVETO_ENDTAG:
@p: and UTF8 string pointer

Skips to the next '>' char.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| MOVETO_STARTTAG | MOVETO_STARTTAG | MOVETO_STARTTAG | MOVETO_STARTTAG | MOVETO_STARTTAG |

---

```
#define MOVETO_STARTTAG(
    p) \ while ((
    *p) && (
    *(
    p) != '<')) (
    p)++
```

##### Discussion

MOVETO_STARTTAG:
@p: and UTF8 string pointer

Skips to the next '<' char.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| SKIP_EOL | SKIP_EOL | SKIP_EOL | SKIP_EOL | SKIP_EOL |

---

```
#define SKIP_EOL(
    p) \ if (
    *(
    p) == 0x13) {
    p++; if (
    *(
    p) == 0x10) p++;
} \ if (
    *(
    p) == 0x10) {
    p++; if (
    *(
    p) == 0x13) p++;
}
```

##### Discussion

SKIP_EOL:
@p: and UTF8 string pointer

Skips the end of line chars.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_MAX_NAMELEN | XML_MAX_NAMELEN | XML_MAX_NAMELEN | XML_MAX_NAMELEN | XML_MAX_NAMELEN |

---

```
#define XML_MAX_NAMELEN 100
```

##### Discussion

XML_MAX_NAMELEN:

Identifiers can be longer, but this will be more costly
at runtime.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SUBSTITUTE_BOTH | XML_SUBSTITUTE_BOTH | XML_SUBSTITUTE_BOTH | XML_SUBSTITUTE_BOTH | XML_SUBSTITUTE_BOTH |

---

```
#define XML_SUBSTITUTE_BOTH 3
```

##### Discussion

XML_SUBSTITUTE_BOTH:

Both general and parameter entities need to be substituted.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SUBSTITUTE_NONE | XML_SUBSTITUTE_NONE | XML_SUBSTITUTE_NONE | XML_SUBSTITUTE_NONE | XML_SUBSTITUTE_NONE |

---

```
#define XML_SUBSTITUTE_NONE 0
```

##### Discussion

XML_SUBSTITUTE_NONE:

If no entities need to be substituted.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SUBSTITUTE_PEREF | XML_SUBSTITUTE_PEREF | XML_SUBSTITUTE_PEREF | XML_SUBSTITUTE_PEREF | XML_SUBSTITUTE_PEREF |

---

```
#define XML_SUBSTITUTE_PEREF 2
```

##### Discussion

XML_SUBSTITUTE_PEREF:

Whether parameter entities need to be substituted.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SUBSTITUTE_REF | XML_SUBSTITUTE_REF | XML_SUBSTITUTE_REF | XML_SUBSTITUTE_REF | XML_SUBSTITUTE_REF |

---

```
#define XML_SUBSTITUTE_REF 1
```

##### Discussion

XML_SUBSTITUTE_REF:

Whether general entities need to be substituted.

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Last Updated: 2006-06-20
