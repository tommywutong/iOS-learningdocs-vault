---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/table/CompositePage.html
archived_at: '2026-07-15T07:23:28.713080Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| table.h | table.h | table.h | table.h | table.h |

|  |  |
| --- | --- |
| __Includes:__ | <architecture/i386/desc.h>  <architecture/i386/tss.h> |

## Introduction

---

## Typedefs

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| netsnmp_column_info | netsnmp_column_info | netsnmp_column_info | netsnmp_column_info | netsnmp_column_info |

---

__See Also:__
> **[struct netsnmp_column_info_t netsnmp_column_info](#apple-f4xwc4dqnrsv64tfmyxwi33df52gs5dmmu5hizdfmyxxg5dsovrxi3tforzw43lql5rw63dvnvxf62lomzxv65domv2hg3tnobpwg33movww4x3jnztg6)**
> :

```
/**
@struct netsnmp_column_info_t
column info struct. OVERLAPPING RANGES ARE NOT SUPPORTED.
    */
typedef struct netsnmp_column_info_t {
    char isRange;
    /** only useful if isRange == 0 */
    char list_count;
    union {
        unsigned int range[2];
        unsigned int *list;
        } details;
    struct netsnmp_column_info_t *next;
} netsnmp_column_info;
```

##### Discussion

\* Typedefs the netsnmp_column_info_t struct into netsnmp_column_info

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| netsnmp_table_registration_info | netsnmp_table_registration_info | netsnmp_table_registration_info | netsnmp_table_registration_info | netsnmp_table_registration_info |

---

__See Also:__
> **[struct netsnmp_table_registration_info_s netsnmp_table_registration_info](#apple-f4xwc4dqnrsv64tfmyxwi33df52gs5dmmu5hizdfmyxxg5dsovrxi3tforzw43lql52gcytmmvpxezlhnfzxi4tboruw63s7nfxgm327onxgk5dtnzwxax3umfrgyzk7ojswo2ltorzgc5djn5xf62lomzxq)**
> :

```
/**
@struct netsnmp_table_registration_info_s
Table registration structure.
    */
typedef struct netsnmp_table_registration_info_s {
    /** list of varbinds with only 'type' set */
    netsnmp_variable_list *indexes;
    /** calculated automatically */
    unsigned int number_indexes;
    /**
the minimum columns number. If there are columns
in-between which are not valid, use valid_columns to get
automatic column range checking.
        */
    unsigned int min_column;
    /** the maximum columns number */
    unsigned int max_column;
    /** more details on columns */
    netsnmp_column_info *valid_columns;
} netsnmp_table_registration_info;
```

##### Discussion

Typedefs the netsnmp_table_registration_info_s struct into
\* netsnmp_table_registration_info

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| netsnmp_table_request_info | netsnmp_table_request_info | netsnmp_table_request_info | netsnmp_table_request_info | netsnmp_table_request_info |

---

__See Also:__
> **[struct netsnmp_table_request_info_s netsnmp_table_request_info](#apple-f4xwc4dqnrsv64tfmyxwi33df52gs5dmmu5hizdfmyxxg5dsovrxi3tforzw43lql52gcytmmvpxezlrovsxg5c7nfxgm327onxgk5dtnzwxax3umfrgyzk7ojsxc5lfon2f62lomzxq)**
> :

```
/**
@struct netsnmp_table_request_info_s
The table request info structure.
    */
typedef struct netsnmp_table_request_info_s {
    /** 0 if OID not long enough */
    unsigned int colnum;
    /** 0 if failure to parse any */
    unsigned int number_indexes;
    /** contents freed by helper upon exit */
    netsnmp_variable_list *indexes;
    oid index_oid[MAX_OID_LEN];
    size_t index_oid_len;
    netsnmp_table_registration_info *reg_info;
} netsnmp_table_request_info;
```

##### Discussion

Typedefs the netsnmp_table_request_info_s struct into
\* netsnmp_table_request_info

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| struct netsnmp_column_info_t netsnmp_column_info | struct netsnmp_column_info_t netsnmp_column_info | struct netsnmp_column_info_t netsnmp_column_info | struct netsnmp_column_info_t netsnmp_column_info | struct netsnmp_column_info_t netsnmp_column_info |

---

__See Also:__
> **[netsnmp_column_info](#apple-f4xwc4dqnrsv64tfmyxwgl3umrswml3omv2hg3tnobpwg33movww4x3jnztg6)**
> :

```
/**
@struct netsnmp_column_info_t
column info struct. OVERLAPPING RANGES ARE NOT SUPPORTED.
    */
typedef struct netsnmp_column_info_t {
    char isRange;
    /** only useful if isRange == 0 */
    char list_count;
    union {
        unsigned int range[2];
        unsigned int *list;
        } details;
    struct netsnmp_column_info_t *next;
} netsnmp_column_info;
```

##### Discussion

\* Typedefs the netsnmp_column_info_t struct into netsnmp_column_info

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| struct netsnmp_table_registration_info_s netsnmp_table_registration_info | struct netsnmp_table_registration_info_s netsnmp_table_registration_info | struct netsnmp_table_registration_info_s netsnmp_table_registration_info | struct netsnmp_table_registration_info_s netsnmp_table_registration_info | struct netsnmp_table_registration_info_s netsnmp_table_registration_info |

---

__See Also:__
> **[netsnmp_table_registration_info](#apple-f4xwc4dqnrsv64tfmyxwgl3umrswml3omv2hg3tnobpxiylcnrsv64tfm5uxg5dsmf2gs33ol5uw4ztp)**
> :

```
/**
@struct netsnmp_table_registration_info_s
Table registration structure.
    */
typedef struct netsnmp_table_registration_info_s {
    /** list of varbinds with only 'type' set */
    netsnmp_variable_list *indexes;
    /** calculated automatically */
    unsigned int number_indexes;
    /**
the minimum columns number. If there are columns
in-between which are not valid, use valid_columns to get
automatic column range checking.
        */
    unsigned int min_column;
    /** the maximum columns number */
    unsigned int max_column;
    /** more details on columns */
    netsnmp_column_info *valid_columns;
} netsnmp_table_registration_info;
```

##### Discussion

Typedefs the netsnmp_table_registration_info_s struct into
\* netsnmp_table_registration_info

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| struct netsnmp_table_request_info_s netsnmp_table_request_info | struct netsnmp_table_request_info_s netsnmp_table_request_info | struct netsnmp_table_request_info_s netsnmp_table_request_info | struct netsnmp_table_request_info_s netsnmp_table_request_info | struct netsnmp_table_request_info_s netsnmp_table_request_info |

---

__See Also:__
> **[netsnmp_table_request_info](#apple-f4xwc4dqnrsv64tfmyxwgl3umrswml3omv2hg3tnobpxiylcnrsv64tfof2wk43ul5uw4ztp)**
> :

```
/**
@struct netsnmp_table_request_info_s
The table request info structure.
    */
typedef struct netsnmp_table_request_info_s {
    /** 0 if OID not long enough */
    unsigned int colnum;
    /** 0 if failure to parse any */
    unsigned int number_indexes;
    /** contents freed by helper upon exit */
    netsnmp_variable_list *indexes;
    oid index_oid[MAX_OID_LEN];
    size_t index_oid_len;
    netsnmp_table_registration_info *reg_info;
} netsnmp_table_request_info;
```

##### Discussion

Typedefs the netsnmp_table_request_info_s struct into
\* netsnmp_table_request_info

## #defines

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TABLE_HANDLER_NAME | TABLE_HANDLER_NAME | TABLE_HANDLER_NAME | TABLE_HANDLER_NAME | TABLE_HANDLER_NAME |

---

```
/**
Notes:

1) illegal indexes automatically get handled for get/set cases.
Simply check to make sure the value is type ASN_NULL before
you answer a request.
    */
/**
used as an index to parent_data lookups
    */
#define TABLE_HANDLER_NAME "table"
```

##### Discussion

The table helper is designed to simplify the task of writing a
table handler for the net-snmp agent. You should create a normal
handler and register it using the netsnmp_register_table() function
instead of the netsnmp_register_handler() function.

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
