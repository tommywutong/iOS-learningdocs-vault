---
title: 在 iOS 上调试文件损坏
source: Meta Engineering — iOS
source_key: fbeng
source_url: 'https://engineering.fb.com/2014/08/12/ios/debugging-file-corruption-on-ios/'
original_language: en
published: 2014-08-12
status: active
license: © Meta → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:deb8e696bf3d7b5f'
translated: true
---

> 原文：[Debugging file corruption on iOS](https://engineering.fb.com/2014/08/12/ios/debugging-file-corruption-on-ios/)　·　Meta Engineering — iOS

大规模运作的能力是 Facebook 工程中最令人兴奋的部分之一。然而，随着规模扩大，某些基础编程挑战必然变得更加困难。例如，调试本身就很困难，即使你能够可靠地重现问题——而当在快速变化的代码库中调试一个高度可见但不确定的问题时，难度会进一步增加。最近，我们解决了一个长期的移动端调试问题，并将 Facebook for iOS App 的崩溃率降低了超过 50%。

几个月前，我们在 iOS 上的一个主要崩溃出现在 Apple 的 Core Data 系统中，这是一个面向底层数据库（SQLite）的对象关系映射器（object-relational mapper）。我们收到了来自崩溃报告分析器的这些崩溃，但花了几个月才找到解决问题的正确方向。通过使用 [Hipal](https://www.facebook.com/note.php?note_id=114588058858) 和 [Scuba](https://www.facebook.com/publications/148418812023978/) 查询并聚合报告，我们发现 Core Data 错误码编号有六种不同的表现形式。

首先，我们尝试确定问题何时开始出现。我们当时有月度发布周期，但每个版本通常有数百名开发者提交代码。虽然我们能够缩小时间范围，但无法将问题隔离到少于几千次提交的范围内。我们也无法将自己限制在仅检查提交变更上。随着多个 [A/B 测试](https://engineering.fb.com/posts/520580318041111/airlock-facebook-s-mobile-a-b-testing-framework/) 在每个版本中不断变化，我们无法验证变更与代码有关还是与配置有关。

由于潜在原因的范围如此广泛，我们接下来致力于收集假设。我们提出了多种不同的理论，涉及竞态条件（race condition）情况、架构变更，甚至包括错误的基础前提。例如，“Core Data 总是被标记为问题所在，但也许它并不是根本原因。”考虑到这一点，我们找到了一段受影响的代码，可以轻松地将 Core Data 切换到 SQLite，从而开始测试我们的假设。

在将 SQLite 变更推送到开发环境后不久，我们收到了新代码的损坏崩溃报告。这是我们的第一个突破！我们查看了 SQLite 提供的潜在原因列表，第一个提到的原因是“由恶意线程（rogue thread）或进程覆写文件” [http://sqlite.org/howtocorrupt.html]。考虑到问题的发生频率以及我们代码变更简化的访问模式（串行化、易于推理、线程安全），我们找到了合理的原因。

接下来，我们需要在一个庞大的代码库中找到那个“恶意线程或进程”。我们决定在打开 SQLite 文件之前，先打开一个蜜罐文件（honeypot file）。如果有人写入这个文件，我们就有了假设的证明和破坏者的输出。然后我们会将损坏的文件附加到崩溃报告中进行分析。

第二天，我们收集了所有崩溃报告的附件数据。使用十六进制分析器，我们发现附件有一个共同的前缀：`17 03 03 00 28`。然后，我们使用 `lldb` 设置了一个条件断点，以识别谁向 POSIX 的 `write()` 命令发送了“类似”的内容：

```
breakpoint set -n write -c "(*(char**) ($esp + 8))[0]==0x17 
    && (*(char**) ($esp + 8))[1]==0x03 
    && (*(char**) ($esp + 8))[2]==0x03 
    && (*(char**) ($esp + 8))[3]==0x00
    && (*(char**) ($esp + 8))[4]==0x28"
```

我们在模拟器里稍微浏览了一下 Facebook——然后“砰”——我们的 SPDY 网络栈（networking stack）命中了好几个断点。

我们现在有了间接证据，接下来我们需要直接证据来证明网络栈写入了错误的地方。一旦检测到，我们知道应该同步中止进程并分析有问题的栈回溯（stack trace）。为了实现这一点，我们需要拦截 POSIX 系统调用（system call）中的 `write` 系列（`write`、`writev`、`pwrite`）。我们决定使用 [Fishhook](https://github.com/facebook/fishhook)，这是我们的同事去年开发并开源的一个项目，可以轻松地重新绑定（rebind）系统 API。

```
// 设置一个蜜罐文件
int trap_fd = open(…); 
// 创建新函数来检测对蜜罐文件的写入
static WRITE_FUNC_T original_write = dlsym(RTLD_DEFAULT, "write");;
ssize_t corruption_write(int fd, const void *buf, size_t size) { 
  FBFatal(fd != trap_fd, @"Writing to the honeypot file");
}
return original_write(fd, buf, size);
}
// 将系统的 write 替换为我们的“检查版本”
rebind_symbols((struct rebinding[1]){{(char *)"write", (void *)corruption_write}}, 1);
```

我们提交了这段代码，第二天就收到了指向网络栈的新崩溃报告。SSL 层正在写入一个已经关闭、随后被重新分配给我们的数据库文件的套接字（socket）。物证确凿！

最后，我们需要分析有问题的代码以寻找解决方案。我们的文件描述符（file descriptor）持有策略看起来存在问题。虽然 SPDY 为我们的数据库使用了推荐的 CFSocket 封装，但 SSL 层没有。SSL 层直接处理原始的文件描述符，因此其生命周期管理没有自动同步。SPDY 套接字在 SSL 之前关闭，创建了一个竞态窗口，在这个窗口中，写入操作会进入一个“幸运地”获得了与刚刚关闭的套接字相同文件描述符的文件。

我们与网络团队合作，在几小时内修复了这个问题。这个修复将 Facebook iOS App 的崩溃率减半，并解决了一个长期存在的问题。事实证明，放弃手动代码分析是一个好策略。这个 bug 是由现有代码暴露出来的，随着我们为所有用户逐步启用默认的安全连接，这些代码被更频繁地执行。

处理庞大且快速演变的代码库有时会让人不知所措。像分析崩溃和理解代码这样的日常任务可能会变成它们自己的编程挑战。在这些时刻，共同协作、集思广益以及依靠计算机编程基础至关重要。祝你调试顺利！

_Slobodan Predolac 和 Nicolas Spiegelberg，他们在纽约市热衷于构建稳固的 Facebook iOS 基础设施。_
