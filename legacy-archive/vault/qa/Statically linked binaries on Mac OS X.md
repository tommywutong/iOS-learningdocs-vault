---
title: Statically linked binaries on Mac OS X
apple_id: DTS10001666
resource_type: QA
platform: Xcode Developer Tools|macOS
topic: Xcode
technology: null
published: '2011-09-20'
source_url: https://developer.apple.com/library/archive/qa/qa1118/_index.html
archived_at: '2026-07-18T02:29:55.849915Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1118

# Statically linked binaries on Mac OS X

## Q:  I'm trying to link my binary statically, but it's failing to link because it can't find `crt0.o`. Why?

A: Before discussing this issue, it's important to be clear about terminology:

- A __static library__ is a library of code that can be linked into a binary that will, eventually, be dynamically linked to the system libraries and frameworks.
- A __statically linked binary__ is one that does not import system libraries and frameworks dynamically, but instead makes direct system calls into the kernel.

Apple fully supports static libraries; if you want to create one, just start with the appropriate Xcode project or target template.

Apple does not support statically linked binaries on Mac OS X. A statically linked binary assumes binary compatibility at the kernel system call interface, and we do not make any guarantees on that front. Rather, we strive to ensure binary compatibility in each dynamically linked system library and framework.

If your project absolutely must create a statically linked binary, you can get the `Csu` (C startup) module from [Darwin](http://www.opensource.apple.com/) and try building `crt0.o` for yourself. Obviously, we won't support such an endeavor.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2011-09-20 | Rewritten to clarify Apple's position on statically linked binaries. |
| 2002-02-07 | New document that explains that statically linked binaries are not supported on Mac OS X. |

