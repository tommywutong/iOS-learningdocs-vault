---
title: 与依赖相关的链接器选项
source: MaskRay (宋方睿)
source_key: maskray
source_url: 'https://maskray.me/blog/2021-06-13-dependency-related-linker-options'
original_language: en
published: 2021-06-13
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:9f69d0276c10e05f'
translated: true
---

> 原文：[与依赖相关的链接器选项](https://maskray.me/blog/2021-06-13-dependency-related-linker-options)　·　MaskRay (宋方睿)

[2021-06-13](https://maskray.me/blog/2021-06-13-dependency-related-linker-options)

# 与依赖相关的链接器选项

本文介绍与依赖有关的链接器选项 `-z defs`、`--no-allow-shlib-undefined` 和 `--warn-backrefs`。在构建系统中采用它们，能够改善构建系统的健康状况。

## `-z defs`

`-z defs`（别名 `--no-undefined`）指示链接器：若可重定位目标文件中存在未解析的非弱未定义符号，就报告错误。相反的选项是 `-z nodefs`，它会抑制这类错误。链接可执行文件（`-no-pie` 和 `-pie`）时，默认启用 `-z defs`；链接共享对象（`-shared`）时，则默认启用 `-z undefs`。

“未解析”是指：(a) 链接进该组件的其他可重定位目标文件没有提供定义；并且 (b) 链接进该组件的共享对象也没有提供定义。

如果 X 中的未定义符号由链接时的共享对象 Y 提供，就可以说 X 依赖 Y。链接器会添加 `DT_NEEDED` 动态标记来记录这一事实。若 Y 带有 `DT_SONAME` 标记，`DT_NEEDED` 的值就是该 SONAME；否则，`DT_NEEDED` 的值就是 Y 的路径（绝对路径或相对路径）。

当 X 中的未定义符号不由任何链接时共享对象提供时，通常称为欠链接（underlinking）。

我能想到若干理由，说明为何 `-shared` 链接默认使用较宽松的 `-z undefs`：

1. ELF 支持符号介入（interposition）。例如，若共享对象含有未定义符号，运行时可以由任意共享对象或可执行文件提供该符号。不要求完整指定依赖关系，便能为运行时保留灵活性。
2. 两个共享对象 X 与 Y 之间可能存在相互引用。若必须完整指定依赖关系，就很难用常规方法打破这种僵局。一种变体是：可执行文件依赖 X，而 X 也引用可执行文件中的符号。

对于第 (a) 点，这种不受约束的灵活性并不十分适合构建系统。在模块化设计中，库应有定义清晰的职责和依赖关系。我们不会以任意共享对象替代某个链接时共享对象。需要这种灵活性时，可以定义一个接口（例如 C++ 虚函数），再让多个共享对象实现该接口。

完整指定依赖关系会使交付的共享对象 X 更易于使用。可执行文件链接很可能不会使用 X 所依赖的 Y；若链接 X 时还必须额外链接 Y，就会很别扭。

如果读过我关于 ELF 符号介入的文章，你就会知道：有了依赖信息，便可以进行直接绑定，从而缩短动态加载器查找符号的时间。不过，除 Solaris 之外，尚无其他 ELF 系统实现直接绑定。

1. 这表明库的分层不佳。X 和 Y 不再是相互隔离的组件：X 的改动可能影响 Y，反之亦然。对 X 进行单元测试时必须纳入 Y。对于归档文件，使用 GNU ld 和 gold 时需要 `--start-group X.a Y.a --end-group`。实际上，把 X 与 Y 合并通常是更好的策略。

如果不合并 X 和 Y，[http://blog.darlinghq.org/2018/07/mach-o-linking-and-loading-tricks.html](http://blog.darlinghq.org/2018/07/mach-o-linking-and-loading-tricks.html) 提到，Mach-O 对此类循环依赖的通常处理方式是将库链接两次。

```sh
ld -o libfoo.dylib foo.o -flat_namespace -undefined suppress
ld -o libbar.dylib bar.o -flat_namespace -undefined suppress
ld -o libfoo.dylib foo.o libbar.dylib
ld -o libbar.dylib bar.o libfoo.dylib
```

ELF 中对应的做法是：1  
2  
3  
4  
ld -shared foo.o -o foo.so  
ld -shared bar.o -o bar.so  
ld -shared -z defs foo.o bar.so -o foo.so  
ld -shared -z defs bar.o foo.so -o bar.so

构建系统可能同时支持归档文件和共享对象。归档文件是普通目标文件的集合，链接器对归档成员有特殊的选择语义（稍后会讨论归档成员选择）。如果 A.a 需要 B.a 中的定义，而链接依赖 A.a 的可执行文件时没有提供 B.a（`ld ... A.a`，而不是 `ld ... A.a b.a`），就可能会收到 `undefined reference to`（GNU ld）或 `undefined symbol:`（ld.lld）。在实践中，构建系统需要跟踪归档文件之间的依赖关系。

Mach-O 链接器默认的 `-undefined error` 与 ELF 的 `-z defs` 相似。Mach-O 链接器的 `-U` 允许单个符号保持未定义；ELF 链接器没有对应选项。

## `-z now`

`-z now` 指示链接器设置 `DF_1_NOW` 动态标记。ld.so 会急切解析 `R_*_JUMP_SLOT` 重定位；若有未解析符号，便报告错误。

可以将 `-z now` 看作放宽版的 `-z defs`：对完整依赖关系的要求从链接时推迟到了运行时。

## `--no-allow-shlib-undefined`

`--no-allow-shlib-undefined` 指示链接器：若共享对象中存在未解析的未定义符号，就报告错误。链接可执行文件（`-no-pie` 和 `-pie`）时默认使用 `-z defs`，而链接共享对象（`-shared`）时默认使用 `-z undefs`。

例如，执行 `ld -shared a.o b.so -o a.so` 时，若 `b.so` 有未定义符号，而 `a.o` 及 `b.so` 的依赖项均未提供其定义，链接器便会报告错误。

gold 和 ld.lld 不会递归加载 `DT_NEEDED` 标记。相反，只有当 `b.so` 的 `DT_NEEDED` 列表中的所有项都作为输入共享对象出现时，它们才会报告错误。假设 `b.so` 依赖 `c.so` 和 `d.so`。`ld.lld -shared a.o b.so c.so -o a.so` 不会因 `b.so` 中未解析的未定义符号而报错，因为 `b.so` 的依赖项 `d.so` 不在链接器命令行中。`ld.lld -shared a.so b.so c.so d.so -o a.so` 则可能报错。

如果一个构建系统使用 `-z defs` 时没有错误，使用 `--no-allow-shlib-undefined` 时也不会有错误。如果构建系统无法使用 `-z defs`，`--no-allow-shlib-undefined` 仍可捕捉一些传播而来的问题。

```cpp
// a.cc => a.o => a.so (not linked with -z defs)
void f(); // f is undefined
void g() { f(); }

// b.cc => b.o
void g();
int main() { g(); }
```

`ld b.o a.so` 会针对 `a.so` 中未定义的符号 `f` 报错。

在 glibc 中，glibc 尝试解析 `f` 时会出现运行时错误 `symbol lookup error: ... undefined symbol:`。

符号解析要么急切进行（`ld -z now` 或 `LD_BIND_NOW=1`），要么延迟进行（首次执行 PLT 表项时）。因此，在延迟 PLT 绑定的情况下，若设法不调用 `g`，`symbol lookup error: ... undefined symbol:` 错误便会消失。

若以 Bazel 的分层检查功能作类比，`-z defs`（link what you use）类似于 `layering_check`（include what you use），而 `--no-allow-shlib-undefined` 则有些类似 `hdrs_check`。参见 [使用 Clang 进行分层检查](https://maskray.me/blog/2022-09-25-layering-check-with-clang)。

GNU ld 会递归检查共享对象，gold 和 ld.lld 则不会。ld.lld 不这样做有几个原因。

首先是复杂性。GNU ld 手册页中，`-rpath-link=dir` 列出了 12 条规则，实在令人应接不暇。其中几条规则与交叉链接并不协调。消除本机链接和交叉链接的差异，是 ld.lld 的一项重要设计取舍。此外，我知道 `--no-copy-dt-needed-entries` 能以微妙的方式影响行为，而相关内容甚至没有文档说明。

其次是性能。递归加载需要解析额外的共享对象，可能会稍微拖慢链接过程。

第三是实用性。`--allow-shlib-undefined` 是 `-shared` 的一个不理想默认值；如今改变它可能带来破坏性影响。Mach-O 和 PE/COFF 有不少问题，但这或许是它们做对的一个地方。我曾在 https://maskray.me/blog/2021-06-13-dependency-related-linker-options 中用数段文字讨论这一点。为配合 `--allow-shlib-undefined` 而递归加载共享对象，让我感觉是在为一个错误的默认值打补丁。

### 如果符号定义在可重定位目标文件中，却没有导出，会怎样？

这是个相当复杂的话题。请参阅 [DSO 中的未定义符号与未导出的定义](https://maskray.me/blog/2023-10-31-dso-undef-and-non-exported-definition)。

---

Gentoo Linux 有一个质量保证项目，用于启用 `-Wl,--no-allow-shlib-undefined`：[https://wiki.gentoo.org/wiki/Project:Quality_Assurance/-Wl,-z,defs_and_-Wl,--no-allow-shlib-undefined](https://wiki.gentoo.org/wiki/Project:Quality_Assurance/-Wl,-z,defs_and_-Wl,--no-allow-shlib-undefined)。

## 归档文件处理

理解 `--warn-backrefs` 必须掌握这一概念。请参阅 [符号处理#归档文件处理](https://maskray.me/blog/2021-06-20-symbol-processing#archive-processing)。

## `--warn-backrefs`

VMS（现为 OpenVMS）、Mach-O ld64、Windows link.exe 和 ld.lld 采用了不同的设计。

对于 `ld.lld ... definition.a reference.o`，`definition.a` 的归档索引列出了其中定义的符号。处理 `definition.a` 时，ld.lld 用“惰性符号”表示这些惰性定义。每个惰性符号都关联着一个归档文件（成员）名称。处理 `reference.o`（或现在已被提取的惰性目标文件）时，未定义符号可能触发获取惰性符号，也就是提取先前 `definition.a` 中的一个成员。

这一归档处理策略的优点在于：在没有重复定义的情况下，`ld.lld ... definition.a reference.o` 和 `ld.lld ... reference.o definition.a` 不会因顺序而产生差异。

此外，`--start-group` 在 ld.lld 中是空操作。传统方法可能需要多次遍历归档成员，而 `--start-group` 会加剧这个问题。ld.lld 的方法最终证明更容易实现，并且能够提高归档处理性能。

我们来分析一个涉及 `a`、`b`、`c` 和 `d` 四个库的案例。依赖边为：`a->b, a->c, b->d, c->d`。还有一条未指定的边：`b->c`。当构建系统按依赖顺序排列这些库时，有两种可能。

- `ld ... a.a c.a b.a d.a` 可能导致未定义符号错误。若 `c.a` 的某些成员没有解析此前未定义的符号，它们可能被舍弃。提取 `b.a` 的成员时，其中的引用无法由已舍弃的 `c.a` 成员满足。
- `ld ... a.a b.a c.a d.a` 没有问题，因为处理完 `b.a` 后，我们应当已经看到 `c.a` 成员的全部符号需求。`a, b, c, d` 是完整依赖列表的一个拓扑顺序。

这种分层检查比较宽松，因为它只检查某一个特定的拓扑顺序。尽管如此，使用该选项的构建系统仍能发现许多缺失的依赖边。

该选项在二进制层面工作，能够捕捉一些基于模块的分层检查 `clang -fmodule-name=X -fmodules-strict-decluse`（`error: module X does not depend on a module exporting 'string.h'`）检测不到的问题，例如使用某个声明却没有包含相应头文件。

对于 ld.lld，`--warn-backrefs` 的引入是为了检查与 GNU ld 的归档处理兼容性问题。ld.lld 11.0.0 中，我大幅改进了 `--warn-backrefs`，使这种兼容性检查变得可靠。

由于 ld.lld 会记住归档名称，诊断信息（例如 `warning: backward reference detected: foo in a1.o refers to a2.o`）优于 GNU ld 的诊断信息（后者不含文件名）。

可以使用 `--warn-backrefs-exclude=a2.o` 抑制这一警告。

### 链接三明治问题

考虑 `ld def1.a ref.o def2.a`：`def1.a` 和 `def2.a` 都定义了 `ref.o` 引用的一个符号。我将这种情形称为链接三明治。

传统方法能够成功：链接器只会忽略 `def1.a`，然后从 `def2.a` 提取一个成员。ld.lld 则会在扫描 `ref.o` 中的未定义符号时，从 `def1.a` 提取一个成员。`def2.a` 的成员可能会被提取，也可能不会。

若被提取，`def1.a` 的成员和 `def2.a` 的成员会包含重复符号。若两个定义均为 `STB_GLOBAL`，ld.lld 会报告重复符号错误。

若未被提取，GNU ld 和 ld.lld 便会提取不同的归档成员。最常见的情形是 `def1.a` 和 `def2.a` 具有相同路径，例如 `liblldCommon.a liblldCOFF.a liblldCommon.a`。这种情况无害。我提交了 [https://reviews.llvm.org/D77522](https://reviews.llvm.org/D77522)，以抑制 `--warn-backrefs` 诊断。若 `def1.a` 和 `def2.a` 的路径不同，这就类似违反单一定义规则。我认为，如果要报告警告，可能需要增加一个新选项。

---

下面的示例展示了 GNU ld 与 LLD 行为不同的另一种情形。链接器首先提取 `b.a(b0.o)`，以解析未定义的 `foo`。

- GNU ld 随后提取 `b.a(b1.o)`，以解析 `dup` 符号。
- LLD 则提取 `a.a(a.o)`。值得注意的是，`--warn-backrefs` 标志未能将这种行为差异识别为潜在问题。

```plaintext
# RUN: rm -rf %t && split-file %s %t && cd %t
# RUN: as main.s -o main.o
# RUN: as a.s -o a.o
# RUN: as b0.s -o b0.o
# RUN: as b1.s -o b1.o
# RUN: ar rc a.a a.o
# RUN: ar rc b.a b0.o b1.o

# RUN: ld.bfd main.o a.a b.a
# RUN: ld.lld --fatal-warnings --warn-backrefs main.o a.a b.a

#--- main.s
.globl _start
_start:
  call foo

#--- a.s
.globl dup; dup: hlt

#--- b0.s
.globl foo; foo: call dup
#--- b1.s
.globl dup; dup: ret
```
