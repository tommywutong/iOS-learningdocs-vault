---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/snmp_agent/CompositePage.html
archived_at: '2026-07-15T07:23:27.887691Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| snmp_agent.h | snmp_agent.h | snmp_agent.h | snmp_agent.h | snmp_agent.h |

|  |  |
| --- | --- |
| __Includes:__ | <net-snmp/library/snmp_impl.h>  [<net-snmp/library/tools.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/tools/index.html#//apple_ref/doc/header/tools.h)  [<net-snmp/library/data_list.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/data_list/index.html#//apple_ref/doc/header/data_list.h) |

## Introduction

---

## Functions

**[netsnmp_set_mode_request_error](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3omv2hg3tnobpxgzlul5ww6zdfl5zgk4lvmvzxix3fojzg64q)**
:

**[netsnmp_set_request_error](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3omv2hg3tnobpxgzlul5zgk4lvmvzxix3fojzg64q)**
:

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| netsnmp_set_mode_request_error | netsnmp_set_mode_request_error | netsnmp_set_mode_request_error | netsnmp_set_mode_request_error | netsnmp_set_mode_request_error |

---

```
int netsnmp_set_mode_request_error(
    int mode,
    netsnmp_request_info *request,
    int error_value);
```

##### Discussion

deprecated, use netsnmp_request_set_error instead

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| netsnmp_set_request_error | netsnmp_set_request_error | netsnmp_set_request_error | netsnmp_set_request_error | netsnmp_set_request_error |

---

```
int netsnmp_set_request_error(
    netsnmp_agent_request_info *reqinfo,
    netsnmp_request_info *request,
    int error_value);
```

##### Discussion

deprecated, use netsnmp_request_set_error instead

## Typedefs

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| netsnmp_agent_request_info | netsnmp_agent_request_info | netsnmp_agent_request_info | netsnmp_agent_request_info | netsnmp_agent_request_info |

---

__See Also:__
> **[struct netsnmp_agent_request_info_s netsnmp_agent_request_info](#apple-f4xwc4dqnrsv64tfmyxwi33df52gs5dmmu5hizdfmyxxg5dsovrxi3tforzw43lql5qwozloorpxezlrovsxg5c7nfxgm327onxgk5dtnzwxax3bm5sw45c7ojsxc5lfon2f62lomzxq)**
> :

```
/** @struct netsnmp_agent_request_info_s
The agent transaction request structure
    */
typedef struct netsnmp_agent_request_info_s {
    int mode;
    /** pdu contains authinfo, eg */
    /* netsnmp_pdu *pdu; */
    struct netsnmp_agent_session_s *asp; /* may not be needed */
    /*
 * can be used to pass information on a per-pdu basis from a
 * helper to the later handlers
        */
    netsnmp_data_list *agent_data;
} netsnmp_agent_request_info;
```

##### Discussion

Typedefs the netsnmp_agent_request_info_s struct into
netsnmp_agent_request_info

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| netsnmp_request_info | netsnmp_request_info | netsnmp_request_info | netsnmp_request_info | netsnmp_request_info |

---

__See Also:__
> **[struct netsnmp_request_info_s netsnmp_request_info](#apple-f4xwc4dqnrsv64tfmyxwi33df52gs5dmmu5hizdfmyxxg5dsovrxi3tforzw43lql5zgk4lvmvzxix3jnztg6x3tnzsxi43onvyf64tfof2wk43ul5uw4ztp)**
> :

```swift
/** @struct netsnmp_request_info_s
The netsnmp request info structure.
    */
typedef struct netsnmp_request_info_s {
    /**
variable bindings
        */
    netsnmp_variable_list *requestvb;
    /**
can be used to pass information on a per-request basis from a
helper to the later handlers
        */
    netsnmp_data_list *parent_data;
    /*
 * pointer to the agent_request_info for this request
        */
    struct netsnmp_agent_request_info_s *agent_req_info;
    /** don't free, reference to (struct tree)->end */
    oid *range_end;
    size_t range_end_len;
    /*
 * flags
        */
    int delegated;
    int processed;
    int inclusive;
    int status;
    /** index in original pdu */
    int index;
    /** get-bulk */
    int repeat;
    int orig_repeat;
    netsnmp_variable_list *requestvb_start;
    /* internal use */
    struct netsnmp_request_info_s *next;
    struct netsnmp_request_info_s *prev;
    struct netsnmp_subtree_s *subtree;
} netsnmp_request_info;
```

##### Discussion

Typedefs the netsnmp_request_info_s struct into
\* netsnmp_request_info

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| struct netsnmp_agent_request_info_s netsnmp_agent_request_info | struct netsnmp_agent_request_info_s netsnmp_agent_request_info | struct netsnmp_agent_request_info_s netsnmp_agent_request_info | struct netsnmp_agent_request_info_s netsnmp_agent_request_info | struct netsnmp_agent_request_info_s netsnmp_agent_request_info |

---

__See Also:__
> **[netsnmp_agent_request_info](#apple-f4xwc4dqnrsv64tfmyxwgl3umrswml3omv2hg3tnobpwcz3fnz2f64tfof2wk43ul5uw4ztp)**
> :

```
/** @struct netsnmp_agent_request_info_s
The agent transaction request structure
    */
typedef struct netsnmp_agent_request_info_s {
    int mode;
    /** pdu contains authinfo, eg */
    /* netsnmp_pdu *pdu; */
    struct netsnmp_agent_session_s *asp; /* may not be needed */
    /*
 * can be used to pass information on a per-pdu basis from a
 * helper to the later handlers
        */
    netsnmp_data_list *agent_data;
} netsnmp_agent_request_info;
```

##### Discussion

Typedefs the netsnmp_agent_request_info_s struct into
netsnmp_agent_request_info

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| struct netsnmp_request_info_s netsnmp_request_info | struct netsnmp_request_info_s netsnmp_request_info | struct netsnmp_request_info_s netsnmp_request_info | struct netsnmp_request_info_s netsnmp_request_info | struct netsnmp_request_info_s netsnmp_request_info |

---

__See Also:__
> **[netsnmp_request_info](#apple-f4xwc4dqnrsv64tfmyxwgl3umrswml3omv2hg3tnobpxezlrovsxg5c7nfxgm3y)**
> :

```swift
/** @struct netsnmp_request_info_s
The netsnmp request info structure.
    */
typedef struct netsnmp_request_info_s {
    /**
variable bindings
        */
    netsnmp_variable_list *requestvb;
    /**
can be used to pass information on a per-request basis from a
helper to the later handlers
        */
    netsnmp_data_list *parent_data;
    /*
 * pointer to the agent_request_info for this request
        */
    struct netsnmp_agent_request_info_s *agent_req_info;
    /** don't free, reference to (struct tree)->end */
    oid *range_end;
    size_t range_end_len;
    /*
 * flags
        */
    int delegated;
    int processed;
    int inclusive;
    int status;
    /** index in original pdu */
    int index;
    /** get-bulk */
    int repeat;
    int orig_repeat;
    netsnmp_variable_list *requestvb_start;
    /* internal use */
    struct netsnmp_request_info_s *next;
    struct netsnmp_request_info_s *prev;
    struct netsnmp_subtree_s *subtree;
} netsnmp_request_info;
```

##### Discussion

Typedefs the netsnmp_request_info_s struct into
\* netsnmp_request_info

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
