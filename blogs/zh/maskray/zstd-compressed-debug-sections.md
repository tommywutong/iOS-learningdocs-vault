---
title: zstd 压缩的调试段
source: MaskRay (宋方睿)
source_key: maskray
source_url: 'https://maskray.me/blog/2022-09-09-zstd-compressed-debug-sections'
original_language: en
published: 2022-09-09
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:ebb5dd8c627c68ed'
translated: true
---

> 原文：[zstd compressed debug sections](https://maskray.me/blog/2022-09-09-zstd-compressed-debug-sections)　·　MaskRay (宋方睿)

[2022-09-09](https://maskray.me/blog/2022-09-09-zstd-compressed-debug-sections)

# zstd 压缩的调试段

2022 年 10 月更新。

1 月我写了[压缩调试段](https://maskray.me/blog/2022-01-23-compressed-debug-sections)。古老的 zlib 已显老态，出现了在除普及度和更大内存占用空间外的所有指标上都更优的替代方案。显而易见的选择是 Zstandard，但我对采用它并解决生态系统问题并没有那么自信。无论如何，我逐渐从 llvm-project 中移除了一些旧的 `.zdebug` 支持，以便更容易地引入新格式。

6 月，Cole Kissane 在 LLVM 论坛上发布了 [[RFC] 将 Zstandard 作为 LLVM 的第二种压缩方法](https://discourse.llvm.org/t/rfc-zstandard-as-a-second-compression-method-to-llvm/63399)。我了解到其他人也在研究更适合 ELF 压缩调试段的压缩格式，于是告诉自己：是时候向 System V 通用应用二进制接口（generic ABI）提议加入 `ELFCOMPRESS_ZSTD` 了。

ELF 是一种优雅的格式，经受住了时间的考验。30 年前前辈们创造的许多东西沿用至今。每个新特性，即使是像引入一个新常量这样的小改动，都必须达到很高的接受标准。关于[添加新的 ch_type 值：ELFCOMPRESS_ZSTD](https://groups.google.com/g/generic-abi/c/satyPkuMisk) 有许多讨论。

我个人认为，选定的格式需要具备以下特性：

- 具有开放的压缩算法和实现。
- 在合理的内存占用空间和复杂度下，能提供显著的益处（压缩速度、解压速度、压缩比）。
- 完全向后兼容。我希望在 20 年后仍能解压今天创建的调试段。
- 拥有广泛且活跃的使用场景。当格式值标准化后，使用者愿意添加支持。
- 有良好的文档。
- 易于使用。

能满足所有这些特性的压缩格式很少。ELF 不喜欢为一个特性引入大量选项。它不是一个实验每种新奇压缩格式的场地。我们担心平台碎片化，消费者也不愿意支持多种格式，每种都从略微不同的角度声称自己是好选择。参见附录，我最近对许多压缩工具进行的测试。

我在提案讨论中提出了许多论据。大约花了一个月时间，`ELFCOMPRESS_ZSTD` 于[2022 年 7 月被接受](https://groups.google.com/g/generic-abi/c/satyPkuMisk/m/KwTF_U8rBAAJ)。

## 工具链支持

下一步是添加工具链支持。最重要的组件是汇编器、链接器和调试器。此外也需要许多其他组件。

工具链组件：

- binutils：[截至 2022 年 11 月全部实现](https://sourceware.org/bugzilla/show_bug.cgi?id=29397)

    - addr2line：符号化需要解压调试段
    - gas：压缩调试段
    - ld, gold：解压压缩的输入段并压缩输出调试段。[已实现](https://sourceware.org/bugzilla/show_bug.cgi?id=29641)
    - dwp：解压压缩的 `.dwo`。dwp 使用 gold 的代码
    - nm：`--line-numbers` 使用调试信息
    - objcopy：`--decompress-debug-sections` 和 `--compress-debug-sections=zstd`
    - objdump：`--dwarf` 解压压缩的调试段
    - readelf：`--debug-dump` 和 `--decompress` 解压压缩的段。[功能请求](https://sourceware.org/bugzilla/show_bug.cgi?id=29640)
- gdb：[已实现](https://sourceware.org/bugzilla/show_bug.cgi?id=29397)

    - 解压可执行文件、共享对象、独立调试文件和 `.dwo` 文件中的压缩调试段。[功能请求](https://sourceware.org/bugzilla/show_bug.cgi?id=29563)
    - MiniDebugInfo 段 `.gnu_debugdata` 使用 xz 压缩。[zstd 功能请求](https://sourceware.org/bugzilla/show_bug.cgi?id=29584)
- GCC：[13.0 将支持 `-gz=zstd`](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=106897)
- llvm-project：截至 2022 年 9 月全部实现（里程碑：16.0.0）。默认的 `LLVM_ENABLE_ZSTD=on` 需要 [CMake 配置文件](https://github.com/facebook/zstd/issues/3271)才能生效。

    - Clang：使用级别 5 压缩 `.o` 和（如果启用 split DWARF）`.dwo`
    - llvm-objcopy：`--decompress-debug-sections` 和 `--compress-debug-sections=zstd`（级别 5）。在 [D130458](https://reviews.llvm.org/D130458)（ELFCLASS64）和 [D134385](https://reviews.llvm.org/D134385)（ELFCLASS32）中实现
    - ld.lld：解压 `ELFCOMPRESS_ZSTD` 输入段（[D129406](https://reviews.llvm.org/D129406)）并使用级别 3 压缩输出调试段（[D133548](https://reviews.llvm.org/D133548), [D133679](https://reviews.llvm.org/D133679)）
    - llvm-dwarfdump：使用 LLVMObject API 解压 `ELFCOMPRESS_ZSTD` 输入段（[D134116](https://reviews.llvm.org/D134116)）
    - llvm-dwp：使用 LLVMObject API
    - llvm-symbolizer：使用 LLVMObject API
    - lldb：使用 LLVMObject API
- elfutils：[2022 年 12 月实现](https://sourceware.org/bugzilla/show_bug.cgi?id=29565)
- mold：[2022 年 9 月实现](https://github.com/rui314/mold/issues/700)

其他语言：

- Go：[cmd/link 功能请求](https://github.com/golang/go/issues/55107)

其他工具：

- bloaty：其 `-d compileunits` 解析 DWARF。[功能请求](https://github.com/google/bloaty/issues/318)
- dwz

### llvm-project 支持

在 llvm-project 方面，关于 API 应该如何设计有很多争论。在 2022 年 9 月 9 日那一周，我们（Cole Kissane、David Blaikie、我）达成一致，自由函数风格的压缩 API 是可以接受的。我已经推送了一些更改，`llvm-objcopy --compress-debug-sections=zstd`、`clang -gz=std`、`ld.lld --compress-debug-sections=zstd` 现在可用。请注意，我选择先实现 llvm-objcopy 支持，这样我就可以用 llvm-objcopy 测试其他组件。

```plaintext
% cat a.cc
#include <iostream>
int main() { std::cout << "zstd"; }
% clang -c -g -gz a.cc
% readelf -x .debug_info a.o

Hex dump of section '.debug_info':
 NOTE: This section has relocations against it, but these have NOT been applied to this dump.
  0x00000000 02000000 00000000 1a180000 00000000 ................
  0x00000010 01000000 00000000 28b52ffd 601a17ed ........(./.`...
...
```

`ELFCOMPRESS_ZSTD` (2) 可以通过前 4 个字节识别。在一个小端对象文件中，它显示为 `02000000`。

如果 llvm-objcopy 是使用 zstd 支持构建的，使用 `--decompress-debug-sections` 解压对象文件：1  
2  
3  
4  
5  
6  
7  
8  
% llvm-objcopy --decompress-debug-sections a.o a.o.decompressed  
% readelf -x .debug_info a.o.decompressed  
  
Hex dump of section '.debug_info':  
 NOTE: This section has relocations against it, but these have NOT been applied to this dump.  
 0x00000000 16180000 05000108 00000000 01002100 ..............!.  
 0x00000010 01000000 00000000 00020000 00000000 ................  
...

在 llvm-project 方面，我们在 2022 年 10 月达到了完全的功能就绪状态。

如果有人能在 GNU 方面接手这些工作项，以便许多 Linux 发行版可以开始研究采用 zstd 压缩的调试段，那将非常好。

### GNU 工具链支持

主要更改针对 binutils-gdb 仓库。这项工作结果证明比我为 llvm-project 所做的工作要困难得多。

zstd 压缩功能的入口点在 binutils、gas 和 ld 中。binutils 和 ld 使用 bfd，所以我们需要更新 bfd。

我通过跟随 `config/zlib.m4` 创建了 `config/zstd.m4`。`AC_ZSTD` 中的 `config/zstd.m4` 定义了 `ZLIB_CFLAGS` 和 `ZLIB_LDLIBS`。在将其接入 `bfd/configure.ac` 和 `bfd/Makefile.am` 后，我需要将 `AC_ZSTD` 添加到每个使用 bfd 的顶级项目中，因为 bfd 是作为归档链接的，并且没有好的传递依赖支持。

以下是针对 `bfd/Makefile.am` 的更改。该模式需要在许多其他目录中重复。1  
2  
3  
4  
5  
6  
7  
8  
--- a/bfd/Makefile.am  
+++ b/bfd/Makefile.am  
@@ -60 +60 @@ NO_WERROR = @NO_WERROR@  
-AM_CFLAGS = $(WARN_CFLAGS) $(ZLIBINC)  
+AM_CFLAGS = $(WARN_CFLAGS) $(ZLIBINC) $(ZSTD_CFLAGS)  
@@ -779 +779 @@ libbfd_la_DEPENDENCIES = $(OFILES) ofiles  
-libbfd_la_LIBADD = `cat ofiles` @SHARED_LIBADD@ $(LIBDL) $(ZLIB)  
+libbfd_la_LIBADD = `cat ofiles` @SHARED_LIBADD@ $(LIBDL) $(ZLIB) $(ZSTD_LIBS)

```text
% rg -l --sort=path ZSTD_LIBS
bfd/Makefile.am
bfd/Makefile.in
bfd/configure
binutils/Makefile.am
binutils/Makefile.in
binutils/configure
gas/Makefile.am
gas/Makefile.in
gas/configure
gdb/Makefile.in
gdb/acinclude.m4
gdb/configure
ld/Makefile.am
ld/Makefile.in
ld/configure
libctf/Makefile.in
libctf/configure
libctf/configure.ac
sim/Makefile.in
sim/arch-subdir.mk.in
sim/common/Make-common.in
sim/configure
sim/ppc/Makefile.in
```

记得使用相应版本的 autoconf 和 automake 更新自动生成的文件：1  
PATH=~/projects/automake-1.15.1/bin:$PATH ~/projects/autoconf-2.69/bin/autoreconf -vf bfd binutils gas ld libctf sim

```sh
make -C bfd headers
```

某些 bfd/ 文件更改需要使用 `make -C $build/bfd headers` 更新 `bfd/bfd-in2.h`。1  
2  
3  
4  
5  
6  
7  
8  
/* DO NOT EDIT! -*- buffer-read-only: t -*- This file is automatically  
 generated from "bfd-in.h", "init.c", "opncls.c", "libbfd.c",  
 "bfdio.c", "bfdwin.c", "section.c", "archures.c", "reloc.c",  
 "syms.c", "bfd.c", "archive.c", "corefile.c", "targets.c", "format.c",  
 "linker.c", "simple.c" and "compress.c".  
 Run "make headers" in your build bfd/ to regenerate. */  
  
/* Main header file for the bfd library -- portable access to object files.

## 附录

（实验于 2022 年 10 月进行。）我用 `-DCMAKE_BUILD_TYPE=Debug -DLLVM_TARGETS_TO_BUILD=all` 构建了一份 Clang 主干版本。三个最大的 DWARF v5 调试段是 `.debug_info`、`.debug_str` 和 `.debug_line`。1  
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
12  
13  
14  
15  
16  
17  
18  
19  
20  
21  
22  
23  
24  
25  
% bloaty clang-16  
 FILE SIZE VM SIZE  
 -------------- --------------  
 32.3% 451Mi 0.0% 0 .debug_info  
 16.4% 229Mi 0.0% 0 .debug_str  
 11.4% 159Mi 0.0% 0 .debug_line  
 11.3% 157Mi 55.0% 157Mi .text  
 8.0% 112Mi 0.0% 0 .strtab  
 5.7% 80.2Mi 0.0% 0 .debug_str_offsets  
 3.6% 50.4Mi 17.6% 50.4Mi .rodata  
 2.4% 33.6Mi 0.0% 0 .debug_addr  
 2.2% 30.8Mi 10.7% 30.8Mi .eh_frame  
 1.7% 24.0Mi 0.0% 0 .symtab  
 1.0% 13.6Mi 4.7% 13.6Mi .rela.dyn  
 1.0% 13.4Mi 0.0% 0 .debug_rnglists  
 0.8% 11.0Mi 3.8% 11.0Mi .dynstr  
 0.7% 10.5Mi 3.7% 10.5Mi .data.rel.ro  
 0.6% 8.05Mi 0.0% 0 .debug_abbrev  
 0.5% 7.69Mi 2.7% 7.69Mi .eh_frame_hdr  
 0.2% 2.79Mi 1.0% 2.79Mi .dynsym  
 0.1% 848Ki 0.3% 848Ki .gnu.hash  
 0.1% 827Ki 0.1% 263Ki [21 Others]  
 0.0% 0 0.2% 544Ki .bss  
 0.0% 497Ki 0.2% 497Ki .data  
 100.0% 1.37Gi 100.0% 286Mi TOTAL

`ninja -t commands bin/clang` 转储链接可执行文件的编译器驱动命令。使用 `-fuse-ld=lld -Wl,--prproduce=/tmp/clang-debug.tar` 调用该命令以获取 tarball。使用 `llvm-objcopy --dump-section` 提取一个段。

```sh
cd /tmp
tar xf clang-debug.tar
cd clang-debug
ld.lld @response.txt

llvm-objcopy --dump-section .debug_info=debug_info clang-16 /dev/null
llvm-objcopy --dump-section .debug_str=debug_str clang-16 /dev/null
llvm-objcopy --dump-section .debug_line=debug_line clang-16 /dev/null
```

我尝试了 brotli、bzip2、gzip、lz4、lzo、pigz、xz、zstd，并手动验证了 zstd 在压缩速度、解压速度和压缩比方面是最优的。找出所有这些库的 API 将很不方便。所以我走了一条捷径：使用包管理器安装这些压缩工具，并希望它们使用类似的编译器驱动选项，这样比较相对公平。

以下是一些结果：

```sh
#!/bin/zsh
i=$1
o0=$i.o0
o1=$i.o1

measure() {
  rm -f $o0 $o1
  local a=$(/usr/bin/time -f '%e\t%M\t' ${=1} 2>&1)
  ${=2}
  local b=$(/usr/bin/time -f '%e\t%M\t' ${=3} 2>&1)
  stat -c "$a$b%s"$'\t'"$1" $o0
}
measure_no_o() {
  rm -f $o0 $o1
  local a=$(/usr/bin/time -f '%e\t%M\t' ${=1} > $o0 2> t0)
  ${=2}
  local b=$(/usr/bin/time -f '%e\t%M\t' ${=3} > $o1 2> t1)
  stat -c "$(<t0)$(<t1)%s"$'\t'"$1" $o0
}

do_pigz() { measure "pigz -zfk -p 1 -S .o0 $i" "cp -f $o0 $o1.gz" "pigz -dfk -p 1 $o1.gz"; }
do_brotli() { measure "brotli -f $* $i -o $o0" "" "brotli -df $o0 -o $o1"; }
do_bzip2() { measure_no_o "bzip2 -cf $* $i" "" "bzip2 -dcf $o0"; }
do_gzip() { measure "gzip -fk -S .o0 $* $i" "" "cp -f $o0 $o1.gz" "gzip -dfk $o1.gz"; }
do_lz4() { measure "lz4 -fq $* $i $o0" "" "lz4 -dfq $o0 $o1"; }
do_lzop() { measure "lzop -f $* $i -o $o0" "" "lzop -df $o0 -o $o1"; }
do_xz() { measure_no_o "xz -c $* $i" "" "xz -dc $o0"; }
do_zstd() { measure "zstd -fq $@ $i -o $o0" "" "zstd -dfq $o0 -o $o1"; }

print 'comp\tRSS\tdecomp\tRSS\tsize\tcommand'
do_pigz
do_brotli -q 1; do_brotli -q 3; do_brotli -q 5; do_brotli -q 9
do_bzip2 -1; do_bzip2 -3
do_gzip -1; do_gzip -3
do_lz4 --fast; do_lz4 -1; do_lz4 -3; do_lz4 -5; do_lz4 -9
do_lzop -1; do_lzop -3; do_lzop -9
do_xz -0; do_xz -1; do_xz -3; do_xz -6
do_zstd --fast; do_zstd -1; do_zstd -3; do_zstd -5; do_zstd -9; do_zstd -18
```

```text
% numactl -C 20 ./bench.sh debug_info
comp    RSS     decomp  RSS     size    command
19.99   2568    2.37    2212    212342615       pigz -zfk -p 1 -S .o0 debug_info
2.44    4044    2.48    19188   244890939       brotli -f -q 1 debug_info -o debug_info.o0
5.92    36300   2.22    19264   211420890       brotli -f -q 3 debug_info -o debug_info.o0
22.77   110516  2.11    21128   193129564       brotli -f -q 5 debug_info -o debug_info.o0
239.99  114140  2.12    20988   191699881       brotli -f -q 9 debug_info -o debug_info.o0
36.24   2396    15.71   1604    212700609       bzip2 -cf -1 debug_info
34.29   3640    16.52   2396    221881700       bzip2 -cf -3 debug_info
9.16    2008    0.14    2604    227302010       gzip -fk -S .o0 -1 debug_info
11.57   2072    0.14    2536    221444175       gzip -fk -S .o0 -3 debug_info
1.16    8872    0.49    9116    310918343       lz4 -fq --fast debug_info debug_info.o0
1.25    8828    0.48    9168    295430369       lz4 -fq -1 debug_info debug_info.o0
6.85    8904    0.49    8896    265793678       lz4 -fq -3 debug_info debug_info.o0
8.60    9016    0.49    9000    263660439       lz4 -fq -5 debug_info debug_info.o0
14.26   8936    0.48    8848    262365618       lz4 -fq -9 debug_info debug_info.o0
1.42    2244    1.24    1720    283798959       lzop -f -1 debug_info -o debug_info.o0
1.43    2088    1.25    1632    282736380       lzop -f -3 debug_info -o debug_info.o0
71.94   2504    1.32    1756    240402339       lzop -f -9 debug_info -o debug_info.o0
27.76   5024    11.23   2560    164560076       xz -c -0 debug_info
34.19   10992   10.97   3292    163894892       xz -c -1 debug_info
56.63   34032   10.83   6296    164369948       xz -c -3 debug_info
149.35  97648   10.75   10400   149764760       xz -c -6 debug_info
2.55    12696   0.70    2916    252027101       zstd -fq --fast debug_info -o debug_info.o0
2.97    12528   0.83    2964    234661626       zstd -fq -1 debug_info -o debug_info.o0
3.95    41764   0.90    4568    215717860       zstd -fq -3 debug_info -o debug_info.o0
5.93    43960   0.91    4572    213222742       zstd -fq -5 debug_info -o debug_info.o0
9.96    90436   0.89    6668    208886078       zstd -fq -9 debug_info -o debug_info.o0
110.59  198708  1.46    10588   178996922       zstd -fq -18 debug_info -o debug_info.o0
% numactl -C 20 ./bench.sh debug_str
comp    RSS     decomp  RSS     size    command
5.19    2552    0.68    2204    41086567        pigz -zfk -p 1 -S .o0 debug_str
0.75    3680    0.50    19156   45784253        brotli -f -q 1 debug_str -o debug_str.o0
1.58    36320   0.42    19116   37832846        brotli -f -q 3 debug_str -o debug_str.o0
4.05    52508   0.38    20012   30553722        brotli -f -q 5 debug_str -o debug_str.o0
18.87   80704   0.34    19924   24386096        brotli -f -q 9 debug_str -o debug_str.o0
16.70   2416    4.67    1600    37520606        bzip2 -cf -1 debug_str
16.96   3736    4.82    2392    31299002        bzip2 -cf -3 debug_str
2.46    1968    0.03    2528    52866269        gzip -fk -S .o0 -1 debug_str
2.89    1996    0.03    2560    48526083        gzip -fk -S .o0 -3 debug_str
0.52    6776    0.23    6944    68238485        lz4 -fq --fast debug_str debug_str.o0
0.53    6644    0.23    7004    65392601        lz4 -fq -1 debug_str debug_str.o0
1.86    6540    0.23    6596    47813656        lz4 -fq -3 debug_str debug_str.o0
2.70    6636    0.23    6528    46341752        lz4 -fq -5 debug_str debug_str.o0
4.92    6568    0.23    6684    45862077        lz4 -fq -9 debug_str debug_str.o0
0.56    2168    0.57    1672    71677076        lzop -f -1 debug_str -o debug_str.o0
0.56    2128    0.57    1604    71133429        lzop -f -3 debug_str -o debug_str.o0
15.73   2488    0.51    1812    47430843        lzop -f -9 debug_str -o debug_str.o0
6.87    4940    2.46    2496    38516552        xz -c -0 debug_str
7.46    10892   2.05    3256    33223964        xz -c -1 debug_str
17.02   34020   1.77    6280    29506364        xz -c -3 debug_str
68.33   97664   1.32    10396   21296880        xz -c -6 debug_str
1.14    11304   0.29    2920    50492121        zstd -fq --fast debug_str -o debug_str.o0
1.16    11096   0.29    3000    42965990        zstd -fq -1 debug_str -o debug_str.o0
1.26    37292   0.31    4512    37978434        zstd -fq -3 debug_str -o debug_str.o0
2.18    39716   0.30    4580    33960116        zstd -fq -5 debug_str -o debug_str.o0
3.87    82580   0.28    6312    29911833        zstd -fq -9 debug_str -o debug_str.o0
66.85   186704  0.28    10668   23900220        zstd -fq -18 debug_str -o debug_str.o0
% numactl -C 20 ./bench.sh debug_line
comp    RSS     decomp  RSS     size    command
5.08    2524    0.63    2200    45210969        pigz -zfk -p 1 -S .o0 debug_line
0.56    3800    0.48    19104   42533806        brotli -f -q 1 debug_line -o debug_line.o0
1.15    36304   0.36    19272   30144639        brotli -f -q 3 debug_line -o debug_line.o0
3.38    56988   0.31    20344   23170193        brotli -f -q 5 debug_line -o debug_line.o0
18.64   86040   0.30    20032   20805984        brotli -f -q 9 debug_line -o debug_line.o0
12.74   2348    3.93    1548    40423655        bzip2 -cf -1 debug_line
13.48   3940    3.93    2364    34569267        bzip2 -cf -3 debug_line
2.19    1992    0.03    2584    51136260        gzip -fk -S .o0 -1 debug_line
2.73    1988    0.03    2440    49092753        gzip -fk -S .o0 -3 debug_line
0.33    7436    0.16    7848    66771211        lz4 -fq --fast debug_line debug_line.o0
0.36    7556    0.16    7656    64913560        lz4 -fq -1 debug_line debug_line.o0
1.55    7204    0.16    7288    49279291        lz4 -fq -3 debug_line debug_line.o0
2.13    7172    0.16    7212    48268337        lz4 -fq -5 debug_line debug_line.o0
3.46    7168    0.16    7080    47963094        lz4 -fq -9 debug_line debug_line.o0
0.42    2164    0.39    1636    67304513        lzop -f -1 debug_line -o debug_line.o0
0.42    2040    0.39    1672    66569062        lzop -f -3 debug_line -o debug_line.o0
24.08   2512    0.40    1704    47788969        lzop -f -9 debug_line -o debug_line.o0
5.44    4884    2.07    2544    31059860        xz -c -0 debug_line
5.71    10980   1.61    3272    24860272        xz -c -1 debug_line
12.29   33944   1.37    6344    21432224        xz -c -3 debug_line
45.04   97644   1.27    10480   18536212        xz -c -6 debug_line
0.67    11688   0.20    2940    50842109        zstd -fq --fast debug_line -o debug_line.o0
0.73    11400   0.21    3012    38849471        zstd -fq -1 debug_line -o debug_line.o0
0.87    37992   0.22    4544    28827098        zstd -fq -3 debug_line -o debug_line.o0
1.30    40180   0.22    4552    26554847        zstd -fq -5 debug_line -o debug_line.o0
2.34    83552   0.21    6624    23464249        zstd -fq -9 debug_line -o debug_line.o0
43.67   188676  0.22    10584   20195067        zstd -fq -18 debug_line -o debug_line.o0
```

在压缩调试段时，zstd 和 brotli 明显优于其他选择。zstd 在压缩速度和压缩比上略优于 brotli，同时解压速度更快。

`xz -3` 具有很好的压缩比（更高级别太慢）。zstd 和 brotli 在较高级别下极其缓慢，几乎无法达到 xz 的压缩比，但它们的解压速度可能弥补这一点。

zlib（由 pigz 使用）和 bzip2 看起来相当糟糕。

对于 zstd，内置的并行压缩支持是一个加分项。
