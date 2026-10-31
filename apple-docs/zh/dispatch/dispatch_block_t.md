---
title: dispatch_block_t
framework: Dispatch
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_block_t
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_block_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_block_t.json'
content_hash: 'sha256:1d45a1d0ded9c937'
translated: true
---

> 导航： [技术](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_block_t

<sub>类型别名</sub>

提交到 dispatch queue 的 block 的原型；这些 block 不接受参数且无返回值。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
typedef void (^)(void) dispatch_block_t;
```

## 讨论

block 的行为与其他 Objective-C 对象类似。在 ARC 下，系统会自动释放和保留它们，并在需要时将它们转换为 malloc block，以便它们能逃逸出当前执行作用域。当禁用 ARC 时，你有责任在适当的时候保留和释放 block，并在允许它们逃逸出当前执行作用域之前拷贝它们。

## 另请参阅

### 异步执行任务

- [dispatch_async](dispatch_async.md) — 将一个 block 提交到某个 dispatch queue 上异步执行，并立即返回。
- [dispatch_async_f](dispatch_async_f.md) — 将一个 App 定义的函数提交到某个 dispatch queue 上异步执行，并立即返回。
- [dispatch_after](dispatch_after.md) — 将一个 block 排队，以便在指定时间执行。
- [dispatch_after_f](dispatch_after_f.md) — 将一个 App 定义的函数排队，以便在指定时间执行。
- [dispatch_function_t](dispatch_function_t.md) — 提交到 dispatch queue 的函数的原型。
