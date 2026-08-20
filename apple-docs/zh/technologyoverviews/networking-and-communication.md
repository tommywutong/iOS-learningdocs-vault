---
title: 网络与通信
framework: Technology Overviews
symbol_kind: article
role: article
role_heading: ''
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/technologyoverviews/networking-and-communication
source_url: 'https://developer.apple.com/documentation/technologyoverviews/networking-and-communication'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/technologyoverviews/networking-and-communication.json'
content_hash: 'sha256:3996704dbf110224'
translated: true
---

> 导航：[技术](../technologies.md) · [技术概述](../technologyoverviews.md) · [硬件、网络与传感器](hardware-networking-sensors.md)

# 网络与通信

通过网络与其他设备通信、扩展系统的核心网络能力，以及将电话功能集成到你的 App 中。

App 让人与人之间以及与日常生活中使用的服务建立连接。许多系统框架在其实现中使用了基于网络的服务，但你可能还需要下载文件、与 RESTful 端点通信，或支持通过网络进行音频和视频通话。这时，系统框架会提供你在网络上发送和接收数据所需的 API。

## 通过网络发送和接收数据与文件

当你想通过网络发送或接收数据或文件时，[URL 加载系统](../foundation/url-loading-system.md) 是发起请求最稳健的选择。该系统提供了一个直接的 API，用于：

- 从 URL [下载](../foundation/downloading-files-from-websites.md)文件。
- 向网站或 RESTful 端点[下载](../foundation/fetching-website-data-into-memory.md)或[上传](../foundation/uploading-data-to-a-website.md)数据。
- 向服务器[上传数据流](../foundation/uploading-streams-of-data.md)。
- 在 App 处于非活跃状态时[在后台下载文件](../foundation/downloading-files-in-the-background.md)。

URL 加载系统使用基于会话的方法来管理网络请求。每个会话的配置告诉系统如何管理网络请求以及可能发生的任何更改。例如，你可以[配置一个会话](../foundation/urlsessionconfiguration.md)，使其仅通过 Wi-Fi 而非蜂窝网络下载大文件。创建会话后，安排任务以发送或接收你想要的数据。系统会执行你安排的任务，并使用会话的配置数据来管理认证凭据、决定如何使用缓存和 Cookie，以及选择合适的网络。为了使你的 App 了解进度，会话会向你提供的委托（delegate）对象报告更新。

由于 URL 加载系统是 [Foundation 框架](../foundation.md)的一部分，因此所有 App 都可以使用它，并且可以在不同设备之间移植。

## 自定义 App 的基于网络的通信

现代网络需要许多不同的通信协议，了解对于与服务器的特定连接应使用哪些协议非常重要。像 [URL 加载系统](../foundation/url-loading-system.md)这样的技术为你处理了大部分这种复杂性，提供了简单的 API 来发送和接收资源。然而，有时你可能需要自己管理连接，以适应性能需求或网络行为。例如：

- 你可能希望在向其他设备发送游戏数据时最大限度地减少延迟。
- 你可能需要为流媒体 App 提供多播支持，或者希望在直播期间防止缓冲。
- 你可能希望在邮件或消息 App 中自己处理不同网络之间的过渡（transition）。

要更直接地控制 App 的网络请求，请采用 [Network](../network.md) 框架。使用此框架，通过标准协议（如 QUIC、TCP、UDP）或你定义的自定义协议来建立与服务器和其他设备的连接。该框架提供了针对你的特定需求调整连接的方法。它优雅地处理与网络相关的更改，使你能够轻松跟踪网络可用性的变化，并将连接迁移到更可靠的网络。它还支持保护发送数据所需的安全和隐私（privacy）选项。

要发起与另一设备的连接，请创建一个 [NWConnection](../network/nwconnection.md) 对象，并使用端点和参数对其进行配置。端点提供另一设备的地址，但你也可以指定 Bonjour 服务和其他值。当你启动连接时，系统会评估网络条件并选择最符合你要求的网络。在服务器端，[NWListener](../network/nwlistener.md) 对象响应连接请求，并将来自服务器的响应发送回客户端。

## 扩展设备的核心网络能力

如果你的 App 有自定义网络需求，你可以通过多种方式增强核心网络的能力。例如：

- 创建自定义 [Wi-Fi 配置](../networkextension/wi-fi-configuration.md)。
- 实现一个用于[认证热点网络](../networkextension/hotspot-helper.md)的助手。
- 创建和管理[虚拟专用网络（VPN）](../networkextension.md#Virtual-private-networks)配置，或实现你自己的配置。
- 创建[网络中继配置](../networkextension/relays.md)。
- 实现设备上的[网络内容](../networkextension.md#Content-filters)或 [URL](../networkextension/url-filters.md) 过滤器。
- 创建和管理系统范围的 [DNS 配置](../networkextension.md#DNS-configurations)。
- 在本地网络上创建你自己的[推送通知服务器](../networkextension/local-push-connectivity.md)。

使用 [Network Extension](../networkextension.md) 框架的类型来实现你所需的能力。大多数功能要求你将代码放在 App 扩展（app extension）中，该扩展随 App 一起交付给用户。并非所有功能在所有平台上都可用，因此请查阅文档以确保你所需的功能可用。

## 使用 Bonjour 通告设备

Bonjour 是 Apple 对 _零配置网络（zero-configuration networking）_ 的实现，是一种简化本地网络上设备设置和交互的过程。借助 Bonjour，App 可以浏览网络上的设备，而无需知道特定的网络地址。Bonjour 提供支持请求功能的可用设备列表。例如，系统打印面板会查找本地网络上的打印机，并将它们作为打印作业的相关目标呈现。

要使 App 的自定义功能在网络中可用，请使用 [Network](../network.md) 框架通过 Bonjour 通告它们。具体来说，配置一个[监听器（listener）](../network/nwlistener.md)来处理来自其他设备的传入请求。要向你的功能发出请求，客户端使用你通过 Bonjour 通告的特定[端点（endpoint）](../network/nwendpoint.md)配置一个 [NWConnection](../network/nwconnection.md) 对象。

## 为 App 添加拨号和通话功能

如果你的 App 管理自己的 IP 语音（VoIP）服务，[LiveCommunicationKit](../livecommunicationkit.md) 支持你的 App 的通话基础设施。使用该框架通知系统你 App 的状态，系统会利用此信息处理来电。例如，如果某人正在通话时有新来电，系统可能会询问此人是否要挂起当前通话并接听新来电。如果你的 App 管理通话，但不提供自己的 VoIP 服务，则使用 [LiveCommunicationKit](../livecommunicationkit.md) 管理通话，该框架会将通话路由到相应的 App。

在某些地区，设备所有者会指定一个 App 来处理传入和传出的通话。当存在多个 App 时，系统需要知道将哪个用于传入的通话。在 iPhone 上，“电话”App 通常是默认的通话和拨号 App，但用户可以选择不同的 App。如果你正在构建一个通话 App，请采用 [LiveCommunicationKit](../livecommunicationkit.md) 框架，让你的 App 准备好成为[默认拨号 App](../livecommunicationkit/preparing-your-app-to-be-the-default-dialer-app.md) 和[默认通话 App](../callkit/preparing-your-app-to-be-the-default-calling-app.md)。除了处理通话之外，默认拨号 App 还可以访问用户设备上的通话记录以及其他权益。
