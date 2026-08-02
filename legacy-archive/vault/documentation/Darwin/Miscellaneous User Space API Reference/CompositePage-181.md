---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/xmlschemas/CompositePage.html
archived_at: '2026-07-15T07:23:29.275900Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlschemas.h | xmlschemas.h | xmlschemas.h | xmlschemas.h | xmlschemas.h |

|  |  |
| --- | --- |
| __Includes:__ | [<libxml/xmlversion.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/xmlversion/index.html#//apple_ref/doc/header/xmlversion.h)  [<libxml/tree.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/tree/index.html#//apple_ref/doc/header/tree.h) |

## Introduction

---

## Typedefs

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlSchema | xmlSchema | xmlSchema | xmlSchema | xmlSchema |

---

```
typedef struct _xmlSchema xmlSchema;
```

##### Discussion

The schemas related types are kept internal

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlSchemaValidError | xmlSchemaValidError | xmlSchemaValidError | xmlSchemaValidError | xmlSchemaValidError |

---

```
typedef enum {
    XML_SCHEMAS_ERR_OK = 0,
    XML_SCHEMAS_ERR_NOROOT = 1,
    XML_SCHEMAS_ERR_UNDECLAREDELEM,
    XML_SCHEMAS_ERR_NOTTOPLEVEL,
    XML_SCHEMAS_ERR_MISSING,
    XML_SCHEMAS_ERR_WRONGELEM,
    XML_SCHEMAS_ERR_NOTYPE,
    XML_SCHEMAS_ERR_NOROLLBACK,
    XML_SCHEMAS_ERR_ISABSTRACT,
    XML_SCHEMAS_ERR_NOTEMPTY,
    XML_SCHEMAS_ERR_ELEMCONT,
    XML_SCHEMAS_ERR_HAVEDEFAULT,
    XML_SCHEMAS_ERR_NOTNILLABLE,
    XML_SCHEMAS_ERR_EXTRACONTENT,
    XML_SCHEMAS_ERR_INVALIDATTR,
    XML_SCHEMAS_ERR_INVALIDELEM,
    XML_SCHEMAS_ERR_NOTDETERMINIST,
    XML_SCHEMAS_ERR_CONSTRUCT,
    XML_SCHEMAS_ERR_INTERNAL,
    XML_SCHEMAS_ERR_NOTSIMPLE,
    XML_SCHEMAS_ERR_ATTRUNKNOWN,
    XML_SCHEMAS_ERR_ATTRINVALID,
    XML_SCHEMAS_ERR_VALUE,
    XML_SCHEMAS_ERR_FACET,
    XML_SCHEMAS_ERR_,
    XML_SCHEMAS_ERR_XXX
} xmlSchemaValidError;
```

##### Discussion

This error codes are obsolete; not used any more.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlSchemaValidityErrorFunc | xmlSchemaValidityErrorFunc | xmlSchemaValidityErrorFunc | xmlSchemaValidityErrorFunc | xmlSchemaValidityErrorFunc |

---

```
typedef void (*xmlSchemaValidityErrorFunc) (
    void *ctx,
    const char *msg,
    ...);
```

##### Discussion

A schemas validation context

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlSchemaValidOption | xmlSchemaValidOption | xmlSchemaValidOption | xmlSchemaValidOption | xmlSchemaValidOption |

---

```
typedef enum {
    XML_SCHEMA_VAL_VC_I_CREATE = 1<<0 /* Default/fixed: create an attribute node
 * or an element's text node on the instance.
        */
} xmlSchemaValidOption;
```

##### Discussion

xmlSchemaValidOption:

This is the set of XML Schema validation options.

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
