---
title: webPlugInStop()
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/webpluginstop()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/webpluginstop()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/webpluginstop%28%29.json'
content_hash: 'sha256:1fc73ac644d9bd3d'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# webPlugInStop()

<sub>实例方法</sub>

告知插件停止正常运行。

<sub>macOS</sub>

```swift
func webPlugInStop()
```

## 讨论

如果应用已调用 [- webPlugInInitialize](<webplugininitialize().md>)，且对此方法的每次调用之前都有对 [- webPlugInStart](<webpluginstart().md>) 的调用，则此方法可能会被调用多次。

## 另请参阅

### 控制插件

- [- webPlugInDestroy](<webplugindestroy().md>) — 为插件释放做准备。
- [- webPlugInInitialize](<webplugininitialize().md>) — 初始化插件。
- [- webPlugInStart](<webpluginstart().md>) — 告知插件开始正常运行。
