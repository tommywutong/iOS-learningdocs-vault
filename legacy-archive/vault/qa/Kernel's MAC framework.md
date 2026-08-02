---
title: Kernel's MAC framework
apple_id: DTS10004558
resource_type: QA
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2008-01-04'
source_url: https://developer.apple.com/library/archive/qa/qa1574/_index.html
archived_at: '2026-07-18T02:32:19.656014Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1574

# Kernel's MAC framework

## Q:  Why isn't the kernel's MAC framework documented?

A: Why isn't the kernel's MAC framework documented?

The kernel's MAC (Mandatory Access Control) framework is not supported for third party development on current systems. The headers were mistakenly included in the Kernel framework installed by the Mac OS X 10.5 SDK
(r. 5645458)
.

Specifically, the functionality in the following headers files is not considered to be a supported Kernel Programming Interface (KPI).

- `<security/_label.h>`
- `<security/mac.h>`
- `<security/mac_alloc.h>`
- `<security/mac_data.h>`
- `<security/mac_framework.h>`
- `<security/mac_internal.h>`
- `<security/mac_mach_internal.h>`
- `<security/mac_policy.h>`

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2008-01-04 | New document that cautions that the kernel's MAC framework is currently not support. |

