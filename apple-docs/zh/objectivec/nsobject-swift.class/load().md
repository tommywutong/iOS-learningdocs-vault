---
title: load()
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/load()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/load()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/load%28%29.json'
content_hash: 'sha256:4be60cbf76ea49ac'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# load()

<sub>类型方法</sub>

每当类或类别添加到 Objective-C 运行时都会调用；实现此方法以在加载时执行特定于类的行为。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func load()
```

## 讨论

[+ load](<load().md>) 消息会发送给动态加载和静态链接的类和类别，但仅当新加载的类或类别实现了可以响应的方法时。

The order of initialization is as follows:

1. 你链接到的任何框架中的所有初始化程序。
2. All `+load` methods in your image.
3. 你的映像中的所有 C++ 静态初始化程序和 C/C++ `__attribute__(constructor)` 函数。
4. 链接到你的框架中的所有初始化程序。

In addition:

- 类的 `+load` 方法在其所有超类的 `+load` 方法之后调用。
- 类别的 `+load` 方法在类自身的 `+load` 方法之后调用。

因此，在 [+ load](<load().md>) 的自定义实现中，你可以安全地向同一映像中的其他无关类发消息，但这些类实现的任何 [+ load](<load().md>) 方法可能尚未运行。

> [!important] 重要
> 桥接到 Objective-C 的 Swift 类的 `load` 方法的自定义实现不会自动调用。

## 另请参阅

### 初始化类

- [+ initialize](<initialize().md>) — 在类收到第一条消息之前对其进行初始化。
