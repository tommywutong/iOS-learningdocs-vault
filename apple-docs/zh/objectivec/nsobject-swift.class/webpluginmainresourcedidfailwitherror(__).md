---
title: 'webPlugInMainResourceDidFailWithError(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.6+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/webpluginmainresourcedidfailwitherror(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/webpluginmainresourcedidfailwitherror(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/webpluginmainresourcedidfailwitherror%28_%3A%29.json'
content_hash: 'sha256:7e4ee8c71ebb92b7'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# webPlugInMainResourceDidFailWithError(_:)

<sub>实例方法</sub>

在载入主资源发生错误时调用。

<sub>macOS</sub>

```swift
func webPlugInMainResourceDidFailWithError(_ error: (any Error)!)
```

## 参数

- `error` — 包含连接未能成功载入请求原因详情的错误对象。

## 讨论

当主资源底层的 `NSURLConnection` 对象向其委托发送 connection:didFailWithError: 消息时，会调用此消息。

## 另请参阅

### 主资源消息

- [- webPlugInMainResourceDidFinishLoading](<webpluginmainresourcedidfinishloading().md>) — 在连接成功完成载入数据时调用。
- [- webPlugInMainResourceDidReceiveData:](<webpluginmainresourcedidreceive(__)-5b6f6.md>) — 在连接增量载入数据时调用。
- [- webPlugInMainResourceDidReceiveResponse:](<webpluginmainresourcedidreceive(__)-6x7b9.md>) — 在连接收到足以构造其请求的 URL 响应的数据时调用。
