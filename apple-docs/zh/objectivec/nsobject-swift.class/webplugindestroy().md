---
title: webPlugInDestroy()
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/webplugindestroy()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/webplugindestroy()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/webplugindestroy%28%29.json'
content_hash: 'sha256:32be07958249eade'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# webPlugInDestroy()

<sub>实例方法</sub>

为插件释放做准备。

<sub>macOS</sub>

```swift
func webPlugInDestroy()
```

## 讨论

通常，此方法会释放插件使用的内存和其他资源。例如，如果插件复制了 WebPlugInContainer 对象，此方法应放弃所有权。

## 另请参阅

### 控制插件

- [- webPlugInInitialize](<webplugininitialize().md>) — 初始化插件。
- [- webPlugInStart](<webpluginstart().md>) — 告知插件开始正常运行。
- [- webPlugInStop](<webpluginstop().md>) — 告知插件停止正常运行。
