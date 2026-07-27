---
title: 管线状态创建
framework: Metal
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/pipeline-state-creation
source_url: 'https://developer.apple.com/documentation/metal/pipeline-state-creation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/pipeline-state-creation.json'
content_hash: 'sha256:54606c64b031e693'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Metal](../metal.md) · [GPU devices and work submission](gpu-devices-and-work-submission.md) · [MTLDevice](mtldevice.md)

# 管线状态创建

<sub>API 集合</sub>

为渲染流程和计算流程、采样器、深度与模板状态，以及间接命令缓冲区创建管线状态。

## 概述

使用这些方法为渲染流程或计算流程创建各种状态类型的实例（分别参阅[渲染流程](render-passes.md)和[计算流程](compute-passes.md)）。

你可以为单个渲染流程编码器（[MTLRenderCommandEncoder](mtlrendercommandencoder.md)）创建多个 [MTLRenderPipelineState](mtlrenderpipelinestate.md) 实例，每个实例分别应用于不同类型的渲染命令。例如，单个渲染流程可以先渲染带有顶点的图元，再渲染网格，最后以一条瓦片着色器命令收尾，每种情况使用不同的管线。要创建这些管线，请配置 [MTLRenderPipelineDescriptor](mtlrenderpipelinedescriptor.md)、[MTLMeshRenderPipelineDescriptor](mtlmeshrenderpipelinedescriptor.md) 和 [MTLTileRenderPipelineDescriptor](mtltilerenderpipelinedescriptor.md) 的实例。然后分别将这些描述符传递给 [- newRenderPipelineStateWithDescriptor:completionHandler:](<mtldevice/makerenderpipelinestate(descriptor_completionhandler_).md>)、[- newRenderPipelineStateWithMeshDescriptor:options:completionHandler:](<mtldevice/makerenderpipelinestate(descriptor_options_completionhandler_)-1wvya.md>) 和 [- newRenderPipelineStateWithTileDescriptor:options:completionHandler:](<mtldevice/makerenderpipelinestate(tiledescriptor_options_completionhandler_).md>) 方法（或对应的方法）。

> [!important] 重要
> 只在你需要反射信息（参阅 [MTLRenderPipelineReflection](mtlrenderpipelinereflection.md)）时才创建反射实例，因为每一个反射实例都可能需要占用大量内存。

## 主题

### 使用顶点着色器创建渲染管线状态

- [- newRenderPipelineStateWithDescriptor:error:](<mtldevice/makerenderpipelinestate(descriptor_).md>) — 同步创建一个渲染管线状态。
- [- newRenderPipelineStateWithDescriptor:completionHandler:](<mtldevice/makerenderpipelinestate(descriptor_completionhandler_).md>) — 异步创建一个渲染管线状态。
- [makeRenderPipelineState(descriptor:options:)](<mtldevice/makerenderpipelinestate(descriptor_options_)-89vxc.md>) — 同步创建一个渲染管线状态，并以元组形式返回反射信息。
- [- newRenderPipelineStateWithDescriptor:options:reflection:error:](<mtldevice/makerenderpipelinestate(descriptor_options_reflection_).md>) — 同步创建一个渲染管线状态及其反射信息。
- [- newRenderPipelineStateWithDescriptor:options:completionHandler:](<mtldevice/makerenderpipelinestate(descriptor_options_completionhandler_)-5gdww.md>) — 异步创建一个渲染管线状态及其反射信息。

### 使用网格着色器创建渲染管线状态

- [makeRenderPipelineState(descriptor:options:)](<mtldevice/makerenderpipelinestate(descriptor_options_)-yrak.md>) — 同步创建一个网格渲染管线状态，并以元组形式返回反射信息。
- [- newRenderPipelineStateWithMeshDescriptor:options:completionHandler:](<mtldevice/makerenderpipelinestate(descriptor_options_completionhandler_)-1wvya.md>) — 异步创建一个网格渲染管线状态及其反射信息。

### 创建瓦片渲染管线状态

- [makeRenderPipelineState(tileDescriptor:options:)](<mtldevice/makerenderpipelinestate(tiledescriptor_options_).md>) — 同步创建瓦片着色器的渲染管线状态，并以元组形式返回反射信息。
- [- newRenderPipelineStateWithTileDescriptor:options:reflection:error:](<mtldevice/makerenderpipelinestate(tiledescriptor_options_reflection_).md>) — 同步创建瓦片着色器的渲染管线状态及其反射信息。
- [- newRenderPipelineStateWithTileDescriptor:options:completionHandler:](<mtldevice/makerenderpipelinestate(tiledescriptor_options_completionhandler_).md>) — 异步创建瓦片着色器的渲染管线状态及其反射信息。

### 创建计算管线状态

- [- newComputePipelineStateWithDescriptor:options:reflection:error:](<mtldevice/makecomputepipelinestate(descriptor_options_reflection_).md>) — 同步创建一个计算管线状态及其反射信息。
- [- newComputePipelineStateWithDescriptor:options:completionHandler:](<mtldevice/makecomputepipelinestate(descriptor_options_completionhandler_).md>) — 异步创建一个计算管线状态及其反射信息。
- [- newComputePipelineStateWithFunction:error:](<mtldevice/makecomputepipelinestate(function_).md>) — 使用一个函数实例同步创建一个计算管线状态。
- [- newComputePipelineStateWithFunction:completionHandler:](<mtldevice/makecomputepipelinestate(function_completionhandler_).md>) — 使用一个函数实例异步创建一个计算管线状态。
- [- newComputePipelineStateWithFunction:options:reflection:error:](<mtldevice/makecomputepipelinestate(function_options_reflection_).md>) — 使用一个函数实例同步创建一个计算管线状态及其反射信息。
- [- newComputePipelineStateWithFunction:options:completionHandler:](<mtldevice/makecomputepipelinestate(function_options_completionhandler_).md>) — 使用一个函数实例异步创建一个计算管线状态及其反射信息。

### 创建深度与模板状态

- [- newDepthStencilStateWithDescriptor:](<mtldevice/makedepthstencilstate(descriptor_).md>) — 创建一个深度-模板状态实例。

### 支持类型

- [MTLNewRenderPipelineStateCompletionHandler](mtlnewrenderpipelinestatecompletionhandler.md) — 某个方法完成渲染管线创建时调用的完成处理程序签名。
- [MTLNewRenderPipelineStateWithReflectionCompletionHandler](mtlnewrenderpipelinestatewithreflectioncompletionhandler.md) — 某个方法完成渲染管线及反射信息创建时调用的完成处理程序签名。
- [MTLNewComputePipelineStateCompletionHandler](mtlnewcomputepipelinestatecompletionhandler.md) — 某个方法完成计算管线创建时调用的完成处理程序签名。
- [MTLNewComputePipelineStateWithReflectionCompletionHandler](mtlnewcomputepipelinestatewithreflectioncompletionhandler.md) — 某个方法完成计算管线及反射信息创建时调用的完成处理程序签名。

## 另请参阅

### 使用 GPU 设备

- [Device inspection](device-inspection.md) — 定位并识别 GPU 及其支持的特性，并对其计数器进行采样。
- [Work submission](work-submission.md) — 创建向 GPU 提交工作的队列，或将资产加载到 GPU 资源中，以及创建将你的高频命令归组在一起的间接命令缓冲区。
- [Resource creation](resource-creation.md) — 使用输入/输出队列加载资产，并创建各种资源实例，比如缓冲区、纹理、加速结构和内存堆。
- [Shader library and archive creation](shader-library-and-archive-creation.md) — 创建静态和动态着色器库，以及二进制着色器归档。
