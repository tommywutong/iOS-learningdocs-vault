---
title: objc_msgSend
source_url: 'https://ridiculousfish.com/blog/posts/objc_msgsend.html'
source_domain: ridiculousfish.com
source_group: single-site
original_language: en
published: ''
archived_at: 2026-07-27
content_hash: 'sha256:ac5d70304bdfb203'
plan_ref: 第三周：Runtime 行为与 Cocoa 对象通信 / Day 1｜把方法调用还原为“查找行为”（对应 W1-03）
plan_week: 第三周：Runtime 行为与 Cocoa 对象通信
plan_day: Day 1｜把方法调用还原为“查找行为”（对应 W1-03）
container: '//div[contains(@class,''content'')]'
container_source: guess
---

> 原文：[objc_msgSend](https://ridiculousfish.com/blog/posts/objc_msgsend.html)

发送消息可以很有趣！你要做的就是把它变成一个游戏。你可能会问，什么样的游戏？比如，我们可以看看在四秒内能发送多少条消息，然后试着打破那个记录。（向 Bart 和 Skinner 校长致歉。）

Objective-C 是一门动态语言。当你向一个对象发送消息时，gcc 会发出对 `objc_msgSend()` 或其类似专用函数的调用。由于每条 Objective-C 消息发送都流经 `objc_msgSend()`，因此尽可能让 `objc_msgSend()` 快速运行是一个优先事项。让我们看看它有多快，以及我们能否做得更好。

### 分析 objc_msgSend()

我写了一些代码，看看在四秒内 Objective-C 能调用一个方法多少次。我使用 `alarm()` 函数设置了一个闹钟。然后我在一个循环中向一个对象发送 increment 消息，直到收到信号 `SIGALRM`，这时我输出方法运行的次数并退出。我使用 Tiger 上的 gcc4 和 `-O3` 优化级别编译了它。这是[我的 Objective-C 代码](https://ridiculousfish.com/blog/misc/objc_msg_send_test.html)。

在三次运行的平均值上，我测得了每秒 25681135 条消息。还行。

正如 Skinner 所说，让我们试着打破那个记录！我们从分析开始。我在 OS X 上最喜欢的分析工具当然是 [Shark](http://developer.apple.com/tools/sharkoptimize.html)。让我们在我们的可执行文件上运行它。好了，[结果出来了](https://ridiculousfish.com/blog/images/objc_msgSend_Shark.png)。Shark 显示 16% 的时间花在了 increment 方法本身，34% 的时间花在了 `dyld_stub_objc_msgSend()` 中，48% 花在了 `objc_msgSend()` 自身。这个 `dyld_stub_objc_msgSend()` 函数是什么，为什么它占了这么多时间？

你可能已经知道了。`objc_msgSend()` 是从一个动态库（即 `libobjc`）动态链接的。为了调用真正的 `objc_msgSend()`，代码会跳转到一个 stub 函数 `dyld_stub_objc_msgSend()`，它负责加载真正的 `objc_msgSend()` 方法并跳转到它。正如你所见，这个 stub 函数相对昂贵。如果我们能消除对它的需求，我们就能看到高达 33% 的性能提升。

### 攻击计划

有一种方法可以摆脱它。与其通过 stub 函数跳转，不如获取一个指向 `objc_msgSend()` 本身的指针，并始终通过该指针调用 `objc_msgSend()`。实际上，这与内联 stub 没有太大区别。

说起来容易做起来难！我们要怎么做呢？嗯，我们可以手动编辑这个小基准测试的汇编代码，甚至摆弄 C 代码，但这太刻意了。如果能让 gcc 替我们做这个工作就好了。

没错，我们要 hack gcc。欢迎下载它并和我一起做！或者只是间接地跟随。对于我提到的每个源文件，我会给出它在刚下载文件中的路径，以及它在 Apple 开源网站上的链接。

### 获取源码

下载并解压 [Apple 最新发布的 gcc 公开版本](http://www.opensource.apple.com/darwinsource/tarballs/other/gcc-4061.tar.gz)。在撰写本文时，它是 gcc-4061。把它放在有足够空间的卷上。完全构建后，gcc 将占用近 1.1 GB 的空间。

### 构建源码

全部解压完了？很好。打开 `gcc-4061` 目录下的 `README.Apple`。它告诉你运行两个命令：

```
	mkdir -p build/obj build/dst build/sym
        gnumake install RC_OS=macos RC_ARCHS=ppc TARGETS=ppc \
                SRCROOT=`pwd` OBJROOT=`pwd`/build/obj \
                DSTROOT=`pwd`/build/dst SYMROOT=`pwd`/build/sym
```

猜怎么着？你来运行这些命令。（注意那是反引号，不是单引号！）然后去喝杯咖啡什么的。这可能需要一段时间，但我们只需要做一次。

回来了？完成了吗？还没？好吧，我等着。

### 测试我们的构建

现在完成了？很好。试试看。用 `build/dst/usr/bin/gcc-4.0` 编译一些东西，比如[我的 Objective-C 代码](https://ridiculousfish.com/blog/?page_id=20)。非常简单：

```
gcc-4061/build/dst/usr/bin/gcc-4.0 -O3 -framework Foundation test1.m ; ./a.out
26129493
```

太好了！它工作了！现在让我们看看能否添加我们的优化。

### Hack gcc

好吧。所以计划是获取一个指向 `objc_msgSend` 的指针，把它存储在一个函数指针变量中，并将对动态链接函数 `objc_msgSend()` 的调用替换为通过这个函数指针的跳转。我们可以在编译器中完成这一切，而无需更改基准测试代码的一行，但现在让我们只做最后一部分——替换对 `objc_msgSend()` 的调用。我们将在我们的 Objective-C 代码中设置这个变量，在那里更容易调整。

天哪，这个 gcc 项目可真大得吓人。它是怎么工作的？看起来源代码主体在 `gcc-4061/gcc` 目录下。让我们看看当我们向一个对象发送 Objective-C 消息时，能否弄清楚 gcc 做了什么。我们从 gcc 开始的地方开始，沿着它的控制流深入到它的深处。开始点是什么？嗯，词法分析器/解析器似乎是个合理的选择。grep 搜索 `YACC`……一堆变更日志……啊哈！[/gcc-4061/gcc/c-parse.in](http://www.opensource.apple.com/darwinsource/10.4.2/gcc-4061/gcc/c-parse.in)！

好了，我们进来了。看起来是一个相当标准的语法。这个 `objcmessageexpr` 看起来很值得研究。搜索它——它把我们引向 `objc_build_message_expr()`。grep 搜索它……它在 [/gcc-4061/gcc/objc/objc-act.c](http://www.opensource.apple.com/darwinsource/10.4.2/gcc-4061/gcc/objc/objc-act.c) 中。嘿，看这里——文件顶部说它为 Objective-C 实现了类和消息传递。我们来对地方了。

`objc_build_message_expr()` 调用 `objc_finish_message_expr()` 调用 `build_objc_method_call()` 调用 `build_function_call()`……等等，倒回去。最后一个函数调用看起来实际上是在跳转到 `objc_msgSend()` 函数。找找这个：

```
 return build_function_call (t, method_params);
```

是的！所以这里的 `t` 是函数，要么是 `objc_msgSend()` 要么是一个类似的函数，而 `method_params` 是所有参数。我们想用我们自己的东西替换 `t`——但前提是它不返回结构体且不是调用 super（我们把这些优化留给另一天）。

我们应该怎么称呼我们的信使函数指针呢？我们就叫它 `_messengerFunctionPointer_` 吧！这样就行。你可以随意命名你的，只要你能跟踪它并进行明显的更改。

所以做这个更改。新代码以红色显示。

```
  /* ??? 此刻选择器还不是我们能在编译器内部使用的东西
     暂时设为垃圾值。 */
  t = build (OBJ_TYPE_REF, sender_cast, method, lookup_object, size_zero_node);
  if (sender == umsg_decl) t = lookup_name(get_identifier("messengerFunctionPointer"));
  return build_function_call (t, method_params);
```

好了，这究竟做了什么？嗯，它说如果我们正在做一个普通的消息发送（不返回结构体，不使用 super），则通过变量 `messengerFunctionPointer` 中的任何值来调用，而不是直接调用函数。注意这段代码实际上并*没有*为我们*创建* `messengerFunctionPointer` 变量；那是我们在 C 代码中的特权。

有趣的是，我们钩住了 gcc 的普通变量查找。我们的 `messengerFunctionPointer` 变量可以是局部的、全局的、静态的、外部的等等，只要它在任何发送 Objective-C 消息的代码的作用域内以某种方式可见。

### 我们可以重建它。我们有技术……

就是这样！并没有那么糟糕。所以保存文件并像之前一样重建 gcc。因为它只有一个文件需要重新编译，不会花太长时间。这里，这样你就不用往上滚动了：

```
        gnumake install RC_OS=macos RC_ARCHS=ppc TARGETS=ppc \
                SRCROOT=`pwd` OBJROOT=`pwd`/build/obj \
                DSTROOT=`pwd`/build/dst SYMROOT=`pwd`/build/sym
```

### 更好……更强……更快……

都好了？好吧，让我们试着重新编译我们之前的代码。

```
gcc-4061/build/dst/usr/bin/gcc-4.0 -O3 -framework Foundation test1.m
test1.m: In function 'main':
test1.m:29: internal compiler error: Bus error
```

哎呀！一个内部编译器错误！但当然，它正在寻找我们名为 `messengerFunctionPointer` 的变量，而这个变量并不存在（而且我们没有收到任何警告，因为 gcc 是在它通常会捕获未声明变量之后才寻找这个变量的）。所以让我们把它添加到[我的 Objective-C 代码](https://ridiculousfish.com/blog/?page_id=20)中，并将其指向 `objc_msgSend()`，我们也需要声明后者。

```
...
void signal_handler(int signal) {
        printf("%d\n", gFoo->val);
        exit(0);
}

id objc_msgSend(id, SEL, ...);
id (*messengerFunctionPointer)(id, SEL, ...) = objc_msgSend;

int main(void) {
        Foo* foo = [[Foo alloc] init];
        gFoo = foo;
        signal(SIGALRM, signal_handler);
...
```

```
gcc-4061/build/dst/usr/bin/gcc-4.0 -O3 -framework Foundation test1.m; ./a.out
35099819
```

它成功了！*而且更快了！*我测得了平均每秒 34967726 条消息，提升了 36%——甚至比预测的 34% 还要好。对 Shark 的一次会话显示 `dyld_stub_objc_msgSend()` 已经完全不再被调用了。

### 更多，更多，更多！

我们还能做得更好吗？由于它每次发送消息时都必须加载全局变量的值，如果我们把它设为 `const`，也许能看到更显著的提升？

```
id objc_msgSend(id, SEL, ...);
id (* const messengerFunctionPointer)(id, SEL, ...) = objc_msgSend;
```

```
gcc-4061/build/dst/usr/bin/gcc-4.0 -O3 -framework Foundation test1.m; ./a.out
26488189
```

什么？把我们的变量设为 `const` 反而让代码*变慢了*！这是怎么回事？快速检查汇编发现，gcc 对我们的 `const` 变量执行了常量传播（constant propagation），再次将通过函数指针的调用替换为对 `dyld_stub_objc_msgSend()` 的调用。它撤销了我们所有的辛勤工作！（这证明了 gcc 善意的优化实际上可能使事情变慢。）一个简单的修复方法：

```
id objc_msgSend(id, SEL, ...);
id (* const volatile messengerFunctionPointer)(id, SEL, ...) = objc_msgSend;
```

（天哪，类型限定符！我们不仅找到了 `volatile` 的一个用途，它实际上还让事情变快了！）

这对其他东西有用吗？首先，它允许我们非常快速和动态地在各种信使函数之间切换，包括我们自己的，这样我们就可以做一些技巧，比如额外的日志记录或花哨的消息转发。我们甚至可以做一些疯狂的事情，比如添加[多重分派（multiple dispatch）](http://www.gwydiondylan.org/gdref/tutorial/multiple-dispatch.html)。而且用这种技术构建的程序应该（原则上）向后兼容到足以在旧版本的 OS X 上运行。不幸的是，这个技巧不会影响已经编译好的库，比如 AppKit。

### 更接近真实生活的测试

作为一个更现实的例子，这里有一个简单的程序对[三百万个对象进行排序](https://ridiculousfish.com/blog/misc/objc_msgsend-sorting-example.html)。这个优化（稍微复杂一点）将运行时间从 17.93 秒提升到了 15.7 秒。

顺便说一下，第一个在评论中正确解释为什么我在上面的代码中没有使用 `qsort()` 的人将赢得[我的 click-pen](https://ridiculousfish.com/blog/images/apple_pen.jpg)。对于这份极其廉价的赠品，请使用你真实的电子邮件地址。

### 缺点

有没有不使用这个技巧的理由？有的，很多。首先，我对 gcc 的更改是个拼凑。它会生成一些虚假的警告，并且在某些情况下可能是不正确的。如果有人决定认真实现这个优化，它必须健壮得多。其次，[带位置无关代码的全局变量并不美观](https://ridiculousfish.com/blog/archives/2005/05/29/nil/)，并且如果没有快速访问变量的方法（比如 `-mdynamic-no-pic`，或者把它做成局部变量，或者确保它被缓存在寄存器中），优化的影响将会减小。

### 结论

总结一下，`objc_msgSend()` 有三分之一的时间花在了它的 stub 函数上。通过调整编译器，使其始终通过一个函数指针变量调用 `objc_msgSend()`，我们可以消除这个开销，并为动态修改消息分派开辟一些有趣的可能性。
