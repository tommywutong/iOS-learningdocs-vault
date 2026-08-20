---
title: File System Events Programming Guide
apple_id: TP40005289
resource_type: Guide
platform: macOS
topic: Data Management
technology: CoreServices
published: '2012-12-13'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/FSEvents_ProgGuide/Introduction/Introduction.html
archived_at: '2026-07-15T07:23:04.134773Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Technology%20Overview.md)

# Introduction

The file system events API provides a way for your application to ask for notification when the contents of a directory hierarchy are modified. For example, your application can use this to quickly detect when the user modifies a file within a project bundle using another application.

It also provides a lightweight way to determine whether the contents of a directory hierarchy have changed since your application last examined them. For example, a backup application can use this to determine what files have changed since a given time stamp or a given event ID.

You should read this document if your application works with a large number of files—particularly if your application works with large hierarchies of files.

This document is organized into the following chapters:

- [Technology Overview](Technology%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2teobzfvbuqmznknltc)—describes the file system events API and explains how it works at a high level.
- [Using the File System Events API](Using%20the%20File%20System%20Events%20API.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2teobzfvbuqnbnknlti)—explains how to use the file system events API, from creating an event stream to writing a handler, including code examples to help you quickly get started.
- [File System Event Security](File%20System%20Event%20Security.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2teobzfvbuqnrnknltc)—describes the security features of the file system events API.
- [Kernel Queues: An Alternative to File System Events](Kernel%20Queues-%20An%20Alternative%20to%20File%20System%20Events.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2teobzfvbuqnjnknlte)—explains the kernel queues mechanism, describes when it may be appropriate to use the kernel queues API in lieu of the file system events API, and includes a brief code example to show you how to use it.

[Next](Technology%20Overview.md)

