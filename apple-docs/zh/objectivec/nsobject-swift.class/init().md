---
title: init()
framework: Objective-C Runtime
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/init()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/init()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/init%28%29.json'
content_hash: 'sha256:24ca24f9d648cfde'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# init()

<sub>初始化方法</sub>

由子类实现，以在为新对象（接收者）分配内存后立即对其进行初始化。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init()
```

## 返回值

已初始化的对象；若由于不会导致异常的某种原因而无法创建对象，则为 `nil`。

## 讨论

[- init](<init().md>) 消息与 [alloc](alloc.md)（或 [allocWithZone:](allocwithzone_.md)）消息在同一行代码中配对：

```objc
SomeClass *object = [[SomeClass alloc] init];
```

对象在初始化之前尚未准备好使用。

在此方法的自定义实现中，你必须调用超类的 [Initialization](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Initialization.html#//apple_ref/doc/uid/TP40008195-CH21)，然后初始化并返回新对象。若无法初始化新对象，该方法应返回 `nil`。例如，假设的 `BuiltInCamera` 类在没有摄像头的设备上运行时，可能会从其 `init` 方法返回 `nil`。

```objc
- (instancetype)init {
    if (self = [super init]) {
        // Initialize self
    }
    return self;
}
```

在某些情况下，[- init](<init().md>) 方法的自定义实现可能会返回替代对象。因此，在后续代码中，你必须始终使用 [- init](<init().md>) 返回的对象，而不是 [alloc](alloc.md) 或 [allocWithZone:](allocwithzone_.md) 返回的对象。

`NSObject` 类中定义的 [- init](<init().md>) 方法不做任何初始化；它只是返回 `self`。就可空性而言，调用者可以假定 `NSObject` 的 [- init](<init().md>) 实现不会返回 `nil`。

## 另请参阅

### 创建、拷贝与释放对象

- [- copy](<copy().md>) — 返回 `copy(with:)` 返回的对象。
- [- mutableCopy](<mutablecopy().md>) — 返回 `mutableCopy(with:)`（其中 zone 为 `nil`）返回的对象。
