---
title: DispatchGroup
framework: Dispatch
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchgroup
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchgroup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchgroup.json'
content_hash: 'sha256:7c624d16df14952d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# DispatchGroup

<sub>Class</sub>

A group of tasks that you monitor as a single unit.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class DispatchGroup
```

## Overview

Groups allow you to aggregate a set of tasks and synchronize behaviors on the group. You attach multiple work items to a group and schedule them for asynchronous execution on the same queue or different queues. When all work items finish executing, the group executes its completion handler. You can also wait synchronously for all tasks in the group to finish executing.

## Relationships

- **Inherits From**: [DispatchObject](dispatchobject.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a Dispatch Group

- [dispatch_group_create](<dispatchgroup/init().md>) — Creates a new group to which you can assign block objects.

### Adding a Completion Handler

- [notify(qos:flags:queue:execute:)](<dispatchgroup/notify(qos_flags_queue_execute_).md>) — Schedules the submission of a block with the specified attributes to a queue when all tasks in the current group have finished executing.
- [notify(queue:work:)](<dispatchgroup/notify(queue_work_).md>) — Schedules the submission of a block to a queue when all tasks in the current group have finished executing.

### Waiting for Tasks to Finish Executing

- [wait()](<dispatchgroup/wait().md>) — Waits synchronously for the previously submitted work to finish.
- [wait(timeout:)](<dispatchgroup/wait(timeout_).md>) — Waits synchronously for the previously submitted work to complete, and returns if the work is not completed before the specified timeout period has elapsed.
- [wait(wallTimeout:)](<dispatchgroup/wait(walltimeout_).md>) — Waits synchronously for the previously submitted work to complete, and returns if the work is not completed before the specified timeout period has elapsed.

### Updating the Group Manually

- [dispatch_group_enter](<dispatchgroup/enter().md>) — Explicitly indicates that a block has entered the group.
- [dispatch_group_leave](<dispatchgroup/leave().md>) — Explicitly indicates that a block in the group finished executing.

## See Also

### Queues and Tasks

- [DispatchQueue](dispatchqueue.md) — An object that manages the execution of tasks serially or concurrently on your app’s main thread or on a background thread.
- [DispatchWorkItem](dispatchworkitem.md) — The work you want to perform, encapsulated in a way that lets you attach a completion handle or execution dependencies.
- [Dispatch Queue](dispatch-queue.md) — An object that manages the execution of tasks serially or concurrently on your app’s main thread or on a background thread.
- [Dispatch Work Item](dispatch-work-item.md) — The work you want to perform, encapsulated in a way that lets you attach a completion handle or execution dependencies.
- [Dispatch Group](dispatch-group.md) — A group of tasks that you monitor as a single unit.
- [Workloop](workloop.md) — A dispatch object that prioritizes the execution of tasks based on their quality-of-service (QoS) level.
