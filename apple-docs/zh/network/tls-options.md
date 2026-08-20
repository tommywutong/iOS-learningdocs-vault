---
title: TLS 选项
framework: Network
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/network/tls-options
source_url: 'https://developer.apple.com/documentation/network/tls-options'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/tls-options.json'
content_hash: 'sha256:a884cbf88e5f90f8'
translated: true
---

> 导航：[技术](../technologies.md) · [Network](../network.md)

# TLS 选项

<sub>API 集合</sub>

配置使用传输层安全协议（Transport Layer Security）的连接选项。

## 主题

### 创建 TLS 连接

- [nw_protocol_copy_tls_definition](<nw_protocol_copy_tls_definition().md>) — 访问传输层安全协议的系统定义。
- [nw_tls_create_options](<nw_tls_create_options().md>) — 初始化一组默认的 TLS 连接选项。
- [nw_tls_copy_sec_protocol_options](<nw_tls_copy_sec_protocol_options(__).md>) — 访问 TLS 将使用的握手安全选项。

### 检查 TLS 状态

- [nw_protocol_metadata_is_tls](<nw_protocol_metadata_is_tls(__).md>) — 检查元数据对象是否包含 TLS 连接状态。
- [nw_tls_copy_sec_protocol_metadata](<nw_tls_copy_sec_protocol_metadata(__).md>) — 访问 TLS 握手的结果。

## 另请参阅

### 网络协议

- [TCP 选项](tcp-options.md) — 配置使用传输控制协议（Transmission Control Protocol）的连接选项。
- [QUIC 选项](quic-options.md) — 配置使用 QUIC 传输协议的连接选项。
- [UDP 选项](udp-options.md) — 配置使用用户数据报协议（User Datagram Protocol）的连接选项。
- [IP 选项](ip-options.md) — 在连接上配置互联网协议（Internet Protocol）选项。
- [WebSocket 选项](websocket-options.md) — 配置使用 WebSocket 的连接选项。
- [Framer 协议选项](framer-protocol-options.md) — 创建自定义协议，在连接上为应用消息添加帧。
