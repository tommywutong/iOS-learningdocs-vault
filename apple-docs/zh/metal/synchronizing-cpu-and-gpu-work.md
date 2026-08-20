---
title: 同步 CPU 与 GPU 工作
framework: Metal
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, Xcode 26.3+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/synchronizing-cpu-and-gpu-work
source_url: 'https://developer.apple.com/documentation/metal/synchronizing-cpu-and-gpu-work'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/synchronizing-cpu-and-gpu-work.json'
content_hash: 'sha256:778e52a1ead5a2a8'
translated: true
---

> 导航：[技术](../technologies.md) · [Metal](../metal.md) · [Metal 示例代码库](metal-sample-code-library.md)

# 同步 CPU 与 GPU 工作

<sub>示例代码</sub>

通过使用资源的多个实例来避免 CPU 与 GPU 工作之间的停滞。

## 概述

在此示例代码项目中，你将学习如何在 CPU 和 GPU 之间管理数据依赖并避免处理器停滞。

项目持续沿正弦波渲染三角形。在每一帧中，示例会更新每个三角形顶点的位置，然后渲染新图像。这些动态数据更新创造了运动错觉，使三角形看起来沿着正弦波移动。

![示例代码项目的截图，显示沿正弦波渲染的彩色三角形。](../../../attachments/5e6872f93f029b321bb48ae20cc72ff5/cpu-gpu-synchronization-1-SampleScreenshot.png)

示例将三角形顶点存储在 CPU 和 GPU 之间共享的缓冲区中。CPU 将数据写入缓冲区，GPU 从中读取。

> [!note] 注意
> Xcode 项目包含用于在 macOS、iOS 和 tvOS 上运行示例的 scheme。默认 scheme 是 macOS，会在你的 Mac 上运行示例。

### 了解数据依赖与处理器停滞的解决方案

资源共享会在处理器之间产生数据依赖（data dependency）；CPU 需要在 GPU 读取资源之前完成写入。如果 GPU 在 CPU 写入之前读取资源，则会读取未定义的资源数据。如果 GPU 在 CPU 写入期间读取资源，则会读取错误的资源数据。

![示意图显示 CPU 和 GPU 在每一帧中依次访问一个缓冲区。](../../../attachments/5f15ee47f49c23cf653705709dac8e42/cpu-gpu-synchronization-2-AccessOrder.png)

这些数据依赖会在 CPU 和 GPU 之间造成处理器停滞（processor stall）；每个处理器都需要等待另一个处理器完成其工作后才能开始自己的工作。

然而，由于 CPU 和 GPU 是独立的处理器，你可以通过使用资源的多个实例让它们同时工作。每帧需要向着色器提供相同的参数，但这并不意味着必须引用同一个资源对象。相反，你可以创建包含多个资源实例的池，每次渲染帧时使用不同的实例。例如，如下所示，CPU 可以将位置数据写入用于帧 `n+1` 的缓冲区，同时 GPU 从用于帧 `n` 的缓冲区读取位置数据。通过使用多个缓冲区实例，只要你持续渲染帧，CPU 和 GPU 就能连续工作并避免停滞。

![示意图显示 CPU 和 GPU 在每一帧中同时访问多个缓冲区副本。](../../../attachments/32b0e436b2811d2b0fe5d32545888bd9/cpu-gpu-synchronization-3-ContinuousWork.png)

### 使用 CPU 初始化数据

定义一个表示顶点的自定义 `AAPLVertex` 结构体。每个顶点都有一个位置和一个颜色：

**AAPLShaderTypes.h**

```objective-c
typedef struct
{
    vector_float2 position;
    vector_float4 color;
} AAPLVertex;
```

定义一个自定义 `AAPLTriangle` 类，提供默认三角形（由 3 个顶点组成）的接口：

**AAPLTriangle.m**

```objective-c
+(const AAPLVertex *)vertices
{
    const float TriangleSize = 64;
    static const AAPLVertex triangleVertices[] =
    {
        // 像素位置，                           RGBA 颜色。
        { { -0.5*TriangleSize, -0.5*TriangleSize },  { 1, 1, 1, 1 } },
        { {  0.0*TriangleSize, +0.5*TriangleSize },  { 1, 1, 1, 1 } },
        { { +0.5*TriangleSize, -0.5*TriangleSize },  { 1, 1, 1, 1 } }
    };
    return triangleVertices;
}
```

用位置和颜色初始化多个三角形顶点，并将它们存储在三角形数组 `_triangles` 中：

**AAPLRenderer.m**

```objective-c
NSMutableArray *triangles = [[NSMutableArray alloc] initWithCapacity:NumTriangles];

// 初始化每个三角形。
for(NSUInteger t = 0; t < NumTriangles; t++)
{
    vector_float2 trianglePosition;

    // 确定三角形在水平线上的起始位置。
    trianglePosition.x = ((-((float)NumTriangles) / 2.0) + t) * horizontalSpacing;
    trianglePosition.y = 0.0;

    // 创建三角形，设置其属性，并将其添加到数组中。
    AAPLTriangle * triangle = [AAPLTriangle new];
    triangle.position = trianglePosition;
    triangle.color = Colors[t % NumColors];
    [triangles addObject:triangle];
}
_triangles = triangles;
```

### 分配数据存储

计算三角形顶点的总存储大小。你的 App 渲染 50 个三角形；每个三角形有 3 个顶点，共 150 个顶点，每个顶点的大小为 `AAPLVertex`：

**AAPLRenderer.m**

```objective-c
const NSUInteger triangleVertexCount = [AAPLTriangle vertexCount];
_totalVertexCount = triangleVertexCount * _triangles.count;
const NSUInteger triangleVertexBufferSize = _totalVertexCount * sizeof(AAPLVertex);
```

初始化多个缓冲区，以存储顶点数据的多个副本。为每个缓冲区分配恰好足以存储 150 个顶点的内存：

**AAPLRenderer.m**

```objective-c
for(NSUInteger bufferIndex = 0; bufferIndex < MaxFramesInFlight; bufferIndex++)
{
    _vertexBuffers[bufferIndex] = [_device newBufferWithLength:triangleVertexBufferSize
                                                       options:MTLResourceStorageModeShared];
    _vertexBuffers[bufferIndex].label = [NSString stringWithFormat:@"Vertex Buffer #%lu", (unsigned long)bufferIndex];
}
```

初始化时，`_vertexBuffers` 数组中缓冲区实例的内容为空。

### 使用 CPU 更新数据

在每一帧的 [`drawInMTKView:`](<../metalkit/mtkviewdelegate/draw(in_).md>) 渲染循环开始时，在 `updateState` 方法中使用 CPU 更新一个缓冲区实例的内容：

**AAPLRenderer.m**

```objective-c
// 当前三角形的顶点数据。
AAPLVertex *currentTriangleVertices = _vertexBuffers[_currentBuffer].contents;

// 更新每个三角形。
for(NSUInteger triangle = 0; triangle < NumTriangles; triangle++)
{
    vector_float2 trianglePosition = _triangles[triangle].position;

    // 使用正弦波移动三角形的 y 位置。
    trianglePosition.y = (sin(trianglePosition.x/waveMagnitude + _wavePosition) * waveMagnitude);

    // 更新三角形的位置。
    _triangles[triangle].position = trianglePosition;

    // 用三角形的新位置更新当前顶点缓冲区的顶点。
    for(NSUInteger vertex = 0; vertex < triangleVertexCount; vertex++)
    {
        NSUInteger currentVertex = vertex + (triangle * triangleVertexCount);
        currentTriangleVertices[currentVertex].position = triangleVertices[vertex].position + _triangles[triangle].position;
        currentTriangleVertices[currentVertex].color = _triangles[triangle].color;
    }
}
```

更新完一个缓冲区实例后，在该帧的剩余时间内不再使用 CPU 访问其数据。

> [!note] 注意
> 你需要在提交引用某个缓冲区实例的命令缓冲区之前，完成 CPU 对其的所有写入。否则，GPU 可能在 CPU 仍在写入时就开始读取该缓冲区实例。

### 编码 GPU 命令

接下来，在渲染 pass 中编码引用该缓冲区实例的命令：

**AAPLRenderer.m**

```objective-c
[renderEncoder setVertexBuffer:_vertexBuffers[_currentBuffer]
                        offset:0
                       atIndex:AAPLVertexInputIndexVertices];

// 设置视口（viewport）大小。
[renderEncoder setVertexBytes:&_viewportSize
                       length:sizeof(_viewportSize)
                      atIndex:AAPLVertexInputIndexViewportSize];

// 绘制三角形顶点。
[renderEncoder drawPrimitives:MTLPrimitiveTypeTriangle
                  vertexStart:0
                  vertexCount:_totalVertexCount];
```

### 提交并执行 GPU 命令

在渲染循环结束时，调用命令缓冲区的 [- commit](<mtlcommandbuffer/commit().md>) 方法将工作提交给 GPU：

**AAPLRenderer.m**

```objective-c
[commandBuffer commit];
```

GPU 开始工作，并从 `RasterizerData` 顶点着色器中的 `vertices` 缓冲区读取数据，该着色器将缓冲区实例作为输入参数接收：

**AAPLShaders.metal**

```metal
vertex RasterizerData
vertexShader(const uint vertexID [[ vertex_id ]],
             const device AAPLVertex *vertices [[ buffer(AAPLVertexInputIndexVertices) ]],
             constant vector_uint2 *viewportSizePointer  [[ buffer(AAPLVertexInputIndexViewportSize) ]])
```

### 在 App 中重复使用多个缓冲区实例

对于每一帧，按上述描述执行以下步骤。当两个处理器都完成其工作时，一帧的全部工作才算完成。

1. 将数据写入到一个缓冲区实例。
2. 编码引用该缓冲区实例的命令。
3. 提交包含所编码命令的命令缓冲区。
4. 从该缓冲区实例读取数据。

当一帧的工作完成时，CPU 和 GPU 不再需要该帧使用的缓冲区实例。然而，丢弃已使用的缓冲区实例并在每帧创建一个新实例既昂贵又浪费。相反，如下所示，将你的 App 设置为循环使用一个先进先出（FIFO）的缓冲区实例队列 `_vertexBuffers`，以便重复使用。队列中缓冲区实例的最大数量由 `MaxFramesInFlight` 的值定义，设置为 3：

**AAPLRenderer.m**

```objective-c
static const NSUInteger MaxFramesInFlight = 3;
```

在每一帧的渲染循环开始时，更新 `_vertexBuffer` 队列中的下一个缓冲区实例。你按顺序循环遍历队列，每帧只更新一个缓冲区实例；在每第三帧结束时，返回到队列开头：

**AAPLRenderer.m**

```objective-c
// 遍历 Metal 缓冲区，当写入到最后一个后循环回到第一个。
_currentBuffer = (_currentBuffer + 1) % MaxFramesInFlight;

// 更新缓冲区数据。
[self updateState];
```

> [!note] 注意
> Core Animation 提供了经过优化的可显示资源，通常称为可绘制对象（drawable），用于渲染内容并将其显示在屏幕上。可绘制对象是高效但昂贵的系统资源，因此 Core Animation 限制了你在 App 中同时使用的可绘制对象数量。默认限制是 3，但你可以通过 [`maximumDrawableCount`](../quartzcore/cametallayer/maximumdrawablecount.md) 属性将其设置为 2（仅支持 2 和 3）。由于最大可绘制对象数为 3，此示例创建了 3 个缓冲区实例。你不需要创建超过可用最大可绘制对象数的缓冲区实例。

### 管理 CPU 和 GPU 的工作速率

当有多个缓冲区实例时，可以让 CPU 对帧 `n+1` 使用一个实例开始工作，同时 GPU 使用另一个实例完成帧 `n` 的工作。这种实现通过让 CPU 和 GPU 同时工作来提高 App 的效率。然而，你需要管理 App 的工作速率，以免超出可用的缓冲区实例数量。

为了管理 App 的工作速率，请使用信号量（semaphore）等待帧的完全完成，以防 CPU 工作速度远快于 GPU。信号量是一个非 Metal 对象，用于控制对跨多个处理器（或线程）共享资源的访问。信号量有一个关联的计数值，你可以递减或递增，以指示某个处理器是否已开始或完成访问某个资源。在你的 App 中，信号量控制 CPU 和 GPU 对缓冲区实例的访问。

使用计数值 `MaxFramesInFlight` 初始化信号量，以匹配缓冲区实例的数量。此值表示你的 App 在任何给定时间最多可以同时处理 3 帧：

**AAPLRenderer.m**

```objective-c
_inFlightSemaphore = dispatch_semaphore_create(MaxFramesInFlight);
```

在渲染循环开始时，将信号量的计数值减 1。这表明你已准备好处理新的一帧。但是，如果计数值降至 0 以下，信号量将使 CPU 等待，直到你递增值为止：

**AAPLRenderer.m**

```objective-c
dispatch_semaphore_wait(_inFlightSemaphore, DISPATCH_TIME_FOREVER);
```

在渲染循环结束时，注册一个命令缓冲区完成处理程序。当 GPU 完成命令缓冲区的执行时，会调用此完成处理程序，并将信号量的计数值加 1。这表明你已完成给定帧的所有工作，并且可以重复使用该帧中使用的缓冲区实例：

**AAPLRenderer.m**

```objective-c
__block dispatch_semaphore_t block_semaphore = _inFlightSemaphore;
[commandBuffer addCompletedHandler:^(id<MTLCommandBuffer> buffer)
 {
     dispatch_semaphore_signal(block_semaphore);
 }];
```

[- addCompletedHandler:](<mtlcommandbuffer/addcompletedhandler(__).md>) 方法注册一段代码块（block），该块在 GPU 完成执行关联的命令缓冲区后立即被调用。由于每帧只使用一个命令缓冲区，因此收到完成回调表示 GPU 已完成该帧。

### 设置缓冲区的可变性

你的 App 在单个线程上执行所有每帧渲染设置。首先，使用 CPU 将数据写入一个缓冲区实例。然后，编码引用该缓冲区实例的渲染命令。最后，提交一个命令缓冲区以供 GPU 执行。由于这些任务总是在一个线程上按此顺序发生，因此 App 能保证在编码引用缓冲区实例的命令之前完成对该实例的数据写入。

这种顺序允许你将缓冲区实例标记为不可变。配置渲染管线描述符时，将缓冲区实例索引处的顶点缓冲区的 [mutability](mtlpipelinebufferdescriptor/mutability.md) 属性设置为 [MTLMutabilityImmutable](mtlmutability/immutable.md)：

**AAPLRenderer.m**

```objective-c
pipelineStateDescriptor.vertexBuffers[AAPLVertexInputIndexVertices].mutability = MTLMutabilityImmutable;
```

Metal 可以优化不可变缓冲区的性能，但不能优化可变缓冲区。为获得最佳结果，请尽可能使用不可变缓冲区。

## 另请参阅

### 同步

- [使用堆和事件实现多阶段图像滤镜](implementing-a-multistage-image-filter-using-heaps-and-events.md) — 使用事件同步对堆上分配的资源的访问。
- [使用堆和围栏实现多阶段图像滤镜](implementing-a-multistage-image-filter-using-heaps-and-fences.md) — 使用围栏同步对堆上分配的资源的访问。

## 下载

- [SynchronizingCPUAndGPUWork.zip](https://docs-assets.developer.apple.com/published/a2ec04f3244c/SynchronizingCPUAndGPUWork.zip)
