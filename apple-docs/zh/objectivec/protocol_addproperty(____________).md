---
title: 'protocol_addProperty(_:_:_:_:_:_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.3+, iPadOS 4.3+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/protocol_addproperty(_:_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/protocol_addproperty(_:_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/protocol_addproperty%28_%3A_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:c65701c9db682e83'
translated: true
---

> 导航： [技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# protocol_addProperty(_:_:_:_:_:_:)

<sub>函数</sub>

向正在构建中的协议添加属性。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func protocol_addProperty(_ proto: Protocol, _ name: UnsafePointer<CChar>, _ attributes: UnsafePointer<objc_property_attribute_t>?, _ attributeCount: UInt32, _ isRequiredProperty: Bool, _ isInstanceProperty: Bool)
```

## 参数

- `proto` — 要向其添加属性的协议。

- `name` — 要添加的属性的名称。

- `attributes` — An array of property attributes.

- `attributeCount` — The number of properties in `attributes`.

- `isRequiredProperty` — 布尔值，指示该属性的访问器方法是否为 `proto` 协议的必需方法。若为 [YES](yes.md)，则访问器方法为必需方法；若为 [NO](no.md)，则为可选方法。

- `isInstanceProperty` — 布尔值，指示该属性的访问器方法是否为实例方法。若为 [YES](yes.md)，则访问器方法为实例方法。[YES](yes.md) 是属性唯一允许的值。因此，若将此值设为 [NO](no.md)，该属性将不会被添加到协议中。

## 讨论

要添加属性的协议必须处于构建中——已分配但尚未通过 [objc_registerProtocol](<objc_registerprotocol(__).md>) 函数向 Objective-C 运行时注册。

## 另请参阅

### Working with Protocols

- [objc_getProtocol](<objc_getprotocol(__).md>) — 返回指定的协议。
- [objc_copyProtocolList](<objc_copyprotocollist(__).md>) — 返回一个数组，包含 runtime 已知的所有协议。
- [objc_allocateProtocol](<objc_allocateprotocol(__).md>) — 创建一个新的协议实例。
- [objc_registerProtocol](<objc_registerprotocol(__).md>) — 向 Objective-C runtime 注册一个新创建的协议。
- [protocol_addMethodDescription](<protocol_addmethoddescription(__________).md>) — 向一个协议添加一个方法。
- [protocol_addProtocol](<protocol_addprotocol(____).md>) — 将一个已注册的协议添加到另一个正在构建中的协议。
- [protocol_getName](<protocol_getname(__).md>) — 返回一个协议的名称。
- [protocol_isEqual](<protocol_isequal(____).md>) — 返回一个布尔值，指示两个协议是否相等。
- [protocol_copyMethodDescriptionList](<protocol_copymethoddescriptionlist(________).md>) — 返回一个数组，包含给定协议中符合给定规范的方法的方法描述。
- [protocol_getMethodDescription](<protocol_getmethoddescription(________).md>) — 返回给定协议中指定方法的方法描述结构体。
- [protocol_copyPropertyList](<protocol_copypropertylist(____).md>) — 返回一个数组，包含某个协议声明的属性。
- [protocol_getProperty](<protocol_getproperty(________).md>) — 返回给定协议中指定的属性。
- [protocol_copyProtocolList](<protocol_copyprotocollist(____).md>) — 返回一个数组，包含某个协议采用的协议。
- [protocol_conformsToProtocol](<protocol_conformstoprotocol(____).md>) — 返回一个布尔值，指示一个协议是否符合另一个协议。
