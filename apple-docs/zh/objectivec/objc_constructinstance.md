---
title: objc_constructInstance
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/objc_constructinstance
source_url: 'https://developer.apple.com/documentation/objectivec/objc_constructinstance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_constructinstance.json'
content_hash: 'sha256:b756e704601299f0'
translated: true
---

> 导航： [技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_constructInstance

<sub>函数</sub>

在指定位置创建类的实例。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern idobjc_constructInstance(Class cls, void *bytes);
```

## 参数

- `cls` — 要为其分配实例的类。

- `bytes` — 要在其中分配 `cls` 类实例的位置。`bytes` 必须指向至少 `class_getInstanceSize(cls)` 字节的对齐良好、已清零的内存。

## 返回值

若成功，则为位于 `bytes` 的 `cls` 类实例；否则为 `nil`（例如，若 `cls` 或 `bytes` 本身为 `nil`）。

## 另请参阅

### 实例化类

- [class_createInstance](<class_createinstance(____).md>) — 创建类的实例，在默认 malloc 内存区域中为该类分配内存。
- [objc_destructInstance](objc_destructinstance.md) — 销毁类的实例但不释放内存，并移除其任何关联引用。
