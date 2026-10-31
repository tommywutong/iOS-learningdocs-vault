---
title: 'isMember(of:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobjectprotocol/ismember(of:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobjectprotocol/ismember(of:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobjectprotocol/ismember%28of%3A%29.json'
content_hash: 'sha256:e769037ce13459df'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObjectProtocol](../nsobjectprotocol.md)

# isMember(of:)

<sub>实例方法</sub>

返回一个布尔值，指示接收者是否是给定类的实例。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isMember(of aClass: AnyClass) -> Bool
```

## 参数

- `aClass` — 表示要测试的 Objective-C 类的类对象。

## 返回值

若接收者是 `aClass` 的实例，则为 [YES](../yes.md)；否则为 [NO](../no.md)。

## 讨论

例如，在此代码中，[- isMemberOfClass:](<ismember(of_).md>) 将返回 [NO](../no.md)：

```objc
NSMutableData *myData = [NSMutableData dataWithCapacity:30];
id anArchiver = [[NSArchiver alloc] initForWritingWithMutableData:myData];
if ([anArchiver isMemberOfClass:[NSCoder class]])
    ...
```

类对象可能是编译器创建的对象，但它们仍支持成员资格概念。因此，你可以使用此方法验证接收者是否是特定的 Class 对象。

## 另请参阅

### Testing Object Inheritance, Behavior, and Conformance

- [- isKindOfClass:](<iskind(of_).md>) — 返回一个布尔值，指示接收者是否为给定类的实例，或是否为继承自该类的任意类的实例。
- [- respondsToSelector:](<responds(to_).md>) — 返回一个布尔值，指示接收者是否实现或继承了可响应指定消息的方法。
- [- conformsToProtocol:](<conforms(to_).md>) — 返回一个布尔值，指示接收者是否符合给定协议。
