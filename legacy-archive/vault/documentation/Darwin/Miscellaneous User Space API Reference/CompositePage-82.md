---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/kern_control/CompositePage.html
archived_at: '2026-07-15T07:23:26.945387Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| kern_control.h | kern_control.h | kern_control.h | kern_control.h | kern_control.h |

|  |  |
| --- | --- |
| __Includes:__ | <sys/appleapiopts.h> |

## Introduction

This header defines an API to communicate between a kernel
extension and a process outside of the kernel.

---

## Structs and Unions

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ctl_event_data | ctl_event_data | ctl_event_data | ctl_event_data | ctl_event_data |

---

```
struct ctl_event_data {
    u_int32_t ctl_id; /* Kernel Controller ID */
    u_int32_t ctl_unit;
};
```

##### Fields

> **`ctl_id`**
> : The kernel control id.
>
> **`ctl_unit`**
> : The kernel control unit.

##### Discussion

This structure is used for KEV_CTL_SUBCLASS kernel
events.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ctl_info | ctl_info | ctl_info | ctl_info | ctl_info |

---

```
struct ctl_info {
    u_int32_t ctl_id; /* Kernel Controller ID */
    char ctl_name[96  ]; /* Kernel Controller Name (a C string) */
};
```

##### Fields

> **`ctl_id`**
> : The kernel control id, filled out upon return.
>
> **`ctl_name`**
> : The kernel control name to find.

##### Discussion

This structure is used with the CTLIOCGINFO ioctl to
translate from a kernel control name to a control id.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sockaddr_ctl | sockaddr_ctl | sockaddr_ctl | sockaddr_ctl | sockaddr_ctl |

---

```
struct sockaddr_ctl {
    u_char sc_len; /* depends on size of bundle ID string */
    u_char sc_family; /* AF_SYSTEM */
    u_int16_t ss_sysaddr; /* AF_SYS_KERNCONTROL */
    u_int32_t sc_id; /* Controller unique identifier */
    u_int32_t sc_unit; /* Developer private unit number */
    u_int32_t sc_reserved[5];
};
```

##### Fields

> **`sc_len`**
> : The length of the structure.
>
> **`sc_family`**
> : AF_SYSTEM.
>
> **`ss_sysaddr`**
> : AF_SYS_KERNCONTROL.
>
> **`sc_id`**
> : Controller unique identifier.
>
> **`sc_unit`**
> : Kernel controller private unit number.
>
> **`sc_reserved`**
> : Reserved, must be set to zero.

##### Discussion

The controller address structure is used to establish
contact between a user client and a kernel controller. The
sc_id/sc_unit uniquely identify each controller. sc_id is a
unique identifier assigned to the controller. The identifier can
be assigned by the system at registration time or be a 32-bit
creator code obtained from Apple Computer. sc_unit is a unit
number for this sc_id, and is privately used by the kernel
controller to identify several instances of the controller.

## #defines

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CTLIOCGCOUNT | CTLIOCGCOUNT | CTLIOCGCOUNT | CTLIOCGCOUNT | CTLIOCGCOUNT |

---

```
#define CTLIOCGCOUNT _IOR(
    'N', 2, int) /* get number of control structures registered */
```

##### Discussion

The CTLIOCGCOUNT ioctl can be used to determine the
number of kernel controllers registered.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CTLIOCGINFO | CTLIOCGINFO | CTLIOCGINFO | CTLIOCGINFO | CTLIOCGINFO |

---

```
#define CTLIOCGINFO _IOWR(
    'N', 3, struct ctl_info) /* get id from name */
```

##### Discussion

The CTLIOCGINFO ioctl can be used to convert a kernel
control name to a kernel control id.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| KEV_CTL_DEREGISTERED | KEV_CTL_DEREGISTERED | KEV_CTL_DEREGISTERED | KEV_CTL_DEREGISTERED | KEV_CTL_DEREGISTERED |

---

```
#define KEV_CTL_DEREGISTERED 2 /* a controller disappears */
```

##### Discussion

The event code indicating a controller was unregistered.
The data portion will contain a ctl_event_data.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| KEV_CTL_REGISTERED | KEV_CTL_REGISTERED | KEV_CTL_REGISTERED | KEV_CTL_REGISTERED | KEV_CTL_REGISTERED |

---

```
#define KEV_CTL_REGISTERED 1 /* a new controller appears */
```

##### Discussion

The event code indicating a new controller was
registered. The data portion will contain a ctl_event_data.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| KEV_CTL_SUBCLASS | KEV_CTL_SUBCLASS | KEV_CTL_SUBCLASS | KEV_CTL_SUBCLASS | KEV_CTL_SUBCLASS |

---

```
#define KEV_CTL_SUBCLASS 2
```

##### Discussion

The kernel event subclass for kernel control events.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| MAX_KCTL_NAME | MAX_KCTL_NAME | MAX_KCTL_NAME | MAX_KCTL_NAME | MAX_KCTL_NAME |

---

```
#define MAX_KCTL_NAME 96
```

##### Discussion

Kernel control names must be no longer than
MAX_KCTL_NAME.

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
