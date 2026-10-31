---
title: class
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/class
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/class'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/class.json'
content_hash: 'sha256:0569dc89bbd29653'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# class

<sub>类型方法</sub>

Returns the class object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (Class) class;
```

## 返回值

The class object.

## 讨论

仅当类是消息的接收者时，才按名称引用该类。在所有其他情况下，必须通过此方法或类似方法获取类对象。例如，此处将 `SomeClass` 作为参数传递给 `NSObject` 协议中声明的 [- isKindOfClass:](<../nsobjectprotocol/iskind(of_).md>) 方法：

```objc
BOOL test = [self isKindOfClass:[SomeClass class]];
```

## 另请参阅

### 相关文档

- [NSStringFromClass(_:)](<../../foundation/nsstringfromclass(__).md>) — 以字符串形式返回类的名称。
- [class](../nsobject-c.protocol/class.md) — 返回接收者所属类的类对象。
- [NSClassFromString(_:)](<../../foundation/nsclassfromstring(__).md>) — 通过名称获取类。

### 识别类

- [+ superclass](<superclass().md>) — 返回接收者超类的类对象。
- [+ isSubclassOfClass:](<issubclass(of_).md>) — 返回一个布尔值，指示接收类是否为给定类的子类，或与给定类相同。
