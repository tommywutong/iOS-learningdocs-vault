---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/xlink/CompositePage.html
archived_at: '2026-07-15T07:23:29.129294Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xlink.h | xlink.h | xlink.h | xlink.h | xlink.h |

|  |  |
| --- | --- |
| __Includes:__ | [<libxml/xmlversion.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/xmlversion/index.html#//apple_ref/doc/header/xmlversion.h)  [<libxml/tree.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/tree/index.html#//apple_ref/doc/header/tree.h) |

## Introduction

---

## Typedefs

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xlinkExtendedLinkFunk | xlinkExtendedLinkFunk | xlinkExtendedLinkFunk | xlinkExtendedLinkFunk | xlinkExtendedLinkFunk |

---

```
typedef void (*xlinkExtendedLinkFunk)(
    void *ctx,
    xmlNodePtr node,
    int nbLocators,
    const xlinkHRef *hrefs,
    const xlinkRole *roles,
    int nbArcs,
    const xlinkRole *from,
    const xlinkRole *to,
    xlinkShow *show,
    xlinkActuate *actuate,
    int nbTitles,
    const xlinkTitle *titles,
    const xmlChar **langs);
```

##### Discussion

xlinkExtendedLinkFunk:
@ctx: user data pointer
@node: the node carrying the link
@nbLocators: the number of locators detected on the link
@hrefs: pointer to the array of locator hrefs
@roles: pointer to the array of locator roles
@nbArcs: the number of arcs detected on the link
@from: pointer to the array of source roles found on the arcs
@to: pointer to the array of target roles found on the arcs
@show: array of values for the show attributes found on the arcs
@actuate: array of values for the actuate attributes found on the arcs
@nbTitles: the number of titles detected on the link
@title: array of titles detected on the link
@langs: array of xml:lang values for the titles

This is the prototype for a extended link detection callback.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xlinkExtendedLinkSetFunk | xlinkExtendedLinkSetFunk | xlinkExtendedLinkSetFunk | xlinkExtendedLinkSetFunk | xlinkExtendedLinkSetFunk |

---

```
typedef void (*xlinkExtendedLinkSetFunk) (
    void *ctx,
    xmlNodePtr node,
    int nbLocators,
    const xlinkHRef *hrefs,
    const xlinkRole *roles,
    int nbTitles,
    const xlinkTitle *titles,
    const xmlChar **langs);
```

##### Discussion

xlinkExtendedLinkSetFunk:
@ctx: user data pointer
@node: the node carrying the link
@nbLocators: the number of locators detected on the link
@hrefs: pointer to the array of locator hrefs
@roles: pointer to the array of locator roles
@nbTitles: the number of titles detected on the link
@title: array of titles detected on the link
@langs: array of xml:lang values for the titles

This is the prototype for a extended link set detection callback.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xlinkHandler | xlinkHandler | xlinkHandler | xlinkHandler | xlinkHandler |

---

```
typedef struct _xlinkHandler xlinkHandler;
```

##### Discussion

This is the structure containing a set of Links detection callbacks.

There is no default xlink callbacks, if one want to get link
recognition activated, those call backs must be provided before parsing.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xlinkHRef | xlinkHRef | xlinkHRef | xlinkHRef | xlinkHRef |

---

```
typedef xmlChar *xlinkHRef;
```

##### Discussion

Various defines for the various Link properties.

NOTE: the link detection layer will try to resolve QName expansion
of namespaces. If "foo" is the prefix for "http://foo.com/"
then the link detection layer will expand role="foo:myrole"
to "http://foo.com/:myrole".
NOTE: the link detection layer will expand URI-Refences found on
href attributes by using the base mechanism if found.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xlinkNodeDetectFunc | xlinkNodeDetectFunc | xlinkNodeDetectFunc | xlinkNodeDetectFunc | xlinkNodeDetectFunc |

---

```
typedef void (*xlinkNodeDetectFunc) (
    void *ctx,
    xmlNodePtr node);
```

##### Discussion

xlinkNodeDetectFunc:
@ctx: user data pointer
@node: the node to check

This is the prototype for the link detection routine.
It calls the default link detection callbacks upon link detection.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xlinkSimpleLinkFunk | xlinkSimpleLinkFunk | xlinkSimpleLinkFunk | xlinkSimpleLinkFunk | xlinkSimpleLinkFunk |

---

```
typedef void (*xlinkSimpleLinkFunk) (
    void *ctx,
    xmlNodePtr node,
    const xlinkHRef href,
    const xlinkRole role,
    const xlinkTitle title);
```

##### Discussion

xlinkSimpleLinkFunk:
@ctx: user data pointer
@node: the node carrying the link
@href: the target of the link
@role: the role string
@title: the link title

This is the prototype for a simple link detection callback.

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
