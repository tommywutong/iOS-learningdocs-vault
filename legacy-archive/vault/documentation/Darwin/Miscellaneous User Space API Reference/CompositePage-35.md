---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/debugXML/CompositePage.html
archived_at: '2026-07-15T07:23:26.457237Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| debugXML.h | debugXML.h | debugXML.h | debugXML.h | debugXML.h |

|  |  |
| --- | --- |
| __Includes:__ | <stdio.h>  [<libxml/xmlversion.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/xmlversion/index.html#//apple_ref/doc/header/xmlversion.h)  [<libxml/tree.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/tree/index.html#//apple_ref/doc/header/tree.h)  [<libxml/xpath.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/xpath/index.html#//apple_ref/doc/header/xpath.h) |

## Introduction

---

## Typedefs

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlShellCmd | xmlShellCmd | xmlShellCmd | xmlShellCmd | xmlShellCmd |

---

```
typedef int (*xmlShellCmd) (
    xmlShellCtxtPtr ctxt,
    char *arg,
    xmlNodePtr node,
    xmlNodePtr node2);
```

##### Discussion

xmlShellCmd:
@ctxt: a shell context
@arg: a string argument
@node: a first node
@node2: a second node

This is a generic signature for the XML shell functions.

Returns an int, negative returns indicating errors.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlShellCtxt | xmlShellCtxt | xmlShellCtxt | xmlShellCtxt | xmlShellCtxt |

---

```
typedef struct _xmlShellCtxt xmlShellCtxt;
```

##### Discussion

xmlShellCtxt:

A debugging shell context.
TODO: add the defined function tables.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlShellReadlineFunc | xmlShellReadlineFunc | xmlShellReadlineFunc | xmlShellReadlineFunc | xmlShellReadlineFunc |

---

```
typedef char * (*xmlShellReadlineFunc)(
    char *prompt);
```

##### Discussion

xmlShellReadlineFunc:
@prompt: a string prompt

This is a generic signature for the XML shell input function.

Returns a string which will be freed by the Shell.

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
