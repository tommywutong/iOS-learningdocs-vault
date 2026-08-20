---
title: 链接器中的分析与自省选项
source: MaskRay (宋方睿)
source_key: maskray
source_url: 'https://maskray.me/blog/2022-02-27-analysis-and-introspection-options-in-linkers'
original_language: en
published: 2022-02-27
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:db08dcffbe789334'
translated: true
---

> 原文：[链接器中的分析与自省选项](https://maskray.me/blog/2022-02-27-analysis-and-introspection-options-in-linkers)　·　MaskRay（宋方睿）

[2022-02-27](https://maskray.me/blog/2022-02-27-analysis-and-introspection-options-in-linkers)

# 链接器中的分析与自省选项

更新于 2026 年 1 月。

## 复现用 tarball

LLD 提供了一个便捷的功能，可将所有输入文件打包成一个 tarball，从而更方便地试验不同的链接器选项。可以使用以下任一命令：

```sh
clang -fuse-ld=lld -Wl,--reproduce=/tmp/rep.tar a.o b.o
LLD_REPRODUCE=/tmp/rep.tar clang -fuse-ld=lld a.o b.o
```

然后解压 tarball，进入该目录，并使用响应文件调用 LLD：

```sh
cd /tmp; tar xf rep.tar; cd rep
ld.lld @response.txt # append options like -y foo
```

响应文件中包含 `--chroot` 选项，GNU ld 不支持该选项。大多数情况下，你可以直接移除这个选项，以检查GNU ld 的行为。

```sh
ld.bfd @response.txt
```

### `--trace-symbol=<sym>`

别名：`-y sym`

打印定义或引用了指定非局部符号的文件。定义分为三种类型：可重定位目标文件中的定义、共享对象中的定义、延迟加载的目标文件/归档文件中的定义。

```text
% ld.lld -y foo a1.a a.o a2.so
a1.a(a1.o): lazy definition of foo
a.o: reference to foo
a1.a(a1.o): definition of foo
a2.so: shared definition of foo
```

### `--trace`

别名：`-t`

打印已处理的文件：可重定位目标文件、共享对象，以及已提取的延迟加载目标文件和归档文件成员。注意，未提取的延迟加载目标文件和归档文件成员不会被打印。

GNU ld 的行为有点奇怪。你需要指定`-t`两次，才能同时获取归档文件名和成员名。

```text
% ld.lld -t a.o b.so c.a
a.o
b.so
c.a(1.o)
% ld.bfd -t a.o b.so c.a
a.o
b.so
c.a
% ld.bfd -t -t a.o b.so c.a
a.o
b.so
(c.a)1.o
```

### `--print-archive-stats=<file>`

gold 在 2008 年 6 月引入了 `--print-symbol-counts=<file>`。其输出包括每个归档文件的成员计数和已提取成员计数。我为`--print-archive-stats=<file>` ld.lld，用于转存归档信息，但格式为制表符分隔。

```text
% ld.lld a.o aweak.a a1.a a1.a --print-archive-stats=-
members extracted       archive
1       0       aweak.a
3       2       a1.a
3       0       a1.a
```

### `--why-extract=<file>`

打印每个归档成员/延迟加载目标文件被提取的原因。我在 ld.lld 14 中添加了这个选项。输出格式为制表符分隔。

```text
% ld.lld main.o a_b.a b_c.a c.a -o /dev/null --why-extract=- | tee stdout
reference       extracted       symbol
main.o  a_b.a(a_b.o)    a
a_b.a(a_b.o)    b_c.a(b_c.o)    b()
b_c.a(b_c.o)    c.a(c.o)        c()
```

追踪指向某个归档成员的引用链很容易：1  
2  
3  
4  
% ruby -ane 'BEGIN{p={}}; p[$F[1]]=[$F[0],$F[2]] if $.\>1; END{x="c.a(c.o)"; while y=p[x]; puts "#{y[0]} extracts #{x} to resolve #{y[1]}"; x=y[0] end}' stdout  
b_c.a(b_c.o) extracts c.a(c.o) to resolve c()  
a_b.a(a_b.o) extracts b_c.a(b_c.o) to resolve b()  
main.o extracts a_b.a(a_b.o) to resolve a

ld64 有一个类似的选项，名为 `-why_load`.

## `-Map=<file>`

将链接映射（link map）打印到文件。若要打印到 stdout，请使用 `-M`.

输出包括输出段地址、文件偏移量、输入段到输出段的映射以及符号分配。

GNU ld 会打印额外信息：`Archive member included to satisfy reference by file (symbol)`, `Discarded input sections`（类似于 `--print-gc-sections`), `Allocating common symbols`, `Memory Configuration`（与内存区域相关），以及`Linker script and memory map`（类似于 `-t`).

如果选项值是一个目录或包含 `%`的名称，则映射文件名将从输出文件名构造。1  
2  
3  
4  
5  
6  
7  
8  
9  
10  
-o foo.exe -Map=bar[创建 ./bar]  
-o ../dir/foo.exe -Map=bar[创建 ./bar]  
-o foo.exe -Map=../dir[创建 ../dir/foo.exe.map]  
-o ../dir2/foo.exe -Map=../dir[创建 ../dir/foo.exe.map]  
-o foo.exe -Map=% [创建 ./foo.exe.map]  
-o ../dir/foo.exe -Map=% [创建 ../dir/foo.exe.map]  
-o foo.exe -Map=%.bar [创建 ./foo.exe.bar]  
-o ../dir/foo.exe -Map=%.bar [创建 ../dir/foo.exe.bar]  
-o ../dir2/foo.exe -Map=../dir/% [创建 ../dir/../dir2/foo.exe.map]  
-o ../dir2/foo.exe -Map=../dir/%.bar [创建 ../dir/../dir2/foo.exe.bar]

有些人希望具备一定稳定性保障的 JSON 输出格式。

## 交叉引用

### `--cref`

打印交叉引用表。对于每个已定义或共享的非局部符号，在第一行打印定义该符号的文件，在后续行打印引用该符号的文件。这种格式有点浪费，因为在 `File` 列之前有 50 个字节。

```text
% ld.lld --cref a1.so a2.o a3.o a.a

Cross Reference Table

Symbol                                            File
foo                                               a1.so
                                                  a2.o
                                                  a3.o
bar                                               a2.o
                                                  a3.o
_start                                            a3.o
baz                                               a3.o
zed                                               a.a(aa.o)
                                                  a3.o
```

如果指定了 `-Map`，会一并打印到链接映射（link map）文件中。我觉得这种行为有点不妥，因为：

- 该信息独立于 `-Map`
- 两者都产生大量输出。如果用户只需要其中一种信息，将它们合并会使链接操作变慢

### `--print-dependencies`

mold 最近以另一种格式添加了该选项到 `--cref`.

```text
# This is an output of the mold linker's --print-dependencies=full option.
#
# Each line consists of 4 fields, <input-section>, <output-section>,
# <symbol-type> and <symbol>, separated by tab characters. It indicates that
# <input-section> depends on <output-section> to use <symbol>. <symbol-type>
# is either "u" or "w" for regular or weak undefined, respectively.
#
# If you want to obtain dependency information per function granularity,
# compile source files with the -ffunction-sections compiler flag.
a3.o:(.text)    a1.so   u       foo
a3.o:(.text)    a2.o:(.text)    u       bar
a3.o:(.text)    a.a(aa.o):(.text)       u       zed
```

### `-why_live sym`

ld64 的手册页说明：`Logs a chain of references to symbol_name.  Only applicable with -dead_strip .  It can help debug why something that you think should be dead strip removed is not removed.`

这通常可以近似地用 `ld.lld --why-extract=-`.

```plaintext
% ld.lld main.o a_b.a b_c.a c.a -o /dev/null --why-extract=- | tee stdout
reference       extracted       symbol
main.o  a_b.a(a_b.o)    a
a_b.a(a_b.o)    b_c.a(b_c.o)    b()
b_c.a(b_c.o)    c.a(c.o)        c()

% ruby -ane 'BEGIN{p={}}; p[$F[1]]=[$F[0],$F[2]] if $.>1; END{x="c.a(c.o)"; while y=p[x]; puts "#{y[0]} extracts #{x} to resolve #{y[1]}"; x=y[0] end}' stdout
b_c.a(b_c.o) extracts c.a(c.o) to resolve c()
a_b.a(a_b.o) extracts b_c.a(b_c.o) to resolve b()
main.o extracts a_b.a(a_b.o) to resolve a
```

[GNU ld 功能请求](https://sourceware.org/bugzilla/show_bug.cgi?id=32720)

### `--why-live=<sym>`

LLD的 ELF 端口已在 [2025 年 3 月](https://github.com/llvm/llvm-project/pull/127112).

## 统计

### `--stats`

```text
% ld.bfd @response.txt --stats
ld.bfd: total time in link: 9.879890
% mold @response.txt --stats
   total_input_bytes=1161772844
         reloc_alloc=3983368
            all_syms=1185762
        defined_syms=747420
      input_sections=692453
      undefined_syms=397776
    regular_sections=319069
      merged_strings=214750
            num_fdes=169858
  removed_comdat_mem=140402
             comdats=131977
            dso_syms=10875
         parsed_objs=3099
            num_objs=2677
            num_cies=2665
       output_chunks=36
            num_dsos=10
     num_unique_cies=2
    string_fragments=0
      reloc_nonalloc=0
.rodata.cst estimation=5425 actual=4689
.rodata.str estimation=240124 actual=210057
.comment estimation=1628 actual=4
```

### `--time-trace`

```text
% ld.lld @response.txt --time-trace -o clang
% jq -r '.traceEvents[] | select(.name|contains("Total")) | "\(.dur/1000000) \(.name)"' < clang.time-trace
1.099133 Total ExecuteLinker
1.064616 Total Link
0.303137 Total Write output file
0.295151 Total Write sections
0.220898 Total Scan relocations
0.183298 Total Parse input files
0.06039 Total Merge/finalize input sections
0.0377 Total Add local symbols
...
% jq -r '.traceEvents[] | select(.name|contains("Write")) | "\(.dur/1000000) \(.name) \(.args)"' < clang.time-trace
0.130966 Write sections {"detail":".rela.dyn"}
0.001995 Write sections {"detail":".rela.plt"}
0.007248 Write sections {"detail":".dynsym"}
0.000967 Write sections {"detail":".gnu.hash"}
0.01489 Write sections {"detail":".hash"}
0.003147 Write sections {"detail":".dynstr"}
0.034617 Write sections {"detail":".rodata"}
0.030412 Write sections {"detail":".eh_frame"}
0.02487 Write sections {"detail":".text"}
...
```

### `/summary`

`lld-link /summary` 会转存 PDB 信息和所有输入 OBJ 文件的累积大小。

### `mold --perf`

```text
% mold @response.txt --perf
     User   System     Real  Name
    4.161    0.533    0.254  all
    2.077    0.302    0.139    read_input_files
    2.100    0.235    0.114    total
    1.537    0.129    0.071      before_copy
    0.000    0.000    0.000        apply_exclude_libs
    0.142    0.051    0.007        do_resolve_symbols
    0.142    0.051    0.007          do_resolve_symbols
    0.245    0.012    0.013        register_section_pieces
    0.002    0.000    0.001        eliminate_comdats
    0.002    0.000    0.000        convert_common_symbols
...
```
