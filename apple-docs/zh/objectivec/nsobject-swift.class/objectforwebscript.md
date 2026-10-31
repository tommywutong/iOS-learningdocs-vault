---
title: objectForWebScript
framework: Objective-C Runtime
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/objectforwebscript
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/objectforwebscript'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/objectforwebscript.json'
content_hash: 'sha256:80aeaab219ee5f50'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# objectForWebScript

<sub>实例属性</sub>

返回暴露插件脚本接口的对象。

<sub>macOS</sub>

```swift
var objectForWebScript: Any! { get }
```

## 返回值

表示插件脚本接口的对象。

## 讨论

返回对象的方法会暴露给脚本环境。发送给返回对象的消息将在脚本环境中调用。参见 WebScripting Protocol Reference 了解详情。
