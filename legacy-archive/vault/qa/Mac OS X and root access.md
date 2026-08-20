---
title: Mac OS X and root access
apple_id: DTS10001568
resource_type: QA
platform: macOS
topic: Security
technology: null
published: '2008-09-16'
source_url: https://developer.apple.com/library/archive/qa/qa1013/_index.html
archived_at: '2026-07-18T02:29:54.687938Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1013

# Mac OS X and root access

## Q:  I'm developing on Mac OS X, and some tasks such as running `kextload` require me to have root privileges. But when I try the usual UNIX command `su root` the system rejects my password. How can I get root access on Mac OS X?

A: I'm developing on Mac OS X, and some tasks such as running `kextload` require me to have root privileges. But when I try the usual UNIX command `su root` the system rejects my password. How can I get root access on Mac OS X?

The client version of Mac OS X ships with the `root` account disabled. This is an intentional security feature to limit the support problems that could arise from casual use of the `root` user's privileges. However, it is sometimes necessary for developers to obtain root privileges, such as when developing kernel extensions.

There are a couple of ways to obtain root privileges. The best approach is especially good for those situations where you need only occasional access to root privileges and you wish to maintain the security of your system. In this case, use the `sudo` command in Terminal to either execute a single command as `root` or to get a root login prompt. Details are in the man page for `sudo`.

The other option is to permanently enable the `root` account. This approach might make sense on development systems where there is a frequent need for root privileges. Detailed instructions are given in this [support article](http://support.apple.com/kb/HT1528).

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2008-09-16 | Modernized and made minor editorial changes. |
| 2001-03-13 | New document that describes how to enable root access in Mac OS X. |

