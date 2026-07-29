---
title: 创建 Metal 动态库
framework: Metal
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, Xcode 26.3+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/creating-a-metal-dynamic-library
source_url: 'https://developer.apple.com/documentation/metal/creating-a-metal-dynamic-library'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/creating-a-metal-dynamic-library.json'
content_hash: 'sha256:9a40498b6025440d'
translated: true
---

> 导航：[技术](../technologies.md) · [Metal](../metal.md) · [Metal 示例代码库](metal-sample-code-library.md)

# 创建 Metal 动态库

<sub>示例代码</sub>

编译着色器（shader）库并将其作为动态链接库（dynamically linked library）写入文件。

## 概述

> [!note] 注意
> 此示例代码项目与 WWDC20 讲座 [10615：使用 Metal 构建 GPU 二进制文件](https://developer.apple.com/wwdc20/10615/) 相关联。

### 配置示例代码项目

此示例需要以下系统和软件配置：

- macOS 10.16 或更高版本
- iOS 14 或更高版本
- Xcode 12 或更高版本

## 另请参阅

### 着色器

- [使用函数特化（function specialization）构建管线（pipeline）变体](using-function-specialization-to-build-pipeline-variants.md) — 从通用着色器源码为不同细节层级创建管线。

## 下载

- [CreatingAMetalDynamicLibrary.zip](https://docs-assets.developer.apple.com/published/77f04547135f/CreatingAMetalDynamicLibrary.zip)
