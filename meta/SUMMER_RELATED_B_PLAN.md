# 暑期强相关 B 类翻译计划

> 用户于 2026-07-29 确认本计划。它取代“只翻译 289 个直接链接”的狭义理解，但不会恢复
> 旧的宽泛 `core` 范围。机器白名单由 `tools/summer_related_b.py` 生成。

## 1. 唯一范围

本轮只处理 **B 类：虽然未必被暑期计划直接贴出 URL，但与暑期底层学习主题高度相关、
值得形成中文译文的成篇资料**。

289 个去重链接仍是重要证据，但不再是唯一边界。不得把“不在 289 个链接中”解释成
“无需翻译”。

本轮不处理：

- 已有中文译文、原生中文文章，以及 objc.io/objccn 的 149 对官方中文配对；
- StoreKit、支付、地图、健康、空间计算、游戏和其他专门业务框架；
- Release Notes、自动生成索引、常量表、错误码表、结构体表和重复的
  `... Implementations` 页面；
- 纯源代码；GitHub 仓库只翻译 README、Wiki 或设计文档；
- 与当前主题只有词面碰撞的文章，例如标题里的普通 “block”“thread”“weak”；
- W3C XML 完整规范和 Open Data Structures 整本教材；
- 旧 `core-r04-all` 状态和旧 `--scope core` 分片。

## 2. 九组已确认内容

### B1. UIKit 的启动、生命周期、事件与性能

保留 App 启动、Scene/App 生命周期、响应链、target-action、手势识别器状态机、触摸事件、
触摸延迟、视图控制器容器/转场，以及列表和集合视图性能。

不因为路径位于 UIKit 就整目录翻译。外观、菜单、文档浏览器、Apple Pencil 功能示例等
没有命中上述主题的页面继续排除。

### B2. Swift 的并发、原子操作、内存和 Objective-C 互操作

保留严格并发、Actor、Sendable、数据竞争、异步 API、原子操作、指针/所有权，以及
Swift 与 C/Objective-C Runtime 互操作的概念页和指南。

不翻译每种标准库类型自动生成的协议实现页，也不因为页面标题含 Swift 就纳入。

### B3. Foundation 的线程、数据、文件、序列化和进程通信

保留 Thread、Operation、Stream、Socket、文件系统、序列化、任务管理、XPC，以及与
内存、并发、网络和持久化直接相关的成篇资料。

### B4. QuartzCore、Core Graphics、Metal 和图像管线

保留 Core Animation、ProMotion、显示链路、帧率、渲染管线、GPU/纹理内存、CPU/GPU
同步、资源加载、动态库，以及图像加载、缓存和解码。

窄业务特效、单个枚举/常量集合和与学习主题无关的完整示例继续排除。

### B5. Network、Security 和 CryptoKit

保留 TCP、HTTP、TLS、证书、Keychain、加密、网络指标、网络调试、连接诊断、Hardened
Runtime 和启动环境/动态库约束。

### B6. Core Data 与 SwiftData 原理

保留 Core Data stack、上下文并发、持久化存储、历史记录、冲突处理、批处理、模型与迁移，
以及 SwiftData 的并发、存储和迁移原理。

CloudKit 分享界面和纯业务示例不因使用 Core Data 就自动纳入。

### B7. AVFoundation 的启动、异步加载和媒体数据管线

只保留快速启动相机、异步媒体加载、HTTP Live Streaming 和底层媒体数据管线。其余相机
功能、播放 UI、音频业务和效果示例继续排除。

### B8. WWDC 底层主题 Session

保留标题明确命中对象/内存、并发、响应性、渲染性能、编译链接、启动、调试、网络和
持久化原理的未译 session。普通 “What’s new”、产品功能和与 iOS 主线无关的 session
不纳入。

### B9. 高质量作者的底层文章

只从以下已归档来源中选择标题明确命中 B 类主题的文章：

- Mike Ash；
- Cocoa with Love；
- MaskRay；
- Ole Begemann；
- Jesse Squires；
- NSHipster；
- Belkadan；
- Meta Engineering；
- Low Level Bits；
- Emerge Tools；
- Bartosz Ciechanowski；
- Saagar Jha；
- Always Processing；
- worthdoingbadly。

作者在白名单中不代表整站翻译；仍须通过主题规则和误命中排除规则。

## 3. 机器白名单

权威文件：

- `meta/summer_related_b_allowlist.json`：逐篇路径、主题、标题、字符数；
- `tools/summer_related_b.py`：可复现的筛选规则；
- `tools/shard.py --scope summer-related-b`：唯一允许的分片入口。

生成或核验：

```bash
python3 tools/summer_related_b.py write
python3 tools/summer_related_b.py check
python3 tools/shard.py \
  --scope summer-related-b-smoke \
  --shards 1 \
  --prefix summer-b-smoke
python3 tools/shard.py \
  --scope summer-related-b \
  --shards 32 \
  --prefix summer-b-full
python3 tools/deepseek_pipeline.py plan \
  --shard meta/shards/summer-b-full-*.json
```

白名单变化时必须先审查本文件和生成器的 Git diff，再使用新 `run-id`。不得在翻译运行中
临时添加目录或关键词。

## 4. 执行顺序

1. 先用 3 篇覆盖 Apple、WWDC/博客不同结构的文件做冒烟；
2. 冒烟使用低并发和费用上限；
3. 逐篇对照标题、正文、代码、否定/条件、术语和链接；
4. 冒烟通过后，使用同一白名单的新完整 run-id；
5. 完整批次可提高 API 并发，但仍由一个执行器统一控制；
6. 初译和独立审校必须是隔离调用；
7. 每轮只提交明确属于 B 类且通过质量门的译文；
8. 执行者不得自行合并 PR。

推荐参数：

```bash
# 冒烟
python3 tools/deepseek_pipeline.py run \
  --shard meta/shards/summer-b-smoke-*.json \
  --run-id summer-related-b-smoke-r01 \
  --concurrency 3 \
  --review-concurrency 2 \
  --max-cost-usd 0.15

# 冒烟通过后的完整批次
python3 tools/deepseek_pipeline.py run \
  --shard meta/shards/summer-b-full-*.json \
  --run-id summer-related-b-full-r01 \
  --concurrency 16 \
  --review-concurrency 8 \
  --max-cost-usd 8
```

冒烟和完整批次使用不同 run-id，避免把试验参数、分片摘要和正式成本记录混在一起。

## 5. 停止条件

出现以下任一情况时停止派发新初译：

- 402、余额不足或费用上限；
- 持续 429、服务异常或模型不可用；
- 连续结构校验失败；
- 代码块、链接或 front matter 被模型破坏；
- 译文出现系统性漏段、术语漂移或解释性废话；
- 英文原文或白名单摘要发生变化；
- 工作区出现不属于当前批次的并发改动。

机械校验通过不等于语言质量通过。冒烟语言检查不合格时，先修提示词、筛选或模型配置，
不得直接放大并发。

## 6. 2026-07-29 执行记录与断点

冻结白名单共 **407 篇 / 5,625,998 字符**：

- Apple 文档 100 篇；
- WWDC 67 篇；
- 技术博客 240 篇。

冒烟批次先完成 3 篇初译和独立复审。人工检查发现首版曾改动链接显示文字中的
Objective-C selector，并把术语表要求保留英文的 `prewarming` 译掉；在放大全量前已：

1. 修正 3 篇烟雾译文；
2. 强制保留原文行内代码、链接显示文字中的 selector 和 `prewarm` 各词形；
3. 把严格标识符校验接入 DeepSeek 每次候选写入前的质量门；
4. 用修订后的提示词对 3 篇重新独立复审，最终 3 / 3 通过。

完整批次 `summer-related-b-full-r01` 使用 16 路初译和 8 路独立复审。多次余额断点和
复杂文档定点恢复后，用户于 2026-07-29 决定停止继续消耗，最终状态为：

- 完整批次完成 385 篇；
- 加上 3 篇烟雾样本，冻结白名单已有译文 388 / 407；
- 尚余 19 篇复杂技术博客未形成最终成品；停止时 9 篇为失败状态，10 篇停在审校状态，
  逐篇路径与最后原因见
  [`SUMMER_RELATED_B_REMAINING.md`](SUMMER_RELATED_B_REMAINING.md)；
- 恢复器会比较同一文件的三轮候选，只在 token 数量和 Markdown 行结构可确定对应时，
  恢复行内代码、链接目标与图片路径；修复后仍须通过原严格校验，不降低质量门；
- 完整批次累计 1,943 次 API 调用，输入 17,961,601 Token、输出 10,255,812 Token，
  估算 6.8095 美元；
- 当前 388 / 388 篇 B 类成品须统一复验后入库。

不得自动恢复该任务，也不得再用完整分片对剩余 19 篇盲目整批重试。原命令只保留为
历史恢复记录；未来只有用户明确重启时才能执行：

```bash
python3 tools/deepseek_pipeline.py run \
  --shard meta/shards/summer-b-full-*.json \
  --run-id summer-related-b-full-r01 \
  --concurrency 16 \
  --review-concurrency 8 \
  --max-cost-usd 8
```

`.staging/deepseek/summer-related-b-full-r01/state.json` 和候选文件是本地断点事实来源，
受 `.gitignore` 保护，不得提交模型原始输出或 API Key。
