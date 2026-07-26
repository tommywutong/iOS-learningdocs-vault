---
title: Calling Conventions in Cocoa - 重识函数 · sunnyxx的技术博客
source: sunnyxx (孙源)
source_key: sunnyxx
source_url: 'http://blog.sunnyxx.com/objc-calling-conventions.html'
original_language: zh
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:30e36f98c2a38af2'
translated: n/a
---

> 原文：[Calling Conventions in Cocoa - 重识函数 · sunnyxx的技术博客](http://blog.sunnyxx.com/objc-calling-conventions.html)　·　sunnyxx (孙源)

# Calling Conventions in Cocoa - 重识函数

2016年5月21日

从最开始学 C 语言，写下 `printf("hello world")` 的时候，**函数**就成了脑海中编程的基本元素，只要严格按照函数原型调用，它就能乖乖的给你正确的结果；本系列文章将带大家重新审视这背后发生的事情，一步步看清函数和函数的调用过程背后的灵魂：`Calling Conventions`，悉数一下它在 Cocoa 中留下的痕迹。

这是系列文章中的一篇：

- [Calling Conventions - 初识](http://localhost:4000/2016/05/21/objc-calling-conventions/)
- Calling Conventions - va_list
- Calling Conventions - objc_msgSend
- Calling Conventions - NSInvocation 与 NSMethodSignature 的勾当
- Calling Conventions - libffi 大杀器

`Calling Conventions` 描述了一个问题，**函数调用是如何发生的？**

平时发呆时候，总喜欢脑洞一些很扯的问题，比如：我们是不是生活在一个模拟器里？时间的最小尺度是不是模拟器 CPU 的一个时钟周期？观察就会导致量子态塌陷其实是模拟器的 lazy calculation - -？再比如说，程序是由编译器编译出来的，但编译器本身也是个程序，那它喵的最开始的编译器是谁编译的呢？时不时码农癌发作，就得赶紧去写几个 bug 压压惊。

所以搞物理的和搞计算机的是两个目标相反的职业：程序员们从让机器执行最简单的指令开始，搞出汇编、搞出函数、搞出高级语言、搞出人工智能，妄图一步步模拟出整个世界；而物理学家就跟逆向工程师似的，从观察宏观现象，到在对撞机中互怼微观粒子，再到迷之量子力学，妄图一步步反推出万物本源；所以写码混饭的时候，还真得感谢被我们踩在脚下，在计算机大楼打地基的一辈人，感谢最初用机器码人肉裸写出编译器的前辈们。

本文在 Objective-C 语境下，对计算机大楼地基中的 `Calling Conventions` 进行研究和介绍，它描述了**函数调用**所遵循的基本原则，了解之后，可以让我们对 iOS 一些机制的理解变的更加清晰，如：可变参数、`objc_msgSend` 为何这样实现、`NSInvocation` 是干嘛的、`NSMethodSignature` 存在的意义、`libffi` 等，下面细细讲来。

## CPU 后厨

要理解 Calling Conventions 就需要先理解程序运行的机制，不妨把

![QQ20121204-1](http://blog.sunnyxx.com/media/QQ20121204-1.png)

不论学任何一种语言，都是从在 `main` 函数中用一个 `print` 函数打印 `"Hello World"` 开始，隐射出**函数是高级语言的基本元素之一**，但我们知道，高级语言的代码会被编译器编译成更低级的汇编指令，进而按指令的对应表翻译成机器认识的 010101 二进制形式

程序逻辑由函数组成，函数由细碎的 CPU 指令集，更背后的背后，是 CPU 如何通过电信号

![68f6e545jw1f2wk2c6g77j20gt0gu766](http://7xtel4.com1.z0.glb.clouddn.com/2016-04-26-68f6e545jw1f2wk2c6g77j20gt0gu766.jpg)

![68f6e545jw1f2wk2l3hujj20gt0cmwgs](http://7xtel4.com1.z0.glb.clouddn.com/2016-04-26-68f6e545jw1f2wk2l3hujj20gt0cmwgs.jpg)

相信 `Calling Conventions` 对多数 iOS 开发者来说都是个陌生概念，它深藏程序之中，几乎感知不到它的存在，但如可变参数、NSInvocation、NSMethodSignature、objc_retainAutorelease 甚至 objc_msgSend 都和它有或多或少的关系

是函数调用的灵魂所在，这篇文章将在 iOS 和 Objective-C 的范畴中简单介绍下 Calling Conventions，同时，一些有意思的机制也将得以解释：

- 可变参数是什么，va_list 如何实现
- objc_msgSend 为何用汇编实现
- NSInvocation 与 NSMethodSignature
- objc_retainAutorelease 的里应外合实现
- 动态反射调用 c 方法与 libffi

## Calling Conventions 是干嘛用的

> a calling convention is an implementation-level (low-level) scheme for how subroutines receive parameters from their caller and how they return a result.

它约定了（包括但不限于）：

- 入参和返回值存放的位置和规则：用 register（寄存器）还是用 stack（栈内存）还是某种组合方式传递、参数个数和类型不同时如何存放（取决于一个值的长度能否被寄存器的长度容下，如一个较大的 struct 的返回方式不同于一个 int 的返回方式）
- 参数的传递顺序  
  -

从刚开始学 C 语言的时候，就在接触函数。只要看到它的声明，就知道了函数名、入参类型、返回值类型：

```c
int addUp2(int first, int second);
```

进而就能够轻松的进行函数调用：

```c
void test() {
  int result = addUp2(233, 666); // 233 + 666 = 899
}
```

一切都非常自然，而背后却是 `Calling Conventions` 定义的规则：

1. C 代码编译后，被揉碎成一行行过程式的汇编指令，能直接操作的只有 `register`（寄存器）和 `stack`（函数栈内存），对于函数调用只是一个 `call` 指令跳转到函数入口地址，那函数参数如何传递、返回值如何返回给 caller 呢？
2. 光我们能接触到的 Architecture 就有很多种，如 i386（ Mac32位和32位模拟器 ）、x86_64（Mac64位和64位模拟器）、真机 armv7、armv7s、arm64 等，每个架构下 CPU 不同导致汇编指令集也不尽相同，

[http://zhuanlan.zhihu.com/p/19893066](http://zhuanlan.zhihu.com/p/19893066)  
1  
2  
3  
4  
  
``` c  
int add(const char *, ...); // declared in stdio.h  
printf("Hello world: %s\\n", "sunnyxx");

这是如此的自然，而在 Objective-C 中，我们知道这个消息机制的核心函数：

```objc
OBJC_EXPORT void objc_msgSend(void); // declared in message.h
```

往一个对象发送 message 最终会转化成 `objc_msgSend` 的函数调用：

```objc
NSRange range = [@"sunnyxx" rangeOfString:@"xx"];
--> NSRange range = objc_msgSend(@"sunnyxx", (SEL)"rangeOfString:", @"xx");
```

那么，问题就来了：方法千千万万，参数类型、个数，返回值类型都不尽相同，Objective-C 是如何做到用一个简单的 `objc_msgSend` 声明来承载所有函数调用呢？

与之而来的一系列问题：

- 函数定义的作用是什么？
- 参数和返回值是如何传递的？
- 函数调用是如何发生的？
- 可变参数是个什么？
- NSInvocation 和 NSMethodSignature 有何卵用？
- 编译器和 CPU 架构都充当了什么角色呢？

让我们一起来扒一扒。

## 汇编视角

要探索 C 语言的函数调用机制，就要从更底层的汇编入手。在 `main.c` 中写一段简单的测试代码：

```c
int add(int a, int b) {
    return a + b;
}
int main() {
    int result = add(233, 666);
    return 0;
}
```

有两种方式可以让我们看到汇编代码，一种是利用 Xcode 的 `Show the Assistant editor` 也就是分成左右两栏的模式，然后点开右边栏上方的下拉菜单，选择 `Assembly`，就能看到左边源码对应的汇编代码了；也可以使用命令行来编译源文件生成汇编：

```bash
$ clang -S -arch x86_64 main.c -o main_x86_64.s
```

其中 `-S` 表示生成汇编代码，`-arch x86_64` 指定在 `x86_64` 架构下编译，`-o` 表示 output 到哪个文件。  
于是乎我们就得到了一大片看不懂的汇编代码，将其中函数调用部分的代码整理出来：

```c
_main:
  pushq	%rbp
  movq	%rsp, %rbp
  subq  $16, %rsp
  movl	$233, %eax
  movl	$666, %ecx
  movl  $0, -4(%rbp)
  callq _add
  // ...
_add:
  pushq	%rbp
  movq	%rsp, %rbp

  movl	%edi, -4(%rbp)
  movl	%esi, -8(%rbp)
  movl	-4(%rbp), %esi
  addl	-8(%rbp), %esi
  movl	%esi, %eax

  popq	%rbp
  retq
```

首先可以清楚的观察到，我们写的 C 函数的被 [Name Mangling](https://en.wikipedia.org/wiki/Name_mangling) 转化成前面加下划线的形式，以 Label 的形式出现，很像 `goto` 语句的那个 Label；然后看到一行行的汇编代码，每一行的格式比较固定，像 `pushq` 这样放在前面的是汇编指令，像 `%rbp` 带百分号的是寄存器，像 `$233` 带美元符号的是立即数，所以这些汇编代码完全可以理解成一个个基本函数的调用，其中的指令和寄存器命名可以查阅[官方手册](http://www.x86-64.org/documentation/assembly.html)，下面就逐行解释一下汇编代码：

```c
_main:
  pushq	%rbp
  movq	%rsp, %rbp
```

`%rbp`（ Frame Base Pointer ）是栈基地址寄存器，`%rsp` ( Frame Stack Pointer ) 栈顶地址寄存器，这俩货是栈内存管理的核心，每当进入一个函数时：

1. 用 `pushq` 指令将历史的 `%rbp` 保存起来，腾出这个寄存器
2. 用 `movq` 指令将 `%rsp` 的值赋值给 `%rbp`，让基地址指向栈顶
3. 在函数 return 前使用对应的 `popq` 回收栈内存。

`%rsp` ( Frame Stack Pointer ) 负责记录栈内存的栈顶地址，和上面的 `%rbp` 配合，一个负责栈底一个负责栈顶；`movq` 指令就是个简单的赋值操作，相当于 `%rbp = %rsp`，

## References

[https://developer.apple.com/library/mac/documentation/DeveloperTools/Conceptual/LowLevelABI/130-IA-32_Function_Calling_Conventions/IA32.html](https://developer.apple.com/library/mac/documentation/DeveloperTools/Conceptual/LowLevelABI/130-IA-32_Function_Calling_Conventions/IA32.html)  
[https://en.wikipedia.org/wiki/Calling_convention](https://en.wikipedia.org/wiki/Calling_convention)  
[https://msdn.microsoft.com/en-us/library/ms235286.aspx](https://msdn.microsoft.com/en-us/library/ms235286.aspx)

[https://www.mikeash.com/pyblog/friday-qa-2011-12-16-disassembling-the-assembly-part-1.html](https://www.mikeash.com/pyblog/friday-qa-2011-12-16-disassembling-the-assembly-part-1.html)  
[https://www.raywenderlich.com/37181/ios-assembly-tutorial](https://www.raywenderlich.com/37181/ios-assembly-tutorial)  
[https://www.mikeash.com/pyblog/friday-qa-2013-03-08-lets-build-nsinvocation-part-i.html](https://www.mikeash.com/pyblog/friday-qa-2013-03-08-lets-build-nsinvocation-part-i.html)  
[http://arigrant.com/blog/2014/2/12/why-objcmsgsend-must-be-written-in-assembly](http://arigrant.com/blog/2014/2/12/why-objcmsgsend-must-be-written-in-assembly)  
[http://eli.thegreenplace.net/2011/09/06/stack-frame-layout-on-x86-64/](http://eli.thegreenplace.net/2011/09/06/stack-frame-layout-on-x86-64/)
