---
title: 在 GPU 上执行计算
framework: Metal
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [macOS 10.14+, Xcode 11.3+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/performing-calculations-on-a-gpu
source_url: 'https://developer.apple.com/documentation/metal/performing-calculations-on-a-gpu'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/performing-calculations-on-a-gpu.json'
content_hash: 'sha256:ced11999ae4b755d'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Metal](../metal.md)

# 在 GPU 上执行计算

<sub>示例代码</sub>

使用 Metal 查找 GPU 并在其上执行计算。

## 概述

本示例演示了所有 Metal App 都会用到的基本任务。你将看到如何把一个用 C 语言编写的简单函数转换为 Metal 着色语言（Metal Shading Language，MSL），使其能够在 GPU 上运行。你会查找一个 GPU，通过创建管线让该 MSL 函数在其上运行做好准备，并创建 GPU 可以访问的数据对象。要针对你的数据执行该管线，需要创建一个_命令缓冲区_，向其中写入命令，然后将该缓冲区提交到命令队列。Metal 会将这些命令发送给 GPU 去执行。

### 编写一个执行计算的 GPU 函数

为了演示 GPU 编程，该 App 会将两个数组中对应的元素相加，并把结果存储到第三个数组中。下面的 C 语言示例通过遍历索引、每次计算一个值，在 CPU 上完成这项计算。

**main.m**

```c
void add_arrays(const float* inA,
                const float* inB,
                float* result,
                int length)
{
    for (int index = 0; index < length ; index++)
    {
        result[index] = inA[index] + inB[index];
    }
}
```

每个值都是独立计算的，因此这些值可以安全地并发计算。要在 GPU 上执行这项计算，你需要用 Metal 着色语言（MSL）重写这个函数。MSL 是专为 GPU 编程设计的 C++ 变体。在 Metal 中，运行在 GPU 上的代码被称为_着色器_（shader），因为从历史上看，它们最早是用于计算 3D 图形中的颜色。下一个示例展示了一个用 MSL 编写的着色器，它执行的计算与前一个示例相同。示例工程在 `add.metal` 文件中定义了这个函数。Xcode 会构建 App target 中所有的 `.metal` 文件，并创建一个默认的 Metal 库，将其嵌入到你的 App 中。你稍后会在本示例中看到如何加载这个默认库。

**add.metal**

```metal
kernel void add_arrays(device const float* inA,
                       device const float* inB,
                       device float* result,
                       uint index [[thread_position_in_grid]])
{
    // the for-loop is replaced with a collection of threads, each of which
    // calls this function.
    result[index] = inA[index] + inB[index];
}
```

这两个示例很相似，但 MSL 版本中有一些重要的区别。

在 MSL 示例中，该函数添加了 `kernel` 关键字，用于声明这个函数是：

- 一个_公开的 GPU 函数_。公开函数是你 App 唯一可见的函数。公开函数也不能被其他着色器函数调用。
- 一个_计算函数_（也称为计算内核），它使用一个线程网格执行并行计算。

关于声明公开图形函数的其他关键字，请参阅[使用 Metal 4 绘制三角形](drawing-a-triangle-with-metal-4.md)。

`add_arrays` 函数用 `device` 关键字声明了它的三个参数，表示这些指针位于 `device` 地址空间中。MSL 为内存定义了若干互不相交的地址空间。每当你在 MSL 中声明一个指针时，都需要提供一个关键字来声明它的地址空间。使用 `device` 地址空间来声明 GPU 可以读写的持久性内存。

MSL 版本去掉了 C 版本中的 for 循环，因为 GPU 会用计算网格中的多个线程来调用该函数。本示例创建了一个恰好与数组维度匹配的一维网格，这样数组中的每个条目都会由不同的线程来计算。

为了替代之前由 for 循环提供的索引，该函数新增了一个 `index` 参数，并使用 C++ 属性语法指定了另一个 MSL 关键字 `thread_position_in_grid`。这个关键字声明了 Metal 应该为每个线程计算一个唯一的索引，并将该索引通过这个参数传入。由于 `add_arrays` 使用的是一维网格，因此该索引被定义为一个标量整数。尽管 MSL 示例去掉了循环，但两个示例中用来把两个数字相加的那一行代码是相同的。如果你想把类似的代码从 C 或 C++ 转换为 MSL，可以用同样的方式，把循环逻辑替换为网格。

### 查找一个 GPU

在你的 App 中，[MTLDevice](mtldevice.md) 对象是对 GPU 的一层轻量抽象；你用它与某个 GPU 通信。Metal 会为每个 GPU 创建一个 `MTLDevice`。你可以通过调用 [MTLCreateSystemDefaultDevice](<mtlcreatesystemdefaultdevice().md>) 来获取默认的设备对象。在 macOS 中，一台 Mac 可能拥有多个 GPU，Metal 会从中选择一个作为默认 GPU，并返回该 GPU 的设备对象。在 macOS 中，Metal 还提供了其他 API，可用来获取所有设备对象，但本示例只使用默认设备。

**main.m**

```objective-c
id<MTLDevice> device = MTLCreateSystemDefaultDevice();
```

### 初始化 Metal 对象

Metal 会把其他与 GPU 相关的实体（比如已编译的着色器、内存缓冲区和纹理）表示为对象。要创建这些特定于 GPU 的对象，你需要在 [MTLDevice](mtldevice.md) 上调用方法，或者在由 [MTLDevice](mtldevice.md) 创建的对象上调用方法。任何由某个设备对象直接或间接创建的对象，都只能与该设备对象一起使用。同时使用多个 GPU 的 App，会为每个 GPU 各持有一个设备实例，并为它们分别创建类似的 Metal 类型实例层级结构。

示例 App 使用一个自定义的 `MetalAdder` 类来管理它与 GPU 通信所需的对象。该类的初始化方法会创建这些对象并将其存储在自己的属性中。App 会创建这个类的一个实例，并传入用于创建这些次级对象的 Metal 设备对象。`MetalAdder` 对象会一直强引用这些 Metal 对象，直到执行完成。

**main.m**

```objective-c
MetalAdder* adder = [[MetalAdder alloc] initWithDevice:device];
```

在 Metal 中，开销较大的初始化任务只需运行一次，其结果就可以被保留下来并低成本地重复使用。你几乎不需要在性能敏感的代码中运行这类任务。

### 获取该 Metal 函数的引用

初始化方法要做的第一件事，就是加载这个函数并让它做好在 GPU 上运行的准备。当你构建 App 时，Xcode 会编译 `add_arrays` 函数，并将其加入到嵌入 App 中的默认 Metal 库里。你可以使用 [MTLLibrary](mtllibrary.md) 和 [MTLFunction](mtlfunction.md) 对象来获取关于 Metal 库及其中所含函数的信息。要获取一个代表 `add_arrays` 函数的对象，需要让 [MTLDevice](mtldevice.md) 为默认库创建一个 [MTLLibrary](mtllibrary.md) 对象，然后向该库请求一个代表该着色器函数的 [MTLFunction](mtlfunction.md) 对象。

**MetalAdder.m**

```objective-c
- (instancetype) initWithDevice: (id<MTLDevice>) device
{
    self = [super init];
    if (self)
    {
        _mDevice = device;

        NSError* error = nil;

        // Load the shader files with a .metal file extension in the project

        id<MTLLibrary> defaultLibrary = [_mDevice newDefaultLibrary];
        if (defaultLibrary == nil)
        {
            NSLog(@"Failed to find the default library.");
            return nil;
        }

        id<MTLFunction> addFunction = [defaultLibrary newFunctionWithName:@"add_arrays"];
        if (addFunction == nil)
        {
            NSLog(@"Failed to find the adder function.");
            return nil;
        }
```

### 准备一条 Metal 管线

函数对象是 MSL 函数的一个代理，但它本身并不是可执行代码。你需要通过创建一条_管线_，把该函数转换为可执行代码。管线指定了 GPU 完成某项具体任务所要执行的步骤。在 Metal 中，管线由一个_管线状态对象_表示。由于本示例使用的是计算函数，因此该 App 会创建一个 [MTLComputePipelineState](mtlcomputepipelinestate.md) 对象。

**MetalAdder.m**

```objective-c
_mAddFunctionPSO = [_mDevice newComputePipelineStateWithFunction: addFunction error:&error];
```

一条计算管线运行单个计算函数，在运行该函数之前可以选择性地处理输入数据，之后也可以处理输出数据。

当你创建一个管线状态对象时，设备对象会针对这个特定的 GPU 完成该函数的编译。本示例是同步创建管线状态对象，并将其直接返回给 App。由于编译确实需要一些时间，请避免在性能敏感的代码中同步创建管线状态对象。

> [!note] 注意
> 到目前为止你所看到的代码中，Metal 返回的所有对象，都是以遵循协议的对象形式返回的。Metal 使用协议来定义大多数特定于 GPU 的对象，从而对底层实现类进行抽象——这些实现类在不同 GPU 上可能有所不同。Metal 使用类来定义与 GPU 无关的对象。任何给定 Metal 协议的参考文档都会清楚说明你是否可以在自己的 App 中实现该协议。

### 创建一个命令队列

要向 GPU 发送工作，你需要一个命令队列。Metal 使用命令队列来调度命令。通过向 [MTLDevice](mtldevice.md) 请求，创建一个命令队列。

**MetalAdder.m**

```objective-c
_mCommandQueue = [_mDevice newCommandQueue];
```

### 创建数据缓冲区并加载数据

初始化基本的 Metal 对象之后，你需要为 GPU 加载要执行的数据。这项任务对性能不太敏感，但仍然适合在你 App 启动早期就完成。

GPU 可以拥有自己专属的内存，也可以与操作系统共享内存。Metal 和操作系统内核需要做一些额外的工作，才能让你把数据存储在内存中，并让 GPU 能够访问这些数据。Metal 使用_资源_对象（[MTLResource](mtlresource.md)）对这种内存管理进行了抽象。资源是 GPU 在执行命令时可以访问的一段内存分配。使用 [MTLDevice](mtldevice.md) 为其 GPU 创建资源。

示例 App 创建了三个缓冲区，为前两个填充随机数据，并将 `add_arrays` 的结果存储在第三个缓冲区中。

**MetalAdder.m**

```objective-c
_mBufferA = [_mDevice newBufferWithLength:bufferSize options:MTLResourceStorageModeShared];
_mBufferB = [_mDevice newBufferWithLength:bufferSize options:MTLResourceStorageModeShared];
_mBufferResult = [_mDevice newBufferWithLength:bufferSize options:MTLResourceStorageModeShared];

[self generateRandomFloatData:_mBufferA];
[self generateRandomFloatData:_mBufferB];
```

本示例中的资源是 [MTLBuffer](mtlbuffer.md) 对象，它们是没有预定义格式的内存分配。Metal 将每个缓冲区都作为一段不透明的字节集合来管理。不过，当你在着色器中使用某个缓冲区时，需要自己指定其格式。这意味着你的着色器和你的 App 需要就来回传递的任何数据的格式达成一致。

在分配一个缓冲区时，你需要提供一个存储模式，用来决定它的一些性能特性，以及 CPU 或 GPU 能否访问它。示例 App 使用的是共享内存（[MTLResourceStorageModeShared](mtlresourceoptions/storagemodeshared.md)），CPU 和 GPU 都可以访问它。

要用随机数据填充一个缓冲区，该 App 会获取该缓冲区内存的指针，并在 CPU 上向其写入数据。MSL 示例中的 `add_arrays` 函数将参数声明为浮点数数组，这意味着你需要提供相同格式的缓冲区：

**MetalAdder.m**

```objective-c
- (void) generateRandomFloatData: (id<MTLBuffer>) buffer
{
    float* dataPtr = buffer.contents;

    for (unsigned long index = 0; index < arrayLength; index++)
    {
        dataPtr[index] = (float)rand()/(float)(RAND_MAX);
    }
}
```

### 创建一个命令缓冲区

请求命令队列创建一个命令缓冲区。

**MetalAdder.m**

```objective-c
id<MTLCommandBuffer> commandBuffer = [_mCommandQueue commandBuffer];
```

### 创建一个命令编码器

要向命令缓冲区中写入命令，你需要针对想要编码的具体命令种类，使用一个_命令编码器_。本示例创建了一个计算命令编码器，用来编码一个_计算流程_。计算流程持有一份执行计算管线的命令列表。每条计算命令都会让 GPU 创建一个线程网格，在 GPU 上执行。

**MetalAdder.m**

```objective-c
id<MTLComputeCommandEncoder> computeEncoder = [commandBuffer computeCommandEncoder];
```

要编码一条命令，你需要在编码器上依次调用一系列方法。有些方法用来设置状态信息，比如管线状态对象（PSO）或要传递给该管线的参数。在完成这些状态更改之后，你再编码一条命令来执行该管线。编码器会把所有的状态更改和命令参数写入命令缓冲区。

![命令编码](../../../attachments/ec94660b320c7fbdcdc5c53327507e16/performing-calculations-on-a-gpu@2x.png)

### 设置管线状态和参数数据

设置你想让该命令执行的那条管线的管线状态对象。然后为该管线需要传入 `add_arrays` 函数的所有参数设置数据。对于这条管线来说，这意味着要提供三个缓冲区的引用。Metal 会按照参数在 MSL 示例的函数声明中出现的顺序，自动为这些缓冲区参数分配索引，从 `0` 开始。你在提供参数时使用相同的索引。

**MetalAdder.m**

```objective-c
[computeEncoder setComputePipelineState:_mAddFunctionPSO];
[computeEncoder setBuffer:_mBufferA offset:0 atIndex:0];
[computeEncoder setBuffer:_mBufferB offset:0 atIndex:1];
[computeEncoder setBuffer:_mBufferResult offset:0 atIndex:2];
```

你还需要为每个参数指定一个偏移量。偏移量为 `0` 表示该命令从缓冲区的起始位置访问数据。不过，你也可以用一个缓冲区存储多个参数，为每个参数分别指定一个偏移量。

你不需要为 index 参数指定任何数据，因为 `add_arrays` 函数把它的值定义为由 GPU 提供。

### 指定线程数量与组织方式

接下来，决定要创建多少个线程，以及如何组织这些线程。Metal 可以创建一维、二维或三维网格。`add_arrays` 函数使用的是一维数组，因此本示例创建了一个大小为（`dataSize` x 1 x 1）的一维网格，Metal 会据此生成介于 0 到 `dataSize`-1 之间的索引。

**MetalAdder.m**

```objective-c
MTLSize gridSize = MTLSizeMake(arrayLength, 1, 1);
```

### 指定线程组大小

Metal 会把网格细分为更小的网格，称为_线程组_。每个线程组都是分别计算的。Metal 可以把线程组分派给 GPU 上不同的处理单元，以加快处理速度。你还需要决定为你的命令把线程组设置成多大。

**MetalAdder.m**

```objective-c
NSUInteger threadGroupSize = _mAddFunctionPSO.maxTotalThreadsPerThreadgroup;
if (threadGroupSize > arrayLength)
{
    threadGroupSize = arrayLength;
}
MTLSize threadgroupSize = MTLSizeMake(threadGroupSize, 1, 1);
```

该 App 向管线状态对象请求可能的最大线程组大小，如果这个大小超过了数据集的大小，就将其缩小。[maxTotalThreadsPerThreadgroup](mtlcomputepipelinestate/maxtotalthreadsperthreadgroup.md) 属性给出了该线程组中允许的最大线程数，这个数值会随着用于创建该管线状态对象的函数的复杂程度而变化。

### 编码计算命令以执行这些线程

最后，编码这条命令，以派发线程网格。

**MetalAdder.m**

```objective-c
[computeEncoder dispatchThreads:gridSize
          threadsPerThreadgroup:threadgroupSize];
```

当 GPU 执行这条命令时，它会使用你之前设置的状态以及该命令的参数来派发线程以执行这项计算。

你可以按照同样的步骤，使用该编码器把多条计算命令编码进这个计算流程中，而不必执行任何多余的步骤。例如，你可以只设置一次管线状态对象，然后针对每一组要处理的缓冲区分别设置参数并编码一条命令。

### 结束计算流程

当你没有更多命令要添加到该计算流程时，需要结束编码过程，以关闭这个计算流程。

**MetalAdder.m**

```objective-c
[computeEncoder endEncoding];
```

### 提交命令缓冲区以执行其中的命令

通过把命令缓冲区提交到队列，来运行该命令缓冲区中的命令。

**MetalAdder.m**

```objective-c
[commandBuffer commit];
```

命令缓冲区是由命令队列创建的，因此提交该缓冲区总是会把它放到那个队列上。提交命令缓冲区之后，Metal 会异步地为执行做准备，然后调度该命令缓冲区在 GPU 上执行。在 GPU 执行完命令缓冲区中的所有命令之后，Metal 会将该命令缓冲区标记为已完成。

### 等待计算完成

在 GPU 处理你的命令期间，你的 App 可以做其他工作。本示例不需要做任何额外的工作，所以它只是简单地等待，直到命令缓冲区完成。

**MetalAdder.m**

```objective-c
[commandBuffer waitUntilCompleted];
```

另外，你也可以给命令缓冲区添加一个完成处理程序（[- addCompletedHandler:](<mtlcommandbuffer/addcompletedhandler(__).md>)），以便在 Metal 处理完所有命令时收到通知，或者通过读取命令缓冲区的 [status](mtlcommandbuffer/status.md) 属性来检查其状态。

### 从缓冲区中读取结果

命令缓冲区完成后，GPU 的计算结果会存储在输出缓冲区中，Metal 会执行任何必要的步骤，确保 CPU 能够看到这些结果。在真实的 App 中，你会从该缓冲区中读取结果并加以处理，比如把结果显示在屏幕上或写入文件。由于这些计算只是用来演示创建 Metal App 的过程，本示例会读取存储在输出缓冲区中的值，并进行测试，以确保 CPU 和 GPU 计算出的结果相同。

**MetalAdder.m**

```objective-c
- (void) verifyResults
{
    float* a = _mBufferA.contents;
    float* b = _mBufferB.contents;
    float* result = _mBufferResult.contents;

    for (unsigned long index = 0; index < arrayLength; index++)
    {
        if (result[index] != (a[index] + b[index]))
        {
            printf("Compute ERROR: index=%lu result=%g vs %g=a+b\n",
                   index, result[index], a[index] + b[index]);
            assert(result[index] == (a[index] + b[index]));
        }
    }
    printf("Compute results as expected\n");
}
```

## 另请参阅

### 基础

- [了解 Metal 4 核心 API](understanding-the-metal-4-core-api.md) — 了解 Metal 4 基础 API 中的功能与特性。
- [使用 Metal 4 绘制三角形](drawing-a-triangle-with-metal-4.md) — 通过在 GPU 上运行带有渲染管线的绘制命令，渲染一个色彩丰富、不断旋转的 2D 三角形。
- [使用 Metal 绘制视图内容](using-metal-to-draw-a-view's-contents.md) — 创建一个 MetalKit 视图和一个渲染流程来绘制该视图的内容。

## 下载

- [PerformingCalculationsOnAGPU.zip](https://docs-assets.developer.apple.com/published/d80f8573d811/PerformingCalculationsOnAGPU.zip)
