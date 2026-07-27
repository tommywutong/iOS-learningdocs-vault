---
title: Metal 库
framework: Metal
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/metal-libraries
source_url: 'https://developer.apple.com/documentation/metal/metal-libraries'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/metal-libraries.json'
content_hash: 'sha256:52870ce4ec9ebb71'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Metal](../metal.md) · [Shader libraries](shader-libraries.md)

# Metal 库

从命令行编译并管理 Metal 库。

## 概述

默认情况下，你的 Metal shader 会编译成一种叫做 _Metal 中间表示_（Metal IR）的格式，这是一种与 GPU 无关的字节码。在你 App 的运行时，Metal 会将这份字节码编译成针对宿主设备的、特定于 GPU 的二进制文件。如果你以字符串形式提供 shader 函数，它们会先在设备上编译成 Metal IR，然后再经过针对 GPU 的二次编译。

你添加到某个 App 源代码编译构建阶段的 Metal 源文件，会编译成一个名为 `default.metallib` 的 Metal IR 库。在你的 App 中，通过对某个 [MTLDevice](mtldevice.md) 调用 [- newDefaultLibrary](<mtldevice/makedefaultlibrary().md>) 方法，在运行时加载这个库。对于更复杂的项目，你可能想为 Metal 库创建单独的 target，在构建脚本中修改它们，或者执行其他优化。

Metal IR 的编译会在执行某次 shader 函数调用之前完成。当你的库由其他 shader 使用的实用函数组成时，请使用 [Metal dynamic libraries](metal-dynamic-libraries.md)。要分发特定于 GPU 的二进制文件并避免运行时 shader 编译，请使用 [Metal binary archives](metal-binary-archives.md)。

## 主题

### 使用 Metal 中间表示库

- [Building a shader library by precompiling source files](building-a-shader-library-by-precompiling-source-files.md) — 使用命令行环境中的 Metal 编译器工具，创建一个可以添加到 Xcode 项目中的 shader 库。
- [Minimizing the binary size of a shader library](minimizing-the-binary-size-of-a-shader-library.md) — 通过选择 Metal 编译器的体积优化选项，缩减 shader 的存储占用空间，并有可能缩短其编译时间。
- [Generating and loading a Metal library symbol file](generating-and-loading-a-metal-library-symbol-file.md) — 通过在编译时创建配套的符号文件，并在调试时加载它们，从你的正式版 App 中调试 Metal shader。

## 另请参阅

### Shader 编译

- [Metal dynamic libraries](metal-dynamic-libraries.md) — 创建一个包含可复用代码的单个 Metal 库，以缩减库的体积，并避免运行时重复编译 shader。
- [Metal binary archives](metal-binary-archives.md) — 将预编译好的、特定于 GPU 的二进制文件随你的 App 一起分发，以避免 Metal shader 的运行时编译。
- [MTL4Compiler](mtl4compiler.md) — 流水线状态与 shader 函数编译器的一个抽象。
- [MTL4CompilerDescriptor](mtl4compilerdescriptor.md) — 将用于创建编译器上下文的各项属性组合在一起。
- [MTL4CompilerTaskOptions](mtl4compilertaskoptions.md) — 控制某个 Metal 4 编译器实例的编译任务行为的配置选项。
- [MTL4CompilerTaskStatus](mtl4compilertaskstatus.md) — 表示某个编译器任务的状态。
- [MTL4Archive](mtl4archive.md) — 一个只读容器，存储来自某个 shader 编译器的流水线状态。
- [MTL4BinaryFunction](mtl4binaryfunction.md) — 表示一个二进制函数。
- [MTL4BinaryFunctionDescriptor](mtl4binaryfunctiondescriptor.md) — 其他函数派生接口的基础接口。
- [MTL4BinaryFunctionOptions](mtl4binaryfunctionoptions.md) — 用于配置二进制函数创建的选项。
- [MTL4PipelineStageDynamicLinkingDescriptor](mtl4pipelinestagedynamiclinkingdescriptor.md) — 将用于驱动某个流水线阶段动态链接过程的各项属性组合在一起。
