---
title: webPlugInMainResourceDidFinishLoading()
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.6+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/webpluginmainresourcedidfinishloading()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/webpluginmainresourcedidfinishloading()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/webpluginmainresourcedidfinishloading%28%29.json'
content_hash: 'sha256:c235510351fbc43a'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# webPlugInMainResourceDidFinishLoading()

<sub>实例方法</sub>

当连接成功完成数据加载时调用。

<sub>macOS</sub>

```swift
func webPlugInMainResourceDidFinishLoading()
```

## 讨论

当 `WebPlugInShouldLoadMainResourceKey` 插件命令行参数设为 [NO](../no.md)，且主资源的底层 `NSURLConnection` 对象成功完成数据加载时，会调用此消息。

## 另请参阅

### 主资源消息

- [- webPlugInMainResourceDidFailWithError:](<webpluginmainresourcedidfailwitherror(__).md>) — 在加载主资源时发生错误时被调用。
- [- webPlugInMainResourceDidReceiveData:](<webpluginmainresourcedidreceive(__)-5b6f6.md>) — 在连接接收到足够的数据以构造其请求的 URL 响应时被调用。
- [- webPlugInMainResourceDidReceiveResponse:](<webpluginmainresourcedidreceive(__)-6x7b9.md>) — 在连接接收到足够的数据以构造其请求的 URL 响应时被调用。
