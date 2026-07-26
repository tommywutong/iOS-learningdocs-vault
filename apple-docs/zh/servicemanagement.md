---
title: Service Management
framework: Service Management
symbol_kind: module
role: collection
role_heading: Framework
platforms: [Mac Catalyst 13.0+, macOS 10.6+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/servicemanagement
source_url: 'https://developer.apple.com/documentation/servicemanagement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/servicemanagement.json'
content_hash: 'sha256:d4a161295e063775'
translated: true
---

> 导航：[Technologies](technologies.md)

# Service Management

<sub>框架</sub>

在 App 内管理启动项、启动代理和启动守护进程。

## 概述

使用 Service Management 来安装并观察 macOS 支持的三种辅助帮助程序可执行文件的权限设置。你可以在 App 包内部使用这三者中的任意一种，为你的 App 提供相关的附加功能：

- **LoginItems（登录项）** — 一个 `launchd` 在用户登录时启动的 App。`LoginItem` 是一个会持续运行直到用户注销或手动退出的 App。它的主要作用是让系统能够自动启动帮助程序可执行文件
- **LaunchAgents（启动代理）** — 代表当前登录用户运行的进程。`launchd`（一个系统级进程）负责管理代理。代理可以与同一用户会话中的其他进程通信，也可以在系统上下文中与系统级守护进程通信。
- **LaunchDaemons（启动守护进程）** — 一个由 `launchd` 代表用户管理的独立后台进程，以 root 身份运行，并且可能在任何用户登录系统之前就已运行。守护进程不会直接与用户进程交互；它只能响应用户进程以底层请求形式发出的请求，例如系统请求，即 [XPC](foundation/xpc.md) 这种底层进程间通信系统。

## 主题

### 要点

- [Updating helper executables from earlier versions of macOS](servicemanagement/updating-helper-executables-from-earlier-versions-of-macos.md) — 简化 App 的帮助程序可执行文件，并支持新的授权控制。
- [Updating your app package installer to use the new Service Management API](servicemanagement/updating-your-app-package-installer-to-use-the-new-service-management-api.md) — 通过一个无图形界面的代理 App 了解 Service Management API。

### 管理

- [SMAppService](servicemanagement/smappservice.md) — 框架用来控制存放在 App 主包内的帮助程序可执行文件的对象。
- [SMJobBless](<servicemanagement/smjobbless(________).md>) — 将给定标签对应的可执行文件作为一项作业提交给 `launchd`。 _(已废弃)_
- [Authorization Constants](servicemanagement/authorization-constants.md) — 描述授权帮助程序可执行文件或修改守护进程应用能力的常量。
- [Property List Keys](servicemanagement/property-list-keys.md) — 描述框架所管理的应用、守护进程和帮助程序可执行文件种类的属性列表键。

### 启用

- [SMLoginItemSetEnabled](<servicemanagement/smloginitemsetenabled(____).md>) — 启用主 App 包目录中的帮助程序可执行文件。 _(已废弃)_

### 状态

- [Status](servicemanagement/smappservice/status-swift.enum.md) — 描述帮助程序可执行文件注册或授权状态的常量。

### 错误

- [Service Management Errors](servicemanagement/service-management-errors.md) — 框架返回的错误。

### 已废弃

- [Deprecated Symbols](servicemanagement/deprecated-symbols.md)

### 变量

- [SMAppServiceErrorDomain](servicemanagement/smappserviceerrordomain.md)
