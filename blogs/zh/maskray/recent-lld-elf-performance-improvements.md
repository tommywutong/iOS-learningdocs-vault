---
title: 近期 lld/ELF 性能改进
source: MaskRay (宋方睿)
source_key: maskray
source_url: 'https://maskray.me/blog/2026-04-12-recent-lld-elf-performance-improvements'
original_language: en
published: 2026-04-12
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:90b3f001f894e795'
translated: true
---

> 原文：[Recent lld/ELF performance improvements](https://maskray.me/blog/2026-04-12-recent-lld-elf-performance-improvements)　·　MaskRay (宋方睿)

[2026-04-12](https://maskray.me/blog/2026-04-12-recent-lld-elf-performance-improvements)

# 近期 lld/ELF 性能改进

更新于 2026-05。

自从 LLVM 22 分支被裁剪以来，我提交了若干补丁，并行化了更多的链接阶段并削减了任务运行时的开销。本文比较了当前 `main` 分支与 lld 22.1、[mold](https://github.com/rui314/mold) 和 [wild](https://github.com/davidlattimore/wild) 的性能。

亮点：在 Release+Asserts 配置下，clang 使用 `--gc-sections` 的链接速度是 lld 22.1 的 1.34 倍；Chromium Debug 配置使用 `--gdb-index` 的链接速度是之前的 1.09 倍。mold 和 wild 仍然领先——最后一部分将解释原因。

## 基准测试

`lld-0201` 是 2026-02-01 的 `main` 分支（6a1803929817）；`lld-HEAD` 是 2026-05-16 的 `main` 分支（20b0089ea340），其中包含了 [`[ELF] Parallelize input file loading`](https://github.com/llvm/llvm-project/commit/83f8eee57d5a2e9215b506a5ddc82db980fb47d0)（commit 83f8eee57d5a）以及后续的任务运行时和 `Symbol` 清理工作。`mold` 和 `wild` 使用 `--no-fork` 运行，因此 Wall clock 时间包含了链接器进程本身。

使用三个可复现的 tar 包，`--threads=8`，`hyperfine -w 2 -r 10`（对于亚秒级的 clang-relassert 链接使用 `-w 3 -r 30`），通过 `numactl -C 20-28` 绑定到 CPU 核心。

| 工作负载 | lld-0201 | lld-HEAD | mold | wild |
|---|---|---|---|---|
| clang-23 Release+Asserts, `--gc-sections` | 1.262 s | 940.7 ms | 599.4 ms | 375.8 ms |
| clang-23 Debug (no `--gdb-index`) | 4.409 s | 4.038 s | 2.745 s | 1.472 s |
| clang-23 Debug (`--gdb-index`) | 6.038 s | 5.627 s | 4.418 s | N/A |
| Chromium Debug (no `--gdb-index`) | 6.094 s | 5.654 s | 2.864 s | 2.033 s |
| Chromium Debug (`--gdb-index`) | 7.708 s | 7.070 s | 4.196 s | N/A |

注意，`llvm/lib/Support/Parallel.cpp` 的设计使得主线程在 `parallelFor` 期间保持空闲，因此 `--threads=N` 实际利用了 `N+1` 个线程。

wild 尚未实现 `--gdb-index`——它会静默警告并跳过，在 Chromium 上产生的输出大约小 477 MB。为了进行公平的四向比较，我也从响应文件中移除了 `--gdb-index`；上表中的 `no --gdb-index` 行使用了该设置。

在深入探讨之前，先看几个观察点：

- 对于 lld，`--gdb-index` 在 Chromium 链接上的额外开销为 `+1.42 s`（5.65 s → 7.07 s），而 mold 为 `+1.33 s`（2.86 s → 4.20 s）。这目前是剩余差距中最大的之一。
- 排除 `--gdb-index`，在这台机器上 mold 快 1.47 到 1.97 倍，wild 快 2.50 到 2.78 倍。还有很大的提升空间。
- `clang-23 Release+Asserts --gc-sections`（工作负载 1）从 1.262 秒降至 941 毫秒，在约 15 周内加速了 1.34 倍。这主要归功于并行的 `--gc-sections` 标记、并行输入加载以及下文的任务运行时清理——每个因素都贡献了一个乘数因子。

### macOS (Apple M4) 说明

相同的 `clang-23 Release+Asserts --gc-sections` 工作负载，相同的 `lld-0201`（6a1803929817）和 `lld-HEAD`（20b0089ea340）commit，在 Apple M4（macOS 26.2，四个链接器均使用系统分配器）上，`--threads=8`，`hyperfine -w 3 -r 30`。wild 没有 `--chroot`，因此需要设置 `--sysroot=` 指向可复现目录，以解析 `libc.so`/`libm.so` `GROUP` 脚本中的绝对路径；执行的工作完全相同。

| 链接器 | Wall | User | Sys | (User+Sys)/Wall |
|---|---|---|---|---|
| lld-0201 | 365.4 ± 4.3 ms | 515.7 ms | 265.8 ms | 2.14x |
| lld-HEAD | 261.9 ± 4.2 ms | 493.0 ms | 471.9 ms | 3.68x |
| mold | 256.6 ± 3.0 ms | 909.9 ms | 345.5 ms | 4.89x |
| wild | 131.4 ± 1.0 ms | 468.0 ms | 319.6 ms | 5.99x |

## 并行化 `--gc-sections` 标记

垃圾回收以前是在 `InputSection` 图上进行的单线程 BFS。在 Release+Asserts 的 clang 链接中，`markLive` 占用了 1562 毫秒 Wall time 中的约 315 毫秒（20%）。

[commit 6f9646a598f2](https://github.com/llvm/llvm-project/commit/6f9646a598f25efa3c4db066d2d51fb248b13526) 添加了 `markParallel`，一种层级同步的 BFS。每个 BFS 层级使用 `parallelFor` 处理；新发现的 section 进入每个线程的队列，在进入下一层级前进行合并。当 `!TrackWhyLive && partitions.size() == 1` 时激活并行路径。事实证明以下实现细节很重要：

- 深度受限的内联递归（`depth < 3`），之后再推入下一层级队列。短引用链保持在缓存中，避免了队列开销。
- 采用乐观的“load then compare-exchange” section 标志去重，而非原子的 fetch-or。绝大多数 section 只被访问一次，因此 load 几乎总是成功的。

在 Release+Asserts 的 clang 链接中，`markLive` 在 `--threads=8` 时从 315 毫秒降至 82 毫秒（在 `--threads=16` 时从 199 毫秒降至 50 毫秒）；总 Wall time 加速 1.16 到 1.18 倍。

为了正确性，需要两个前置清理：

- [commit 6a874161621e](https://github.com/llvm/llvm-project/commit/6a874161621ec52b8efa125790e3e8e72bb9167a) 将 `Symbol::used` 移入已有的 `std::atomic<uint16_t> flags`。该位域之前与其他标记线程存在竞争。
- [commit 2118499a898b](https://github.com/llvm/llvm-project/commit/2118499a898b514f70fb1754ad8713a4267f7bd3) 将 `SharedFile::isNeeded` 与标记遍历解耦。`--as-needed` 曾用来在 `isNeeded` 内部翻转 `resolveReloc`，这需要跨线程的协调写入；现在它变成了对全局符号的 GC 后扫描。

## 并行化输入文件加载

历史上，`LinkerDriver::createFiles` 遍历命令行并串行调用 `addFile`。`addFile` 映射文件（`MemoryBuffer::getFile`），嗅探 magic 值，并构造 `ObjFile`、`SharedFile`、`BitcodeFile` 或 `ArchiveFile`。对于 thin archive，它还会实例化每个成员。在具有数百个 archive 和数千个 object 的工作负载上，这个串行遍历主导了链接的早期阶段。

[commit 83f8eee57d5a](https://github.com/llvm/llvm-project/commit/83f8eee57d5a2e9215b506a5ddc82db980fb47d0) 重写了 `addFile`，为每个非脚本输入记录一个 `LoadJob`，同时记录驱动程序状态机的快照（`inWholeArchive`、`inLib`、`asNeeded`、`withLOption`、`groupId`）。`createFiles` 完成后，`loadFiles` 将 job 分发到工作线程。链接脚本保留在主线程上，因为 `INPUT()` 和 `GROUP()` 会递归回调 `addFile`。

一些微妙之处使得这项工作比听起来更难：

- `BitcodeFile` 和 fatLTO 构造调用 `ctx.saver` / `ctx.uniqueSaver`，两者都是非线程安全的 `StringSaver` / `UniqueStringSaver`。我将这些构造函数序列化在互斥锁之后；纯 ELF 链接不会触发它们。
- Thin archive 成员缓冲区以前直接追加到 `ctx.memoryBuffers`。为了跨 `--threads` 值保持输出确定性，每个 job 现在累积到一个每 job 的 `SmallVector` 中，然后按命令行顺序合并到 `ctx.memoryBuffers`。
- `InputFile::groupId` 以前是在 `InputFile` 构造函数内部通过全局计数器分配的。并行构造时，赋值竞争虽然不可观测但仍然不优雅；[b6c8cba516daabced0105114a7bcc745bc52faae](https://github.com/llvm/llvm-project/commit/b6c8cba516daabced0105114a7bcc745bc52faae) 将 `++nextGroupId` 提升到串行驱动程序循环中，并在构造后将该值存储到每个文件中。

输出与旧版 lld 在字节级别相同，并且跨 `--threads` 值具有确定性，我通过在 Chromium 上使用 `diff` 比较 `--threads={1,2,4,8}` 的结果进行了验证。

使用 `--time-trace` 分解有助于设定预期。在 Chromium 上，`createFiles` 的串行部分仅占 5.9 秒 Wall time 中的约 81 毫秒，而 `loadFiles`（在此补丁之后）并行运行约 103 毫秒。串行的 `readFile`/mmap 不是瓶颈。真正起作用的是将每文件构造函数的工作（magic 嗅探、archive 成员实例化、bitcode 初始化）与主线程上启动的其他一切重叠执行，同时工作线程处理 job 列表。

## 扩展并行重定位扫描

自 LLVM 17 以来，重定位扫描已经是并行的，但三种情况通过 `bool serial` 选择退出：

1. `-z nocombreloc`，因为 `.rela.dyn` 合并了相对和非相对重定位，需要确定性排序。
2. MIPS，因为 `MipsGotSection` 在扫描期间被修改。
3. PPC64，因为 `ctx.ppc64noTocRelax`（一个包含 `DenseSet` 对的 `(Symbol*, offset)`）在无锁的情况下被写入。

[commit 076226f378df](https://github.com/llvm/llvm-project/commit/076226f378df115622d0d959e975ee7c7fb3c051) 和 [commit dc4df5da886e](https://github.com/llvm/llvm-project/commit/dc4df5da886e09d36577b3302952bc91b5e7e154) 无条件分离相对和非相对动态重定位，并且始终以 `.rela.dyn` 构建 `combreloc=true`；`-z nocombreloc` 的唯一剩余作用是抑制 `DT_RELACOUNT`。[commit 2f7bd4fa9723](https://github.com/llvm/llvm-project/commit/2f7bd4fa97232dfab7f2347c745005eb9e2ffd2d) 随后使用已有的 `ctx.ppc64noTocRelax` 保护 `ctx.relocMutex`，该互斥锁仅在罕见的慢路径上被获取。在这些更改之后，只有 MIPS 仍然串行运行扫描。

## 特定目标的重定位扫描

重定位扫描以前通过 `Relocations.cpp` 中的一个通用循环进行，该循环为每次重定位通过虚函数调用 `Target->getRelExpr`——一次用于分类表达式类型（PC 相对、PLT、TLS 等），另一次来自 TLS 优化分发。在任何实际的链接中，这是一个处理数千万次重定位的热内部循环，虚函数调用及其后的分发 switch 占据了实际的一部分成本。

解决方案是将整个每 section 扫描循环移到特定目标代码中，这样每个 `Target::scanSection` / `scanSectionImpl` 对可以内联自己的 `getRelExpr`，原地处理 TLS 优化，并针对该架构上占主导地位的两三种重定位类型进行特化。已于 2026 年初在大多数后端部署：

- [4b887533389c](https://github.com/llvm/llvm-project/commit/4b887533389c78e3e678b3af85d1dc8e3bf59e83) x86 (i386 / x86-64)。在 lld 自己的对象文件中，`R_X86_64_PC32` 和 `R_X86_64_PLT32` 占重定位的约 95%，现在命中了内联热路径。
- [371e0e2082e9](https://github.com/llvm/llvm-project/commit/371e0e2082e9) AArch64, [4ea72c1e8cbd](https://github.com/llvm/llvm-project/commit/4ea72c1e8cbd) RISC-V, [cd01e6526af6](https://github.com/llvm/llvm-project/commit/cd01e6526af6) LoongArch, [c04b00de7508](https://github.com/llvm/llvm-project/commit/c04b00de7508) ARM, [6d9169553029](https://github.com/llvm/llvm-project/commit/6d9169553029) Hexagon, [aec1c984266c](https://github.com/llvm/llvm-project/commit/aec1c984266c) SystemZ, [5e87f8147d68](https://github.com/llvm/llvm-project/commit/5e87f8147d68) PPC32, [aecc4997bf12](https://github.com/llvm/llvm-project/commit/aecc4997bf12) PPC64。

除了去虚拟化，将 TLS 重定位处理内联到 `scanSectionImpl` 中使得特定于 TLS 优化的表达式类型可以被通用表达式取代：`R_RELAX_TLS_GD_TO_LE` / `R_RELAX_TLS_LD_TO_LE` / `R_RELAX_TLS_IE_TO_LE` 折叠为 `R_TPREL`，`R_RELAX_TLS_GD_TO_IE` 折叠为 `R_GOT_PC`，并且 `getTlsGdRelaxSkip` 被移除。共享分发路径中剩余的部分——从 `getRelExpr` 和 `relocateNonAlloc` 调用的 `relocateEH`——是一个小得多的集合。

在 clang-14 链接（`Scan relocations`，x86-64，50 次运行，通过 `--threads=8` 测量）上，平均 `--time-trace` Wall time 从 110 毫秒下降到 102 毫秒，仅 x86 commit 就贡献了约 8% 的提升。

## 更快的 `getSectionPiece`

合并 section（`SHF_MERGE`）将其输入分割成“块（piece）”。每次对合并 section 的引用都需要将偏移量映射到一个块。旧的实现总是在 `MergeInputSection::pieces` 中进行二分查找，从 `MarkLive`、`includeInSymtab` 和 `getRelocTargetVA` 中调用。

[commit 42cc45477727](https://github.com/llvm/llvm-project/commit/42cc454777274a06933abcd098ec3281158717f9) 以两种方式改变了这一点：

1. 对于非字符串的固定大小合并 section，`getSectionPiece` 直接使用 `offset / entsize`。
2. 对于指向合并 section 的非 section `Defined` 符号，块索引在 `splitSections` 期间预先解析，并打包到 `Defined::value` 中，格式为 `((pieceIdx + 1) << 32) | intraPieceOffset`。

二分查找现在仅限于通过 section 符号（基于 addend）进行的引用，这在 AArch64 上很常见，但在 x86-64 上很少见，因为汇编器会为 `.L` 引用到可合并字符串时发出本地标签。带 `--gc-sections` 的 clang-relassert 链接加速了 1.05 倍。

## 优化底层的 `llvm/lib/Support/Parallel.cpp`

上述所有成果都依赖于 `llvm/lib/Support/Parallel.cpp`，这个由 lld、dsymutil 和少数调试信息工具共享的小型工作窃取式任务运行时。该文件中的四个更改至关重要：

- [commit c7b5f7c635e2](https://github.com/llvm/llvm-project/commit/c7b5f7c635e2534a9b2b2b204998b0bc39921b7e) — `parallelFor` 以前将工作预先拆分成最多 `MaxTasksPerGroup`（1024）个任务，并通过执行器的互斥锁 + 条件变量生成每个任务。现在它只生成 `ThreadCount` 个工作线程；每个工作线程通过原子的 `fetch_add` 获取下一个块。在 clang-14 链接（`--threads=8`）上，futex 调用从约 31K 下降到约 1.4K（glibc release+asserts）；Wall time 从 927 毫秒降至 879 毫秒。这就是为什么并行的标记和并行的扫描数字值得引用的原因——在旧的运行时上，生成开销是正在并行化的工作中实际的一部分。
- [commit 9085f74018a4](https://github.com/llvm/llvm-project/commit/9085f74018a4f465afa84815d64af850f09b733f) — `TaskGroup::spawn()` 将基于互斥锁的 `Latch::inc()` 替换为原子的 `fetch_add`，并通过 `Latch&` 传递 `Executor::add()`，以便工作线程直接调用 `dec()`。每次 spawn 消除了一次 `std::function` 构造。
- [commit 5b1be759295c](https://github.com/llvm/llvm-project/commit/5b1be759295c4a2f357fbad852e04c74fc012dc1) — 移除了 `Executor` 抽象基类。`ThreadPoolExecutor` 一直是唯一的实现；`add()` 和 `getThreadCount()` 现在是直接调用而非虚函数分发。
- [commit 8daaa26efdda](https://github.com/llvm/llvm-project/commit/8daaa26efdda3802f73367d844b267bda3f84cbe) — 通过工作窃取启用嵌套的并行 `TaskGroup`。历史上，嵌套组串行运行以避免死锁（本应运行嵌套任务的工作线程可能被阻塞在外层组的 `sync()` 中）。工作线程现在在等待时主动执行队列中的任务，而不是仅仅阻塞。主线程上的根级组保持高效的阻塞式 `Latch::sync()`，因此常见的非嵌套情况没有任何开销。在 lld 中，这使得从 `SyntheticSection::writeTo` 内部调用时具有内部并行性的 `GdbIndexSection`（`MergeNoTailSection`、`OutputSection::writeTo`）能够自动并行化，而不是退化为在工作线程上串行执行——这正是 [D131247](https://reviews.llvm.org/D131247) 通过一直向下传递根 `TaskGroup` 来绕过的确切情况。

## 值得提及的小改进

- [036b755daedb](https://github.com/llvm/llvm-project/commit/036b755daedb) 并行化了 `demoteAndCopyLocalSymbols`。每个文件通过 `parallelFor` 将本地 `Symbol*` 指针收集到一个每文件的向量中，然后串行合并到符号表。在链接带有 208K `.symtab` 条目的 clang-14 时（使用 `--no-gc-sections`），速度是原来的 1.04 倍。

xxh3 `hash_combine` 交换（[71d78b2220e4](https://github.com/llvm/llvm-project/commit/71d78b2220e4dc4b022fd74aec16ed8d93fc419e)）以及 `Symbol` 构造函数初始化和冗余 `memset` 移除（[905a88b92343](https://github.com/llvm/llvm-project/commit/905a88b923433eb8cd83677ea55bee82eb9ba498), [20b0089ea340](https://github.com/llvm/llvm-project/commit/20b0089ea340d6c9355e631c81f0ce82d80263e5)）也有微小改进。

| lld 构建 | clang-relassert 链接 |
|---|---|
| pre-xxh3 (525fab579da1) | 939.0 ± 29.0 ms |
| xxh3 (71d78b2220e4) | 932.2 ± 23.3 ms |
| pre Symbol-init (2e4c820c05fd) | 928.4 ± 31.4 ms |
| HEAD (20b0089ea340) | 926.3 ± 30.0 ms |

## lld 仍然耗时的地方

为了定位差距，我在 clang-relassert 链接（clang-23 Release+Asserts，`lld --time-trace`，`mold --perf`；每个阶段的数据是 5 次运行的平均值）上运行了 `wild --time`、`--gc-sections` 和 `--threads=8`。按可比阶段分组：

| 工作范围 | lld-0201 | lld-HEAD | mold | wild |
|---|---|---|---|---|
| mmap + 解析 section + 合并字符串 + 符号解析 | 391 ms | 320 ms | 218 ms | 120 ms |
| `--gc-sections` 标记 | 285 ms | 76 ms | 36 ms | — * |
| Scan relocations | 116 ms | 91 ms | 61 ms | — * |
| 分配 / 最终化 / symtab | 77 ms | 86 ms | 27 ms | 86 ms |
| 写入 section | 87 ms | 87 ms | 77 ms | 103 ms |
| **Wall (hyperfine)** | **1262 ms** | **941 ms** | **599 ms** | **376 ms** |

* wild 将 `--gc-sections` 标记和重定位驱动的活跃 section 传播融合到一个 `Find required sections` 阶段（62 ms），因此这两行实际上是合并的。

关于 wild 解析数字的一个微妙之处：wild 的 `Load inputs into symbol DB` 阶段本身只有 24 ms，但它只做了 `mmap` + `.symtab` 扫描 + 全局名称哈希分桶。Section 头解析、可合并字符串拆分、COMDAT 处理和符号解析被推迟到后续的 wild 阶段。上表中的 120 ms 行汇总了这些（`Load inputs into symbol DB` 24 + `Resolve symbols` 13 + `Resolve alternative symbol definitions` 4 + `Section resolution` 21 + `Merge strings` 58），因此它覆盖了 lld 称为 `Parse input files` 的相同工作。

有意义的差距，按绝对影响排序：

**解析：lld-HEAD 320 ms 对比 wild 120 ms ≈ 2.7 倍。** 在此工作负载上剩余的最大跨链接器差距，同样的模式也适用于下面更大的工作负载。该阶段已经是并行的；差距在于每对象解析路径的常数因子（读取 section 头、驻留字符串、拆分 CIE/FDE、将全局符号合并到符号表）。在 clang-relassert 上，仅 200 ms 的解析差距就约占 lld-HEAD 和 wild 之间 565 ms Wall clock 差距的 35%。

**分配 / 最终化 / symtab：86 ms 对比 mold 27 ms ≈ 3.2 倍。** `finalizeAddressDependentContent`、`assignAddresses`、`finalizeSynthetic`、`Add symbols to symtabs` 和 `Finalize .eh_frame` 在此工作负载上总共花费约 86 ms；mold 的等效操作（`compute_section_sizes`、`compute_symtab_size`、`create_output_sections`、`set_osec_offsets`）总计 27 ms。此差距随 `.symtab` 条目数量线性增长——在 clang-debug 上是 127 ms lld 对比 27 ms mold，在 Chromium 上是 570 ms 对比约 80 ms。我有一个本地分支，它将 `SymbolTableBaseSection::finalizeContents` 转换为前缀和驱动的并行填充，并用每文件 `stable_partition` 缓冲区替换 `MapVector` + `lateLocals` shuffle。1640 个 ELF 测试通过；尚未提交。

**`markLive`：76 ms，比 2 月 1 日的基线（285 ms）快 3.7 倍。** 这是苹果对橘子的比较：lld 支持 `__start_`/`__stop_` 边、`SHF_LINK_ORDER` 依赖、链接脚本 `KEEP` 以及其他特性。lld 使用 `--gc-sections --as-needed` 正确处理 `Symbol::used`（测试了 `gc-sections-shared.s`、`weak-shared-gc.s`、`as-needed-not-in-regular.s`）：

- **mold 在两个轴向上过度近似 `DT_NEEDED`**：它会为仅通过弱重定位引用的 DSO 发出 `DT_NEEDED`，也会为仅从 GC 后的 section 引用的 DSO 发出。它还会在 `.dynsym` 中保留仅可从死 section 到达的未定义符号。
- **wild 正确处理弱引用，但未正确处理死 section 引用**：仅弱引用不会强制 `DT_NEEDED`（与 lld 一致），但仅从 GC 后的 section 引用的 DSO 仍然会得到 `DT_NEEDED` 条目。wild 确实从 `.dynsym` 中丢弃了相应的未定义符号，因此其 `DT_NEEDED` 决策和其 symtab 包含决策略有分歧。
- **lld 在所有三个轴向上都是最严格的**

**扫描重定位：91 ms 对比 61 ms。** 干净的 1.5 倍比例，绝对值较小。特定目标扫描（`Add target-specific relocation scanning for …`）移除了一些分发开销；剩余的是 `InputSectionBase::relocations` 的开销。wild 将重定位驱动的活跃性折叠到 `Find required sections` 中，这就是为什么没有单独的 wild 行。

有趣的是，**写入 section 内容不是差距**（四个链接器都在 77–103 ms 之间）。先前认为 `.debug_*` section 写入是 lld 弱点的假设并未经得起测量。

一个仅在对调试信息密集的工作负载上表现出来的成本是 `--gdb-index` 构建，lld 在 Chromium 上花费约 1.3 秒，而 mold 约 0.9 秒。这项工作按输入来说是高度并行的，但 lld 通过分片的 `DenseMap` 汇集字符串驻留；mold 使用由 HyperLogLog 调整大小的无锁 `ConcurrentMap`。wild 尚未实现 `--gdb-index`。

wild 值得单独指出：其用户时间与 lld 相当，但系统时间大约是其一半，并且其解析阶段在所有三个工作负载上比两个 C++ 链接器快 4 到 8 倍。mold 则处于另一个极端——在所有工作负载上用户时间最高，但通过激进的并行性弥补。
