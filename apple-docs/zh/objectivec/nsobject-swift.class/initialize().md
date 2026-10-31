---
title: initialize()
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/initialize()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/initialize()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/initialize%28%29.json'
content_hash: 'sha256:cc2fe1a4747a387c'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# initialize()

<sub>类型方法</sub>

在类收到第一条消息之前对其进行初始化。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func initialize()
```

## 讨论

运行时在程序中的每个类（或继承自它的任何类）即将收到来自程序内的第一条消息之前，向该类发送 [+ initialize](<initialize().md>)。超类在其子类之前收到此消息。

运行时以线程安全的方式向类发送 [+ initialize](<initialize().md>) 消息。也就是说，[+ initialize](<initialize().md>) 由向类发送消息的第一个线程运行，任何尝试向该类发送消息的其他线程都会阻塞，直到 [+ initialize](<initialize().md>) 完成。

若子类未实现 [+ initialize](<initialize().md>)——运行时将调用继承的实现——或子类显式调用 `[super initialize]`，则超类实现可能会被多次调用。若要保护自己免于多次运行，可以按以下方式构建实现：

```objc
+ (void)initialize {
  if (self == [ClassName self]) {
    // ... do the initialization ...
  }
}
```

由于 [+ initialize](<initialize().md>) 以阻塞方式调用，将方法实现限制为尽可能最少的必要工作非常重要。具体而言，任何获取其他类在其 [+ initialize](<initialize().md>) 方法中可能需要的锁的代码都可能导致死锁。因此，你不应依赖 [+ initialize](<initialize().md>) 进行复杂初始化，而应将其限制为简单的、类本地的初始化。

### 特殊注意事项

[+ initialize](<initialize().md>) 每个类只调用一次。若要对类和该类的类别执行独立初始化，应实现 [+ load](<load().md>) 方法。

## 另请参阅

### 相关文档

- [- init](<init().md>) — 由子类实现，以在为新对象（接收者）分配内存后立即对其进行初始化。

### 初始化类

- [+ load](<load().md>) — 每当类或类别添加到 Objective-C 运行时都会调用；实现此方法以在加载时执行特定于类的行为。
