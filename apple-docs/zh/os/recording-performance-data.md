---
title: 记录性能数据
framework: os
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/os/recording-performance-data
source_url: 'https://developer.apple.com/documentation/os/recording-performance-data'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/recording-performance-data.json'
content_hash: 'sha256:62f28301f70acc4a'
translated: true
---

> 导航：[Technologies](../technologies.md) · [os](../os.md) · [Logging](logging.md)

# 记录性能数据

<sub>文章</sub>

添加 signpost 来记录感兴趣的、基于时间的事件。

## 概述

用户会注意到 App 性能下降，这让性能调优成为 App 开发中至关重要的一环。如果你的 App 会执行多项任务并利用并发，往往很难可视化地看出哪些任务正在执行、每个任务各花了多长时间才完成。

signpost 让你可以用与日志记录相同的子系统和分类来测量 App 的任务。用 [OSSignposter](ossignposter.md) 给 App 添加 signpost 之后，你可以用 Xcode 的 Instruments App 在执行待测量的任务时记录 App 的行为，Instruments 会把这些数据显示在一条时间线上。如果你的工作负载比较复杂，还可以创建一个 instrument，以自定义的方式呈现 App 的 signpost 数据。

### 消除同一任务各实例之间的歧义

发出 signpost 时，你需要能够区分同一段被测量代码的不同调用。例如，如果你的 App 会向远程服务器请求数据，而你正在测量这些请求，你就需要能够识别每一个单独的请求，尤其是在多个请求并发执行时。为此，把一个 signpost ID 关联到每一组相关的 signpost 上。

创建 signpost ID 最简单的方法是调用你的 signposter 的 [makeSignpostID()](<ossignposter/makesignpostid().md>) 方法，它会在该 signposter 的作用域内创建一个唯一标识符。下面的示例展示了如何创建一个可用于追踪特定请求的 signpost ID：

```swift
// Create a signposter that uses the default subsystem and category.
let signposter = OSSignposter()
        
// Generate a signpost ID to associate with a signposted interval.
let signpostID = signposter.makeSignpostID()
```

或者，也可以使用系统定义的某个 signpost ID，或者从 App 某个对象的实例派生出一个。这两种方法各有需要注意的地方。详见 [OSSignpostID](ossignpostid.md)。

### 发出带 signpost 标记的时间区间和事件

生成 signpost ID 之后，为想要测量的任务发出 signpost。要开始一个带 signpost 标记的时间区间，使用 signposter 的 [beginInterval(_:id:)](<ossignposter/begininterval(__id_).md>) 方法。保存该方法返回的时间区间状态，然后把它传给 [endInterval(_:_:)](<ossignposter/endinterval(____).md>) 方法来结束这个时间区间。时间区间状态包含 signpost ID，signposter 用它来配对这两次调用，并执行一系列运行时断言。[OSSignposter](ossignposter.md) 还提供了这两个方法的替代版本，让你可以捕获一条 Instruments 会显示的消息，此外还提供了用于测量特定闭包执行情况的方法。要标记时间上的单个关注点，使用 [emitEvent(_:id:)](<ossignposter/emitevent(__id_).md>) 方法。

下面的示例创建了一个带 signpost 标记的时间区间，用于测量处理一次服务器请求所花的时间。它还在这个过程中发出了一个值得注意的事件。

```swift
func processRequest(_ request: URLRequest, signposter: OSSignposter) {
    // Generate a signpost ID to associate with the signposted interval.
    let signpostID = signposter.makeSignpostID()
        
    // Begin a signposted interval and store the interval state.
    let state = signposter.beginInterval("processRequest", id: signpostID)
        
    let data = fetchData(from: request)
        
    // Emit an event to mark a specific point of interest.
    signposter.emitEvent("Fetch complete.", id: signpostID)
    processData(data)
        
    // End the signposted interval using the stored interval state.
    signposter.endInterval("processRequest", state)
}
```

### 在 Instruments 中查看 signpost

要记录和查看你的 signpost，在 Xcode 中打开你的项目，选择 Product \> Profile 来启动 Instruments。选择 Blank 分析模板，然后点按添加按钮 (+) 打开 Instrument 资源库。双击 os_signposts instrument，把它添加到你的会话中。然后点按 Record 按钮，执行你想在 App 中测量的任务。os_signpost instrument 会为每一种子系统与分类的组合显示单独的行，时间线下方的表格则为 Instruments 捕获到的每个 signpost 提供详细信息。

![](../../../attachments/2ae4fce259d625a63eadf1927479a993/media-3854076@2x.png)

<sub>Instruments App 的一张截图，展示了若干条已捕获的 signpost。上方的窗格以时间线形式显示这些 signpost，下方的窗格是一张表格，列出各个 signpost 及其对应的元数据。</sub>

如果你的 App 生成的 signpost 数据量很大，用标准 instrument 分析可能会比较困难。可以考虑构建一个自定义 instrument 来替你完成分析工作。找出 App 的具体行为，创建一套规则来检测并显示相应的数据。详情参见 [Creating Custom Instruments](https://developer.apple.com/videos/play/wwdc2018/410/)。

## 另请参阅

### 测量事件

- [OSSignposter](ossignposter.md) — 用于借助统一日志系统测量任务性能的对象。
- [Legacy Signpost Symbols](legacy-signpost-symbols.md) — 把你的代码从这些遗留符号迁移出来。
- [OSSignpostType](ossignposttype.md) — signpost 的各种类型。 _(已废弃)_
- [os_signpost_id_t](os_signpost_id_t.md) — 用于区分名称和目标日志相同的多个 signpost 的标识符。
