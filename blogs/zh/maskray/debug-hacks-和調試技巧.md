---
title: 《Debug Hacks》和调试技巧
source: MaskRay (宋方睿)
source_key: maskray
source_url: 'https://maskray.me/blog/2013-07-25-debug-hacks'
original_language: en
published: 2013-07-25
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:e9b1ac0812794ea0'
translated: true
---

> 原文：[《Debug Hacks》和调试技巧](https://maskray.me/blog/2013-07-25-debug-hacks)　·　MaskRay (宋方睿)

[2013-07-25](https://maskray.me/blog/2013-07-25-debug-hacks)

# 《Debug Hacks》和调试技巧

下篇见[调试技巧2](https://maskray.me/blog/2015-03-14-debug-hacks-2)。

## Debug Hacks

作者为吉冈弘隆、大和一洋、大岩尚宏、安部东洋、吉田俊辅，有中文版《Debug Hacks中文版—深入调试的技术和工具》。这本书涉及了很多调试技巧，对调试器使用、内核调试方法、常见错误的原因，还介绍了`systemtap`、`strace`、`ltrace`等一大堆工具，非常值得一读。

话说我听说过的各程序设计课程似乎都没有强调过调试的重要性，把调试当作单独一节课来上(就算有估计也上不好)，很多人都只会`printf`调试法，breakpoint都很少用，就不提conditional breakpoint、watchpoint、reverse execution之类的了。也看到过很多同学在调试上浪费了很长很长的时间。

下面是篇review，也包含了一些我自己整理的一些调试技巧。

## 折腾工具

继续牢骚几句，我接触过的人当中感觉最执着与折腾工具的人只有两个，[ppwwyyxx](http://ppwwyyxx.com/)和[xiaq](http://wiki.tuna.tsinghua.edu.cn/xiaq)，他们是少有的能把折腾工具当作正经工作来做的人。

很久以前我还会到处在网上搜索好的实用工具，尤其是那些CLI程序，比如`renameutils`、`xsel`、`recode`、`the_silver_searcher`，查阅文档定制自己的配置文件。但这么做花费的时间太多。后来就想我可以搜索一些善于折腾的人的配置文件，关注他们修改了哪些地方，我的配置只要取众家之所长就可以了。

先厚颜自荐一下[我的配置](https://github.com/MaskRay/Config)。下面的用户列表就是我找到的在GitHub上把`dotfiles`配置地井井有条的人(如果GitHub支持按照项目的大小排序，列表搜集就能省很多麻烦了)：

```plaintext
alejandrogomez bhj craigbarnes dotvim hamaco joedicastro laurentb ok100 pyx roylez sjl trapd00r vodik w0ng
```

有了上述的`dotfiles`，其他人的`dotfiles`大多都不愿看了。但是五岳归来不看山，黄山归来不看岳，`ppwwyyxx`的[dotfiles](https://github.com/ppwwyyxx/dotfiles)感觉与之前诸位相比更胜一筹。

无关的话到此结束，下面是正文：

## gdb

### 记录历史

把下面几行添加到`~/.gdbinit`中吧，`gdb`启动时会自动读取里面的命令并执行：

```plaintext
set history save on
set history size 10000
set history filename ~/.history/gdb
```

我习惯在`~/.history`堆放各个历史文件。有了历史，使用`readline`的`reverse-search-history (C-r)`就能轻松唤起之前输入过的命令。

### 修改任意内存地址的值

```plaintext
set {int}0x83040 = 4
```

### 显示intel风格的汇编指令

```plaintext
set disassembly-flavor intel
```

### 断点在function prologue前

先说一下function prologue吧，每个函数最前面一般有三四行指令用来保存旧的帧指针(rbp)，并腾出一部分栈空间(通常用于储存局部变量、为当前函数调用其他函数腾出空间存放参数，有时候还会存储字面字符串，当有nested function时也会用于保存当前的栈指针)。

在x86-64环境下典型的funcition prologue长成这样：

```plaintext
push rbp
mov rbp, rsp
sub rsp, 0x10
```

可能还会有`and`指令用于对齐`rsp`。如果编译时加上`-fomit-frame-pointer`(Visual Studio中文版似乎译作“省略框架指针”)，那么生成的指令就会避免使用`rbp`，function prologue就会简化成下面一行：

```plaintext
sub rsp, 0x10
```

设置断点时如果使用了`b *func`的格式，也就是说在函数名前加上`*`，`gdb`就会在执行function prologue前停下，而`b func`则是在执行function prologue后停下。参考下面的会话：

```text
% gdb a.out
Reading symbols from /tmp/a.out...done.
(gdb) b *main
Breakpoint 1 at 0x4005cc: file a.c, line 4.
(gdb) r
Starting program: /tmp/a.out
warning: Could not load shared library symbols for linux-vdso.so.1.
Do you need "set solib-search-path" or "set sysroot"?

Breakpoint 1, main () at a.c:4
4       {
(gdb) disas
Dump of assembler code for function main:
=> 0x00000000004005cc <+0>:     push   rbp
   0x00000000004005cd <+1>:     mov    rbp,rsp
   0x00000000004005d0 <+4>:     sub    rsp,0x10
   0x00000000004005d4 <+8>:     mov    DWORD PTR [rbp-0x4],0x0
   0x00000000004005db <+15>:    mov    eax,DWORD PTR [rbp-0x4]
   0x00000000004005de <+18>:    mov    esi,eax
   0x00000000004005e0 <+20>:    mov    edi,0x4006ec
   0x00000000004005e5 <+25>:    mov    eax,0x0
   0x00000000004005ea <+30>:    call   0x400454 <printf@plt>
   0x00000000004005ef <+35>:    leave
   0x00000000004005f0 <+36>:    ret
End of assembler dump.
(gdb)
```

### Checkpoint

`gdb`可以为被调试的程序创建一个快照，即保存程序运行时的状态，等待以后恢复。这个是非常方便的一个功能，特别适合需要探测接下来会发生什么但又不想离开当前状态时使用。

`ch`是创建快照，`d c ID`是删除指定编号的快照，`i ch`是查看所有快照，`restart ID`是切换到指定编号的快照，详细说明可以在shell里键入`info '(gdb) Checkpoint/Restart'`查看。

```text
% gdb ./a.out
Reading symbols from /tmp/a.out...done.
(gdb) b 6
Breakpoint 1 at 0x4005db: file a.c, line 6.
(gdb) r
Starting program: /tmp/a.out
warning: Could not load shared library symbols for linux-vdso.so.1.
Do you need "set solib-search-path" or "set sysroot"?

Breakpoint 1, main () at a.c:6
6         printf("%d\n", a);
(gdb) ch
checkpoint: fork returned pid 6420.
(gdb) p a=3
$1 = 3
(gdb) i ch
  1 process 6420 at 0x4005db, file a.c, line 6
* 0 process 6416 (main process) at 0x4005db, file a.c, line 6
(gdb) restart 1
Switching to process 6420
#0  main () at a.c:6
6         printf("%d\n", a);
(gdb) c
Continuing.
0
[Inferior 1 (process 6420) exited with code 02]
[Switching to process 6416]
(gdb)
```

上面的会话中先用`ch`创建了一个快照，紧接着`a`被修改为了3，随后用`restart 1`恢复到编号为1的快照，继续运行程序可以发现`a`仍然为原来的值0。

以色列的Haifa Linux club有一次讲座讲`gdb`，讲稿值得一看：http://haifux.org/lectures/210/gdb_-_customize_it.html

### 逆向技术

Long Le的[peda](https://github.com/longld/peda)很不错，感觉比http://reverse.put.as的https://github.com/gdbinit/Gdbinit好用。

## gcc

### Mudflap

使用了compile-time instrumentation(CTI)的工具。编译时加上`-fmudflap -lmudflap`选项即可，会在很多不安全代码生成的指令前加上判断合法性的指令。

```plaintext
% echo 'int main() { int z[1]; z[1] = 2; }' | cc -xc - -fmudflap -lmudflap
% ./a.out
*******
mudflap violation 1 (check/write): time=1376473424.792953 ptr=0x7fff2cde3150 size=8
pc=0x7fa2bacf86f1 location=`<stdin>:1:29 (main)'
      /usr/lib/gcc/x86_64-pc-linux-gnu/4.7.3/libmudflap.so.0(__mf_check+0x41) [0x7fa2bacf86f1]
      ./a.out(main+0x8f) [0x400b6b]
      /lib64/libc.so.6(__libc_start_main+0xf5) [0x7fa2ba968c35]
Nearby object 1: checked region begins 0B into and ends 4B after
mudflap object 0x7070e0: name=`<stdin>:1:18 (main) z'
bounds=[0x7fff2cde3150,0x7fff2cde3153] size=4 area=stack check=0r/3w liveness=3
alloc time=1376473424.792946 pc=0x7fa2bacf7de1
number of nearby objects: 1
```

第一行用`-xc -`让`cc`从标准输入读源代码，并当作C来编译。接来下执行`./a.out`，可以看到运行时程序报错了。

使用`MUDFLAP_OPTIONS`环境变量可以控制Mudflap的运行期行为，具体参见[Mudflap Pointer Debugging](http://gcc.gnu.org/wiki/Mudflap_Pointer_Debugging)。

### AddressSanitizer

和Mudflap类似的工具，`clang`和`gcc`可以加上选项`-fsanitize=address`使用，比如：

```bash
clang -fsanitize=address a.c
```

如果想在出错的地方断点停下来，可以用`gdb`打开，输入`b __asan_report_store1`回车，再输入`r`回车运行程序。

### `-ftrapv`

这个选项是调试有符号整型溢出问题的利器。在i386环境下，gcc会把`int32_t`运算编译成`call __addvsi3`，`__addvsi3`函数会在运行时检查32位有符号加法运算是否产生溢出，如果是则调用`abort`函数中止程序。减法、乘法和取反运算也有类似的运行时函数检查溢出，另外也有64位版本的`__addvdi3`等函数。但不存在对无符号整型的溢出检测函数。比如下面这些代码均会触发trap：

```c
int a = INT_MAX; a++;
int b = INT_MIN; b--;
int c = INT_MAX; c *= 2;
int d = INT_MIN; d = -d;
```

这段代码来自`gcc`项目目录的`libgcc/libgcc2.c`：

```c
#ifdef L_subvsi3
Wtype
__subvSI3 (Wtype a, Wtype b)
{
  const Wtype w = (UWtype) a - (UWtype) b;

  if (b >= 0 ? w > a : w < a)
    abort ();

  return w;
}
```

但注意在x86-64环境下`-ftrapv`只检查64位溢出。考虑下面这段代码：

```c
#include <limits.h>
#include <stdio.h>

int main()
{
  int a = INT_MAX;
  a++;

  puts("barrier");

  long b = LONG_MAX;
  b++;
}
```

在x86-64下用`gcc`编译运行，输出`barrier`后才会执行`abort`使程序中止，因为`int32_t`的溢出不会触发trap。

`clang`也有`-ftrapv`，在x86-64环境下对于`int32_t`的溢出也能触发trap。

### `_FORTIFY_SOURCE`

`gets`、`strcpy`这类函数容易造成stack mashing。`gcc`编译时如果指定了`-D_FORTIFY_SOURCE=1`，生成的汇编程序中这些不安全的函数调用会被替代为`libc.so`中名字类似`__gets_chk`的一类安全函数，会在运行期检查是否产生了缓冲区溢出。比如，下面的代码会在运行时报错：

```c
#include <string.h>

int main()
{
  char a[2];
  strcpy(a, "meow");
}
```

Gentoo Portage从`gcc-4.3.3-r1`开始默认开启`_FORTIFY_SOURCE`标志了，好多发行版都开启了，测试发现Arch Linux的`gcc`似乎没有。shell里执行下面代码就可以看到Gentoo里是怎么定义`_FORTIFY_SOURCE`的了：

```bash
echo -e '#undef __OPTIMIZE__\nmain() { printf("%d\\n", _FORTIFY_SOURCE); }' | cpp
```

也就是当优化等级在`-O1`或以上时`_FORTIFY_SOURCE`会生效，名字为`__$func_chk`模式的函数会被使用。这种做法造成了一些麻烦，比如`suricata` git tree里的`src/suricata.c`使用了`#ifdef _FORTIFY_SOURCE`，会造成编译无法通过。

### `-fstack-protector`

-fstack-protector -fstack-protector-all gcc 4.8.1 -fstack-protector-strong

https://securityblog.redhat.com/2013/10/23/debugging-stack-protector-failures/

开启Stack-Smashing Protector (SSP)。我的理解是在存储的帧指针(rbp)前写入一个magic number，函数返回的时候检查下这个magic number是否被改动，如果是就可能产生stack smashing了。这个方法的footprint最小，但是保护力度也比较弱。

#### IA32

```plaintext
function prologue
 80484c0:       65 a1 14 00 00 00       mov    eax,gs:0x14
 80484c6:       89 45 f4                mov    DWORD PTR [ebp-0xc],eax

function epilogue
 80484d7:       8b 45 f4                mov    eax,DWORD PTR [ebp-0xc]
 80484da:       65 33 05 14 00 00 00    xor    eax,DWORD PTR gs:0x14
 80484e1:       74 05                   je     80484e8 <foo+0x33>
 80484e3:       e8 68 fe ff ff          call   8048350 <__stack_chk_fail@plt>
 80484e8:       c9                      leave
 80484e9:       c3                      ret
```

#### x86-64

```plaintext
function prologue:

  4005c9:       64 48 8b 04 25 28 00    mov    rax,QWORD PTR fs:0x28
  4005d0:       00 00
  4005d2:       48 89 45 f8             mov    QWORD PTR [rbp-0x8],rax

function epilogue

  400618:       64 48 33 04 25 28 00    xor    rax,QWORD PTR fs:0x28
  40061f:       00 00
  400621:       74 05                   je     400628 <foo+0x3b>
  400623:       e8 88 fe ff ff          call   4004b0 <__stack_chk_fail@plt>
  400628:       48 83 c4 78             add    rsp,0x78
  40062c:       c3                      ret
```

### execinfo.h

提供了`int backtrace (void **buffer, int size)`、`char ** backtrace_symbols (void *const *buffer, int size)`在程序运行时查看函数调用栈。参见http://www.gnu.org/software/libc/manual/html_node/Backtraces.html。

## Misc

### Valgrind

一系列调试和profiling工具的套件，其中的Memcheck是一个使用了dynamic binary instrumentation(DBI)的工具， 在程序指令间插入自己的指令检查validity和addressablity。另外Memcheck替换了标准的`malloc`，这样就可以检测出off-by-one error、double free、内存泄漏等许多问题。

Memcheck引入的footprint极小，无需重编译程序，也没有繁琐的配置。比如原来是用`./a.out`执行程序，需要Memcheck时就换成`valgrind ./a.out`。

在程序访问某一内存地址时Memcheck会检查是否有越界之类的错误，Memcheck能诊断出大量但不是全部的访问错误，比如下面这样有问题的代码就没法检查出来：

```c
int main()
{
  int a[1];
  a[1992] = 12;
}
```

因为`a[1992]`的地址在栈上，允许访问。

Valgrind启动时会读取`~/.valgrindrc`，对于`memcheck`我配置了下面这几行：

```text
--memcheck:leak-check=yes
--memcheck:show-possibly-lost=yes
--memcheck:show-reachable=yes
--memcheck:track-origins=yes
--memcheck:dsymutil=yes
--memcheck:track-fds=yes
--memcheck:track-origins=yes
--memcheck:gen-suppressions=all
```

`valgrind --vgdb-error=0 --vgdb=yes`很强大，可以在进程遇到错误时让`gdb`调试。

### strace

记录程序执行的系统调用和收到的信号，和`valgrind`类似，使用非常简单：

```bash
strace ./a.out
```

有一些选项可以attach到现有进程上去(-p)、记录时刻(-t)、统计系统调用使用次数(-c)、过滤特定的系统调用(-e)等。

带上`-c`选项可以统计系统调用的使用次数： 1  
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
26  
27  
28  
% strace -c ls  
chap04 chap05 chap06 chap07 chap08 chap09 chap10 chap11 chap12 chap13 chap14 chap15 chap16 chap17  
% time seconds usecs/call calls errors syscall  
------ ----------- ----------- --------- --------- ----------------  
 0.00 0.000000 0 5 read  
 0.00 0.000000 0 1 write  
 0.00 0.000000 0 7 open  
 0.00 0.000000 0 10 close  
 0.00 0.000000 0 8 fstat  
 0.00 0.000000 0 20 mmap  
 0.00 0.000000 0 12 mprotect  
 0.00 0.000000 0 2 munmap  
 0.00 0.000000 0 3 brk  
 0.00 0.000000 0 2 rt_sigaction  
 0.00 0.000000 0 1 rt_sigprocmask  
 0.00 0.000000 0 2 ioctl  
 0.00 0.000000 0 1 1 access  
 0.00 0.000000 0 1 execve  
 0.00 0.000000 0 1 fcntl  
 0.00 0.000000 0 2 getdents  
 0.00 0.000000 0 1 getrlimit  
 0.00 0.000000 0 1 arch_prctl  
 0.00 0.000000 0 2 1 futex  
 0.00 0.000000 0 1 set_tid_address  
 0.00 0.000000 0 1 openat  
 0.00 0.000000 0 1 set_robust_list  
------ ----------- ----------- --------- --------- ----------------  
100.00 0.000000 85 2 total

`-e`选项只跟踪指定系统调用：

```plaintext
% strace -e read,open ls
open("/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
open("/lib64/librt.so.1", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\220(\0\0\0\0\0\0"..., 832) = 832
open("/lib64/libacl.so.1", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\320#\0\0\0\0\0\0"..., 832) = 832
open("/lib64/libc.so.6", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0@M\2\0\0\0\0\0"..., 832) = 832
open("/lib64/libpthread.so.0", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0@}\0\0\0\0\0\0"..., 832) = 832
open("/lib64/libattr.so.1", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0`\25\0\0\0\0\0\0"..., 832) = 832
open("/usr/lib64/locale/locale-archive", O_RDONLY|O_CLOEXEC) = 3
chap04  chap05  chap06  chap07  chap08  chap09  chap10  chap11  chap12  chap13  chap14  chap15  chap16  chap17
+++ exited with 0 +++
```

使用`strace`还可以做一些很可怕的事，比如有`root`权限的情况下嗅探`sshd`以得到其他尝试SSH登录的用户的密码：[SSHD 密码嗅探](http://blog.0x10.co.uk/2009/12/sshd-password-sniffing.html)。

`-p`很有用，比如调试CGI wrapper`fcgiwrap`，观察它的输出：

```plaintext
strace -s200 -p$(pidof -s fcgiwrap) -e write
```

### ltrace

记录程序调用的动态库中的函数。名字和`strace`很像，使用方式和很多命令行选项也如出一辙。

查看`echo test`

```plaintext
% ltrace echo test
__libc_start_main(0x401590, 2, 0x7fff2bb3d4d8, 0x403ef0 <unfinished ...>
getenv("POSIXLY_CORRECT")                                                                        = nil
strrchr("echo", '/')                                                                             = nil
setlocale(LC_ALL, "")                                                                            = "en_US.UTF-8"
bindtextdomain("coreutils", "/usr/share/locale")                                                 = "/usr/share/locale"
textdomain("coreutils")                                                                          = "coreutils"
__cxa_atexit(0x401cf8, 0, 0, 0x736c6974756572)                                                   = 0
strcmp("test", "--help")                                                                         = 71
strcmp("test", "--version")                                                                      = 71
fputs_unlocked(0x7fff2bb3f1d3, 0x7f50af982160, 0, 45)                                            = 1
putchar_unlocked(10, 116, 0x7f50afba6004, 0xfbad2a84test
)                                            = 10
exit(0 <unfinished ...>
__fpending(0x7f50af982160, 0, 4, 0x7f50af982cf0)                                                 = 0
ferror_unlocked(0x7f50af982160, 0, 4, 0x7f50af982cf0)                                            = 0
fileno(0x7f50af982160)                                                                           = 1
__freading(0x7f50af982160, 0, 4, 0x7f50af982cf0)                                                 = 0
__freading(0x7f50af982160, 0, 2052, 0x7f50af982cf0)                                              = 0
fflush(0x7f50af982160)                                                                           = 0
fclose(0x7f50af982160)                                                                           = 0
__fpending(0x7f50af982080, 0, 0, 0)                                                              = 0
ferror_unlocked(0x7f50af982080, 0, 0, 0)                                                         = 0
fileno(0x7f50af982080)                                                                           = 2
__freading(0x7f50af982080, 0, 0, 0)                                                              = 0
__freading(0x7f50af982080, 0, 4, 0)                                                              = 0
fflush(0x7f50af982080)                                                                           = 0
fclose(0x7f50af982080)                                                                           = 0
+++ exited (status 0) +++
```

[Ltrace 内部机制](https://www.kernel.org/doc/ols/2007/ols2007v1-pages-41-52.pdf)描述了`ltrace`的实现机制。

### SystemTap

SystemTap提供了一套底层工具用于trace/probe。用户编写SystemTap script语言的程序，SystemTap将其翻译为C代码，再编译成临时的内核模块。内核模块加载时SystemTap script脚本里的hook就会在特定event发生时执行。当SystemTap脚本停止运行时，相应的hook就被删除，移除临时的内核模块。这一整套流程都是通过一个简单的CLI程序`stap`驱动的。

SystemTap使用前的配置过程比较复杂，需要特制的内核，开启`CONFIG_KPROBES=y`、`CONFIG_DEBUG_INFO=y`等诸多内核编译选项。

比如如下的简单脚本就能显示各进程调用`net/socket.c`内函数的情况：

```text
probe kernel.function("*@net/socket.c").call {
  printf ("%s -> %s\n", thread_indent(1), ppfunc())
}
probe kernel.function("*@net/socket.c").return {
  printf ("%s <- %s\n", thread_indent(-1), ppfunc())
}
```

### perf

```bash
perf record -e probe_a:main -e probe_a:main_1 /home/ray/tmp/a
perf annotate
sudo perf probe -x ~/tmp/a 'main%return %ip %sp'
sudo perf record -e probe_a:main -e probe_a:main_1 /home/ray/tmp/a && sudo perf script
```

可执行文件不能在tmpfs分区。

```bash
A=~/tmp; cc -xc <(echo 'main(){}') -Wl,-rpath,$A -o a && sudo perf probe -d '*' || :; sudo perf probe -x $A/libc.so.6 malloc && sudo perf record -e probe_libc:malloc -aR ./a && sudo perf report -n
```

### 其他

书里还介绍了很多神奇的玩意儿，比如`kaho`，用于读取被编译器优化掉的变量；`livepatch`，运行时动态修改变量、替换函数等。这两个工具我在网上检索了下，感觉是个proof of concept的东西，也没有更新了。不过这些思路很奇特，想到了并试图去解决调试时常受困扰的问题，很棒。
