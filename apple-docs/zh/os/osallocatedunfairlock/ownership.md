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
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [OSAllocatedUnfairLock](../osallocatedunfairlock.md)

# OSAllocatedUnfairLock.Ownership

<sub>枚举</sub>

表示 unfair lock 所有权状态的枚举。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen enum Ownership
```

## 关系

- **遵循**： [BitwiseCopyable](../../swift/bitwisecopyable.md)、[Copyable](../../swift/copyable.md)、[Equatable](../../swift/equatable.md)、[Hashable](../../swift/hashable.md)、[Sendable](../../swift/sendable.md)、[SendableMetatype](../../swift/sendablemetatype.md)

## 主题

### 指定所有权

- [OSAllocatedUnfairLock.Ownership.owner](ownership/owner.md) — 描述拥有该锁的代码。
- [OSAllocatedUnfairLock.Ownership.notOwner](ownership/notowner.md) — 描述不拥有该锁的代码。

## 另请参阅

### 判定锁所有权

- [precondition(_:)](<precondition(__).md>) — 如果锁对象未能满足指定的所有权要求，则触发断言。
