---
title: Avoiding Kernel Event Conflicts
apple_id: DTS10001615
resource_type: QA
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2011-07-26'
source_url: https://developer.apple.com/library/archive/qa/qa1063/_index.html
archived_at: '2026-07-18T02:29:55.113222Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1063

# Avoiding Kernel Event Conflicts

## Q:  I'm writing a Mac OS X kernel extension and I want to use kernel events (as defined in `<sys/kern_event.h>`) to talk to a daemon process. I'm worried that my use of kernel events might conflict with other kernel extensions. What should I set the `vendor_code` field of the `kern_event_msg` structure to?

A: This field should either be set to `KEV_VENDOR_APPLE` (1) for Apple-defined events, or a registered creator code for third party events. If your product already has a registered creator code, you can use that. Otherwise you should register one using the [Creator Code Registration](https://developer.apple.com/support/mac/creator-code-registration.html) page on the Apple developer web site.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2011-07-26 | Reformatted content and made minor editorial changes. |
| 2001-09-14 | New document that documents the namespace for the vendor_code field of the kern_event_msg structure. |

