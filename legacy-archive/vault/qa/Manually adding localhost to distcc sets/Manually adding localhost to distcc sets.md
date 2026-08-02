---
title: Manually adding localhost to distcc sets
apple_id: DTS40007921
resource_type: QA
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/qa/qa1597/_index.html
archived_at: '2026-07-18T02:32:22.035236Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1597

# Manually adding localhost to distcc sets

## Q:  Why isn't distcc using localhost (127.0.0.1) for distributed builds?

A: Using `distcc` can result in significantly improved build system performance when available. When using `distcc`, unless your build is being distributed to enough high performance remote machines to saturate your local I/O bandwidth or CPU with preprocessing work, you will likely want to use `localhost` (127.0.01) when building your project.

In the Xcode preferences `Distributed Builds` pane, you need to add a computer named `localhost` to a set of machines designated for `distcc` builds. Make sure the set of machines to which you've added (`localhost`) is enabled by clicking the relevant checkbox. This behavior is new in Xcode 3.0 - in Xcode 2.4 `localhost` was never included, and in Xcode 2.3 `localhost` was always included in `distcc` builds.

__Figure 1__  Xcode 3 Distributed Builds Preference Pane.

!!

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2008-08-08 | New document that describes how to manually configure distcc to use localhost |

