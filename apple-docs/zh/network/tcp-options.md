---
title: TCP 选项
framework: Network
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/network/tcp-options
source_url: 'https://developer.apple.com/documentation/network/tcp-options'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/tcp-options.json'
content_hash: 'sha256:44ab537ab71b97d9'
translated: true
---

> 导航：[技术](../technologies.md) · [网络](../network.md)

# TCP 选项

<sub>API 集合</sub>

配置使用传输控制协议的连接的选项。

## 主题

### 创建 TCP 连接

- [nw_protocol_copy_tcp_definition](<nw_protocol_copy_tcp_definition().md>) — 访问传输控制协议的系统定义。
- [nw_tcp_create_options](<nw_tcp_create_options().md>) — 初始化一组默认的 TCP 连接选项。

### 自定义 TCP 选项

- [nw_tcp_options_set_enable_fast_open](<nw_tcp_options_set_enable_fast_open(____).md>) — 在连接上启用 TCP Fast Open。
- [nw_tcp_options_set_maximum_segment_size](<nw_tcp_options_set_maximum_segment_size(____).md>) — 设置 TCP 的最大分段大小（以字节为单位）。
- [nw_tcp_options_set_no_delay](<nw_tcp_options_set_no_delay(____).md>) — 为 TCP 禁用 Nagle 算法。
- [nw_tcp_options_set_no_options](<nw_tcp_options_set_no_options(____).md>) — 将 TCP 设置为无选项模式。
- [nw_tcp_options_set_no_push](<nw_tcp_options_set_no_push(____).md>) — 将 TCP 设置为无推送模式。
- [nw_tcp_options_set_retransmit_fin_drop](<nw_tcp_options_set_retransmit_fin_drop(____).md>) — 使 TCP 在 FIN 后未收到 ACK 时断开连接。
- [nw_tcp_options_set_disable_ack_stretching](<nw_tcp_options_set_disable_ack_stretching(____).md>) — 禁用 TCP 确认拉伸。
- [nw_tcp_options_set_disable_ecn](<nw_tcp_options_set_disable_ecn(____).md>) — 禁用显式拥塞通知标记的协商。

### 配置 Keepalive

- [nw_tcp_options_set_enable_keepalive](<nw_tcp_options_set_enable_keepalive(____).md>) — 启用 TCP keepalive。
- [nw_tcp_options_set_keepalive_idle_time](<nw_tcp_options_set_keepalive_idle_time(____).md>) — 设置 TCP 在发送 keepalive 探测包前等待的空闲秒数。
- [nw_tcp_options_set_keepalive_count](<nw_tcp_options_set_keepalive_count(____).md>) — 设置 TCP 在终止连接前发送的 keepalive 探测包数量。
- [nw_tcp_options_set_keepalive_interval](<nw_tcp_options_set_keepalive_interval(____).md>) — 设置 TCP 在发送 keepalive 探测包之间的等待秒数。

### 设置超时

- [nw_tcp_options_set_connection_timeout](<nw_tcp_options_set_connection_timeout(____).md>) — 设置 TCP 在握手超时前等待的秒数。
- [nw_tcp_options_set_retransmit_connection_drop_time](<nw_tcp_options_set_retransmit_connection_drop_time(____).md>) — 设置 TCP 在重传尝试之间等待的秒数。
- [nw_tcp_options_set_persist_timeout](<nw_tcp_options_set_persist_timeout(____).md>) — 按 RFC 6429 定义，设置 TCP 持久超时时间（以秒为单位）。

### 检查 TCP 状态

- [nw_protocol_metadata_is_tcp](<nw_protocol_metadata_is_tcp(__).md>) — 检查元数据对象是否包含 TCP 连接状态。
- [nw_tcp_get_available_send_buffer](<nw_tcp_get_available_send_buffer(__).md>) — 访问 TCP 发送缓冲区中的可用字节数。
- [nw_tcp_get_available_receive_buffer](<nw_tcp_get_available_receive_buffer(__).md>) — 访问 TCP 接收缓冲区中的可用字节数。

## 另请参阅

### 网络协议

- [TLS 选项](tls-options.md) — 配置使用传输层安全性协议的连接的选项。
- [QUIC 选项](quic-options.md) — 配置使用 QUIC 传输协议的连接的选项。
- [UDP 选项](udp-options.md) — 配置使用用户数据报协议的连接的选项。
- [IP 选项](ip-options.md) — 配置连接上的 Internet 协议选项。
- [WebSocket 选项](websocket-options.md) — 配置使用 WebSocket 的连接的选项。
- [Framer 协议选项](framer-protocol-options.md) — 创建自定义协议以在连接上对应用消息进行帧化。
