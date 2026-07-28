# 暑期学习定向翻译计划

> 基线日期：2026-07-28
> 权威范围：本地《2026 暑假 iOS 底层学习计划》；仓库内可移植映射见
> [`../_indexes/study-plan.md`](../_indexes/study-plan.md)
> 用户最新裁决：**高价值博客优先；Apple 官方文档和 WWDC 只翻译暑期计划实际涉及的部分。**

## 1. 结论

旧的“完整 A 方案”已经停止，不再把下列内容当作当前目标：

- 不再继续翻译宽泛 `core` 范围中的 1,519 篇 Apple / WWDC；
- 不再以“翻完全部 2,053 篇英文博客”为目标；
- 不翻译与暑期计划无关的 SwiftUI、Xcode Cloud、Metal、版本说明、API 实现列表；
- 不翻译 `*-implementations.md` 这类自动生成的协议实现页；
- 不重译 objc.io：学习计划命中的 10 篇已有 objccn 正式中文配对。

新的剩余范围是 **69 篇、1,086,322 个英文字符**：

| 顺序 | 范围 | 待译 | 英文字符 | 选择依据 |
|---|---|---:|---:|---|
| B0 | 暑期计划直接点名的高价值英文博客 | 41 | 666,822 | 先补原理、源码和工程经验 |
| O1 | 暑期计划直接点名的 Apple 现行文档 | 24 | 280,211 | 严格白名单，不扩整个框架 |
| O2 | 暑期计划直接点名的 WWDC | 4 | 139,289 | Runtime、构建、链接、启动 |
| — | **合计** | **69** | **1,086,322** | — |

按前一轮 DeepSeek 实际消耗估算，这一范围约需 **440 万模型 Token**。给失败重试和博客
长文留余量后按 **440–550 万 Token** 准备更稳妥；按历史实付比例估计约 **1.2–2 美元**
的 DeepSeek API 费用。这只是实测外推，不是计费承诺。

暑期计划还引用了 Apple 旧版归档指南。它们属于独立的
`apple-developer-archive-vault`，不计入本仓库 69 篇；需要阅读时从旧仓库进入，不在
这里重复抓取或翻译。

## 2. B0：高价值博客先翻

### 2.1 Objective-C 对象模型、Runtime 与内存

**Always Processing（7 篇，全部优先）**

- `blogs/en/alwaysprocessing/size-matters-an-exploration-of-virtual-memory-on-ios-an-out-of-memory-crash-while-debuggin.md`
- `blogs/en/alwaysprocessing/objective-c-internals-class-architecture-objective-c-has-an-unique-class-architecture-wher.md`
- `blogs/en/alwaysprocessing/objective-c-internals-class-graph-implementation-a-brief-look-at-the-objective-c-runtime-s.md`
- `blogs/en/alwaysprocessing/objective-c-internals-the-many-uses-of-isa-the-objective-c-runtime-optimizes-performance-b.md`
- `blogs/en/alwaysprocessing/objective-c-internals-tagged-pointer-objects-tagged-pointer-objects-a-private-runtime-feat.md`
- `blogs/en/alwaysprocessing/objective-c-internals-retain-objective-c-memory-is-managed-through-a-reference-counting-sc.md`
- `blogs/en/alwaysprocessing/objective-c-internals-associated-references-a-comparison-of-apple-s-associated-references-.md`

**Mike Ash：对象、ARC、weak、Block、消息发送（12 篇）**

- `blogs/en/mikeash/friday-q-a-2008-12-26.md`（Blocks）
- `blogs/en/mikeash/friday-q-a-2009-03-13-intro-to-the-objective-c-runtime.md`
- `blogs/en/mikeash/friday-q-a-2009-03-27-objective-c-message-forwarding.md`
- `blogs/en/mikeash/friday-q-a-2010-01-15-stack-and-heap-objects-in-objective-c.md`
- `blogs/en/mikeash/my-friday-q-a-post-this-week.md`（Zeroing Weak References）
- `blogs/en/mikeash/friday-q-a-2011-09-02-let-s-build-nsautoreleasepool.md`
- `blogs/en/mikeash/friday-q-a-2011-09-30-automatic-reference-counting.md`
- `blogs/en/mikeash/tagged-pointers.md`（Let’s Build Tagged Pointers）
- `blogs/en/mikeash/friday-q-a-2015-07-31-tagged-pointer-strings.md`
- `blogs/en/mikeash/friday-q-a-2017-06-30-dissecting-objc-msgsend-on-arm64.md`
- `blogs/en/mikeash/friday-q-a-2017-09-22-swift-4-weak-references.md`
- `blogs/en/mikeash/previous.md`（Exploring Swift Memory Layout）

**其他直接补强（5 篇）**

- `blogs/en/cocoawithlove/what-is-a-meta-class-in-objective-c-cocoa-with-love.md`
- `blogs/en/mikeash/friday-q-a-2012-03-02-key-value-observing-done-right-take-2.md`
- `blogs/en/nshipster/associated-objects.md`
- `blogs/en/nshipster/key-value-observing.md`
- `blogs/en/nshipster/method-swizzling.md`

### 2.2 GCD、Operation、锁与性能测量

- `blogs/en/mikeash/friday-q-a-2009-08-28-intro-to-grand-central-dispatch-part-i-basics-and-dispatch-queues.md`
- `blogs/en/mikeash/friday-q-a-2015-09-04-let-s-build-dispatch-queue.md`
- `blogs/en/mikeash/friday-q-a-2016-04-15-performance-comparisons-of-common-operations-2016-edition.md`
- `blogs/en/mikeash/friday-q-a-2017-10-27-locks-thread-safety-and-swift-2017-edition.md`
- `blogs/en/nshipster/nsoperation.md`

### 2.3 UIKit、滚动性能、卡顿监控与架构

- `blogs/en/fbeng/delivering-high-scroll-performance.md`
- `blogs/en/fbeng/the-evolution-of-facebook-s-ios-app-architecture.md`
- `blogs/en/jessesquires/how-to-find-and-fix-premature-view-controller-loading-on-ios.md`
- `blogs/en/jessesquires/implementing-a-main-thread-watchdog-on-ios.md`

RunLoop 不再补英文译文作为前置条件：仓库已有 ibireme《深入理解 RunLoop》的原生中文
全文。objc.io 在这一阶段命中的并发、通信、动画、表格、MVVM 文章已有 objccn 配对，也不
重复翻译。

### 2.4 Mach-O、链接与启动

- `blogs/en/mikeash/friday-q-a-2009-11-06-linking-and-install-names.md`
- `blogs/en/mikeash/friday-q-a-2012-11-30-let-s-build-a-mach-o-executable.md`
- `blogs/en/emergetools/emerge-tools-blog-how-ios-15-makes-your-app-launch-faster.md`
- `blogs/en/emergetools/emerge-tools-blog-how-order-files-reduce-app-startup-time.md`

旧文章中的工具命令、时间数据和 dyld 版本必须在译文中忠实保留，但审校时要避免把历史实现
描述成当前系统事实；必要时只在译者注中标明“原文发布年代”，不得擅自改写原文。

### 2.5 集合与序列化

- `blogs/en/ciechanowski/exposing-nsdictionary-bartosz-ciechanowski.md`
- `blogs/en/ciechanowski/exposing-nsmutablearray-bartosz-ciechanowski.md`
- `blogs/en/kreya/demystifying-the-protobuf-wire-format-kreya.md`
- `blogs/en/kreya/demystifying-the-protobuf-wire-format-part-2-kreya.md`

## 3. O1：Apple 现行文档严格白名单

只有下面 24 篇属于本轮官方文档目标。即使同一框架还有大量待译页面，也不得顺带扩展。

### 第一至三周：对象、通信与 Runtime 周边

- `apple-docs/en/foundation/nscopying.md`
- `apple-docs/en/foundation/notificationcenter.md`

### 第四周：并发、Operation 与锁

- `apple-docs/en/dispatch/dispatchqos.md`
- `apple-docs/en/dispatch/dispatchqueue.md`
- `apple-docs/en/dispatch/dispatchsource.md`
- `apple-docs/en/dispatch/dispatchworkitemflags/barrier.md`
- `apple-docs/en/foundation/operation.md`
- `apple-docs/en/foundation/operationqueue.md`
- `apple-docs/en/os/os_unfair_lock.md`

### 第五、六周：RunLoop、响应者链、视图控制器与表格

- `apple-docs/en/corefoundation/cfrunloop.md`
- `apple-docs/en/uikit/uiresponder.md`
- `apple-docs/en/uikit/uiviewcontroller.md`
- `apple-docs/en/uikit/uitableview.md`
- `apple-docs/en/uikit/uitableviewdatasource.md`
- `apple-docs/en/uikit/uitableviewdelegate.md`

### 第七周：Mach-O

- `apple-docs/en/kernel/mach-o.md`

### 第八阶段：存储、序列化与网络

- `apple-docs/en/foundation/jsonserialization.md`
- `apple-docs/en/foundation/nsdictionary.md`
- `apple-docs/en/foundation/nsmutablearray.md`
- `apple-docs/en/foundation/urlcache.md`
- `apple-docs/en/foundation/urlsession.md`
- `apple-docs/en/foundation/userdefaults.md`
- `apple-docs/en/foundation/using-the-file-system-effectively.md`
- `apple-docs/en/security/keychain-services.md`

计划点名且已经有译文的 7 篇无需重做：

- `apple-docs/zh/coredata.md`
- `apple-docs/zh/foundation/url-loading-system.md`
- `apple-docs/zh/uikit/filling-a-table-with-data.md`
- `apple-docs/zh/uikit/using-responders-and-the-responder-chain-to-handle-events.md`
- `apple-docs/zh/xcode/improving-your-app-s-performance.md`
- `apple-docs/zh/xcode/performance-and-metrics.md`
- `apple-docs/zh/xcode/reducing-your-app-s-launch-time.md`

## 4. O2：WWDC 严格白名单

- `wwdc/en/wwdc2020/10163-advancements-in-the-objective-c-runtime.md`
- `wwdc/en/wwdc2018/415-behind-the-scenes-of-the-xcode-build-process.md`
- `wwdc/en/wwdc2022/110362-link-fast-improve-build-and-launch-times.md`
- `wwdc/en/wwdc2019/423-optimizing-app-launch.md`

其他 144 场未译 WWDC 暂停。只有当暑期计划新增明确引用，或某个实验缺少一手解释时，才
能把单篇加入白名单。

## 5. B1：后续高价值博客候选池

69 篇是当前可直接执行的确定范围，不代表高价值博客永远只保留 41 篇。B0 完成后，如果
仍有预算，可以继续从以下来源逐篇筛选：

- Always Processing 的 Objective-C Internals 系列；
- Mike Ash Friday Q&A 中的 Runtime、内存、并发、链接与语言实现文章；
- Belkadan 的 Swift Runtime / ABI 系列；
- Cocoa with Love 的底层机制文章；
- Emerge Tools、Low Level Bits 等有实测证据的启动、体积和性能文章。

进入 B1 必须同时满足“作者/来源可信、讲原理或有可复现实验、直接补足八周主题、不是已有
中文材料的低价值重复”四项。先把候选路径追加到本文件，再生成分片；不得把整个作者站点
直接加入翻译队列。

## 6. 执行顺序与批次

1. **B0-Runtime**：Always Processing 7 篇 + Mike Ash Runtime/内存 12 篇；
2. **B0-并发与 UI**：GCD/锁 5 篇 + UIKit/性能/架构 4 篇；
3. **B0-构建与数据**：Mach-O/启动 4 篇 + 集合/Protobuf 4 篇 + 其他 Runtime 5 篇；
4. **O1**：24 篇 Apple 白名单；
5. **O2**：4 篇 WWDC 白名单。

每轮仍执行：

`初译 → 独立审校 → validate.py → audit_consistency.py → 人工抽检 → 提 PR → 用户审核合并`

批次约束：

- 博客一篇一组，不按作者把数十篇合成一个巨组；
- 每个 PR 建议 8–15 篇，或 120K–180K 英文字符；
- 初译和审校必须是隔离请求，不能让初译模型声明自己已经独立审校；
- 只提交 `zh/`、必要的术语裁决和进度文档；
- 不提交 `.staging/`、`meta/shards/`、API Key 或模型原始响应；
- 不覆盖已有译文，不改 `en/`；
- 所有翻译 PR 只能由执行者提交，最终由用户审核合并。

## 7. 当前断点处理

`.staging/deepseek/core-r04-all/` 和本机旧的 64 个分片可以保留作历史证据，但**不得继续
运行**。它们混入了大量新范围之外的官方页面。

下一次执行必须：

1. 从本文件白名单重新生成任务清单；
2. 再次排除已经存在的 `zh/` 和 objc.io / objccn 配对；
3. 使用新的 `run-id`，例如 `summer-b0-r01`；
4. 先 `--limit 3` 冒烟并人工审阅；
5. 冒烟通过后再放大并发。

现有 `tools/shard.py --scope core` 是旧的宽泛框架范围，不能用于这个新计划。后续若修改
调度器，应新增显式的 `summer` / allowlist 范围，而不是重新定义 `core` 后让历史命令静默
改变含义。

## 8. 完成定义

69 篇白名单全部完成后，本轮翻译计划结束。仓库外仍存在数千篇未译官方文档和博客是正常
状态，不再视为本项目当前缺口。

新增范围必须满足以下至少一项：

- 被暑期学习计划明确引用；
- 是某个计划实验不可替代的一手文档；
- 属于高价值作者的原理/源码文章，并直接补足八周主题；
- 用户明确要求加入。

不能仅因为“英文原文已经在仓库里”就自动加入翻译队列。
