---
title: Supported KPIs
apple_id: DTS40007491
resource_type: QA
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2008-03-25'
source_url: https://developer.apple.com/library/archive/qa/qa1575/_index.html
archived_at: '2026-07-18T02:32:19.691136Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1575

# Supported KPIs

## Q:  How do I tell whether a kernel function is part of a supported KPI?

A: How do I tell whether a kernel function is part of a supported KPI?

There are two basic criteria:

- Does the function appear in the Kernel framework headers?
- Is the function exported by one of the supported KPI symbol sets?

Checking the first criterion is easy: use your favorite text search tool to see if the function is declared in the Kernel framework headers.

There are two ways to check the second criterion.

- If you have already built a KEXT, you can use the `kextlibs` tool to determine the KPI symbol sets that it requires. See the man page for more details.
- If you haven't yet built a KEXT, you can use the FindKPI.py script to determine the KPI symbol set, if any, for a given symbol. Listing 1 shows an example of this.

__Listing 1__  Using FindKPI.py

```
$ ./FindKPI.py vnode_create lck_mtx_lock vnode_create com.apple.kpi.bsd lck_mtx_lock com.apple.kpi.libkern $ # You can also supply C++ class names. $ ./FindKPI.py OSDictionary IOMemoryDescriptor OSDictionary com.apple.kpi.libkern IOMemoryDescriptor com.apple.kpi.iokit
```

Of course, there are exceptions to every rule. For example:

- The header `<sys/appleapiopts.h>` defines a set of compile-time variables that are used to indicate the stability of a particular interface. Some of these—specifically `__APPLE_API_EVOLVING`, `__APPLE_API_UNSTABLE`, `__APPLE_API_PRIVATE` and `__APPLE_API_OBSOLETE`—are used to guard KPIs that are not 100% stable. You should try to avoid such KPIs where possible.

  To check whether you depend on such KPIs, define the compile-time variable `__APPLE_API_STRICT_CONFORMANCE`.
- [Technical Q&A QA1574, 'Kernel's MAC framework'](https://developer.apple.com/qa/qa2007/qa1574.html) documents a bug that might mislead you into thinking that the kernel's MAC framework is a supported KPI.
- The `com.apple.kpi.unsupported` KPI is a compatibility measure intended for use by a limited number of Apple KEXTs. Your KEXT should not depend on this unsupported functionality.

- FindKPI.py script ("qa1575_FindKPI.zip", 1.3K)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2008-03-25 | New document that describes how to check whether a kernel function is part of a supported KPI. |

