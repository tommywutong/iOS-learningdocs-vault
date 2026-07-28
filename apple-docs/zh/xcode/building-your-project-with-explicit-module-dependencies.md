---
title: 使用显式模块依赖项构建项目
framework: updates
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/building-your-project-with-explicit-module-dependencies
source_url: 'https://developer.apple.com/documentation/xcode/building-your-project-with-explicit-module-dependencies'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/building-your-project-with-explicit-module-dependencies.json'
content_hash: 'sha256:7f563918175de20d'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [构建系统](build-system.md)

# 使用显式模块依赖项构建项目

<sub>文章</sub>

使用 Xcode 构建系统消除不必要的模块变体，从而缩短编译时间。

## 概述

Xcode 构建系统负责管理项目中源文件的编译。通常，这些源代码依赖于项目、SDK 或外部依赖项中的其他模块。使用模块进行构建时，C 或 Objective-C 源代码依赖于通过 `@import` 导入的模块，以及涵盖通过 `#import` 导入的头文件的模块。Swift 代码依赖于通过 `import` 导入的模块。必须先构建这些模块，编译才能继续。在 Xcode 16 及更高版本中，构建系统会与编译器协调，在构建日志中将这项工作呈现为一组显式任务。

显式调度模块构建可让 Xcode 构建系统做出智能的调度决策，从而最大限度地提高并行度并缩短编译时间。在诊断模块依赖项中的编译器错误时，它还会在构建日志中生成更清晰、更具可操作性的错误消息。

在以下情况下，Xcode 构建系统会显式构建模块依赖项：

- 在启用模块的情况下编译 C 或 Objective-C 源代码。构建设置编辑器中的 `Enable Modules (C and Objective-C)` 设置控制模块的使用。所有新项目默认采用此设置，但可以在构建设置编辑器的 `Apple Clang - Language - Modules` 部分中更改。
- 使用默认 C/Objective-C 互操作模式编译 Swift 源代码。

对于 Swift 代码，显式构建的模块可改善调试体验。

> [!note] 注意
> 在 Swift 中使用 C++ 互操作功能时，不支持显式构建的模块；对于使用 Swift 4 或更早版本的 target，默认不启用此功能。要启用显式构建的模块，请将 [Explicitly Built Modules](build-settings-reference.md#Explicitly-Built-Modules) 构建设置设为 `Yes`。

### 了解模块依赖项的构建方式

显式构建模块依赖项时，编译分为三个不同阶段：

- **依赖项扫描**：编译器扫描输入源文件，以确定其依赖的模块。对于 C 和 Objective-C 源代码，这项工作由每个文件各自的依赖项扫描任务执行。编译 Swift 源代码时，编译器会在其规划任务期间扫描所有模块源代码。
- **模块编译**：依赖项扫描完成后，结果会传递给 Xcode 构建系统。构建系统会调用 Clang 和 Swift 编译器，按照依赖关系顺序构建模块，并行构建不相关的模块。
- **源代码编译**：使用已经构建的模块依赖项编译主要编译单元。

除了在构建日志中显示为不同步骤外，你还可以在构建时间线中查看这些任务：

![](../../../attachments/38ec6d9e7cdbcd71c1cb18ff85bf815e/building-your-project-with-explicit-module-dependencies-1@2x.png)

<sub>一张 Xcode 构建日志及随附时间线的截图，其中显示依赖项扫描、模块构建和编译任务。</sub>

### 通过减少模块变体缩短编译时间

在更复杂的项目中，构建日志可能会显示多个任务，它们对应同一模块采用不同选项集的构建。模块对其依赖方使用的编译器选项很敏感，因此使用不同选项构建项目的不同部分时，可能需要构建多个变体。有时确实需要构建模块的多个变体。例如，为多个架构构建代码时，每个架构至少需要构建一个模块变体。在其他情况下，不一致的项目配置可能会导致不必要地构建模块的许多变体。例如，具有相同依赖项但 `Preprocessor Macros` 构建设置值不同的两个 target 无法共享已构建模块。为了缩短构建时间并减少需要构建的变体数量，你应改为更新项目配置，使用一组统一选项编译源代码。

Xcode 提供的工具可用于确定项目设置中的差异何时需要构建额外模块变体。如果选择 Product \> Perform Action \> Build With Timing Summary 来启动构建，Xcode 会生成一份报告，其中显示所有已构建的模块，以及构建这些模块时所用选项之间的差异。

## 另请参阅

### 性能

- [配置项目以使用可合并库](configuring-your-project-to-use-mergeable-libraries.md) — 使用可合并动态库，使发布构建中的 App 启动时间接近静态链接，同时不损失调试构建中动态链接的构建速度。
- [提高增量构建速度](improving-the-speed-of-incremental-builds.md) — 告知 Xcode 构建系统项目中与 target 相关的依赖关系，并减少每个构建周期中的编译器工作量。
- [通过良好的编码实践提高构建效率](improving-build-efficiency-with-good-coding-practices.md) — 减少代码导出的符号数量，并向编译器提供所需的显式信息，从而缩短编译时间。
