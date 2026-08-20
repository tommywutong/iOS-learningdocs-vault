---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/HTMLparser/CompositePage.html
archived_at: '2026-07-15T07:23:25.217849Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| HTMLparser.h | HTMLparser.h | HTMLparser.h | HTMLparser.h | HTMLparser.h |

|  |  |
| --- | --- |
| __Includes:__ | [<libxml/xmlversion.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/xmlversion/index.html#//apple_ref/doc/header/xmlversion.h)  [<libxml/parser.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/parser/index.html#//apple_ref/doc/header/parser.h) |

## Introduction

---

## Typedefs

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| htmlParserOption | htmlParserOption | htmlParserOption | htmlParserOption | htmlParserOption |

---

```
typedef enum {
    HTML_PARSE_NOERROR = 1<<5, /* suppress error reports */
    HTML_PARSE_NOWARNING= 1<<6, /* suppress warning reports */
    HTML_PARSE_PEDANTIC = 1<<7, /* pedantic error reporting */
    HTML_PARSE_NOBLANKS = 1<<8, /* remove blank nodes */
    HTML_PARSE_NONET = 1<<11 /* Forbid network access */
} htmlParserOption;
```

##### Discussion

xmlParserOption:

This is the set of XML parser options that can be passed down
to the xmlReadDoc() and similar calls.

## Globals

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

Interfaces for the Push mode.

## #defines

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| htmlDefaultSubelement | htmlDefaultSubelement | htmlDefaultSubelement | htmlDefaultSubelement | htmlDefaultSubelement |

---

```swift
#define htmlDefaultSubelement(
    elt) elt->defaultsubelt
```

##### Discussion

htmlDefaultSubelement:
@elt: HTML element

Returns the default subelement for this element

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| htmlElementAllowedHereDesc | htmlElementAllowedHereDesc | htmlElementAllowedHereDesc | htmlElementAllowedHereDesc | htmlElementAllowedHereDesc |

---

```swift
#define htmlElementAllowedHereDesc(
    parent,elt) \ htmlElementAllowedHere((
    parent), (
    elt)->name)
```

##### Discussion

htmlElementAllowedHereDesc:
@parent: HTML parent element
@elt: HTML element

Checks whether an HTML element description may be a
direct child of the specified element.

Returns 1 if allowed; 0 otherwise.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| htmlRequiredAttrs | htmlRequiredAttrs | htmlRequiredAttrs | htmlRequiredAttrs | htmlRequiredAttrs |

---

```
#define htmlRequiredAttrs(
    elt)
```

##### Discussion

htmlRequiredAttrs:
@elt: HTML element

Returns the attributes required for the specified element.

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
