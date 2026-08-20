---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/stl_pair/CompositePage.html
archived_at: '2026-07-15T07:23:28.497833Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| stl_pair.h | stl_pair.h | stl_pair.h | stl_pair.h | stl_pair.h |

## Introduction

This is an internal header file, included by other library headers.
You should not attempt to use it directly.

---

## Functions

**[make_pair](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3nmfvwkx3qmfuxex2ej5hfitcjjzfv6mdygjsdsyjrgm4tq)**
:

**[pair](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3qmfuxex2ej5hfitcjjzfv6mdygjtdgmrtmrtdq)**
:

**[pair( __b)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3qmfuxex2ej5hfitcjjzfv6mdygjtdgmrtmy4ta)**
:

**[pair(__p .)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3qmfuxex2ej5hfitcjjzfv6mdygjtdiztgmzrta)**
:

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| make_pair | make_pair | make_pair | make_pair | make_pair |

---

```
// _GLIBCXX_RESOLVE_LIB_DEFECTS
// 181. make_pair() unintended behavior
template<class _T1, class _T2> inline pair<_T1, _T2> make_pair(
    _T1 __x,
    _T2 __y)
```

##### Parameters

**`x`**
: The first object.

**`y`**
: The second object.

##### Return Value

A newly-constructed pair<> object of the appropriate type.

The standard requires that the objects be passed by reference-to-const,
but LWG issue #181 says they should be passed by const value. We follow
the LWG by default.

##### Discussion

@brief A convenience wrapper for creating a pair from two objects.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| pair | pair | pair | pair | pair |

---

```
pair() : first(), second()
```

##### Discussion

The default constructor creates @c first and @c second using their
\* respective default constructors.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| pair( __b) | pair( __b) | pair( __b) | pair( __b) | pair( __b) |

---

```
pair(
    const _T1& __a,
    const _T2& __b) : first(
    __a), second(
    __b)
```

##### Discussion

Two objects may be passed to a @c pair constructor to be copied.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| pair(__p .) | pair(__p .) | pair(__p .) | pair(__p .) | pair(__p .) |

---

```
template<class _U1, class _U2> pair(
    const pair<_U1, _U2>& __p) : first(
    __p.first), second(
    __p.second)
```

##### Discussion

There is also a templated copy ctor for the @c pair class itself.

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
