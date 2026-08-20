---
title: 流编程指南
apple_id: 10000188i
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Networking, Internet, & Web
technology: Foundation
published: '2013-12-16'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Streams/Streams.html
archived_at: '2026-07-15T07:19:28.666307Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md)


[下一页](Cocoa%20Streams.md)

# Cocoa 流编程指南简介

流（stream）是编程中的一个基本抽象：从一个点串行传输到另一个点的比特序列。Cocoa 提供了三个类来表示流并方便你在程序中使用它们：NSStream、NSInputStream 和 NSOutputStream。借助这些类的实例，你可以从文件和应用程序内存中读取数据，也可以把数据写入其中。你还可以在基于套接字（socket）的连接中使用这些对象，与远程主机交换数据。此外，你可以派生这些流类的子类，以获得特定的流行为。

本文档包含以下文章：

- [Cocoa 流](Cocoa%20Streams.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi3telkcifbeurscijba) 概览 Cocoa 的流类，介绍其架构、能力和一般用法。
- [从输入流读取](Reading%20From%20Input%20Streams.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi3tglkcineuuscbi5ca) 说明如何创建并准备一个（非套接字的）输入流对象。文中还介绍了如何处理各类 NSInputStream 对象产生的流事件。
- [向输出流写入](Writing%20To%20Output%20Streams.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi3tilkciffegqkcijbq) 说明如何创建并准备一个（非套接字的）输出流对象。文中还介绍了如何处理各类 NSOutputStream 对象产生的流事件。
- [轮询与运行循环调度](Polling%20Versus%20Run-Loop%20Scheduling.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi3tklkdjjbekrceijdq) 讨论在读写流时用于避免阻塞的两种技术各自的优劣。文中还演示了如何使用流类的 API 轮询流数据。
- [处理流错误](Handling%20Stream%20Errors.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi3tmlkcineuircgjbda) 介绍如何处理流处理过程中发生的错误。
- [设置套接字流](Setting%20Up%20Socket%20Streams.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi3tolkcineuirsdireq) 说明如何设置用于通过套接字与远程主机通信的流对象。

如果你要实现基于套接字的网络流，以下外部资源可能会有帮助：

- OpenSSL — [http://www.openssl.org/](http://www.openssl.org/)
- Apache SSL — [http://www.apache-ssl.org/](http://www.apache-ssl.org/)
- SOCKS — [http://tools.ietf.org/html/rfc1928](http://tools.ietf.org/html/rfc1928)
[下一页](Cocoa%20Streams.md)

