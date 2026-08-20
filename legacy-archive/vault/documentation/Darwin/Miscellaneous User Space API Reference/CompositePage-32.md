---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/data_list/CompositePage.html
archived_at: '2026-07-15T07:23:26.397961Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| data_list.h | data_list.h | data_list.h | data_list.h | data_list.h |

|  |  |
| --- | --- |
| __Includes:__ | <net-snmp/library/snmp_impl.h>  [<net-snmp/library/tools.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/tools/index.html#//apple_ref/doc/header/tools.h) |

## Introduction

---

## Functions

**[netsnmp_add_list_data](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3omv2hg3tnobpwczdel5wgs43ul5sgc5db)**
:

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| netsnmp_add_list_data | netsnmp_add_list_data | netsnmp_add_list_data | netsnmp_add_list_data | netsnmp_add_list_data |

---

```
void netsnmp_add_list_data(
    netsnmp_data_list **head,
    netsnmp_data_list *node);
```

##### Discussion

depreciated: use netsnmp_data_list_add_node()

## Typedefs

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| netsnmp_data_list | netsnmp_data_list | netsnmp_data_list | netsnmp_data_list | netsnmp_data_list |

---

__See Also:__
> **[netsnmp_data_list_s](#apple-f4xwc4dqnrsv64tfmyxwgl3umrswml3omv2hg3tnobpwiylumfpwy2ltorpxg)**
> :

```swift
typedef struct netsnmp_data_list_s {
    struct netsnmp_data_list_s *next;
    char *name;
    /** The pointer to the data passed on. */
    void *data;
    /** must know how to free netsnmp_data_list->data */
    Netsnmp_Free_List_Data *free_func;
} netsnmp_data_list;
```

##### Discussion

used to iterate through lists of data

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| netsnmp_data_list_s | netsnmp_data_list_s | netsnmp_data_list_s | netsnmp_data_list_s | netsnmp_data_list_s |

---

__See Also:__
> **[netsnmp_data_list](#apple-f4xwc4dqnrsv64tfmyxwgl3umrswml3omv2hg3tnobpwiylumfpwy2ltoq)**
> :

```swift
typedef struct netsnmp_data_list_s {
    struct netsnmp_data_list_s *next;
    char *name;
    /** The pointer to the data passed on. */
    void *data;
    /** must know how to free netsnmp_data_list->data */
    Netsnmp_Free_List_Data *free_func;
} netsnmp_data_list;
```

##### Discussion

used to iterate through lists of data

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
