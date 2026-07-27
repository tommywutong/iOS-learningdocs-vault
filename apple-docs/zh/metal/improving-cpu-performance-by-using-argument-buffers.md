---
title: 通过使用参数缓冲区提升 CPU 性能
framework: Metal
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/improving-cpu-performance-by-using-argument-buffers
source_url: 'https://developer.apple.com/documentation/metal/improving-cpu-performance-by-using-argument-buffers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/improving-cpu-performance-by-using-argument-buffers.json'
content_hash: 'sha256:dd13c06467135e94'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Metal](../metal.md) · [Buffers](buffers.md)

# 通过使用参数缓冲区提升 CPU 性能

<sub>文章</sub>

通过将资源归入参数缓冲区，优化你 App 的性能。

## 概述

使用参数缓冲区，将多个资源归集到单个着色器参数中。_参数缓冲区_是一种 Metal 缓冲区，包含对其他 Metal 资源的引用，包括 [MTLBuffer](mtlbuffer.md)、[MTLTexture](mtltexture.md)、[MTLSamplerState](mtlsamplerstate.md) 和 [MTLAccelerationStructure](mtlaccelerationstructure.md) 实例。与单独分配每个资源相比，参数缓冲区的开销更小。对于在多帧之间不发生变化的资源来说尤其如此，因为你可以只分配一次参数缓冲区并多次重用它。

> [!note] 注意
> 要将资源绑定到由你用 [Metal shader converter](https://developer.apple.com/metal/shader-converter/) 编译的着色器组成的管线，你需要使用参数缓冲区。

有关参数缓冲区的更多信息，请观看 [Go bindless with Metal 3](https://developer.apple.com/videos/play/wwdc2022/10101/) 和 [Explore bindless rendering in Metal](https://developer.apple.com/wwdc21/10286)。

### 在 Metal 着色语言中定义参数缓冲区格式

在 Metal Shading Language（MSL）源文件中，将你的参数缓冲区声明为结构体。

```metal
struct ArgumentBufferExample{
    texture2d<float, access::write> a;
    depth2d<float> b;
    sampler c;
    texture2d<float> d;
    device float4* e;
    texture2d<float> f;
    int g;
};

kernel void example(constant ArgumentBufferExample & argumentBuffer [[buffer(0)]])
{
    // 
    ...
}
```

将以下类型添加到结构体中：

- 基本标量数据类型，例如 `half` 和 `float`
- 基本向量和矩阵数据类型，例如 `half4` 和 `float4x4`
- 纹理，例如 `texture2d`
- 采样器，例如线性采样器
- 加速结构
- 间接命令缓冲区
- 存储上述类型的数组和结构体
- 其他数组和结构体

> [!note] 注意
> 参数缓冲区不能包含联合类型，尽管遵循 [MTLBuffer](mtlbuffer.md) 协议的实例支持联合类型。

### 将资源编码到参数缓冲区中

常规 Metal 缓冲区中的结构体定义了数据在内存中的确切布局。参数缓冲区的内存布局取决于 GPU 对参数缓冲区的支持情况以及设备的操作系统版本。Metal 将参数缓冲区的支持划分为两个层级：Tier 1 和 Tier 2。对于 Tier 2，在以下操作系统发行版本上，参数缓冲区的内存布局与等效 C 结构体的内存布局相匹配：

- iOS 16.0 及更高版本
- tvOS 16.0 及更高版本
- macOS 13.0 及更高版本

要在这些 Tier 2 设备上直接编码参数缓冲区资源，请将 [MTLBuffer](mtlbuffer.md)`.`[gpuAddress](mtlbuffer/gpuaddress.md) 属性——对于其他资源类型（采样器、纹理和加速结构），则是 [gpuResourceID](mtlcomputepipelinestate/gpuresourceid.md) 属性——写入相应的结构体成员中。要编码偏移量，请将这些属性值当作 `uint64` 类型处理，并将偏移量加到它们上面。

对于 Tier 1 设备以及 Tier 2 设备上较旧的操作系统版本，缓冲区具有一种可能因 GPU 而异的私有内存布局。对于这些设备，请使用一个 [MTLArgumentEncoder](mtlargumentencoder.md) 实例，将参数缓冲区的数据编码到目标 [MTLBuffer](mtlbuffer.md) 实例中。然后将该参数缓冲区作为参数传递给 [MTLRenderCommandEncoder](mtlrendercommandencoder.md) 或 [MTLComputeCommandEncoder](mtlcomputecommandencoder.md) 的图形或计算函数，例如以下这些：

- [- setVertexBuffer:offset:atIndex:](<mtlrendercommandencoder/setvertexbuffer(__offset_index_).md>)
- [- setFragmentBuffer:offset:atIndex:](<mtlrendercommandencoder/setfragmentbuffer(__offset_index_).md>)
- [- setMeshBuffer:offset:atIndex:](<mtlrendercommandencoder/setmeshbuffer(__offset_index_).md>)
- [- setObjectBuffer:offset:atIndex:](<mtlrendercommandencoder/setobjectbuffer(__offset_index_).md>)
- [- setTileBuffer:offset:atIndex:](<mtlrendercommandencoder/settilebuffer(__offset_index_).md>)
- [- setBuffer:offset:atIndex:](<mtlcomputecommandencoder/setbuffer(__offset_index_).md>)

你可以使用以下类型将资源编码到参数缓冲区中：

- [MTLBuffer](mtlbuffer.md)
- [MTLTexture](mtltexture.md)
- [MTLSamplerState](mtlsamplerstate.md)
- [simd_float1](../simd/simd_float1.md)、[simd_float4](../simd/simd_float4.md) 以及其他内联常量数据
- [MTLAccelerationStructure](mtlaccelerationstructure.md)
- [MTLIndirectCommandBuffer](mtlindirectcommandbuffer.md)
- [MTLComputePipelineState](mtlcomputepipelinestate.md)
- [MTLRenderPipelineState](mtlrenderpipelinestate.md)

### 使用堆来提升效率

将资源编码到参数缓冲区中，省去了 Metal 驱动程序在将单个资源分配给函数参数表索引时捕获状态和跟踪驻留情况的需要。参数缓冲区提供了对资源驻留更强的控制能力，你需要在发出绘制或分派调用之前显式声明它。

当你将资源堆与参数缓冲区结合使用时，只需一次对 `useHeap` 方法的调用，就可以让所有只读资源都由一个 [MTLHeap](mtlheap.md) 支持，从而进一步降低开销。不过，对于每个可写资源，即使你的渲染流程只打算从中读取，你仍需要调用 `useResource` 方法。

最后，参数缓冲区允许 Metal 在函数执行时动态地为资源编制索引，这提高了它能够放入缓冲区内的资源数量上限。

### 理解参数缓冲区层级的限制与能力

使用 [MTLDevice](mtldevice.md) 实例的 [argumentBuffersSupport](mtldevice/argumentbufferssupport.md) 属性来获取其层级。

**Tier 1 和 Tier 2 的共同限制**

在 iOS 和 tvOS 上，每个 App 唯一采样器的最大数量为 `96`；在 macOS 上，则为 `1024` 或更多，具体取决于设备和操作系统版本。这些限制仅适用于 [supportArgumentBuffers](mtlsamplerdescriptor/supportargumentbuffers.md) 属性设置为 [true](../swift/true.md) 的采样器。使用 [MTLDevice](mtldevice.md)`.`[maxArgumentBufferSamplerCount](mtldevice/maxargumentbuffersamplercount.md) 属性，获取某设备上每个 App 唯一采样器数量的确切上限。

如果两个 [MTLSamplerState](mtlsamplerstate.md) 实例其来源 [MTLSamplerDescriptor](mtlsamplerdescriptor.md) 属性的配置是唯一的，Metal 就会认为该实例是唯一的。例如，如果两个采样器的 [minFilter](mtlsamplerdescriptor/minfilter.md) 值相同，但 [magFilter](mtlsamplerdescriptor/magfilter.md) 值不同，Metal 会认为它们是不同的实例。

有关每个函数参数表中最大条目数，请参阅 [Metal 特性集表格](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf)。

**Tier 1 的限制**

对于 Tier 1，Metal 会对每个图形或计算函数中、在参数缓冲区内设置的资源与单独设置的资源二者组合的最大数量施加资源限制。Metal 会将参数缓冲区中的条目计入每个函数参数表的最大缓冲区条目数中。例如，如果某个内核函数使用了四个单独的纹理和一个包含八个纹理的参数缓冲区，那么该内核函数的纹理总数为 12 个。Tier 1 的参数缓冲区不能包含可写纹理。

Tier 1 参数缓冲区的其他限制包括：

- 必须是不可变的，因为 GPU 无法修改参数缓冲区的内容
- 必须可被 CPU 访问，因此需要将缓冲区的存储模式设置为 [MTLStorageModeShared](mtlstoragemode/shared.md) 或 [MTLStorageModeManaged](mtlstoragemode/managed.md)
- 在 MSL 中，不能通过指针索引访问，也不能包含指向其他参数缓冲区的指针

**Tier 2 的限制**

支持 Tier 2 参数缓冲区的 GPU 有着显著更高的限制，这为你的 App 带来了更多能力。

对于 Tier 2，参数缓冲区可以是可变的，这样 GPU 和 CPU 就都能在任意时刻修改其内容。不过，如果你指定从 Metal 将该缓冲区设置到某个函数的参数表中，到 Metal 完成相关命令缓冲区执行期间，CPU 和 GPU 都不会修改该缓冲区的内容，Metal 可能会执行某些优化。Metal 会将这类参数缓冲区视为不可变的。要表明某个参数缓冲区是不可变的、并让 Metal 执行优化，请将其关联的 [MTLPipelineBufferDescriptor](mtlpipelinebufferdescriptor.md)`.`[mutability](mtlpipelinebufferdescriptor/mutability.md) 属性设置为 [MTLMutabilityImmutable](mtlmutability/immutable.md)。

在 MSL 中，你通过对指针编制索引来访问 Tier 2 参数缓冲区。

```metal
struct ArgumentBufferTextures {
    texture2d<float> diffuse;
    texture2d<float> specular;
};

struct ArgumentBufferMaterial {
    device ArgumentBufferTextures *textures;
};

fragment float4 exampleFragment(device ArgumentBufferMaterial & material)
{
    return material.textures[4]->diffuse.read(uint2(0));
}
```

由于你无法将采样器从线程地址空间复制到设备地址空间，你只能在参数缓冲区之间复制参数缓冲区采样器。例如，如果你在着色器中默认在线程地址空间里创建 `constexpr` 采样器，你就无法将它们赋值给设备地址空间中的缓冲区。

```metal
struct ArgumentBufferSampler {
    sampler sampler0;
};

kernel void exampleKernel(device ArgumentBufferSampler *source,
                          device ArgumentBufferSampler *destination,
                          sampler sampler1) {
    constexpr sampler sampler2;

    // Metal 允许设备到设备的复制。
    destination->sampler0 = source->sampler0;

    // Metal 不允许线程到设备的复制。
    destination->sampler0 = sampler1;
    destination->sampler0 = sampler2;
}
```

## 另请参阅

### 参数缓冲区

- [使用参数缓冲区管理资源组](managing-groups-of-resources-with-argument-buffers.md) — 创建参数缓冲区来组织相关的资源。
- [跟踪参数缓冲区的资源驻留情况](tracking-the-resource-residency-of-argument-buffers.md) — 优化参数缓冲区内的资源性能。
- [为参数缓冲区编制索引](indexing-argument-buffers.md) — 在参数缓冲区内分配资源索引。
- [使用参数缓冲区动态渲染地形](rendering-terrain-dynamically-with-argument-buffers.md) — 使用参数缓冲区，通过 GPU 驱动的管线实时渲染地形。
- [在 GPU 上编码参数缓冲区](encoding-argument-buffers-on-the-gpu.md) — 使用一个计算流程来编码参数缓冲区，并在后续的渲染流程中访问其参数。
- [将参数缓冲区与资源堆搭配使用](using-argument-buffers-with-resource-heaps.md) — 通过在参数缓冲区内使用数组并将其与资源堆结合，降低 CPU 开销。
- [MTLArgumentDescriptor](mtlargumentdescriptor.md) — 参数缓冲区内某个参数的表示形式。
- [MTLArgumentEncoder](mtlargumentencoder.md) — 一个可用于将参数数据编码到参数缓冲区中的接口。
- [MTLAttributeStrideStatic](mtlattributestridestatic.md)
