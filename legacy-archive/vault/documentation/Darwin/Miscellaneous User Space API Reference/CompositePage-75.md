---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/hash/CompositePage.html
archived_at: '2026-07-15T07:23:26.800798Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| hash.h | hash.h | hash.h | hash.h | hash.h |

|  |  |
| --- | --- |
| __Includes:__ | ["wx/defs.h"](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/defs/index.html#//apple_ref/doc/header/defs.h)  "wx/object.h"  ["wx/list.h"](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/list/index.html#//apple_ref/doc/header/list.h)  "wx/dynarray.h"  [<libxml/xmlversion.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/xmlversion/index.html#//apple_ref/doc/header/xmlversion.h)  [<libxml/parser.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/parser/index.html#//apple_ref/doc/header/parser.h) |

## Introduction

---

## Typedefs

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlHashCopier | xmlHashCopier | xmlHashCopier | xmlHashCopier | xmlHashCopier |

---

```
typedef void *(*xmlHashCopier)(
    void *payload,
    xmlChar *name);
```

##### Discussion

xmlHashCopier:
@payload: the data in the hash
@name: the name associated

Callback to copy data from a hash.

Returns a copy of the data or NULL in case of error.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlHashDeallocator | xmlHashDeallocator | xmlHashDeallocator | xmlHashDeallocator | xmlHashDeallocator |

---

```
typedef void (*xmlHashDeallocator)(
    void *payload,
    xmlChar *name);
```

##### Discussion

xmlHashDeallocator:
@payload: the data in the hash
@name: the name associated

Callback to free data from a hash.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlHashScanner | xmlHashScanner | xmlHashScanner | xmlHashScanner | xmlHashScanner |

---

```
typedef void (*xmlHashScanner)(
    void *payload,
    void *data,
    xmlChar *name);
```

##### Discussion

xmlHashScanner:
@payload: the data in the hash
@data: extra scannner data
@name: the name associated

Callback when scanning data in a hash with the simple scanner.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlHashScannerFull | xmlHashScannerFull | xmlHashScannerFull | xmlHashScannerFull | xmlHashScannerFull |

---

```
typedef void (*xmlHashScannerFull)(
    void *payload,
    void *data,
    const xmlChar *name,
    const xmlChar *name2,
    const xmlChar *name3);
```

##### Discussion

xmlHashScannerFull:
@payload: the data in the hash
@data: extra scannner data
@name: the name associated
@name2: the second name associated
@name3: the third name associated

Callback when scanning data in a hash with the full scanner.

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
