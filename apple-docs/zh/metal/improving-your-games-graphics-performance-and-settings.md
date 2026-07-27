---
title: 提升你游戏的图形性能与设置
framework: Metal
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/metal/improving-your-games-graphics-performance-and-settings
source_url: 'https://developer.apple.com/documentation/metal/improving-your-games-graphics-performance-and-settings'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/improving-your-games-graphics-performance-and-settings.json'
content_hash: 'sha256:55f72475fe0b7544'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Metal](../metal.md)

# 提升你游戏的图形性能与设置

<sub>文章</sub>

使用功能强大的 Metal 开发工具套件，修复性能故障并为 Apple 平台上的流畅体验制定默认设置。

## 概述

Metal 游戏的性能需求跨度很大，从要求不高到把硬件推向极限都有。玩家期望流畅的帧率和动画效果，一旦达不到，就会被察觉为游戏中的故障。你可以调查这些故障的根本原因，并通过制定一份数据采集计划来组织你的工作，在做出改进前后测量你的性能数据。

在了解了你游戏的性能特征之后，你就可以根据可用功能集、计算能力和内存资源，为不同设备量身定制玩家体验。你还可以识别出游戏中以性能或画质为导向的功能，并选出一套适用于整个游戏、且能在各种情形下都行之有效的子集。有许多工具，比如 Instruments、Metal HUD 和 GPU 调试器，可以在你调查 Metal 游戏中的性能瓶颈时提供帮助。

### 避免帧故障

理想情况下，如果没有明显的帧故障，玩家就会感觉游戏运行流畅。帧故障通常被定义为任何一种渲染错误、卡顿、突然的视觉变化，以及偏低或不均匀的帧率。当某一帧渲染耗时过长、最终错过了它本应显示到屏幕上的时机时，就会发生卡顿（hitching）。低效的资源流式加载和着色器加载会导致游戏画面出现突然的视觉变化。而不一致的帧率会导致游戏在稳定帧率和较低帧率之间波动，尤其是当玩家需要最佳帧率来良好发挥时，比如在动作场景中。

这些帧故障发生在 CPU 或 GPU 时间线上。例如，游戏在 CPU 时间线上流式加载数据和加载着色器，而你的渲染器则在 GPU 时间线上运行着色器并执行渲染流程。如果游戏在其中一条时间线上出现瓶颈，就可能在另一条时间线上造成延迟。

如果你希望某一帧以特定的每秒帧数（fps）速率渲染，那就需要对游戏进行性能分析，确保它不超过按毫秒（ms）计的每帧特定时间间隔。例如，30 fps 大约是 33 毫秒，40 fps 是 25 毫秒，60 fps 大约是 16 毫秒。如果你把游戏设计为以 60 fps 运行，那么最好让游戏的 CPU 时间不超过 16 毫秒，GPU 时间也不超过 16 毫秒。Apple ProMotion 显示屏支持不同的帧率，因此游戏可以使用诸如 30、40 和 60 fps 之类的速率。请注意，CPU 和 GPU 时间线可以重叠，因此每条时间线最多可占用 16 毫秒。下图展示了一条节奏良好的 CPU 和 GPU 时间线：

![](../../../attachments/6127a4b2ba981eb86502a0e11e61a466/improving-your-games-graphics-performance-and-settings-1@2x.png)

<sub>展示了针对一个由五帧组成的序列进行编码、渲染和显示时，CPU、GPU 和显示时间线的示意图。其时序是统一的，表明没有帧节奏方面的问题。</sub>

通常，每帧的耗时并不一致。屏幕上可见的对象数量各不相同，游戏可能正在流式加载下一关卡，阴影贴图可能需要更新，诸如此类。如果编码和渲染时间保持在其时间预算之内，你游戏的运动就能保持流畅。然而，如果几乎相同的两帧之间存在相当大的差异，那么了解其原因就很重要。下图展示了这种差异并不构成问题的情况：

![](../../../attachments/a4e16b45cf3ea2b4ea8d85a2803301bc/improving-your-games-graphics-performance-and-settings-2@2x.png)

<sub>展示了针对一个由五帧组成的序列进行编码、渲染和显示时，CPU、GPU 和显示时间线的示意图。各个区块的大小并不统一，但都保持在时间限制之内，不会造成帧节奏问题。</sub>

一项意料之外的长任务会在时间线上造成帧故障。例如，当游戏为某个渲染流程加载纹理、模型或着色器时，可能会引入一个数据依赖关系。某些游戏任务会提高 CPU 利用率，并影响游戏的渲染线程。下图展示了 CPU 时间线上的一项长任务如何延迟某一帧的编码，从而导致故障。使用 Instruments 对游戏的各个部分进行性能分析，以排除这些问题。

![](../../../attachments/86aa662fb11204a098600750d12b827a/improving-your-games-graphics-performance-and-settings-3@2x.png)

<sub>展示了针对一个由五帧组成的序列进行编码、渲染和显示时，CPU、GPU 和显示时间线的示意图。CPU 时间线中插入了一项长任务，延迟了其中一帧的编码，导致前一帧被显示了两倍的时长，从而在显示端造成了卡顿。</sub>

要解决这类问题，可以重新组织渲染器的某项长任务，将其拆分到多个帧中完成。计划将这些任务调度到另一个线程上，或者提前处理好任何依赖关系，以免它们造成停滞。下图展示了拆分这项长任务如何解决该故障，并恢复编码线程的最佳时间线：

![](../../../attachments/d5b6650062d1aca8a130436bfc00a104/improving-your-games-graphics-performance-and-settings-4@2x.png)

<sub>展示了针对一个由五帧组成的序列进行编码、渲染和显示时，CPU、GPU 和显示时间线的示意图。上一张图中的长任务被拆分，因此不再延迟各帧的编码，也不会在显示端造成卡顿。</sub>

将同样的方法也应用到 GPU 时间线上。可以考虑使用缓存来存储诸如阴影贴图之类的临时资源，或者使用 GPU 剔除来降低几何复杂度。请注意，并非每一帧都会出现的任务会带来产生延迟的机会。仔细了解游戏渲染管线的每个部分，以定位并消除故障。这里有一些用于测量、理解和修复这些性能问题的技巧。

### 系统地思考性能问题

性能问题通常有若干潜在原因，也就是根本原因。根本原因通常是各自独立的问题，对游戏造成不同程度的影响。修复这些问题的流程是：测量、分析、改进。调查性能问题的第一步是使用工具进行测量。分析这些测量数据，以确定性能问题的根本原因。有些问题很容易发现和修复，但大多数需要深入调查。在确定了根本原因之后，优先修复对游戏性能影响最大的问题。完成这项改进后，重新测量游戏，直到它满足性能要求，或者重复这一改进过程。

「五个为什么」技巧是发现并界定性能问题根本原因的有效方法。反复提出并回答「为什么？」这个问题，重复五次，以更具体地理解问题。以下是一些示例问题和答案：

- 为什么我的游戏会出现帧故障？在 Instruments 的 Metal 系统跟踪记录中，有些帧的渲染耗时超过了 33 毫秒。
- 为什么每帧耗时会超过 33 毫秒？系统跟踪记录显示，游戏花费了 22 毫秒来渲染几何缓冲区。
- 为什么渲染几何缓冲区需要 22 毫秒？测量顶点着色器阶段的耗时显示为 16 毫秒，片段着色器渲染耗时为 6 毫秒。
- 为什么顶点着色器运行需要 16 毫秒？GPU 跟踪记录显示，顶点着色器正在处理 5,000,000 个顶点，看起来受限于 ALU。
- 为什么顶点着色器受限于 ALU？该顶点着色器使用了多次矩阵乘法运算，且没有使用半精度类型。

这个过程会带来提出更多附加问题的机会。一次专注于一条问题线索，并把其他问题记下来留待之后调查。在这个例子中，本可以选择检查顶点着色器耗时或片段着色器耗时。由于顶点着色器耗时似乎是瓶颈的来源，那就是首先要查看的地方。之后，再调查片段着色器，看看是否存在问题。将这些问题和答案画在图表或看板上，有助于看清全局。当你对游戏做出改进后，请再次进行一次完整的性能分析，比较结果，并调查下一个瓶颈在哪里。

### 用计划来组织你的工作

为了保持条理清晰，请制定一份数据采集计划，以确定调查中的关键数据点，并验证你是否达成了预期结果。请安排一个流程，在你采集调查数据时将其存储起来，因为游戏及其数据可能会在开发过程中发生变化。这样可以更方便地记录某个具体问题，或验证你对游戏所做的改进。

性能数据有两种：特定采集和一般采集。Instruments 跟踪记录或 GPU 调试器跟踪记录，就是聚焦于游戏中某个时刻的特定数据采集的例子。一般数据采集的例子则是在整个关卡或整个游戏过程中记录帧率，比如使用 Metal HUD 或屏幕遥测数据。

制定数据采集计划的一些技巧：

- 以描述性的格式在数据测量记录中包含测量的时间和日期。例如，你可以在文件名中使用 `YYYYMMDD-HHMM-工具名称-描述-其他有用信息` 这样的格式。
- 描述你采集数据时游戏中所处的位置，以及相关细节，比如游戏内的时间、游戏坐标，以及玩家和摄像机的朝向。
- 在数据中加上测量工具的名称，比如 Metal HUD、GPU 调试器跟踪记录、Instruments 的 Metal 系统跟踪记录，或游戏内遥测数据。

下面是一个记录帧率测量结果的示例。在一次游戏过程中，开启 Metal HUD 和屏幕遥测数据，录制一段游戏视频。Metal HUD 的日志记录选项会将性能数据打印到控制台，可以将其转换为诸如逗号分隔值（CSV）之类的文件格式，以便用电子表格分析数据。逐帧查看视频以寻找故障。做出改进之后，重新录制一段类似的视频，比较结果以了解改进效果。有关屏幕录制的技巧，请参阅以下资源：

- [如何在 Mac 上录制屏幕](https://support.apple.com/en-us/102618)
- [在 iPhone、iPad 或 iPod touch 上录制屏幕](https://support.apple.com/en-us/102653)

将数据与你想要做出的改进类型相匹配。例如，如果目标是提升帧率，那么记录 GPU 帧时间就至关重要。在这种情况下，使用 Instruments 录制大约 5 到 10 秒的 Metal 系统跟踪记录。另一个使用 Metal HUD 的例子是记录并显示游戏的内存利用率，尤其是当内存中资源过多导致不稳定时。这些性能数据测量方式，有助于为诸如玩家设备能力、偏好帧率或画质等各种情形下正确的初始默认值提供决策依据。

### 为你的游戏选择初始默认值

性能数据对于选择良好的默认设置很有用。选出几组始终有效的选项，而不是把所有选项都呈现给玩家。避免会导致不稳定或性能不佳的设置组合。针对玩家可能使用的各种设备范围优化游戏，并根据游戏运行所在的设备调整默认设置。例如，游戏可以根据内存容量和处理器类型选择一组默认值。举例来说，iOS 上的 [userInterfaceIdiom](../uikit/uidevice/userinterfaceidiom.md) API 会返回游戏所运行设备的种类。有关在不同 Apple 平台上自定游戏行为的详细信息，请参阅文章[在特定平台或操作系统版本上运行代码](../xcode/running-code-on-a-specific-version.md)。

游戏所运行的每种设备——比如 iPhone、iPad 或 Mac——都有着不同范围的性能特征。相比 Mac，玩家期望在 iPhone 上运行的游戏提供更少、但经过调校的设置。为较小的便携设备设计几套效果良好的设置，比如一种优先考虑电池续航和帧率的性能模式，以及一种优先考虑画质的质量模式。对于所有设备，都要调校设置以优化输入延迟、帧节奏，以及与设备上其他功能的互操作性。例如，测试玩家能否在不需要重启的情况下录制屏幕或切换 App。

### 确定适用于整个游戏的一套选项

使用前面提到的数据采集计划，监控整个游戏的关键细节。以下数据点列表有助于确定游戏是否稳定、是否保持在其内存预算之内，以及帧率是否良好：

- 测量时间
- 帧时间和呈现时间
- 内存使用情况
- 游戏的一套选项或图形设置

如果游戏未能达到所需的性能目标，这些数据有助于找出原因。游戏可能需要针对某个关卡进行额外的纹理和几何体优化、修复渲染器、改进着色器，或为某个设备使用不同的图形设置。重复这一过程，直到整个游戏的游玩过程流畅，并达到其性能目标。

### 限制系统的突发性能

在游戏运行期间，使用持续执行模式来限制系统的突发性能。在 `Info.plist` 中加入 [com.apple.developer.sustained-execution](../bundleresources/entitlements/com.apple.developer.sustained-execution.md) entitlement，并将 App 类别设置为「游戏」类别之一。使用此 entitlement，可以在游戏运行期间获得准确的性能测量结果。对游戏中的各个区域进行基准测试和测试，以在不同设备上调校持续性能。

### 检测设备能力以选择设置

游戏可以通过应用以下建议来调整其运行时性能特征：

- 通过将枚举的某个 case——例如 [MTLGPUFamilyApple8](mtlgpufamily/apple8.md)、[MTLGPUFamilyApple9](mtlgpufamily/apple9.md) 等——传给设备的 [- supportsFamily:](<mtldevice/supportsfamily(__).md>) 方法，检查某个 [MTLDevice](mtldevice.md) 实例是否支持某个 [MTLGPUFamily](mtlgpufamily.md) 实例所具备的能力。
- 在某些 iOS 设备上使用 [com.apple.developer.kernel.increased-memory-limit](../bundleresources/entitlements/com.apple.developer.kernel.increased-memory-limit.md) entitlement 来获取额外内存。检查 [os_proc_available_memory](../os/os_proc_available_memory.md) 以获取可用的运行时设备内存量。
- 按照[为 Apple 芯片调校代码性能](../apple-silicon/tuning-your-code-s-performance-for-apple-silicon.md)中所示，使用服务质量（QoS）和 Grand Central Dispatch（GCD）。

要更精细地调校你的 App 和游戏，你可以调用 [Kernel](../kernel.md) 函数 [sysctlbyname](../kernel/1387446-sysctlbyname.md)。有关检查设备具体信息（例如以下内容）的信息，请参阅[确定系统能力](../kernel/1387446-sysctlbyname/determining_system_capabilities.md)和 [Apple Silicon CPU 优化指南](https://developer.apple.com/download/apple-silicon-cpu-optimization-guide/)：

- `hw.perflevels` 用于获取系统中通用核心类型的数量
- `hw.perflevel0.logicalcpu` 用于获取性能核心的数量
- `hw.perflevel1.logicalcpu` 用于获取能效核心的数量

### 在具备硬件支持的设备上支持相应功能

当游戏启动时，使用 [- supportsFamily:](<mtldevice/supportsfamily(__).md>) API 查询 GPU 家族支持情况，并在设备支持的硬件功能可用时加以使用。例如，当硬件支持硬件加速的光线追踪时，优先启用它。如果游戏使用某项功能所需的内存超过了可用内存，那么作为最后手段，请禁用该功能，并在可能的情况下提供后备方案。玩家更倾向于使用硬件所支持的功能。

> [!note] 注意
> 硬件加速的网格着色器和光线追踪在 `MTLGPUFamilyApple9` GPU 家族上得到支持。

### 针对电池续航或低电量模式调整游戏

在设计运行于便携设备上的游戏时，请考虑检测 App 何时进入低电量模式。有关在系统进入低电量模式时获取通知的更多信息，请参阅 [isLowPowerModeEnabled](../foundation/processinfo/islowpowermodeenabled.md) API。这项技巧可以让游戏调整其图形设置，从而减少能耗。例如，游戏可以：

- 降低渲染分辨率
- 限制帧率
- 使用细节更少的模型、纹理和着色器

## 另请参阅

### 开发者工具

- [在 Metal App 中支持模拟器](supporting-simulator-in-a-metal-app.md) — 在你的 Metal App 中配置备用渲染路径，以便能够在「模拟器」中运行你的 App。
- [以编程方式捕获 Metal 命令](capturing-metal-commands-programmatically.md) — 从你的 App 中调用一次 Metal 帧捕获，然后将生成的 GPU 跟踪记录保存到文件中，或在 Xcode 中查看它。
- [记录着色器调试消息](logging-shader-debug-messages.md) — 使用着色器日志记录功能，打印着色器生成的调试消息。
- [开发可在模拟器中运行的 Metal App](developing-metal-apps-that-run-in-simulator.md) — 在「模拟器」中对你的 Metal App 进行原型设计和测试。
- [Metal 调试器](../xcode/metal-debugger.md) — 使用 GPU 跟踪记录调试并分析你的 Metal 工作负载。
- [Metal 开发者工作流程](../xcode/metal-developer-workflows.md) — 定位并修复与你 App 使用 Metal API 和 GPU 函数相关的问题。
- [GPU 计数器与计数器样本缓冲区](gpu-counters-and-counter-sample-buffers.md) — 通过对一个或多个计数器采样，从 GPU 设备中获取运行时数据。
- [Metal 调试类型](metal-debugging-types.md) — 创建捕获管理器和捕获范围，并在 GPU 设备运行某个命令缓冲区之后查看其日志。
