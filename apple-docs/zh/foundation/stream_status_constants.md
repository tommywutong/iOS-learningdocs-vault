---
title: 流状态常量
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/stream_status_constants
source_url: 'https://developer.apple.com/documentation/foundation/stream_status_constants'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/stream_status_constants.json'
content_hash: 'sha256:95babd18140eb624'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md) · [Streams, Sockets, and Ports](streams-sockets-and-ports.md) · [Stream](stream.md)

# 流状态常量

<sub>API 集合</sub>

这些常量表示流的当前状态。它们由 [streamStatus](stream/streamstatus.md) 返回。

## 主题

### 常量

- [NSStreamStatusNotOpen](stream/status/notopen.md) — 流未打开以进行读取或写入。此状态在底层打开流的调用之前、流创建之后返回。
- [NSStreamStatusOpening](stream/status/opening.md) — 流正在被打开以进行读取或写入。对于网络流，此状态可能包括流已打开但网络 DNS 解析仍在进行的时间段。
- [NSStreamStatusOpen](stream/status/open.md) — 流已打开，但没有读取或写入正在进行。
- [NSStreamStatusReading](stream/status/reading.md) — 正在从流中读取数据。如果另一线程上的代码在 [- read:maxLength:](<inputstream/read(__maxlength_).md>) 调用（[InputStream](inputstream.md)）进行期间对该流调用 [streamStatus](stream/streamstatus.md)，就会返回此状态。
- [NSStreamStatusWriting](stream/status/writing.md) — 正在向流中写入数据。如果另一线程上的代码在 [- write:maxLength:](<outputstream/write(__maxlength_).md>) 调用（[OutputStream](outputstream.md)）进行期间对该流调用 [streamStatus](stream/streamstatus.md)，就会返回此状态。
- [NSStreamStatusAtEnd](stream/status/atend.md) — 没有更多数据可读，或无法再向流写入数据。返回此状态时，流处于「非阻塞」模式且没有可用数据。
- [NSStreamStatusClosed](stream/status/closed.md) — 流已关闭（已对其调用 [- close](<stream/close().md>)）。
- [NSStreamStatusError](stream/status/error.md) — 连接的远端无法联系，或连接因其他原因被切断。

## 另请参阅

### 常量

- [Status](stream/status.md) — doc:stream/stream_status_constants 中所列常量声明的类型。
- [Event](stream/event.md) — 描述可能作为位域在 [- stream:handleEvent:](<streamdelegate/stream(__handle_).md>) 的第二个参数中发送给委托的常量，用于指定流事件的种类。
- [StreamNetworkServiceTypeValue](streamnetworkservicetypevalue.md) — `NSStream` 定义了这些字符串常量，用于指定流的服务类型。
- [StreamSOCKSProxyConfiguration](streamsocksproxyconfiguration.md)
- [StreamSOCKSProxyVersion](streamsocksproxyversion.md)
- [StreamSocketSecurityLevel](streamsocketsecuritylevel.md) — `NSStream` 定义了这些字符串常量，用于指定安全套接字层（SSL）安全级别。
- [PropertyKey](stream/propertykey.md) — `NSStream` 定义了这些字符串常量，作为使用 [- propertyForKey:](<stream/property(forkey_).md>) 访问流属性以及使用 [- setProperty:forKey:](<stream/setproperty(__forkey_).md>) 设置属性的键：
- [NSStreamSocketSSLErrorDomain](nsstreamsocketsslerrordomain.md) — `NSError` 报告 SSL 错误时使用的错误域。
- [NSStreamSOCKSErrorDomain](nsstreamsockserrordomain.md) — `NSError` 报告 SOCKS 错误时使用的错误域。
