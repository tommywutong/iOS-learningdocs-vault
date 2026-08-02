# 模块 8：操作系统、网络与数据库基础

> 补齐进程线程、虚拟内存、网络协议和数据库索引等通用基础。
> 对应仓库范围：并发与线程、内存与 ARC、网络与安全、数据与持久化。中文正文优先，随后列出未翻译资料。

- [返回暑期计划知识地图](../summer.md)
- [查看全库主题地图](../topics.md)

## 学习步骤

| 步骤 | 内容 | 产出 |
|---|---|---|
| 操作系统 | 进程和线程；地址空间；虚拟内存；上下文切换；同步互斥；死锁；调度；小林 coding 一、三基础知识，重点看四五六 | 每个概念一句话 + 一个 iOS 对应例子 |
| 计网 | 小林 coding 计网部分看一遍；只看上三层：应用层、传输层、网络层；HTTP/HTTPS、TCP/UDP、IP；上网搜面试题 | 应用层/传输层/网络层三层关系图；每个基础概念一句话 |
| 数据库 | 基础特性、SQL 基础语法、`insert` 等 CRUD；事务；事务特性；数据库用什么数据结构实现 | 一页数据库最低面试清单；事务 + 索引实验 |

## 计划指定材料

- [计划材料](https://www.rfc-editor.org/rfc/rfc9110) — 第三方博客（未归档（rfc-editor.org））
- [计划材料](https://www.rfc-editor.org/rfc/rfc9293) — 第三方博客（未归档（rfc-editor.org））
- [计划材料](https://www.rfc-editor.org/rfc/rfc8200) — 第三方博客（未归档（rfc-editor.org））
- [计划材料](https://www.xiaolincoding.com/network/) — 第三方博客（未归档（xiaolincoding.com））
- [计划材料](https://www.xiaolincoding.com/network/2_http/http_interview.html) — 第三方博客（未归档（xiaolincoding.com））
- [计划材料](https://javaguide.cn/cs-basics/network/tcp-connection-and-disconnection.html) — 第三方博客（未归档（javaguide.cn））
- [计划材料](https://segmentfault.com/a/1190000022410446) — 第三方博客（未归档（segmentfault.com））
- [计划材料](https://www.xiaolincoding.com/network/2_http/http3.html) — 第三方博客（未归档（xiaolincoding.com））
- [简介](../../legacy-archive/vault/documentation/Cocoa/Threading%20Programming%20Guide/Introduction.md) · [原文网页](https://github.com/XiyouMobile3G-iOS/apple-developer-archive-vault/blob/main/documentation/Cocoa/Threading%20Programming%20Guide/Introduction.md) — Apple 旧归档
- [计划材料](https://www.xiaolincoding.com/os/) — 第三方博客（未归档（xiaolincoding.com））

## 中文资料

共 61 份。包含译文和原生中文文章。

| 优先级 | 文章 | 类型 | 来源 | 阅读 | 状态 |
|---|---|---|---|---|---|
| 计划核心 | [TCP 三次握手和四次挥手（传输层）](../../blogs/snapshots/javaguide.cn/tcp-%E4%B8%89%E6%AC%A1%E6%8F%A1%E6%89%8B%E5%92%8C%E5%9B%9B%E6%AC%A1%E6%8C%A5%E6%89%8B-%E4%BC%A0%E8%BE%93%E5%B1%82.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots/javaguide.cn/tcp-%E4%B8%89%E6%AC%A1%E6%8F%A1%E6%89%8B%E5%92%8C%E5%9B%9B%E6%AC%A1%E6%8C%A5%E6%89%8B-%E4%BC%A0%E8%BE%93%E5%B1%82.md) | 原生中文 |
| 计划核心 | [详解 TCP 三次握手、四次挥手，附带精美图解和超高频面试题](../../blogs/snapshots/segmentfault.com/%E8%AF%A6%E8%A7%A3-tcp-%E4%B8%89%E6%AC%A1%E6%8F%A1%E6%89%8B-%E5%9B%9B%E6%AC%A1%E6%8C%A5%E6%89%8B-%E9%99%84%E5%B8%A6%E7%B2%BE%E7%BE%8E%E5%9B%BE%E8%A7%A3%E5%92%8C%E8%B6%85%E9%AB%98%E9%A2%91%E9%9D%A2%E8%AF%95%E9%A2%98.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots/segmentfault.com/%E8%AF%A6%E8%A7%A3-tcp-%E4%B8%89%E6%AC%A1%E6%8F%A1%E6%89%8B-%E5%9B%9B%E6%AC%A1%E6%8C%A5%E6%89%8B-%E9%99%84%E5%B8%A6%E7%B2%BE%E7%BE%8E%E5%9B%BE%E8%A7%A3%E5%92%8C%E8%B6%85%E9%AB%98%E9%A2%91%E9%9D%A2%E8%AF%95%E9%A2%98.md) | 原生中文 |
| 官方资料 | [TCP 选项](../../apple-docs/zh/network/tcp-options.md) | Apple 文档 | Apple · Network | [中文](../../apple-docs/zh/network/tcp-options.md) | 已翻译 |
| 官方资料 | [为 HTTP Live Streaming 编写分片 MPEG-4 文件](../../apple-docs/zh/avfoundation/writing-fragmented-mpeg-4-files-for-http-live-streaming.md) | Apple 文档 | Apple · AVFoundation | [中文](../../apple-docs/zh/avfoundation/writing-fragmented-mpeg-4-files-for-http-live-streaming.md) | 已翻译 |
| 官方资料 | [为局域网 TLS 创建身份](../../apple-docs/zh/network/creating-an-identity-for-local-network-tls.md) | Apple 文档 | Apple · Network | [中文](../../apple-docs/zh/network/creating-an-identity-for-local-network-tls.md) | 已翻译 |
| 官方资料 | [使用 AVFoundation 播放和存储 HTTP Live Stream](../../apple-docs/zh/avfoundation/using-avfoundation-to-play-and-persist-http-live-streams.md) | Apple 文档 | Apple · AVFoundation | [中文](../../apple-docs/zh/avfoundation/using-avfoundation-to-play-and-persist-http-live-streams.md) | 已翻译 |
| 官方资料 | [使用 CFNetwork 诊断日志调试 HTTPS 问题](../../apple-docs/zh/network/debugging-https-problems-with-cfnetwork-diagnostic-logging.md) | Apple 文档 | Apple · Network | [中文](../../apple-docs/zh/network/debugging-https-problems-with-cfnetwork-diagnostic-logging.md) | 已翻译 |
| 官方资料 | [使用 Instruments 分析 HTTP 流量](../../apple-docs/zh/foundation/analyzing-http-traffic-with-instruments.md) | Apple 文档 | Apple · Foundation | [中文](../../apple-docs/zh/foundation/analyzing-http-traffic-with-instruments.md) | 已翻译 |
| 官方资料 | [使用 Multipath TCP 提升网络可靠性](../../apple-docs/zh/foundation/improving-network-reliability-using-multipath-tcp.md) | Apple 文档 | Apple · Foundation | [中文](../../apple-docs/zh/foundation/improving-network-reliability-using-multipath-tcp.md) | 已翻译 |
| 官方资料 | [使用 Network Framework 实现 netcat](../../apple-docs/zh/network/implementing-netcat-with-network-framework.md) | Apple 文档 | Apple · Network | [中文](../../apple-docs/zh/network/implementing-netcat-with-network-framework.md) | 已翻译 |
| 官方资料 | [使用安全套接字层进行网络通信](../../apple-docs/zh/security/using-the-secure-socket-layer-for-network-communication.md) | Apple 文档 | Apple · Security | [中文](../../apple-docs/zh/security/using-the-secure-socket-layer-for-network-communication.md) | 已翻译 |
| 官方资料 | [创建线程（Thread）与线程组（Threadgroup）](../../apple-docs/zh/metal/creating-threads-and-threadgroups.md) | Apple 文档 | Apple · Metal | [中文](../../apple-docs/zh/metal/creating-threads-and-threadgroups.md) | 已翻译 |
| 官方资料 | [利用第三方网络调试工具](../../apple-docs/zh/network/taking-advantage-of-third-party-network-debugging-tools.md) | Apple 文档 | Apple · Network | [中文](../../apple-docs/zh/network/taking-advantage-of-third-party-network-debugging-tools.md) | 已翻译 |
| 官方资料 | [尽早诊断内存、线程和崩溃问题](../../apple-docs/zh/xcode/diagnosing-memory-thread-and-crash-issues-early.md) | Apple 文档 | Apple · xcode | [中文](../../apple-docs/zh/xcode/diagnosing-memory-thread-and-crash-issues-early.md) | 已翻译 |
| 官方资料 | [收集网络连接指标](../../apple-docs/zh/network/collecting-network-connection-metrics.md) | Apple 文档 | Apple · Network | [中文](../../apple-docs/zh/network/collecting-network-connection-metrics.md) | 已翻译 |
| 官方资料 | [流、Socket 与端口](../../apple-docs/zh/foundation/streams-sockets-and-ports.md) | Apple 文档 | Apple · Foundation | [中文](../../apple-docs/zh/foundation/streams-sockets-and-ports.md) | 已翻译 |
| 官方资料 | [线程泄漏](../../apple-docs/zh/xcode/thread-leaks.md) | Apple 文档 | Apple · xcode | [中文](../../apple-docs/zh/xcode/thread-leaks.md) | 已翻译 |
| 官方资料 | [网络与通信](../../apple-docs/zh/technologyoverviews/networking-and-communication.md) | Apple 文档 | Apple · Technology Overviews | [中文](../../apple-docs/zh/technologyoverviews/networking-and-communication.md) | 已翻译 |
| 官方资料 | [训练一个神经网络以实时渲染辐照度](../../apple-docs/zh/metal/training-a-neural-network-to-render-irradiance-in-real-time.md) | Apple 文档 | Apple · Metal | [中文](../../apple-docs/zh/metal/training-a-neural-network-to-render-irradiance-in-real-time.md) | 已翻译 |
| 官方资料 | [进程与线程](../../apple-docs/zh/foundation/processes-and-threads.md) | Apple 文档 | Apple · Foundation | [中文](../../apple-docs/zh/foundation/processes-and-threads.md) | 已翻译 |
| 官方资料 | [选择网络调试工具](../../apple-docs/zh/network/choosing-a-network-debugging-tool.md) | Apple 文档 | Apple · Network | [中文](../../apple-docs/zh/network/choosing-a-network-debugging-tool.md) | 已翻译 |
| 官方资料 | [配置网络扩展](../../apple-docs/zh/xcode/configuring-network-extensions.md) | Apple 文档 | Apple · xcode | [中文](../../apple-docs/zh/xcode/configuring-network-extensions.md) | 已翻译 |
| 官方资料 | [防止不安全的网络连接](../../apple-docs/zh/security/preventing-insecure-network-connections.md) | Apple 文档 | Apple · Security | [中文](../../apple-docs/zh/security/preventing-insecure-network-connections.md) | 已翻译 |
| 官方资料 | [降低网络和蓝牙的功耗](../../apple-docs/zh/xcode/reducing-networking-and-bluetooth-power-usage.md) | Apple 文档 | Apple · xcode | [中文](../../apple-docs/zh/xcode/reducing-networking-and-bluetooth-power-usage.md) | 已翻译 |
| 官方资料 | [使用现代网络技术提升性能与安全性](../../wwdc/zh/wwdc2020/10111-boost-performance-and-security-with-modern-networking.md) | WWDC | Apple · WWDC2020 | [中文](../../wwdc/zh/wwdc2020/10111-boost-performance-and-security-with-modern-networking.md) | 已翻译 |
| 官方资料 | [在 Instruments 中分析 HTTP 流量](../../wwdc/zh/wwdc2021/10212-analyze-http-traffic-in-instruments.md) | WWDC | Apple · WWDC2021 | [中文](../../wwdc/zh/wwdc2021/10212-analyze-http-traffic-in-instruments.md) | 已翻译 |
| 官方资料 | [在 Network framework 中使用结构化并发](../../wwdc/zh/wwdc2025/250-use-structured-concurrency-with-network-framework.md) | WWDC | Apple · WWDC2025 | [中文](../../wwdc/zh/wwdc2025/250-use-structured-concurrency-with-network-framework.md) | 已翻译 |
| 官方资料 | [网络技术进展，第 2 部分](../../wwdc/zh/wwdc2019/713-advances-in-networking-part-2.md) | WWDC | Apple · WWDC2019 | [中文](../../wwdc/zh/wwdc2019/713-advances-in-networking-part-2.md) | 已翻译 |
| 官方资料 | [网络技术进展，第一部分](../../wwdc/zh/wwdc2019/712-advances-in-networking-part-1.md) | WWDC | Apple · WWDC2019 | [中文](../../wwdc/zh/wwdc2019/712-advances-in-networking-part-1.md) | 已翻译 |
| 官方资料 | [认识 Network.framework：一种现代的 Sockets 替代方案](../../wwdc/zh/wwdc2018/715-introducing-network-framework-a-modern-alternative-to-sockets.md) | WWDC | Apple · WWDC2018 | [中文](../../wwdc/zh/wwdc2018/715-introducing-network-framework-a-modern-alternative-to-sockets.md) | 已翻译 |
| 深度补充 | [Cocoa 中一个简单可扩展的 HTTP 服务器](../../blogs/zh/cocoawithlove/a-simple-extensible-http-server-in-cocoa-cocoa-with-love.md) | 技术博客 | Cocoa with Love (Matt Gallagher) | [中文](../../blogs/zh/cocoawithlove/a-simple-extensible-http-server-in-cocoa-cocoa-with-love.md) | 已翻译 |
| 深度补充 | [Core Data 与数据库的区别 \| Cocoa with Love](../../blogs/zh/cocoawithlove/the-differences-between-core-data-and-a-database-cocoa-with-love.md) | 技术博客 | Cocoa with Love (Matt Gallagher) | [中文](../../blogs/zh/cocoawithlove/the-differences-between-core-data-and-a-database-cocoa-with-love.md) | 已翻译 |
| 深度补充 | [iPhone OS 设备上的网络数据需求 \| Cocoa with Love](../../blogs/zh/cocoawithlove/network-data-requirements-on-iphone-os-devices-cocoa-with-love.md) | 技术博客 | Cocoa with Love (Matt Gallagher) | [中文](../../blogs/zh/cocoawithlove/network-data-requirements-on-iphone-os-devices-cocoa-with-love.md) | 已翻译 |
| 深度补充 | [关于 Swift 中锁和线程安全的文章](../../blogs/zh/mikeash/an-article-about-locks-and-thread-safety-in-swift.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/an-article-about-locks-and-thread-safety-in-swift.md) | 已翻译 |
| 深度补充 | [内存和线程安全的自定义属性方法 \| Cocoa with Love](../../blogs/zh/cocoawithlove/memory-and-thread-safe-custom-property-methods-cocoa-with-love.md) | 技术博客 | Cocoa with Love (Matt Gallagher) | [中文](../../blogs/zh/cocoawithlove/memory-and-thread-safe-custom-property-methods-cocoa-with-love.md) | 已翻译 |
| 深度补充 | [大小问题：iOS 虚拟内存探究](../../blogs/zh/alwaysprocessing/size-matters-an-exploration-of-virtual-memory-on-ios-an-out-of-memory-crash-while-debuggin.md) | 技术博客 | Always Processing (Brian T. Kelley) | [中文](../../blogs/zh/alwaysprocessing/size-matters-an-exploration-of-virtual-memory-on-ios-an-out-of-memory-crash-while-debuggin.md) | 已翻译 |
| 深度补充 | [安全的线程化设计与线程间通信](../../blogs/zh/cocoawithlove/safe-threaded-design-and-inter-thread-communication-cocoa-with-love.md) | 技术博客 | Cocoa with Love (Matt Gallagher) | [中文](../../blogs/zh/cocoawithlove/safe-threaded-design-and-inter-thread-communication-cocoa-with-love.md) | 已翻译 |
| 深度补充 | [星期五问答 2009-06-19：Mac OS X 进程内存统计](../../blogs/zh/mikeash/friday-q-a-2009-06-19-mac-os-x-process-memory-statistics.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/friday-q-a-2009-06-19-mac-os-x-process-memory-statistics.md) | 已翻译 |
| 深度补充 | [星期五问答 2009-12-11：一个 GCD 案例研究：构建 HTTP 服务器](../../blogs/zh/mikeash/friday-q-a-2009-12-11-a-gcd-case-study-building-an-http-server.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/friday-q-a-2009-12-11-a-gcd-case-study-building-an-http-server.md) | 已翻译 |
| 深度补充 | [星期五问答 2013-12-06：网络协议设计](../../blogs/zh/mikeash/friday-q-a-2013-12-06-network-protocol-design.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/friday-q-a-2013-12-06-network-protocol-design.md) | 已翻译 |
| 深度补充 | [星期五问答 2014-03-14：Sockets API 入门](../../blogs/zh/mikeash/friday-q-a-2014-03-14-introduction-to-the-sockets-api.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/friday-q-a-2014-03-14-introduction-to-the-sockets-api.md) | 已翻译 |
| 深度补充 | [星期五问答 2017-10-27：锁、线程安全与 Swift：2017 版](../../blogs/zh/mikeash/friday-q-a-2017-10-27-locks-thread-safety-and-swift-2017-edition.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/friday-q-a-2017-10-27-locks-thread-safety-and-swift-2017-edition.md) | 已翻译 |
| 深度补充 | [生成线程的开销（性能实验） \| Cocoa with Love](../../blogs/zh/cocoawithlove/the-overhead-of-spawning-threads-a-performance-experiment-cocoa-with-love.md) | 技术博客 | Cocoa with Love (Matt Gallagher) | [中文](../../blogs/zh/cocoawithlove/the-overhead-of-spawning-threads-a-performance-experiment-cocoa-with-love.md) | 已翻译 |
| 深度补充 | [由 HTTP 数据驱动的 Cocoa 应用程序](../../blogs/zh/cocoawithlove/a-cocoa-application-driven-by-http-data-cocoa-with-love.md) | 技术博客 | Cocoa with Love (Matt Gallagher) | [中文](../../blogs/zh/cocoawithlove/a-cocoa-application-driven-by-http-data-cocoa-with-love.md) | 已翻译 |
| 深度补充 | [网络链路调节器](../../blogs/zh/nshipster/network-link-conditioner.md) | 技术博客 | NSHipster (Mattt) | [中文](../../blogs/zh/nshipster/network-link-conditioner.md) | 已翻译 |
| 深度补充 | [通过 HTTP 获取并解析 XML 或 JSON 的类](../../blogs/zh/cocoawithlove/classes-for-fetching-and-parsing-xml-or-json-via-http-cocoa-with-love.md) | 技术博客 | Cocoa with Love (Matt Gallagher) | [中文](../../blogs/zh/cocoawithlove/classes-for-fetching-and-parsing-xml-or-json-via-http-cocoa-with-love.md) | 已翻译 |
| 深度补充 | [Android 中的 SQLite 数据库支持](../../blogs/zh/objccn/android-%E4%B8%AD%E7%9A%84-sqlite-%E6%95%B0%E6%8D%AE%E5%BA%93%E6%94%AF%E6%8C%81.md) | 技术博客 | ObjC 中国 (objccn.io) | [中文](../../blogs/zh/objccn/android-%E4%B8%AD%E7%9A%84-sqlite-%E6%95%B0%E6%8D%AE%E5%BA%93%E6%94%AF%E6%8C%81.md) | 原生中文 |
| 深度补充 | [Core Data 网络应用实例](../../blogs/zh/objccn/core-data-%E7%BD%91%E7%BB%9C%E5%BA%94%E7%94%A8%E5%AE%9E%E4%BE%8B.md) | 技术博客 | ObjC 中国 (objccn.io) | [中文](../../blogs/zh/objccn/core-data-%E7%BD%91%E7%BB%9C%E5%BA%94%E7%94%A8%E5%AE%9E%E4%BE%8B.md) | 原生中文 |
| 深度补充 | [IP，TCP 和 HTTP](../../blogs/zh/objccn/ip-tcp-%E5%92%8C-http.md) | 技术博客 | ObjC 中国 (objccn.io) | [中文](../../blogs/zh/objccn/ip-tcp-%E5%92%8C-http.md) | 原生中文 |
| 深度补充 | [用 SQLite 和 FMDB 替代 Core Data](../../blogs/zh/objccn/%E7%94%A8-sqlite-%E5%92%8C-fmdb-%E6%9B%BF%E4%BB%A3-core-data.md) | 技术博客 | ObjC 中国 (objccn.io) | [中文](../../blogs/zh/objccn/%E7%94%A8-sqlite-%E5%92%8C-fmdb-%E6%9B%BF%E4%BB%A3-core-data.md) | 原生中文 |
| 补充资料 | [[objc 解析]: 线程本地垃圾回收](../../blogs/zh/sealiesoftware/objc-explain-thread-local-garbage-collection.md) | 技术博客 | Hamster Emporium (Greg Parker) | [中文](../../blogs/zh/sealiesoftware/objc-explain-thread-local-garbage-collection.md) | 已翻译 |
| 补充资料 | [《 Web 性能权威指南》阅读笔记-HTTP](../../blogs/zh/dirtmelon/web-%E6%80%A7%E8%83%BD%E6%9D%83%E5%A8%81%E6%8C%87%E5%8D%97-%E9%98%85%E8%AF%BB%E7%AC%94%E8%AE%B0-http.md) | 技术博客 | dirtmelon | [中文](../../blogs/zh/dirtmelon/web-%E6%80%A7%E8%83%BD%E6%9D%83%E5%A8%81%E6%8C%87%E5%8D%97-%E9%98%85%E8%AF%BB%E7%AC%94%E8%AE%B0-http.md) | 原生中文 |
| 补充资料 | [为 Instagram 和 Threads 带来 HDR 照片支持](../../blogs/zh/fbeng/bringing-hdr-photo-support-to-instagram-and-threads.md) | 技术博客 | Meta Engineering — iOS | [中文](../../blogs/zh/fbeng/bringing-hdr-photo-support-to-instagram-and-threads.md) | 已翻译 |
| 补充资料 | [使用 SQLite Magellan 漏洞让 Chrome 70 崩溃](../../blogs/zh/worthdoingbadly/crash-chrome-70-with-the-sqlite-magellan-bug.md) | 技术博客 | worthdoingbadly (Zhuowei Zhang) | [中文](../../blogs/zh/worthdoingbadly/crash-chrome-70-with-the-sqlite-magellan-bug.md) | 已翻译 |
| 补充资料 | [协议扩展中的方法派发](../../blogs/zh/oleb/method-dispatch-in-protocol-extensions.md) | 技术博客 | Ole Begemann | [中文](../../blogs/zh/oleb/method-dispatch-in-protocol-extensions.md) | 已翻译 |
| 补充资料 | [在 iOS 上实现主线程看门狗](../../blogs/zh/jessesquires/implementing-a-main-thread-watchdog-on-ios.md) | 技术博客 | Jesse Squires | [中文](../../blogs/zh/jessesquires/implementing-a-main-thread-watchdog-on-ios.md) | 已翻译 |
| 补充资料 | [如何制作 Core Data SQLite 数据库的副本](../../blogs/zh/oleb/how-to-make-a-copy-of-a-core-data-sqlite-database.md) | 技术博客 | Ole Begemann | [中文](../../blogs/zh/oleb/how-to-make-a-copy-of-a-core-data-sqlite-database.md) | 已翻译 |
| 补充资料 | [我们如何看待 Threads 的 iOS 性能](../../blogs/zh/fbeng/how-we-think-about-threads-ios-performance.md) | 技术博客 | Meta Engineering — iOS | [中文](../../blogs/zh/fbeng/how-we-think-about-threads-ios-performance.md) | 已翻译 |
| 补充资料 | [管理网络活动指示器](../../blogs/zh/oleb/managing-the-network-activity-indicator.md) | 技术博客 | Ole Begemann | [中文](../../blogs/zh/oleb/managing-the-network-activity-indicator.md) | 已翻译 |
| 补充资料 | [线程局部存储详解](../../blogs/zh/maskray/all-about-thread-local-storage.md) | 技术博客 | MaskRay (宋方睿) | [中文](../../blogs/zh/maskray/all-about-thread-local-storage.md) | 已翻译 |
| 补充资料 | [探索 SQLite 的内部机制](../../blogs/snapshots-zh/bswanson.dev/exploring-sqlite-s-internals.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots-zh/bswanson.dev/exploring-sqlite-s-internals.md) | 已翻译 |

## 未翻译资料

共 43 份。可能已有中文目录标题，但正文仍为英文。

| 优先级 | 文章 | 类型 | 来源 | 阅读 | 状态 |
|---|---|---|---|---|---|
| 官方资料 | [Ad network attribution](../../apple-docs/en/storekit/ad-network-attribution.md) | Apple 文档 | Apple · StoreKit | [英文](../../apple-docs/en/storekit/ad-network-attribution.md) | 待翻译 |
| 官方资料 | [Ad network install-validation keys](../../apple-docs/en/storekit/ad-network-install-validation-keys.md) | Apple 文档 | Apple · StoreKit | [英文](../../apple-docs/en/storekit/ad-network-install-validation-keys.md) | 待翻译 |
| 官方资料 | [Batch processing](../../apple-docs/en/coredata/batch-processing.md) | Apple 文档 | Apple · Core Data | [英文](../../apple-docs/en/coredata/batch-processing.md) | 待翻译 |
| 官方资料 | [CFStream Socket Security Level Constants](../../apple-docs/en/corefoundation/cfstream-socket-security-level-constants.md) | Apple 文档 | Apple · Core Foundation | [英文](../../apple-docs/en/corefoundation/cfstream-socket-security-level-constants.md) | 待翻译 |
| 官方资料 | [Connecting iPadOS and visionOS apps over the local network](../../apple-docs/en/visionos/connecting-ipados-and-visionos-apps-over-the-local-network.md) | Apple 文档 | Apple · network | [英文](../../apple-docs/en/visionos/connecting-ipados-and-visionos-apps-over-the-local-network.md) | 待翻译 |
| 官方资料 | [Customizing the Xcode archive process](../../apple-docs/en/security/customizing-the-xcode-archive-process.md) | Apple 文档 | Apple · Security | [英文](../../apple-docs/en/security/customizing-the-xcode-archive-process.md) | 待翻译 |
| 官方资料 | [Debugging HTTP Server-Side Errors](../../apple-docs/en/network/debugging-http-server-side-errors.md) | Apple 文档 | Apple · Network | [英文](../../apple-docs/en/network/debugging-http-server-side-errors.md) | 待翻译 |
| 官方资料 | [Hardware, networking, and sensors](../../apple-docs/en/technologyoverviews/hardware-networking-sensors.md) | Apple 文档 | Apple · Technology Overviews | [英文](../../apple-docs/en/technologyoverviews/hardware-networking-sensors.md) | 待翻译 |
| 官方资料 | [HTTP URL Properties](../../apple-docs/en/corefoundation/http-url-properties.md) | Apple 文档 | Apple · Core Foundation | [英文](../../apple-docs/en/corefoundation/http-url-properties.md) | 待翻译 |
| 官方资料 | [Indicating the source of network activity](../../apple-docs/en/network/indicating-the-source-of-network-activity.md) | Apple 文档 | Apple · Network | [英文](../../apple-docs/en/network/indicating-the-source-of-network-activity.md) | 待翻译 |
| 官方资料 | [Making network requests in a widget extension](../../apple-docs/en/widgetkit/making-network-requests-in-a-widget-extension.md) | Apple 文档 | Apple · WidgetKit | [英文](../../apple-docs/en/widgetkit/making-network-requests-in-a-widget-extension.md) | 待翻译 |
| 官方资料 | [Network](../../apple-docs/en/network.md) | Apple 文档 | Apple · Network | [英文](../../apple-docs/en/network.md) | 待翻译 |
| 官方资料 | [Network](../../apple-docs/en/kernel/hardware_families/network.md) | Apple 文档 | Apple · Kernel | [英文](../../apple-docs/en/kernel/hardware_families/network.md) | 待翻译 |
| 官方资料 | [Network Constants](../../apple-docs/en/network/network-constants.md) | Apple 文档 | Apple · Network | [英文](../../apple-docs/en/network/network-constants.md) | 待翻译 |
| 官方资料 | [Network Data Types](../../apple-docs/en/network/network-data-types.md) | Apple 文档 | Apple · Network | [英文](../../apple-docs/en/network/network-data-types.md) | 待翻译 |
| 官方资料 | [Network Enumerations](../../apple-docs/en/network/network-enumerations.md) | Apple 文档 | Apple · Network | [英文](../../apple-docs/en/network/network-enumerations.md) | 待翻译 |
| 官方资料 | [Network Extension](../../apple-docs/en/networkextension.md) | Apple 文档 | Apple · Network Extension | [英文](../../apple-docs/en/networkextension.md) | 待翻译 |
| 官方资料 | [Network Extension updates](../../apple-docs/en/updates/networkextension.md) | Apple 文档 | Apple · Updates | [英文](../../apple-docs/en/updates/networkextension.md) | 待翻译 |
| 官方资料 | [Network Functions](../../apple-docs/en/network/network-functions.md) | Apple 文档 | Apple · Network | [英文](../../apple-docs/en/network/network-functions.md) | 待翻译 |
| 官方资料 | [Network Macros](../../apple-docs/en/network/network-macros.md) | Apple 文档 | Apple · Network | [英文](../../apple-docs/en/network/network-macros.md) | 待翻译 |
| 官方资料 | [Network updates](../../apple-docs/en/updates/network.md) | Apple 文档 | Apple · Updates | [英文](../../apple-docs/en/updates/network.md) | 待翻译 |
| 官方资料 | [Policy Database Constants](../../apple-docs/en/security/policy-database-constants.md) | Apple 文档 | Apple · Security | [英文](../../apple-docs/en/security/policy-database-constants.md) | 待翻译 |
| 官方资料 | [Registering an ad network](../../apple-docs/en/storekit/registering-an-ad-network.md) | Apple 文档 | Apple · StoreKit | [英文](../../apple-docs/en/storekit/registering-an-ad-network.md) | 待翻译 |
| 官方资料 | [Secure Sockets (SOCKS) Errors](../../apple-docs/en/cfnetwork/1518266-secure-sockets-socks-errors.md) | Apple 文档 | Apple · CFNetwork | [英文](../../apple-docs/en/cfnetwork/1518266-secure-sockets-socks-errors.md) | 待翻译 |
| 官方资料 | [SKAdNetwork 1 release notes](../../apple-docs/en/storekit/skadnetwork-1-release-notes.md) | Apple 文档 | Apple · StoreKit | [英文](../../apple-docs/en/storekit/skadnetwork-1-release-notes.md) | 待翻译 |
| 官方资料 | [SKAdNetwork 2 release notes](../../apple-docs/en/storekit/skadnetwork-2-release-notes.md) | Apple 文档 | Apple · StoreKit | [英文](../../apple-docs/en/storekit/skadnetwork-2-release-notes.md) | 待翻译 |
| 官方资料 | [SKAdNetwork 2.1 release notes](../../apple-docs/en/storekit/skadnetwork-2-1-release-notes.md) | Apple 文档 | Apple · StoreKit | [英文](../../apple-docs/en/storekit/skadnetwork-2-1-release-notes.md) | 待翻译 |
| 官方资料 | [SKAdNetwork 2.2 release notes](../../apple-docs/en/storekit/skadnetwork-2-2-release-notes.md) | Apple 文档 | Apple · StoreKit | [英文](../../apple-docs/en/storekit/skadnetwork-2-2-release-notes.md) | 待翻译 |
| 官方资料 | [SKAdNetwork 3 release notes](../../apple-docs/en/storekit/skadnetwork-3-release-notes.md) | Apple 文档 | Apple · StoreKit | [英文](../../apple-docs/en/storekit/skadnetwork-3-release-notes.md) | 待翻译 |
| 官方资料 | [SKAdNetwork 4 release notes](../../apple-docs/en/storekit/skadnetwork-4-release-notes.md) | Apple 文档 | Apple · StoreKit | [英文](../../apple-docs/en/storekit/skadnetwork-4-release-notes.md) | 待翻译 |
| 官方资料 | [SKAdNetwork release notes](../../apple-docs/en/storekit/skadnetwork-release-notes.md) | Apple 文档 | Apple · StoreKit | [英文](../../apple-docs/en/storekit/skadnetwork-release-notes.md) | 待翻译 |
| 官方资料 | [Socket Name Server Utilities](../../apple-docs/en/corefoundation/socket-name-server-utilities.md) | Apple 文档 | Apple · Core Foundation | [英文](../../apple-docs/en/corefoundation/socket-name-server-utilities.md) | 待翻译 |
| 官方资料 | [UDP Options](../../apple-docs/en/network/udp-options.md) | Apple 文档 | Apple · Network | [英文](../../apple-docs/en/network/udp-options.md) | 待翻译 |
| 官方资料 | [WebSocket Options](../../apple-docs/en/network/websocket-options.md) | Apple 文档 | Apple · Network | [英文](../../apple-docs/en/network/websocket-options.md) | 待翻译 |
| 深度补充 | [Android 中的 SQLite 数据库支持](../../blogs/en/objcio/sqlite-database-support-in-android.md) | 技术博客 | objc.io | [英文](../../blogs/en/objcio/sqlite-database-support-in-android.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [IP、TCP 和 HTTP](../../blogs/en/objcio/ip-tcp-and-http.md) | 技术博客 | objc.io | [英文](../../blogs/en/objcio/ip-tcp-and-http.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [使用 SQLite 和 FMDB 替代 Core Data](../../blogs/en/objcio/on-using-sqlite-and-fmdb-instead-of-core-data.md) | 技术博客 | objc.io | [英文](../../blogs/en/objcio/on-using-sqlite-and-fmdb-instead-of-core-data.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [线程安全的类设计](../../blogs/en/objcio/thread-safe-class-design.md) | 技术博客 | objc.io | [英文](../../blogs/en/objcio/thread-safe-class-design.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [联网的 Core Data 应用程序](../../blogs/en/objcio/a-networked-core-data-application.md) | 技术博客 | objc.io | [英文](../../blogs/en/objcio/a-networked-core-data-application.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [Meta 如何在 5 个月内构建 Threads](../../blogs/en/fbeng/how-meta-built-threads-in-5-months.md) | 技术博客 | Meta Engineering — iOS | [英文](../../blogs/en/fbeng/how-meta-built-threads-in-5-months.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [家庭网络布线](../../blogs/en/saagarjha/wiring-your-house-for-networking.md) | 技术博客 | Saagar Jha | [英文](../../blogs/en/saagarjha/wiring-your-house-for-networking.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [新 HTTP QUERY 方法详解 \| Kreya](../../blogs/en/kreya/the-new-http-query-method-explained-kreya.md) | 技术博客 | Kreya Blog | [英文](../../blogs/en/kreya/the-new-http-query-method-explained-kreya.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [零设备成本研究 VoLTE/VoWiFi：通过 Wi-Fi 通话搭建电话网络](../../blogs/en/worthdoingbadly/volte-vowifi-research-with-0-of-equipment-set-up-a-phone-network-over-wi-fi-calling.md) | 技术博客 | worthdoingbadly (Zhuowei Zhang) | [英文](../../blogs/en/worthdoingbadly/volte-vowifi-research-with-0-of-equipment-set-up-a-phone-network-over-wi-fi-calling.md) | 仅标题中文，正文待翻译 |
