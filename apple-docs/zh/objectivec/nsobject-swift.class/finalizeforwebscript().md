---
title: finalizeForWebScript()
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/finalizeforwebscript()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/finalizeforwebscript()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/finalizeforwebscript%28%29.json'
content_hash: 'sha256:4cceff2eb3115dbe'
translated: true
---
> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# finalizeForWebScript()

<sub>实例方法</sub>

在脚本环境重置时执行清理。

<sub>macOS</sub>

```swift
func finalizeForWebScript()
```

## 讨论

此方法在脚本环境即将重置之前，对暴露给脚本环境的对象调用。调用后，接收对象将不再被脚本环境引用。对由该暴露对象创建的 `WebScriptObject` 实例的进一步引用将无效，并可能产生不可预测的结果。
