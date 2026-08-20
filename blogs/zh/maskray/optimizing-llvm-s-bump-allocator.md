---
title: 优化 LLVM 的 bump 分配器
source: MaskRay (宋方睿)
source_key: maskray
source_url: 'https://maskray.me/blog/2026-06-28-optimizing-llvm-bump-allocator'
original_language: en
published: 2026-06-28
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:340231e9e29a9f34'
translated: true
---

> 原文：[Optimizing LLVM's bump allocator](https://maskray.me/blog/2026-06-28-optimizing-llvm-bump-allocator)　·　MaskRay (宋方睿)

[2026-06-28](https://maskray.me/blog/2026-06-28-optimizing-llvm-bump-allocator)

# 优化 LLVM 的 bump 分配器

`BumpPtrAllocator` 是 LLVM 的 bump 分配器（arena 分配器）：每次分配在 slab 内递增一个指针，当分配器销毁时一次性释放所有内存。它支撑着 Clang 的 `ASTContext`、lld 的 `make<T>` 对象池、TableGen 记录以及许多其他 arena。

以下是三次近期变更前的快速路径：

```cpp
__attribute__((returns_nonnull)) void *Allocate(size_t Size, Align Alignment) {
  BytesAllocated += Size;                               // (3) accounting RMW
  uintptr_t AlignedPtr = alignAddr(CurPtr, Alignment);  // (1) always realign
  size_t SizeToAllocate = Size;
#if LLVM_ADDRESS_SANITIZER_BUILD
  SizeToAllocate += RedZoneSize;
#endif
  uintptr_t AllocEndPtr = AlignedPtr + SizeToAllocate;
  if (LLVM_LIKELY(AllocEndPtr <= uintptr_t(End)
                  && CurPtr != nullptr)) {              // (2) bound + null check
    CurPtr = reinterpret_cast<char *>(AllocEndPtr);
    ...
    return reinterpret_cast<char *>(AlignedPtr);
  }
  return AllocateSlow(Size, SizeToAllocate, Alignment);
}
```

三项变更简化了标记的三行。

## 最小对齐跳过重新对齐（[#205240](https://github.com/llvm/llvm-project/pull/205240)）

`alignAddr(CurPtr, Alignment)` 是浪费的：刚递增过的指针通常已经足够对齐。[#205240](https://github.com/llvm/llvm-project/pull/205240) 将每个大小向上取整到 `MinAlign`（默认 8），因此快速路径仅对超对齐请求进行重新对齐。我从 [Bump Allocation: Up or Down?](https://coredumped.dev/2024/03/25/bump-allocation-up-or-down/) 学到了这个技巧：

```cpp
// 优化为常量
SizeToAllocate = alignToPowerOf2(SizeToAllocate, MinAlign);

uintptr_t AlignedPtr = uintptr_t(CurPtr);
// 对于常见的 `alignof(T) <= 8` 情况，该分支完全消除。
if (Alignment.value() > MinAlign)
  AlignedPtr = alignAddr(CurPtr, Alignment);
```

我在第一次尝试中犯了一个错误：`nullptr` 加上非零偏移量触发了 UBSan 诊断。通过将运算保持在 `uintptr_t` 域中修复。

`SpecificBumpPtrAllocator<T>` 是类型化变体：它拥有自己的对象，并在 `DestroyAll` 中为每个对象运行 `~T()`，该方法按固定的 `sizeof(T)` 步长遍历 slab。

在声明分配器的位置，`T` 可能是不**完整类型**——例如类成员 `SpecificBumpPtrAllocator<MCSectionELF>` 旁只有 `MCSectionELF` 的前向声明。`alignof(T)` 会强制 `T` 在那里完整化；而字面量则不会。

```cpp
using BumpPtrAllocatorTy =
    BumpPtrAllocatorImpl<MallocAllocator, 4096, 4096, 128, /*MinAlign=*/1>;

T *Allocate(size_t num = 1) {
  if constexpr (alignof(T) <= alignof(std::max_align_t))
    return static_cast<T *>(Allocator.Allocate(num * sizeof(T), Align()));
  return Allocator.Allocate<T>(num);
}
```

Slab 按 `max_align_t` 对齐，此分配器只分配 `num * sizeof(T)` 字节——这是 `alignof(T)` 的倍数——因此 bump 指针**已经**是 `alignof(T)` 对齐的；请求 `Align()`（即 1）能让快速路径跳过重新对齐分支。函数体只有在 `Allocate` 实际被调用时才会实例化，此时 `T` 是完整类型，因此即使类声明允许不完整的 `T`，这里的 `alignof(T)` 也没问题。超对齐类型（`alignof(T) > alignof(std::max_align_t)`）走通用路径，该路径会重新对齐。

## 哨兵 End 删除空检查（[#205485](https://github.com/llvm/llvm-project/pull/205485)）

`__attribute__((returns_nonnull))` 指定返回值非空。在一个 `CurPtr` 和 `End` 都为空的新分配器中，`Allocate(0)` 之前返回 null。2022 年，[https://reviews.llvm.org/D125040](https://reviews.llvm.org/D125040) 将 `&& CurPtr != nullptr` 检查添加到了快速路径条件中，这并不理想。

我尝试了 1  
2  
3  
// 快速路径检查。该条件对于新分配器（End ==  
// nullptr）也会失败，以避免单独的空检查。  
if (LLVM_LIKELY(AlignedPtr + SizeToAllocate - 1 \< uintptr_t(End))) { ... }

但后来采纳了 aengelke 的建议。将结尾存储为实际结尾之后的一个哨兵（`EndSentinel = realEnd + 1`，当没有 slab 时为 `0`）将两个条件折叠为一次无符号比较：

```cpp
if (LLVM_LIKELY(AllocEndPtr < EndSentinel)) { ... }
```

空分配器的 `EndSentinel == 0`，因此 `AllocEndPtr < 0` 始终为 false，空情况会落入慢速路径，无需单独的分支。

## 删除每次分配的统计（[#205711](https://github.com/llvm/llvm-project/pull/205711)）

`BytesAllocated += Size` 是每次分配时对成员变量的读-改-写操作，支撑着 `getBytesAllocated()`，该函数报告**请求的**字节数——与 `getTotalMemory()` 的 slab 容量不同。它只有统计/诊断消费者：lldb 的 ConstString 内存报告、clangd 的调试日志、TableGen 的 `dumpAllocationStats` 以及一个 clang 回归测试。删除该成员变量并将这些消费者迁移（主要迁移到 `getTotalMemory()`）移除了热路径上的存储操作。

**一个细节：红区与 ABI。** ASan 红区大小也是一个成员变量。将其限定在 `#if LLVM_ADDRESS_SANITIZER_BUILD` 下以在发布版本中移除，是 ABI 隐患：该宏是**按编译单元**的，因此一个 ASan 插桩的 TU 和一个非 ASan 的 `libLLVM` 会在结构体布局上默默不一致。该成员变量改为限定在 `LLVM_ENABLE_ABI_BREAKING_CHECKS` 下，该宏按每个库构建固定，并在链接时强制（通过 `EnableABIBreakingChecks` 符号）；红区运算则同时受两个宏控制。

综合来看，快速路径变为：

```cpp
void *Allocate(size_t Size, Align Alignment) {
  size_t SizeToAllocate = Size;
#if LLVM_ADDRESS_SANITIZER_BUILD && LLVM_ENABLE_ABI_BREAKING_CHECKS
  SizeToAllocate += RedZoneSize;
#endif
  SizeToAllocate = alignToPowerOf2(SizeToAllocate, MinAlign);
  uintptr_t AlignedPtr = uintptr_t(CurPtr);
  if (Alignment.value() > MinAlign)
    AlignedPtr = alignAddr(CurPtr, Alignment);
  uintptr_t AllocEndPtr = AlignedPtr + SizeToAllocate;
  if (LLVM_LIKELY(AllocEndPtr < EndSentinel)) {
    CurPtr = reinterpret_cast<char *>(AllocEndPtr);
    ...
    return reinterpret_cast<char *>(AlignedPtr);
  }
  return AllocateSlow(Size, SizeToAllocate, Alignment);
}
```

## 生成的汇编

分配一个典型 arena 对象——通过 `Allocate<T>()` 分配一个 24 字节、8 对齐的节点——编译为六条指令的快速路径（`clang -O2`，release）：

```plaintext
mov  rax, [rdi]        # CurPtr (also the return value)
lea  rcx, [rax + 0x18] # new = CurPtr + 24
cmp  rcx, [rdi + 0x8]  # vs EndSentinel
jae  .slow
mov  [rdi], rcx        # CurPtr = new
ret
```

这匹配了经典的 bump 快速路径。一个**向下**递增的分配器不需要区分 `rax`/`rcx`——少一个活动值，但指令数保持不变。LLVM 的设计是向上递增：`identifyObject`、分配顺序和 `SpecificBumpPtrAllocator::DestroyAll` 的前向 `sizeof(T)` 步长都假定如此。剩余的差距在于空间，而非指令。

## 聚合编译时影响

这些变更将 `Allocate` 缩小到内联器的成本阈值以下，因此其调用者（例如 `new (Context) T`）会在之前调用非内联的位置进行内联。执行的指令数下降——但这是**再分布**：其中内联链现在扩展的目标文件变大，而其他文件则因移除的存储操作而略微缩小。

在 stage2（由 stage1 Clang 构建）上的性能提升大于 stage1（由系统 GCC 构建）。

在 `main` 之上回滚所有三项变更可以隔离它们的组合效果（[对比](https://llvm-compile-time-tracker.com/compare.php?from=dbd070fbd793c8a9129044abd669466e87d2ea8e&to=3a7d64a882421052101899d7d9c23685db5fd355&stat=instructions:u)）：

显著（≥3σ vs. 测量噪声）：🟢 改进。未标记 = 在噪声范围内。

| 配置 | instructions:u | max-rss |
|---|---|---|
| stage1-O3 | −0.04% | +0.04% |
| stage1-ReleaseThinLTO | −0.04% | −0.01% |
| stage1-ReleaseLTO-g | −0.04% | +0.06% |
| stage1-O0-g | 🟢 −0.09% | +0.25% |
| stage1-aarch64-O3 | −0.04% | +0.04% |
| stage1-aarch64-O0-g | 🟢 −0.12% | −0.01% |
| stage2-O3 | 🟢 −0.14% | −0.15% |
| stage2-O0-g | 🟢 −0.36% | −0.06% |

## 要点

- bump 分配器的快速路径是几条实际工作指令，包裹在对齐和统计中；每条都可以从常见情况中提出。
- 将“空”编码为 `0` 哨兵可以将空检查折叠到边界比较中。
- 可测量的指令数提升来自于更廉价 `Allocate` 解锁的内联，而非移除的微操作——并且表现为**再分布**，而非均匀缩小。
- 影响布局的成员变量可以依赖于 `LLVM_ENABLE_ABI_BREAKING_CHECKS`（链接时强制），但绝不能依赖于按 TU 的 `LLVM_ADDRESS_SANITIZER_BUILD`。
