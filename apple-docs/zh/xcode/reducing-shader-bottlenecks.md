---
title: 减少 shader 瓶颈
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/reducing-shader-bottlenecks
source_url: 'https://developer.apple.com/documentation/xcode/reducing-shader-bottlenecks'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/reducing-shader-bottlenecks.json'
content_hash: 'sha256:c4ef1469a94aa913'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Debugging](debugging.md) · [Metal developer workflows](metal-developer-workflows.md)

# 减少 shader 瓶颈

<sub>文章</sub>

通过检查 GPU 的限制器（limiter）和利用率（utilization）计数器，找出并减少其各子系统中的拥塞点。

## 概述

GPU 通常可以将子任务分派给专门处理不同操作（例如内存访问、数学与逻辑运算、像素光栅化）的各个子系统，从而同时运行这些子任务。然而，App 的 GPU 函数（shader 函数和计算内核）中的代码可能会迫使其中一些子系统停顿（stall），也就是等待自身完成某项操作，或等待另一个子系统就绪。

GPU 驱动程序会通过计数器公布其各子系统的工作时间和停顿时间，你可以通过监控这些计数器来了解这些子系统花在工作上与花在停顿上的时间各是多少：

- _利用率（utilization）_ 计数器显示 GPU 子系统处于工作状态的时间，不包括停顿时间。
- _限制器（limiter）_ 计数器显示 GPU 花在工作上的时间，包括停顿时间。

将以下计数器用作线索，帮助你识别在运行时哪些 GPU 子系统可能是瓶颈：

| 计数器 | 限制器计数器 | 利用率计数器 | 说明 |
|---|---|---|---|
| GPU memory read | 是 | 否 | 衡量 GPU 峰值内存读取性能的百分比。参阅[衡量 GPU 的内存带宽使用情况](measuring-the-gpus-use-of-memory-bandwidth.md)。 |
| GPU memory write | 是 | 否 | 衡量 GPU 峰值内存写入性能的百分比。参阅[衡量 GPU 的内存带宽使用情况](measuring-the-gpus-use-of-memory-bandwidth.md)。 |
| Memory managament unit (MMU) | 是 | 是 | 衡量 GPU 在内存管理单元上花费的时间。 |
| Last level cache | 是 | 是 | 衡量 GPU 处理最高级别 GPU 缓存请求所花费的时间。 |
| Tile memory read | 是 | 是 | Tile 内存是 GPU 本地的内存，与线程组内存和 imageblock 内存同义。 |
| Tile memory write | 是 | 是 | Tile 内存是 GPU 本地的内存，与线程组内存和 imageblock 内存同义。 |
| Arithmetic logic unit (ALU) | 是 | 是 | 衡量 GPU 花在算术、逻辑和按位运算上的时间。 |
| F16 | 否 | 是 | 衡量 GPU 花在 16 位浮点运算上的时间。 |
| F32 | 否 | 是 | 衡量 GPU 花在 32 位浮点运算上的时间。 |
| Texture sampling | 是 | 是 | 衡量 GPU 花在纹理采样上的时间。 |
| Texture filtering | 是 | 否 | 衡量 GPU 花在执行纹理过滤操作上的时间。 |
| Texture read cache | 是 | 否 | 衡量 GPU 花在纹理读取缓存上的时间。 |
| Texture write | 是 | 是 | 衡量 GPU 花在写入纹理上的时间。 |
| Buffer read | 是 | 是 | 衡量 GPU 从缓冲区读取数据所花费的时间。 |
| Buffer write | 是 | 是 | 衡量 GPU 向缓冲区写入数据所花费的时间，包括 GPU 函数写入设备地址空间内存的任何时间。 |
| Fragment shader input interpolation | 是 | 是 | 衡量 GPU 花在对片元 shader 的输入进行插值上的时间。 |

你可以在 Instruments 的 Metal system trace 以及 Metal 调试器的 Performance 时间线中监控利用率和限制器计数器。更多信息参阅[分析 Metal App 的性能](analyzing-the-performance-of-your-metal-app.md)和[使用可视化时间线分析 Apple GPU 性能](analyzing-apple-gpu-performance-using-a-visual-timeline.md)。

为了减轻特定 GPU 子系统的压力并帮助 GPU 更快地运行命令，你可以调整 GPU 函数的运行方式和资源使用方式。大多数代码调整通常属于以下几种策略：

- 减少操作数量
- 将工作转移到负载较轻的另一个子系统
- 降低工作的图像质量或数学精度
- 以能提高 GPU 内存缓存命中率的方式访问内存

有些调整存在权衡取舍，例如降低图像质量或数学精度，具体哪些调整值得为你的 App 采用，由你自行决定。

> [!tip] 提示
> 通过在你的 App 上进行实验，找出能带来更好性能的调整方式。

### 减少算术逻辑单元的工作负载

算术逻辑单元（ALU）负责处理代码中的算术、逻辑和按位运算。如果计数器显示 ALU 可能是瓶颈，你可以尝试以下每种调整并评估其效果：

- 用近似值替代精确公式。
- 如果精度和范围足够满足计算需求，用半浮点数（half-float）替代浮点数。
- 使用 Metal 编译器的 `-ffast-math` 标志编译你的 GPU 函数，该标志会启用运行更快、但可能引入精度误差的优化（参阅 [Metal Shading Language Specification](https://developer.apple.com/metal/Metal-Shading-Language-Specification.pdf) 中的 1.5 节）。
- 用查找表或纹理替代复杂计算。

这些调整通过让工作变得更简单，或将工作转移给另一个子系统（例如纹理采样器），来减少 ALU 的工作负载。例如，你可以创建一张噪声纹理，每次代码需要一个值时从中采样，从而省去噪声计算函数。

### 减少纹理操作的工作负载

当你将渲染流程（render pass）某个颜色附件的 [loadAction](../metal/mtlrenderpassattachmentdescriptor/loadaction.md) 属性设置为 [MTLLoadAction.load](../metal/mtlloadaction/load.md)，以及每次 GPU 函数读取、聚集（gather）或采样一张纹理时，GPU 都会为该颜色附件读取纹理数据。尺寸更大或使用更大像素格式的纹理会占用更多内存，通常也会增加 GPU 为采样该纹理而读取的数据量。

如果计数器显示纹理 _采样（sample）_ 操作可能是瓶颈，你可以尝试以下调整并评估其对 App 性能的影响：

- 对使用缩小过滤器（minification filter）的纹理，从 mipmap 采样。
- 选择双线性过滤而非三线性过滤。
- 在 GPU 函数内计算成本比读取纹理更低的数值。
- 使用尺寸更小或像素格式更小的纹理。
- 用聚集操作替代对单通道纹理的读取或采样，聚集操作能更高效地使用 GPU。

同样地，当你将渲染流程某个颜色附件的 [storeAction](../metal/mtlrenderpassattachmentdescriptor/storeaction.md) 属性设置为 [MTLStoreAction.store](../metal/mtlstoreaction/store.md)，以及每次 GPU 函数显式写入一张纹理时，GPU 都会为该颜色附件保存纹理数据。

如果计数器显示纹理 _写入（write）_ 操作可能是瓶颈，你可以尝试以下调整并评估其对 App 性能的影响：

- 使用尺寸更小或像素格式更小的纹理。
- 减少多重采样抗锯齿（MSAA）的采样数。
- 减少非常小的三角形的渲染数量，尤其是在同时使用 MSAA 时。
- 修改在空间或时间上聚集写入操作（更高的空间或时间局部性）的纹理，这样 GPU 就能将它们合并为更少的内存写入事务。

### 减少缓冲区操作的工作负载

写入操作计数器衡量 GPU 函数将数据存储到 GPU 设备地址空间内存所花费的时间。读取操作计数器衡量 GPU 函数从设备地址空间和常量地址空间中获取数据所花费的时间。

当 GPU 函数使用大量线程内存或以 _动态索引（dynamic indexing）_ 方式访问线程内存时，会增加读写活动。当某个函数需要存储的数据量超出 GPU 寄存器容量时就会发生这种情况，这会迫使 GPU 将数据存储到设备内存中，之后再读取。

如果计数器显示缓冲区的 _读取（read）_ 或 _写入（write）_ 操作可能是瓶颈，你可以尝试以下调整并评估其对 App 性能的影响：

- 将数据更紧凑地打包进缓冲区。
- 使用 SIMD 类型打包标量值，例如用 `float4` 这个 SIMD 类型替代四个独立的 `float` 值。
- 使用更小的数据类型，例如用 `packed_half3` 类型存储位置数据而不是 `float4`。
- 避免随机索引线程作用域数组的实现方式，这样可以给编译器更多灵活性，以便更好地优化 GPU 函数。

对于缓冲区 _读取_ 操作，你也可以尝试改为从纹理而非缓冲区读取数据，将部分工作负载分摊给另一个子系统。对于缓冲区 _写入_ 操作，尝试减少 GPU 函数对设备内存进行原子写入的次数。

### 减少线程组和 imageblock 操作的工作负载

Apple 芯片 GPU 使用线程组内存和 imageblock 内存（统称为 _tile 内存_），它们由 GPU 内部一组本地、统一的高性能存储组成。

当你在计算 shader 中写入线程组内存、写入 imageblock 中的某个像素、在渲染流程中使用混合（blending），或从片元 shader 向颜色附件写入数据时，就会访问这种高速内存。

在应用混合的渲染流程期间，以及出现以下情况时，你的 App 会访问这种高速内存：

- GPU 函数读取或写入 imageblock 数据
- 片元 shader 从颜色附件读取或向其写入
- 计算内核从线程组内存读取或向其写入

如果计数器显示线程组和 imageblock 的 _读取_ 或 _写入_ 操作可能是瓶颈，你可以在计算内核中尝试以下调整，并评估其对 App 性能的影响：

- 将线程组内存分配对齐到 16 字节边界。
- 减少内核对线程组内存的原子读取或写入。
- 重新排列内存访问模式，使一个四元组（quad group）中相邻的线程写入（或读取）线程组内存中相邻的元素。

对于线程组和 imageblock 的 _读取_ 操作，你也可以尝试移除同一线程组内多个线程对同一内存位置的访问。

### 减少片元输入插值的工作负载

在渲染流程期间，GPU 会在将顶点阶段的输出数据发送到片元阶段之前对其进行插值。如果计数器显示片元输入插值可能是瓶颈，你可以尝试减少片元 shader 所使用的顶点属性数量。

### 减少最高级别缓存的工作负载

最高级别缓存计数器衡量 GPU 处理最高级别 GPU 缓存请求所花费的时间。这里的数值较高，可能表明你的 shader 正在请求大量不在缓存中的数据。

> [!tip] 提示
> 在尝试下面的调整之前，先检查并改善纹理和缓冲区操作中的任何瓶颈。

如果计数器显示最高级别缓存可能是瓶颈，你可以尝试以下调整并评估其对 App 性能的影响：

- 减小 GPU 函数所处理数据集的大小。
- 对 GPU 函数只读取或采样的纹理使用压缩像素格式。
- 通过将中间结果存储在线程组内存中并改用该处的原子操作，减少对设备内存的原子读取和写入次数。
- 访问在空间或时间上聚集读取操作（更高的空间或时间局部性）的内存，这可以减少缓存未命中并降低该子系统的工作负载。

## 另请参阅

### 计数器

- [了解 Metal App 的 GPU 占用率](finding-your-metal-apps-gpu-occupancy.md) — 通过占用率了解执行 shader 时的 GPU 使用情况。
- [衡量 GPU 的内存带宽使用情况](measuring-the-gpus-use-of-memory-bandwidth.md) — 通过衡量 GPU 的内存带宽，检查你的 Metal App 是否正确地读写内存。
