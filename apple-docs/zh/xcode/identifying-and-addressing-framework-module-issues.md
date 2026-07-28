---
title: 识别并解决框架模块问题
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/identifying-and-addressing-framework-module-issues
source_url: 'https://developer.apple.com/documentation/xcode/identifying-and-addressing-framework-module-issues'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/identifying-and-addressing-framework-module-issues.json'
content_hash: 'sha256:d55198ff1b5f857d'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [构建系统](build-system.md)

# 识别并解决框架模块问题

<sub>文章</sub>

使用模块验证器检测并修复框架模块中常见的问题。

## 概述

当你创建包含 Objective-C、Objective-C++、C 或 C++ 代码的框架，并将其分发给客户、客户端或其他开发者时，发现框架中在构建时不会显现的问题，通常既困难又耗时。

在 Xcode 14.3 或更高版本中，在你的 Xcode 项目的构建设置中启用模块验证器，以便在分发框架之前识别并解决框架模块的问题。

这些问题的一些示例包括：

- 伞头（umbrella header）中缺少头文件引用
- 使用引号包含（quoted include）而不是尖括号包含（angle-bracketed include）
- 在你的公开和私有头文件中使用 `@import` 语法
- 不正确的目标条件（target conditional）
- 在 `extern "C"` 语言链接规范（language linkage specification）内部使用导入
- 伞头中的非模块化头文件
- 公开头文件中引用私有头文件

当你启用模块验证器时，它会在你的代码中查找模块问题，并在 Xcode 的问题导航器（Issue navigator）中像编译器错误或警告一样显示错误。

### 启用模块验证器构建设置

在你的 Xcode 项目中，选择框架的目标（target），然后选择“构建设置（Build Settings）”标签页。滚动到 Apple Clang - 模块验证器部分。对于在 Xcode 14.3 或更高版本中创建的新项目，“启用模块验证器（Enable Module Verifier）”设置默认为“是”。对于在早期版本的 Xcode 中创建的项目，请将该设置更改为“是”。

![显示“启用模块验证器”设置为“是”的 Xcode 构建设置。](../../../attachments/92030186c87ab22e06bb2557407e46eb/identifying-and-addressing-framework-module-issues-2@2x.png)

然后，检查“支持的语言（Supported Languages）”和“支持的语言方言（Supported Language Dialects）”的值，并根据你的项目需求进行更新。查看每个设置的“快速帮助（Quick Help）”以找到有效值。

有关配置构建设置的更多信息，请参阅[配置目标的构建设置](configuring-the-build-settings-of-a-target.md)。

### 构建项目并识别问题

在 Xcode 中构建你的项目，然后显示问题导航器以查看项目中的问题。模块验证器问题会在问题导航器中显示为错误。

![](../../../attachments/db4ffdc937389b10643936183d53eb3a/identifying-and-addressing-framework-module-issues-1@2x.png)

<sub>Xcode 问题导航器，显示了一个高亮的模块验证器问题以及头文件中对应的代码行。</sub>

检查这些问题，然后点击某个问题以在你的源代码中高亮显示它。

### 解决常见问题

将你发现的每个问题与下表中的示例错误消息进行匹配。然后，使用错误解决示例来帮助你在代码中解决问题。

| 错误消息 | 错误解决方法 |
|---|---|
| 模块“ExampleModule”的伞头未包含头文件“MyObject.h” | 将缺少的头文件添加到你的伞头中。像这样包含缺少的头文件：`#import <ExampleModule/MyObject.h>`。 |
| 框架头文件中使用了双引号包含 “MyObject.h”，应改用尖括号包含 | 将引号包含替换为尖括号包含。将 `#import "MyObject.h"` 改为 `#import <ExampleModule/MyObject.h>`。 |
| 不鼓励在框架头文件中使用“`@import`”，包含此头文件需要 `-fmodules` | 避免在公开和私有头文件中使用语义导入语法。将 `@import Foundation;` 改为 `#import <Foundation/Foundation.h>`。 |
| “`TARGET_OS_IPHONE`”未定义，计算结果为 0 | 修复目标条件。在头文件中添加使用目标条件的 include 语句：`#include <TargetConditionals.h>`。如果这不能解决问题，请检查你使用的目标条件是否在 `TargetConditionals.h` 中定义。 |
| 在 extern "C" 语言链接规范内部导入了 C++ 模块“ExampleFramework.ExampleSource”_，或者_ extern "C" 语言链接规范从此处开始 | 避免在 `extern "C"` 语言链接规范内部包含导入。将 include 语句移到 `extern "C"` 作用域之外。不要在模块映射（module map）中使用 `[extern_c]` 属性。 |
| 在框架模块“ExampleModule”内部包含非模块化头文件 | 从头文件中移除 include 语句。你尝试包含的头文件不是模块化的，因此不能将其包含在框架模块中。如果可能，使该代码模块化，以便你可以将其包含在框架模块中。 |
| 公开框架头文件包含了私有框架头文件“ExampleModule/MyObject_Private.h” | 避免在公开头文件中引用私有头文件。要么将私有头文件设为公开，要么从公开头文件中移除对私有头文件的包含。 |

## 另请参阅

### 构建设置

- [配置目标的构建设置](configuring-the-build-settings-of-a-target.md) — 指定编译、链接目标并从目标生成产品所使用的选项，并识别从项目或系统继承的设置。
- [向项目添加构建配置文件](adding-a-build-configuration-file-to-your-project.md) — 以纯文本文件指定项目的构建设置，并为调试和发布构建提供不同的设置。
- [构建设置参考](build-settings-reference.md) — 用于控制或更改目标构建方式的各个 Xcode 构建设置的详细列表。
- [了解 Xcode 中构建产品布局的变更](understanding-build-product-layout-changes.md)
