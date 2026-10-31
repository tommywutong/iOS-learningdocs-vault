---
title: 'conforms(to:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/conforms(to:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/conforms(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/conforms%28to%3A%29.json'
content_hash: 'sha256:1ed75d21e31b8fa2'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# conforms(to:)

<sub>类型方法</sub>

返回一个布尔值，指示目标是否符合给定协议。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func conforms(to protocol: Protocol) -> Bool
```

## 参数

- `protocol` — A protocol.

## 返回值

若目标符合 `protocol`，则为 [YES](../yes.md)；否则为 [NO](../no.md)。

## 讨论

若类采用协议或继承自采用该协议的另一个类，则该类“符合”该协议。类通过在接口声明后的尖括号内列出协议来采用协议。例如，此处 `MyClass` 采用（虚构的）`AffiliationRequests` 和 `Normalization` 协议：

```objc
@interface MyClass : NSObject <AffiliationRequests, Normalization>
```

类也符合它采用或继承的协议中包含的任何协议。协议以与类采用协议相同的方式合并其他协议。例如，此处 `AffiliationRequests` 协议合并了 `Joining` 协议：

```objc
@protocol AffiliationRequests <Joining>
```

若类采用合并了另一个协议的协议，它也必须实现被合并协议中的所有方法，或从采用该协议的类继承这些方法。

此方法仅基于头文件中的正式声明（如上所示）来判定符合性。它不会检查协议中声明的方法是否实际已实现——那是程序员的责任。

要指定作为此方法参数所需的协议，请使用 `@protocol()` 指令：

```objc
BOOL canJoin = [MyClass conformsToProtocol:@protocol(Joining)];
```

### Performance Considerations

在性能敏感的代码中调用此方法可能导致不必要的性能问题。[+ conformsToProtocol:](<conforms(to_).md>) 需要获取 Objective-C 运行时锁并遍历目标的类层次结构以检查协议符合性，这可能花费大量时间。

Consider the following alternatives in your code:

- 改用 [- respondsToSelector:](<../nsobjectprotocol/responds(to_).md>) 检查协议中的方法，尤其是在你只需要检查协议的某些方法时。
- 若确实需要使用 [- conformsToProtocol:](<../nsobjectprotocol/conforms(to_).md>)，请尽可能缓存结果，而不是反复调用此方法。
