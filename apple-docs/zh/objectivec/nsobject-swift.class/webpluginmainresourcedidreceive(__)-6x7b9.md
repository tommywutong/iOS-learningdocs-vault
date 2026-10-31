---
title: 'webPlugInMainResourceDidReceive(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.6+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/webpluginmainresourcedidreceive(_:)-6x7b9'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/webpluginmainresourcedidreceive(_:)-6x7b9'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/webpluginmainresourcedidreceive%28_%3A%29-6x7b9.json'
content_hash: 'sha256:e7f5503274926f71'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# webPlugInMainResourceDidReceive(_:)

<sub>实例方法</sub>

在连接收到足以构造其请求的 URL 响应的数据时调用。

<sub>macOS</sub>

```swift
func webPlugInMainResourceDidReceive(_ response: URLResponse!)
```

## 参数

- `response` — 连接请求的 URL 响应。

## 讨论

当 `WebPlugInShouldLoadMainResourceKey` 插件命令行参数设为 [NO](../no.md)，且主资源底层的 `NSURLConnection` 对象向其委托发送 connection:didReceiveResponse: 消息时，会调用此消息。

## 另请参阅

### 主资源消息

- [- webPlugInMainResourceDidFailWithError:](<webpluginmainresourcedidfailwitherror(__).md>) — 在载入主资源发生错误时调用。
- [- webPlugInMainResourceDidFinishLoading](<webpluginmainresourcedidfinishloading().md>) — 在连接成功完成载入数据时调用。
- [- webPlugInMainResourceDidReceiveData:](<webpluginmainresourcedidreceive(__)-5b6f6.md>) — 在连接增量载入数据时调用。
