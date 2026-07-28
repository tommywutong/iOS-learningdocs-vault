---
title: 通过 jetsam 事件报告识别高内存使用情况
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/identifying-high-memory-use-with-jetsam-event-reports
source_url: 'https://developer.apple.com/documentation/xcode/identifying-high-memory-use-with-jetsam-event-reports'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/identifying-high-memory-use-with-jetsam-event-reports.json'
content_hash: 'sha256:9e173c04425e5f26'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [调试](debugging.md) · [使用崩溃报告和设备日志诊断问题](diagnosing-issues-using-crash-reports-and-device-logs.md)

# 通过 jetsam 事件报告识别高内存使用情况

<sub>文章</sub>

了解可用内存不足时操作系统终止 App 的原因。

## 概述

iOS、iPadOS、tvOS、visionOS 和 watchOS 具有虚拟内存系统。当操作系统遇到_内存压力（memory pressure）_，也就是可用内存不足、系统无法满足所有运行中 App 的需求时，这个系统依赖所有 App 释放内存。在内存压力下，App 会在收到低内存通知后释放内存。如果所有运行中的 App 总共释放了足够的内存来缓解内存压力，你的 App 就会继续运行。但是，如果 App 没有交还足够的内存，导致内存压力持续存在，系统就会终止应用来回收其内存。这称为 _jetsam 事件（jetsam event）_，系统会创建一份 jetsam 事件报告，其中包含系统为何选择移除某个 App 的信息。

jetsam 事件报告与崩溃报告不同，因为前者包含设备上所有 App 和系统进程的总体内存使用情况，采用 JSON 格式，并且不包含 App 中任何线程的回溯记录。如果系统因内存压力而在 App 可见时将其移除，看起来就像是 App 崩溃了。即使你的 App 没有被移除，也可以使用 jetsam 事件报告来识别 App 在 jetsam 事件中所起的作用。

### 识别内存页大小和最大进程

jetsam 事件报告会记录系统移除 App 之前每个进程所使用的内存量。虚拟内存系统以称为_内存页（memory page）_的区块为单位分配和管理内存，报告则以所用内存页的数量列出内存使用情况。若要将内存页数转换为 App 所用内存的字节数，你需要知道_页大小（page size）_，即一个内存页中的字节数。

jetsam 事件报告标头中的 `pageSize` 字段会记录每个内存页的字节数。除了页大小，jetsam 报告的标头还会描述整体设备环境，例如操作系统版本和硬件型号。在此示例中，页大小为 16,384 字节，即 16 KB。

```other
"crashReporterKey" : "b9aa251a63bd9e743afbb906f43eb7ea5f206292",
"product" : "iPad8,2",
"incident" : "32B05E3C-CB45-40F8-BA66-5668779740E1",
"date" : "2019-10-10 23:30:39.48 -0700",
"build" : "iPhone OS 13.1.2 (17A860)",
"memoryStatus" : {
   "pageSize" : 16384,
},
"largestProcess" : "OneCoolApp",

```

> [!note] 注意
> 此示例显示了诊断 jetsam 事件报告所记录崩溃所需的标头字段。完整的标头信息包含的字段比此示例所示更多。

检查标头时，请查看 `largestProcess` 字段，此字段给出系统上使用内存页数最多的进程名称。如果除你的 App 外还有其他 App 经常被移除，并且你的 App 是最大进程，你就应减少内存使用，以便更好地配合其他 App 的内存需求。

### 识别 jetsam 原因

jetsam 事件报告包含一个 `processes` 数组，其中每一项描述系统中的一个进程。搜索 `reason` 键，以识别被移除的进程以及系统移除它的原因。只有被移除的进程具有 reason 键。

> [!important] 重要
> 如果你的 App 崩溃，但被移除的进程并非你的 App，那么此次崩溃不是内存压力所致。若要诊断 App 的问题，请参阅[获取崩溃报告和诊断日志](acquiring-crash-reports-and-diagnostic-logs.md)，以找到它的崩溃报告。

此示例是 `processes` 数组中的一个进程条目：

```other
{
    "uuid" : "a02fb850-9725-4051-817a-8a5dc0950872",
    "states" : [
      "frontmost"
    ],
    "lifetimeMax" : 92802,
    "purgeable" : 0,
    "coalition" : 68,
    "rpages" : 92802,
    "reason" : "per-process-limit",
    "name" : "MyCoolApp"
}
```

> [!note] 注意
> 此示例显示了诊断 jetsam 事件报告所记录崩溃所需的进程字段。报告中的完整进程信息包含的字段比此示例所示更多。

如果被移除的进程是你的 App，`reason` 键的值会说明导致 jetsam 事件的条件：

- `per-process-limit`：进程越过了系统对所有 App 施加的常驻内存限制。越过此限制后，该进程就符合终止条件。如果此进程是你 App 的 App 扩展（extension），请注意，扩展的单进程内存限制远低于前台 App。在扩展点中使用具有较高基准内存开销的技术（例如 [SpriteKit](../spritekit.md) 或 [MKMapView](../mapkit/mkmapview.md)）之前，请仔细考虑你的需求。其他解决方案可能更合适。例如，由 [MKMapSnapshotter](../mapkit/mkmapsnapshotter.md) 创建的图像比 [MKMapView](../mapkit/mkmapview.md) 使用的内存更少，对许多扩展点场景来说是更好的选择。
- `vm-pageshortage`：系统遇到内存压力，需要为当前前台 App 释放后台进程的内存。
- `vnode-limit`：整个系统中打开的文件过多。内核中为打开文件提供底层支持的内存结构 _vnode_ 数量有限，而这些 vnode 几乎耗尽。为了在 vnode 即将耗尽时避免终止最前端的 App，系统可能会终止处于后台的你的 App 以释放 vnode，即便 App 并非 vnode 使用过量的来源。
- `highwater`：系统守护进程超过了其预期的最高内存占用空间（memory footprint）。
- `fc-thrashing`：某个进程使系统文件缓存发生抖动。频繁读取和写入内存映射文件中的非连续部分时，就会发生这种情况。为了避免终止最前端的 App，系统可能会终止处于后台的你的 App 以释放文件缓存中的空间，即便并非你的 App 导致文件缓存抖动。
- `jettisoned`：系统因其他原因移除了该进程。

若要确定 App 正在使用的内存量，请将 `rpages` 字段报告的内存页数乘以 jetsam 事件报告标头中 `pageSize` 字段的页大小值。结果就是 App 所用内存的字节数。例如，某进程的 `rpages` 值为 92,802，乘以 `pageSize` 值 16,384 字节后，该进程使用 1,520,467,968 字节（1.52 GB）内存。

`processes` 数组中的每一项还具有以下键，它们可为诊断问题提供更多信息。

- `uuid`：二进制文件的构建 UUID。将此值与面向用户分发的构建版本所提供的 dSYM 文件进行比较，有助于识别 App 的版本。若要进一步了解构建 UUID，请参阅[构建 App 以包含调试信息](building-your-app-to-include-debugging-information.md)。
- `states`：描述 App 当前的内存使用状态，例如作为 `frontmost` App 使用内存，或者处于 `suspended` 状态且未主动使用内存。
- `lifetimeMax`：进程生命周期中所分配内存页的最高数量。
- `coalition`：如果 App 的进程属于一个联盟（coalition），其中还有其他系统进程代表 App 执行工作，请使用此信息来识别相关进程及其内存使用情况，因为 App 可以影响其他联盟进程的内存使用量。
- `name`：进程名称。查看此名称是否与 App 的某个二进制文件匹配，或是否属于另一个 App 或系统进程。

### 更改 App 的内存使用情况

分析 jetsam 事件报告并确认 App 是因内存使用量过高而崩溃后，请参阅[收集内存使用信息](gathering-information-about-memory-use.md)来了解 App 的内存使用模式，并参阅[进行更改以减少内存使用](making-changes-to-reduce-memory-use.md)，了解降低内存使用量的技巧。

除了降低 App 的内存使用量，还要确保你能够收到系统发送的低内存警告并据此采取行动，以配合操作系统的需求并降低 App 的内存使用量。有关系统通知 App 的具体方式，请参阅[响应低内存警告](responding-to-low-memory-warnings.md)。

## 另请参阅

### 相关文档

- [减少 App 的内存使用](reducing-your-app-s-memory-use.md) — 通过分析内存使用指标并进行更改以最大限度提高内存效率，改善 App 的性能。

### 设备日志

- [日志记录](../os/logging.md) — 使用统一日志记录系统捕获 App 的遥测数据，以便进行调试和性能分析。
