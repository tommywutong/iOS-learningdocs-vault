---
title: UITableView 流畅度优化实践
source_url: 'https://blog.aberlt.com/2017/12/30/UITableView-%E6%B5%81%E7%95%85%E5%BA%A6%E4%BC%98%E5%8C%96%E5%AE%9E%E8%B7%B5/'
source_domain: blog.aberlt.com
source_group: single-site
original_language: zh
published: 2017-12-30
archived_at: 2026-07-27
content_hash: 'sha256:8cf9d4d8ac71c927'
plan_ref: 第六周：UIKit 渲染、UITableView 与性能 / Day 4｜先建立 baseline，再谈列表优化（对应 W6-09）
plan_week: 第六周：UIKit 渲染、UITableView 与性能
plan_day: Day 4｜先建立 baseline，再谈列表优化（对应 W6-09）
container: //article
container_source: guess
---

> 原文：[UITableView 流畅度优化实践](https://blog.aberlt.com/2017/12/30/UITableView-%E6%B5%81%E7%95%85%E5%BA%A6%E4%BC%98%E5%8C%96%E5%AE%9E%E8%B7%B5/)

[2017-12-30](https://blog.aberlt.com/2017/12/30/UITableView-流畅度优化实践/)

# UITableView 流畅度优化实践

[性能优化](https://blog.aberlt.com/categories/性能优化/)

11 月份对公司项目的列表流畅度进行了一次优化，做完之后一直有别的事情需要处理就把这篇文章一直拖着，这次元旦假期抽一点时间出来对优化工作做一下记录。

## 背景

10 月底看到第三方服务商关于公司项目的性能监控报告后发现卡顿率特别高，因此在小组会议上主动提起需要对项目的流畅度进行优化，恰好老大也觉得首页列表的卡顿很严重，后来询问了我关于这个模块优化的想法之后便把这项任务交给了我。其实当时还是挺虚的，虽然看过相关的内容，但并没有实践过，不过对于一个新人来说既然有机会可以做一些业务以外的工作就得好好把握，于是硬着头皮把任务给做了下来。

优化前：

![Before_fluency_optimization](http://images.aberlt.com/2018-03-13-Before_fluency_optimization.gif)

优化后：

![After_fluency_optimization](http://images.aberlt.com/2018-03-12-After_fluency_optimization.gif)

## 屏幕显示的原理

![ios_screen_display](http://images.aberlt.com/2018-01-01-ios_screen_display.png)

经过查阅资料，图像显示到屏幕需要经过如上图所示的过程进行处理。

首先，CPU 把视图创建、布局计算、图片解码、文本绘制等显示内容计算好提交给 GPU；然后 GPU 对内容进行变换、合成、渲染并将渲染结果放入帧缓冲区 FrameBuffer；最后视频控制器通过**垂直同步信号（V-Sync）**逐行读取帧缓冲区的数据并转换后传递给屏幕显示。

### 双缓冲机制和垂直同步机制

iOS 设备为了提升效率使用了双缓冲机制。其原理是 GPU 先将一个渲染结果放入一个缓冲区让视频控制器读取，当下一个内容渲染完成后，GPU 会将视频控制器的指针直接指向第二个缓冲区。

但双缓冲机制会因为视频控制器读取速度与 GPU 渲染速度的不同步造成图像撕裂的情况。

为了解决这个问题，GPU 采用了垂直同步机制，即等待显示器的 VSync 信号发出后才进行新的渲染和缓冲区的更新。

双缓冲和垂直同步两种机制的使用提升了屏幕刷新的效率和画面的流畅度，但也增加了资源的消耗。

## 卡顿的产生

已知垂直同步机制中一个 VSync 信号产生将会引起一个新的内容计算和渲染的流程，在下一个 VSync 信号产生之前，就需要完成从 CPU 的计算到屏幕的显示这个流程。但是并不能保证每一 CPU 或者 GPU 都能够在两个 VSync 之间的时间内完成任务，而这个没有及时完成的任务将会被舍弃，此时屏幕的内容就没有被更新，所以造成了卡顿。如下图所示：

![ios_frame_drop](http://images.aberlt.com/2018-01-01-ios_frame_drop.png)

因此，我们需要从 CPU 和 GPU 在这个过程中所执行的任务入手，找到可以进行优化的地方。

## 优化

### CPU 在屏幕显示过程中执行的任务及本人进行优化的内容

CPU 执行的任务主要是：

- 创建对象
- 调整对象
- 销毁对象
- 布局计算
- 文本计算
- 文本绘制
- 图片解码

这里每个任务都有可优化的地方，而我在优化的过程中则根据项目的实际情况对几个任务进行了优化。

#### 创建对象

由于列表中只有一个 `UITableViewCell` 中的一个子控件需要响应触摸事件，所以我将原来使用的 `UIView`、`UIImageView` 等控件改为使用 `CALayer`。这里主要是因为 `CALyer` 相对来说更加轻量，而且原来的控件有很多属性的设置其实还是在对 `CALayer` 进行操作。

#### 布局计算

原来项目中使用 `Masonary` 对控件进行布局，这在开发的时候非常方便，但是程序在运行的时候计算量很大，同时还需要对控件的 `frame/bounds/center` 等属性进行调整，需要消耗很多的资源进而造成性能的损失。

因此，我将自动布局改为通过 frame 布局，在获取到数据的时候提前对布局进行计算并存储到布局模型中，TableView 可以直接从布局模型获取 Cell 的高度，Cell 也可以直接获取各个子控件的位置和尺寸等信息，避免多次计算，节省资源的消耗和内存的占用。

#### 文本计算和渲染

原项目中使用 `UILabel` 显示文本，由于对行高有特别的要求，需要将内容处理为富文本。这些都是在 Cell 初始化的时候进行操作的，并且是在主线程操作，这对主线程造成了一定的阻塞。

由于项目中刚好引用了 `YYKit`，我决定使用文本布局类 `YYTextLayout` 进行文本的计算和富文本的绘制并将其保存在布局模型中以供后面渲染使用；使用 `YYLabel` 来做文本的异步渲染，将渲染的工作放到子线程进行。既避免了阻塞主线程，还减少了使用 `UILabel` 时的很多计算。

> 因为原来项目中调整对象的操作比较少，而图片则使用了 `YYWebImage` 进行异步加载，所以这两处没有进行处理。  
> 至于对象的销毁，目前并没有造成多大的影响。为了避免由于操作不当造成问题，所以没有从这个方面入手。

### GPU 在屏幕显示过程中执行的任务及可优化的内容

GPU 执行的任务是：

- 渲染纹理
- 混合视图
- 生成图形

相对来说 GPU 执行的任务类型没有 CPU 那么多。在这个环节我从**混合视图**和**生成图形**两个方面入手进行优化。

#### 混合视图

开发过程中为了实现某些需求常常会使得一个视图上有很多个控件层叠在一起，导致视图层级太多、结构复杂。特别是对于透明的控件，GPU 需要计算多个视图混合后的效果，这个过程会消耗更多的资源。

这里我做的就是将能够组合在一起的视图绘制成富文本或者与其它视图一起合成一张图片，减少视图的层级。同时将不需要透明的视图都设置了与父视图一样的颜色，将 opaque 设置为 YES。

#### 生成图形

原项目的列表中几乎每个 Cell 都有一个圆形的图标，实现这个需求的做法是通过设置 `CALayer` 的 `cornerRadius` 和 `masksToBounds` 完成的。众所周知，这两个属性分开使用的时候没问题，但是一起使用的话就必定会造成离屏渲染（Off-Screen rendering）。

离屏渲染需要先在屏幕外（Off-Screen）渲染完成后再绘制到当前屏幕（On-Screen），这里需要另外分配一块内存进行渲染，而且 On-Screen 和 Off-Screen 之间的上下文环境切换的过程需要很大的开销。

网上有很多解决离屏渲染的方法，我采用了比较彻底的解决方法，直接在后台通过重绘将图片裁剪为圆角。

### 优化后列表的加载过程

![List_show_flow](http://images.aberlt.com/2018-01-03-List_show_flow.png)

优化思路很简单，但是实际操作起来工作量比较大，也有不少坑，这里说一下最大的坑 `CALayer` 的光栅化属性 `shouldRasterize`。

#### shouldRasterize

在调研的时候看到网上的资料说设置这个属性可以提高性能，便在优化的时候尝试了一下，将圆角图标的圆框设置了这个属性，但是结果却不尽人意。当页面出现比较多的圆角图标时，加载几页的内容之后就会变得异常卡顿，肉眼能够非常明显的感受到，FPS 也极速下降，但是通过 Time Profile 和 Core Animation 工具无法排查出问题，后来通过对控件的删减排查才知道是这个属性导致的问题。

开启 `shouldRasterize` 后 `CAlayer` 会被光栅化为位图 bitmap 保存在缓存中以备重用，可以加快渲染过程。但是使用的过程需要注意几个问题：

- 不要对经常变动的内容开启，因为一旦更新已经光栅化的 layer 会造成大量离屏渲染
- 不要过度使用，系统限制缓存的大小为 2.5x screen size，过度使用的话也会造成离屏渲染
- 光栅化的位图如果超过 100 毫秒没有被使用则会被移除，所以对于不连续使用的内容进行光栅化是既没有意义又浪费资源的

如图为 WWDC 2014 的内容：

![Rasterization](http://images.aberlt.com/2018-01-03-Rasterization.png)

而我在优化过程中犯的错误就是第一个需要注意的问题：

把添加到 TableViewCell 的 layer 进行了光栅化，而 TableViewCell 由于复用的原因需要频繁的进行重绘，对已经光栅化的内容进行了更新，导致大量的离屏渲染，所以列表的流畅度才会极速下降。

## 总结

这次优化中查询了很多资料，了解到不少的原理知识，对于视图是如何绘制到屏幕上也更加了解，也更能针对性地进行分析和优化，在这个过程中也学会了如何使用 Time Profile 和 Core Animation 工具进行检测。

从这次的踩坑领悟到了不应该人云亦云，对于别人提出的东西要自己去验证是否正确、是否适合运用到自己的项目中。一旦出现无法直接判断、工具也无法排查出的问题应该要逐步去对代码进行校验定位问题所在。

## 参考

[iOS 保持界面流畅的技巧](https://blog.ibireme.com/2015/11/12/smooth_user_interfaces_for_ios/)

[iOS — UITableView的优化技巧](https://icetime17.github.io/2015/07/04/2015-07/iOS-UITableView的优化技巧/)

[WWDC心得：Advanced Graphics and Animations for iOS Apps](https://github.com/100mango/zen/blob/master/WWDC心得：Advanced%20Graphics%20and%20Animations%20for%20iOS%20Apps/Advanced%20Graphics%20and%20Animations%20for%20iOS%20Apps.md)

[高性能添加图片圆角方法原理：cornerRadius，layer.shouldRasterize，layer.setShadowPath和透明图片](http://iandai.github.io/blog/2015/09/21/gao-xing-neng-tian-jia-tu-pian-yuan-jiao-fang-fa-bi-jiao-:layer-dot-shouldrasterize,layer-dot-setshadowpathhe-tou-ming-tu-pian/)

[iOS性能优化（一）：Time Profile](http://www.jianshu.com/p/080108c969e8)

[iOS app性能优化的那些事(二)](https://www.jianshu.com/p/2a01e5e2141f)

本文标题:[UITableView 流畅度优化实践](https://blog.aberlt.com/2017/12/30/UITableView-流畅度优化实践/)

文章作者:[aberlt](https://blog.aberlt.com/)

发布时间:2017年12月30日 - 19时07分

最后更新:2018年08月08日 - 10时23分

原始链接:[https://blog.aberlt.com/2017/12/30/UITableView-流畅度优化实践/](https://blog.aberlt.com/2017/12/30/UITableView-流畅度优化实践/)

许可协议: ["知识共享 署名-非商业性使用-相同方式共享 4.0 国际 许可协议"](http://creativecommons.org/licenses/by-nc-sa/4.0/) 转载请保留原文链接及作者。
