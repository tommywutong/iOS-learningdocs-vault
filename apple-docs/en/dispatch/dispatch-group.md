---
title: Dispatch Group
framework: Dispatch
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch-group
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch-group'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch-group.json'
content_hash: 'sha256:10eab6646dccba73'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# Dispatch Group

<sub>API Collection</sub>

A group of tasks that you monitor as a single unit.

## Overview

Groups allow you to aggregate a set of tasks and synchronize behaviors on the group. You attach multiple blocks to a group and schedule them for asynchronous execution on the same queue or different queues. When all blocks finish executing, the group executes its completion handler. You can also wait synchronously for all blocks in the group to finish executing.

## Topics

### Creating a Dispatch Group

- [dispatch_group_create](<dispatchgroup/init().md>) — Creates a new group to which you can assign block objects.
- [dispatch_group_t](dispatch_group_t.md) — A group of block objects submitted to a queue for asynchronous invocation.

### Updating the Group Manually

- [dispatch_group_enter](<dispatchgroup/enter().md>) — Explicitly indicates that a block has entered the group.
- [dispatch_group_leave](<dispatchgroup/leave().md>) — Explicitly indicates that a block in the group finished executing.

## See Also

### Queues and Tasks

- [DispatchQueue](dispatchqueue.md) — An object that manages the execution of tasks serially or concurrently on your app’s main thread or on a background thread.
- [DispatchWorkItem](dispatchworkitem.md) — The work you want to perform, encapsulated in a way that lets you attach a completion handle or execution dependencies.
- [DispatchGroup](dispatchgroup.md) — A group of tasks that you monitor as a single unit.
- [Dispatch Queue](dispatch-queue.md) — An object that manages the execution of tasks serially or concurrently on your app’s main thread or on a background thread.
- [Dispatch Work Item](dispatch-work-item.md) — The work you want to perform, encapsulated in a way that lets you attach a completion handle or execution dependencies.
- [Workloop](workloop.md) — A dispatch object that prioritizes the execution of tasks based on their quality-of-service (QoS) level.
