---
title: 重识 Objective-C Runtime - 看透 Type 与 Value · sunnyxx的技术博客
source: sunnyxx (孙源)
source_key: sunnyxx
source_url: 'http://blog.sunnyxx.com/reunderstanding-runtime-1.html'
original_language: zh
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:6adacc4407e99b05'
translated: n/a
---

> 原文：[重识 Objective-C Runtime - 看透 Type 与 Value · sunnyxx的技术博客](http://blog.sunnyxx.com/reunderstanding-runtime-1.html)　·　sunnyxx (孙源)

# 重识 Objective-C Runtime - 看透 Type 与 Value

2016年8月13日

这是**重识 Objective-C Runtime**系列文章的其中一篇：

- [重识 Objective-C Runtime - Smalltalk 与 C 的融合](http://blog.sunnyxx.com/2016/08/13/reunderstanding-runtime-0/)
- [重识 Objective-C Runtime - 看透 Type 与 Value](http://blog.sunnyxx.com/2016/08/13/reunderstanding-runtime-1/)
- 重识 Objective-C Runtime - 何为对象何为类
- 重识 Objective-C Runtime - Calling Conventions
- 重识 Objective-C Runtime - 能写完上面的就不错了

## 看透 Type 与 Value

对于 C 语言来说，Type 就个比较虚幻的东西，它唯一的目的便是**让编译器知道一段数据的长度，来决定如何存取**，举个例子：

```c
int i = 123;
char c = (char)i;
```

这段代码声明了一个 int 类型的变量和一个 char 类型的变量，有初始化和类型强转过程，在 x86_64 架构下，这两行代码的汇编如下：

```c
movl $123, -4(%rbp)
movl -4(%rbp), %eax
movb %al, %cl
movb %cl, -5(%rbp)
```

汇编看起来混乱，但却能最真实的反映出程序的运行过程，逐行解释下：

`movl $123, -4(%rbp)`：move 指令就是简单的值拷贝，这条指令中出现的 `movl` 表示按低 32 位的长度来拷贝（也就是一个 int 的长度），与之相似的还有 8 位的 `movb`（char）、16 位的 `movw` (short)、64 位的 `movq` (long in 64) 等；`$123` 即字面常量值；`-4(%rbp)` 代表 base pointer - 栈基地址寄存器，偏移 4 字节的位置。这个指令执行后内存如下所示：  
![屏幕快照 2016-07-27 下午10.32.46](http://blog.sunnyxx.com/media/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202016-07-27%20%E4%B8%8B%E5%8D%8810.32.46.png)

`movl -4(%rbp), %eax`：将刚才 4 字节长度内存赋值给 `%eax` 寄存器，它是最常用的通用寄存器之一，名为 accumulator，在 64 位架构下，`rax` 表示这个寄存器的完全体，`eax` 表示它的低 32 位，`ax` 表示低 16 位，`ah` 表示第 8~16 位，`al` 表示最低的 8 位。这样抠门的设计一部分因为兼容历史的 32 架构，一方面也是为了更充分利用寄存器这个宝贵的资源：

![屏幕快照 2016-07-27 下午10.51.59](http://blog.sunnyxx.com/media/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202016-07-27%20%E4%B8%8B%E5%8D%8810.51.59.png)

`movb %al, %cl`: 按 8 位长度 (char) 将 a 寄存器的最低 8 位移动到 c 寄存器（count register）的低 8 位。这一个指令就在做 int 到 char 的类型转换，把 123 存在寄存器的低 32 位上，再把寄存器的最低 8 位取出来，相当于把 00000000000000000000000001111011 截断成了 01111011。

`movb %cl, -5(%rbp)`: 最后，再把刚才的结果按 8 字节的长度拷贝到 %rbp 偏移 5 的位置，完成这个 char 类型栈变量的赋值：  
![屏幕快照 2016-07-27 下午11.10.45](http://blog.sunnyxx.com/media/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202016-07-27%20%E4%B8%8B%E5%8D%8811.10.45.png)

因此，对于 C 这种静态语言，Type 信息只用于编译器解析，除了静态检查外还影响生成：

1. 相应长度的指令 (是 movq、movl 还是 movb ?)
2. 寄存器长度的选用（是 rax、eax 还是 al ?）
3. 栈变量内存大小的确定，也可以说是 sp 的位置（ sp 表示 Stack Pointer， 它和 Base Pointer 配合管理栈内存的分配与回收，所谓“分配”栈内存只是用如 `subq $32, %rsp` 的指令将 sp 向低地址移动）

然而，对于动态语言，Type 不仅在编译期起到上述作用，**还需要保留到运行时，让动态调用得以实现**，被称作 `Type Encodings`，对于 Objective-C 所有 Type 的编码，都可以在[这个官方文档](https://developer.apple.com/library/mac/documentation/Cocoa/Conceptual/ObjCRuntimeGuide/Articles/ocrtTypeEncodings.html)中查到，里面的编码和用 `@encode()` 生成的一致，比如：

```plain
@encode(int) => "i"
@encode(float) => "f"
@encode(id) => "@"
@encode(SEL) => ":"
@encode(CGRect) => "{CGRect={CGPoint=dd}{CGSize=dd}}" // 64
```

Objective-C Class 中每个实例变量的 Type 信息全部被编码，Runtime 也提供了 `ivar_getTypeEncoding` 来访问。  
同时，为支持消息的转发和动态调用，Objective-C Method 的 Type 信息也被以 “返回值 Type + 参数 Types” 的形式**组合编码**，还需要考虑到 `self` 和 `_cmd` 这两个隐含参数：

```plain
- (void)foo; => "v@:"
- (int)barWithBaz:(double)baz; => "iv@:d"
```

> 注：上面的方法的 Encoding 使用新的格式，旧的格式中包含调用栈大小和布局信息，如 `i24@0:8i16i20`，表示调用栈帧共 24 字节大小，后面每个参数跟着的数字表示该参数在调用栈的偏移值，在 x86_64 和 ARM 成为主流后，调用的 Calling Conventions 发生巨大变化，开始借助寄存器传参，所以在“参数压栈”时代的这种编码方式逐渐被废弃。

方法的编码可以使用 `method_getTypeEncoding` 获取，在 Cocoa 层，被 `NSMethodSignature` 封装，并提供了一些便捷的解析方法。

多说一句，纯 Swift 声称自己是静态的语言，因为在编译后，任何结构都会被 `Name Mangling` 压缩成一个符号，比如下面的方法：

```swift
class Sark {
    func foo(bar: Int) -> Int {
        return bar;
    }
}
```

经过 Name Mangling 的符号是 `_TFC12TestSwift4Sark3foofT3barSi_Si`，虽然把结构都拍扁了，但该有的信息都在，Module、Class、Method、参数和返回值类型等，按照一定的格式进行了编码，感兴趣可以看[这篇文章](https://mikeash.com/pyblog/friday-qa-2014-08-15-swift-name-mangling.html)。

既然 Swift 已经把类型信息带入到了 Runtime，那么理论上就可以对它进行动态的调用，[https://github.com/sunnyxx/PatchSwiftDemo](https://github.com/sunnyxx/PatchSwiftDemo)

## ABI

## Tagged Pointer

值类型对象  
po 12071766408378668855

# Function

## Name Mangling

# Message

class 可以作为 UITableViewDataSource 么

runtime = type + value + call

type-\> function name + arg type + ret type  
name mangling  
function name -\> c (dlsym) swift -\> github objc -\> SEL

# References

[https://zh.wikipedia.org/wiki/Objective-C](https://zh.wikipedia.org/wiki/Objective-C)  
[http://web.cecs.pdx.edu/~harry/musings/SmalltalkOverview.html](http://web.cecs.pdx.edu/~harry/musings/SmalltalkOverview.html)
