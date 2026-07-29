---
title: 常见操作的性能比较：iPhone 版
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/performance-comparisons-of-common-operations-iphone-edition.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:1eb6964cef389d6c'
translated: true
---

> 原文：[Performance Comparisons of Common Operations, iPhone Edition](https://www.mikeash.com/pyblog/performance-comparisons-of-common-operations-iphone-edition.html)　·　mikeash.com Friday Q&A

发布于 2008-03-19 21:40 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([全文 feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇文章：[Deconstructing the iPhone SDK: Malware](https://www.mikeash.com/pyblog/deconstructing-the-iphone-sdk-malware.html)  
上一篇文章：[Use strnstr](https://www.mikeash.com/pyblog/use-strnstr.html)  
标签：[cocoa](https://www.mikeash.com/pyblog/?tag=cocoa) [iphone](https://www.mikeash.com/pyblog/?tag=iphone) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec) [performance](https://www.mikeash.com/pyblog/?tag=performance)

常见操作的性能比较：iPhone 版

作者：[Mike Ash](https://www.mikeash.com/)

作为对比，你可能希望查看最初那篇[《常见操作的性能比较》](https://www.mikeash.com/pyblog/performance-comparisons-of-common-operations.html)及其后续文章[《常见操作的性能比较：Leopard 版》](https://www.mikeash.com/pyblog/performance-comparisons-of-common-operations-leopard-edition.html)。本测试使用的源代码可[在此处](http://www.mikeash.com/perf_iphone.mm)获取。

以下是时间数据：

| 名称 | 迭代次数 | 总时间（秒） | 每次时间（纳秒） |
|---|---|---|---|
| C++ 虚方法调用 | 1000000000 | 80.8 | 80.8 |
| IMP 缓存消息发送 | 1000000000 | 85.4 | 85.4 |
| 浮点数除法 | 100000000 | 13.4 | 134.4 |
| 整数除法 | 1000000000 | 139.5 | 139.5 |
| 16 字节 memcpy | 100000000 | 17.6 | 175.7 |
| Objective-C 消息发送 | 1000000000 | 192.9 | 192.9 |
| 带整数转换的浮点数除法 | 100000000 | 19.3 | 193.0 |
| NSInvocation 消息发送 | 10000000 | 19.0 | 1899.0 |
| 16 字节 malloc/free | 100000000 | 198.8 | 1988.4 |
| NSObject alloc/init/release | 10000000 | 118.8 | 11883.6 |
| NSAutoreleasePool alloc/init/release | 10000000 | 172.7 | 17272.9 |
| 16MB malloc/free | 100000 | 3.1 | 30754.5 |
| 读取 16 字节文件 | 100000 | 51.1 | 511041.3 |
| 零秒延迟 perform | 100000 | 67.5 | 674994.5 |
| pthread create/join | 10000 | 8.0 | 802160.2 |
| 写入 16 字节文件（原子操作） | 10000 | 51.5 | 5153943.7 |
| 写入 16 字节文件 | 10000 | 80.9 | 8089726.2 |
| 1MB memcpy | 10000 | 81.3 | 8130009.1 |
| 读取 16MB 文件 | 100 | 137.6 | 1376092573.3 |
| 写入 16MB 文件（原子操作） | 30 | 143.8 | 4793527088.9 |
| 写入 16MB 文件 | 30 | 151.2 | 5038515361.1 |

请注意，与原始测试套件相比，本测试套件有所缩减。NSTask 和 NSButtonCell 不存在，因此移除了那些测试。理论上可以用替代项替换，但我没有费心去做。

首先引人注目的是，与原始测试中使用的 Mac Pro 相比，底层操作的速度差异巨大。当然，我不会指望一款手持设备能与现代桌面电脑竞争，但反差仍然惊人。最差的是 IMP 缓存消息发送，在 iPhone 上慢了超过一百倍。

同样有趣的是，C++ 虚方法调用的时间优于 IMP 缓存消息发送。我会假设这个差异在误差范围内，实际上两者速度相同。这仍然是一个有趣的结果，因为 C++ 虚方法调用比调用 IMP 涉及更多的间接寻址。我猜测 ARM 架构包含一条原生处理这种间接寻址的指令；有熟悉 ARM 的人愿意评论一下吗？

另一对有趣的比较是整数除法和浮点数除法。在 iPhone 上它们似乎速度相同，但在 Mac Pro 上浮点数除法大约慢 3.5 倍。这使得 iPhone 上的浮点数除法仅仅慢了 15 倍。

结果还显示，原子文件写入比非原子写入更快。除了测试误差，我对此没有别的解释，但 16 字节文件的时间差异相当大。写入 16 字节文件需要 5-8 毫秒，这个时间大得出奇。在这种尺寸下，寻道时间应该完全占主导地位，而闪存几乎没有寻道时间，所以我不明白这个数字为什么会这么大。也许是 CPU 性能为此付出了巨大代价。16MB 测试显示持续写入速度约为 3MB/s，还算不错。

1MB memcpy 测试揭示出大约 120MB/s 的可用内存带宽。考虑到[片上 RAM](http://www.semiconductor.com/resources/reports_database/view_device.asp?sinumber=18016)，我对这个数值如此之低有点惊讶，但即便如此，它与系统的其他部分大致相当。

总体而言，这台小机器短期内不会取代 Mac Pro，但对于一台在成本、电池使用和散热方面受到如此限制的口袋大小的电脑来说，它并不算差。现在，要是 Apple [能让我往上面装软件](http://www.rogueamoeba.com/utm/2008/03/07/code-signing-and-you/)就好了。

喜欢这篇文章吗？我正出售装满此类文章的整套书籍！第 II 卷和第 III 卷现已上市！提供 ePub、PDF、印刷版，以及 iBooks 和 Kindle 版本。[点击此处了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[此页面的评论 RSS feed](https://www.mikeash.com/commentsrss.py?page=pyblog/performance-comparisons-of-common-operations-iphone-edition.html)

发表想法，添加评论：

垃圾评论和离题帖子将被删除，恕不另行通知。违规者可能由我酌情公开羞辱。
