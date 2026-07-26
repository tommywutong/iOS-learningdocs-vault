---
title: 在 Swift 中以延迟光照渲染场景
framework: Metal
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, Xcode 26.3+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/rendering-a-scene-with-deferred-lighting-in-swift
source_url: 'https://developer.apple.com/documentation/metal/rendering-a-scene-with-deferred-lighting-in-swift'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/rendering-a-scene-with-deferred-lighting-in-swift.json'
content_hash: 'sha256:33e7af66694e52de'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Metal](../metal.md) · [Metal sample code library](metal-sample-code-library.md)

# 在 Swift 中以延迟光照渲染场景

<sub>示例代码</sub>

通过实现一个针对即时模式渲染器和基于瓦片的延迟渲染器 GPU 进行优化的延迟光照渲染器，避免昂贵的光照计算。

## 概述

本示例演示了一个延迟光照渲染器，它使用阴影贴图实现阴影，并使用模板缓冲区剔除光照体积。

![示例 App 运行时展示丰富光照效果的屏幕截图。](../../../attachments/b57c4c654a8c9cf836ff539a70bfeb59/deferred-lighting-swift-1-DeferredLighting.png)

与前向光照相比，延迟光照能更轻松地渲染大量光源。例如，使用前向光照时，在一个包含大量光源的场景中，让每个片段都计算每个光源的贡献是不现实的。此时需要实现复杂的排序和分箱算法，将光照贡献的计算限制在影响每个片段的光源上。而使用延迟光照，可以轻松地将多个光源应用到场景中。

### 配置示例代码项目

该 Xcode 项目包含用于在 macOS、iOS 或 tvOS 上运行示例的 scheme。默认 scheme 是 macOS，它会在你的 Mac 上按原样运行该示例。

> [!note] 注意
> 将渲染目标拆分为独立的组以执行片段函数，需要一台支持光栅顺序组（raster order group）的 macOS 或 iOS 设备。查询你设备的 `rasterOrderGroupsSupported` 属性以确定是否支持。

该示例包含以下预处理器条件，你可以修改它们来控制该 App 的配置。

**AAPLConfig.h**

```objective-c
#define USE_EYE_DEPTH              1
#define LIGHT_STENCIL_CULLING      1
```

它们对该 App 行为的影响如下：

- `USE_EYE_DEPTH` — 启用时，将眼空间中的深度值写入几何缓冲区的深度分量。这使延迟阶段能更轻松地计算眼空间中的片段位置以应用光照。禁用时，屏幕深度会被写入几何缓冲区的深度分量，此时在延迟阶段计算光照贡献还需要一次从屏幕空间到眼空间的额外逆变换。
- `LIGHT_STENCIL_CULLING` — 启用时，使用模板缓冲区来避免对与 3D 光照体积不相交的片段执行光照计算。禁用时，GPU 会为屏幕空间中受某个光源覆盖的所有片段计算光照。这意味着需要进行昂贵光照计算的片段数量，会远超实际所需的数量。

### 回顾重要概念

在开始使用该示例 App 之前，先回顾以下概念，以便更好地理解延迟光照渲染器的关键细节以及 Metal 的一些独特特性。

**传统的延迟光照渲染器**

传统的延迟光照渲染器通常分为两个渲染通道：

- **第一个通道：几何缓冲区渲染。** 渲染器绘制并变换场景中的模型，片段函数将结果渲染到一组称为 _几何缓冲区_（geometry buffer，简称 _g-buffer_）的纹理中。几何缓冲区包含来自模型的材质颜色，以及逐片段的法线、阴影和深度值。
- **第二个通道：延迟光照与合成。** 渲染器绘制每个光照体积，使用几何缓冲区数据重建每个片段的位置并应用光照计算。在绘制各个光源时，每个光源的输出都会与之前光源的输出叠加混合。最后，渲染器通过执行一个全屏四边形或一个计算内核，将阴影和方向光照等其他数据合成到场景中。

![展示传统延迟光照算法中两个渲染通道输出的示意图。](../../../attachments/bb16b6059e1d10fa353fb7491b0fa3c4/deferred-lighting-swift-2-TraditionalDeferredLighting.png)

> [!note] 注意
> 部分 macOS GPU 采用 _即时模式渲染_（immediate mode rendering，IMR）架构。在 IMR GPU 上，延迟光照渲染器至少需要两个渲染通道才能实现。因此，该示例为该 App 的 macOS 版本实现了一个两通道的延迟光照算法。由于 iOS 和 tvOS 模拟器运行在 macOS 的 Metal 实现之上，因此它们同样使用这种两通道延迟光照算法。

**Apple 芯片 GPU 上的单通道延迟光照**

所有 iOS 和 tvOS 设备以及现在部分 macOS 设备上的 Apple 芯片 GPU，采用基于瓦片的延迟渲染（tile-based deferred rendering，TBDR）架构，这使它们能够将数据渲染到 GPU 内部的瓦片内存中。通过渲染到瓦片内存，设备可以避免 GPU 与系统内存之间（经由带宽受限的内存总线）潜在的高开销往返。GPU 是否会将瓦片内存写入系统内存，取决于以下配置：

- App 渲染命令编码器的存储操作。
- App 纹理的存储模式。

当存储操作设置为 `MTLStoreAction.store` 时，渲染通道的渲染目标的输出数据会从瓦片内存写入系统内存，渲染目标由纹理支持。如果这些数据随后被用于后续的渲染通道，则来自这些纹理的输入数据会从系统内存读取到 GPU 中的纹理缓存里。因此，一个访问系统内存的传统延迟光照渲染器，需要在第一个和第二个渲染通道之间将几何缓冲区数据存储到系统内存中。

![](../../../attachments/f2c124cf30e70158df0c358057d5526c/deferred-lighting-swift-3-TraditionalDeferredLightingOnTBDR.png)

<sub>展示传统延迟光照算法中几何缓冲区数据如何在 GPU 与系统内存之间传输的示意图。</sub>

不过，由于 TBDR 架构，Apple 芯片 GPU 也可以在任意时刻从瓦片内存中读取数据。这使得片段着色器能够在瓦片内存中的渲染目标数据再次被写入之前，对其进行读取和计算。这项特性使该示例得以避免在第一个和第二个渲染通道之间将几何缓冲区数据存储到系统内存中；因此，延迟光照渲染器可以只用一个渲染通道来实现。

几何缓冲区数据只由 GPU 在单个渲染通道内产生并消费，而不涉及 CPU。因此，这些数据既不会在渲染通道开始前从系统内存加载，也不会在渲染通道结束后存储到系统内存中。光照片段函数不是从系统内存中的纹理读取几何缓冲区数据，而是在几何缓冲区仍作为渲染目标附加到该渲染通道时直接读取其数据。因此，无需为几何缓冲区纹理分配系统内存，这些纹理都可以声明为 `MTLStorageMode.memoryless` 存储模式。

![展示单通道延迟光照算法中几何缓冲区数据如何在瓦片内存中被访问的示意图。](../../../attachments/ef0f59c934f11dc0faad9b37bfe5d269/deferred-lighting-swift-4-SinglePassDeferredLightingOnTBDR.png)

> [!note] 注意
> 允许 TBDR GPU 在片段函数中读取已附加渲染目标的这一特性，也被称为 _可编程混合_（programmable blending）。

**使用光栅顺序组实现延迟光照**

默认情况下，当一个片段着色器向某个像素写入数据时，GPU 会等待该着色器完全写完该像素之后，才开始为同一像素执行另一个片段着色器。

![展示在没有光栅顺序组的情况下，片段着色器执行两个光源的示意图。](../../../attachments/82a3a4f44d2a51fdead28bb54a2eda50/deferred-lighting-swift-5-DeferredLightingWithoutRasterOrderGroups.png)

光栅顺序组让 App 能够提高 GPU 片段着色器的并行度。借助光栅顺序组，一个片段函数可以将渲染目标划分到不同的执行组中。这种划分使 GPU 能够在另一组中片段着色器的前一个实例尚未完成向像素写入数据之前，读取并计算这一组中的渲染目标数据。

![展示在使用光栅顺序组的情况下，片段着色器执行两个光源的示意图。](../../../attachments/4bc70e042db17895e6cec98e56ea7b76/deferred-lighting-swift-6-DeferredLightingWithRasterOrderGroups.png)

在本示例中，部分光照片段函数使用了以下光栅顺序组：

- **光栅顺序组 0。** `AAPLLightingROG` 用于包含光照计算结果的渲染目标。
- **光栅顺序组 1。** `AAPLGBufferROG` 用于光照函数中的几何缓冲区数据。

这些光栅顺序组使 GPU 能够在片段着色器中读取几何缓冲区并执行光照计算，而无需等待前一个片段着色器实例的光照计算完成对其输出数据的写入。

### 渲染一帧延迟光照画面

该示例按以下顺序渲染每个完整帧的各个阶段：

1. 阴影贴图
2. 几何缓冲区
3. 方向光
4. 光照掩码
5. 点光源
6. 天空盒
7. 仙灵光

该示例的单通道延迟渲染器在一个渲染通道中生成几何缓冲区，并执行所有后续阶段。这种单通道实现之所以可行，得益于 iOS 和 tvOS GPU 的 TBDR 架构，它允许设备从瓦片内存中的渲染目标读取几何缓冲区数据。

**SinglePassDeferredRenderer.swift**

```swift
encodePass(into: commandBuffer, using: gBufferAndLightingPassDescriptor, label: "GBuffer & Lighting Pass") { renderEncoder in

    encodeGBufferStage(using: renderEncoder)
    encodeDirectionalLightingStage(using: renderEncoder)
    encodeLightMaskStage(using: renderEncoder)
    encodePointLightStage(using: renderEncoder)
    encodeSkyboxStage(using: renderEncoder)
    encodeFairyBillboardStage(using: renderEncoder)
}
```

该示例的传统延迟渲染器在一个渲染通道中生成几何缓冲区，然后在另一个渲染通道中执行所有后续阶段。这种两通道实现对于使用 IMR 架构的 GPU 是必需的，因为这类 GPU 不支持在片段函数中读取渲染目标的颜色数据。

**TraditionalDeferredRenderer.swift**

```swift
encodePass(into: commandBuffer,
           using: gBufferPassDescriptor,
           label: "GBuffer Generation Pass") { renderEncoder in

            encodeGBufferStage(using: renderEncoder)
}
```

```swift
encodePass(into: commandBuffer,
           using: lightingPassDescriptor,
           label: "Lighting Pass") { (renderEncoder) in

            encodeDirectionalLightingStage(using: renderEncoder)
            encodeLightMaskStage(using: renderEncoder)
            encodePointLightStage(using: renderEncoder)
            encodeSkyboxStage(using: renderEncoder)
            encodeFairyBillboardStage(using: renderEncoder)
}
```

### 渲染阴影贴图

该示例通过从光源（太阳）的视角渲染模型，为场景中唯一的方向光渲染阴影贴图。

![展示阴影贴图的渲染效果。](../../../attachments/12a52f863370a51de55d4ae8dea30d20/deferred-lighting-swift-7-ShadowMap.png)

阴影贴图的渲染管线有顶点函数但没有片段函数；因此，该示例无需执行渲染管线的更多阶段，就能确定写入阴影贴图的屏幕空间深度值。（此外，由于没有片段函数，这次渲染执行得很快。）

**PipelineStates.swift**

```swift
lazy var shadowGeneration = makeRenderPipelineState(label: "Shadow Generation Stage") { descriptor in
    descriptor.vertexFunction = library.makeFunction(name: "shadow_vertex")
    descriptor.depthAttachmentPixelFormat = .depth32Float
}
```

在为阴影贴图绘制几何体之前，该示例设置了一个深度偏移值，以减少阴影伪影：

**Renderer.swift**

```swift
renderEncoder.setDepthBias(0.015, slopeScale: 7, clamp: 0.02)
```

然后，在几何缓冲区阶段的片段函数中，该示例测试该片段是否被遮挡并处于阴影中：

**AAPLGBuffer.metal**

```metal
// Compare the depth value in the shadow map to the depth value of the fragment in the sun's.
// frame of reference.  If the sample is occluded, it will be zero.
float shadow_sample = shadowMap.sample_compare(shadowSampler, in.shadow_coord.xy, in.shadow_coord.z);
```

该示例将 `sample_compare` 函数的结果存储在 `normal_shadow` 渲染目标的 `w` 分量中：

**AAPLGBuffer.metal**

```metal
gBuffer.normal_shadow = half4(eye_normal.xyz, shadow_sample);
```

在方向光和点光源的合成阶段，该示例从几何缓冲区读取阴影值并将其应用到片段上。

### 渲染几何缓冲区

该示例的几何缓冲区包含以下纹理：

- `albedoSpecular`，存储反照率（albedo）和高光（specular）数据。反照率数据存储在 `x`、`y`、`z` 分量中；高光数据存储在 `w` 分量中。
- `normalShadow`，存储法线和阴影数据。法线数据存储在 `x`、`y`、`z` 分量中；阴影数据存储在 `w` 分量中。
- `depth`，存储眼空间中的深度值。

![展示几何缓冲区纹理的渲染效果。](../../../attachments/5a41635942f1a18ca12ec170a704cc37/deferred-lighting-swift-8-GBufferTextures.png)

在该示例渲染几何缓冲区时，传统延迟渲染器和单通道延迟渲染器都会将所有几何缓冲区纹理作为该渲染通道的渲染目标附加上去。不过，由于使用 TBDR 架构的设备既能渲染几何缓冲区，也能在同一个渲染通道中读取它，该示例以 memoryless 存储模式创建几何缓冲区纹理，这表示不会为这些纹理分配系统内存。相反，这些纹理只在该渲染通道持续期间于瓦片内存中被分配和填充。

该示例在通用的 `drawableSizeWillChange` 计算属性的实现中创建几何缓冲区纹理，但单通道延迟渲染器将 `storageMode` 变量设置为 `MTLStorageMode.memoryless`，而传统延迟渲染器则将其设置为 `MTLStorageMode.private`。

**SinglePassDeferredRenderer.swift**

```swift
var storageMode = MTLStorageMode.private
```

对于传统延迟渲染器，在该示例完成向几何缓冲区纹理写入数据后，它会调用 `endEncoding` 方法来完成几何缓冲区渲染通道。由于该渲染命令编码器的存储操作被设置为 `MTLStoreAction.store`，GPU 会在该编码器完成执行时，将每个渲染目标纹理写入显存。这使得该示例能够在随后的延迟光照与合成渲染通道中从显存读取这些纹理。

对于单通道延迟渲染器，在该示例完成向几何缓冲区纹理写入数据后，该示例不会完成该渲染命令编码器，而是继续将其用于后续阶段。

### 应用方向光照和阴影

该示例将方向光照和阴影应用到最终要显示的可绘制对象上。

传统延迟渲染器从作为片段函数参数设置的纹理中读取几何缓冲区数据：

**AAPLDirectionalLight.metal**

```metal
fragment half4
deferred_directional_lighting_fragment_traditional(
    QuadInOut                in                      [[ stage_in ]],
    constant AAPLFrameData & frameData               [[ buffer(AAPLBufferFrameData) ]],
    texture2d<half>          albedo_specular_GBuffer [[ texture(AAPLRenderTargetAlbedo) ]],
    texture2d<half>          normal_shadow_GBuffer   [[ texture(AAPLRenderTargetNormal) ]],
    texture2d<float>         depth_GBuffer           [[ texture(AAPLRenderTargetDepth)  ]])
```

单通道延迟渲染器从附加到该渲染通道的渲染目标中读取几何缓冲区数据：

**AAPLShaderCommon.h**

```metal
struct GBufferData
{
    half4 lighting        [[color(AAPLRenderTargetLighting), raster_order_group(AAPLLightingROG)]];
    half4 albedo_specular [[color(AAPLRenderTargetAlbedo),   raster_order_group(AAPLGBufferROG)]];
    half4 normal_shadow   [[color(AAPLRenderTargetNormal),   raster_order_group(AAPLGBufferROG)]];
    float depth           [[color(AAPLRenderTargetDepth),    raster_order_group(AAPLGBufferROG)]];
};
```

**AAPLDirectionalLight.metal**

```metal
deferred_directional_lighting_fragment_single_pass(
    QuadInOut                in        [[ stage_in ]],
    constant AAPLFrameData & frameData [[ buffer(AAPLBufferFrameData) ]],
    GBufferData              GBuffer)
```

尽管这些片段函数的输入不同，它们在 `deferred_directional_lighting_fragment_common` 片段函数中共用同一份实现。该函数执行以下操作：

- 从几何缓冲区的法线数据重建法线，以计算漫反射项。
- 从几何缓冲区的深度数据重建眼空间位置，以应用镜面高光。
- 使用几何缓冲区的阴影数据使片段变暗，将阴影应用到场景中。

由于这是第一个渲染到可绘制对象的阶段，iOS 和 tvOS 渲染器会在此前的几何缓冲区阶段之前就获取一个可绘制对象，以便该可绘制对象能与后续阶段的输出合并。而传统延迟渲染器则会将获取可绘制对象的时机延迟到几何缓冲区阶段完成之后、方向光阶段开始之前。这种延迟减少了该 App 持有可绘制对象的时间，从而提升了性能。

> [!note] 注意
> 由于 `DepthStencilStates` 对象的 `directionalLighting` 属性的状态，`deferred_directional_lighting_fragment` 系列函数只会为应当被照亮的片段执行。这项优化虽然简单，却很重要，能节省大量片段着色器的执行周期。

### 剔除光照体积

该示例创建了一个模板遮罩，用于避免对许多片段执行开销高昂的光照计算。它通过使用几何缓冲区阶段生成的深度缓冲区和模板缓冲区，来追踪某个光照体积是否与任何几何体相交（如果没有相交，那么它就没有照射到任何东西）来创建这个模板遮罩。

在 `encodeLightMaskStage` 的实现中，该示例设置了 `PipelineStates` 类的 `lightMask` 对象，并编码一次实例化绘制调用，只绘制包裹点光源体积的二十面体的背面。如果该绘制调用中的某个片段未通过深度测试，就表明该二十面体的背面处于某些几何体之后。

**Renderer.swift**

```swift
renderEncoder.setRenderPipelineState(lightMaskPipelineState)
renderEncoder.setDepthStencilState(lightMaskDepthStencilState)

renderEncoder.setStencilReferenceValue(128)
renderEncoder.setCullMode(.front)

renderEncoder.setVertexBuffer(scene.frameData,
                              offset: 0,
                              index: Int(AAPLBufferFrameData.rawValue))

renderEncoder.setVertexBuffer(scene.pointLights,
                              offset: 0,
                              index: Int(AAPLBufferIndexLightsData.rawValue))

renderEncoder.setVertexBuffer(scene.lightPositions,
                              offset: 0,
                              index: Int(AAPLBufferIndexLightsPosition.rawValue))

renderEncoder.setFragmentBuffer(scene.frameData,
                                offset: 0,
                                index: Int(AAPLBufferFrameData.rawValue))

renderEncoder.draw(meshes: [scene.icosahedron],
                   instanceCount: scene.numberOfLights,
                   requiresMaterials: false)
```

`lightMask` 管线对象没有片段函数，因此该渲染管线不会写入任何颜色数据。然而，由于设置了 `lightMask` 的深度和模板状态，任何未通过深度测试的片段都会使该片段的模板缓冲区值递增。包含几何体的片段的起始深度值为 `128`，这是该示例在几何缓冲区阶段设置的。因此，在设置了 `lightMask` 深度和模板状态期间，任何未通过深度测试的片段，其深度值都会递增到大于 `128`。（由于启用了正面剔除，一个未通过深度测试且值大于 `128` 的片段，表明该二十面体至少有背面一半处于所有几何体之后。）

在下一次绘制调用中，即 `encodePointLightStage` 的实现里，该示例将点光源的贡献应用到可绘制对象上。该示例测试该二十面体的正面是否处于所有几何体之前，以此判断该体积是否与某些几何体相交，从而判断该片段是否应当被照亮。为该绘制调用设置的深度和模板状态 `pointLight`，只有当该片段的模板值大于参考值 `128` 时才会执行片段函数。（由于模板测试值被设置为 `MTLCompareFunction.less`，该示例只有在参考值 `128` 小于模板缓冲区中的值时才会通过测试。）

**Renderer.swift**

```swift
renderEncoder.setRenderPipelineState(pipelineStates.pointLighting)
renderEncoder.setDepthStencilState(depthStencilStates.pointLighting)

if !device.supportsFamily(.apple1) {
    scene.setGBufferTextures(renderEncoder: renderEncoder)
}

renderEncoder.setStencilReferenceValue(128)
renderEncoder.setCullMode(.back)

renderEncoder.setVertexBuffer(scene.frameData,
                              offset: 0,
                              index: Int(AAPLBufferFrameData.rawValue))

renderEncoder.setVertexBuffer(scene.pointLights,
                              offset: 0,
                              index: Int(AAPLBufferIndexLightsData.rawValue))

renderEncoder.setVertexBuffer(scene.lightPositions,
                              offset: 0,
                              index: Int(AAPLBufferIndexLightsPosition.rawValue))

renderEncoder.setFragmentBuffer(scene.frameData,
                                offset: 0,
                                index: Int(AAPLBufferFrameData.rawValue))

renderEncoder.setFragmentBuffer(scene.pointLights,
                                offset: 0,
                                index: Int(AAPLBufferIndexLightsData.rawValue))

renderEncoder.setFragmentBuffer(scene.lightPositions,
                                offset: 0,
                                index: Int(AAPLBufferIndexLightsPosition.rawValue))

renderEncoder.draw(meshes: [scene.icosahedron],
                   instanceCount: scene.numberOfLights,
                   requiresMaterials: false)
```

由于 `encodeLightMaskStage` 中的绘制调用会使处于任何几何体之后的片段的模板值递增，该示例只会对同时满足以下两个条件的片段执行片段函数：

- 正面通过深度测试、处于某些几何体之前的片段。
- 背面未通过深度测试、处于某些几何体之后的片段。

以下示意图展示了使用该模板遮罩算法渲染的一帧与未使用该算法渲染的一帧之间，片段覆盖范围的差异。启用该算法时，绿色像素是执行了点光源片段函数的像素。

![展示启用模板遮罩时点光源片段覆盖范围的渲染效果。](../../../attachments/b50b2dbf65424a8afffeeffa5c4a13ec/deferred-lighting-swift-9-StencilMaskOnly.png)

禁用该算法时，绿色和红色像素都是执行了点光源片段函数的像素。

![展示禁用模板遮罩时点光源片段覆盖范围的渲染效果。](../../../attachments/285a44a90bdba37c7a9adf4245d17cf2/deferred-lighting-swift-10-StencilMaskVSFullVolumes.png)

### 渲染天空盒和仙灵光

在最后的光照阶段中，该示例为场景应用更简单的光照技术。

该示例针对神庙的几何体对天空盒应用深度测试，因此渲染器只会渲染到可绘制对象中尚未被任何几何体填充的区域。

**Renderer.swift**

```swift
renderEncoder.setRenderPipelineState(pipelineStates.skybox)
renderEncoder.setDepthStencilState(depthStencilStates.skybox)

renderEncoder.setCullMode(.front)

renderEncoder.setVertexBuffer(scene.frameData, offset: 0, index: Int(AAPLBufferFrameData.rawValue))
renderEncoder.setFragmentTexture(scene.skyMap, index: Int(AAPLTextureIndexBaseColor.rawValue))

renderEncoder.draw(meshes: [scene.skyMesh],
                   requiresMaterials: false)
```

该示例将仙灵光以 2D 圆形渲染到可绘制对象上，并使用一张纹理来确定其片段的 alpha 混合系数。

**AAPLFairy.metal**

```metal
half4 c = colorMap.sample(linearSampler, float2(in.tex_coord));

half3 fragColor = in.color * c.x;

return half4(fragColor, c.x);
```

## 另请参阅

### 光照技术

- [Rendering a scene with forward plus lighting using tile shaders](rendering-a-scene-with-forward-plus-lighting-using-tile-shaders.md) — 使用 Apple GPU 上的最新特性实现一个前向+渲染器。
- [Rendering a scene with deferred lighting in Objective-C](rendering-a-scene-with-deferred-lighting-in-objective-c.md) — 通过实现一个针对即时模式渲染器和基于瓦片的延迟渲染器 GPU 进行优化的延迟光照渲染器，避免昂贵的光照计算。
- [Rendering a scene with deferred lighting in C++](rendering-a-scene-with-deferred-lighting-in-c++.md) — 通过实现一个针对即时模式渲染器和基于瓦片的延迟渲染器 GPU 进行优化的延迟光照渲染器，避免昂贵的光照计算。
- [Rendering reflections with fewer render passes](rendering-reflections-with-fewer-render-passes.md) — 使用图层选择来减少生成环境贴图所需的渲染通道数量。

## 下载

- [RenderingASceneWithDeferredLightingInSwift.zip](https://docs-assets.developer.apple.com/published/badbf3ddc465/RenderingASceneWithDeferredLightingInSwift.zip)
