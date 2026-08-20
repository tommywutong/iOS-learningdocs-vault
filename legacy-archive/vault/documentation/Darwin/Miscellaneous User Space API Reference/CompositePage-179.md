---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/xmlreader/CompositePage.html
archived_at: '2026-07-15T07:23:29.242916Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlreader.h | xmlreader.h | xmlreader.h | xmlreader.h | xmlreader.h |

|  |  |
| --- | --- |
| __Includes:__ | [<libxml/xmlversion.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/xmlversion/index.html#//apple_ref/doc/header/xmlversion.h)  [<libxml/tree.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/tree/index.html#//apple_ref/doc/header/tree.h)  [<libxml/xmlIO.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/xmlIO/index.html#//apple_ref/doc/header/xmlIO.h)  [<libxml/relaxng.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/relaxng/index.html#//apple_ref/doc/header/relaxng.h) |

## Introduction

---

## Typedefs

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlParserProperties | xmlParserProperties | xmlParserProperties | xmlParserProperties | xmlParserProperties |

---

```
typedef enum {
    XML_PARSER_LOADDTD = 1,
    XML_PARSER_DEFAULTATTRS = 2,
    XML_PARSER_VALIDATE = 3,
    XML_PARSER_SUBST_ENTITIES = 4
} xmlParserProperties;
```

##### Discussion

xmlParserProperties:

Some common options to use with xmlTextReaderSetParserProp, but it
is better to use xmlParserOption and the xmlReaderNewxxx and
xmlReaderForxxx APIs now.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlParserSeverities | xmlParserSeverities | xmlParserSeverities | xmlParserSeverities | xmlParserSeverities |

---

```
typedef enum {
    XML_PARSER_SEVERITY_VALIDITY_WARNING = 1,
    XML_PARSER_SEVERITY_VALIDITY_ERROR = 2,
    XML_PARSER_SEVERITY_WARNING = 3,
    XML_PARSER_SEVERITY_ERROR = 4
} xmlParserSeverities;
```

##### Discussion

xmlParserSeverities:

How severe an error callback is when the per-reader error callback API
is used.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlReaderTypes | xmlReaderTypes | xmlReaderTypes | xmlReaderTypes | xmlReaderTypes |

---

```
typedef enum {
    XML_READER_TYPE_NONE = 0,
    XML_READER_TYPE_ELEMENT = 1,
    XML_READER_TYPE_ATTRIBUTE = 2,
    XML_READER_TYPE_TEXT = 3,
    XML_READER_TYPE_CDATA = 4,
    XML_READER_TYPE_ENTITY_REFERENCE = 5,
    XML_READER_TYPE_ENTITY = 6,
    XML_READER_TYPE_PROCESSING_INSTRUCTION = 7,
    XML_READER_TYPE_COMMENT = 8,
    XML_READER_TYPE_DOCUMENT = 9,
    XML_READER_TYPE_DOCUMENT_TYPE = 10,
    XML_READER_TYPE_DOCUMENT_FRAGMENT = 11,
    XML_READER_TYPE_NOTATION = 12,
    XML_READER_TYPE_WHITESPACE = 13,
    XML_READER_TYPE_SIGNIFICANT_WHITESPACE = 14,
    XML_READER_TYPE_END_ELEMENT = 15,
    XML_READER_TYPE_END_ENTITY = 16,
    XML_READER_TYPE_XML_DECLARATION = 17
} xmlReaderTypes;
```

##### Discussion

xmlReaderTypes:

Predefined constants for the different types of nodes.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlTextReader | xmlTextReader | xmlTextReader | xmlTextReader | xmlTextReader |

---

```
typedef struct _xmlTextReader xmlTextReader;
```

##### Discussion

xmlTextReader:

Structure for an xmlReader context.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlTextReaderMode | xmlTextReaderMode | xmlTextReaderMode | xmlTextReaderMode | xmlTextReaderMode |

---

```
typedef enum {
    XML_TEXTREADER_MODE_INITIAL = 0,
    XML_TEXTREADER_MODE_INTERACTIVE = 1,
    XML_TEXTREADER_MODE_ERROR = 2,
    XML_TEXTREADER_MODE_EOF =3,
    XML_TEXTREADER_MODE_CLOSED = 4,
    XML_TEXTREADER_MODE_READING = 5
} xmlTextReaderMode;
```

##### Discussion

xmlTextReaderMode:

Internal state values for the reader.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlTextReaderPtr | xmlTextReaderPtr | xmlTextReaderPtr | xmlTextReaderPtr | xmlTextReaderPtr |

---

```
typedef xmlTextReader *xmlTextReaderPtr;
```

##### Discussion

xmlTextReaderPtr:

Pointer to an xmlReader context.

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
