---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/agent_handler/CompositePage.html
archived_at: '2026-07-15T07:23:25.258621Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| agent_handler.h | agent_handler.h | agent_handler.h | agent_handler.h | agent_handler.h |

## Introduction

@addtogroup handler

@{

---

## Typedefs

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| netsnmp_handler_registration | netsnmp_handler_registration | netsnmp_handler_registration | netsnmp_handler_registration | netsnmp_handler_registration |

---

__See Also:__
> **[struct netsnmp_handler_registration_s netsnmp_handler_registration](#apple-f4xwc4dqnrsv64tfmyxwi33df52gs5dmmu5hizdfmyxxg5dsovrxi3tforzw43lql5ugc3tenrsxex3smvtws43uojqxi2lpnzpxg3tforzw43lql5ugc3tenrsxex3smvtws43uojqxi2lpny)**
> :

```
/** @struct netsnmp_handler_registration_s
Root registration info.
The variables handlerName, contextName, and rootoid need to be allocated
on the heap, when the registration structure is unregistered using
unregister_mib_context() the code attempts to free them.
    */
typedef struct netsnmp_handler_registration_s {
    /** for mrTable listings, and other uses */
    char *handlerName;
    /** NULL = default context */
    char *contextName;
    /**
where are we registered at?
        */
    oid *rootoid;
    size_t rootoid_len;
    /**
handler details
        */
    netsnmp_mib_handler *handler;
    int modes;
    /**
more optional stuff
        */
    int priority;
    int range_subid;
    oid range_ubound;
    int timeout;
    int global_cacheid;
    /**
void ptr for registeree
        */
    void *my_reg_void;
} netsnmp_handler_registration;
```

##### Discussion

\* Typedefs the netsnmp_handler_registration_s struct into netsnmp_handler_registration

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| netsnmp_mib_handler | netsnmp_mib_handler | netsnmp_mib_handler | netsnmp_mib_handler | netsnmp_mib_handler |

---

__See Also:__
> **[struct netsnmp_mib_handler_s netsnmp_mib_handler](#apple-f4xwc4dqnrsv64tfmyxwi33df52gs5dmmu5hizdfmyxxg5dsovrxi3tforzw43lql5wwsys7nbqw4zdmmvzf643omv2hg3tnobpw22lcl5ugc3tenrsxe)**
> :

```
/** @struct netsnmp_mib_handler_s
the mib handler structure to be registered
    */
typedef struct netsnmp_mib_handler_s {
    char *handler_name;
    /** for handler's internal use */
    void *myvoid;
    /** for agent_handler's internal use */
    int flags;
    /** if you add more members, you probably also want to update
        */
    /** _clone_handler in snmp_agent.c. */
    int (*access_method) (
        struct netsnmp_mib_handler_s *,
        struct netsnmp_handler_registration_s *,
        struct netsnmp_agent_request_info_s *,
        struct netsnmp_request_info_s *);
    struct netsnmp_mib_handler_s *next;
    struct netsnmp_mib_handler_s *prev;
} netsnmp_mib_handler;
```

##### Discussion

\* Typedefs the netsnmp_mib_handler_s struct into netsnmp_mib_handler

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| struct netsnmp_handler_registration_s netsnmp_handler_registration | struct netsnmp_handler_registration_s netsnmp_handler_registration | struct netsnmp_handler_registration_s netsnmp_handler_registration | struct netsnmp_handler_registration_s netsnmp_handler_registration | struct netsnmp_handler_registration_s netsnmp_handler_registration |

---

__See Also:__
> **[netsnmp_handler_registration](#apple-f4xwc4dqnrsv64tfmyxwgl3umrswml3omv2hg3tnobpwqylomrwgk4s7ojswo2ltorzgc5djn5xa)**
> :

```
/** @struct netsnmp_handler_registration_s
Root registration info.
The variables handlerName, contextName, and rootoid need to be allocated
on the heap, when the registration structure is unregistered using
unregister_mib_context() the code attempts to free them.
    */
typedef struct netsnmp_handler_registration_s {
    /** for mrTable listings, and other uses */
    char *handlerName;
    /** NULL = default context */
    char *contextName;
    /**
where are we registered at?
        */
    oid *rootoid;
    size_t rootoid_len;
    /**
handler details
        */
    netsnmp_mib_handler *handler;
    int modes;
    /**
more optional stuff
        */
    int priority;
    int range_subid;
    oid range_ubound;
    int timeout;
    int global_cacheid;
    /**
void ptr for registeree
        */
    void *my_reg_void;
} netsnmp_handler_registration;
```

##### Discussion

\* Typedefs the netsnmp_handler_registration_s struct into netsnmp_handler_registration

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| struct netsnmp_mib_handler_s netsnmp_mib_handler | struct netsnmp_mib_handler_s netsnmp_mib_handler | struct netsnmp_mib_handler_s netsnmp_mib_handler | struct netsnmp_mib_handler_s netsnmp_mib_handler | struct netsnmp_mib_handler_s netsnmp_mib_handler |

---

__See Also:__
> **[netsnmp_mib_handler](#apple-f4xwc4dqnrsv64tfmyxwgl3umrswml3omv2hg3tnobpw22lcl5ugc3tenrsxe)**
> :

```
/** @struct netsnmp_mib_handler_s
the mib handler structure to be registered
    */
typedef struct netsnmp_mib_handler_s {
    char *handler_name;
    /** for handler's internal use */
    void *myvoid;
    /** for agent_handler's internal use */
    int flags;
    /** if you add more members, you probably also want to update
        */
    /** _clone_handler in snmp_agent.c. */
    int (*access_method) (
        struct netsnmp_mib_handler_s *,
        struct netsnmp_handler_registration_s *,
        struct netsnmp_agent_request_info_s *,
        struct netsnmp_request_info_s *);
    struct netsnmp_mib_handler_s *next;
    struct netsnmp_mib_handler_s *prev;
} netsnmp_mib_handler;
```

##### Discussion

\* Typedefs the netsnmp_mib_handler_s struct into netsnmp_mib_handler

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
