---
title: os_block_t
framework: os
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_block_t
source_url: 'https://developer.apple.com/documentation/os/os_block_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_block_t.json'
content_hash: 'sha256:c8bddd12fd68a7b1'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# os_block_t

<sub>类型别名</sub>

一种不接受参数且不返回值的 block。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
typedef void (^)(void) os_block_t;
```

## 讨论

在未启用 Objective-C ARC 进行构建时，在堆上分配或复制到堆上的 block 对象必须通过 [release](../objectivec/nsobject-c.protocol/release.md) 消息或 `Block_release` 函数释放。

block 字面量的声明会在栈上分配存储空间。

## 另请参阅

### 内存

- [os_proc_available_memory](os_proc_available_memory.md) — 确定当前 App 可用的内存量。
- [os_function_t](os_function_t.md) — 指向函数的指针。
- [os_release](os_release-c.func.md)
- [os_retain](os_retain-c.func.md)
