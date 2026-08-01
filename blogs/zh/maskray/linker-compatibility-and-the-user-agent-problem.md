---
title: '链接器兼容性与“User-Agent”问题'
source: MaskRay (宋方睿)
source_key: maskray
source_url: 'https://maskray.me/blog/2024-07-07-linker-compatibility-and-the-user-agent-problem'
original_language: en
published: 2024-07-07
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:1298a9a1f632ca9d'
translated: true
---

> 原文：[链接器兼容性与“User-Agent”问题](https://maskray.me/blog/2024-07-07-linker-compatibility-and-the-user-agent-problem)　·　MaskRay (宋方睿)

[2024-07-07](https://maskray.me/blog/2024-07-07-linker-compatibility-and-the-user-agent-problem)

# 链接器兼容性与“User-Agent”问题

`ld.lld -v` 的输出包含“compatible with GNU linkers”消息，以应对 [GNU Libtool 使用的检测机制](https://lists.gnu.org/archive/html/libtool/2017-01/msg00007.html)。[软件兼容性与我们自己的“User-Agent”问题](https://www.sigbus.info/software-compatibility-and-our-own-user-agent-problem)描述了这一问题。

最新的 `m4/libtool.m4` 仍依赖 `GNU` 检查。

```plaintext
[AC_CACHE_CHECK([if the linker ($LD) is GNU ld], lt_cv_prog_gnu_ld,
[# I'd rather use --version here, but apparently some GNU lds only accept -v.
case `$LD -v 2>&1 </dev/null` in
*GNU* | *'with BFD'*)
  lt_cv_prog_gnu_ld=yes
  ;;
*)
  lt_cv_prog_gnu_ld=no
  ;;
esac])
```

[基于检查的配置](https://leahneukirchen.org/blog/archive/2024/04/what-autoconf-got-right.html)可以成为很有价值的工具，确保软件未来仍然可用。不过，这个示例也说明过于具体的检查会如何带来意料之外的后果。

如果 Libtool 需要检查某些选项是否可用，可以使用 [`-v`](#more-fun-with-versions)。

```plaintext
% ld.bfd -v --whole-archive
GNU ld (GNU Binutils) 2.42.0
% ld.bfd -v --whole-archivex; echo $?
GNU ld (GNU Binutils) 2.42.0
ld.bfd: unrecognized option '--whole-archivex'
ld.bfd: use the --help option for usage information
1
```

本文探讨一个改变版本消息格式的 LLD 补丁所暴露出的更多“User-Agent”问题形式。

LLD 支持许多目标文件格式。对于 ELF，它主要模拟 GNU ld 的行为；对于 PE/COFF，则模拟 MSVC link.exe 的行为。此前，LLD 的 ELF 端口按如下方式显示版本信息：1  
2  
% /tmp/out/custom2/bin/ld.lld --version  
LLD 19.0.0 (compatible with GNU linkers)

最近的补丁（[llvm-project#97323](https://github.com/llvm/llvm-project/pull/97323)）根据构建时变量 `LLVM_APPEND_VC_REV`，将其改为以下格式之一：

当 `LLVM_APPEND_VC_REV=on` 时：1  
2  
% /tmp/out/custom2/bin/ld.lld --version  
LLD 19.0.0 (git@github.com:llvm/llvm-project.git 0f9fbbb63cfcd2069441aa2ebef622c9716f8dbb), compatible with GNU linkers

当 `LLVM_APPEND_VC_REV=off` 时：1  
2  
% /tmp/out/custom2/bin/ld.lld --version  
LLD 19.0.0, compatible with GNU linkers

## Meson

在 Meson 中，`mesonbuild/linkers/detect.py:guess_win_linker` 会检查 `--version` 的输出，以确定 LLD 调用面向 ELF 还是 PE/COFF。它原先进行了过于严格的“(compatible with GNU linkers)”检查；当 #97323 移除了括号后，这个检查就失败了。

```python
# mesonbuild/linkers/detect.py
    if 'LLD' in o.split('\n', maxsplit=1)[0]:
        if '(compatible with GNU linkers)' in o:
            return linkers.LLVMDynamicLinker(
                compiler, for_machine, comp_class.LINKER_PREFIX,
                override, version=search_version(o))
        elif not invoked_directly:
            return linkers.ClangClDynamicLinker(
                for_machine, override, exelist=compiler, prefix=comp_class.LINKER_PREFIX,
                version=search_version(o), direct=False, machine=None)
```

最新的 Meson 已放宽这项检查（[meson#13383](https://github.com/mesonbuild/meson/pull/13383)）。

链接器检测似乎还有一个更大的问题：使用 Clang 时没有考虑 `--target=`（[#6662](https://github.com/mesonbuild/meson/issues/6662)）。

## Linux 内核

Linux 内核的 `scripts/ld-version.sh` 脚本会检测链接器版本。它于 2014 年引入，起初为 GCC LTO 检查 GNU ld 兼容性（尽管 LTO 支持仍未合入）。之后它经过改造，也能处理 LLD 版本。它可以处理 `2.34-4.fc32` 一类后缀，却无法处理带逗号后缀（`19.0.0,`）的版本。

```plaintext
% scripts/ld-version.sh /tmp/out/custom2/bin/ld.lld
scripts/ld-version.sh: line 19: 10000 * 19 + 100 * 0 + 0,: syntax error: operand expected (error token is ",")
```

该脚本从 `--version` 输出中提取版本字符串，并将其解析为主版本号.次版本号.修订号。

```sh
# Get the first line of the --version output.
IFS='
'
set -- $(LC_ALL=C "$@" --version)

# Split the line on spaces.
IFS=' '
set -- $1

...

# Some distributions append a package release number, as in 2.34-4.fc32
# Trim the hyphen and any characters that follow.
version=${version%-*}
```

为支持以 `-` 或 `,` 开头的后缀，该脚本[将采用 POSIX shell 技巧](https://lore.kernel.org/all/20240705160007.GA875035@thelio-3990X/)，利用“移除最大后缀模式”功能：

```sh
version=${version%%[!0-9.]*}
```

## 更多版本相关趣事

llvm-nm 和 llvm-objcopy 也宣称与 GNU 兼容。

```plaintext
% /tmp/Rel/bin/llvm-nm --version
llvm-nm, compatible with GNU nm
LLVM (http://llvm.org/):
  LLVM version 19.0.0git
  Optimized build with assertions.
% /tmp/Rel/bin/llvm-objcopy --version
llvm-objcopy, compatible with GNU objcopy
LLVM (http://llvm.org/):
  LLVM version 19.0.0git
  Optimized build with assertions.
```

你是否想过，使用 GNU ld 时 `-v`、`-V` 与 `--version` 有何细微差别？下面逐一说明：

- `--version` 会跳过链接器输入处理，并显示简短的版权信息。
- `-v` 和 `-V` 会继续处理命令行参数并执行链接步骤。这种行为提供了检查选项是否受支持的简便方式。
- `-V` 比 `-v` 更进一步：除版本信息外，它还会列出支持的 BFD 模拟。

在 2022 年 9 月之前，ld.lld 中的 `-V` 曾是 `--version` 的别名。这会导致在 `*-freebsd` 和 `powerpc-*` 等特定目标上使用 `gcc -v -fuse-ld=lld` 时出现问题：gcc 会把 `-V` 传给链接器，并期望它处理输入文件、完成链接步骤；但 ld.lld 对 `-V` 的处理跳过了这一过程。

我随后做出调整，[让 `-V` 成为 `-v` 的别名](https://github.com/llvm/llvm-project/issues/57859)。这确保 `gcc -v -fuse-ld=lld` 会执行链接步骤。

GCC 的 `-v` 与 `--version` 也有相似行为，但不存在 `-V`。

Clang 的 GNU 驱动模拟 GCC 4.2.1，不过你可以使用 `-fgnuc-version=` 更改版本。

```plaintext
% clang -E -dM -xc /dev/null | grep GNU
#define __GNUC_MINOR__ 2
#define __GNUC_PATCHLEVEL__ 1
#define __GNUC_STDC_INLINE__ 1
#define __GNUC__ 4
% clang -E -dM -xc /dev/null -fgnuc-version=5.3.2 | grep GNU
#define __GNUC_MINOR__ 3
#define __GNUC_PATCHLEVEL__ 2
#define __GNUC_STDC_INLINE__ 1
#define __GNUC__ 5
```
