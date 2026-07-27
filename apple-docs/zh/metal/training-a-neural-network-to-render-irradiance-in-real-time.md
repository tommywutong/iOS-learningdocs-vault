---
title: 训练一个神经网络以实时渲染辐照度
framework: Metal
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [macOS 26.0+, Xcode 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/training-a-neural-network-to-render-irradiance-in-real-time
source_url: 'https://developer.apple.com/documentation/metal/training-a-neural-network-to-render-irradiance-in-real-time'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/training-a-neural-network-to-render-irradiance-in-real-time.json'
content_hash: 'sha256:006f2fbed2882857'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Metal](../metal.md) · [Metal sample code library](metal-sample-code-library.md)

# 训练一个神经网络以实时渲染辐照度

<sub>示例代码</sub>

在 GPU 上训练一个小型神经网络来近似漫反射辐照度，并将结果与蒙特卡罗积分和一个预训练的 ML 模型进行比较。

## 概述

此示例渲染了一个由 HDR 环境贴图照亮的 PBR 球体，使用三种不同的技术逐像素计算漫反射辐照度，你可以在运行时在它们之间切换：

- **Monte Carlo（蒙特卡罗）** 每帧对每个像素的半球进行积分，生成一个真值参考。
- **MPP** 在启动时使用 Metal Performance Primitives 协同矩阵运算，在 GPU 上训练一个轻量级 MLP，然后逐像素对其求值。
- **ML Encoder** 通过 `MTL4MachineLearningCommandEncoder` 分派一个预训练的 Core ML 模型。

该渲染器使用三阶段的延迟渲染方式。几何阶段将世界空间法线和材质参数光栅化到纹理中。所选的辐照度技术随后以这些法线作为输入，输出一个包含辐照度值的张量。合成阶段随后使用 Cook-Torrance BRDF 计算直接光照，加上来自辐照度张量的间接光照，然后对结果进行色调映射。

### 配置示例代码项目

要运行此示例，你需要：

- 一台运行 macOS 26 或更高版本的 Mac
- Xcode 26 或更高版本

> [!note] 注意
> 此示例需要 Metal 4。

### 在 GPU 上训练

当选择 MPP 技术时，该示例会通过蒙特卡罗积分生成 512 组真值法线/辐照度对，然后每帧使用一个三层 MLP 运行多次训练迭代。该 MLP 有 3 个输入（法线 xyz）、2 个各含 16 个神经元的隐藏层，以及 3 个输出（辐照度 rgb）。输入层被填充至 16 个元素，输出层被填充至 8 个元素，辐照度值会在对数空间与原始空间之间相互转换，以保证数值稳定性。

前向传播使用张量运算和协同张量，跨一个 SIMD 组协同对网络求值，其中 32 个线程同时处理 32 个像素。反向传播以类似的方式工作，计算权重梯度，并通过每一层传播激活梯度，优化器采用 Adam。

### 使用 PyTorch 进行离线训练

当选择 ML Encoder 技术时，会使用一个 `MTL4MachineLearningCommandEncoder` 来执行同一个 MLP 网络的预训练版本。与 MPP 方式不同，预训练网络不会跳过空像素，因此这种技术效率较低，但要简单得多。

`train_irradiance.py` 脚本实现了 `Irradiance.metal` 中的蒙特卡罗积分，可用于使用 PyTorch 重新生成离线模型（`Irradiance.mtlpackage`）。运行方式如下：

```
uv run ./train_irradiance.py
```

## 另请参阅

### 机器学习工作流程

- [在 GPU 时间线上运行机器学习模型](running-a-machine-learning-model-on-the-gpu-timeline.md) — 在 Metal 4 命令缓冲区中，通过机器学习阶段分派模型推理命令。
- [使用 Metal 4 在着色器中运行内联 ML 操作](running-inline-ml-operations-in-a-shader-with-metal-4.md) — 通过内联张量运算，在多个 GPU 核心上进行矩阵相乘。

## 下载

- [TrainingANeuralNetworkToRenderIrradianceInRealTime.zip](https://docs-assets.developer.apple.com/published/210b0e935e71/TrainingANeuralNetworkToRenderIrradianceInRealTime.zip)
