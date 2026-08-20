---
title: What is the "main bundle" of a command-line foundation tool?
apple_id: DTS10004115
resource_type: QA
platform: macOS
topic: Languages & Utilities
technology: null
published: '2006-10-10'
source_url: https://developer.apple.com/library/archive/qa/qa1436/_index.html
archived_at: '2026-07-18T02:30:43.163780Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1436

# What is the "main bundle" of a command-line foundation tool?

## Q:  What is the main bundle of a command-line foundation tool?

A: The main bundle of a command-line foundation tool is considered to be the tool's enclosing directory. That directory is what will be returned by the `[NSBundle mainBundle]` call. For exampe, a foundation tool binary located in: `/path/to/tool` would have the main bundle path returned as: `/path/to/tool`.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2006-10-10 | New document that reveals the location of the main bundle of a command-line foundation tool. |

