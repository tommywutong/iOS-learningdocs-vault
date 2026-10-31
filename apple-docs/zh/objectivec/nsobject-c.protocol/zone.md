---
title: zone
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-c.protocol/zone
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-c.protocol/zone'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-c.protocol/zone.json'
content_hash: 'sha256:ddf6b7cb1646dbec'
translated: true
---


> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObjectProtocol](../nsobjectprotocol.md)

# zone

<sub>实例方法</sub>

Zone 已废弃，大多数将其作为参数的类都会忽略它。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (struct _NSZone *) zone;
```

## 返回值

指向分配接收者所用 zone 的指针。

## 另请参阅

### 过时方法

- [retain](retain.md) — 递增接收者的引用计数。
- [release](release.md) — 递减接收者的引用计数。
- [autorelease](autorelease.md) — 在当前自动释放池块结束时递减接收者的保留计数。
- [retainCount](retaincount.md) — 不要使用此方法。
