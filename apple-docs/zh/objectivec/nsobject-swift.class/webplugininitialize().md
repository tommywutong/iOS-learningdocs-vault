---
title: webPlugInInitialize()
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/webplugininitialize()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/webplugininitialize()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/webplugininitialize%28%29.json'
content_hash: 'sha256:547b8b3a088db8fc'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# webPlugInInitialize()

<sub>实例方法</sub>

初始化插件。

<sub>macOS</sub>

```swift
func webPlugInInitialize()
```

## 讨论

告知插件执行一次性初始化。每个插件对象实例在调用协议中的任何其他方法之前，必须且只能调用此方法一次。

## 另请参阅

### 控制插件

- [- webPlugInDestroy](<webplugindestroy().md>) — 为插件释放做准备。
- [- webPlugInStart](<webpluginstart().md>) — 告知插件开始正常运行。
- [- webPlugInStop](<webpluginstop().md>) — 告知插件停止正常运行。
