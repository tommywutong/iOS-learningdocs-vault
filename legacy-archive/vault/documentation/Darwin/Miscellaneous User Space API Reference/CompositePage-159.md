---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/tree/CompositePage.html
archived_at: '2026-07-15T07:23:28.912777Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tree.h | tree.h | tree.h | tree.h | tree.h |

|  |  |
| --- | --- |
| __Includes:__ | <stdio.h>  [<libxml/xmlversion.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/xmlversion/index.html#//apple_ref/doc/header/xmlversion.h)  [<libxml/xmlstring.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/xmlstring/index.html#//apple_ref/doc/header/xmlstring.h)  [<libxml/xmlregexp.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/xmlregexp/index.html#//apple_ref/doc/header/xmlregexp.h)  [<libxml/xmlmemory.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/xmlmemory/index.html#//apple_ref/doc/header/xmlmemory.h)  "backward_warning.h"  <ext/rb_tree>  "backward_warning.h"  <ext/rb_tree>  "backward_warning.h"  <ext/rb_tree> |

## Introduction

---

## Typedefs

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlAttr | xmlAttr | xmlAttr | xmlAttr | xmlAttr |

---

```
typedef struct _xmlAttr xmlAttr;
```

##### Discussion

xmlAttr:

An attribute on an XML node.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlAttribute | xmlAttribute | xmlAttribute | xmlAttribute | xmlAttribute |

---

```
typedef struct _xmlAttribute xmlAttribute;
```

##### Discussion

xmlAttribute:

An Attribute declaration in a DTD.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlAttributeDefault | xmlAttributeDefault | xmlAttributeDefault | xmlAttributeDefault | xmlAttributeDefault |

---

```
typedef enum {
    XML_ATTRIBUTE_NONE = 1,
    XML_ATTRIBUTE_REQUIRED,
    XML_ATTRIBUTE_IMPLIED,
    XML_ATTRIBUTE_FIXED
} xmlAttributeDefault;
```

##### Discussion

xmlAttributeDefault:

A DTD Attribute default definition.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlAttributeType | xmlAttributeType | xmlAttributeType | xmlAttributeType | xmlAttributeType |

---

```
typedef enum {
    XML_ATTRIBUTE_CDATA = 1,
    XML_ATTRIBUTE_ID,
    XML_ATTRIBUTE_IDREF,
    XML_ATTRIBUTE_IDREFS,
    XML_ATTRIBUTE_ENTITY,
    XML_ATTRIBUTE_ENTITIES,
    XML_ATTRIBUTE_NMTOKEN,
    XML_ATTRIBUTE_NMTOKENS,
    XML_ATTRIBUTE_ENUMERATION,
    XML_ATTRIBUTE_NOTATION
} xmlAttributeType;
```

##### Discussion

xmlAttributeType:

A DTD Attribute type definition.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlBuffer | xmlBuffer | xmlBuffer | xmlBuffer | xmlBuffer |

---

```
typedef struct _xmlBuffer xmlBuffer;
```

##### Discussion

xmlBuffer:

A buffer structure.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlBufferAllocationScheme | xmlBufferAllocationScheme | xmlBufferAllocationScheme | xmlBufferAllocationScheme | xmlBufferAllocationScheme |

---

```
typedef enum {
    XML_BUFFER_ALLOC_DOUBLEIT,
    XML_BUFFER_ALLOC_EXACT,
    XML_BUFFER_ALLOC_IMMUTABLE
} xmlBufferAllocationScheme;
```

##### Discussion

xmlBufferAllocationScheme:

A buffer allocation scheme can be defined to either match exactly the
need or double it's allocated size each time it is found too small.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlDoc | xmlDoc | xmlDoc | xmlDoc | xmlDoc |

---

```
typedef struct _xmlDoc xmlDoc;
```

##### Discussion

xmlDoc:

An XML document.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlDtd | xmlDtd | xmlDtd | xmlDtd | xmlDtd |

---

```
typedef struct _xmlDtd xmlDtd;
```

##### Discussion

xmlDtd:

An XML DTD, as defined by

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlElement | xmlElement | xmlElement | xmlElement | xmlElement |

---

```
typedef struct _xmlElement xmlElement;
```

##### Discussion

xmlElement:

An XML Element declaration from a DTD.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlElementContent | xmlElementContent | xmlElementContent | xmlElementContent | xmlElementContent |

---

```
typedef struct _xmlElementContent xmlElementContent;
```

##### Discussion

xmlElementContent:

An XML Element content as stored after parsing an element definition
in a DTD.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlElementContentOccur | xmlElementContentOccur | xmlElementContentOccur | xmlElementContentOccur | xmlElementContentOccur |

---

```
typedef enum {
    XML_ELEMENT_CONTENT_ONCE = 1,
    XML_ELEMENT_CONTENT_OPT,
    XML_ELEMENT_CONTENT_MULT,
    XML_ELEMENT_CONTENT_PLUS
} xmlElementContentOccur;
```

##### Discussion

xmlElementContentOccur:

Possible definitions of element content occurrences.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlElementContentType | xmlElementContentType | xmlElementContentType | xmlElementContentType | xmlElementContentType |

---

```
typedef enum {
    XML_ELEMENT_CONTENT_PCDATA = 1,
    XML_ELEMENT_CONTENT_ELEMENT,
    XML_ELEMENT_CONTENT_SEQ,
    XML_ELEMENT_CONTENT_OR
} xmlElementContentType;
```

##### Discussion

xmlElementContentType:

Possible definitions of element content types.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlElementTypeVal | xmlElementTypeVal | xmlElementTypeVal | xmlElementTypeVal | xmlElementTypeVal |

---

```
typedef enum {
    XML_ELEMENT_TYPE_UNDEFINED = 0,
    XML_ELEMENT_TYPE_EMPTY = 1,
    XML_ELEMENT_TYPE_ANY,
    XML_ELEMENT_TYPE_MIXED,
    XML_ELEMENT_TYPE_ELEMENT
} xmlElementTypeVal;
```

##### Discussion

xmlElementTypeVal:

The different possibilities for an element content type.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlEnumeration | xmlEnumeration | xmlEnumeration | xmlEnumeration | xmlEnumeration |

---

```
typedef struct _xmlEnumeration xmlEnumeration;
```

##### Discussion

xmlEnumeration:

List structure used when there is an enumeration in DTDs.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlID | xmlID | xmlID | xmlID | xmlID |

---

```
typedef struct _xmlID xmlID;
```

##### Discussion

xmlID:

An XML ID instance.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlNode | xmlNode | xmlNode | xmlNode | xmlNode |

---

```
typedef struct _xmlNode xmlNode;
```

##### Discussion

xmlNode:

A node in an XML tree.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlNotation | xmlNotation | xmlNotation | xmlNotation | xmlNotation |

---

```
typedef struct _xmlNotation xmlNotation;
```

##### Discussion

xmlNotation:

A DTD Notation definition.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlNs | xmlNs | xmlNs | xmlNs | xmlNs |

---

```
typedef struct _xmlNs xmlNs;
```

##### Discussion

xmlNs:

An XML namespace.
Note that prefix == NULL is valid, it defines the default namespace
within the subtree (until overridden).

xmlNsType is unified with xmlElementType.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlRef | xmlRef | xmlRef | xmlRef | xmlRef |

---

```
typedef struct _xmlRef xmlRef;
```

##### Discussion

xmlRef:

An XML IDREF instance.

## #defines

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| BASE_BUFFER_SIZE | BASE_BUFFER_SIZE | BASE_BUFFER_SIZE | BASE_BUFFER_SIZE | BASE_BUFFER_SIZE |

---

```
#define BASE_BUFFER_SIZE 4096
```

##### Discussion

BASE_BUFFER_SIZE:

default buffer size 4000.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_GET_CONTENT | XML_GET_CONTENT | XML_GET_CONTENT | XML_GET_CONTENT | XML_GET_CONTENT |

---

```swift
#define XML_GET_CONTENT(
    n) \ ((
    n)->type == XML_ELEMENT_NODE ? NULL : (
    n)->content)
```

##### Discussion

XML_GET_CONTENT:

Macro to extract the content pointer of a node.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_GET_LINE | XML_GET_LINE | XML_GET_LINE | XML_GET_LINE | XML_GET_LINE |

---

```
#define XML_GET_LINE(
    n) \ (
    xmlGetLineNo(
    n))
```

##### Discussion

XML_GET_LINE:

Macro to extract the line number of an element node.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_LOCAL_NAMESPACE | XML_LOCAL_NAMESPACE | XML_LOCAL_NAMESPACE | XML_LOCAL_NAMESPACE | XML_LOCAL_NAMESPACE |

---

```
#define XML_LOCAL_NAMESPACE XML_NAMESPACE_DECL
```

##### Discussion

XML_LOCAL_NAMESPACE:

A namespace declaration node.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_XML_ID | XML_XML_ID | XML_XML_ID | XML_XML_ID | XML_XML_ID |

---

```
#define XML_XML_ID
```

##### Discussion

XML_XML_ID:

This is the name for the special xml:id attribute

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_XML_NAMESPACE | XML_XML_NAMESPACE | XML_XML_NAMESPACE | XML_XML_NAMESPACE | XML_XML_NAMESPACE |

---

```
#define XML_XML_NAMESPACE \ (
    const xmlChar *) "http://www.w3.org/XML/1998/namespace"
```

##### Discussion

XML_XML_NAMESPACE:

This is the namespace for the special xml: prefix predefined in the
XML Namespace specification.

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
