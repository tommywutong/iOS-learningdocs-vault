---
title: 优化内存性能
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/optimizing-memory-performance
source_url: 'https://developer.apple.com/documentation/uikit/optimizing-memory-performance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/optimizing-memory-performance.json'
content_hash: 'sha256:930c09b39ba9d658'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [App 与环境](app-and-environment.md) · [将 App 从 32 位架构更新到 64 位架构](updating-your-app-from-32-bit-to-64-bit-architecture.md)

# 优化内存性能

<sub>文章</sub>

衡量 64 位运行时对 App 内存用量的影响。

## 概述

64 位运行时增大了指针和某些标量数据的大小，导致 App 的内存占用空间（memory footprint）增大。其结果是处理器缓存和虚拟内存的压力增大，这可能对性能产生不利影响。开发 64 位 App 时，对 App 的内存用量进行性能分析和优化至关重要。

### 测试 App 并进行性能分析

首先创建标准测试，用于测试 App 的 64 位版本。通过这些测试，你可以衡量编译 64 位版本相较于 32 位版本所带来的性能损失。随着 App 内存用量的优化，你也可以衡量取得的改进。

至少有一项测试要使用最小内存占用场景，例如 App 刚打开并显示空白文稿的场景。其他测试则使用不同大小的数据，其中至少有一项测试使用非常大的数据集。复杂 App 可能需要多组测试数据，每组覆盖 App 功能的一个子集。

这些测试旨在衡量内存用量是否会随数据类型或数量而变化。如果某类特定数据导致 App 的 64 位版本使用的内存远多于原来的 32 位版本，那么很可能可以从这里找到改进机会。

### 使用正确的函数获取虚拟内存页大小

大多数 App 不需要知道虚拟内存页的大小，但有些 App 会将其用于缓冲区分配和框架调用。页面大小可能因设备而异，因此始终使用 `getpagesize()` 函数获取页面大小。

### 确保代码与位置无关

64 位运行时环境仅支持位置无关可执行文件（PIE）。默认情况下，大多数 App 都与位置无关。如果静态链接库或汇编代码等因素导致 App 无法构建为 PIE，则在将 App 移植到 64 位运行时时需要更新代码。

## 另请参阅

### 性能与准确性

- [验证数学计算](verifying-mathematical-calculations.md) — 确保数学运算在 64 位架构中的准确性。
