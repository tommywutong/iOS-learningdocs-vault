---
title: Matrix-iOS 卡顿监控
source_url: 'https://cloud.tencent.cn/developer/article/1427933'
source_domain: cloud.tencent.cn
source_group: platform
original_language: zh
published: ''
archived_at: 2026-07-27
content_hash: 'sha256:26e771e4942fb12c'
plan_ref: 第五周：RunLoop、AutoreleasePool、响应者链与生命周期 / Day 2｜先会 RunLoop，再理解常驻线程与卡顿监测（对应 W4-03）
plan_week: 第五周：RunLoop、AutoreleasePool、响应者链与生命周期
plan_day: Day 2｜先会 RunLoop，再理解常驻线程与卡顿监测（对应 W4-03）
container: '//div[contains(@class,''rno-markdown'')]'
container_source: map
---

> 原文：[Matrix-iOS 卡顿监控](https://cloud.tencent.cn/developer/article/1427933)

### **前言**

---

在早期开发 iOS 微信的过程中，我们时不时会收到类似的反馈：

- “我的微信卡在主界面，怎么也滑动不了”
- “我的微信从后台切换前台卡了一下，最近偶尔会遇到几次”，等等。

这类问题有个共同点：用户的微信在一段时间内无法点击；即使获得用户的操作路径，也无法重现。

我们把这类问题叫做卡顿问题。这类问题很影响用户的体验，是必须进行解决的。为了精确地定位用户的卡顿问题，iOS 微信在 2014 年 9 月份上线了卡顿监控系统。在这几年间，卡顿监控经历了几次优化，不断成熟，在这里我们将其分享出来。

### **什么是卡顿**

---

卡顿就是在应用使用过程中出现界面不响应或者界面渲染粘滞的情况。而应用界面的渲染以及事件响应是在主线程完成的，出现卡顿的原因可以归结为主线程阻塞。

在开发过程中，遇到的造成主线程阻塞的原因可能是：

- 主线程在进行大量I/O操作：为了方便代码编写，直接在主线程去写入大量数据；
- 主线程在进行大量计算：代码编写不合理，主线程进行复杂计算；
- 大量UI绘制：界面过于复杂，UI绘制需要大量时间；
- 主线程在等锁：主线程需要获得锁A，但是当前某个子线程持有这个锁A，导致主线程不得不等待子线程完成任务。

针对这些问题，如果我们能够捕获得到卡顿当时应用的主线程堆栈，那么问题就迎刃而解了。有了堆栈，就可以知道主线程在什么函数哪一行代码卡住了，是在等什么锁，还是在进行I/O操作，或者是进行复杂计算。有了堆栈，就可以对问题进行针对性解决。

### **原理**

---

在 iOS/macOS 平台应用中，主线程有一个 Runloop。Runloop 是一个 Event Loop 模型，让线程可以处于接收消息、处理事件、进入等待而不马上退出。在进入事件的前后，Runloop 会向注册的 Observer 通知相应的事件。

Runloop 的详细介绍可以网上查阅《深入理解RunLoop》。一个简易的 Runloop 流程如下所示：

![](https://ask.qcloudimg.com/http-save/598196/6kdxk5jhhv.jpeg)

Matrix 卡顿监控在 Runloop 的起始最开始和结束最末尾位置添加 Observer，从而获得主线程的开始和结束状态。卡顿监控起一个子线程定时检查主线程的状态，当主线程的状态运行超过一定阈值则认为主线程卡顿，从而标记为一个卡顿。

![](https://ask.qcloudimg.com/http-save/598196/g1xipfxbt4.jpeg)

目前微信使用的卡顿监控，主程序 Runloop 超时的阈值是 2 秒，子线程的检查周期是 1 秒。每隔 1 秒，子线程检查主线程的运行状态；如果检查到主线程 Runloop 运行超过 2 秒则认为是卡顿，并获得当前的线程快照。

同时，我们也认为 CPU 过高也可能导致应用出现卡顿，所以在子线程检查主线程状态的同时，如果检测到 CPU 占用过高，会捕获当前的线程快照保存到文件中。目前微信应用中认为，单核 CPU 的占用超过了 80%，此时的 CPU 占用就过高了。

### **退火算法**

为了降低检测带来的性能损耗，我们为检测线程增加了退火算法：

- 每次子线程检查到主线程卡顿，会先获得主线程的堆栈并保存到内存中（不会直接去获得线程快照保存到文件中）；
- 将获得的主线程堆栈与上次卡顿获得的主线程堆栈进行比对：

    - 如果堆栈不同，则获得当前的线程快照并写入文件中；
    - 如果相同则会跳过，并按照斐波那契数列将检查时间递增直到没有遇到卡顿或者主线程卡顿堆栈不一样。

这样，可以避免同一个卡顿写入多个文件的情况；避免检测线程遇到主线程卡死的情况下，不断写线程快照文件。

### **耗时堆栈提取**

---

子线程检测到主线程 Runloop 时，会获得当前的线程快照当做卡顿文件。但是这个当前的主线程堆栈不一定是最耗时的堆栈，不一定是导致主线程超时的主要原因。

例如，主线程在绘制一个微信logo，过程如下：

![](https://ask.qcloudimg.com/http-save/598196/y15rq9pn8d.jpeg)

子线程在检测到超出阈值时获得的线程快照，主线程的当前任务是“画小气泡”。但其实“画大气泡”才是耗时操作，导致主线程超时的主要原因。Matrix 卡顿监控通过主线程耗时堆栈提取来解决这个问题。

卡顿监控定时获取主线程堆栈，并将堆栈保存到内存的一个循环队列中。如下图，每间隔时间 t 获得一个堆栈，然后将堆栈保存到一个最大个数为 3 的循环队列中。有一个游标不断的指向最近的堆栈。

微信的策略是每隔 50 毫秒获取一次主线程堆栈，保存最近 20 个主线程堆栈。这个会增加 3% 的 CPU 占用，内存占用可以忽略不计。

![](https://ask.qcloudimg.com/http-save/598196/v2o1c5rv5a.jpeg)

当主线程检测到卡顿时，通过对保存到循坏队列中的堆栈进行回溯，获取最近最耗时堆栈。

如下图，检测到卡顿时，内存的循环队列中记录了最近的20个主线程堆栈，需要从中找出最近最耗时的堆栈。Matrix 卡顿监控用如下特征找出最近最耗时堆栈：

- 以栈顶函数为特征，认为栈顶函数相同的即整个堆栈是相同的；
- 取堆栈的间隔是相同的，堆栈的重复次数近似作为堆栈的调用耗时，重复越多，耗时越多；
- 重复次数相同的堆栈可能很有多个，取最近的一个最耗时堆栈。

获得的最近最耗时堆栈会附带到卡顿文件中。

![](https://ask.qcloudimg.com/http-save/598196/opgp4kws52.jpeg)

**卡死卡顿**

---

Matrix 中内置了应用被杀原因的检测机制。这个机制从 Facebook 的博文 中获得灵感，在其基础上增加了系统强杀的判定。Matrix 检测应用被杀原因的具体机制如下图所示：

![](https://ask.qcloudimg.com/http-save/598196/vtufqxef2i.jpeg)

Matrix 检测到应用卡死被强杀，会把应用上次存活时的最后一份卡顿日志标记为卡死卡顿。

### **性能数据**

---

Matrix 卡顿监控不打开耗时堆栈提取，性能损耗可以忽略不计。

打开耗时堆栈提取后，性能损耗和定时获取主线程堆栈的间隔有关。实测，每隔 50 毫秒不断获取主线程堆栈，会增加 3% 的 CPU 占用。

### **结尾**

---

以上是 iOS 微信卡顿监控的原理性介绍，它同样可以应用在 macOS 平台上。iOS 微信团队通过卡顿监控上报的堆栈，找到微信的代码不合理之处或者是一些性能瓶颈，通过卡顿监控的辅助，尽可能地提升 iOS 微信的流畅性，给用户带来更加极致美好的体验。

卡顿监控依然在不断进行优化，不断地扩展能力，近期我们计划会为它增添捕获应用的耗电堆栈等，使其功能更加完备。我们决定通过 Matrix 将其开源，并希望能获得大家的意见和建议。

### **开源地址**

[Matrix]https://github.com/Tencent/matrix/tree/master/matrix/matrix-apple

请给 Matrix 一个 Star !

欢迎提出你的 issue 和 PR。

var first_sceen__time = (+new Date());if ("" == 1 && document.getElementById('js_content')) { document.getElementById('js_content').addEventListener("selectstart",function(e){ e.preventDefault(); }); } (function(){ if (navigator.userAgent.indexOf("WindowsWechat") != -1){ var link = document.createElement('link'); var head = document.getElementsByTagName('head')[0]; link.rel = 'stylesheet'; link.type = 'text/css'; link.href = "//res.wx.qq.com/mmbizwap/zh_CN/htmledition/style/page/appmsg_new/winwx45ba31.css"; head.appendChild(link); } })();

陈志炯

赞赏

长按二维码向我转账

![](https://ask.qcloudimg.com/http-save/598196/j36vjoybub.png)

受苹果公司新规定影响，微信 iOS 版的赞赏功能被关闭，可通过二维码转账支持公众号。

阅读原文

阅读

分享 在看

**已同步到看一看**

取消 发送

我知道了

##### 朋友会在“发现-看一看”看到你“在看”的内容

确定

![](https://ask.qcloudimg.com/http-save/598196/rql4z47qiv.png)

已同步到看一看写下你的想法

最多200字，当前共字 发送

已发送

##### 朋友将在看一看看到

确定

写下你的想法...

取消

##### 发布到看一看

确定

最多200字，当前共字

发送中

微信扫一扫 关注该公众号

微信扫一扫 使用小程序

即将打开""小程序

取消 打开
