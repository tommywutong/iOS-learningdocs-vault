---
title: WebPlugIn
framework: Objective-C Runtime
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/webplugin
source_url: 'https://developer.apple.com/documentation/objectivec/webplugin'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/webplugin.json'
content_hash: 'sha256:0c24d454f77cac65'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md) · [NSObject](nsobject-swift.class.md)

# WebPlugIn

<sub>API 集合</sub>

`WebPlugIn` 这个非正式协议定义了一些方法，使得使用 WebKit 框架的应用程序与其可能使用的任何基于 WebKit 的插件之间能够进行交互。

## Topics

### Accessing the Scripting Environment

- [objectForWebScript](nsobject-swift.class/objectforwebscript.md) — 返回一个对象，公开该插件的脚本编写接口。

### Using Plug-in State Information

- [- webPlugInSetIsSelected:](<nsobject-swift.class/webpluginsetisselected(__).md>) — 根据插件的选中状态控制其行为。

### Controlling the Plug-in

- [- webPlugInDestroy](<nsobject-swift.class/webplugindestroy().md>) — 为插件的释放做准备。
- [- webPlugInInitialize](<nsobject-swift.class/webplugininitialize().md>) — 初始化插件。
- [- webPlugInStart](<nsobject-swift.class/webpluginstart().md>) — 告知插件开始正常运行。
- [- webPlugInStop](<nsobject-swift.class/webpluginstop().md>) — 告知插件停止正常运行。

### Main resource messages

- [- webPlugInMainResourceDidFailWithError:](<nsobject-swift.class/webpluginmainresourcedidfailwitherror(__).md>) — 在加载主资源时发生错误时被调用。
- [- webPlugInMainResourceDidFinishLoading](<nsobject-swift.class/webpluginmainresourcedidfinishloading().md>) — 在连接成功完成数据加载时被调用。
- [- webPlugInMainResourceDidReceiveData:](<nsobject-swift.class/webpluginmainresourcedidreceive(__)-5b6f6.md>) — 在连接以增量方式加载数据时被调用。
- [- webPlugInMainResourceDidReceiveResponse:](<nsobject-swift.class/webpluginmainresourcedidreceive(__)-6x7b9.md>) — 在连接接收到足够的数据以构造其请求的 URL 响应时被调用。

## See Also

### Interacting with Web Plug-ins

- [WebPlugInContainer](webplugincontainer.md) — `WebPlugInContainer` 是一个非正式协议，使插件能够向应用程序发送消息。
