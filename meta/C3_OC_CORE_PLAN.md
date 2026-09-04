# C3：Objective-C 相关存量清零计划

> 状态日期：2026-09-05
> 范围状态：已批准，分批执行中
> 用户裁决：PR #26（C2 批次）暂不合并，后续批次按 [`CONTRIBUTING.md`](../CONTRIBUTING.md)
> 堆叠规则基于前一批分支推进；批 1a–9 全部纳入；工具链/汇编类加做批 9。

## 目标与边界

C2 之后，把仓库中与 Objective-C 直接相关的存量未译文章清零。纳入标准：主题为
Objective-C 运行时、内存管理、消息机制、类簇/集合、C 语言地基（OC 的直接基础）、
Cocoa 编程模式与并发原语。排除标准见文末「明确排除」。

本计划为固定清单。新增篇目必须先改本文件再开工；不得按目录前缀或关键词批量扩张。

## 批次与固定清单

> 存根说明：部分英文文件因抓取时以「上一篇」引用文字入库，frontmatter `title` 为
> `Last time` 类存根。译文 `title` 取正文首行的真实标题（如
> `Friday Q&A 2013-01-25: Let's Build NSObject`）译出；en 文件一律不改。
> 文件名去重结论：`discussion-from-last-week.md` 与
> `friday-q-a-2010-02-26-futures.md` 的 content_hash 相同，为同文重复归档，
> 只翻译后者；`a-post-on-defensive-programming.md`（2009-10-09）与
> `defensive-programming-in-cocoa.md`（2010-08-27）为两篇不同文章，均纳入批 8。

### 批 1a（C3-R01）Let's Build：NSObject 与 NSInvocation · 3 篇 76,849 B

| 英文原文（en 文件名） | 真实标题 | 字节 |
|---|---|---:|
| `blogs/en/mikeash/last-time.md` | Friday Q&A 2013-01-25: Let's Build NSObject | 19,007 |
| `blogs/en/mikeash/last-time-on-friday-q-a.md` | Friday Q&A 2013-03-08: Let's Build NSInvocation, Part I | 23,512 |
| `blogs/en/mikeash/friday-q-a-2013-03-22-let-s-build-nsinvocation-part-ii.md` | Let's Build NSInvocation, Part II | 34,330 |

### 批 1b（C3-R02）Let's Build：通知与集合 · 3 篇 61,617 B

| 英文原文 | 真实标题 | 字节 |
|---|---|---:|
| `blogs/en/mikeash/previously-explored-building-nsnotificationcenter.md` | Friday Q&A 2011-07-08: Let's Build NSNotificationCenter | 18,381 |
| `blogs/en/mikeash/last-time-on-friday-q-a-29b955.md` | Friday Q&A 2012-03-09: Let's Build NSMutableArray | 16,560 |
| `blogs/en/mikeash/last-time-7579f9.md` | Friday Q&A 2012-07-06: Let's Build NSNumber | 26,676 |

### 批 2（C3-R03）内存调试与对象生命周期 · 7 篇 90,882 B

| 英文原文 | 字节 |
|---|---:|
| `blogs/en/mikeash/friday-q-a-2014-11-07-let-s-build-nszombie.md` | 11,679 |
| `blogs/en/mikeash/the-implementation-of-zombies.md` | 11,791 |
| `blogs/en/mikeash/last-time-768338.md`（PLWeakCompatibility Part I） | 16,536 |
| `blogs/en/mikeash/friday-q-a-2010-08-12-implementing-nscoding.md` | 18,477 |
| `blogs/en/mikeash/friday-q-a-2010-06-18-implementing-equality-and-hashing.md` | 14,057 |
| `blogs/en/mikeash/the-how-and-why-of-cocoa-initializers.md` | 8,335 |
| `blogs/en/cocoawithlove/what-does-it-mean-when-you-assign-super-init-to-self-cocoa-with-love.md` | 10,007 |

### 批 3（C3-R04）通知、定时器与运行循环 · 4 篇 约 58KB

`friday-q-a-2010-01-08-nsnotificationqueue.md`、
`friday-q-a-2010-07-02-background-timers.md`、
`cocoawithlove` 的 Five approaches to listening, observing and notifying 与
Design patterns for safe timer usage（执行时以实际文件名核验）。

### 批 4（C3-R05）类簇、集合与无缝桥接 · 6 篇 56,163 B

`friday-q-a-2010-03-12-subclassing-class-clusters.md`（8,842）、
`friday-q-a-2010-01-22-toll-free-bridging-internals.md`（10,179）、
`friday-q-a-2010-05-28-leopard-collection-classes.md`（13,849）、
cocoawithlove 的 OrderedDictionary、Simplifying your code using NSDictionary、
Sorting an NSMutableArray（8,109 / 8,846 / 6,338）。

### 批 5（C3-R06）block、可变参数与格式化 · 5 篇 94,836 B

`friday-q-a-2011-05-06-a-tour-of-mablockclosure.md`（31,704）、
`friday-q-a-2013-05-17-let-s-build-stringwithformat.md`（32,786）、
`friday-q-a-2009-07-17-format-strings-tips-and-tricks.md`（11,313）、
`friday-q-a-2009-08-21-writing-vararg-macros-and-functions.md`（7,551）、
cocoawithlove 的 Variable argument lists in Cocoa（11,482）。

### 批 6a（C3-R07）NSHipster OC 语言概念 · 7 篇 44,322 B

`attribute.md`（10,431）、`c-storage-classes.md`（7,014）、
`object-subscripting.md`（5,978）、`bool-bool-boolean-nscfboolean.md`（5,239）、
`ns_enum-ns_options.md`（5,452）、`instancetype.md`（5,685）、
`nil-nil-null-nsnull.md`（4,523）。

### 批 6b（C3-R08）mikeash C 语言系列 · 4 篇 59,363 B

`friday-q-a-2009-06-26-type-qualifiers-in-c-part-1.md`（9,739）、
`friday-q-a-2009-07-03-type-specifiers-in-c-part-2.md`（10,332）、
`friday-q-a-2009-07-10-type-specifiers-in-c-part-3.md`（12,679）、
`friday-q-a-2012-08-24-things-you-never-wanted-to-know-about-c.md`（26,613）。

### 批 7（C3-R09）并发、Futures 与分布式对象 · 7 篇 102,143 B

`friday-q-a-2009-02-13-operations-based-parallelization.md`（7,703）、
`friday-q-a-2009-04-10-multithreaded-optimization-in-chemicalburn.md`（11,693）、
`friday-q-a-2010-02-26-futures.md`（21,367）、
`friday-q-a-2010-03-05-compound-futures.md`（25,409）、
`friday-q-a-2009-02-20-the-good-and-bad-of-distributed-objects.md`（9,882）、
`friday-q-a-2012-01-20-fork-safety.md`（13,070）、
cocoawithlove 的 Serving an NSManagedObjectContext over an NSConnection（13,019）。

### 批 8（C3-R10）Cocoa 模式与实践杂项 · 13 篇 约 162KB（执行时拆 8a/8b 两个分支）

mikeash：Care and Feeding of Singletons（13,339）、Dangerous Cocoa Calls（9,371）、
Let's Break Cocoa（19,516）、Defensive Programming in Cocoa（19,276）、
Defensive Programming（2009-10-09，12,974）、Model Serialization With Property Lists
（存根 `promised-last-time.md`，25,668）、Proper Use of Asserts（14,726）、
Type-Safe Scalars with Single-Field Structs（10,785）；
cocoawithlove：Singletons, AppDelegates and top-level data（9,364）、
Doing things in Cocoa with "nil"（6,501）、The value of immutable values（7,695）、
The weirdest subclass（12,249）、Supersequent implementation（11,157）。

### 批 9（C3-R11）工具链、汇编与诊断 · 12 篇 约 268KB（执行时拆 9a/9b/9c）

Object File Inspection Tools（27,293）、Disassembling the Assembly Part 1–3
（35,767 / 32,781 / 30,174）、The Hopper Disassembler（10,747）、
gdb Tips and Tricks（30,770）、Introduction to libclang（13,001）、
Mach Exception Handlers（存根 `guest-post-about-mach-exception-handlers.md`，17,884）、
ARM64 and You（存根 `previous-article-on-arm64.md`，19,416）、
Using the Clang Static Analyzer（8,456）、Introduction to Valgrind（10,120）、
Probing Cocoa With PyObjC（11,760）。

## 每批固定流程

1. 核验篇目：en 存在、zh 缺失、不在 `meta/summer_related_b_allowlist.json`；
2. 本文件补充该批完成记录；
3. 多个子代理上下文并行初译，主会话兜底；zh 文件与 en 文件同相对路径（含存根文件名）；
4. 独立审校由未参与初译的上下文完成，修订建议逐条采纳或记录保留理由；
5. 机械校验全套零问题：`validate.py --strict-identifiers`、`test_validate.py`、
   `check_links.py`、`title_aliases.py check`、`indexes.py`、`studyplan.py`；
6. clean-commit 分主题提交；PR 按堆叠规则以上一批分支为 base，注明合并顺序，
   不自行合并；上游合并删除分支后由 GitHub 自动改基到 `main`。

## 明确排除（非 OC 相关，后续另立计划）

- **Swift 专题**：Interesting Swift Features、Secrets of Swift's Speed、
  Swift Name Mangling、Let's Build Swift Notifications、Let's Build Swift.Array、
  When to Use Swift Structs and Classes、Why is Swift's String API So Hard?、
  Swift Struct Storage、Swift Asserts、Swift.Unmanaged、Swift Error Handling
  Implementation、Type-Safe User Defaults、Type Erasure in Swift、Swift.Codable、
  Covariance and Contravariance、The Best of What's New in Swift 等；
- **算法 / 音频 / 图形**：Flood Fill、Fourier Transforms、Optimizing Flood Fill、
  Building the FFT、Obtaining and Interpreting Audio Data、Fluid Simulation、
  Asteroids 系列、MP3 流、tone generator、图像数据处理（存根 `previous.md` 待确认）；
- **硬件 / 系统**：A11 Heterogenous Cores、Secure Enclave、OpenCL、
  Why Registers Are Fast、Practical Floating Point、Random Numbers、
  Signal Handling、Character Encodings、Reachability；
- **AppKit / UI 专题**：Windows and Window Controllers、Custom Slider、
  Custom NSCells、NSOpenGLContext、Goodbye, Nibs（可另立 UI 批）；
- **C 语言边缘短文（可选池，默认不做）**：Compound Literals、C Macro Tips and
  Tricks、C Quiz、Compile-Time Tips、Namespaced Constants、Preprocessor Abuse、
  Hacking C++ From C、Error Returns with CPS、Don't/Use strnstr、
  The Mac Toolbox 系列等；
- **公告 / 生活 / 测验类**：hiring、workshop、NSHipster Quiz、Reader Submissions、
  WWDC 2008、iPhone Development Story、各存根碎片（A Brief Pause 等）。

## 完成记录

- 批 1a（C3-R01）：执行中。
