---
title: 减小着色器库的二进制大小
framework: Metal
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/minimizing-the-binary-size-of-a-shader-library
source_url: 'https://developer.apple.com/documentation/metal/minimizing-the-binary-size-of-a-shader-library'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/minimizing-the-binary-size-of-a-shader-library.json'
content_hash: 'sha256:9242e370bc01e725'
translated: true
---

> 导航：[技术](../technologies.md) · [Metal](../metal.md) · [着色器库](shader-libraries.md) · [Metal 库](metal-libraries.md)

# 减小着色器库的二进制大小

<sub>文章</sub>

通过选择 Metal 编译器的大小优化选项（size optimization option），减少着色器的存储占用，并可能缩短其编译时间。

## 概述

默认情况下，Metal 编译器会优化着色器代码以提升运行时性能。例如，编译器可能会使用内联（inlining）或循环展开（loop unrolling）等技术——这些技术通过复制可执行代码来避免运行时的分支惩罚。取决于着色器代码的具体情况，这些运行时优化工作可能会显著增加着色器库的二进制大小和着色器的编译时间。

你可以更改编译器的优化设置，使其优先考虑最小化二进制的大小。编译器会避免使用那些复制代码的技术，从而最小化着色器库的大小，并且通常也能缩短编译时间。

着色器库的二进制大小、编译时间性能和运行时性能在很大程度上取决于代码的复杂度。请检查着色器编译器的哪种优化设置最适合你的 App 和工作流程。如果编译生成的二进制文件对你的 App 来说过大或编译时间过长，请考虑使用 Metal 编译器的大小优化选项。

你可以通过以下方式设置 Metal 编译器的大小优化选项：

- 在 Xcode 14 或更高版本中设置
- 从命令行设置
- 在运行时使用 Metal API 设置

编译着色器最简单的方法是让 Xcode 将着色器与 App 的其余部分一起编译。随着着色器复杂度、大小或构建时间的增加，你可以考虑使用 Metal 命令行工具预编译它们，以避免在 Xcode 中编译。某些 App 可能需要在设备上、运行时使用 Metal API 编译着色器。

### 在构建时编译着色器

要在构建时编译着色器的同时优化大小，请在 Xcode 中设置 Metal 编译器的大小优化选项：

1. 点击项目中的构建目标。
2. 点击“构建设置”标签页，并过滤 Metal 编译器。
3. 在“Metal Compiler - Build Options”下，将“Optimization Level”设置为 `Size [-Os]`。

![](../../../attachments/f2c3feea8922259318e2f4e8b5650f04/minimizing-the-binary-size-of-a-shader-library-1@2x.png)

<sub>一张 Xcode 窗口的截图，其中显示了 Hello Triangle 示例 App 的 macOS 目标的构建设置。Metal 编译器的“Optimization Level”设置为 </sub>

每次你构建包含着色器代码的目标时，Xcode 都会将此设置传递给 Metal 编译器。

### 在命令行预编译着色器

对于使用大量或复杂着色器的 App，请考虑在 Xcode 外部预编译着色器，以节省每次编译 App 时的构建时间。有关手动编译着色器库的更多信息，请参阅[通过预编译源文件构建着色器库](building-a-shader-library-by-precompiling-source-files.md)。

要在命令行环境（例如终端）中编译 Metal 着色器源文件时优化大小，请使用 Metal 编译器的 `-Os` 优化选项。

```shell
% xcrun -sdk macosx metal -Os Shadows.metal
```

> [!note] 注意
> 此示例使用 `macosx` SDK，但你可以使用你的 App 所针对的任何 SDK。

### 在运行时编译着色器

如果你想在运行时编译着色器，你的 App 可以配置 Metal API 以优化大小。对于某些 App，在 App 运行时在设备上编译着色器可能更实际，这通常是为了减少 App 的存储大小。你还可以在运行时编译着色器以进行快速原型设计和调试。

这种方法通过将着色器编译推迟到 App 在用户设备上运行时进行，来减少 App 的构建时间，但你的 App 在首次启动时的加载时间可能会明显变长。

要在设备上编译着色器库时最小化二进制大小：

1. 创建一个 [MTLCompileOptions](mtlcompileoptions.md) 实例。
2. 将其 [optimizationLevel](mtlcompileoptions/optimizationlevel.md) 属性设置为 [MTLLibraryOptimizationLevelSize](mtllibraryoptimizationlevel/size.md)。
3. 使用 [MTLDevice](mtldevice.md) 实例的 [- newLibraryWithSource:options:error:](<mtldevice/makelibrary(source_options_).md>) 或 [- newLibraryWithSource:options:completionHandler:](<mtldevice/makelibrary(source_options_completionhandler_).md>) 方法编译你的库。

## 另请参阅

### 使用 Metal 中间表示库

- [通过预编译源文件构建着色器库](building-a-shader-library-by-precompiling-source-files.md) — 使用命令行环境中的 Metal 编译器工具创建可以添加到 Xcode 项目的着色器库。
- [生成和加载 Metal 库符号文件](generating-and-loading-a-metal-library-symbol-file.md) — 通过在编译时创建配套符号文件并在调试时加载，从生产 App 中调试 Metal 着色器。
