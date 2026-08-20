---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/baby_steps/CompositePage.html
archived_at: '2026-07-15T07:23:25.327631Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| baby_steps.h | baby_steps.h | baby_steps.h | baby_steps.h | baby_steps.h |

|  |  |
| --- | --- |
| __Includes:__ | [<net-snmp/agent/agent_handler.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/agent_handler/index.html#//apple_ref/doc/header/agent_handler.h) |

## Introduction

---

## Typedefs

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| netsnmp_baby_steps_access_methods | netsnmp_baby_steps_access_methods | netsnmp_baby_steps_access_methods | netsnmp_baby_steps_access_methods | netsnmp_baby_steps_access_methods |

---

```
/** @name access_multiplexer

This helper calls individual access methods based on the mode. All
access methods share the same handler, and the same myvoid pointer.
If you need individual myvoid pointers, check out the multiplexer
handler (though it currently only works for traditional modes).

    */
/** @struct netsnmp_mib_handler_access_methods
Defines the access methods to be called by the access_multiplexer helper
    */
typedef struct netsnmp_baby_steps_access_methods_s {
    /*
 * baby step modes
        */
    Netsnmp_Node_Handler *pre_request;
    Netsnmp_Node_Handler *object_lookup;
    Netsnmp_Node_Handler *get_values;
    Netsnmp_Node_Handler *object_syntax_checks;
    Netsnmp_Node_Handler *row_creation;
    Netsnmp_Node_Handler *undo_setup;
    Netsnmp_Node_Handler *set_values;
    Netsnmp_Node_Handler *consistency_checks;
    Netsnmp_Node_Handler *commit;
    Netsnmp_Node_Handler *undo_sets;
    Netsnmp_Node_Handler *undo_cleanup;
    Netsnmp_Node_Handler *undo_commit;
    Netsnmp_Node_Handler *irreversible_commit;
    Netsnmp_Node_Handler *post_request;
    void *my_access_void;
} netsnmp_baby_steps_access_methods;
```

##### Discussion

@}

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| netsnmp_baby_steps_modes | netsnmp_baby_steps_modes | netsnmp_baby_steps_modes | netsnmp_baby_steps_modes | netsnmp_baby_steps_modes |

---

```
typedef struct netsnmp_baby_steps_modes_s {
    u_int registered;
    u_int completed;
} netsnmp_baby_steps_modes;
```

##### Discussion

@name baby_steps

This helper expands the original net-snmp set modes into the newer, finer
grained modes.

\* @{

## #defines

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| netsnmp_get_baby_steps_handler | netsnmp_get_baby_steps_handler | netsnmp_get_baby_steps_handler | netsnmp_get_baby_steps_handler | netsnmp_get_baby_steps_handler |

---

```
/** backwards compatability. don't use in new code */
#define netsnmp_get_baby_steps_handler netsnmp_baby_steps_handler_get
```

##### Discussion

@}

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
