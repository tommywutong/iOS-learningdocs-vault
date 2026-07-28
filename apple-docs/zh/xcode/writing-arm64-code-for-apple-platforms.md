---
title: 为 Apple 平台编写 ARM64 代码
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/writing-arm64-code-for-apple-platforms
source_url: 'https://developer.apple.com/documentation/xcode/writing-arm64-code-for-apple-platforms'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/writing-arm64-code-for-apple-platforms.json'
content_hash: 'sha256:9933b85afe4887c3'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [应用二进制接口](application-binary-interfaces.md)

# 为 Apple 平台编写 ARM64 代码

<sub>文章</sub>

创建符合 Apple 平台所支持的应用二进制接口（application binary interface，ABI）的 64 位 ARM 汇编语言指令。

## 概述

ARM 架构定义了有关如何调用函数、管理栈和执行其他操作的规则。如果部分代码包含 ARM 汇编指令，就必须遵守这些规则，代码才能与编译器生成的代码正确互操作。同样，如果你要编写编译器，生成的机器指令也必须遵守这些规则。如果不遵守，代码可能会出现意外行为，甚至崩溃。

Apple 平台在少数特定方面与标准 64 位 ARM 架构有所不同。除这些细微差异外，iOS、tvOS 和 macOS 均遵循 64 位 ARM 规范的其余部分。有关 ARM64 规范的信息，包括《ARM 64 位架构过程调用标准》（AArch64），请访问 [https://developer.arm.com](https://developer.arm.com)。

### 遵循特定 CPU 寄存器的用途

ARM 标准将某些决定交由平台设计者作出。Apple 平台采用以下约定：

- 平台保留寄存器 `x18`。不要使用此寄存器。
- 帧指针寄存器（`x29`）必须始终指向有效的帧记录。某些函数（例如叶函数或尾调用）可以选择不在此列表中创建条目。因此，即使没有调试信息，栈跟踪也始终具有意义。

### 正确处理数据类型和数据对齐

C 语言的某些基本类型采用略有不同的实现：

- `wchar_t` 类型为 32 位有符号类型。
- `char` 类型为有符号类型。
- `long` 类型为 64 位。
- `__fp16` 类型在适用时使用 IEEE754-2008 格式。
- `long` `double` 类型是双精度 IEEE754 二进制浮点类型，因此与 `double` 类型相同。这与标准规范不同；在标准规范中，`long` `double` 是四倍精度 IEEE754 二进制浮点类型。

下表列出了 Apple 平台上的整数数据类型、大小和自然对齐方式。

| 数据类型 | 大小（字节） | 自然对齐（字节） |
|---|---|---|
| `BOOL`, `bool` | 1 | 1 |
| `char` | 1 | 1 |
| `short` | 2 | 2 |
| `int` | 4 | 4 |
| `long` | 8 | 8 |
| `long long` | 8 | 8 |
| 指针 | 8 | 8 |
| `size_t` | 8 | 8 |
| `NSInteger` | 8 | 8 |
| `CFIndex` | 8 | 8 |
| `fpos_t` | 8 | 8 |
| `off_t` | 8 | 8 |

### 遵循栈的红区约定

ARM64 红区（red zone）由紧邻栈指针下方的 128 字节组成。Apple 平台在发生异常时不会修改这些字节。用户模式程序可以认为栈指针下方的字节不会意外发生变化，并可将这块空间用于局部变量。

> [!note] 注意
> 如果函数调用自身，调用方必须假定被调用方会修改其红区的内容。因此，调用方必须创建正确的栈帧。

### 正确向函数传递实参

Apple 平台上的栈指针遵循 ARM64 标准 ABI，并要求按 16 字节对齐。向函数传递实参时，Apple 平台在以下方面与 ARM64 标准 ABI 不同：

- 函数实参可以占用大小不是 8 字节倍数的栈槽。如果基于栈的实参总字节数不是 8 的倍数，请在栈上插入填充，以满足 8 字节对齐要求。
- 在整数寄存器中传递要求 16 字节对齐的实参时，Apple 平台允许该实参从编号为奇数的 `xN` 寄存器开始。标准 ABI 要求它从编号为偶数的 `xN` 寄存器开始。
- 对于任何不足 32 位的实参，函数调用方负责对其执行符号扩展或零扩展。标准 ABI 则要求被调用方对这些实参执行符号扩展或零扩展。
- 函数可以忽略包含空结构体类型的形参。此行为适用于 C 中的 GNU 扩展，也适用于语言允许这种用法时的 C++。AArch64 文档没有说明将空结构体用作形参的问题，但 Apple 的实现选择了这种方式。

以下示例说明 Apple 平台如何指定大小不是 8 字节倍数的基于栈的实参。进入函数时，`s0` 占据当前栈指针（`sp`）处的一个字节，`s1` 占据 `sp+1` 处的一个字节。编译器仍会在 `s1` 后添加填充，以满足栈的 16 字节对齐要求。

```swift
void two_stack_args(char w0, char w1, char w2, char w3, char w4, char w5, char w6, char w7, char s0, char s1) {}
```

以下示例展示了一个第二个实参要求按 16 字节对齐的函数。标准 ABI 要求将第二个实参放入 `x2` 和 `x3` 寄存器，而 Apple 平台允许将其放入 `x1` 和 `x2` 寄存器。

```swift
void large_type(int x0, __int128 x1_x2) {} 
```

### 更新向可变参数函数传递实参的代码

对于形参数量可变的函数，Apple 会照常初始化相关寄存器（阶段 A），并确定如何填充或扩展实参（阶段 B）。在向寄存器和栈槽分配实参时，Apple 平台针对每个可变实参采用以下规则：

1. 将下一个 SIMD 和浮点寄存器编号（Next SIMD and Floating-point Register Number，NSRN）向上舍入到下一个 8 字节倍数。
2. 将可变实参分配到数量合适的 8 字节栈槽中。

由于这些更改，`va_list` 类型是 `char*` 的别名，而不是通用过程调用标准中的结构体类型。编译 C++ 代码时，此类型也不位于 `std` 命名空间中。

> [!note] 注意
> C 语言要求在调用前提升小于 int 的实参。除此之外，Apple 平台 ABI 不会向栈中添加未使用的字节。

### 处理 C++ 差异

通用 ARM64 C++ ABI 仿照许多类 UNIX 系统使用的 Itanium C++ ABI。Apple 的 C++ ABI 与该 ABI 存在以下差异：

- `va_list` 类型的修饰名称为 `Pc`，而不是 `St9__va_list`。产生此差异是因为 `va_list` 是 `char *` 的别名，并使用相同的名称修饰约定。
- NEON 向量类型的修饰名称与其 32 位 ARM 对应类型相同，而不是使用 64 位方案。例如，Apple 平台使用 `17__simd128_int32_t`，而不是通用的 `11_int32x4_t`。
- 向函数传递形参时，Apple 平台会忽略空结构体，除非这些结构体具有非平凡析构函数或拷贝构造函数。传递此类非平凡结构体时，以通用方式将它们视为具有一个字节成员的聚合体。
- ABI 要求完整对象（C1）构造函数和基对象（C2）构造函数向调用方返回 this。同样，完整对象（D1）析构函数和基对象（D2）析构函数也返回 this。此行为与 ARM 32 位 C++ ABI 一致。
- ABI 为数组 cookie 提供由两个 `size_t` 字组成的固定布局，并且没有额外的对齐要求。此行为与 ARM 32 位 C++ ABI 一致。
- 对象初始化保护变量名义上是 `uint64_t`，而不是 `int64_t`。此行为会影响函数 `__cxa_guard_acquire`、`__cxa_guard_release` 和 `__cxa_guard_abort` 的原型。
- 声明为 `extern “C”` 的函数指针不能与声明为 `extern “c++”` 的函数互换。这与 ARM64 ABI 不同，后者允许互换这些函数。

有关通用 ARM64 C++ ABI 的更多信息，请参阅 developer.arm.com 上的《ARM 64 位架构 C++ 应用二进制接口标准》。

### 为恒定时间加密操作启用 DIT

ARM64 上的某些指令（包括但不限于 [Arm Architecture Registers for Future Architecture Technologies](https://developer.arm.com/documentation/ddi0601/2020-12/AArch64-Registers/DIT--Data-Independent-Timing) 中所述的指令）可能会根据其操作的数据值而花费不同的运行时间。设备上运行的恶意代码可能会利用此属性推断 CPU 所处理数据的相关信息，例如加密密钥或其他敏感数据。

Apple 芯片提供与数据无关的计时（data-independent timing，DIT），使处理器能以恒定时长完成某些指令。启用 DIT 后，无论输入数据如何，处理器都会采用更长的最坏情况时长来完成指令。如果你编写的软件专门用于避免泄露内部信息并以恒定时间运行代码，请在加载加密密钥材料、执行加密操作或处理敏感数据之前启用 DIT，并将代码限制为支持 DIT 的指令，从而确保特定指令的执行时间不会泄露有关所处理数据的信息。

请在加密例程等专门场景中启用 DIT。由于 DIT 可能会减慢代码运行速度，因此仅当你编写的软件需要针对敏感数据以恒定时间运行并避免泄露敏感信息时才启用它。操作系统中实现并通过 Apple CryptoKit 等 API 提供的 Apple 加密例程会在内部启用 DIT。

> [!important] 重要
> 虽然 DIT 能确保某些指令的执行时间不会泄露数据相关信息，但你仍需采用其他编程实践，防止处理器微架构状态的其他变化向攻击者提供与秘密值有关的信号。例如，应避免根据秘密数据的值进行条件分支或选择内存访问位置。

在 iOS 18.2、iPadOS 18.2、macOS 15.2、tvOS 18.2、watchOS 11.2 和 visionOS 2.2 及更高版本中，有两个新函数调用可用于控制并优化 Apple 设备上的 DIT。这些函数在所有设备上均可用，无论设备是否支持 DIT；但它们只会在受支持的设备上开启 DIT。

要保护一组加密操作，请无条件调用 `timingsafe_enable_if_supported` 来开启 DIT。在内部，该函数会采用适合设备 CPU 的安全措施来限制推测计算，例如推测屏障（speculation barrier，SB）。该 API 函数经过优化，因此设备会自动采用最高效的安全措施，你也无需进行若干编译时和运行时检查。如果不支持计时安全功能，系统会忽略它们，函数不会产生任何效果。

该函数会返回一个用于恢复先前状态的不透明令牌。请存储返回的令牌，并在计时敏感操作完成后，将令牌传递给 `timingsafe_restore_if_supported`，以将 CPU 恢复到先前状态。

如果调用 `timingsafe_enable_if_supported` 之前 DIT 已开启，那么调用 `timingsafe_restore_if_supported` 后它仍会保持开启；否则，DIT 会被关闭。

若要在执行恒定时间加密操作前开启计时安全模式，并在随后恢复 CPU 的先前状态，请使用以下代码：

```c
#include <timingsafe.h>

int cryptographic_routine() {
    timingsafe_token_t restore_token = timingsafe_enable_if_supported();
    // 在此执行恒定时间加密操作。
    timingsafe_restore_if_supported(restore_token);
    return 0;
}
```

或者，若要在这些 API 不可用的旧版 SDK 或平台上开启 DIT，你需要检查 CPU 是否定义并支持 DIT，然后使用底层内核和 CPU 寄存器。若要测试 API 是否可用，请使用编译器的 [__builtin_available](https://clang.llvm.org/docs/LanguageExtensions.html#objective-c-available) 指令。

若要确定设备的 CPU 是否支持 DIT，请使用 [sysctlbyname](../kernel/1387446-sysctlbyname.md) 测试 `hw.optional.arm.FEAT_DIT` 系统控制项：

```c
#include <sys/sysctl.h>
#include <stdbool.h>

bool is_DIT_supported(void) {
    static int has_DIT = -1;
    if (has_DIT == -1) {
        size_t has_DIT_size = sizeof(has_DIT);
        if (sysctlbyname("hw.optional.arm.FEAT_DIT", &has_DIT, &has_DIT_size, NULL, 0) == -1) {
            has_DIT = 0;
        }
    }
    return has_DIT;
}
```

如果 DIT 可用，此函数返回 `1`；否则返回 `0`。

若要检查当前线程是否已开启 DIT，请测试处理器状态寄存器的 `dit` 位（第 24 位）。`dit` 位仅在某些设备上定义，你可以为函数设置属性，以避免在针对不受支持的设备进行编译时出现错误：

```c
#ifdef __arm64__
__attribute__((target("dit")))
bool get_DIT_enabled(void) {
    return (__builtin_arm_rsr64("dit") >> 24) & 1;
}
#endif
```

将 `dit` 处理器状态寄存器的值设为 `1`，即可为当前线程开启 DIT。为确保后续指令的执行时间反映更新后的 DIT 处理器状态，请在开启 DIT 后添加推测屏障。使用 `sb` 指令添加推测屏障：

```c
#ifdef __arm64__
__attribute__((target("sb")))
void inst_dit_speculation_barrier(void) {
  __asm__ __volatile__("sb" ::: "memory");
}
#endif
```

若要在敏感操作后恢复 DIT 状态，请在开启 DIT 前读取并返回其当前状态：

```c
#ifdef __arm64__
__attribute__((target("dit")))
bool set_DIT_enabled(void) {
    bool was_DIT_enabled = get_DIT_enabled();
    __asm__ __volatile__("msr dit, #1");
    inst_dit_speculation_barrier();
    return was_DIT_enabled;
}
#endif
```

若要为当前线程关闭 DIT，请将 `dit` 处理器状态寄存器的值设为 `0`。为了避免在嵌套调用中意外关闭 DIT，请将 DIT 恢复为先前的值，而不是无条件将其关闭。由于可以在不同线程上分别开启或关闭 DIT，因此请将初始值存储在线程局部存储中。如果开启 DIT 前记录的 DIT 值为 `0`，请将 DIT 值设为 `0`：

```c
#ifdef __arm64__
__attribute__((target("dit")))
void restore_DIT(bool was_DIT_enabled) {
    if (was_DIT_enabled == false) {
        __asm__ __volatile__("msr dit, #0");
    }
}
#endif
```

若要测试推测屏障的可用性，请使用与上述 DIT 类似的机制：

```c
bool is_SB_supported(void) {
    static int has_SB = -1;
    if (has_SB == -1) {
        size_t has_SB_size = sizeof(has_SB);
        if (sysctlbyname("hw.optional.arm.FEAT_SB", &has_SB, &has_SB_size, NULL, 0) == -1) {
            has_SB = 0;
        }
    }
    return has_SB;
}
```

不支持推测屏障时，请使用：

```c
#ifdef __arm64__
void inst_dit_speculation_barrier_unsupported(void) {
  __asm__ __volatile__ ("dsb nsh" ::: "memory");
  __asm__ __volatile__ ("isb sy" ::: "memory");
}
#endif
```

若要创建在所有设备上都可用的函数（无论设备是否支持 DIT 和推测屏障），请定义函数指针。如果设备支持 DIT，请将函数指针设为测试和更改处理器状态寄存器的函数。如果不支持 DIT，请将函数指针设为不执行任何操作的函数，并对推测屏障采用相同模式：

```c
bool(* set_DIT_enabled_if_supported)(void);
void(* restore_DIT_if_supported)(bool);
bool(* get_DIT_enabled_if_supported)(void);
void(* inst_dit_speculation_barrier_if_supported)(void);

bool set_DIT_enabled(void);
void restore_DIT(bool);
bool get_DIT_enabled(void);
void inst_dit_speculation_barrier(void);

bool set_DIT_enabled_unsupported(void);
void restore_DIT_unsupported(__unused bool was_DIT_enabled);
bool get_DIT_enabled_unsupported(void);
void inst_dit_speculation_barrier_unsupported(void);

void init_DIT_control(void);

#ifdef __arm64__
__attribute__((target("dit")))
bool set_DIT_enabled(void) {
    bool was_DIT_enabled = get_DIT_enabled();
    __asm__ __volatile__("msr dit, #1");
    inst_dit_speculation_barrier_if_supported();
    return was_DIT_enabled;
}
#endif

bool get_DIT_enabled_unsupported(void) {
    return false;
}

bool set_DIT_enabled_unsupported(void) {
    return false;
}

void restore_DIT_unsupported(__unused bool was_DIT_enabled) {
    return;
}

void init_DIT_control(void) {
#ifdef __arm64__
    if (is_SB_supported()) {
        inst_dit_speculation_barrier_if_supported = inst_dit_speculation_barrier; 
    }
    else {
        inst_dit_speculation_barrier_if_supported = inst_dit_speculation_barrier_unsupported;
    }

    if (is_DIT_supported()) {
        set_DIT_enabled_if_supported = set_DIT_enabled;
        restore_DIT_if_supported = restore_DIT;
        get_DIT_enabled_if_supported = get_DIT_enabled;
    } else
#endif
    {
        set_DIT_enabled_if_supported = set_DIT_enabled_unsupported;
        restore_DIT_if_supported = restore_DIT_unsupported;
        get_DIT_enabled_if_supported = get_DIT_enabled_unsupported;
    }
#ifdef __arm64__
    inst_dit_speculation_barrier_if_supported();
#endif
}
```

综上，你可以在执行加密操作之前调用经过抽象的 DIT 启用函数，并在操作之后恢复先前的 DIT 状态，从而保护一组加密指令：

```c
#if __has_include(<timingsafe.h>)
#include <timingsafe.h>
#endif

int main(void) {
    init_DIT_control();
    // 运行程序的其余部分。
    return 0;
}

int cryptographic_routine(void) {
#if __has_include(<timingsafe.h>)
    if (__builtin_available(macOS 15.2, iOS 18.2, visionOS 2.2, tvOS 18.2, watchOS 11.2, *)) {
        // 基于 API 的 DIT 控制。
        timingsafe_token_t token = timingsafe_enable_if_supported();
        // 在此执行恒定时间加密操作。
        timingsafe_restore_if_supported(token);
    } else 
#endif
    {
        // 回退到早期版本的 DIT 控制方式。
        bool was_DIT_enabled = set_DIT_enabled_if_supported();
        // 在此执行恒定时间加密操作。
        restore_DIT_if_supported(was_DIT_enabled);
    }
    return 0;
}
```

## 另请参阅

### 64 位接口

- [为 Apple 平台编写 64 位 Intel 代码](writing-64-bit-intel-code-for-apple-platforms.md) — 创建符合 Apple 平台所支持的应用二进制接口（ABI）的 64 位 Intel 汇编语言指令。
