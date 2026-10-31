---
title: 'protocol_addMethodDescription(_:_:_:_:_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.3+, iPadOS 4.3+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/protocol_addmethoddescription(_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/protocol_addmethoddescription(_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/protocol_addmethoddescription%28_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:c019ac4cf8ea55cd'
translated: true
---

> 导航： [技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# protocol_addMethodDescription(_:_:_:_:_:)

<sub>函数</sub>

Adds a method to a protocol.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func protocol_addMethodDescription(_ proto: Protocol, _ name: Selector, _ types: UnsafePointer<CChar>?, _ isRequiredMethod: Bool, _ isInstanceMethod: Bool)
```

## 参数

- `proto` — 要向其添加方法的协议。

- `name` — 要添加的方法的名称。

- `types` — 表示要添加的方法签名的 C 字符串。

- `isRequiredMethod` — 布尔值，指示该方法是否为 `proto` 协议的必需方法。若为 [YES](yes.md)，则为必需方法；若为 [NO](no.md)，则为可选方法。

- `isInstanceMethod` — 布尔值，指示该方法是否为实例方法。若为 [YES](yes.md)，则为实例方法；若为 [NO](no.md)，则为类方法。

## 讨论

要使用此函数向协议添加方法，该协议必须处于构建中。也就是说，必须在通过 [objc_registerProtocol](<objc_registerprotocol(__).md>) 函数向 Objective-C 运行时注册 `proto` 之前添加所有方法。

## 另请参阅

### Working with Protocols

- [objc_getProtocol](<objc_getprotocol(__).md>) — 返回指定的协议。
- [objc_copyProtocolList](<objc_copyprotocollist(__).md>) — 返回一个数组，包含 runtime 已知的所有协议。
- [objc_allocateProtocol](<objc_allocateprotocol(__).md>) — 创建一个新的协议实例。
- [objc_registerProtocol](<objc_registerprotocol(__).md>) — 向 Objective-C runtime 注册一个新创建的协议。
- [protocol_addProtocol](<protocol_addprotocol(____).md>) — 将一个已注册的协议添加到另一个正在构建中的协议。
- [protocol_addProperty](<protocol_addproperty(____________).md>) — 向一个正在构建中的协议添加一个属性。
- [protocol_getName](<protocol_getname(__).md>) — 返回一个协议的名称。
- [protocol_isEqual](<protocol_isequal(____).md>) — 返回一个布尔值，指示两个协议是否相等。
- [protocol_copyMethodDescriptionList](<protocol_copymethoddescriptionlist(________).md>) — 返回一个数组，包含给定协议中符合给定规范的方法的方法描述。
- [protocol_getMethodDescription](<protocol_getmethoddescription(________).md>) — 返回给定协议中指定方法的方法描述结构体。
- [protocol_copyPropertyList](<protocol_copypropertylist(____).md>) — 返回一个数组，包含某个协议声明的属性。
- [protocol_getProperty](<protocol_getproperty(________).md>) — 返回给定协议中指定的属性。
- [protocol_copyProtocolList](<protocol_copyprotocollist(____).md>) — 返回一个数组，包含某个协议采用的协议。
- [protocol_conformsToProtocol](<protocol_conformstoprotocol(____).md>) — 返回一个布尔值，指示一个协议是否符合另一个协议。
