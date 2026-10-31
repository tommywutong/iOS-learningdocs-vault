---
title: 'precondition(_:)'
framework: os
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/osallocatedunfairlock/precondition(_:)'
source_url: 'https://developer.apple.com/documentation/os/osallocatedunfairlock/precondition(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/osallocatedunfairlock/precondition%28_%3A%29.json'
content_hash: 'sha256:709eebcd62048a43'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [OSAllocatedUnfairLock](../osallocatedunfairlock.md)

# precondition(_:)

<sub>实例方法</sub>

如果锁对象未能满足指定的所有权要求，则触发断言。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func precondition(_ condition: OSAllocatedUnfairLock<State>.Ownership)
```

## 参数

- `condition` — 要检查的所有权状态。

## 讨论

调用此函数以确保锁的所有权状态符合代码的要求。例如，若调用此函数并传入 [OSAllocatedUnfairLock.Ownership.owner](ownership/owner.md)，而对象已锁定但调用代码并不拥有该锁，则 App 会终止。类似地，若调用时传入 [OSAllocatedUnfairLock.Ownership.notOwner](ownership/notowner.md)，而调用代码不拥有该锁，或者对象未锁定，则 App 会终止。

## 另请参阅

### 判定锁所有权

- [Ownership](ownership.md) — 表示 unfair lock 所有权状态的枚举。
