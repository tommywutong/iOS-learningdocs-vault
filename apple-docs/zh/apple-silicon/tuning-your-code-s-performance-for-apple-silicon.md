---
title: 为 Apple silicon 优化代码性能
framework: os
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/apple-silicon/tuning-your-code-s-performance-for-apple-silicon
source_url: 'https://developer.apple.com/documentation/apple-silicon/tuning-your-code-s-performance-for-apple-silicon'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/apple-silicon/tuning-your-code-s-performance-for-apple-silicon.json'
content_hash: 'sha256:5336608edb806a9e'
translated: true
---

> 导航：[技术](../technologies.md) · [Apple silicon](../apple-silicon.md)

# 为 Apple silicon 优化代码性能

<sub>文章</sub>

优化代码，使其在 Apple silicon 和基于 Intel 的 Mac 电脑上都能发挥最佳性能。

## 概述

要优化代码性能，需要在 Apple silicon 和基于 Intel 的 Mac 电脑上分别进行调优。在一个平台上运行良好的代码，在另一个平台上可能表现不佳；对底层硬件做出的假设也可能导致代码中出现意想不到的性能衰退（regression）。在实际硬件上测试是验证代码运行高效且无性能衰退的唯一方法。

提升两个平台性能的方法之一是尽可能利用 Apple 技术。Apple 会针对每种架构优化其框架，并通常提供 API 来帮助你调整自己代码的性能。充分利用这些 API，确保你的代码在所有 Mac 电脑上高效运行。

![Mac 电脑的非对称与对称核心差异示意图。](../../../attachments/90fa376487547a82aa73139b9b65bdd4/tuning-your-code-s-performance-for-apple-silicon-1@2x.png)

### 使用 Instruments 及其他 Apple 工具收集信息

使用 Instruments 在 Apple silicon 和基于 Intel 的 Mac 电脑上收集 App 的性能数据。Instruments 在这两种系统上原生运行，并提供相同的工具来收集数据。利用收集到的数据，你可以识别潜在的性能衰退，以及可能需要修改的代码部分。

### 为工作分配服务质量（QoS）等级

服务质量（Quality-of-Service，QoS）等级用于分类通过 [Operation](../foundation/operation.md) 对象、[OperationQueue](../foundation/operationqueue.md) 对象、[Process](../foundation/process.md) 对象、[Thread](../foundation/thread.md) 对象、dispatch 队列以及 POSIX 线程（pthreads）执行的工作。你分配给某个工作项的 QoS 等级向系统传达了该项目的重要性。系统利用该信息相应地对此项目进行优先级排序和调度。系统定义了以下 QoS 等级：

- 用户交互级（User interactive）——适用于与用户交互的工作，例如在 App 主线程上运行的代码。如果这部分工作不能快速完成，用户界面可能会显得冻结。此类等级追求最高的性能和响应能力。
- 用户发起级（User initiated）——适用于用户发起的工作，例如打开已保存的文稿（document）。用户期望你的 App 能快速完成这些工作。此类等级追求性能和响应能力。
- 实用工具级（Utility）——适用于需要几秒到几分钟才能完成的工作。例如下载文稿或导入数据。此类等级在响应性、性能和能效之间取得平衡。
- 后台级（Background）——适用于用户不可见且可能需要较长时间完成的工作。例如索引、备份或同步数据。此类等级强调能效。

准确分配 QoS 等级可以确保你的 App 在所有 Mac 上既有响应性又节能。在 Apple silicon 上，任务的 QoS 等级会影响系统是否运行该任务。例如，系统更可能将后台任务分配到性能较低的核心上运行，以最大化电池续航。如果你不分配 QoS 等级，你的 App 的响应性和效率可能会因此受到影响。

如果你使用 `pthread_setschedparam`、`setpriority` 或 `thread_set_policy` 手动配置线程的优先级，请改用设置 QoS 等级的 API。例如，使用 `pthread_set_qos_class_self_np` 函数来设置 POSIX 线程的 QoS 等级。

有关系统如何应用和解释 QoS 的更多信息，请参阅《[Mac App 能效指南](https://developer.apple.com/library/archive/documentation/Performance/Conceptual/power_efficiency_guidelines_osx/index.html)》中的[“在任务级别对工作排定优先级”](https://developer.apple.com/library/archive/documentation/Performance/Conceptual/power_efficiency_guidelines_osx/PrioritizeWorkAtTheTaskLevel.html)。有关配置 dispatch 队列和 QoS 等级的更多信息，请参阅 [Dispatch](../dispatch.md)。

### 使用 Grand Central Dispatch 处理任务

Grand Central Dispatch（GCD）负责管理 App 任务的高效执行。使用 GCD 可以在系统的可用核心上串行、并发或并行地执行任务。GCD 处理任务在系统提供的线程上的调度，并将这些线程安排到系统可用的处理器核心上执行。在搭载 Apple silicon 的 Mac 上，GCD 会考虑核心类型的差异，将任务分配到适当的核心类型上，以获得所需的性能或能效。

对于大多数 App，GCD 是执行任务的最佳方案。你可以使用 dispatch 队列（而不是自定义的线程池）来安排任务的执行。Dispatch 队列支持串行或并发地执行任务。

有关如何使用 GCD 的更多信息，请参阅 [Dispatch](../dispatch.md)。

### 高效管理并行计算任务

提升性能的一种方法是将一个问题分解为多个部分，并在可用核心上并行执行这些部分。对于需要大量处理资源的大型任务，可以采用此方法。例如，将一个图像分割成多个部分并并行处理这些部分。

在 GCD 中，[concurrentPerform(iterations:execute:)](<../dispatch/dispatchqueue/concurrentperform(iterations_execute_).md>) 函数接受一个提供的 block，并在系统可用的核心上多次调用它。该函数使用一种“工作窃取”（work‑stealing）算法来确保每个核心都有工作可做，是一种高效并行处理大型任务的方式。在 Apple silicon 上，该算法会将工作高效地分配到各种可用的处理核心和其他的代码路径中，并根据需要动态调整任务的分配。为了充分发挥此算法的优势，迭代次数至少应为系统总核心数的三倍。系统需要足够的迭代次数，以确保任务在不同类型的核心之间得到合理分配。

如果你使用自己的线程池实现并行计算，请使用自己的工作窃取算法来动态分配任务。如果你使用静态分配，那么在能效更高的核心上运行的线程会比在能效更低的核心上运行的线程更快地完成。与 GCD 函数一样，确保任务数量多于核心数量，以保证工作分配的公平性。

### 不要让线程保持活跃且空闲

让一个线程在尝试获取资源时保持活跃，或许能减少线程上下文切换的开销，但代价非常高昂。当一个线程保持活跃却无所事事时，会阻止 CPU 核心做其他工作。在 Apple silicon 上，当消费者线程运行在性能更高的代码路径上，而生产者线程运行在性能更低的路径上时，这种行为会加剧“生产者-消费者”（producer‑consumer）算法中的性能问题。因此，请消除自旋锁（spin lock）和其他导致线程占用核心的自旋等待（spin‑wait）代码。将它们替换为 [os_unfair_lock](../os/os_unfair_lock.md)、条件变量（condition variable）或标准的互斥锁（mutex），使线程可以阻塞（block）。

除了避免自旋锁，还需避免使用 `pthread_yield_np` 及与之等效的函数——这些函数只是将线程的时间让给优先级更高的线程，而不是完全阻塞。与让出（yield）相关的 API 允许当前线程在等待线程优先级较低时继续运行，这会阻止系统调度一些较低优先级的线程并执行有意义的工作。

有关线程同步原语的更多信息，请参阅 [os](../os.md) 框架或 pthreads API。

### 配置代表 App 工作的守护进程和代理

守护进程（daemon）和启动代理（launch agent）是独立的后台进程，为你的 App 提供按需服务。你可以使用它们来提供网页服务、协调对共享数据库的访问，或代表前台 App 执行工作。在创建守护进程或启动代理时，请执行以下操作：

- 始终在守护进程或启动代理的 `Info.plist` 文件中包含 `ProcessType` 键。系统使用此键来确定守护进程的用途，并相应调整其可用资源。例如，将此键设置为 `Adaptive` 会根据与 App 的交互来调整资源。更多信息，请参见 `launchd.plist` 手册页面。
- 使用 XPC 与你的守护进程或启动代理进行通信。系统使用 XPC 消息中的上下文信息来跟踪守护进程或启动代理何时代表你的 App 执行工作。如果你使用套接字（socket）或其他 IPC 机制进行通信，系统将无法跟踪这一点，这可能导致调度决策不够优化。

在 Apple silicon 上，默认情况下，你的 App 的行为不会影响任何关联的守护进程或启动代理的性能特征。当你使用 XPC 时，系统会识别出 App 与守护进程或启动代理之间存在关系。这种关系会使系统将守护进程或启动代理的工作与 App 的性能特征关联起来。

在从 XPC 消息处理器中调度异步任务执行时，Grand Central Dispatch（GCD）和 Core Foundation 等 Apple 技术会自动将相关的 XPC 上下文信息添加到对应的线程状态中。系统依靠该状态信息来跟踪你的 App 与守护进程之间的关系。如果你使用自定义的线程技术来分发工作，请调用 [dispatch_block_create](../dispatch/dispatch_block_create.md) 来捕获 XPC 上下文信息并将其传播到你的自定义线程中。

## 另请参阅

### 性能

- [Apple Silicon CPU Optimization Guide Version 4](cpu-optimization-guide.md) — 识别针对 Apple silicon M 系列和 A 系列芯片的性能优化策略。
