---
title: Metal 动态库
framework: Metal
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/metal-dynamic-libraries
source_url: 'https://developer.apple.com/documentation/metal/metal-dynamic-libraries'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/metal-dynamic-libraries.json'
content_hash: 'sha256:9b00a05bef9a5855'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Metal](../metal.md) · [Shader libraries](shader-libraries.md)

# Metal 动态库

创建一个包含可复用代码的单个 Metal 库，以缩减库的体积，并避免运行时重复编译 shader。

## 概述

随着 shader 在体积、复杂度和范围上的增长，它们常常最终会共享一些实用函数。在 Metal 的默认编译模型下，链接会将库嵌入进去，类似于 LLVM 链接器的静态链接方式。对 Metal 来说，以这种方式嵌入库会带来两个后果：二进制体积增大，以及编译时间增加。每当加载一个库时，它都会编译一份自己的实用函数副本，这意味着 Metal 会多次编译并重复生成你的实用函数。

为避免这个问题，Metal 提供了动态库，类似于 LLVM 的动态共享库。你的 App 只在某个 shader 第一次请求时，为设备 GPU 加载并编译一次动态库。之后的 shader 调用会使用这些已编译好的实用函数，而不是再编译同一 shader 二进制的另一个版本。

要在你的 App 中支持 Metal 动态库，请对你随 App 一起打包的动态库调用 [- newDynamicLibrary:error:](<mtldevice/makedynamiclibrary(library_).md>)。然后通过像 [preloadedLibraries](mtlcomputepipelinedescriptor/preloadedlibraries.md) 这样的属性，将其添加到流水线描述符的动态库信息中。

## 主题

### 使用 Metal 动态库

- [Compiling and linking Metal dynamic libraries](compiling-and-linking-metal-dynamic-libraries.md) — 从命令行构建一个 Metal 动态库，以支持运行时加载共享的 shader。
- [Creating a Metal dynamic library](creating-a-metal-dynamic-library.md) — 编译一个 shader 库，并将其作为动态链接库写入文件。

## 另请参阅

### Shader 编译

- [Metal libraries](metal-libraries.md) — 从命令行编译并管理 Metal 库。
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
