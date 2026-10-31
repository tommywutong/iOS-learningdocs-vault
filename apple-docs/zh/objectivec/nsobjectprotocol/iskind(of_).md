---
title: 'isKind(of:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobjectprotocol/iskind(of:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobjectprotocol/iskind(of:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobjectprotocol/iskind%28of%3A%29.json'
content_hash: 'sha256:8cecdb5c76ea963e'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObjectProtocol](../nsobjectprotocol.md)

# isKind(of:)

<sub>实例方法</sub>

返回一个布尔值，指示接收者是否是给定类的实例，或继承自该类的任何类的实例。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isKind(of aClass: AnyClass) -> Bool
```

## 参数

- `aClass` — 表示要测试的 Objective-C 类的类对象。

## 返回值

若接收者是 `aClass` 的实例或继承自 `aClass` 的任何类的实例，则为 [YES](../yes.md)；否则为 [NO](../no.md)。

## 讨论

例如，在此代码中，[- isKindOfClass:](<iskind(of_).md>) 将返回 [YES](../yes.md)，因为在 Foundation 中，[NSArchiver](../../foundation/nsarchiver.md) 类继承自 [NSCoder](../../foundation/nscoder.md)：

```objc
NSMutableData *myData = [NSMutableData dataWithCapacity:30];
id anArchiver = [[NSArchiver alloc] initForWritingWithMutableData:myData];
if ( [anArchiver isKindOfClass:[NSCoder class]] )
    ...
```

在由类簇表示的对象上使用此方法时要小心。由于类簇的性质，你取回的对象可能并不总是你期望的类型。若你调用返回类簇的方法，该方法返回的确切类型是你可以对该对象执行什么操作的最佳指示。例如，若方法返回指向 [NSArray](../../foundation/nsarray.md) 对象的指针，则不应使用此方法来查看数组是否可变，如下列代码所示：

```objc
// DO NOT DO THIS!
if ([myArray isKindOfClass:[NSMutableArray class]])
{
    // Modify the object
}
```

若在代码中使用此类构造，你可能认为可以修改实际上不应修改的对象。这样做可能会给期望该对象保持不变的其他代码带来问题。

若接收者是类对象，则当 `aClass` 是相同类型的 Class 对象时，此方法返回 [YES](../yes.md)，否则返回 [NO](../no.md)。

## 另请参阅

### Testing Object Inheritance, Behavior, and Conformance

- [- isMemberOfClass:](<ismember(of_).md>) — 返回一个布尔值，指示接收者是否为给定类的实例。
- [- respondsToSelector:](<responds(to_).md>) — 返回一个布尔值，指示接收者是否实现或继承了可响应指定消息的方法。
- [- conformsToProtocol:](<conforms(to_).md>) — 返回一个布尔值，指示接收者是否符合给定协议。
