---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/container/CompositePage.html
archived_at: '2026-07-15T07:23:26.343332Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| container.h | container.h | container.h | container.h | container.h |

|  |  |
| --- | --- |
| __Includes:__ | [<net-snmp/types.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/types/index.html#//apple_ref/doc/header/types.h)  <net-snmp/library/factory.h>  <net-snmp/library/snmp_logging.h> |

## Introduction

---

## Functions

**[netsnmp_compare_cstring](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3omv2hg3tnobpwg33nobqxezk7mnzxi4tjnztq)**
:

**[netsnmp_compare_mem](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3omv2hg3tnobpwg33nobqxezk7nvsw2)**
:

**[netsnmp_compare_netsnmp_index](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3omv2hg3tnobpwg33nobqxezk7nzsxi43onvyf62lomrsxq)**
:

**[netsnmp_container_simple_free](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3omv2hg3tnobpwg33oorqws3tfojpxg2lnobwgkx3gojswk)**
:

**[while](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3xnbuwyzk7irhu4vcmjfhewxzqpaytqmdcgu2tena)**
:

**[while( x)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3xnbuwyzi)**
:

**[while( x)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3xnbuwyzk7irhu4vcmjfhewxzqpaytqmdbg4ywcoa)**
:

**[while( x)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3xnbuwyzk7irhu4vcmjfhewxzqpaytqmdbmfqwcoa)**
:

**[while(x -)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3xnbuwyzk7irhu4vcmjfhewxzqpaytqmdbmm2dqna)**
:

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| netsnmp_compare_cstring | netsnmp_compare_cstring | netsnmp_compare_cstring | netsnmp_compare_cstring | netsnmp_compare_cstring |

---

```
int netsnmp_compare_cstring(
    const void *lhs,
    const void *rhs);
```

##### Discussion

first data element is a 'char \*'

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| netsnmp_compare_mem | netsnmp_compare_mem | netsnmp_compare_mem | netsnmp_compare_mem | netsnmp_compare_mem |

---

```
int netsnmp_compare_mem(
    const char *lhs,
    size_t lhs_len,
    const char *rhs,
    size_t rhs_len);
```

##### Discussion

useful for octet strings

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| netsnmp_compare_netsnmp_index | netsnmp_compare_netsnmp_index | netsnmp_compare_netsnmp_index | netsnmp_compare_netsnmp_index | netsnmp_compare_netsnmp_index |

---

```
int netsnmp_compare_netsnmp_index(
    const void *lhs,
    const void *rhs);
```

##### Discussion

first data element is a 'netsnmp_index'

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| netsnmp_container_simple_free | netsnmp_container_simple_free | netsnmp_container_simple_free | netsnmp_container_simple_free | netsnmp_container_simple_free |

---

```
void netsnmp_container_simple_free(
    void *data,
    void *context);
```

##### Discussion

for_each callback to call free on data item

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| while | while | while | while | while |

---

```swift
while(
    x->prev) x = x->prev;  while(
    x)
```

##### Discussion

start at first container

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| while( x) | while( x) | while( x) | while( x) | while( x) |

---

```swift
while(
    x->prev) x = x->prev;  while(
    x)
```

##### Discussion

start at first container

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| while( x) | while( x) | while( x) | while( x) | while( x) |

---

```swift
while(
    x->next) x = x->next;  while(
    x)
```

##### Discussion

start at last container

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| while( x) | while( x) | while( x) | while( x) | while( x) |

---

```swift
while(
    x->next) x = x->next;  while(
    x)
```

##### Discussion

start at last container

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| while(x -) | while(x -) | while(x -) | while(x -) | while(x -) |

---

```swift
while(
    x->next) x = x->next;  while(
    x->prev)
```

##### Discussion

start at last container

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
