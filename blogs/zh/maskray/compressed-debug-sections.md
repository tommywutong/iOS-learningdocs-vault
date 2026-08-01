---
title: 压缩的调试段
source: MaskRay (宋方睿)
source_key: maskray
source_url: 'https://maskray.me/blog/2022-01-23-compressed-debug-sections'
original_language: en
published: 2022-01-23
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:0b58d229e1a6119a'
translated: true
---

> 原文：[Compressed debug sections](https://maskray.me/blog/2022-01-23-compressed-debug-sections)　·　MaskRay (宋方睿)

[2022-01-23](https://maskray.me/blog/2022-01-23-compressed-debug-sections)

# 压缩的调试段

更新于 2024-05。

二进制文件大小很重要。文件系统压缩虽然易用，但通常无法很好地利用应用层面的信息。压缩可分配段（text、data）会延长程序启动时间并增加内存开销。此外，文件系统压缩的可移植性也不够好。

调试段体积庞大，占二进制文件大小的很大一部分。因此，压缩调试段很有吸引力。

下面的数据来自一个刚运行过 `ninja clang` 的 llvm-project `-DCMAKE_BUILD_TYPE=Debug` 构建目录（2022-10-21）。这里分别统计 `.o` 文件、text 节和调试节的总大小。调试信息通常远大于 text 节，这是很典型的情况。

```text
% stat -c %s **/*.o | awk '{s+=$1} END{print s}'
1464767464
% readelf -WS **/*.o | awk 'BEGIN{FPAT="\\[.*?\\]|\\S+"} $2~/\.text/{d += strtonum("0x"$6)} END{print d}'
210026370
% readelf -WS **/*.o | awk 'BEGIN{FPAT="\\[.*?\\]|\\S+"} $2~/\.debug_/{d += strtonum("0x"$6)} END{print d}'
631069751
% readelf -WS **/*.o | awk 'BEGIN{FPAT="\\[.*?\\]|\\S+"} $2~/\.rela\.debug_/{d += strtonum("0x"$6)} END{print d}'
78448968
```

一些汇编器和链接器提供了压缩调试段的功能。

llvm-objcopy 支持 `--compress-debug-sections=zlib` 来压缩调试段。我们可以使用该选项来检查如果为汇编器压缩调试段会如何。
1  
2  
% for i in **/*.o; do /tmp/Rel/bin/llvm-objcopy --compress-debug-sections=zlib $i /tmp/c/o && readelf -WS /tmp/c/o | awk 'BEGIN{FPAT="\\\\[.*?\\\\]|\\\\S+"} $2~/\\.debug_/{d += strtonum("0x"$6)} END{print d}'; done | awk '{s+=$1} END{print s}'  
161691798

对于调试段，我们得到了 3.90 的压缩比！.o 文件总大小为 995438992 字节，是原来的 68%。

接下来试试 zstd。
1  
2  
% for i in **/*.o; do /tmp/Rel/bin/llvm-objcopy --compress-debug-sections=zstd $i /tmp/c/o && readelf -WS /tmp/c/o | awk 'BEGIN{FPAT="\\\\[.*?\\\\]|\\\\S+"} $2~/\\.debug_/{d += strtonum("0x"$6)} END{print d}'; done | awk '{s+=$1} END{print s}'  
159341878

要检查目标文件是否有压缩的调试段，我们可以使用 `readelf`。

```plaintext
% readelf -S a.o
...
Section Headers:
  [Nr] Name              Type            Address          Off    Size   ES Flg Lk Inf Al
...
  [ 5] .debug_abbrev     PROGBITS        0000000000000000 000080 000087 00   C  0   0  8
```

在 `readelf -S` 输出中，`Flg` 列描述了 `sh_flags`，其中 `C` 表示 `SHF_COMPRESSED` 标志。

```plaintext
% readelf -t a.o
...
Section Headers:
  [Nr] Name
       Type            Address          Off    Size   ES   Lk Inf Al
       Flags
...
  [ 5] .debug_abbrev
       PROGBITS        0000000000000000 000080 000087 00   0   0  8
       [0000000000000800]: COMPRESSED
       ZLIB, 0000000000000093, 1
```

## 历史

2007-11，Craig Silverstein [向 gold 添加了 `--compress-debug-sections=zlib`](https://sourceware.org/git/?p=binutils-gdb.git;a=commit;h=9a0910c33e1a6962d475ee0a994fd1f5e446a888)。指定该选项时，gold 会用 zlib 压缩 `.debug*` 段的内容，并将段名称改为 `.debug*.zlib.$uncompressed_size`。

2008-04，Craig Silverstein [更改了格式](https://sourceware.org/pipermail/binutils/2008-April/055837.html)并向 gdb 贡献了 [处理压缩段的补丁](https://sourceware.org/pipermail/gdb-patches/2008-March/056449.html)。压缩段被重命名为 `.zdebug*`。

2010-06，Cary Coutant [向 gas 添加了 `--compress-debug-sections`](https://sourceware.org/pipermail/binutils/2010-June/067606.html)，并为 objdump 和 readelf 添加了读取支持。

[ELF 节压缩](http://www.linker-aliens.org/blogs/ali/entry/elf_section_compression/) 对 `.zdebug` 格式做了很好的总结。文章列出了该格式的一些问题；2012 年由通用 ELF ABI 标准化的新格式解决了这些问题。我建议对 ELF 格式感兴趣的人阅读这篇文章。我实现 ELF 特性的思路深受这类文章以及通用 ABI 邮件列表中其他讨论的影响。

在 Solaris 11.2 中，其链接器引入了 `-z compress-sections` 来压缩候选段。

通用 ABI 格式导致了对 binutils 中现有汇编器和链接器选项的修改。2015-04，H.J. Lu [向 gas 添加了 `--compress-debug-sections=[none|zlib|zlib-gnu|zlib-gabi]`](https://sourceware.org/pipermail/binutils/2015-April/088496.html) 并[向 GNU ld 添加了 `--compress-debug-sections=[none|zlib|zlib-gnu|zlib-gabi]`](https://sourceware.org/pipermail/binutils/2015-April/088607.html)。2015-07，H.J. Lu [向 gold 添加了 `--compress-debug-sections=[none|zlib|zlib-gnu|zlib-gabi]`](https://sourceware.org/bugzilla/show_bug.cgi?id=18322)。`zlib` 和 `zlib-gnu` 指示 `.zdebug` 格式，而 `zlib-gabi` 指示通用 ABI 格式。

2015-07，[[PATCH] Make default compression gABI compliant](https://sourceware.org/pipermail/binutils/2015-July/089559.html)（里程碑：binutils 2.26）更改了 `zlib` 以指示通用 ABI 格式。

汇编器和链接器的 `--compress-debug-sections=` 选项又长又难用。2014-06，Rainer Orth [向 GCC 添加了 `-gz` 和 `-gz=[none|zlib|zlib-gnu]`](https://sourceware.org/pipermail/gcc-patches/2014-June/390257.html)。

2022 年，我向 generic-abi 提交的 `ELFCOMPRESS_ZSTD` 提案获得接受。参见 [zstd 压缩调试节](https://maskray.me/blog/2022-09-09-zstd-compressed-debug-sections)。

## `.zdebug` 残存问题

Go 1.11 默认启用了 `.zdebug`。我意识到 Go 仍在用旧格式后，提交了 [https://github.com/golang/go/issues/50796](https://github.com/golang/go/issues/50796)。Meng Zhuo 在 2022-03 将其迁移了出去。

## 用法

要使用压缩的调试段，只需记住一个 GCC/Clang 驱动选项 `-gz`（或其变体 `-gz=zlib`）。该选项结合了两个任务。

### 汇编

```text
% clang -c -g -gz a.c
% clang -c -g -gz=zlib a.c
```

对于目标文件生成，`-gz=zlib` 充当 `-Wa,--compress-debug-sections=zlib`，要求汇编器压缩输出 `.o` 中的调试段（以及指定 `-gsplit-dwarf` 时的 `.dwo`）。压缩段具有 `SHF_COMPRESSED` 标志，其内容以标识压缩算法的压缩头部结构开始。
1  
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
typedef struct {  
 Elf32_Word ch_type;  
 Elf32_Word ch_size;  
 Elf32_Word ch_addralign;  
} Elf32_Chdr;  
  
typedef struct {  
 Elf64_Word ch_type;  
 Elf64_Word ch_reserved;  
 Elf64_Xword ch_size;  
 Elf64_Xword ch_addralign;  
} Elf64_Chdr;

截至 2022 年，只定义了 `ELFCOMPRESS_ZLIB` 和 `ELFCOMPRESS_ZSTD`：

> ELFCOMPRESS_ZLIB - 段数据使用 ZLIB 算法压缩。压缩后的 ZLIB 数据字节从紧跟压缩头部后的字节开始，一直延伸到段末尾。有关 ZLIB 的更多文档，请访问 http://zlib.net。
>  
> ELFCOMPRESS_ZSTD - 段数据使用 Zstandard 算法压缩。压缩后的 Zstandard 数据字节从紧跟压缩头部后的字节开始，一直延伸到段末尾。有关 Zstandard 的更多文档，请访问 http://www.zstandard.org

```text
% clang -c -g -gz a.c
% clang -c -g -gz=zlib a.c
```

请注意，`-gz` 并不意味着生成调试信息，这由 `-g` 控制。因此通常你需要同时使用 `-g -gz`。这种特性正交性在只需要一部分目标文件选择不生成调试信息时很方便。

### 链接

```text
% clang -gz a.o
% clang -gz=zlib a.o
```

对于链接，`-gz` 充当 `-Wl,--compress-debug-sections=zlib`，要求链接器压缩链接后镜像中的调试段。如果你只需要解压缩链接器输入，而不需要压缩链接器输出，则不必使用 `-gz`。链接器能识别压缩输入并自动解压缩。

如果你将汇编和链接合并为一步（`gcc -g -gz a.c`，不使用 `-S` 或 `-c`），你可能不想使用 `-gz`。中间的 `.o` 文件会被丢弃。汇编器压缩的调试段会立即被链接器解压缩，造成浪费。

binutils 和 GCC 支持 `zlib-gabi`。这是为了对应重命名的旧格式 `zlib-gnu` 而添加的。现在只需使用 `zlib`，避免 `zlib-gabi`。ELF 压缩已经标准化，新格式（如 zstd）不使用 `-gabi`。

## 评估

我测试了两个 `-DCMAKE_BUILD_TYPE=Debug` 的 clang 构建。`clang.dw4` 是未压缩的 DWARF v4 构建，而 `clang.dw5` 是未压缩的 DWARF v5 构建。`objcopy --compress-debug-sections` 压缩 `.debug*` 段。效果等同于使用 `--compress-debug-sections=zlib` 调用链接器。

```text
% objcopy --compress-debug-sections clang.dw4 clang.dw4.compressed
% objcopy --compress-debug-sections clang.dw5 clang.dw5.compressed
% bloaty clang.dw4.compressed -- clang.dw4
...
 -89.7%  -572Ki  [ = ]       0    .debug_loc
 -80.2% -3.33Mi  [ = ]       0    .debug_abbrev
 -92.6% -35.3Mi  [ = ]       0    .debug_ranges
 -72.9% -92.3Mi  [ = ]       0    .debug_line
 -84.2%  -175Mi  [ = ]       0    .debug_str
 -57.7%  -221Mi  [ = ]       0    .debug_info

% bloaty clang.dw5.compressed -- clang.dw5
...
 -69.8%    -572  [ = ]       0    .debug_ranges
 -63.4%  -134Ki  [ = ]       0    .debug_loclists
 -81.8%  -162Ki  [ = ]       0    .debug_line_str
 -32.2% -3.27Mi  [ = ]       0    .debug_rnglists
 -78.4% -4.49Mi  [ = ]       0    .debug_abbrev
 -33.2% -16.7Mi  [ = ]       0    .debug_str_offsets
 -88.8% -19.2Mi  [ = ]       0    .debug_addr
 -72.9% -89.8Mi  [ = ]       0    .debug_line
 -84.2%  -175Mi  [ = ]       0    .debug_str
 -55.9%  -177Mi  [ = ]       0    .debug_info
```

关于压缩比，有一些有趣的点。

- `.debug_str` 是一个字符串表。它主要由标识符字符组成，压缩效果非常好。
- DWARF v5 之前的 `.debug_loc` 和 `.debug_ranges` 压缩效果很好，因为它们的编码相对低效。
- 压缩后的 `.debug_rnglists` 比压缩后的 `.debug_ranges` 更大。`.debug_rnglists` 使用手动优化的面向字节的编码，这里没有 LZ77 :)
- `.debug_info` 的压缩效果不好。这可能还不算太糟，因为其原始编码已经很紧凑了。

`-gsplit-dwarf{,=split}` 将 `.debug_{abbrev,info,loclists,rnglists,str,str_offsets}`（以及 DWARF v5 之前的 `.debug_loc`）的大部分内容移到 `.dwo` 文件中。对于不使用 `.dwo` 文件的符号化，大量 `.debug_line` 仍保留在 `.o` 文件中，因此 `-gz` 依然有用。

## 对齐

通用 ABI 规定：

> 压缩段的段头中 sh_size 和 sh_addralign 字段反映了压缩段的要求。

一种严格的解释是，对于 ELFCLASS64，压缩的 `.debug_*` 段应有 8 字节对齐。BFD 使用 8 字节对齐，而 gold/lld/mold 使用 1 字节对齐。我不知道 Solaris 链接器如何设置对齐。

看起来 1 字节对齐已经被广泛接受并使用了很长时间。当有许多压缩输出段时，移除对齐填充尤其有用。

## 压缩更多段

2021-02，我提交了功能请求 [ld：支持压缩任意节（泛化 `--compress-debug-sections=`）](https://sourceware.org/bugzilla/show_bug.cgi?id=27452)，但它还没有直接的使用场景。

## 利弊

好处是明显的：压缩减少了可重定位目标文件和/或链接后镜像的大小。

压缩在开发的许多阶段都会带来内存使用上的开销。汇编器、链接器和调试器需要分配额外内存来存放压缩或未压缩的数据。

对于目标文件生成，性能取决于环境。一方面，压缩做了更多工作，并为链接器带来了解压缩工作。另一方面，压缩后的数据更小，所以 I/O 更快。我测试了一些 C++ 源文件。编译器的其他阶段占主导地位，`-gz` 似乎对编译时间影响甚微。

对于链接，压缩可能会大大增加链接时间。在一个项目中，一个 `.o` 文件的内容可能会进入多个链接后镜像。同一数据可能被多次压缩，但几乎不可能复用压缩结果，因为每个链接后镜像在重定位后的内容都不同。

此外，压缩的调试段可能会使调试器显著变慢。gdb 和 lldb 都不会并行解压缩调试段。

如果你关心文件大小，并且很少进行调试，那么链接后镜像中的压缩调试段可能是不错的选择。

## 链接器

zlib 使用 DEFLATE 压缩数据格式，它不是为并行解压缩设计的。幸运的是，链接器不需要处理这个任务，因为解压缩输入段是高度可并行的。

然而，压缩输入段是一个主要的瓶颈。我测试了一个包含 265MiB `SHF_ALLOC` 段和 920MiB 未压缩调试段的 `-DCMAKE_BUILD_TYPE=Debug` clang 构建。如果我在 `--threads=1` 链接中指定 `--compress-debug-sections=zlib`，"Compress debug sections" 阶段会占用 2/3 的时间。在 `--threads=8` 链接中，"Compress debug sections" 阶段会占用近 70% 的时间。

我们基本上有四个选择来改善这种情况。

- 调整 zlib 参数
- 替代压缩格式
- 更优化的库
- 并行分治

第一个已经完成（[D70658](https://reviews.llvm.org/D70658)）。ld.lld 切换为对 `-O1`（默认）和 `-O0` 使用压缩级别 1（`Z_BEST_SPEED`）。先前的默认值（6）已知在花费过多时间的同时，尺寸减少并不明显。从 lld 19 开始，[zlib 的默认压缩级别](https://github.com/llvm/llvm-project/pull/90567)是 `Z_BEST_SPEED`，与 `-O` 选项无关。

关于第二个选择：使用更好的格式是一个生态系统问题，需要大量投入和利益相关者的支持。zstd 在所有指标上（压缩速度、解压缩速度和压缩比）都优于 zlib。然而，它当时尚未标准化（通用 ABI 指定的唯一标志是 `ELFCOMPRESS_ZLIB`）。它也没有调试生产者/消费者支持。

第三个选择对于像 lld 这样的链接器来说很困难。将库导入到 llvm-project 有很高的门槛。新的 CMake 配置的可发现性很差，并且只惠及少数群体。libdeflate 高效且似乎做得不错，但我不知道如何证明将其导入 llvm-project 是合理的。

第四个选择是可行的。Rui Ueyama 告诉我，mold 通过分片（sharding）来优化 `--compress-debug-sections=zlib`。我做了一些研究。pigz 有一个很好的注释解释了它如何利用多线程：[https://github.com/madler/pigz/blob/master/pigz.c](https://github.com/madler/pigz/blob/master/pigz.c)。它有一些链接器可能不需要的复杂特性：

- 除非指定了 `-i`，否则前一块的最后 32KiB（窗口大小）会用作字典（`deflateSetDictionary`）以改善压缩比。
- 即使没有 `--rsyncable`，也存在同步标记。

我提交了 [[ELF] 并行化 `--compress-debug-sections=zlib`](https://reviews.llvm.org/D117853)（里程碑：LLD 14.0.0）来改进 ld.lld 的算法。采用分治方法时，需要拼接压缩流，并添加 zlib 头和尾部校验和。根据 [RFC1950](https://datatracker.ietf.org/doc/html/rfc1950)，zlib 流具有以下结构。我们不使用预置字典，因此省略了 2 字节头之后的一个字段。

```text
byte 0: CMF
byte 1: FLG
compressed data
last 4 bytes: Alder-32 checksum
```

压缩数据使用 DEFLATE 压缩数据格式（RFC1951）编码。它由多个分片（shard）组成。
1  
2  
3  
4  
shard 0: blocks produced by deflate(&strm0, Z_SYNC_FLUSH)  
shard 1: blocks produced by deflate(&strm1, Z_SYNC_FLUSH)  
...  
last shard: blocks produced by deflate(&strmN_1, Z_FINISH)

DEFLATE 块是比特序列。我们需要确保每个分片从字节边界开始，以便进行拼接。我们对除最后一个之外的所有分片使用 `Z_SYNC_FLUSH`，以便将输出刷新到字节边界。（也可以使用 `Z_FULL_FLUSH`，但 `Z_FULL_FLUSH` 会清除哈希表，这只会浪费时间。）

最后一个块需要 BFINAL 标志。我们使用 `Z_FINISH` 调用 `deflate` 来设置该标志并将输出刷新到字节边界。在底层，`Z_SYNC_FLUSH`、`Z_FULL_FLUSH` 和 `Z_FINISH` 都会发出一个非压缩块（在 zlib 中称为存储块）。RFC1951 说“任何输入中直到下一个字节边界的比特位都会被忽略。”

在压缩数据之后，zlib 流的最后 4 个字节是 Adler-32 校验和。`adler32_combine` 可以合并两个 Adler-32 校验和，即 `adler32_combine(adler32(A), adler32(B)) = adler32(cat(A, B))`。

最后一步是并行写入 DEFLATE 块。

我们还能做得更好吗？同一时刻，压缩数据会存放在两个位置：一份位于保存压缩分片的已分配内存中，另一份位于内存映射的输出文件中。若能避免这次内存分配会更好。遗憾的是，我们必须先计算节大小，否则无法确定后续节和节头表（通常位于最后一个节之后）的偏移量；而不实际压缩就没有好办法估算压缩节大小。理论上，可以把节头表及 `.symtab`/`.shstrtab`/`.strtab` 移到调试节之前，再压缩调试节并将其追加到输出文件。但这样的输出文件不合常规，而且链接器脚本明确指定节顺序时也无法使用这种方法。

```text
SECTIONS {
  ...
  .debug_info 0 : { *(.debug_info) }
  .strtab 0 : { *(.strtab) }
```

仅为节省少量内存而做这么多特殊处理并不值得。此外，把 `.symtab`、`.shstrtab`、`.strtab` 和节头表放在文件末尾还有一个优点：如果优化后的 strip 程序只执行符号相关操作，它只需修改这些字节，不过我不知道是否有 strip 程序利用了这一特性。

我就使用并行实现的事 [通知了 binutils](https://sourceware.org/bugzilla/show_bug.cgi?id=28812)。dwp 打包多个 `.dwo` 文件并执行类似链接器的任务。dwp 尚不支持 `--compress-debug-sections`，但我不知道是否有人有这种需求。

[dwz](https://sourceware.org/dwz/) 是一个 DWARF 优化和去重工具。有一个关于[添加 `--compress-debug-sections`](https://sourceware.org/bugzilla/show_bug.cgi?id=24822) 的功能请求。

## binutils 配置

`--enable-compressed-debug-sections=all` 将 gas 和 ld 的默认值更改为 `--compress-debug-sections=zlib`。

### 更多想法

问：对于压缩输入和未压缩输出，我们能避免存放未压缩输出的临时缓冲区吗？

这是可能的，但在解析重定位时会遇到困难。我的估计是，避免临时缓冲区可能不会带来显著的加速或内存节省。

问：对于压缩输入和压缩输出，我们能否不对其数据重新压缩？

答案是在没有重定位的情况下是可以的，但改动很复杂，并且可能不是划算的交换。zlib 提供了 [examples/gzjoin.c](https://github.com/madler/zlib/blob/master/examples/gzjoin.c)，它可以拼接多个 gzip 流（gzip 也使用 DEFLATE）而无需重新压缩。它需要解压缩输入以定位每个输入流中的最后一个块。如果链接器利用此优化：

- 它需要移植涉及的代码
- 它需要保留压缩数据。这在 ld.lld 中很困难，因为像 `--gdb-index` 这样的特性会将 `InputSection` 成员（最初指向压缩数据）更新为指向未压缩数据。保留两者需要在段表示中增加一个额外成员，从而增加内存使用。

问：如果存储系统提供内置压缩，调试段压缩还有用吗？

这样的比较会很有用。我还没听说有人做过定量比较。

存储系统可以进行压缩，但应用通常能做出更好的决策。

- 文件传输开销：存储系统可能需要多次压缩或解压缩数据，可能比工具链压缩消耗更多的 CPU 资源。
- 效率：工具链可以将压缩与其他任务交织进行，从而更好地利用 CPU。特别是，链接器可以利用并行性，并将压缩与其他阶段交织。
- 更明智的决策：工具链级别的压缩可以访问关于被压缩数据的更多上下文信息（调试信息 vs 代码/数据、构建配置等），从而允许更好的压缩策略。
- 计费目的：分布式构建系统可能对未压缩的输入大小设置限制。使这些系统适应计算压缩输入可能需要大量修改，且可行性不确定。
