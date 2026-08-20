---
title: Bonjour 概述
apple_id: 10000119i
resource_type: Guide
platform: iOS|macOS
topic: Networking, Internet, & Web
technology: null
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NetServices/Articles/programming.html
archived_at: '2026-07-15T07:17:15.481545Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [Bonjour 概述](About%20Bonjour.md)


[下一页](Bonjour%20Operations.md)[上一页](Domain%20Naming%20Conventions.md)

# Bonjour API 架构

OS X 和 iOS 为 Bonjour 服务应用程序提供了多个层次的应用编程接口（API）：Foundation 框架中的 NSNetService 和 NSNetServiceBrowser 类；Core Services 中 CFNetwork 框架的一部分 CFNetServices；面向 Java 的 DNS Service Discovery（仅 OS X）；以及围绕 BSD 套接字构建的低层 DNS Service Discovery API。这三套 API 都提供了发布、发现和解析网络服务的能力。[图 3-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdinjzfvjvomq) 展示了这些 API 层次的结构。可以看到，多播 DNS 响应程序（或其他 DNS 服务器）位于最底层，因此你的软件不必直接与 DNS 打交道。

__图 3-1__  Bonjour 网络服务的 API 层次

!

`NSNetService` 和 `NSNetServiceBrowser` 类属于 Cocoa 中的 Foundation 框架，它们为服务发现和发布提供了面向对象的抽象。`NSNetService` 对象表示 Bonjour 服务的实例，既可以是待发布的服务，也可以是客户端发现的服务；`NSNetServiceBrowser` 则表示针对某一类服务的浏览器。对大多数 Cocoa 程序员来说，这些类应该已经够用。如果你需要更精细的控制，可以在 Cocoa 应用程序中使用 DNS Service Discovery API。

`NSNetService` 和 `NSNetServiceBrowser` 会被调度到默认的 `NSRunLoop` 对象上，以异步方式执行发布、发现和解析。`NSNetService` 与 `NSNetServiceBrowser` 对象返回的所有结果都由委托（delegate）对象处理。这些对象必须关联到某个运行循环才能工作，但不一定非得是默认的那个。

Core Services 框架中声明的 CFNetServices API 提供了 Core Foundation 风格的类型和函数，用于管理服务和服务发现。CFNetServices 定义了三种 Core Foundation 对象类型：CFNetService、CFNetServiceBrowser 和 CFNetServiceMonitor。CFNetService 是服务实例的抽象表示，既可用于发布也可用于使用服务，相关函数提供了发布和解析服务的支持。CFNetServiceBrowser 表示针对特定域中某一类服务的浏览器。一般来说，只有当你在 OS X 或 iOS 上编写 Core Foundation 层的代码时，才应该使用这套 API。

CFNetService 和 CFNetServiceBrowser 对象通常都在 CFRunLoop 中得到服务。要获取结果，应用程序需要实现回调函数来处理各类事件，例如新服务出现或消失、实例被解析以及发生错误。与 NSNetService 和 NSNetServiceBrowser 不同，CFNetServices 的各类型不要求有运行循环，在需要时也可以同步运行。不过，使用这些函数的同步模式是一种不良实践。

DNS Service Discovery API 声明在 `/usr/include/dns_sd.h` 中，为 Bonjour 服务提供低层的 BSD 套接字通信。DNS Service Discovery 充当你的软件与多播 DNS 响应程序或 DNS 服务器之间的中间层。它替你管理多播 DNS 响应程序，让你可以用服务和服务浏览器的概念来编写程序，而不必直接面对 DNS 资源记录。

由于 DNS Service Discovery API 是 Darwin 开源项目的一部分，因此当你编写跨平台代码（面向 iOS 和 OS X 之外的平台）时，或者当你需要使用 `NSNetService` 等高层 API 所不具备的低层特性时，就应当使用它。

如果要为 Windows、Linux 或 FreeBSD 开发 Bonjour 服务应用程序，也应当使用 DNS Service Discovery。

[下一页](Bonjour%20Operations.md)[上一页](Domain%20Naming%20Conventions.md)

