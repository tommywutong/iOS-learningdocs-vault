---
title: 尽早诊断内存、线程和崩溃问题
framework: xcode
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/diagnosing-memory-thread-and-crash-issues-early
source_url: 'https://developer.apple.com/documentation/xcode/diagnosing-memory-thread-and-crash-issues-early'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/diagnosing-memory-thread-and-crash-issues-early.json'
content_hash: 'sha256:4e95753d9a479dfa'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [调试](debugging.md)

# 尽早诊断内存、线程和崩溃问题

在测试期间，使用 Xcode 的 Sanitizer 工具识别 App 中的运行时崩溃和未定义行为。

## 概述

在开发期间识别潜在问题可以节省后续测试时间，并提高代码的稳定性。Xcode 提供了多种运行时工具，用于识别代码中的潜在问题：

- **Address Sanitizer**——ASan 工具可识别潜在的内存相关损坏问题。
- **Thread Sanitizer**——TSan 工具可检测线程之间的竞态条件（race condition）。
- **Main Thread Checker**——此工具可验证必须运行在主线程（main thread）上的系统 API 是否确实在该线程上运行。
- **Undefined Behavior Sanitizer**——UBSan 工具可检测除零错误、尝试使用未对齐指针访问内存以及其他未定义行为。

这些是基于 LLVM 的工具，会为代码添加特定检查。你可以使用 Xcode 方案编辑器（scheme editor）在构建时启用它们。为你的项目选择正确的方案，然后选择 Product \> Scheme \> Edit Scheme 以显示方案编辑器。选择“运行”或“测试”方案，导航至 Diagnostics 部分，然后选择要运行的 Sanitizer 工具。

> [!note] 注意
> Sanitizer 工具支持所有基于 C 的语言。这些工具也支持 Swift 语言，但 Undefined Behavior Sanitizer 工具除外，它仅支持基于 C 的语言。

在启用 Sanitizer 工具的情况下测试你的 App，以捕获那些难以捕捉的错误。使用全面的单元测试集测试你的代码，并使用额外的集成测试和 UI 测试在运行时执行更多代码。测试计划配置中的 `Address Sanitizer`、`Thread Sanitizer`、`Undefined Behavior Sanitizer` 和 `Main Thread Checker` 值可在测试运行期间启用这些 Sanitizer 工具，请参阅[通过将测试组织为测试计划来改进代码评估](organizing-tests-to-improve-feedback.md)。有关测试代码的更多信息，请参阅[测试](testing.md)。

### 定位代码中的内存损坏问题

不当的内存访问可能会给代码带来意外问题，甚至构成安全威胁。Address Sanitizer 工具可检测不属于已分配内存区域的非法访问尝试。要启用此工具，请从相应方案的 Diagnostics 部分选择 Address Sanitizer。

![方案编辑器的截图，其中选中了 Address Sanitizer 复选框。](../../../attachments/dc57cd0c87d0f51db4549a5b2b4ce9ac/diagnosing-memory-thread-and-crash-issues-early-1@2x.png)

要从命令行启用 ASan，请使用以下标志：

- `-fsanitize=address` (clang)
- `-sanitize=address` (swiftc)
- `-enableAddressSanitizer YES` (xcodebuild)

Address Sanitizer 工具会用自己的实现替换 `malloc(_:)` 和 `free(_:)` 函数。自定义的 `malloc(_:)` 函数会在请求的内存块周围设置特殊的禁区，并报告任何访问这些区域的尝试。`free(_:)` 函数会将已释放的内存块放入一个特殊的隔离队列，并报告任何访问该隔离内存的尝试。

> [!important] 重要
> Address Sanitizer 不检测内存泄漏、尝试访问未初始化内存或整数溢出错误。请使用 Instruments 和其他 Sanitizer 工具来查找其他错误。

对于大多数用例，Address Sanitizer 为代码增加的性能开销在日常开发中是可以接受的。使用 Address Sanitizer 运行代码会使内存使用量增加两到三倍，并导致代码运行速度降低 2 到 5 倍。要改进代码的内存使用情况，请使用 `-O1` 优化级别编译代码。

### 检测 App 线程间的数据争用

当多个线程在没有正确同步的情况下访问同一内存时，就会发生竞态条件。竞态条件在常规测试中很难检测到，因为它们不会稳定复现。然而，修复它们非常重要，因为它们会导致代码行为不可预测，甚至可能引发内存损坏。

要检测竞态条件和其他与线程相关的问题，请从相应构建方案的 Diagnostics 部分启用 Thread Sanitizer 工具。

![方案编辑器的截图，其中选中了 Thread Sanitizer 复选框。](../../../attachments/5f4e9baa5ed4045dd526e1ad00f7f4c7/diagnosing-memory-thread-and-crash-issues-early-2@2x.png)

要从命令行启用 TSan，请使用以下标志：

- `-fsanitize=thread` (clang)
- `-sanitize=thread` (swiftc)
- `-enableThreadSanitizer YES` (xcodebuild)

Thread Sanitizer 工具会在代码中插入诊断信息，以记录每次内存读取或写入操作。这些诊断信息会为每次操作生成时间戳以及其在内存中的位置。然后，该工具会报告任何在同一位置、大约同一时间发生的操作。该工具还会检测其他与线程相关的错误，例如未初始化的互斥锁和线程泄漏。

> [!important] 重要
> 你不能使用 Thread Sanitizer 来诊断在设备上运行的 iOS、iPadOS、tvOS、visionOS 和 watchOS App。Thread Sanitizer 仅用于你的 64 位 macOS App，或诊断在模拟器中运行的 64 位 iOS、iPadOS、tvOS、visionOS 或 watchOS App。

由于 Thread Sanitizer 会在代码中插入诊断信息，因此内存使用量会增加五到十倍。使用这些诊断信息运行代码还会导致 App 速度降低 2 到 20 倍。要改进代码的内存使用情况，请使用 `-O1` 优化级别编译代码。

### 检测后台线程上不正确的 UI 更新

某些系统框架包含只能从 App 主线程调用的 API。此要求适用于大多数 AppKit 和 UIKit 用户界面 API，也适用于一些其他系统 API。从主线程调用这些 API 可以通过序列化相关任务的执行来防止竞态条件。未在主线程上执行这些操作可能导致视觉缺陷、数据损坏或崩溃。

Main Thread Checker 工具可确保所有必须在主线程上执行的调用都能在主线程上执行。要启用此工具，请从相应方案的 Diagnostics 部分选择 Main Thread Checker。

![方案编辑器的截图，其中选中了 Main Thread Checker 复选框。](../../../attachments/04880faceb0dc2a0aa2a6a3445a0013f/diagnosing-memory-thread-and-crash-issues-early-3@2x.png)

Main Thread Checker 工具会动态地将那些必须在主线程上执行的系统方法替换为检查当前线程的变体。该工具仅替换具有已知线程要求的系统 API，而不会替换所有系统 API。由于替换发生在系统框架中，因此 Main Thread Checker 不需要你重新编译 App。

> [!note] 注意
> 由于 Main Thread Checker 不需要你重新编译代码，因此你可以将其直接用于现有的 macOS 二进制文件。将位于 `/Applications/Xcode.app/Contents/Developer/usr/lib/libMainThreadChecker.dylib` 的动态库注入到你的可执行文件中。

要修复 Main Thread Checker 识别出的问题，请将调用分派到 App 的主线程。主线程错误最常见的地方是完成处理程序（completion handler）回调。以下代码通过异步分派到主线程来包装文本标签的修改。

```swift
let task = URLSession.shared.dataTask(with: url) { (data, response, error) in
   if let data = data {
      // 重定向到主线程。
      DispatchQueue.main.async {
         self.label.text = "\(data.count) bytes downloaded"
      }
   }
}
task.resume()

```

Main Thread Checker 对性能的影响微乎其微。该工具会为你的进程增加 1–2% 的 CPU 开销，并使进程启动时间增加不超过 100 毫秒。由于影响极小，Xcode 默认会为你的开发方案启用 Main Thread Checker。

### 检测具有未定义语义的操作

导致未定义行为的代码可能会引发崩溃或产生错误结果。在某些情况下，该代码最初可能根本不会出现任何问题，这使得在条件发生变化后更难诊断问题。Undefined Behavior Sanitizer 工具会检查基于 C 的代码中各种常见的运行时错误，包括：

- 尝试除以零
- 尝试从未对齐的指针加载内存
- 尝试解引用 `NULL` 指针
- 导致整数溢出的数学运算

要启用此工具，请从相应方案的 Diagnostics 部分选择 Undefined Behavior Sanitizer。

![方案编辑器的截图，其中选中了 Undefined Behavior Sanitizer 复选框。](../../../attachments/b962b1adca1dfcad379d29557171cd45/diagnosing-memory-thread-and-crash-issues-early-4@2x.png)

要从命令行启用 UBSan，请在 clang 中添加 `-fsanitize=undefined` 选项，或在 xcodebuild 中添加 `enableUndefinedBehaviorSanitizer YES` 选项。要启用单独的 Sanitizer 检查，请使用以下选项：

| 编译器标志 | UBSan 检查 |
|---|---|
| `-fsanitize=alignment` | [未对齐指针](misaligned-pointer.md) |
| `-fsanitize=bool` | [无效布尔值](invalid-boolean.md) |
| `-fsanitize=bounds` | [数组越界访问](out-of-bounds-array-access.md) |
| `-fsanitize=enum` | [无效枚举值](invalid-enumeration-value.md) |
| `-fsanitize=vptr` | [动态类型违规](dynamic-type-violation.md) |
| `-fsanitize=integer-divide-by-zero` | [除零错误](division-by-zero.md) |
| `-fsanitize=float-divide-by-zero` | [除零错误](division-by-zero.md) |
| `-fsanitize=float-cast-overflow` | [无效浮点转换](invalid-float-cast.md) |
| `-fsanitize=nonnull-attribute` | [非空参数违规](nonnull-argument-violation.md) |
| `-fsanitize=nullability-arg` | [非空参数违规](nonnull-argument-violation.md) |
| `-fsanitize=nullability-assign` | [非空变量赋值违规](nonnull-variable-assignment-violation.md) |
| `-fsanitize=returns-nonnull-attribute` | [非空返回值违规](nonnull-return-value-violation.md) |
| `-fsanitize-nullability-return` | [非空返回值违规](nonnull-return-value-violation.md) |
| `-fsanitize=null` | [空引用创建与空指针解引用](null-reference-creation-and-null-pointer-dereference.md) |
| `-fsanitize=object-size` | [无效对象大小](invalid-object-size.md) |
| `-fsanitize=shift` | [无效移位](invalid-shift.md) |
| `-fsanitize=signed-integer-overflow` | [整数溢出](integer-overflow.md) |
| `-fsanitize=unreachable` | [到达不可达点](reaching-of-unreachable-point.md) |
| `-fsanitize=vla-bound` | [无效变长数组](invalid-variable-length-array.md) |

Undefined Behavior Sanitizer 工具会在编译时将诊断信息插入到代码中。这些检查的性质根据操作类型而不同。例如，在对整数值执行数学运算之前，该工具会添加一个检查来确定该运算是否会导致整数溢出。

Undefined Behavior Sanitizer 对性能的影响很小。该工具平均会给 App 的调试版本增加 20% 的 CPU 开销。

## 主题

### Address Sanitizer

- [使用已释放内存](use-of-deallocated-memory.md) — 检测已释放内存的使用。
- [再次释放已释放内存](deallocation-of-deallocated-memory.md) — 检测释放已释放内存的尝试。
- [释放未分配的内存](deallocation-of-nonallocated-memory.md) — 检测释放未分配内存的尝试。
- [函数返回后使用栈内存](use-of-stack-memory-after-function-return.md) — 检测在声明栈变量的函数返回后访问该变量内存的行为。
- [使用超出作用域的栈内存](use-of-out-of-scope-stack-memory.md) — 检测在变量声明作用域之外访问变量。
- [缓冲区溢出和下溢](overflow-and-underflow-of-buffers.md) — 检测访问缓冲区边界之外的内存。
- [C++ 容器溢出](overflow-of-c-containers.md) — 检测在 C++ 容器边界之外进行访问。

### Thread Sanitizer

- [数据争用（data race）](data-races.md) — 检测跨多个线程对可变状态（mutable state）的未同步访问。
- [Swift 访问争用](swift-access-races.md) — 检测 Swift 中跨多个线程对可变状态的未同步访问。
- [集合和其他 API 上的争用](races-on-collections-and-other-apis.md) — 检测一个线程访问可变对象而另一个线程正在写入该对象的情况。
- [未初始化的互斥锁](uninitialized-mutexes.md) — 检测使用未初始化互斥锁的情况。
- [线程泄漏](thread-leaks.md) — 检测使用后未关闭线程的情况。

### Undefined Behavior Sanitizer

- [未对齐指针](misaligned-pointer.md) — 检测代码访问未对齐指针或创建未对齐引用的情况。
- [无效布尔值](invalid-boolean.md) — 检测程序访问布尔变量且其值不是 true 或 false 的情况。
- [数组越界访问](out-of-bounds-array-access.md) — 检测数组的越界访问。
- [无效枚举值](invalid-enumeration-value.md) — 检测枚举变量包含无效值的情况。
- [到达不可达点](reaching-of-unreachable-point.md) — 检测程序到达不可达点的情况。
- [动态类型违规](dynamic-type-violation.md) — 检测对象具有错误的动态类型的情况。
- [无效浮点转换](invalid-float-cast.md) — 检测向浮点类型、从浮点类型或浮点类型之间的超出范围的转换。
- [除零错误](division-by-zero.md) — 检测除数为零的除法。
- [非空参数违规](nonnull-argument-violation.md) — 检测参数错误地接收空值的情况。
- [非空返回值违规](nonnull-return-value-violation.md) — 检测函数错误地返回 null 的情况。
- [非空变量赋值违规](nonnull-variable-assignment-violation.md) — 检测错误地将 null 赋值给变量的情况。
- [空引用创建与空指针解引用](null-reference-creation-and-null-pointer-dereference.md) — 检测空引用的创建以及空指针的解引用。
- [无效对象大小](invalid-object-size.md) — 检测由于类型大小差异导致的无效指针转换。
- [无效移位](invalid-shift.md) — 检测无效和溢出的移位操作。
- [整数溢出](integer-overflow.md) — 检测算术运算中的溢出。
- [无效变长数组](invalid-variable-length-array.md) — 检测负数的数组边界。

## 另请参阅

### 调试策略

- [诊断正在运行的 App 的外观问题](diagnosing-issues-in-the-appearance-of-your-running-app.md) — 检查正在运行的 App，以调查其显示内容的外观和位置问题。
- [使用 Instruments 分析 HTTP 流量](../foundation/analyzing-http-traffic-with-instruments.md) — 测量 App 基于 HTTP 的网络性能和用量。
- [检测 App 是否连接了可能分析用户的域名](detecting-when-your-app-contacts-domains-that-may-be-profiling-users.md) — 使用 Instruments 评估你的 App 或其第三方 SDK 是否连接到可能分析用户的域名。
