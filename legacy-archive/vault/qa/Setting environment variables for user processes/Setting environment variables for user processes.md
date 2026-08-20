---
title: Setting environment variables for user processes
apple_id: DTS10001619
resource_type: QA
platform: macOS
topic: General
technology: null
published: '2011-11-09'
source_url: https://developer.apple.com/library/archive/qa/qa1067/_index.html
archived_at: '2026-07-18T02:29:55.145867Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1067

# Setting environment variables for user processes

## Q:  How do I set environment for all processes launched by a specific user?

A: It is actually a fairly simple process to set environment variables for processes launched by a specific user.

There is a special environment file which loginwindow searches for each time a user logs in. The environment file is: `~/.MacOSX/environment.plist` (be careful it's case sensitive). Where '~' is the home directory of the user we are interested in. You will have to create the .MacOSX directory yourself using terminal (by typing `mkdir .MacOSX`). You will also have to create the environment file yourself. The environment file is actually in XML/plist format (make sure to add the .plist extension to the end of the filename or this won't work). An example environment file is shown below. The file was created using Xcode.

__Figure 1__  Example environment.plist using Property List Editor

!!

Here the environment variables `TestEnvironmentVariable` and `MrX` are set to MyValue and 1 respectively, every time that specific user logs in. Note that the key class must be string. If any other class is used the key will not be recognized by loginwindow. You can confirm the environment variables have been set as expected by typing `set` into terminal.

Cocoa applications can retrieve environment variables in NSDictionary form by using the NSProcessInfo class contained in the Foundation framework.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2011-11-09 | Reflects plist creation in Xcode rather than Property List Editor. |
| 2010-11-16 | Updated. |
| 2001-10-25 | New document that tells how to set environment variables for user processes. |

