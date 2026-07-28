---
title: 为智能 Instruments 创建自定义建模器
framework: xcode
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 12.2+, macOS 14.2+, Xcode 15.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/creating-custom-modelers-for-intelligent-instruments
source_url: 'https://developer.apple.com/documentation/xcode/creating-custom-modelers-for-intelligent-instruments'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/creating-custom-modelers-for-intelligent-instruments.json'
content_hash: 'sha256:35cea86cff86c72d'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [性能与指标](performance-and-metrics.md)

# 为智能 Instruments 创建自定义建模器

<sub>示例代码</sub>

使用 CLIPS 语言创建自定义建模器，并了解嵌入式规则引擎的工作原理。

## 概述

> [!note] 注意
> 此示例代码与 WWDC 2019 讲座 [421: Modeling in Custom Instruments](https://developer.apple.com/videos/play/wwdc19/421) 相关。

使用此示例代码项目来逐步了解如何为 GoatList（一款显示和修改山羊列表的 App）构建自定义建模器。GoatList App 使用 `MobileAgent` 模式将一个目标（例如对列表排序）分解为更小的子目标。子目标在停止点（stops，满足前置条件的位置）执行，然后继续执行。

Xcode 项目中的每个 Instruments 分发包目标都使用用 CLIPS 语言编写的、逐步更复杂的建模逻辑，来构建一个 Instrument，该 Instrument 可以可视化在 GoatList 中使用的 `MobileAgent` 模式的不同活动部分。

### 配置示例代码项目

此示例需要 Xcode 11 或更高版本以及 iOS 12 或更高版本。

在 Xcode 的目标选择中选择 GoatList，即可在 iOS 模拟器或 iOS 设备上运行示例 App。App 启动后，选择一个建模目标在你的 Mac 上运行。建模目标会启动 Instruments。接着，选择 Blank 模板，然后点击右上角的添加按钮（+）来搜索构建目标时创建的 Instrument。搜索“Mobile Agent”应该能找到自定义 Instrument。在 Instruments 中选择正确的设备和目标进程后，你就可以开始记录了。

### 为 MobileAgent 活动设计自定义建模器

`os_signpost` API 让你可以在 App 中标记重要的事件或时间间隔，并附加可选的消息，是将数据传入 Instruments 的一种有效且强大的方式。此示例 App 实现的 `MobileAgent` 模式仅使用了三条 `os_signpost` 消息，但其功能却非常强大。

`ExecutionModeling`（`mobile-agent-modeling.clp`）目标中的规则依赖 GoatList App 发出的 `os_signpost` 数据来生成时间间隔，在此期间 `MobileAgent` 在一个停止点主动执行。该目标使用 `Mobile Agent Exec` 信号点分两步生成执行间隔：首先，它确定哪个 `MobileAgent` 正在执行；其次，它跟踪 `MobileAgent` 何时开始执行。建模规则通过将事实断言到工作内存（working memory）来处理这些簿记。

一旦示例 App 发出 `Mobile Agent Moved` 信号点，建模逻辑就会检查与发出 `Mobile Agent Moved` 信号点的 `MobileAgent` 相关的执行间隔事实。如果执行间隔事实存在，则认为执行完成，并且 `RECORDER` 模块会使用输出。

### 整合 MobileAgent 过渡

`MobileAgent` 还会进行过渡，当 `MobileAgent` 从一个停止点移动到另一个停止点以执行其下一个子目标时会发生此事件。你可以使用此移动来为 `MobileAgent` 建立执行环境，等待某些条件满足后再让 `MobileAgent` 在一个停止点执行，或发出失败状态信号。

`Mobile Agent Moved` 信号点标记过渡；它也是 `ExecutionModeling` 目标用来确定执行间隔结束的同一个信号点。在 `ExecutionAndTransitionModeling` 中，此信号点扮演了新的角色。除了作为执行间隔的结束标记，它还确定了过渡何时开始。类似地，`Mobile Agent Exec` 信号点也承担了新的角色：它发出过渡结束的信号。

因此，建模器在处理信号点时必须考虑四个可能的逻辑步骤：

1.  如果是 `Mobile Agent Exec` 信号点，则断言一个新的执行簿记事实。
2.  如果是 `Mobile Agent Exec` 信号点，_并且_工作内存中存在之前的_过渡_簿记事实，则关闭过渡时间间隔。
3.  如果是 `Mobile Agent Moved` 信号点，则断言一个新的过渡簿记事实。
4.  如果是 `Mobile Agent Moved` 信号点，_并且_工作内存中存在之前的_执行_簿记事实，则关闭执行时间间隔。

实现这四个步骤需要使用 CLIPS 条件元素（Conditional Element，简称 CE）。CE 的例子包括 `and`、`or` 和 `not`。顾名思义，这些 CE 分别在其所有、任意或没有任何输入表达式满足时激活。`ExecutionAndTransitionModeling` 使用这些 CE 构建匹配四种可能情况的规则。

### 压缩信号点数据

尽管 `os_signpost` 方便将数据传入 Instruments，但请考虑压缩这些数据以减少对记录技术造成的负担。例如，在 GoatList 中，`MobileAgent` 模式发送代表 `MobileAgent` 和 `MobileAgentStop` 类型的整数代码（称为种类代码），而不是在信号点消息中使用描述性字符串。

在建模端，这些代码会扩展为其更长的字符串表示形式。`Modelers` 文件夹中的每个目标都包含将整数种类代码映射回字符串表示形式的事实。当信号点发送种类代码时，建模规则会将代码映射到其字符串表示形式。

### 防止不完整事实到达记录器

`Modelers` 目标包含若干规则，用于注释和增强工作内存事实，使其成为完整的、可供 `RECORDER` 模块输出到数据表的事实。当 `MODELER` 模块输出事实时，防止 `RECORDER` 模块的规则看到不完整的事实并将其插入数据表是很重要的。有几种不同的机制可确保你的建模逻辑在传递给 `RECORDER` 规则之前完全执行，下面将介绍其中两种。

第一种机制涉及 CLIPS 如何确定接下来要触发哪些规则。CLIPS 确保 `MODELER` 模块中的所有激活规则在任何 `RECORDER` 模块中的规则执行之前执行。换句话说，`RECORDER` 规则不会与 `MODELER` 模块中规则的执行交错进行。所有可行的 `MODELER` 规则都会在任何可行的 `RECORDER` 规则执行之前执行。

此外，你可以在规则的 `LHS` 上设置限制，以确定何时适合触发。例如，`RECORDER` 规则可以指定它要求 `mobile-agent-execution-interval` 事实具有包含执行发生的停止点的非空描述。因此，即使种类代码到字符串的映射规则在一个执行周期内没有机会触发，并且 CLIPS 正在考虑哪些 `RECORDER` 规则准备触发，非空限制也意味着种类代码到字符串的解析会在数据表记录任何数据之前发生。

### 避免重叠的时间间隔

将所有执行间隔存储在一个轨道上可能会导致 UI 卡顿，当你的建模器将重叠的时间间隔提交到同一条车道时就会发生这种情况。重叠的时间间隔使得在车道上应显示哪个间隔变得模糊不清。

然而，有时重叠的片段是必需的，例如，如果 `MobileAgent` 在不同的线程（thread）上并发执行。要解决此问题，你需要以某种方式区分数据集，以便它们可以显示在不同的车道或轨道上。如果有多个代理并行运行，可以通过它们运行的线程来区分。你可以使用 plot-template 来区分代理。plot-template 充当模板，为每个独特特征的唯一实例创建单独的图。

在前一段的多线程 MobileAgent 示例中，可以构建一个为每个线程创建图的 plot-template。由于每个线程的图是不同的，重叠的时间间隔不会争用同一条车道。此 Xcode 项目中的 `PlotTemplatesModeling` 目标使用 plot-template 来解决此问题。有关构建 plot-template 的更多信息和示例，请参阅 `PlotTemplatesModeling` 目标。

### 使用推测规则

许多有趣的建模问题都会涉及时间间隔，并且在处理时间间隔时必须实现某些建模结构以支持即时模式（immediate mode）。Instruments 中的即时模式会在数据可用时立即在标准 UI 上显示数据，而不是将数据作为一个大批次处理并在跟踪完成后才进行渲染。诸如 `Time Profiler` 和 `Core Data` 等 Instrument 支持即时模式。

为了支持即时模式，你在构建建模器时必须考虑推测（Speculation）的概念。例如，对于长时间运行的 `Mobile Agent`，建模器规则会断言初始的执行簿记事实，但它们无法知道间隔何时结束。`Mobile Agent` 可能在执行中被延迟，或者可能正在执行一个昂贵的任务。无论哪种情况，在初始的 `Mobile Agent Exec` 信号点和结束的 `Mobile Agent Moved` 信号点之间都有一个不确定的时间。如果没有特殊规则，Instruments UI 将被迫在跟踪完成后重新建模事件，或者为了插入新的间隔而卡顿 UI。如果在跟踪结束前间隔不完整，该间隔也将从跟踪中省略。

为了解决这个问题，请创建一个推测规则（speculation rule）。分析核心（Analysis Core）要求你的建模器推测间隔的结束，以便在间隔关闭前渲染其进度，并在跟踪结束后为你的建模器提供推断间隔可能如何关闭的机会。

推测规则的操作与 `RECORDER` 模块中的其他规则非常相似。它也将条目输出到数据表中，但只是暂时的。推测规则也没有关于间隔的完整信息。例如，考虑 `SpeculationModeling` 目标中的 `mobile-agent-recording.clp` 文件。推测规则要求工作内存中存在一个 `speculate` 事实。该事实包含一个用于请求推测时间的槽位。

```
(defrule RECORDER::speculatively-record-execution
    (speculate (event-horizon ?end))
    (table (table-id ?output) (side append))
    (table-attribute (table-id ?output) (has schema mobile-agent-activity))
    (mobile-agent-execution-started (start ?start)
    (instance ?instance) (stop-kind ?stop-kind&~sentinel))
    
    =>
    (bind ?duration (- ?end ?start))
    (create-new-row ?output)
    (set-column start ?start)
    (set-column duration ?duration)
    (set-column instance ?instance)
    (set-column state "Executing")
    (set-column activity-type "Green")
    (set-column stop-kind ?stop-kind)
    (set-column-narrative activity "Executing at stop %string%" ?stop-kind)
)
```

尽管此规则没有关于 `mobile-agent-execution-interval` 的完整信息，但它确实包含了初始的 `mobile-agent-execution-started` 簿记事实以及请求推测的时间。这两个时间可用于确定推测的持续时间。推测数据表的其余部分使用在推测时可收集到的任何信息填充。

有了推测规则，分析核心现在可以在需要执行任何推测时查询建模器。

### 指定工程类型轨道

Instruments 11 及更高版本支持工程类型轨道。当与增强功能（augmentations）结合使用时，工程类型轨道允许你指定一个工程类型，随着数据表的填充，在 Instruments UI 中动态地将其添加到你其他 Instruments 轨道旁边。

例如，如果有多个线程执行 `MobileAgents`，则负责的线程可以作为轨道显示在 UI 中，并带有可自定义的车道和标题。工程类型轨道有效地将普通的工程类型提升为 Instruments UI 中的一等公民。然后，增强功能与这些提升后的类型一起工作，将它们可视化地呈现在 Instruments UI 上。

`EngineeringTypeTracksModeling` 目标使用这些功能将访问过的停止点显示为 UI 中的独立轨道。MobileAgents 的活动显示在这些轨道内。

### CLIPS 建模器函数

构建自定义建模器需要使用 CLIPS 语言。随 Xcode 一起提供的 CLIPS 发行版提供了丰富的函数集，用于从事实中提取和推断信息。此示例项目大量使用了 CLIPS 函数，但并非每个函数都适用于建模 GoatList。为此，下文记录了大量不同类型的 CLIPS 函数。

### 数据输出操作

### `create-new-row`

在绑定到建模器的输出表中创建新行。唯一的参数是绑定表的 INTEGER `table-id`。这通常作为规则的一部分进行匹配，使用表模式和属性来定位 table-id。创建行后，可以使用 `set-column` 来填充新行的每一列。未填充的列将采用默认值，通常是该工程类型的哨兵值（sentinel，如果已定义）。

```
(table (side append) (table-id ?output))
(table-attribute (table-id ?output) (has schema example))
 =>
(create-new-row ?output)   ;; create the row before trying to set columns
```

### `set-column`

在规则的 RHS 中设置最近创建的行的指定列。第一个参数是列名助记符（在模式中定义），第二个参数是要设置的值。在可能的情况下，会自动从实现类型（例如 INTEGER、STRING、FLOAT、EXTERNAL-ADDRESS）转换为列的工程类型。

```
(set-column size-column ?example-size) ;; Sets size-column to the value ?example-size 
```

### `set-column-narrative`

`set-column-narrative` 与 `set-column` 类似，不同之处在于它应用格式字符串来创建 `narrative` 类型的工程值。narrative 类似于长文本字符串；然而，narrative 的每一部分都会被保留，并用格式字符串中指定的工程类型进行标记。此信息允许 UI 稍后拆分字符串以实现更丰富的呈现。第一个参数是列名助记符，后面是格式字符串，再后面是一系列参数，类似于 printf 风格的格式字符串。

格式字符串参数包含由 `%` 包围的标记，例如：`Some text with a %thread% in the middle`。标记的值必须是有效的工程类型标识符。此示例是一个 `thread` 工程类型。

```
(set-column-narrative narrative-column "Some text with a %thread% in the middle" ?thread-value)
```

### 数据转换

### `process-from-thread`

`thread` 工程类型与特定进程相关联。此函数接受一个线程值作为参数，并返回与其关联的进程对象。

```
(bind ?proc (process-from-thread ?thread)) ;;  Extracts the process object from ?thread and store it in ?proc
(set-column process ?proc) ;; set the process column to the value ?proc
```

### `pid-from-process`

从其参数（必须是 `process` 工程类型）中提取 INTEGER pid。

```
(bind ?process (process-from-thread ?thread))
(bind ?pid (pid-from-process ?process))
```

### `bit-test`

一个布尔返回函数，测试第一个参数的第 n 位，如果该位被设置则返回 true，否则返回 false。第二个参数提供要测试的位索引。位索引范围为 [0-63]，其中位 0 是 INTEGER 的最低有效位。

```
(bit-test ?value-to-test 63) ;  returns true if the most significant bit in ?value-to-test is set
```

### `extract-bits`

通过从第一个参数中提取一定范围的位来返回一个 INTEGER。返回值已移位，使得提取范围中的最低位变为位 0。位 0 是最低有效位。第二个和第三个参数保存要提取的位范围（包含两端）。通常，范围内的最高位是第二个参数，但如果它们颠倒了，函数仍能按预期工作。

```
(extract-bits ?integer-value 63 32) ; extracts the most significant 32-bits and shifts them to the right by 32 bits.
```

### `make-int64`

接受两个 32 位 INTEGER 参数，并将它们连接起来创建一个 64 位 INTEGER 返回值。此函数取第一个参数的高 32 位放入返回值的高 32 位，取第二个参数的低 32 位放入返回值的低 32 位。此函数通常用于重建已被拆分为多个字段的 64 位值时非常有用。即使返回值和参数值是有符号的 INTEGER，它们在内部也被视为无符号位模式。

```
(make-int64 ?msb ?lsb)
```

### `memory-to-string`

将其 INTEGER 参数视为连续的内存值序列，并从中提取 UTF8 编码的字符串。此函数会自动检测 INTEGER 序列是 32 位还是 64 位，假设序列一致为其中一种长度，但_不能_是二者的混合。UTF8 编码约定使我们能够以很小的开销可靠地做出此判断。

注意：你不能将多字段值作为单个参数传递。失败时，此函数将返回符号 `sentinel`。

```
(memory-to-string ?part1 ?part2 ?part3) ; treats the three INTEGER arguments as a run of INTEGERs and returns the string value for it.
```

### 杂项

### `log-narrative`

当通过 Instruments Inspector 为分析核心启用了额外日志记录时，会创建一个建模器日志表，并使用此函数写入该表。当日志记录被禁用时，该函数不执行任何操作，但调用仍会产生少量开销。第一个参数是格式字符串，后面的参数被解释为 printf 风格的参数。

```
(log-narrative "Resolved stop kind code %uint64% to %string%" ?stop-kind-code ?kind)
```

### `(new integer-array)`

创建一个空的 `integer-array` 并返回它。

内置了 `integer-array` 的 EXTERNAL-ADDRESS 类型，允许建模器避免将整数数据序列保存在多字段（multifields）中。多字段通常很高效，但在高数据速率下，或者当你不希望数组的更改导致规则激活时，你可能希望创建此类型的对象并将其用于替代多字段值。`integer-array` 通常在建模器需要累积长的标识符列表（它将作为单个数组在建模结束时发出）或其他周期性事件（例如“滴答”）时非常有用。

### `add-integer`

将第二个参数追加到第一个参数中的 `integer-array`。不会导致规则激活。

### `nth-integer`

返回第一个参数中 `integer-array` 的第 n 个整数。第二个参数是 n。遵循 CLIPS 索引约定，其中 1 是第一个元素，而不是像许多其他语言那样从 0 开始。

### `length-of-array`

返回第一个参数中 `integer-array` 的第 n 个整数。第二个参数是 n。遵循 CLIPS 索引约定，其中 1 是第一个元素，而不是像许多其他语言那样从 0 开始。

### `sort-array`

对第一个参数中的 `integer-array` 进行排序。不会导致规则激活。

### `duplicate-array`

复制第一个参数中的 `integer-array` 并返回 EXTERNAL-ADDRESS。

## 下载

- [CreatingCustomModelersForIntelligentInstruments.zip](https://docs-assets.developer.apple.com/published/58a236c85443/CreatingCustomModelersForIntelligentInstruments.zip)
