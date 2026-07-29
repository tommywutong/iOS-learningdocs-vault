---
title: 使用安全套接字层进行网络通信
framework: Security
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/using-the-secure-socket-layer-for-network-communication
source_url: 'https://developer.apple.com/documentation/security/using-the-secure-socket-layer-for-network-communication'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/using-the-secure-socket-layer-for-network-communication.json'
content_hash: 'sha256:bf45f35d49736809'
translated: true
---

> 导航：[技术](../technologies.md) · [安全性](../security.md) · [Secure Transport](secure-transport.md)

# 使用安全套接字层进行网络通信

<sub>文章</sub>

建立安全套接字层（SSL）会话，以促进客户端与服务器之间的安全通信。

## 概述

以下术语在本讨论中使用：

- **客户端（Client）** — SSL 会话的发起方。客户端的一个典型例子是与 HTTPS URL 通信的网页浏览器。
- **服务器（Server）** — 接受客户端发起的 SSL 会话请求的实体。一个例子是安全网页服务器。
- **SSLSession** — 其存在范围由 [SSLHandshake](<sslhandshake(__).md>) 和 [SSLClose](<sslclose(__).md>) 函数的调用所界定。一个活动会话处在这两次调用之间的某种状态（含两端）。
- **SSLSessionContext** — 与一个会话相关联的状态。会话上下文不能用于多个会话。

大多数 App 仅需要此 API 中的少数几个函数，这些函数通常按以下顺序调用：

- 准备会话
- 调用 [SSLCreateContext](<sslcreatecontext(______).md>) 创建新的 SSL 会话上下文。
- 编写 [SSLWriteFunc](sslwritefunc.md) 和 [SSLReadFunc](sslreadfunc.md) 的 I/O 函数，并通过调用 [SSLSetIOFuncs](<sslsetiofuncs(______).md>) 函数将它们注册到 Secure Transport。
- 使用 [CFNetwork](../cfnetwork.md)、BSD Sockets 或 Open Transport 建立连接。然后调用 [SSLSetConnection](<sslsetconnection(____).md>) 指定该 SSL 会话上下文所应用的连接。
- 调用 [SSLSetPeerDomainName](<sslsetpeerdomainname(______).md>) 指定要连接的对端完全限定域名（可选，但强烈建议）。
- 调用 [SSLSetCertificate](<sslsetcertificate(____).md>) 指定用于身份验证的证书（服务器端必需，客户端可选）。
- 启动会话
- 调用 [SSLHandshake](<sslhandshake(__).md>) 执行 SSL 握手并建立安全会话。
- 维护会话
- 为了在安全会话上传输数据，Secure Transport 会根据需要调用你的 [SSLWrite](<sslwrite(________).md>) 和 [SSLRead](<sslread(________).md>) 函数。
- 结束会话
- 调用 [SSLClose](<sslclose(__).md>) 关闭安全会话。
- 关闭连接并释放连接引用。
- 通过调用 [CFRelease](../corefoundation/cfrelease.md) 释放 SSL 会话上下文。
- 如果你调用过 `SSLGetPeerCertificates` 获取任何证书，调用 [CFRelease](../corefoundation/cfrelease.md) 释放证书引用对象。

在许多情况下，使用 CFNetwork API 比使用 Secure Transport 更容易实现到安全（HTTPS）URL 的简单连接。有关 CFNetwork API 的文档以及从 URL 下载数据的代码示例，请参阅 [CFNetwork 编程指南](https://developer.apple.com/library/archive/documentation/Networking/Conceptual/CFNetwork/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001132) 和 CFNetworkHTTPDownload 示例代码。如果你指定 HTTPS URL，此例程会自动使用 Secure Transport 加密数据流。

有关管理和评估证书的函数，请参阅[证书、密钥和信任服务](certificate-key-and-trust-services.md)。
