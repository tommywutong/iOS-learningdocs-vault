---
title: 为你的 App 启用增强安全性
framework: updates
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/enabling-enhanced-security-for-your-app
source_url: 'https://developer.apple.com/documentation/xcode/enabling-enhanced-security-for-your-app'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/enabling-enhanced-security-for-your-app.json'
content_hash: 'sha256:2d6fb647bf604715'
translated: true
---

> 导航： [技术](../technologies.md) · [Xcode](../xcode.md) · [构建系统](build-system.md)

# 为你的 App 启用增强安全性

<sub>文章</sub>

检测越界内存访问、已释放内存的使用以及其他潜在漏洞。

## 概述

用户的设备可能包含大量敏感数据，攻击者可能出于恶意目的想要获取这些数据。如果你的 App 存在任何安全漏洞，攻击者可能利用这些漏洞访问或修改你的 App、扩展、轻 App 或设备驱动程序中的数据。

在你的 Xcode 项目中采用“增强安全性”（Enhanced Security）功能，以启用一系列构建设置和 entitlement，旨在缓解你的 App 中的某些常见漏洞。在启用这些设置的情况下审查你的 App 的行为，并修复 Xcode 和系统报告的任何问题。

> [!important] 重要
> “增强安全性”功能启用的安全检查可能会影响那些并未以安全性为首要考虑来设计和构建的 App 的性能和稳定性。请审查你的 App 的威胁模型（threat model），并且仅在其启用的保护措施与你的 App 的安全目标相符时才采用“增强安全性”功能。全面测试你的 App，以确保你已处理所有“增强安全性”缓解措施可能导致 App 崩溃的情况。

针对为 iOS、iPadOS、macOS 和 visionOS 构建的 App 和扩展、iOS 中的轻 App 以及 iPadOS 和 macOS 中的 DriverKit 扩展，均可使用“增强安全性”编译器设置和运行时检查。此外，你可以在 iOS、iPadOS 和 macOS 上创建“增强安全性”辅助扩展（Enhanced Security helper extension），系统会为其提供进一步保护；更多信息，请参阅[创建增强安全性辅助扩展](creating-enhanced-security-helper-extensions.md)。

### 采用“增强安全性”功能

导航到你的 Xcode target 的“签名与功能”（Signing and Capabilities）编辑器，然后点击“添加功能”（Add Capability）按钮。从功能列表中，选择“增强安全性”。将“增强安全性”功能添加到你的 target 后，使用“签名与功能”编辑器中“增强安全性”功能的复选框来采用特定的强化（hardening）特性。此外，点击“启用构建设置”（Enable Build Settings）以将安全相关的构建设置添加到你项目中的所有 target，从而启用某些强化特性。

以下章节描述了构成“增强安全性”的各个 entitlement 和构建设置，以及你可以在代码中采用这些强化特性所采取的步骤。此外，这些章节还描述了如何关闭任何单独的强化设置，以便你在准备代码以支持额外保护措施时执行此操作。

> [!important] 重要
> “签名与功能”编辑器会强制实施各个 entitlement 之间的依赖关系，但如果你直接编辑 `.entitlements` 文件，请确保添加了所有必需的 entitlement。任何以 `com.apple.security.hardened-process.` 开头的 entitlement 都需要 [`com.apple.security.hardened-process`](../bundleresources/entitlements/com.apple.security.hardened-process.md) entitlement 和 [`com.apple.security.hardened-process.enhanced-security-version-string`](../bundleresources/entitlements/com.apple.security.hardened-process.enhanced-security-version-string.md) entitlement。此外，任何以 `com.apple.security.hardened-process.checked-allocations.` 开头的 entitlement 都需要 [`com.apple.security.hardened-process.checked-allocations`](../bundleresources/entitlements/com.apple.security.hardened-process.checked-allocations.md) entitlement。

### 为指针认证（Pointer Authentication）准备你的 App

“增强安全性”功能包括额外的运行时平台限制，当你采用该功能时，Xcode 默认会通过将 `ENABLE_POINTER_AUTHENTICATION` 构建设置设为 `Yes` 来为你的 App 启用这些限制。启用这些额外的运行时平台限制后，Xcode 会为 `arm64e` 架构构建你的 App，并启用_指针认证（pointer authentication）_。

当你启用指针认证时，系统会为你 App 通过分配内存或构造 C++ 对象而创建的指针生成签名元数据。然后，当你的 App 访问这些指针所指向的内存时，系统会验证签名是否未更改。如果指针的签名无效，系统会遇到异常并使你的 App 崩溃。这样做有助于防止攻击者覆写你 App 中的内存以破坏其控制流。

要采用指针认证，请使用 `__ptrauth` 类型限定符（type qualifier）来指示编译器为你代码中存储数据和函数指针的变量生成指针认证保护。

当变量使用指针认证时，如果你在你的代码中使用原始指针覆写其值，或者将其值复制到使用不同指针认证模式的另一个变量，系统会抛出错误。如果你的 App 执行了上述任一操作，系统会遇到异常并使你的 App 崩溃。相反，请在存储指针之前对其进行签名，并在必要时重新签名以用于不同用途。更多信息，请参阅[使用指针认证改善控制流完整性](../apple-silicon/improving-control-flow-integrity-with-pointer-authentication.md)。

如果你需要为你的 target 关闭指针认证，请取消选中“签名与功能”编辑器中的“认证指针”（Authenticate Pointers）复选框，或将 `ENABLE_POINTER_AUTHENTICATION` 构建设置设为 `No`。

### 采用类型化分配器（Typed Allocator）支持

当你采用“增强安全性”功能时，Xcode 会配置构建设置以在 C 和 C++ 代码中启用编译器的类型化分配器（typed allocator）。有关类型化分配器以及如果你使用自定义内存分配器包装函数需要在代码中进行的更改的更多信息，请参阅[采用类型感知的内存分配](adopting-type-aware-memory-allocation.md)。

要为你的 target 关闭类型化分配器支持，请取消选中“签名与功能”编辑器中的“启用类型化分配器”（Enable Typed Allocators）复选框，或将 `CLANG_ENABLE_C_TYPED_ALLOCATOR_SUPPORT` 构建设置设为 `No`（针对 C 代码），并将 `CLANG_ENABLE_CPLUSPLUS_TYPED_ALLOCATOR_SUPPORT` 构建设置设为 `No`（针对 C++ 代码）。

### 采用内存完整性强制（Memory Integrity Enforcement）

当你启用硬件内存标记（hardware memory tagging）时，每个新的内存分配以及指向该内存的任何指针都包含一个称为_标签（tag）_的嵌入值。通过指针访问内存需要指针的标签与分配的标签匹配。如果标签不匹配——例如，由于释放后使用（use-after-free）错误或越界访问——App 会崩溃，而不是执行不安全的访问。

要启用内存标记，请导航到你的 Xcode target 的“签名与功能”编辑器。启用“增强安全性”功能，然后在“内存安全”（Memory Safety）下，点击“启用硬件内存标记”（Enable Hardware Memory Tagging）。Xcode 会将 [`com.apple.security.hardened-process.checked-allocations`](../bundleresources/entitlements/com.apple.security.hardened-process.checked-allocations.md) entitlement 添加到你的 App。

要在调试时启用额外的诊断信息，请导航到方案编辑器（Scheme Editor）并选择“运行”（Run）操作，然后选择“诊断”（Diagnostics）面板并启用“硬件内存标记”。

当你在 Xcode 中启用内存标记时，它还会添加 [`com.apple.security.hardened-process.checked-allocations.soft-mode`](../bundleresources/entitlements/com.apple.security.hardened-process.checked-allocations.soft-mode.md) entitlement。此 entitlement 使硬件内存标记以_软模式（soft mode）_运行，在此模式下，如果指针的标签与内存分配的标签不匹配，系统会产生模拟崩溃而不是终止 App。你可以查看来自模拟崩溃的报告，以帮助你发现内存问题，并帮助验证你的 App 没有内存损坏错误，这些错误在软模式禁用时会导致崩溃。在确信 App 的稳定性后，禁用软模式以保护你的用户。要禁用软模式，请导航到你的 Xcode target 的“签名与功能”编辑器，然后在“内存安全”下，取消选中“为内存标记启用软模式”（Enable Soft Mode for Memory Tagging）。

你还可以启用 [`com.apple.security.hardened-process.checked-allocations.enable-pure-data`](../bundleresources/entitlements/com.apple.security.hardened-process.checked-allocations.enable-pure-data.md) 和 [`com.apple.security.hardened-process.checked-allocations.no-tagged-receive`](../bundleresources/entitlements/com.apple.security.hardened-process.checked-allocations.no-tagged-receive.md) entitlement。

> [!note] 注意
> 在不支持硬件内存标记的设备上，此设置无效。支持的设备包括搭载 A19 芯片或更新芯片的 iPhone 和 iPad，以及搭载 M5 芯片或更新芯片的 Mac 和 Apple Vision Pro。

### 将栈变量初始化为零

当你为你的 target 启用“增强安全性”功能时，Xcode 会将 `CLANG_ENABLE_STACK_ZERO_INIT` 构建设置设为 `Yes`。此构建设置使编译器将代码中的自动变量（automatic variable）初始化为零。这样做有助于防止特定类型的释放后使用漏洞，因为你的 App 在将栈内存重新用于其他变量之前，会将其中的先前值清零。

如果你需要为你的 target 关闭栈变量的零初始化，请将 `CLANG_ENABLE_STACK_ZERO_INIT` 构建设置设为 `No`。

### 处理安全相关的编译器警告

当你为你的 target 启用“增强安全性”功能时，Xcode 会配置一些有助于识别潜在不安全代码的编译器警告。这些警告包括：

- **`-Wshadow`**——当变量声明_遮蔽（shadows）_另一个变量或类型别名时，编译器会发出警告；也就是说，该变量与另一个实体同名，并且当前作用域中对该变量名的使用会引用新声明的变量，而本意可能是使用原始实体。通过将 `GCC_WARN_SHADOW` 构建设置设为 `No` 来关闭此警告。
- **`-Wempty-body`**——当控制流语句（例如 `for` 循环或 `if` 语句）的主体不包含任何代码时，编译器会发出警告。通过将 `CLANG_WARN_EMPTY_BODY` 构建设置设为 `No` 来关闭此警告。

Xcode 还会将 `ENABLE_SECURITY_COMPILER_WARNINGS` target 构建设置设为 `Yes`。这会打开一系列安全相关的编译器警告，当你构建 target 时，Xcode 会在问题导航器（Issues navigator）中报告这些警告。这些额外的警告包括：

- **`-Wbuiltin-memcpy-chk-size`**——当 `memcpy` 操作中的目标缓冲区小于你复制到其中的字节数时，编译器会发出警告。
- **`-Wformat-nonliteral`**——当类似 `printf` 的函数的格式字符串不是字符串字面量时，编译器会发出警告。
- **`-Warray-bounds`**——当数组索引位于数组开头之前或超过数组末尾时，编译器会发出警告；或者你传递给函数的数组参数小于函数期望的最小大小时，编译器会发出警告。
- **`-Warray-bounds-pointer-arithmetic`**——当计算出的指针值导致指针位于数组开头之前或超过数组末尾时，编译器会发出警告。
- **`-Wsuspicious-memaccess`**——当内存操作作用于动态类并可能操作其 `vtable` 指针时；`memset` 的参数被调换时；内存操作移动或复制不可平凡复制（trivially copyable）的对象时；或者请求的内存操作大小为 `0`，或对源指针调用 `sizeof` 的结果时，编译器会发出警告。
- **`-Wsizeof-array-div`**——当 `sizeof` 计算由于使用了不正确的类型而未正确计算数组中的元素数量时，编译器会发出警告。
- **`-Wsizeof-pointer-div`**——当 `sizeof` 计算结果为指针的大小，而不是它所引用的数组的大小时，编译器会发出警告。
- **`-Wreturn-stack-address`**——当你的代码向调用函数返回栈上的地址（例如，局部变量的地址）时，编译器会发出警告。

如果你需要关闭“增强安全性”为你的 target 配置的额外编译器警告，请将 `ENABLE_SECURITY_COMPILER_WARNINGS` 构建设置设为 `No`。

### 采用 C++ 标准库强化（Hardening）和编译器边界检查

当你为你的 target 启用“增强安全性”功能时，Xcode 会将 `ENABLE_CPLUSPLUS_BOUNDS_SAFE_BUFFERS` target 构建设置设为 `YES`。这会启用 C++ 标准库中的一系列安全检查。具体来说，它启用了_快速（fast）_强化模式。

在快速模式下，C++ 标准库会在你的使用标准库容器类型的代码中执行以下断言检查：

- **有效的元素访问**——标准库会检查，当你的代码访问集合元素（包括包含在单元素集合类型 `std::function` 和 `std::optional` 中的元素）时，这些元素确实存在于集合中。
- **有效的输入范围**——标准库会检查你传递给标准算法函数的范围是有效的，并且如果你使用 `begin` 迭代器和哨兵（sentinel）定义了一个范围，则库可以从迭代器到达哨兵。

标准库会在常数时间内计算这些检查。如果强化断言失败（即，如果检查结果为 `false`），系统会遇到异常并使你的 App 崩溃。

要为项目中的单个文件更改 C++ 标准库强化模式，请使用以下值之一定义 `_LIBCPP_HARDENING_MODE` 宏：

- **`_LIBCPP_HARDENING_MODE_NONE`**——无强化
- **`_LIBCPP_HARDENING_MODE_FAST`**——快速模式
- **`_LIBCPP_HARDENING_MODE_EXTENSIVE`**——广泛强化
- **`_LIBCPP_HARDENING_MODE_DEBUG`**——所有强化检查

如果你在代码中定义该宏，则需要将定义放置在文件的开头，在任何标准库头文件包含之前。

此外，将 `ENABLE_CPLUSPLUS_BOUNDS_SAFE_BUFFERS` 设为 `Yes` 会为 C++ 中不安全的缓冲区使用添加编译器警告，并将这些警告视为错误。如果 C++ 编译器检测到你的代码执行以下操作，它会遇到错误：

- 对原始指针进行数组索引、执行指针算术或使用不安全的 C 标准库函数
- 在指向对象列表的智能指针上调用 `operator[]()`
- 使用两个参数（指针和大小）构造函数构造 `std::span` 对象

要为你的 target 关闭 C++ 标准库强化和编译器边界检查，请将 `ENABLE_CPLUSPLUS_BOUNDS_SAFE_BUFFERS` 构建设置设为 `No`。

有关 C++ 标准库强化的更多信息，请参阅 LLVM 文档中的[强化模式](https://libcxx.llvm.org/Hardening.html)。

### 采用额外的运行时限制

当你为你的 target 启用“增强安全性”功能时，Xcode 会将 [`com.apple.security.hardened-process.platform-restrictions-string`](../bundleresources/entitlements/com.apple.security.hardened-process.platform-restrictions-string.md) entitlement 添加到你的 App。此 entitlement 指示系统对你 App 或扩展加载的动态库以及你的 App 或扩展从其他进程接收的 Mach 消息执行额外检查。

如果你使用 [XPC](../xpc.md) 进行进程间通信（IPC）并且不使用 Mach IPC 陷阱，或者在你的 App 或扩展中没有显式的 IPC 机制，启用额外的运行时限制将开启不太可能需要你进行任何代码更改的保护措施。

在使用 Mach IPC 陷阱的 App 和扩展中，额外的运行时限制会将潜在的不安全情况转化为崩溃，以避免攻击者通过 Mach 端口获得对你的进程的特权访问。有关解释这些崩溃以及为避免不安全使用 Mach 消息传递 API 而需要对代码进行的更改的信息，请参阅[遵守 Mach IPC 安全限制](conforming-to-mach-ipc-security-restrictions.md)。

要为你的 target 关闭额外的运行时限制，请取消选中“签名与功能”编辑器中的“启用额外的运行时平台限制”（Enable Additional Runtime Platform Restrictions）复选框。

### 为内部平台状态采用只读内存

当你为你的 target 启用“增强安全性”功能时，Xcode 会将 [`com.apple.security.hardened-process.dyld-ro`](../bundleresources/entitlements/com.apple.security.hardened-process.dyld-ro.md) entitlement 添加到你的 App。此 entitlement 指示系统将你进程中平台用于其内部状态的内存区域标记为只读。

在大多数情况下，此额外保护不需要你进行任何更改。如果你的 App 修改了受保护区域中的数据——例如，它修改了 `const` 数据段的值——则在你采用此 entitlement 时，系统会使你的 App 崩溃。要修复此崩溃，请删除修改只读内存区域的代码。

如果你需要为动态加载器关闭只读内存，请取消选中“签名与功能”编辑器中的“启用只读平台内存”（Enable Read-Only Platform Memory）复选框。

### 采用守卫对象（Guard Objects）

守卫对象通过将已释放的内存区域替换为不可访问的守卫区域来防御释放后使用漏洞。当你的 App 访问这些区域之一时，它会崩溃，以防止已释放的内存被利用。当你将 [`com.apple.security.hardened-process.enhanced-security-version-string`](../bundleresources/entitlements/com.apple.security.hardened-process.enhanced-security-version-string.md) 设置为 `2` 或更高时，此保护会自动激活。如果你未设置此 entitlement，系统会自动应用最新的“增强安全性”版本。当你的 App 释放虚拟内存映射和堆分配（统称为_对象（objects）_）时，内核和用户空间内存分配器可以用不可访问的守卫区域替换它们。守卫放置是动态的：系统将相似大小的对象分组并管理其生命周期，随着你的 App 分配和释放内存而移动守卫位置。

> [!important] 重要
> 守卫对象可能会导致内存使用增加或执行速度下降，具体取决于你的 App 的工作负载。在采用“增强安全性”版本 `2` 后，请对你的 App 进行性能分析以衡量其影响。

如果守卫对象的内存或性能影响过大，你可以为你的 target 关闭守卫对象。要关闭守卫对象，请手动将 [`com.apple.security.hardened-process.no-guard-objects`](../bundleresources/entitlements/com.apple.security.hardened-process.no-guard-objects.md) entitlement 添加到你的 target。然后更新你的配置文件（provisioning profile）。更多信息，请参阅[编辑、下载或删除配置文件](https://developer.apple.com/help/account/provisioning-profiles/edit-download-or-delete-profiles)。

### 在 C 中采用边界检查

可选地，为你的 target 启用边界检查，以补充“增强安全性”中的安全特性。

`ENABLE_C_BOUNDS_SAFETY` 构建设置会在 Xcode 编译 C 源文件时向编译器调用添加 `-fbounds-safety` 标志。这是 C 编程语言的一个扩展，它通过强制实施边界安全来防止越界内存访问。

编译器假设你代码中使用 `-fbounds-safety` 标志编译的每个指针都指向单个对象，并且如果你尝试使用该指针执行指针算术，或使用下标基于该指针访问数组元素，它会发出错误。要指示指针标识一组指定大小的对象，请使用以下注解之一：

- **`__counted_by(N)`**——指针定位长度为 `N` 的数组中的第一个元素。参数 `N` 可以是常量、算术表达式或变量名。
- **`__sized_by(N)`**——指针是大小为 `N` 字节的内存缓冲区的起始位置。参数 `N` 可以是常量、算术表达式或变量名。
- **`__ended_by(P)`**——指针位于上界为 `P` 的内存区域中。参数 `P` 是内存区域中最后一个元素之后的第一个指针。

如果指针可能为 `NULL`，请在注解名称后添加 `_or_null` 后缀；例如，`__counted_by_or_null(N)`。

要指示指针标识一组具有特定哨兵值表示结尾的对象——例如，空终止字符串——请使用以下注解之一：

- **`__null_terminated`**——哨兵值为 `0`。
- **`__terminated_by(T)`**——哨兵值为 `T`。

要指示指针引用一个你尚未审计其边界安全的值，请添加 `__unsafe_indexable` 注解。

更多信息，请参阅 LLVM 网站上的 [`-fbounds-safety`：为 C 强制实施边界安全](https://clang.llvm.org/docs/BoundsSafety.html)。

要在 C 中关闭边界检查，请将 `ENABLE_C_BOUNDS_SAFETY` 构建设置的值设为 `No`。

## 另请参阅

### 安全与隐私

- [验证你的 XCFrameworks 的来源](verifying-the-origin-of-your-xcframeworks.md)——了解谁签署了框架，并在其发生变化时采取行动。
- [创建增强安全性辅助扩展](creating-enhanced-security-helper-extensions.md)——减少攻击者通过扩展针对你 App 的机会。
- [采用类型感知的内存分配](adopting-type-aware-memory-allocation.md)——减少在代码中将指针视为数据的机会。
- [遵守 Mach IPC 安全限制](conforming-to-mach-ipc-security-restrictions.md)——避免与 Mach 消息相关的崩溃和潜在不安全情况。
