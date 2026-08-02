---
title: Retain Counts of io_object_t Objects in IOKit.framework
apple_id: DTS10001723
resource_type: QA
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: IOKit
published: '2008-09-24'
source_url: https://developer.apple.com/library/archive/qa/qa1195/_index.html
archived_at: '2026-07-18T02:30:12.311732Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1195

# Retain Counts of io_object_t Objects in IOKit.framework

## Q:  I think I'm leaking `io_object_t` objects in my user space I/O Kit code. I used the function `IOObjectGetRetainCount` to find the retain count of those objects, but the values I get back are larger than I expected. Why is this?

A: I think I'm leaking `io_object_t` objects in my user space I/O Kit code. I used the function `IOObjectGetRetainCount` to find the retain count of those objects, but the values I get back are larger than I expected. Why is this?

There are actually two separate retain counts involved here. The first is the retain count of the underlying kernel object represented by the `io_object_t`. The function `IOObjectGetRetainCount` returns this retain count by calling through to the kernel.

The second is the retain count of the `io_object_t` itself. An `io_object_t` is a wrapper around a Mach port used to communicate between user space and the kernel, and Mach ports have their own retain count. This also applies to the other types derived from `io_object_t`: `io_service_t, io_connect_t, io_iterator_t, io_registry_entry_t,` and `io_enumerator_t`. (These types are defined in `IOKit/IOTypes.h`.)

`IOObjectRetain` and `IOObjectRelease` operate on the retain count of the `io_object_t`  Mach port itself. This can be verified by looking at `IOKitLib.c`  in the IOKitUser project in [Darwin](http://www.opensource.apple.com/darwinsource/).

So, the correct way to get the retain count of an `io_object_t` is to use the Mach function `mach_port_get_refs` as shown in the snippet in Listing 1.

__Listing 1__  Getting the retain count of an io_object_t.

```c
#include <IOKit/IOKitLib.h> #include <mach/mach_port.h>  kern_return_t   kr; unsigned int    result; io_object_t     theObject; io_name_t       className;  kr = IOObjectGetClass(theObject, className);  if (KERN_SUCCESS == kr) {     kern_return_t  kr2;      kr2 = mach_port_get_refs(mach_task_self(),                              theObject,                              MACH_PORT_RIGHT_SEND,                              &result);      printf("io_object_t: 0x%08x, Class: %s, Retain Count: %d, Result=0x%08x\n",            theObject, className, result, kr2); }
```

If you get the famous 0x10000003 (`MACH_SEND_INVALID_DEST`) return code back from an IOKit.framework function, that's referring to a stale `io_object_t`, not the underlying kernel object. For more information on I/O Kit error codes, please refer to _[Making sense of IOKit error codes](https://developer.apple.com/library/archive/qa/qa1075/_index.html#//apple_ref/doc/uid/DTS10001627)_.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2008-09-24 | Minor editorial changes. |
| 2002-09-04 | New document that distinguishes between the retain counts of an I/O Kit kernel object and its io_object_t user space proxy. |

