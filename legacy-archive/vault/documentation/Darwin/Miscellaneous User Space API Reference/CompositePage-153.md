---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/table_iterator/CompositePage.html
archived_at: '2026-07-15T07:23:28.765504Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| table_iterator.h | table_iterator.h | table_iterator.h | table_iterator.h | table_iterator.h |

## Introduction

@addtogroup table_iterator
@{

---

## Typedefs

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| netsnmp_iterator_info | netsnmp_iterator_info | netsnmp_iterator_info | netsnmp_iterator_info | netsnmp_iterator_info |

---

__See Also:__
> **[struct netsnmp_iterator_info_s netsnmp_iterator_info](#apple-f4xwc4dqnrsv64tfmyxwi33df52gs5dmmu5hizdfmyxxg5dsovrxi3tforzw43lql5uxizlsmf2g64s7nfxgm327onxgk5dtnzwxax3jorsxeylun5zf62lomzxq)**
> :

```
/** @struct netsnmp_iterator_info_s

Holds iterator information containing functions which should be
called by the iterator_handler to loop over your data set and
sort it in a SNMP specific manner.

The netsnmp_iterator_info typedef can be used instead of directly calling this struct if you would prefer.
    */
typedef struct netsnmp_iterator_info_s {
    /** Responsible for: returning the first set of "index" data, a
loop-context pointer, and optionally a data context
        */
    Netsnmp_First_Data_Point *get_first_data_point;
    /** Given the previous loop context, this should return the
next loop context, assiocated index set and optionally a
        */
    Netsnmp_Next_Data_Point *get_next_data_point;
    /** If a data context wasn't supplied by the
get_first_data_point or get_next_data_point functions and
the make_data_context pointer is defined, it will be called
        */
    Netsnmp_Make_Data_Context *make_data_context;
    /** A function which should free the loop context. This
function is called at *each* iteration step, which is
not-optimal for speed purposes. The use of
free_loop_context_at_end instead is strongly
        */
    Netsnmp_Free_Loop_Context *free_loop_context;
    /** Frees a data context. This will be called at any time a
data context needs to be freed. This may be at the same
time as a correspondng loop context is freed, or much much
later. Multiple data contexts may be kept in existence at
        */
    Netsnmp_Free_Data_Context *free_data_context;
    /** Frees a loop context at the end of the entire iteration
sequence. Generally, this would free the loop context
allocated by the get_first_data_point function (which would
then be updated by each call to the get_next_data_point
function). It is not called until the get_next_data_point
        */
    Netsnmp_Free_Loop_Context *free_loop_context_at_end;
    /** This can be used by client handlers to store any
        */
    void *myvoid;
    int flags;
    #define NETSNMP_ITERATOR_FLAG_SORTED 0x01  /** A pointer to the netsnmp_table_registration_info object
        */
    netsnmp_table_registration_info *table_reginfo;
} netsnmp_iterator_info;
```

##### Discussion

\* Typedefs the netsnmp_iterator_info_s struct into netsnmp_iterator_info

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| struct netsnmp_iterator_info_s netsnmp_iterator_info | struct netsnmp_iterator_info_s netsnmp_iterator_info | struct netsnmp_iterator_info_s netsnmp_iterator_info | struct netsnmp_iterator_info_s netsnmp_iterator_info | struct netsnmp_iterator_info_s netsnmp_iterator_info |

---

__See Also:__
> **[netsnmp_iterator_info](#apple-f4xwc4dqnrsv64tfmyxwgl3umrswml3omv2hg3tnobpws5dfojqxi33sl5uw4ztp)**
> :

```
/** @struct netsnmp_iterator_info_s

Holds iterator information containing functions which should be
called by the iterator_handler to loop over your data set and
sort it in a SNMP specific manner.

The netsnmp_iterator_info typedef can be used instead of directly calling this struct if you would prefer.
    */
typedef struct netsnmp_iterator_info_s {
    /** Responsible for: returning the first set of "index" data, a
loop-context pointer, and optionally a data context
        */
    Netsnmp_First_Data_Point *get_first_data_point;
    /** Given the previous loop context, this should return the
next loop context, assiocated index set and optionally a
        */
    Netsnmp_Next_Data_Point *get_next_data_point;
    /** If a data context wasn't supplied by the
get_first_data_point or get_next_data_point functions and
the make_data_context pointer is defined, it will be called
        */
    Netsnmp_Make_Data_Context *make_data_context;
    /** A function which should free the loop context. This
function is called at *each* iteration step, which is
not-optimal for speed purposes. The use of
free_loop_context_at_end instead is strongly
        */
    Netsnmp_Free_Loop_Context *free_loop_context;
    /** Frees a data context. This will be called at any time a
data context needs to be freed. This may be at the same
time as a correspondng loop context is freed, or much much
later. Multiple data contexts may be kept in existence at
        */
    Netsnmp_Free_Data_Context *free_data_context;
    /** Frees a loop context at the end of the entire iteration
sequence. Generally, this would free the loop context
allocated by the get_first_data_point function (which would
then be updated by each call to the get_next_data_point
function). It is not called until the get_next_data_point
        */
    Netsnmp_Free_Loop_Context *free_loop_context_at_end;
    /** This can be used by client handlers to store any
        */
    void *myvoid;
    int flags;
    #define NETSNMP_ITERATOR_FLAG_SORTED 0x01  /** A pointer to the netsnmp_table_registration_info object
        */
    netsnmp_table_registration_info *table_reginfo;
} netsnmp_iterator_info;
```

##### Discussion

\* Typedefs the netsnmp_iterator_info_s struct into netsnmp_iterator_info

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
