---
title: lld 中的 RISC-V 链接器松弛
source: MaskRay (宋方睿)
source_key: maskray
source_url: 'https://maskray.me/blog/2022-07-10-riscv-linker-relaxation-in-lld'
original_language: en
published: 2022-07-10
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:9d0d0d2494c7e4bf'
translated: true
---

> 原文：[RISC-V linker relaxation in lld](https://maskray.me/blog/2022-07-10-riscv-linker-relaxation-in-lld)　·　MaskRay (宋方睿)

[2022-07-10](https://maskray.me/blog/2022-07-10-riscv-linker-relaxation-in-lld)

# lld 中的 RISC-V 链接器松弛

2022年7月7日，我在 ld.lld 中添加了一个 RISC-V 链接器松弛框架，并实现了 `R_RISCV_ALIGN/R_RISCV_CALL/R_RISCV_CALL_PLT` 松弛。这些更改将包含在下一个 llvm-project 版本 15.0.0 中。本文描述了该实现。

更多关于 RISC-V 链接器松弛的信息，请参阅 [RISC-V 链接器松弛的阴暗面](https://maskray.me/blog/2021-03-14-the-dark-side-of-riscv-linker-relaxation)。

## 问题

ld.lld 执行以下步骤（已简化）：

- 解析命令行参数
- 查找并扫描输入文件（.o、.so、.a），与符号解析交错进行
- 调用 LLVM LTO 获取 ELF 目标文件
- 全局转换（基于段的垃圾回收、相同代码折叠等）
- 创建合成段
- 将输入段和合成（链接器生成的）段映射到输出段
- 扫描重定位
- 确定合成段的最终形式
- 布局（地址、thunk、`SHT_RELR`、符号赋值）
- 分配文件偏移
- 写入头部和段

我们需要找到一个位置来插入松弛处理。

### 重定位扫描

重定位扫描决定动态重定位决策，并确定 `.got`、`.got.plt`、`.plt`、`.rela.dyn` 和 `.relr.dyn` 段的大小。它们地址和大小的变化将影响后续段以及使用某些链接器脚本特性的段。单次重定位扫描方案与整个 ld.lld 的设计紧密相关，难以更改。重定位扫描耗时，我们希望仅在必要时执行它。

链接器松弛可能会使输入段变小，并使当前的段布局失效。对于调用代码序列，如果尺寸减小使得目标距离重定位位置足够近，我们需要将代码序列重写为更短的形式。这种更改可能会产生级联效应，并触发进一步的松弛。例如，在以下由三个输入段组成的图中，如果段 B 中的 `call x`（一个展开为 8 字节的伪指令）被缩短，B 的尺寸将减小，而 A 中的 `call c` 可能成为新的松弛候选。

```text
A[... call c; ...] -- B[... call x; ...] -- C[c: ...]
```

### 符号值

段布局的改变可能会改变符号值。虽然罕见，但输出段地址可以使用符号值。在以下链接器脚本示例中，`.mid` 尺寸的改变将改变 `.high` 的地址。

```text
SECTIONS {
  .mid 0x10800 : { mid_start = .; *(.mid); mid_end = .; }
  .high 0x110000+(mid_end-mid_start) : { *(.high) }
  .high2 0x210000+SIZEOF(.mid) : { *(.high2) }
}
```

## 设计

链接器松弛必须是一个迭代过程。由于它与地址相关的段和符号赋值相互作用，主要思路是将链接器松弛添加到布局阶段。因此我们得到：

- 扫描重定位
- 确定合成段的最终形式
- 布局（_松弛_、地址、thunk、`SHT_RELR`、符号赋值）
- 分配文件偏移

“扫描重定位”被保留。我们添加另一个重定位扫描来处理所有可松弛的重定位。此过程会计算多个结果。

- 对于每个重定位位置，替换的重定位类型、重写的代码序列以及要删除的字节数
- 每个输入代码段的大小
- 相对于该段定义的每个符号的 `st_value` 和 `st_size`

这些结果被 `script->assignAddresses()` 用于计算下一次布局：段地址和符号值。我们重复此过程直到结果收敛。

在某些不常见的情况下，输入段可能会在后续迭代中扩大。如果我们选择在一次迭代结束时收缩段，那么扩大将难以处理。我的想法是，段尺寸收缩和代码序列重写需要推迟到迭代固定点达到之后。

```cpp
template <class ELFT> void Writer<ELFT>::finalizeAddressDependentContent() {
  ...
  uint32_t pass = 0;
  for (;;) {
    Create thunks or call relaxOnce;
    ++pass;

    Report "not converged" if pass is too large;

    Update address-dependent sections;
    Assign addresses to sections and symbols;
  }
  if (!config->relocatable && config->emachine == EM_RISCV)
    riscvFinalizeRelax(pass);
  ...
}
```

在 `finalizeAddressDependentContent` 中新增了两个函数调用：`relaxOnce` 和 `riscvFinalizeRelax`。RISC-V 端口实现了 `relaxOnce`，它对所有输入代码段调用 `relax`。

```cpp
bool RISCV::relaxOnce(int pass) const {
  ...
  bool changed = false;
  for (OutputSection *osec : outputSections) {
    if (!(osec->flags & SHF_EXECINSTR))
      continue;
    for (InputSection *sec : getInputSections(*osec, storage))
      changed |= relax(*sec);
  }
  return changed;
}
```

```cpp
static bool relax(InputSection &sec) {
  Restore original st_value for symbols relative to this section.

  std::fill_n(aux.relocTypes.get(), sec.relocations.size(), R_RISCV_NONE);
  aux.writes.clear();
  for (auto [i, r] : llvm::enumerate(sec.relocations)) {
    const uint64_t loc = secAddr + r.offset - delta;
    uint32_t &cur = aux.relocDeltas[i], remove = 0;
    switch (r.type) {
    case R_RISCV_ALIGN: {
      remove = the number of bytes to delete;
      break;
    }
    case R_RISCV_CALL:
    case R_RISCV_CALL_PLT:
      if (i + 1 != sec.relocations.size() &&
          sec.relocations[i + 1].type == R_RISCV_RELAX)
        relaxCall(sec, i, loc, r, remove);
      break;
    // Other relaxable relocation types
    }

    Update symbol st_value/st_size according to symbol anchors;

    delta += remove;
    if (delta != cur) {
      cur = delta;
      changed = true;
    }
  }

  Update trailing symbol anchors;

  sec.bytesDropped = delta;
  return changed;
}
```

`relax` 遍历此输入段的未解析重定位，并将 `remove` 设置为要删除的字节数。`delta` 是要删除的累计字节数。它被存储在 `aux.relocDeltas[i]` 中，供 `riscvFinalizeRelax` 处理。

### 符号锚点

为相对于该段定义的每个符号更新 `st_value` 和 `st_size` 使用了一种巧妙的技术。

```plaintext
  ...
a:
  .balign 16  # R_RISCV_ALIGN(r_addend=12)
b:
```

在这个例子中，`R_RISCV_ALIGN` 位置有一个 `.balign` 重定位。它的偏移量等于符号 `a` 的 `st_value`。如果 `a` 前面的某些字节被删除，`a` 的 `st_value` 需要减少相应数量的字节。`b` 具有更大的 `st_value`，其 `st_value` 还需要额外考虑 `R_RISCV_ALIGN` 松弛的影响。

要计算相对于当前输入段的所有符号的 `st_value`，我们维护两个已排序列表：(a) 可松弛的重定位 (b) `st_value`。对于每个符号，找到其 `r_offset` 小于该符号 `st_value` 的最大重定位，然后将 `st_value` 减去该 `r_offset`。`st_value` 值和 `r_offset` 值的交错处理类似于归并排序的合并函数。

`st_size` 可以类似地计算。我们将 `st_value+st_size` 值与 `r_offset` 值交错处理。在确定最终的 `st_value+st_size` 后，将总和减去最终的 `st_value` 以计算最终的 `st_size`。在实现中，我将所有初始的 `st_value` 和 `st_value+st_size` 值放在一个已排序列表中。两者都由一个 `SymbolAnchor` 对象表示。

```cpp
struct SymbolAnchor {
  uint64_t offset;
  Defined *d;
  bool end; // true for the anchor of st_value+st_size
};

    if (remove) {
      for (; sa.size() && sa[0].offset <= r.offset; sa = sa.slice(1)) {
        if (sa[0].end)
          sa[0].d->size = sa[0].offset - delta - sa[0].d->value;
        else
          sa[0].d->value -= delta;
      }
    }
```

由于我们使用了递减量（`sa[0].d->value -= delta;`），当开始下一次迭代时，我们需要恢复原始的 `st_value`。

### 最终确定松弛

```cpp
void elf::riscvFinalizeRelax(int passes) {
  ...
  for (OutputSection *osec : outputSections) {
    if (!(osec->flags & SHF_EXECINSTR))
      continue;
    for (InputSection *sec : getInputSections(*osec, storage)) {
      RISCVRelaxAux &aux = *sec->relaxAux;
      if (!aux.relocDeltas)
        continue;

      Allocate space for the new section content to `p`;
      sec->rawData = makeArrayRef(p, newSize);

      // Update section content: remove NOPs for R_RISCV_ALIGN and rewrite
      // instructions for relaxed relocations.
      for (size_t i = 0, e = rels.size(); i != e; ++i) {
        uint32_t remove = aux.relocDeltas[i] - delta;
        delta = aux.relocDeltas[i];
        if (remove == 0)
          continue;

        // Copy from last location to the current relocated location.
        const Relocation &r = rels[i];
        uint64_t size = r.offset - offset;
        memcpy(p, old.data() + offset, size);
        p += size;
```

```cpp
        // For R_RISCV_ALIGN, we will place `offset` in a location (among NOPs)
        // to satisfy the alignment requirement. If `remove` is a multiple of 4,
        // it is as if we have skipped some NOPs. Otherwise we are in the middle
        // of a 4-byte NOP, and we need to rewrite the NOP sequence.
        int64_t skip = 0;
        if (r.type == R_RISCV_ALIGN) {
          if (remove % 4 != 0) {
            skip = r.addend - remove;
            Rewrite `skip` bytes with nop and an optional trailing c.nop;
          }
        } else if (RelType newType = aux.relocTypes[i]) {
          Rewrite code sequence;
        }

        p += skip;
        offset = r.offset + skip + remove;
      }
      memcpy(p, old.data() + offset, old.size() - offset);

      Subtract the previous relocDeltas value from the relocation offset.
      For a pair of R_RISCV_CALL/R_RISCV_RELAX with the same offset, decrease
      their r_offset by the same delta.
    }
  }
}
```

对于每个输入代码段，我们遍历其未解析的重定位。对于与某些要删除字节相关联的 `R_RISCV_ALIGN`，我们将所有内容从上一个位置复制到 `r_offset`，然后为下一次复制跳过一些字节。 1  
2  
3  
4  
... # 将所有内容从上一个位置复制到 r_offset  
.balign 8 # R_RISCV_ALIGN(r_addend=6)  
# 可能会跳过 NOP 的前缀部分供下一次 memcpy 使用  
addi a0, a0, 1

假设我们需要删除 2 个字节。如果我们使用 `[]` 来表示已复制的字节，当前和下一次复制模式将如下所示： 1  
2  
3  
4  
5  
旧：...] NOP NOP [NOP NOP NOP NOP ADDI ADDI ADDI ADDI ...]  
旧：下一次复制  
  
新：...] [NOP NOP NOP NOP ADDI ADDI ADDI ADDI ...]  
新：

让我们看一个调用松弛的例子。`call` 伪指令展开为一对 auipc 和 jalr。 1  
call dest@plt # R_RISCV_CALL_PLT，R_RISCV_RELAX

如果 auipc+jalr 可以松弛为一条 4 字节的 jal，我们忽略 auipc，将 jalr 替换为 jal，并递增 `p` 和 `offset`，以便下一次 memcpy 将从 jalr 之后的第一个字节开始复制。重写的指令从 `skip=4` 指示的第一个字节开始。 1  
2  
3  
4  
旧：...] AUIPC AUIPC AUIPC AUIPC JALR JALR JALR JALR [.........]  
 remove=4 skip=4 下一次复制  
  
新：...] JAL JAL JAL JAL [.........]

这是一个 `tail` 伪指令被松弛为 `c.j` 的演示。 1  
tail dest@plt # R_RISCV_CALL_PLT，R_RISCV_RELAX  
 1  
2  
3  
4  
旧：...] AUIPC AUIPC AUIPC AUIPC JALR JALR JALR JALR [.........]  
 remove=6 skip=2 下一次复制  
  
新：...] C.J C.J [.........]

## 可松弛的代码序列

### 对齐松弛

使用 3 个值我们可以计算出重定位位置的地址：`secAddr + r.offset - delta`。`delta` 是要删除的累计字节数。它从原始的 `r_offset` 值中减去。

对齐是 `PowerOf2Ceil(r.addend + 2)`。对齐后的预期位置是 `(loc + align - 1) & -align`，因此 `loc + r.addend  - ((loc + align - 1) & -align)` 是要删除的字节数。

### 调用松弛

以下伪指令可用于调用子例程。 1  
2  
3  
4  
5  
6  
7  
8  
9  
10  
11  
call a@plt # @plt 可以省略。在 ld.lld 中 R_RISCV_CALL/R_RISCV_CALL_PLT 无法区分  
# auipc ra，0 # R_RISCV_CALL_PLT(a)，R_RISCV_RELAX  
# jalr ra，0(ra)  
  
tail a@plt  
# auipc t1，0 # R_RISCV_CALL_PLT(a)，R_RISCV_RELAX  
# jalr zero，0(t1)  
  
jump a，t0  
# auipc t0，0 # R_RISCV_CALL(a)，R_RISCV_RELAX  
# jalr zero，0(t0)

每个都展开为一对 `auipc` 和 `jalr`。

- `call`：ra 既是临时寄存器又是目标寄存器
- `tail`：t1 是临时寄存器。x0 是目标寄存器
- `jump`：指定了临时寄存器。x0 是目标寄存器

这两个指令可以松弛为一个替代指令。有 3 种选择：

- `c.j`：RVC，目标寄存器是 x0，偏移量可以表示为 int12
- `c.jal`：RV32C，目标寄存器是 ra，偏移量可以表示为 int12
- `jal`：偏移量可以表示为 int21

前两种需要删除 6 个字节并重写 2 个字节，而第三种需要删除 4 个字节并重写 4 个字节。

### 局部执行 TLS 松弛

更多关于 TLS 的信息，请参阅 [关于线程本地存储的一切](https://maskray.me/blog/2021-02-14-all-about-thread-local-storage)。

计算 TLS 变量的地址或向其中存储值需要 3 条指令。如果 `st_value(x) < 2048`（即 `hi20(x) == 0`），一条指令就足够了。

```text
lui rd, %tprel_hi(x)           # R_RISCV_TPREL_HI20, R_RISCV_RELAX
add rd, rd, tp, %tprel_add(x)  # R_RISCV_TPREL_ADD, R_RISCV_RELAX
addi rd, rd, %tprel_lo(x)      # R_RISCV_TPREL_LO12_I, R_RISCV_RELAX

=>

addi rd, tp, st_value(x)
```

```text
lui rd, %tprel_hi(x)           # R_RISCV_TPREL_HI20, R_RISCV_RELAX
add rd, rd, tp, %tprel_add(x)  # R_RISCV_TPREL_ADD, R_RISCV_RELAX
sw rs, st_value(x)(rd)         # R_RISCV_TPREL_LO12_S, R_RISCV_RELAX

=>

sw rs, st_value(x)(rd)
```

待定补丁： [https://reviews.llvm.org/D129425](https://reviews.llvm.org/D129425)

### lui 松弛

如果 ld.lld 实现了这个，大多数绝对和 PC 相对重定位需要记录，因为它们可以成为松弛的候选。这可能会增加相当大的开销。

### 针对全局指针的松弛

请参阅 [https://www.sifive.com/blog/all-aboard-part-3-linker-relaxation-in-riscv-toolchain](https://www.sifive.com/blog/all-aboard-part-3-linker-relaxation-in-riscv-toolchain) 上的“针对全局指针的松弛”。

我认为这种选择是短视的，因此我创建了 [https://github.com/riscv-non-isa/riscv-elf-psabi-doc/issues/298](https://github.com/riscv-non-isa/riscv-elf-psabi-doc/issues/298)，但它很快就被关闭了。然而，我没有收到支持该方案的强有力的论据。我希望感兴趣的用户能通过做一些测量来帮助我。
