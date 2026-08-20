---
title: 指定动态链接器以使用高版本 GCC
source: MaskRay (宋方睿)
source_key: maskray
source_url: 'https://maskray.me/blog/2015-09-29-specify-dynamic-linker-to-use-higher-version-gcc'
original_language: en
published: 2015-09-29
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:2db07d5fbf9234f8'
translated: true
---

> 原文：[指定动态链接器以使用高版本 GCC](https://maskray.me/blog/2015-09-29-specify-dynamic-linker-to-use-higher-version-gcc)　·　MaskRay（宋方睿）

[2015-09-29](https://maskray.me/blog/2015-09-29-specify-dynamic-linker-to-use-higher-version-gcc)

# 指定动态链接器以使用高版本 GCC

今天有人问怎么在没有 root 的不可更新老旧 Linux 环境里使用高版本 GCC，主要困难在于 GCC 对 glibc 版本有一定要求。假设使用现成的 GCC 二进制包，解压到本地后执行 `gcc`，报错：`/lib64/libc.so.6: version `GLIBC_2.14' not found`，即系统 glibc 的 `libc.so.6` 中缺乏更高版本的符号（参考`info '(ld) VERSION'`）。使用新符号通常表示 API 有更新，不过很多时候旧版本的库也能用，可能有两个原因：一是编译机器的库版本可能较新，soname 版本号较高，编译出来的可执行文件也会有较高的版本要求；二是源文件因保守指定了较高的版本号，实际上旧版本也能用。

比如最近 ncurses 主版本号更新到 6，`/usr/lib/libncursesw.so.5` 变成了 `/usr/lib/libncursesw.so.6`，导致很多可执行文件没法用了：

```plaintext
% ldd /usr/lib/j8/bin/jconsole
        linux-vdso.so.1 (0x00007ffcdb9ec000)
        libedit.so.2 => /usr/lib/libedit.so.2 (0x00007fd995a09000)
        libdl.so.2 => /usr/lib/libdl.so.2 (0x00007fd995805000)
        libncursesw.so.5 => not found
        libc.so.6 => /usr/lib/libc.so.6 (0x00007fd9951f4000)
        /lib64/ld-linux-x86-64.so.2 (0x00007fd995c45000)
```

不想重新编译的话，可以软链接做一个 `libncursesw.so.5`，放在 `ld.so` 默认会查找的路径下，或者运行时指定环境变量 `LD_LIBRARY_PATH`。另外还有一种修改可执行文件的方法：用十六进制编辑工具把 `.dynstr` section 中的字符串 `libncursesw.so.5` 改成 `libncursesw.so.6`。再次执行时，`ld.so` 将会用新的名字查找依赖的库，就顺利找到了 `/usr/lib/libncursesw.so.6`，但做这样的修改得保证新的路径名长度小于等于原长，否则会覆盖 `.dynstr` 中后面的字符串。另一种办法是构造一个新的 `.dynstr` 放到 ELF 的其他地方，并变更 section header 中的 `.dynstr` 地址信息，非常麻烦。

回到正题，xptree 下载了 `gcc-c++-4.8.3-9.el7.x86_64.rpm` 和 `gcc-4.8.3-9.el7.x86_64.rpm`，解压后执行，报错：`/lib64/libc.so.6: version `GLIBC_2.14' not found`。解压`glibc-2.17-78.el7.x86_64.rpm`，报错：

```plaintext
/usr/bin/python: relocation error: MY_LOCAL/lib64/libc.so.6: symbol
_dl_starting_up, version GLIBC_PRIVATE not defined in file ld-linux-x86-64.so.2
with link time reference
g++: relocation error: MY_LOCAL/lib64/libc.so.6: symbol _dl_starting_up,
version GLIBC_PRIVATE not defined in file ld-linux-x86-64.so.2 with link time
reference
```

看来对 `ld-linux-x86-64.so.2`（动态链接器，下面简称为 `ld.so`）的版本也有要求。就像修改依赖库的路径那样，修改 program header 中的 `PT_INTERP`：

```plaintext
bbe -b '/\x2flib64\x2fld-linux-x86-64.so.2/:27' -e 'L 1' -e 'r 0 /tmp/l/ld.so\0' bin/gcc -o bin/gcc.new
```

效果是把 `gcc` 中第一次出现的 `/lib64/ld-linux-x86-64.so.2`(`PT_INTERP` 项）替换成 `/tmp/l/ld.so\0`，可以观察到：

```plaintext
% ldd bin/gcc.new
        linux-vdso.so.1 (0x00007ffff85f5000)
        libm.so.6 => /usr/lib/libm.so.6 (0x00007f36788ca000)
        libc.so.6 => /usr/lib/libc.so.6 (0x00007f3678526000)
        /tmp/l/ld.so (0x00007f3678bc8000)
```

有几个被 `gcc` `g++` 调用的可执行文件如 `cc1`、`cc1plus` 等可能也得做同样修改。之后 `gcc` 即可执行，但编译生成的可执行文件还使用原先的动态链接器，也许会在某些情况下无法执行。一种办法是在用 `gcc` `g++` 链接时指定 `-Wl,--dynamic-linker,/tmp/l/ld.so`，这样产生的可执行文件就会使用 `/tmp/l/ld.so` 作为动态链接器。另一种方法是修改 `gcc` 中的 built-in 内置 specs：

```plaintext
% gcc -dumpspecs
......
*link:
...%{m16|m32|mx32:;:-dynamic-linker %{muclibc:/lib/ld64-uClibc.so.0;:%{mbionic:/system/bin/linker64;:/lib64/ld-linux-x86-64.so.2}}}...
......
```

用 `bvi`、`bviplus` 等十六进制编辑器在可执行文件 `gcc` 中找这段字串，把 `/lib64/ld-linux-x86-64.so.2}}}` 改成 `/tmp/l/ld.so}}}`，原串多出来的地方用空格填充。这样得到的 `gcc` 产生的可执行文件无需指定 `-Wl,--dynamic-linker`，默认就会使用新的动态链接器了：

```plaintext
% bin/gcc.new -xc - -o a <<< 'int main(){}'
% ldd a
        linux-vdso.so.1 (0x00007ffeff9b3000)
        libc.so.6 => /usr/lib/libc.so.6 (0x00007f337fe5b000)
        /tmp/l/ld.so (0x00007f33801ff000)
```

## 跳出 XY problem

如果要装的东西多些，可以考虑 Gentoo Prefix、[NixOS](http://nixos.org/)等，还有 unprivileged LXC containers 等。轻量省事的方法是 userspace chroot[PRoot](http://proot.me/)，不需要 root，但弊端是运行的进程处于 ptrace 下，而一个进程不能被 ptrace 两次，因此 gdb、strace 等都没法用。
