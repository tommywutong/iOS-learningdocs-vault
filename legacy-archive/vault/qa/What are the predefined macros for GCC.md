---
title: What are the predefined macros for GCC?
apple_id: DTS10003638
resource_type: QA
platform: macOS
topic: Xcode
technology: null
published: '2010-06-18'
source_url: https://developer.apple.com/library/archive/qa/qa1424/_index.html
archived_at: '2026-07-18T02:30:39.856000Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1424

# What are the predefined macros for GCC?

## Q:  Is there any way to get a list of GCC's predefined macros?

A: The following command line entered in terminal will generate a list of GCC's predefined macros for the i386 architecture:


```
gcc -arch i386 -dM -E - < /dev/null | sort
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2010-06-18 | Fixed typo: "effect" -> "affect". -arch changed from ppc to i386 and x86_64. |
| 2005-07-06 | New document that shows how to display a list of GCC predefined macros. |

