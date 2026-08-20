---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/kern_event/CompositePage.html
archived_at: '2026-07-15T07:23:26.962562Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| kern_event.h | kern_event.h | kern_event.h | kern_event.h | kern_event.h |

|  |  |
| --- | --- |
| __Includes:__ | <sys/appleapiopts.h>  <sys/ioccom.h>  <sys/sys_domain.h> |

## Introduction

This header defines in-kernel functions for generating kernel events as well
as functions for receiving kernel events using a kernel event socket.

---

## Structs and Unions

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| kern_event_msg | kern_event_msg | kern_event_msg | kern_event_msg | kern_event_msg |

---

```
struct kern_event_msg {
    u_long total_size; /* Size of entire event msg */
    u_long vendor_code; /* For non-Apple extensibility */
    u_long kev_class; /* Layer of event source */
    u_long kev_subclass; /* Component within layer */
    u_long id; /* Monotonically increasing value */
    u_long event_code; /* unique code */
    u_long event_data[1]; /* One or more data longwords */
};
```

##### Fields

> **`total_size`**
> : Total size of the kernel event message including the
> header.
>
> **`vendor_code`**
> : The vendor code indicates which vendor generated the
> kernel event. This gives every vendor a unique set of classes and
> subclasses to use. Use the SIOCGKEVVENDOR ioctl to look up vendor codes
> for vendors other than Apple. Apple uses KEV_VENDOR_APPLE.
>
> **`kev_class`**
> : The class of the kernel event.
>
> **`kev_subclass`**
> : The subclass of the kernel event.
>
> **`id`**
> : Monotonically increasing value.
>
> **`event_code`**
> : The event code.
>
> **`event_data`**
> : Any additional data about this event. Format will depend
> on the vendor_code, kev_class, kev_subclass, and event_code. The length
> of the event_data can be determined using total_size -
> KEV_MSG_HEADER_SIZE.

##### Discussion

This structure is prepended to all kernel events. This structure
is used to determine the format of the remainder of the kernel event.
This structure will appear on all messages received on a kernel event
socket. To post a kernel event, a slightly different structure is used.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| kev_request | kev_request | kev_request | kev_request | kev_request |

---

```
struct kev_request {
    u_long vendor_code;
    u_long kev_class;
    u_long kev_subclass;
};
```

##### Fields

> **`total_size`**
> : Total size of the kernel event message including the
> header.
>
> **`vendor_code`**
> : All kernel events that don't match this vendor code will
> be ignored. KEV_ANY_VENDOR can be used to receive kernel events with any
> vendor code.
>
> **`kev_class`**
> : All kernel events that don't match this class will be
> ignored. KEV_ANY_CLASS can be used to receive kernel events with any
> class.
>
> **`kev_subclass`**
> : All kernel events that don't match this subclass will be
> ignored. KEV_ANY_SUBCLASS can be used to receive kernel events with any
> subclass.

##### Discussion

This structure is used with the SIOCSKEVFILT and SIOCGKEVFILT to
set and get the control filter setting for a kernel control socket.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| kev_vendor_code | kev_vendor_code | kev_vendor_code | kev_vendor_code | kev_vendor_code |

---

```
struct kev_vendor_code {
    u_long vendor_code;
    char vendor_string[200  ];
};
```

##### Fields

> **`vendor_code`**
> : After making the SIOCGKEVVENDOR ioctl call, this will
> be filled in with the vendor code if there is one.
>
> **`vendor_string`**
> : A bundle style identifier.

##### Discussion

This structure is used with the SIOCGKEVVENDOR ioctl to convert
from a string identifying a kext or vendor, in the form of a bundle
identifier, to a vendor code.

## #defines

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| KEV_APPLESHARE_CLASS | KEV_APPLESHARE_CLASS | KEV_APPLESHARE_CLASS | KEV_APPLESHARE_CLASS | KEV_APPLESHARE_CLASS |

---

```
#define KEV_APPLESHARE_CLASS 4
```

##### Discussion

AppleShare kernel event class.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| KEV_IOKIT_CLASS | KEV_IOKIT_CLASS | KEV_IOKIT_CLASS | KEV_IOKIT_CLASS | KEV_IOKIT_CLASS |

---

```
#define KEV_IOKIT_CLASS 2
```

##### Discussion

IOKit kernel event class.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| KEV_IOKIT_CLASS | KEV_IOKIT_CLASS | KEV_IOKIT_CLASS | KEV_IOKIT_CLASS | KEV_IOKIT_CLASS |

---

__See Also:__
> **[KEV_SYSTEM_CLASS](#apple-f4xwc4dqnrsv64tfmyxwgl3nmfrxe3zpjncvmx2tlfjvirknl5buyqktkm)**
> :

```
#define KEV_SYSTEM_CLASS 3
```

##### Discussion

System kernel event class.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| KEV_MSG_HEADER_SIZE | KEV_MSG_HEADER_SIZE | KEV_MSG_HEADER_SIZE | KEV_MSG_HEADER_SIZE | KEV_MSG_HEADER_SIZE |

---

```
#define KEV_MSG_HEADER_SIZE
```

##### Discussion

Size of the header portion of the kern_event_msg structure. This
accounts for everything right up to event_data. The size of the data can
be found by subtracting KEV_MSG_HEADER_SIZE from the total size from the
kern_event_msg.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| KEV_NETWORK_CLASS | KEV_NETWORK_CLASS | KEV_NETWORK_CLASS | KEV_NETWORK_CLASS | KEV_NETWORK_CLASS |

---

```
#define KEV_NETWORK_CLASS 1
```

##### Discussion

Network kernel event class.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| KEV_SYSTEM_CLASS | KEV_SYSTEM_CLASS | KEV_SYSTEM_CLASS | KEV_SYSTEM_CLASS | KEV_SYSTEM_CLASS |

---

__See Also:__
> **[KEV_IOKIT_CLASS](#apple-f4xwc4dqnrsv64tfmyxwi33df52gs5dmmu5g2yldojxs6s2fkzpust2ljfkf6q2mifjvg)**
> :

```
#define KEV_SYSTEM_CLASS 3
```

##### Discussion

System kernel event class.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| KEV_VENDOR_APPLE | KEV_VENDOR_APPLE | KEV_VENDOR_APPLE | KEV_VENDOR_APPLE | KEV_VENDOR_APPLE |

---

```
#define KEV_VENDOR_APPLE 1
```

##### Discussion

Apple generated kernel events use the hard coded vendor code
value of 1. Third party kernel events use a dynamically allocated vendor
code. The vendor code can be found using the SIOCGKEVVENDOR ioctl.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| KEV_VENDOR_CODE_MAX_STR_LEN | KEV_VENDOR_CODE_MAX_STR_LEN | KEV_VENDOR_CODE_MAX_STR_LEN | KEV_VENDOR_CODE_MAX_STR_LEN | KEV_VENDOR_CODE_MAX_STR_LEN |

---

```
#define KEV_VENDOR_CODE_MAX_STR_LEN 200
```

##### Discussion

This define sets the maximum length of a string that can be used
to identify a vendor or kext when looking up a vendor code.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| SIOCGKEVFILT | SIOCGKEVFILT | SIOCGKEVFILT | SIOCGKEVFILT | SIOCGKEVFILT |

---

```
#define SIOCGKEVFILT _IOR(
    'e', 3, struct kev_request)
```

##### Discussion

Retrieve the kernel event filter for this socket. Kernel events
not matching this filter will not be received on this socket.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| SIOCGKEVID | SIOCGKEVID | SIOCGKEVID | SIOCGKEVID | SIOCGKEVID |

---

```
#define SIOCGKEVID _IOR(
    'e', 1, u_long)
```

##### Discussion

Retrieve the current event id. Each event generated will have
a new idea. The next event to be generated will have an id of id+1.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| SIOCGKEVVENDOR | SIOCGKEVVENDOR | SIOCGKEVVENDOR | SIOCGKEVVENDOR | SIOCGKEVVENDOR |

---

```
#define SIOCGKEVVENDOR _IOWR(
    'e', 4, struct kev_vendor_code)
```

##### Discussion

Lookup the vendor code for the specified vendor. ENOENT will be
returned if a vendor code for that vendor string does not exist.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| SIOCSKEVFILT | SIOCSKEVFILT | SIOCSKEVFILT | SIOCSKEVFILT | SIOCSKEVFILT |

---

```
#define SIOCSKEVFILT _IOW(
    'e', 2, struct kev_request)
```

##### Discussion

Set the kernel event filter for this socket. Kernel events not
matching this filter will not be received on this socket.

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
