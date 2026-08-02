---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/HTMLtree/CompositePage.html
archived_at: '2026-07-15T07:23:25.232495Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| HTMLtree.h | HTMLtree.h | HTMLtree.h | HTMLtree.h | HTMLtree.h |

|  |  |
| --- | --- |
| __Includes:__ | <stdio.h>  [<libxml/xmlversion.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/xmlversion/index.html#//apple_ref/doc/header/xmlversion.h)  [<libxml/tree.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/tree/index.html#//apple_ref/doc/header/tree.h)  [<libxml/HTMLparser.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/HTMLparser/index.html#//apple_ref/doc/header/HTMLparser.h) |

## Introduction

---

## #defines

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| HTML_COMMENT_NODE | HTML_COMMENT_NODE | HTML_COMMENT_NODE | HTML_COMMENT_NODE | HTML_COMMENT_NODE |

---

```
#define HTML_COMMENT_NODE XML_COMMENT_NODE
```

##### Discussion

HTML_COMMENT_NODE:

Macro. A comment in a HTML document is really implemented
the same way as a comment in an XML document.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| HTML_ENTITY_REF_NODE | HTML_ENTITY_REF_NODE | HTML_ENTITY_REF_NODE | HTML_ENTITY_REF_NODE | HTML_ENTITY_REF_NODE |

---

```
#define HTML_ENTITY_REF_NODE XML_ENTITY_REF_NODE
```

##### Discussion

HTML_ENTITY_REF_NODE:

Macro. An entity reference in a HTML document is really implemented
the same way as an entity reference in an XML document.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| HTML_PI_NODE | HTML_PI_NODE | HTML_PI_NODE | HTML_PI_NODE | HTML_PI_NODE |

---

```
#define HTML_PI_NODE XML_PI_NODE
```

##### Discussion

HTML_PI_NODE:

Macro. A processing instruction in a HTML document is really implemented
the same way as a processing instruction in an XML document.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| HTML_PRESERVE_NODE | HTML_PRESERVE_NODE | HTML_PRESERVE_NODE | HTML_PRESERVE_NODE | HTML_PRESERVE_NODE |

---

```
#define HTML_PRESERVE_NODE XML_CDATA_SECTION_NODE
```

##### Discussion

HTML_PRESERVE_NODE:

Macro. A preserved node in a HTML document is really implemented
the same way as a CDATA section in an XML document.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| HTML_TEXT_NODE | HTML_TEXT_NODE | HTML_TEXT_NODE | HTML_TEXT_NODE | HTML_TEXT_NODE |

---

```
#define HTML_TEXT_NODE XML_TEXT_NODE
```

##### Discussion

HTML_TEXT_NODE:

Macro. A text node in a HTML document is really implemented
the same way as a text node in an XML document.

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
