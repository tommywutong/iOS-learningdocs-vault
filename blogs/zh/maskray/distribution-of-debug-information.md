---
title: 调试信息的分布
source: MaskRay (宋方睿)
source_key: maskray
source_url: 'https://maskray.me/blog/2022-10-30-distribution-of-debug-information'
original_language: en
published: 2022-10-30
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:bd50a96da31959f0'
translated: true
---

> [调试信息的分布](https://maskray.me/blog/2022-10-30-distribution-of-debug-information)

[2022-10-30](https://maskray.me/blog/2022-10-30-distribution-of-debug-information)

# 调试信息的分布

2024 年 8 月更新。

注意：该文章可能会在接下来几天内频繁更新。

本文描述了一些分发调试信息的方法。下面的命令将使用两个简单的 C 文件进行演示。

```sh
cat > a.c <<eof
void foo(int);
int main() { foo(42); }
eof
cat > b.c <<eof
#include <stdio.h>
void foo(int x) { printf("%d\n", x); }
eof
```

这是最简单的模型。调试信息位于可执行文件或共享对象中。

```sh
gcc -c -g a.c b.c
gcc a.o b.o -o a
```

链接器收集输入的调试段，解析重定位，进行最小化合并（`SHF_STRING` 合并 `.debug_str` 和 `.debug_line_str`），并将它们组合成输出的调试段。

```text
 0                0       a7     1 .debug_abbrev
 0                0       38     1         a.o:(.debug_abbrev)
38               38       6f     1         b.o:(.debug_abbrev)
 0                0       94     1 .debug_info
 0                0       37     1         a.o:(.debug_info)
37               37       5d     1         b.o:(.debug_info)
 0                0       44     1 .debug_str_offsets
 0                0       1c     1         a.o:(.debug_str_offsets)
1c               1c       28     1         b.o:(.debug_str_offsets)
 0                0       c1     1 .debug_str
 0                0       c1     1         <internal>:(.debug_str)
 0                0       28     1 .debug_addr
 0                0       10     1         a.o:(.debug_addr)
10               10       18     1         b.o:(.debug_addr)
 0                0       bf     1 .debug_line
 0                0       5e     1         a.o:(.debug_line)
5e               5e       61     1         b.o:(.debug_line)
 0                0        f     1 .debug_line_str
 0                0        f     1         <internal>:(.debug_line_str)
```

## 单独的调试文件

调试信息体积很大，而且多数用户并不需要。作为一种常见的体积优化，许多发行版不会在主软件包中提供调试信息。为满足调试需求，发行版可以利用调试器支持独立调试文件的特性，在单独的软件包中提供调试信息。参见 [GDB 文档](https://sourceware.org/gdb/onlinedocs/gdb/Separate-Debug-Files.html)。

binutils-gdb 中的 objcopy 可以创建独立调试文件（自 2003 年起）。1  
2  
objcopy --only-keep-debug a a.debug  
strip -S a -o a.stripped

elfutils 中的 eu-strip 可以通过一次调用生成两个输出文件。1  
eu-strip -f a.debug a -o a.stripped

elfutils 的方式对简单用例很方便，rpm 也采用了这种方式。但它通常存在一个歧义：某项操作究竟应用于一个输出文件，还是两个文件都应用。`--only-keep-debug` 的方式与其他操作相互独立，也能很好地结合其他功能（例如 `--compress-debug-sections`、`--remove-section`）。我更喜欢 `--only-keep-debug`，并在 [D67137](https://reviews.llvm.org/D67137) 中为 llvm-objcopy 实现了它。

在 gdb 中调试 `a.stripped` 时，使用 `add-symbol-file -o xxx a.debug` 来加载单独的调试文件。

Solaris 11 Update 1 引入了名为 Ancillary Object 的类似功能。参见 [Ancillary Objects：Solaris 的独立调试 ELF 文件](http://www.linker-aliens.org/blogs/ali/entry/ancillary_objects_separate_debug_elf/)。`ld -z ancilliary` 直接创建两个输出文件，这是个不错的设计，在 GNU 链接模型中可以省去一次 objcopy 命令。不过，如果还需要 `--only-keep-debug` 之外的 objcopy 选项，仍然要再调用 objcopy。

2024 年 7 月，mold 增加了 [`--separate-debug-info`](https://github.com/rui314/mold/issues/1294)，它类似于 Solaris ld 的 `-z ancilliary` 的一种变体。

### `.gnu_debuglink`

`objcopy --add-gnu-debuglink=a.debug a.stripped` 向 `a.stripped` 添加一个非 `SHF_ALLOC` 的 `.gnu_debuglink` 节。该节包含文件名（不含目录信息）和一个四字节 CRC 校验和。1  
2  
3  
4  
5  
6  
% objdump -g a.stripped  
...  
Contents of the .gnu_debuglink section (loaded from a.stripped):  
  
 Separate debug info file: a.debug  
 CRC value: 0x4d1e2a66

gdb [自 2003 年起支持 `.gnu_debuglink`](https://sourceware.org/git/?p=binutils-gdb.git;a=commit;h=5b5d99cf4d5ded93b60fd64c6069d45e3eeab1d3)。它会在可执行文件所在目录及该目录下的 `.debug/` 中查找调试文件。（2022 年 9 月，我提交了支持 zstd 的[功能请求](https://sourceware.org/bugzilla/show_bug.cgi?id=29584)。）1  
2  
3  
% gdb -ex q a.stripped  
Reading symbols from a.stripped...  
Reading symbols from /tmp/c/a.debug...

还会使用 `debug-file-directory` 指定的目录。该选项必须在加载被调试程序之前设置。1  
2  
3  
4  
5  
6  
7  
% pwd  
/tmp/c  
% install -D -t debug/tmp/c a.debug  
% rm a.debug  
% gdb -iex 'set debug-file-directory debug' -ex q a.stripped  
Reading symbols from a.stripped...  
Reading symbols from debug//tmp/c/a.debug...

也可以通过构建 ID 查找调试文件。构建 ID 位于 ELF note 节中。许多 Linux 发行版使用 `--enable-linker-build-id` 配置 GCC，使其默认生成构建 ID。有关该选项，请参阅 [`--build-id`](https://maskray.me/blog/2020-11-15-explain-gnu-linker-options)。

```text
% readelf -Wn a.stripped
...
Displaying notes found in: .note.gnu.build-id
  Owner                Data size        Description
  GNU                  0x00000008       NT_GNU_BUILD_ID (unique build ID bitstring)         Build ID: a3b3f0788440fd94
% install -D -T debug/tmp/c/a.debug debug/.build-id/a3/b3f0788440fd94.debug
% rm debug/tmp/c/a.debug
% gdb -nx -iex 'set debug-file-directory debug' -ex q a.stripped
Reading symbols from a.stripped...
Reading symbols from /tmp/c/debug/.build-id/a3/b3f0788440fd94.debug...
```

lldb 使用 `target.debug-file-search-paths` 定位独立调试文件。（TODO）

在 Debian 上，安装 `hello-dbgsym` 后，调试文件会出现在 `/usr/lib/debug` 中。1  
2  
3  
4  
5  
% gdb -batch -ex 'show debug-file-directory'  
The directory where separate debug symbols are searched for is "/usr/lib/debug".  
% gdb -ex q =hello  
Reading symbols from /usr/bin/hello...  
Reading symbols from /usr/lib/debug/.build-id/ff/29703f105c66821e9b10149db8cff3b2e4043a.debug...

Debian 使用 [`dh_strip`](https://github.com/Debian/debhelper/blob/master/dh_strip) 执行打包操作。`dh_strip` 使用 `objcopy --only-keep-debug --compress-debug-sections` 来[压缩调试节](https://maskray.me/blog/2022-01-23-compressed-debug-sections)。

## MiniDebugInfo

参见 [MiniDebugInfo 文档](https://sourceware.org/gdb/onlinedocs/gdb/MiniDebugInfo.html)（[实现于 2012 年](https://sourceware.org/git/?p=binutils-gdb.git;a=commit;h=608e2dbbfefcec9aa3efc863ffcc889786ae93d7)）。当二进制文件包含 `.gnu_debugdata` 时，gdb 会用 xz 解压并加载它。1  
2  
3  
objcopy --only-keep-debug a a.debug  
xz a.debug  
objcopy -S --add-section=.gnu_debugdata=a.debug.xz a a.stripped  
 1  
2  
3  
% gdb -ex q a.stripped  
Reading symbols from a.stripped...  
Reading symbols from .gnu_debugdata for /tmp/c/a.stripped...

Fedora 使用此功能，在缺少调试信息时改善堆栈回溯的符号化。Fedora MiniDebugInfo 文件主要包含 note 节，以及一个含有 `.dynsym` 中不存在符号的 `.symtab`。非 `SHF_ALLOC` 的 `SHT_PROGBITS/SHT_NOTE/SHT_NOBITS` 节（例如 `.comment`）会被移除。由于 `eu-strip -f` 少了一项小优化，note 节会同时存在于原二进制文件和 MiniDebugInfo 文件中。

原始实现参见 [rpm 中的 MiniDebugInfo 支持](https://bugzilla.redhat.com/show_bug.cgi?id=834073)。新实现位于 [`debugedit`](https://sourceware.org/debugedit/) 仓库的 `scripts/find-debuginfo.in` 中。[LLDB 中的 mini-debuginfo 支持](https://archive.fosdem.org/2020/schedule/event/debugging_mini/)介绍了 lldb 的实现。

以下是 `scripts/find-debuginfo.in` 所执行操作的简化演示：1  
2  
3  
4  
5  
6  
7  
eu-strip --remove-comment -f a.mini a -o a.stripped  
nm a -f sysv --defined-only | awk -F \\| '$4 ~ "FUNC" {print $1}' | sort \> a.symtab  
nm a -f sysv --defined-only -D | sort \> a.dynsym  
comm -13 a.dynsym a.symtab \> a.keepsyms  
objcopy -S --keep-symbols=a.keepsyms a.mini  
xz a.mini  
objcopy -S --add-section=.gnu_debugdata=a.mini.xz a a.stripped

## DWARF 补充目标文件

DWARF 补充目标文件包含可供多个可执行文件和共享对象引用的调试节。dwz 提供 `-m file`，用于把重复的调试信息提取到补充目标文件中，并重写输入文件，使其引用该补充目标文件。补充目标文件可以包含调试信息条目、字符串和宏描述。

```sh
print '#include <stdio.h>\nint main() { puts("hello"); }' | gcc -g -gdwarf-5 -xc - -o 1
cp 1 2
dwz --dwarf-5 -m 3 1 2
```

`3` 是一个补充目标文件，包含少量 `.debug_*` 节；其中 `.debug_sup` 使用 `is_supplementary=1`。

`1` 会新增一个使用 `is_supplementary=0` 的 `.debug_sup` 节。它可以使用 `DW_FORM_ref_sup4 (DW_FORM_GNU_ref_alt), DW_FORM_strp_sup (DW_FORM_GNU_strp_alt), DW_MACRO_define_sup, DW_MACRO_undef_sup, DW_MACRO_import_sup` 等属性引用补充目标文件。在这个简单示例中，只使用了 `DW_FORM_ref_sup4` 和 `DW_FORM_strp_sup`。

在 DWARF v5 标准化之前，使用的是特殊节名 `.gnu_debugaltlink`。

## 分割 DWARF 目标文件

这一方案最初以 GCC [debug fission](https://gcc.gnu.org/wiki/DebugFission) 的名义提出，后来在 DWARF v5 中标准化为分割 DWARF 目标文件，通常简称“分割 DWARF”。其思路是把大部分 `.debug_*` 节移到独立文件（`.dwo`）中，只在可重定位目标文件（`.o`）中保留少量内容。链接器不处理 `.dwo` 文件，因此能减少输入节合并和重定位工作，缩短链接时间并降低内存用量。更小的输入对分布式构建集群也有好处。

```sh
% clang -c -g -gsplit-dwarf a.c b.c
% readelf -WS a.o | grep ' .debug_gnu_pub'
  [12] .debug_gnu_pubnames PROGBITS        0000000000000000 0000be 00001c 00      0   0  1
  [14] .debug_gnu_pubtypes PROGBITS        0000000000000000 0000da 00001b 00      0   0  1
% readelf -WS a.dwo | grep ']'
  [Nr] Name              Type            Address          Off    Size   ES Flg Lk Inf Al
  [ 0]                   NULL            0000000000000000 000000 000000 00      0   0  0
  [ 1] .strtab           STRTAB          0000000000000000 000155 000051 00      0   0  1
  [ 2] .debug_str_offsets.dwo PROGBITS        0000000000000000 000040 00001c 00   E  0   0  1
  [ 3] .debug_str.dwo    PROGBITS        0000000000000000 00005c 00009d 01 MSE  0   0  1
  [ 4] .debug_info.dwo   PROGBITS        0000000000000000 0000f9 00002e 00   E  0   0  1
  [ 5] .debug_abbrev.dwo PROGBITS        0000000000000000 000127 00002e 00   E  0   0  1
% clang -fuse-ld=lld -Wl,--gdb-index a.o b.o -o a
```

（注意：不要将编译和链接合为一个步骤：DWO 文件的位置可能会出乎意料。）

`-gsplit-dwarf` 隐式启用 `-ggnu-pubnames`，后者会生成 `.debug_gnu_pubnames` 和 `.debug_gnu_pubtypes` 节。（也可以在不使用 `-gsplit-dwarf` 时单独使用 `-ggnu-pubnames`，但这种情况并不常见。）

一些 ELF 链接器（gold、ld.lld、mold）支持 `--gdb-index`。该选项让链接器读取 `.debug_gnu_pubnames`、`.debug_gnu_pubtypes` 以及其他调试节（`.debug_info`、`.debug_addr`、`.debug_ranges`、`.debug_rnglists` 等）来构建 `.gdb_index`；随后丢弃 `.debug_gnu_pubnames` 和 `.debug_gnu_pubtypes`。

gdb 加载符号文件时会构建内部符号表。[`.gdb_index`](https://sourceware.org/gdb/onlinedocs/gdb/Index-Files.html) 可以缩短启动时间。使用分割 DWARF 时，按需完整解析可执行文件或共享对象所引用的 `.dwo` 文件。

Clang 支持用 `-gsplit-dwarf=single` 将 `.dwo` 节嵌入可重定位目标文件；编译过程不会生成 `.dwo` 文件。这种模式便于在单机上链接。

lldb 使用 `target.debug-file-search-paths` 搜索 `.dwo`，但不使用目录结构。（TODO）

分发大量 `.dwo` 文件可能很不方便。[DWARF 包文件](https://gcc.gnu.org/wiki/DebugFissionDWP)（通常使用 `.dwp` 扩展名）可以替代这些 `.dwo` 文件。（注意：DWP 目前对 [DWARF64 的支持不完整](https://dwarfstd.org/ShowIssue.php?issue=220708.2)。）binutils-gdb/gold 中的 dwp 可以构建 DWARF 包文件；[llvm-dwp](https://discourse.llvm.org/t/implementing-a-dwp-tool-in-llvm/38799) 是 llvm-project 中的另一种实现，但在内存用量扩展性方面存在一些问题。1  
dwp a.dwo b.dwo -o a.dwp

把 DWARF 压缩（例如 dwz）集成进 dwp 仍是一项 TODO。

gold 近年来维护不足，dwp 尚不支持 DWARF v5。

```sh
# Note: older Bazel needs --features=per_object_debug_info
bazel -c dbg --fission=yes :a  # bazel-bin/_objs/a/a.pic.dwo
bazel -c dbg --fission=yes :a.dwp  # bazel-bin/a.dwp
```

DWARF v5 引入 `.debug_names` 节，作为调试符号的加速查询表。可以用 `clang -g -gpubnames` 生成该节，从而为每个编译单元创建索引。链接时，链接器通常只是拼接各输入目标文件中的 `.debug_names` 节。LLDB 可以并行读取这些 `.debug_names` 节。ld.lld 实现了 `--debug-names`，用于创建覆盖整个模块的统一合并 `.debug_names` 索引，其性能优于分散的逐编译单元方案（[#86508](https://github.com/llvm/llvm-project/pull/86508)）。

### Bazel

Bazel 设置 `PWD=/proc/self/cwd` 以实现本地确定性。但是，如果你在仓库根目录之外的目录中调用可执行文件，调试器可能找不到源文件或 `.dwo` 文件。你可以使用以下命令调试 C++ 测试。

```sh
gdb -cd $PROJ/bazel-bin/path/to/a_test/_main -iex "directory $PROJ" -iex "set debug-file-directory $PROJ" --args path/to/a_test other args
```

## debuginfod

虽然 gdb 能提示缺少调试信息（例如 `Missing separate debuginfos, use: dnf debuginfo-install xxx`），许多人仍认为手动安装相应调试信息包很不方便。2019 年，elfutils 引入了新程序 [debuginfod](https://sourceware.org/elfutils/Debuginfod.html)。一些发行版已把调试信息托管在公共服务器上。参见 [debuginfod 项目的演进](https://www.redhat.com/en/blog/how-debuginfod-project-evolved-2021)。

以下示例展示了 debuginfod 的功能：

```sh
objcopy --only-keep-debug a a.debug
strip -S a -o a.stripped
tar cf a.tar.zst --zstd a.stripped a.debug
debuginfod -d debuginfod.sqlite -F -Z .tar.zst=zstdcat .
```

debuginfod 默认监听 8002 端口。`-F` 让它扫描指定目录中的归档文件；`-Z .tar.zst=zstdcat` 让它使用 zstdcat 处理 `.tar.zst` 文件，例如 Arch Linux 软件包。

对于每个归档成员，debuginfod 会把文件归类为普通可执行文件/共享对象（至少包含一个 `SHF_ALLOC SHT_PROGBITS` 节），或调试文件（包含 `.debug_*` 节）。默认情况下，debuginfod 会解析 `.debug_line`

`debuginfod-find` 是一个客户端。1  
2  
3  
4  
buildid=$(readelf -n a | awk '/Build ID:/ {print $3}')  
DEBUGINFOD_URLS='http://localhost:8002/' debuginfod-find debuginfo $buildid  
DEBUGINFOD_URLS='http://localhost:8002/' debuginfod-find executable $buildid  
DEBUGINFOD_URLS='http://localhost:8002/' debuginfod-find source $buildid /tmp/c/a.c

我们可以手动查询服务器：1  
2  
3  
curl -s localhost:8002/buildid/$buildid/debuginfo -o output && cmp a.debug output  
curl -s localhost:8002/buildid/$buildid/executable -o output && cmp a.stripped output  
curl -s localhost:8002/buildid/a3b3f0788440fd94/source/$(\<\<\</tmp/c/a.c sed 's,/,%2F,g') | diff /tmp/c/a.c -

启用 [`set debuginfod enabled on`](https://sourceware.org/gdb/onlinedocs/gdb/Debuginfod-Settings.html) 后，如果找不到符号文件，gdb 可以查询 debuginfod 服务器。目前只有少数程序支持 debuginfod，例如 valgrind。

Arch Linux 的主要变更：[debuginfod：实现该角色](https://gitlab.archlinux.org/archlinux/infrastructure/-/commit/194bc84bf4c698be3a21ebae41d03f35fc7d1b4c)

在 llvm-project 中，llvm-debuginfod 是另一种实现，需要 `LLVM_ENABLE_HTTPLIB=on`。

## Microsoft SymbolStore

它与 debuginfod 类似。参见 [Symbol Store Query Protocol Key Conventions](https://github.com/dotnet/symstore/blob/main/docs/specs/SSQP_Key_Conventions.md)。

## Apple 的“惰性”DWARF 方案

参见 [Apple 的“惰性”DWARF 方案](http://wiki.dwarfstd.org/index.php?title=Apple%27s_%22Lazy%22_DWARF_Scheme)。

Apple 平台使用的模型与 Linux 发行版不同。Apple ld64 不会将输入的 `__debug_*` 节合并到输出节中。相反，除非指定了 `-S`，调试映射条目会被发送到符号表中，以记录源文件和可重定位目标文件。在这些条目中，`N_OS` 和 `N_OSO` 记录源文件和可重定位目标文件。`N_FUN` 提供函数的值/大小。`N_GSYM`/`N_STSYM` 描述全局/静态变量符号。

使用 lldb 调试程序时，lldb 会从 dSYM bundle 以及 `N_OSO` 条目对应的可重定位目标文件中解析 DWARF。

```sh
clang -c -g a.c b.c
clang a.o b.o -o a
dsymutil a
```

dsymutil 可以从可重定位目标文件创建 dSYM bundle。它接受可执行文件名；指定 `-y` 时，也可接受 YAML 调试映射。dsymutil 找到 `a.o` 和 `b.o` 两个可重定位目标文件，将其 DWARF 信息合并、优化到一个 dSYM 文件中，并构建加速表（`.apple_*` 或 `.debug_names`）。

## Windows PDB

TODO

## 附录：调试信息大小

[https://gcc.gnu.org/onlinedocs/gcc/Debugging-Options.html#index-feliminate-unused-debug-types](https://gcc.gnu.org/onlinedocs/gcc/Debugging-Options.html#index-feliminate-unused-debug-types)

`-fdebug-types-section`：更大的可重定位文件，但更小的镜像文件

`-mllvm -minimize-addr-in-v5=Ranges` 对分割 DWARF 很有用

`-gsimple-template-names` 已被 Chrome [采用](https://crrev.com/c/3988987)
