---
title: 编译与链接 Metal 动态库
framework: Metal
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/compiling-and-linking-metal-dynamic-libraries
source_url: 'https://developer.apple.com/documentation/metal/compiling-and-linking-metal-dynamic-libraries'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/compiling-and-linking-metal-dynamic-libraries.json'
content_hash: 'sha256:95a6696e1529dc9a'
translated: true
---

> 导航：[技术](../technologies.md) · [Metal](../metal.md) · [着色器库](shader-libraries.md) · [Metal 动态库](metal-dynamic-libraries.md)

# 编译与链接 Metal 动态库

<sub>文章</sub>

通过命令行构建 Metal 动态库，从而实现共享着色器在运行时的加载。

## 概述

当你需要在多个 Metal 库之间共享一组实用函数时，在编译时进行静态链接会将这些函数包含到所有库中。这会导致库文件体积增大，因为每个 Metal 库都包含了实用函数的重复代码。同时，Metal 会为每个库独立编译相同的实用函数版本，从而延长着色器编译时间。

Metal 提供了支持运行时加载的动态库来解决这些问题——你将实用函数编译为动态库，然后将其他 Metal 库链接到该动态库，从而为实用函数提供单一来源。

本文介绍如何通过 Metal 编译器从命令行构建动态库、添加二进制归档，然后将动态库链接到其他 Metal 库。你的 App 在运行时加载已链接的库。本文代码示例中使用以下文件名：

- `utilities.metal`，一个包含实用函数的 Metal 源文件
- `shaders.ir`，由 Metal 编译器生成的中间表示（intermediate representation，IR），其中包含调用 `utilities.metal` 中函数的着色器

有关如何编译 Metal 中间表示的说明，请参阅[通过预编译源文件构建着色器库](building-a-shader-library-by-precompiling-source-files.md)。有关在运行时构建和链接动态库的 App 示例，请参阅[创建 Metal 动态库](creating-a-metal-dynamic-library.md)。

### 将着色器编译为动态库

首先将实用函数编译为动态库。使用 `metal` 命令行工具，并添加 `-dynamiclib` 和 `-install_name` 选项。`-dynamiclib` 标志将输出构建为动态库，而 `-install_name` 是链接器用于解析库的库名称。以下编译器调用将 `utilities.metal` 构建为动态库 `libUtility.ir.metallib`，并以 `Utility` 作为库的名称链接该库：

```shell
% xcrun -sdk macosx metal -dynamiclib utilities.metal -o libUtility.ir.metallib -install_name libUtility.metallib
```

> [!important] 重要
> 确保安装名称使用 l`ib${LIBRARY_NAME}.metallib` 的格式。否则，Metal 链接器无法定位你的动态库。

### 可选地向动态库添加二进制归档

二进制归档（binary archives）是针对你在编译时指定的 GPU 的预构建着色器函数。当你需要在分发更大的 App 文件与避免运行时从 Metal IR 编译着色器的开销之间进行权衡时，可以使用二进制归档。有关二进制归档的更多信息，请参阅 [Metal 二进制归档](metal-binary-archives.md)。

Metal 翻译器（Metal translator）允许你在 Metal IR 切片的基础上，创建一个包含 GPU 特定二进制的动态库。下面的示例提供了 `metal-tt` 用来将 Metal 3 二进制添加到 `libUtility.metalir.metallib` 的命令行参数。然后，合并后的输出写入到 `libUtility.metallib`。

```shell
% xcrun -sdk macosx metal-tt libUtility.metalir.metallib -o libUtility.metallib $(xcrun -sdk macosx metal-config --native-arch-flags --gpu-family=metal3)
```

有关 `metal-config` 的更多信息，请在终端中运行 `man metal-config`。

有关 Metal 翻译器以及如何自定义从 Metal IR 文件构建哪些二进制的更多信息，请参阅[从设备构建的管线状态对象创建二进制归档](creating-binary-archives-from-device-built-pipeline-state-objects.md)和[从自定义配置脚本编译二进制归档](compiling-binary-archives-from-a-custom-configuration-script.md)。

### 将实用函数着色器链接到 Metal 库

将动态库预链接到其他库，可以避免与解析要从动态库加载的符号相关的一些运行时开销。在编译最终要分发的 Metal 库时，请将 `-L` 和 `-l` 链接器选项与 `metal` 命令行工具一起使用。`-l` 选项提供要链接到的库的名称，`-L` 提供自定义库搜索路径。以下代码示例演示了将中间表示 `shaders.ir` 链接到上一步编译的 `Utilities` 库。如果跳过将二进制编译到动态库中，请将 `libUtility.metalir.metallib` 重命名为 `libUtility.metallib`。

```shell
% # Uncomment the next line to rename the library if you need to.
% # mv libUtility.metalir.metallib libUtility.metallib
% xcrun -sdk macosx metal shaders.ir -o shaders.metallib -lUtility -L ./
```

将 `shaders.metallib` 和 `libUtility.metallib` 作为资源添加到你的 Xcode 项目。如果你通过命令行链接动态库，为了使其正确加载，请将其放置在 App 资源中与 `-L` 参数设置的路径相对应的位置。在此示例中，将 `shaders.metallib` 和 l`ibUtility.metallib` 放在同一资源包中的同一目录下。

### 在 App 中加载动态库

在你的 App 中使用 [- newDynamicLibraryWithURL:error:](<mtldevice/makedynamiclibrary(url_).md>) 方法来加载你的 Metal 动态库，然后将其添加到管线描述符中，以便调用其他 Metal 库中的着色器函数。以下代码示例加载了一个动态库，并创建了一个 [MTLComputePipelineDescriptor](mtlcomputepipelinedescriptor.md) 将其作为要加载的库包含在内：

**Swift**

```swift
fn createComputePipeline(descriptor: MTLComputePipelineDescriptor, dynamicLibrary: URL, device: MTLDevice) throws -> MTLComputePipeline {
    let library = device.makeDynamicLibrary(url: dynamicLibrary)

    var newDescriptor = descriptor.copy()
    newDescriptor.insertLibraries.append(library)

    return device.makeComputePipelineState(descriptor: newDescriptor, options: MTLCompilationOption(rawValue: 0), nil)
}
```

**Objective-C**

```objective-c
-(id<MTLComputePipeline>) createComputePipelineFromDescriptor:(MTLComputePipelineDescriptor*)pipelineDescriptor withDynamicLibrary:(NSURL*)libraryURL forDevice:(id<MTLDevice>)device error:(NSError**) {
    id<MTLDynamicLibrary> library = [device newDynamicLibraryWithURL:libraryURL error:error];
    if (library == nil) {
        return nil;
    }

    MTLComputePipelineDescriptor* newDescriptor = [pipelineDescriptor copy];
    newDescriptor.insertLibraries = [pipelineDescriptor.insertLibraries arrayByAddingObject:library];

    id<MTLComputePipelineState> computePipeline = [device newComputePipelineStateWithDescriptor: newDescriptor options: MTLPipelineOptionNone reflection: nil error: error];
    return computePipeline;
}
```

## 另请参阅

### 使用 Metal 动态库

- [创建 Metal 动态库](creating-a-metal-dynamic-library.md) — 编译一个着色器库并将其作为动态链接的库写入文件。
