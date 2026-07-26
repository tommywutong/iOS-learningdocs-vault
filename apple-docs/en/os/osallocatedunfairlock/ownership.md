---
title: OSAllocatedUnfairLock.Ownership
framework: os
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/osallocatedunfairlock/ownership
source_url: 'https://developer.apple.com/documentation/os/osallocatedunfairlock/ownership'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/osallocatedunfairlock/ownership.json'
content_hash: 'sha256:b0d8ace846fb9a56'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSAllocatedUnfairLock](../osallocatedunfairlock.md)

# OSAllocatedUnfairLock.Ownership

<sub>Enumeration</sub>

An enumeration that represents the ownership status of an unfair lock.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen enum Ownership
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Copyable](../../swift/copyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Specifying ownership

- [OSAllocatedUnfairLock.Ownership.owner](ownership/owner.md) — Describes code that owns the lock.
- [OSAllocatedUnfairLock.Ownership.notOwner](ownership/notowner.md) — Describes code that doesn’t own the lock.

## See Also

### Determining lock ownership

- [precondition(_:)](<precondition(__).md>) — Asserts if the lock object fails to meet specified ownership requirements.
