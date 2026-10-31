---
title: lockIfAvailable()
framework: os
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/osallocatedunfairlock/lockifavailable()
source_url: 'https://developer.apple.com/documentation/os/osallocatedunfairlock/lockifavailable()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/osallocatedunfairlock/lockifavailable%28%29.json'
content_hash: 'sha256:1e6251818fea7ad1'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [OSAllocatedUnfairLock](../osallocatedunfairlock.md)

# lockIfAvailable()

<sub>实例方法</sub>

尝试获取锁。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func lockIfAvailable() -> Bool
```

## 返回值

[true](../../swift/true.md) 表示成功；否则为 [false](../../swift/false.md)。

## 另请参阅

### 使用锁

- [lock()](<lock().md>) — 获取锁。
- [unlock()](<unlock().md>) — 解锁。
