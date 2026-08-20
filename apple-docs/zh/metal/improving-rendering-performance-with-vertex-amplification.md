---
title: 使用顶点放大提高渲染性能
framework: Metal
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/improving-rendering-performance-with-vertex-amplification
source_url: 'https://developer.apple.com/documentation/metal/improving-rendering-performance-with-vertex-amplification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/improving-rendering-performance-with-vertex-amplification.json'
content_hash: 'sha256:1a77cc3159e44e61'
translated: true
---

> 导航：[技术](../technologies.md) · [Metal](../metal.md) · [渲染通道](render-passes.md)

# 使用顶点放大提高渲染性能

<sub>文章</sub>

执行使用相同顶点数据多次渲染到不同输出的绘制命令。

## 概述

使用*顶点放大（vertex amplification）*，你可以编码绘制命令，使每个顶点针对每个渲染目标处理多次。顶点放大为每个渲染管线生成命令顶点数据的副本。顶点放大比使用相同顶点多次编码命令更高效，因为 GPU 只获取一次顶点数据。然后，GPU 为每个顶点调用你的顶点函数多次——次数等于放大倍数。

![](../../../attachments/c63c5aa8cceb65dc6421201c86838cee/improving-rendering-performance-with-vertex-amplification-1@2x.png)

<sub>一个流程图，从顶点数据的单个实例开始，流入单个顶点阶段。然后，顶点阶段产生两个输出，流入两个独立的并行渲染管线实例。</sub>

例如，你可以使用顶点放大来实现级联阴影贴图，放大倍数等于级联级别数。

App 通常利用顶点放大将相同的顶点渲染到不同的纹理层或多个视口。有关这些技术的更多信息，请参见[在绘制命令中渲染到多个纹理切片](rendering-to-multiple-texture-slices-in-a-draw-command.md)和[在绘制命令中渲染到多个视口](rendering-to-multiple-viewports-in-a-draw-command.md)。

### 检查 GPU 是否支持顶点放大倍数

通过将整数值传递给 [MTLDevice](mtldevice.md) 实例的 [`- supportsVertexAmplificationCount:`](<mtldevice/supportsvertexamplificationcount(__).md>) 方法，确认 GPU 是否支持顶点放大的特定倍数。传递一个 `2` 或更大的放大倍数。值 `1` 无效，因为它实际上禁用了顶点放大。

> [!important] 重要
> 向 [`- supportsVertexAmplificationCount:`](<mtldevice/supportsvertexamplificationcount(__).md>) 方法传递 `1` 或更小的倍数会触发 API 验证错误。

你的 App 在运行时确认 GPU 支持顶点放大倍数后，就可以安全地配置管线状态以使用该倍数。

### 设置渲染管线描述符的最大顶点放大倍数

将 [MTLRenderPipelineDescriptor](mtlrenderpipelinedescriptor.md) 实例的 [maxVertexAmplificationCount](mtlrenderpipelinedescriptor/maxvertexamplificationcount.md) 属性配置为 GPU 支持的倍数。使用该描述符创建的任何编码器都可以支持 `[1, `[maxVertexAmplificationCount](mtlrenderpipelinedescriptor/maxvertexamplificationcount.md)`]` 范围内的任意顶点放大因子。

**Swift**

```swift
let pipelineStateDescriptor = MTLRenderPipelineDescriptor()
pipelineStateDescriptor.vertexFunction = vertexFunction
pipelineStateDescriptor.fragmentFunction = fragmentFunction
pipelineStateDescriptor.maxVertexAmplificationCount = 2

...
```

**Objective-C**

```objective-c
MTLRenderPipelineDescriptor *pipelineStateDescriptor = [[MTLRenderPipelineDescriptor alloc] init];
pipelineStateDescriptor.vertexFunction = vertexFunction;
pipelineStateDescriptor.fragmentFunction = fragmentFunction;
pipelineStateDescriptor.maxVertexAmplificationCount = 2;

...
```

继续配置你的管线描述符，并用它创建一个可以分配给渲染命令编码器的 [MTLRenderPipelineState](mtlrenderpipelinestate.md) 实例。

上面的例子将描述符的 [maxVertexAmplificationCount](mtlrenderpipelinedescriptor/maxvertexamplificationcount.md) 属性设置为 `2`。大多数 App 通常将此属性设置为 GPU 支持的最大放大因子。这样，使用该描述符中管线状态的编码器就可以选择使用该 GPU 的任何有效顶点放大因子。

### 为渲染通道启用顶点放大

通过调用其 [`- setVertexAmplificationCount:viewMappings:`](<mtlrendercommandencoder/setvertexamplificationcount(__viewmappings_).md>) 方法，配置 [MTLRenderCommandEncoder](mtlrendercommandencoder.md) 实例以对后续渲染命令应用顶点放大。

**Swift**

```swift
renderEncoder.setVertexAmplificationCount(2, viewMappings: nil)
```

**Objective-C**

```objective-c
[renderEncoder setVertexAmplificationCount:2 viewMappings:nil];
```

将顶点放大计数参数设置为小于或等于配置当前渲染管线的 [maxVertexAmplificationCount](mtlrenderpipelinedescriptor/maxvertexamplificationcount.md) 属性。

你还可以在配置顶点放大时提供一个 [MTLVertexAmplificationViewMapping](mtlvertexamplificationviewmapping.md) 实例数组。App 通常提供视图映射以使用顶点放大渲染到多个纹理或视口。

下面的例子分别为第一个和第二个映射将 [renderTargetArrayIndexOffset](mtlvertexamplificationviewmapping/rendertargetarrayindexoffset.md) 值设置为 `0` 和 `1`。同时，分别为第一个和第二个映射将 [viewportArrayIndexOffset](mtlvertexamplificationviewmapping/viewportarrayindexoffset.md) 值设置为 `1` 和 `2`。

GPU 将这些偏移量加到具有相应特性（attribute）的顶点着色器输出上。在本例中，对于第一次和第二次管线调用，GPU 分别将 `0` 和 `1` 加到带有 `[[render_target_array_index]]` 特性的输出值上；对于第一次和第二次管线调用，GPU 分别将 `1` 和 `2` 加到带有 `[[viewport_array_index]]` 特性的输出值上。

**Swift**

```swift
func configureEncoder(_ renderEncoder: MTLRenderCommandEncoder) {
    // Create two mappings for vertex amplification.
    var mapping0 = MTLVertexAmplificationViewMapping()
    var mapping1 = MTLVertexAmplificationViewMapping()

    // Set each mapping's index offset for a render target array.
    mapping0.renderTargetArrayIndexOffset = 0
    mapping1.renderTargetArrayIndexOffset = 1

    // Set each mapping's index offset for a viewport array.
    mapping0.viewportArrayIndexOffset = 1
    mapping1.viewportArrayIndexOffset = 2

    // Create an array of the two mappings.
    let mappings = [mapping0, mapping1]

    // Set the vertex amplification multiplier with view mappings.
    renderEncoder.setVertexAmplificationCount(2, viewMappings: mappings)
}
```

**Objective-C**

```objective-c
- (void)configureEncoder:(id<MTLRenderCommandEncoder>) renderEncoder {
    // Create two mappings for vertex amplification.
    MTLVertexAmplificationViewMapping mapping0;
    MTLVertexAmplificationViewMapping mapping1;

    // Set each mapping's index offset for a render target array.
    mapping0.renderTargetArrayIndexOffset = 0;
    mapping1.renderTargetArrayIndexOffset = 1;

    // Set each mapping's index offset for a viewport array.
    mapping0.viewportArrayIndexOffset = 1;
    mapping1.viewportArrayIndexOffset = 2;

    // Create an array of the two mappings.
    MTLVertexAmplificationViewMapping mappings[] = { mapping0, mapping1 };

    // Set the vertex amplification multiplier.
    [renderEncoder setVertexAmplificationCount:2 viewMappings:mappings];
}
```

有关如何将特性（attribute）应用于 GPU 函数（着色器和内核）参数的信息，请参见 [Metal Shading Language 规范](https://developer.apple.com/metal/Metal-Shading-Language-Specification.pdf)。

### 将顶点放大添加到顶点着色器

通过添加表示放大 ID 和放大因子的参数，在你的着色器代码中实现顶点放大。通过为每个参数附加一个特性来指定哪个参数是什么。

例如，带有 `[[amplification_id]]` 特性的参数表示顶点数据每个副本的唯一标识符。带有 `[[amplification_count]]` 特性的参数表示唯一标识符的总数。

```metal
vertex VertexOut vs_main(VertexIn in[[stage_in]],
                         ushort amp_id [[amplification_id]],
                         ushort amp_count [[amplification_count]],
                         constant int* buffer)
{
    ...
}
```

GPU 为每个放大 ID 调用着色器一次。对于每次调用，GPU 将带有 `[[amplification_id]]` 的参数设置为 `[0, amplification_count - 1]` 范围内的唯一值。GPU 将带有 `[[amplification_count]]` 特性的参数设置为与配置绘制命令所用相同的放大因子，用于所有调用。

你可以使用这些参数（在本例中为 `amp_id` 和 `amp_count`）为每个渲染管线实例自定义着色器的行为。

```metal
struct VertexOut
{
    int data;
    ...
};

...

vertex VertexOut vs_main(VertexIn in[[stage_in]],
                         ushort amp_id [[amplification_id]],
                         ushort amp_count [[amplification_count]],
                         constant int* buffer)
{
    VertexOut out;
    ...
 
    if (amp_count == 1) {
        // The draw command isn't using vertex amplification.
        ...
    } else {
        out.data = buffer[amp_id];
        ...
    }

    ...
    return out;
}
```

你还可以在未应用顶点放大的绘制调用中调用带有这些参数的着色器。在这些场景中，GPU 为每个顶点调用着色器一次，并将带有 `[[amplification_id]]` 和 `[[amplification_count]]` 的参数分别设置为 `0` 和 `1`。

### 将所有顶点共有的值标记为共享

你可以通过将顶点所有放大 ID 中相同的值标注出来，帮助减少 GPU 的运行时工作量。Metal 编译器将跨所有放大 ID 保持不变的值检测为*共享（shared）*值。你也可以通过添加 `[[shared]]` 特性告诉编译器哪些值被认为是共享的。

默认情况下，Metal 着色器编译器通过检测计算在顶点所有放大 ID 中是否具有相同值来寻找共享值。编译器指示 GPU 为每个顶点计算一次这些值，这样 GPU 就不会为每个放大 ID 计算相同的值。例如，如果着色器直接从输入复制值，编译器会推断这是一个共享值。

```metal
#define PositionAttribute            0
#define TextureCoordinatesAttribute  1
#define NormalAttribute              2

struct VertexIn
{
    float3 position         [[attribute(PositionAttribute)]];
    float2 textureLocation  [[attribute(TextureCoordinatesAttribute)]];
    float3 normal           [[attribute(NormalAttribute)]];
};

struct VertexOut
{
    int data;
    float4 position [[position]];
    float3 normal;
    float2 textureLocation [[shared]];
};

...

vertex VertexOut vs_main(VertexIn in[[stage_in]],
                         ushort amp_id [[amplification_id]],
                         ushort amp_count [[amplification_count]],
                         constant int* buffer)
{
    VertexOut out;
    ...

    // This is a shared value because it's the same for all copies of the vertex.
    out.normal = in.normal;

    ...
    return out;
}
```

如果顶点的计算结果对所有放大 ID 都相同，编译器还可以将其他计算推断为共享值。

相反，编译器将跨放大 ID 变化的计算推断为*非共享（nonshared）*。例如，依赖于 `[[amplification_id]]` 参数的计算是非共享值，因为放大 ID 随每个顶点副本而变化。

```metal
struct VertexOut
{
    int data;
    ...
};

...

vertex VertexOut vs_main(VertexIn in[[stage_in]],
                         ushort amp_id [[amplification_id]],
                         ushort amp_count [[amplification_count]],
                         constant int* buffer)
{
    VertexOut out;
    ...

    // This is a nonshared value because it depends on the [[amplification_id]] parameter.
    out.data = buffer[amp_id];

    ...
    return out;
}
```

编译器还将依赖于 `[[position]]` 参数的任何计算推断为非共享值。

```metal
#define PositionAttribute            0
...

struct VertexIn
{
    float3 position         [[attribute(PositionAttribute)]];
    ...
 };

struct VertexOut
{
    ...
    float4 position [[position]];
    ...
};

constant float4x4 transform = { ... };

vertex VertexOut vs_main(VertexIn in[[stage_in]],
                         ushort amp_id [[amplification_id]],
                         ushort amp_count [[amplification_count]],
                         constant int* buffer)
{
    VertexOut out;
    ...

    // This is a nonshared value because the assignment stores the result to the [[position]] parameter.
    out.position = transform * float4(in.position, 1.0);

    ...
    return out;
}
```

> [!note] 注意
> Metal 编译器将赋值给内置特性参数的所有值推断为*共享*值，但赋值给 `[[position]]` 特性的情况除外。

如果编译器可以证明结果对所有放大 ID 相同，则将其余计算推断为共享值。但是，你可以通过添加 `[[shared]]` 特性作为对着色器编译器的提示，显式地将一个参数指定为共享值。

```metal
struct VertexOut
{
    ...
     float2 textureLocation [[shared]];
};
vertex VertexOut vs_main(VertexIn in[[stage_in]],
                         ushort amp_id [[amplification_id]],
                         ushort amp_count [[amplification_count]],
                         constant int* buffer)
{
    VertexOut out;
    ...

    // This is a shared value the `VertexOut` type declares with the [[shared]] attribute.
    out.textureLocation = in.position.xy;

    ...
    return out;
}
```

### 结合顶点放大与图元实例化

*图元实例化（primitive instancing）*是生成顶点数据副本的另一种方式，它通过为每个实例提供额外数据来修改原始顶点。例如，你可以通过用一系列姿态偏移（每个偏移对应一个动画帧）来改变顶点数据，从而对模型进行动画处理。

图元实例化为每个实例生成一个顶点数据副本。如果你编码一个实例计数为 `10` 的绘制调用，GPU 会调用渲染管线 10 次，每个实例一次。与顶点放大不同，GPU 在每次调用你的顶点着色器时都会重新计算所有顶点输出值。

你可以在同一个渲染通道中将顶点放大和图元实例化应用于场景的不同组件。你可以使用图元实例化来绘制多个角色，然后使用顶点放大来渲染到不同的阴影贴图。

渲染管线实例的总数等于顶点放大因子与图元实例数的乘积。例如，如果你编码一个具有 `10` 个图元实例和顶点放大因子为 `2` 的绘制调用，GPU 会为每个顶点调用你的顶点着色器 20 次。在这种情况下，顶点着色器会为 10 个实例中的每一个各运行两次。但是，GPU 会为所有放大 ID 计算一次顶点放大的共享输出值。

## 另请参阅

### 应用渲染技术

- [使用 Metal 4 绘制三角形](drawing-a-triangle-with-metal-4.md)——通过在 GPU 上使用渲染管线执行绘制命令，渲染一个彩色旋转的 2D 三角形。
- [自定义渲染通道设置](customizing-render-pass-setup.md)——通过创建自定义渲染通道渲染到屏幕外纹理。
- [设置加载和存储操作](setting-load-and-store-actions.md)——设置定义渲染通道如何加载和存储渲染目标的操作。
