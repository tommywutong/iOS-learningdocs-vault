---
title: 遵循 Mach IPC 安全限制
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/conforming-to-mach-ipc-security-restrictions
source_url: 'https://developer.apple.com/documentation/xcode/conforming-to-mach-ipc-security-restrictions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/conforming-to-mach-ipc-security-restrictions.json'
content_hash: 'sha256:d2ab3908fdd891b4'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Build system](build-system.md)

# 遵循 Mach IPC 安全限制

<sub>文章</sub>

避免与 Mach 消息相关的崩溃和潜在的不安全情况。

## 概述

Mach 端口代表系统上的底层进程间通信（IPC）能力，因此是一种基础而强大的构造。攻击者一旦获得对你 App 或扩展的 Mach 端口的访问权限，就可能获得大量特权，可用来攻击你的 App 以及系统上的其他资源。

包括 Mach Interface Generator（MIG）和 [XPC](../xpc.md) 在内的更高层级的 IPC 机制，旨在缓解许多与 Mach IPC 相关的安全问题。直接使用 Mach IPC 陷阱不会利用这些缓解措施，并且很难正确地做到这一点。在 Enhanced Security 功能中采用 [com.apple.security.hardened-process.platform-restrictions](../bundleresources/entitlements/com.apple.security.hardened-process.platform-restrictions.md) entitlement，可以把对 Mach 和 VM API 潜在不安全的误用转变为崩溃，然后用崩溃报告来诊断，并修复或移除这些潜在不安全的代码。

### 用其他 IPC 机制替换 Mach IPC 陷阱

修复潜在不安全的 Mach IPC 陷阱用法最简单的方式，是完全避免使用这个 API。改为使用另一种能避开潜在不安全情况的 IPC 机制，例如 [XPC](../xpc.md)。

### 诊断因额外运行时平台限制引发的崩溃

如果你的进程拥有值至少为 `1` 的 [com.apple.security.hardened-process.platform-restrictions](../bundleresources/entitlements/com.apple.security.hardened-process.platform-restrictions.md) entitlement，并且系统检测到潜在不安全的 Mach IPC 用法，系统就会使你的进程崩溃。崩溃报告的异常类型为 `EXC_GUARD`，异常子类型为 `GUARD_TYPE_MACH_PORT`。崩溃报告中的异常消息是下列值之一：

- **`REQUIRE_REPLY_PORT_SEMANTICS`** — 系统检测到这样一种情况：恶意进程有可能拦截或转移你的进程用来与由 `launchd` 管理的服务通信的 Mach 消息。请改用 XPC 而不是 Mach IPC 陷阱与该服务通信。
- **`KOBJECT_REPLY_PORT_SEMANTICS`** — 系统检测到这样一种情况：恶意进程有可能拦截或转移你的进程用来与内核通信的 Mach 消息。请使用 `libSystem` 中的函数来访问内核能力，或使用内核的 MIG 接口来调用内核 API。
- **`OOL_PORT_ARRAY`** — 系统检测到你的进程在 MIG 接口或 Mach IPC 陷阱中使用了不安全的描述符布局。请将你使用的 Mach 消息传递替换为 XPC；或者，修改你的 MIG 接口，使其不发送 Mach 端口数组。
- **`THREAD_SET_STATE`** — 系统检测到你的进程以潜在不安全的方式在其某个线程上调用了 [thread_set_state](../kernel/1418827-thread_set_state.md)。这个 API 提供了对你进程中任意线程状态的完全控制权，攻击者可以利用它改变你进程的控制流。不要调用 `thread_set_state`。如果你在 Mach 异常处理程序中调用了 `thread_set_state`，请重写该处理程序以使用安全的异常行为。参见下面的 `SET_EXCEPTION_BEHAVIOR`。
- **`SET_EXCEPTION_BEHAVIOR`** — 系统检测到你的进程在一个使用了不安全 Mach 异常行为的进程上设置了异常端口。包括 `EXCEPTION_DEFAULT` 在内的异常行为都是不安全的，因为它们会在发送异常消息的同时把一个任务或线程端口发送给接收方，这使得能够拦截该异常消息的攻击者有办法控制那个任务或线程。启用额外的运行时平台限制后，你的进程只能在使用 Mach 异常行为 `EXCEPTION_IDENTITY_PROTECTED`、`EXCEPTION_STATE` 或 `EXCEPTION_STATE_IDENTITY_PROTECTED` 的进程上设置异常端口。使用这些行为发送的异常消息中会附带一个任务身份令牌，你可以通过调用 [task_identity_token_get_task_port](../kernel/3727998-task_identity_token_get_task_por.md) 将其转换为线程端口，该函数会检查你的进程是否有权限使用该线程端口。
- **`ILLEGAL_MOVE`** — 系统检测到你的进程把一个指向其任务或线程控制端口的发送权限移交给了另一个进程。_发送权限_是指一个进程向某个 Mach 端口发送 Mach 消息的许可。把任务或线程控制端口的发送权限交给另一个进程，会让接收方进程完全控制你的进程。请使用异常回溯来定位负责把该端口的发送权限发送给另一个进程的代码，并将这段代码从你的 App 中移除。

## 另请参阅

### 安全性与隐私

- [Verifying the origin of your XCFrameworks](verifying-the-origin-of-your-xcframeworks.md) — 找出是谁对某个框架进行了签名，并在情况发生变化时采取行动。
- [Enabling enhanced security for your app](enabling-enhanced-security-for-your-app.md) — 检测越界内存访问、已释放内存的使用，以及其他潜在的漏洞。
- [Creating enhanced security helper extensions](creating-enhanced-security-helper-extensions.md) — 减少攻击者通过 App 的扩展来攻击它的机会。
- [Adopting type-aware memory allocation](adopting-type-aware-memory-allocation.md) — 减少代码中把指针当作数据处理的机会。
