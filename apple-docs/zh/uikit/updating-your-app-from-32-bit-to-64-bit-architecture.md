---
title: 将 App 从 32 位架构更新到 64 位架构
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/updating-your-app-from-32-bit-to-64-bit-architecture
source_url: 'https://developer.apple.com/documentation/uikit/updating-your-app-from-32-bit-to-64-bit-architecture'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/updating-your-app-from-32-bit-to-64-bit-architecture.json'
content_hash: 'sha256:1b855ce1bec391a2'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [App 与环境](app-and-environment.md)

# 将 App 从 32 位架构更新到 64 位架构

通过调整 App 以支持较新版本的操作系统，确保其行为符合预期。

## 概述

在 iOS 11 及更高版本中，所有 App 都使用 64 位架构。如果 App 的目标是较早版本的 iOS，则必须更新 App，才能在更高版本上运行。

### 将 App 更新到最新 SDK

首先将现有 App 更新到 iOS 11 或更高版本。先更新 App 后，你可以移除已废弃的代码路径、处理所有编译器警告，并在代码中搜索特定的 64 位问题。

1. 安装最新版本的 Xcode 并打开项目。Xcode 会提示你对项目进行*现代化改造*。现代化改造会添加在为 64 位架构编译 App 时非常重要的新警告和错误。
2. 更新项目设置，以支持最新版本的 iOS。如果项目的目标版本早于 iOS 5.1，就无法构建 64 位项目。
3. 将项目中的 Architectures 构建设置更改为 Standard Architectures。
4. 更新 App 以支持 64 位运行时环境。新的编译器警告和错误会帮助引导你完成此过程。
5. 在实际的 64 位硬件上测试 App。不要依赖 Simulator App。尽管它在开发期间很有帮助，但某些更改（例如函数调用约定）只有在 App 于设备上运行时才会显现。
6. 使用 Instruments 调整 App 的内存性能。

### 审核代码

检查代码是否正确使用指针至关重要。对指针大小的假设可能导致不稳定行为，甚至崩溃。请重点关注以下方面：

- [更新数据结构](updating-data-structures.md)。消除结构中有关类型大小和对齐方式的假设，并使用显式数据类型。
- [审核指针用法](auditing-pointer-usage.md)。遵循正确的类型转换行为，并检查用于分配内存的方法。
- [管理函数和函数指针](managing-functions-and-function-pointers.md)**。**为确保安全，请使用函数原型，并检查对具有可变长度实参列表的函数的调用。

解决指针用法问题后，App 应当趋于稳定，此时可以专注于性能并进行相应优化：

- [优化内存性能](optimizing-memory-performance.md)。建立性能测试，衡量在 64 位运行时环境中对内存的使用。
- [验证数学计算](verifying-mathematical-calculations.md)。验证数学运算中的有符号值以确保结果准确，并检查位掩码运算的用法。

## 主题

### 内存与指针访问

- [更新数据结构](updating-data-structures.md) — 检查 App 的数据设计，并将其更新为符合 64 位架构。
- [审核指针用法](auditing-pointer-usage.md) — 确保代码中的指针对 64 位运行时而言是安全的。
- [管理函数和函数指针](managing-functions-and-function-pointers.md) — 确保代码正确处理函数、函数指针和 Objective-C 消息。

### 性能与准确性

- [优化内存性能](optimizing-memory-performance.md) — 衡量 64 位运行时对 App 内存用量的影响。
- [验证数学计算](verifying-mathematical-calculations.md) — 确保数学运算在 64 位架构中的准确性。

## 另请参阅

### 架构

- [UIApplicationMain](<uiapplicationmain(________)-1yub7.md>) — 创建 App 对象和 App 委托（app delegate），并设置事件循环。
