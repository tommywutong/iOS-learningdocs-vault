---
title: 应用程序二进制接口
framework: xcode
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/application-binary-interfaces
source_url: 'https://developer.apple.com/documentation/xcode/application-binary-interfaces'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/application-binary-interfaces.json'
content_hash: 'sha256:ec305ece526da45c'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md)

# 应用程序二进制接口

编写遵循 Apple 平台应用程序二进制接口（application binary interface，ABI）的汇编指令。

## 概述

Apple 产品中的 CPU 定义了如何调用函数、管理栈和执行其他操作的规则。如果你的代码包含汇编指令，就必须遵循这些规则，才能与编译器生成的代码正确协同工作。如果不遵循这些规则，你的代码可能会崩溃或出现意外行为。

## 主题

### 64 位接口

- [为 Apple 平台编写 ARM64 代码](writing-arm64-code-for-apple-platforms.md) — 创建遵循 Apple 平台所支持应用程序二进制接口（ABI）的 64 位 ARM 汇编语言指令。
- [为 Apple 平台编写 64 位 Intel 代码](writing-64-bit-intel-code-for-apple-platforms.md) — 创建遵循 Apple 平台所支持应用程序二进制接口（ABI）的 64 位 Intel 汇编语言指令。

### iOS 接口

- [为 iOS 编写 ARMv7 代码](writing-armv7-code-for-ios.md) — 创建遵循 iOS 所支持应用程序二进制接口（ABI）的 ARMv7 汇编语言指令。
- [为 iOS 编写 ARMv6 代码](writing-armv6-code-for-ios.md) — 创建遵循 iOS 所支持应用程序二进制接口（ABI）的 ARMv6 汇编语言指令。

## 另请参阅

### 硬件注意事项

- [Apple 芯片](../apple-silicon.md) — 获取为搭载 Apple 芯片的 Mac 创建软件所需的资源。
