---
title: 'objc_getProtocol(_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/objc_getprotocol(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/objc_getprotocol(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_getprotocol%28_%3A%29.json'
content_hash: 'sha256:b6948a3e093ed441'
translated: true
---

> 导航： [技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_getProtocol(_:)

<sub>函数</sub>

Returns a specified protocol.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func objc_getProtocol(_ name: UnsafePointer<CChar>) -> Protocol?
```

## 参数

- `name` — The name of a protocol.

## 返回值

名为 `name` 的协议；若找不到名为 `name` 的协议，则返回 `NULL`。

## 讨论

This function acquires the runtime lock.

## 另请参阅

### Working with Protocols

- [objc_copyProtocolList](<objc_copyprotocollist(__).md>) — 返回一个数组，包含 runtime 已知的所有协议。
- [objc_allocateProtocol](<objc_allocateprotocol(__).md>) — 创建一个新的协议实例。
- [objc_registerProtocol](<objc_registerprotocol(__).md>) — 向 Objective-C runtime 注册一个新创建的协议。
- [protocol_addMethodDescription](<protocol_addmethoddescription(__________).md>) — 向一个协议添加一个方法。
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
