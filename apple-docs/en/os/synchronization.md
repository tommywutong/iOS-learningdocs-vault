---
title: Synchronization
framework: os
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/os/synchronization
source_url: 'https://developer.apple.com/documentation/os/synchronization'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/synchronization.json'
content_hash: 'sha256:b1b55c8cdbc98a5d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# Synchronization

<sub>API Collection</sub>

Access low-level synchronization mechanisms to control state across threads.

## Overview

> [!note] Note
> When possible, use higher-level synchronization primitives such as `pthread`, Grand Central Dispatch, or Swift’s concurrency features to control access to state across different threads. For more information, see [Updating an App to Use Swift Concurrency](../swift/updating_an_app_to_use_swift_concurrency.md).

## Topics

### Swift Wrappers

- [OSAllocatedUnfairLock](osallocatedunfairlock.md) — A structure that creates an unfair lock.
- [OSAllocatedUnfairLockFlags](osallocatedunfairlockflags.md)
