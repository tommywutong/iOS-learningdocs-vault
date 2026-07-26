---
title: 优化UITableViewCell高度计算的那些事 · sunnyxx的技术博客
source: sunnyxx (孙源)
source_key: sunnyxx
source_url: 'http://blog.sunnyxx.com/2015/05/17/cell-height-calculation/'
original_language: zh
published: 2015-05-17
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:5824b48916e5e71b'
translated: n/a
---

> 原文：[优化UITableViewCell高度计算的那些事 · sunnyxx的技术博客](http://blog.sunnyxx.com/2015/05/17/cell-height-calculation/)　·　sunnyxx (孙源)

# 优化UITableViewCell高度计算的那些事

2015年5月17日

# [#我是前言](#我是前言)我是前言

这篇文章是我和我们团队最近对 **UITableViewCell** 利用 **AutoLayout** 自动高度计算和 **UITableView** 滑动优化的一个总结。  
我们也在维护一个开源的扩展，`UITableView+FDTemplateLayoutCell`，让高度计算这个事情变的前所未有的简单，也受到了很多星星的支持，[github链接请戳我](https://github.com/forkingdog/UITableView-FDTemplateLayoutCell)

这篇总结你可以读到：

- UITableView高度计算和估算的机制
- 不同iOS系统在高度计算上的差异
- iOS8 self-sizing cell
- UITableView+FDTemplateLayoutCell如何用一句话解决高度问题
- UITableView+FDTemplateLayoutCell中对RunLoop的使用技巧

---

# [#UITableViewCell高度计算](#UITableViewCell高度计算)UITableViewCell高度计算

## [#rowHeight](#rowHeight)rowHeight

`UITableView`是我们再熟悉不过的视图了，它的 **delegate** 和 **data source** 回调不知写了多少次，也不免遇到 UITableViewCell 高度计算的事。UITableView 询问 cell 高度有两种方式。  
一种是针对所有 Cell 具有固定高度的情况，通过：

```objc
self.tableView.rowHeight = 88;
```

上面的代码指定了一个所有 cell 都是 88 高度的 UITableView，对于定高需求的表格，**强烈建议**使用这种（而非下面的）方式保证不必要的高度计算和调用。`rowHeight`属性的默认值是 44，所以一个空的 UITableView 显示成那个样子。

另一种方式就是实现 UITableViewDelegate 中的：

```objc
- (CGFloat)tableView:(UITableView *)tableView heightForRowAtIndexPath:(NSIndexPath *)indexPath {
    // return xxx
}
```

需要注意的是，实现了这个方法后，`rowHeight` 的设置将无效。所以，这个方法适用于具有多种 cell 高度的 UITableView。

## [#estimatedRowHeight](#estimatedRowHeight)estimatedRowHeight

这个属性 iOS7 就出现了， 文档是这么描述它的作用的：

> If the table contains variable height rows, it might be expensive to calculate all their heights when the table loads. Using estimation allows you to defer some of the cost of geometry calculation from load time to scrolling time.

恩，听上去蛮靠谱的。我们知道，UITableView 是个 UIScrollView，就像平时使用 UIScrollView 一样，加载时指定 `contentSize` 后它才能根据自己的 bounds、contentInset、contentOffset 等属性共同决定是否可以滑动以及滚动条的长度。而 UITableView 在一开始并不知道自己会被填充多少内容，于是询问 data source 个数和创建 cell，同时询问 delegate 这些 cell 应该显示的高度，这就造成它在加载的时候浪费了多余的计算在**屏幕外边**的 cell 上。和上面的 `rowHeight` 很类似，设置这个估算高度有两种方法：

```objc
self.tableView.estimatedRowHeight = 88;
// or
- (CGFloat)tableView:(UITableView *)tableView estimatedHeightForRowAtIndexPath:(NSIndexPath *)indexPath {
    // return xxx
}
```

有所不同的是，即使面对种类不同的 cell，我们依然可以使用简单的 `estimatedRowHeight` 属性赋值，只要**整体估算值接近**就可以，比如大概有一半 cell 高度是 44， 一半 cell 高度是 88， 那就可以估算一个 66，基本符合预期。

说完了估算高度的基本使用，可以开始吐槽了：

1. 设置估算高度后，contentSize.height 根据“cell估算值 x cell个数”计算，这就导致滚动条的大小处于不稳定的状态，contentSize 会随着滚动从估算高度慢慢替换成真实高度，肉眼可见滚动条突然变化甚至“跳跃”。
2. 若是有设计不好的下拉刷新或上拉加载控件，或是 KVO 了 contentSize 或 contentOffset 属性，有可能使表格滑动时跳动。
3. 估算高度设计初衷是好的，让加载速度更快，那凭啥要去侵害滑动的流畅性呢，用户可能对进入页面时多零点几秒加载时间感觉不大，但是滑动时实时计算高度带来的卡顿是明显能体验到的，个人觉得还不如一开始都算好了呢（iOS8更过分，即使都算好了也会边划边计算）

---

# [#iOS8-self-sizing-cell](#iOS8-self-sizing-cell)iOS8 self-sizing cell

具有动态高度内容的 cell 一直是个头疼的问题，比如聊天气泡的 cell， frame 布局时代通常是用数据内容反算高度：

```objc
CGFloat height = textHeightWithFont() + imageHeight + topMargin + bottomMargin + ...;
```

供 UITableViewDelegate 调用时很可能是个 cell 的类方法：

```objc
@interface BubbleCell : UITableViewCell
+ (CGFloat)heightWithEntity:(id)entity;
@end
```

各种魔法 margin 加上耦合了屏幕宽度。

AutoLayout 时代好了不少，提供了`-systemLayoutSizeFittingSize:`的 API，在 contentView 中设置约束后，就能计算出准确的值；缺点是计算速度肯定没有手算快，而且这是个实例方法，需要维护专门为计算高度而生的 `template layout cell`，它还要求使用者对约束设置的比较熟练，要保证 contentView 内部上下左右所有方向都有约束支撑，设置不合理的话计算的高度就成了0。

这里还不得不提到一个 UILabel 的蛋疼问题，当 UILabel 行数大于0时，需要指定 `preferredMaxLayoutWidth` 后它才知道自己什么时候该折行。这是个“鸡生蛋蛋生鸡”的问题，因为 UILabel 需要知道 superview 的宽度才能折行，而 superview 的宽度还依仗着子 view 宽度的累加才能确定。这个问题好像到 iOS8 才能够自动解决（不过我们找到了解决方案）

回到正题，iOS8 WWDC 中推出了 `self-sizing cell` 的概念，旨在让 cell 自己负责自己的高度计算，使用 frame layout 和 auto layout 都可以享受到：

![](http://ww3.sinaimg.cn/mw690/51530583jw1es3hwpsb71j20pe0f2ab4.jpg)

这个特性首先要求是 iOS8，要是最低支持的系统版本小于8的话，还得针对老版本单写套老式的算高（囧），不过用的 API 到不是新面孔：

```objc
self.tableView.estimatedRowHeight = 213;
self.tableView.rowHeight = UITableViewAutomaticDimension;
```

这里又不得不吐槽了，自动计算 rowHeight 跟 estimatedRowHeight 到底是有什么仇，如果不加上估算高度的设置，自动算高就失效了- -  
PS：iOS8 系统中 rowHeight 的默认值已经设置成了 UITableViewAutomaticDimension，所以第二行代码可以省略。

问题：

1. 这个自动算高在 push 到下一个页面或者转屏时会出现高度特别诡异的情况，不过现在的版本修复了。
2. 求一个能让最低支持 iOS8 的公司- -

---

# [#iOS8抽风的算高机制](#iOS8抽风的算高机制)iOS8抽风的算高机制

相同的代码在 iOS7 和 iOS8 上滑动顺畅程度完全不同，iOS8 莫名奇妙的卡。很大一部分原因是 iOS8 上的算高机制大不相同，这是我做的小测试：

![](http://ww1.sinaimg.cn/mw690/51530583jw1es3j7avlelj20w4084jsv.jpg)

研究后发现这么多次额外计算有下面的原因：

1. 不开启高度估算时，UITableView 上来就要对所有 cell 调用算高来确定 contentSize
2. 相比不带 “forIndexPath” 的版本会多调用一次高度计算
3. iOS7 计算高度后有”缓存“机制，不会重复计算；而 iOS8 不论何时都会重新计算 cell 高度

iOS8 把高度计算搞成这个样子，从 WWDC 也倒是能找到点解释，cell 被认为随时都可能改变高度（如从设置中调整动态字体大小），所以每次滑动出来后都要重新计算高度。

说了这么多，究竟有没有既能省去算高烦恼，又能保证顺畅的滑动，还能支持 iOS6+ 的一站式解决方案呢？

---

# [#UITableView-FDTemplateLayoutCell](#UITableView-FDTemplateLayoutCell)UITableView+FDTemplateLayoutCell

使用 `UITableView+FDTemplateLayoutCell` 无疑是解决算高问题的最佳实践之一，既有 iOS8 self-sizing 功能简单的 API，又可以达到 iOS7 流畅的滑动效果，还保持了最低支持 iOS6。  
使用起来大概是这样：

```objc
#import <UITableView+FDTemplateLayoutCell.h>
- (CGFloat)tableView:(UITableView *)tableView heightForRowAtIndexPath:(NSIndexPath *)indexPath {
    return [tableView fd_heightForCellWithIdentifier:@"identifer" cacheByIndexPath:indexPath configuration:^(id cell) {
        // 配置 cell 的数据源，和 "cellForRow" 干的事一致，比如：
        cell.entity = self.feedEntities[indexPath.row];
    }];
}
```

写完上面的代码后，你就已经使用到了：

- 这个 cell 只为了参加高度计算，不会真的显示到屏幕上；它通过 UITableView 的

  方法 lazy 创建并保存，所以要求这个 ReuseID 必须已经被注册到了 UITableView 中，也就是说，要么是 Storyboard 中的原型 cell，要么就是使用了 UITableView 的

  或

  其中之一的注册方法。
- 使用了系统在 iOS6 就提供的 API：
- 计算出的高度会自动进行缓存，所以滑动时每个 cell 真正的高度计算只会发生一次，后面的高度询问都会命中缓存，减少了非常可观的多余计算。
- 无须担心你数据源的变化引起的缓存失效，当调用如

  ，

  等任何一个触发 UITableView 刷新机制的方法时，已有的高度缓存将以

  执行失效。如删除一个 indexPath 为 [0:5] 的 cell 时，[0:0] ~ [0:4] 的高度缓存不受影响，而 [0:5] 后面所有的缓存值都向前移动一个位置。自动缓存失效机制对 UITableView 的 9 个公有 API 都进行了分别的处理，以保证没有一次多余的高度计算。
- 预缓存机制将在 UITableView 没有滑动的空闲时刻执行，计算和缓存那些还没有显示到屏幕中的 cell，整个缓存过程完全没有感知，这使得完整列表的高度计算既没有发生在加载时，又没有发生在滑动时，同时保证了加载速度和滑动流畅性，下文会着重讲下这块的实现原理。

我们在设计这个工具的 API 时斟酌了非常长的时间，既要保证功能的强大，也要保证接口的精简，一行调用背后隐藏着很多功能。

这一套缓存机制能对滑动起多大影响呢？除了肉眼能明显的感知到外，我还做了个小测试：  
一个有 54 个内容和高度不同 cell 的 table view，从头滑动到尾，再从尾滑动到头，iOS8 系统下，iPhone6，使用 `Time Profiler` 监测算高函数所花费的时间：

未使用缓存API、未使用估算，共花费 877 ms：  
![](http://ww3.sinaimg.cn/mw690/51530583jw1es7f5l357cj213k0g07eh.jpg)

使用缓存API、开启估算，共花费 77 ms：  
![](http://ww2.sinaimg.cn/mw690/51530583jw1es7f5lefy3j21440hsgw8.jpg)

测试数据的精度先不管，从量级上就差了一个数量级，说实话自己也没想到差距有这么大- -

同时，工具也顺手解决了`-preferredMaxLayoutWidth`的问题，在计算高度前向 contentView 加了一条和 table view 宽度相同的宽度约束，强行让 contentView 内部的控件知道了自己父 view 的宽度，再反算自己被外界约束的宽度，破除“鸡生蛋蛋生鸡”的问题，这里比较 tricky，就不展开说了。下面说说利用 RunLoop 预缓存的实现。

---

# [#利用RunLoop空闲时间执行预缓存任务](#利用RunLoop空闲时间执行预缓存任务)利用RunLoop空闲时间执行预缓存任务

FDTemplateLayoutCell 的高度预缓存是一个优化功能，它要求页面处于**空闲**状态时才执行计算，当用户正在滑动列表时显然不应该执行计算任务影响滑动体验。  
一般来说，这个功能要耦合 UITableView 的滑动状态才行，但这种实现十分不优雅且可能破坏外部的 delegate 结构，但好在我们还有`RunLoop`这个工具，了解它的运行机制后，可以用很简单的代码实现上面的功能。

## [#空闲RunLoopMode](#空闲RunLoopMode)空闲RunLoopMode

在曾经的 RunLoop 线下分享会（[视频可戳](http://yun.baidu.com/share/link?shareid=2268593032&uk=2885973690)）中介绍了 RunLoopMode 的概念。  
当用户正在滑动 UIScrollView 时，RunLoop 将切换到 `UITrackingRunLoopMode` 接受滑动手势和处理滑动事件（包括减速和弹簧效果），此时，其他 Mode （除 NSRunLoopCommonModes 这个组合 Mode）下的事件将全部暂停执行，来保证滑动事件的优先处理，这也是 iOS 滑动顺畅的重要原因。  
当 UI 没在滑动时，默认的 Mode 是 `NSDefaultRunLoopMode`（同 CF 中的 kCFRunLoopDefaultMode），同时也是 CF 中定义的 “空闲状态 Mode”。当用户啥也不点，此时也没有什么网络 IO 时，就是在这个 Mode 下。

## [#用RunLoopObserver找准时机](#用RunLoopObserver找准时机)用RunLoopObserver找准时机

注册 RunLoopObserver 可以观测当前 RunLoop 的运行状态，并在状态机切换时收到通知：

1. RunLoop开始
2. RunLoop即将处理Timer
3. RunLoop即将处理Source
4. RunLoop即将进入休眠状态
5. RunLoop即将从休眠状态被事件唤醒
6. RunLoop退出

因为“预缓存高度”的任务需要在最无感知的时刻进行，所以应该同时满足：

1. RunLoop 处于“空闲”状态 Mode
2. 当这一次 RunLoop 迭代处理完成了所有事件，马上要休眠时

使用 CF 的带 block 版本的注册函数可以让代码更简洁：

```objc
CFRunLoopRef runLoop = CFRunLoopGetCurrent();
CFStringRef runLoopMode = kCFRunLoopDefaultMode;
CFRunLoopObserverRef observer = CFRunLoopObserverCreateWithHandler
(kCFAllocatorDefault, kCFRunLoopBeforeWaiting, true, 0, ^(CFRunLoopObserverRef observer, CFRunLoopActivity _) {
    // TODO here
});
CFRunLoopAddObserver(runLoop, observer, runLoopMode);
```

在其中的 TODO 位置，就可以开始任务的收集和分发了，当然，不能忘记适时的移除这个 observer

## [#分解成多个RunLoop-Source任务](#分解成多个RunLoop-Source任务)分解成多个RunLoop Source任务

假设列表有 20 个 cell，加载后展示了前 5 个，那么开启估算后 table view 只计算了这 5 个的高度，此时剩下 15 个就是“预缓存”的任务，而我们并不希望这 15 个计算任务在同一个 RunLoop 迭代中同步执行，这样会卡顿 UI，所以应该把它们**分别分解**到 15 个 RunLoop 迭代中执行，这时就需要手动向 RunLoop 中添加 Source 任务（由应用发起和处理的是 Source 0 任务）  
Foundation 层没对 RunLoopSource 提供直接构建的 API，但是提供了一个间接的、既熟悉又陌生的 API：

```objc
- (void)performSelector:(SEL)aSelector
               onThread:(NSThread *)thr
             withObject:(id)arg
          waitUntilDone:(BOOL)wait
                  modes:(NSArray *)array;
```

这个方法将创建一个 Source 0 任务，分发到指定线程的 RunLoop 中，在给定的 Mode 下执行，若指定的 RunLoop 处于休眠状态，则唤醒它处理事件，简单来说就是“睡你xx，起来嗨！”  
于是，我们用一个可变数组装载当前所有需要“预缓存”的 index path，每个 RunLoopObserver 回调时都把第一个任务拿出来分发:

```objc
NSMutableArray *mutableIndexPathsToBePrecached = self.fd_allIndexPathsToBePrecached.mutableCopy;
CFRunLoopObserverRef observer = CFRunLoopObserverCreateWithHandler(kCFAllocatorDefault, kCFRunLoopBeforeWaiting, true, 0, ^(CFRunLoopObserverRef observer, CFRunLoopActivity _) {
    if (mutableIndexPathsToBePrecached.count == 0) {
        CFRunLoopRemoveObserver(runLoop, observer, runLoopMode);
        CFRelease(observer); // 注意释放，否则会造成内存泄露
        return;
    }
    NSIndexPath *indexPath = mutableIndexPathsToBePrecached.firstObject;
    [mutableIndexPathsToBePrecached removeObject:indexPath];
    [self performSelector:@selector(fd_precacheIndexPathIfNeeded:)
                 onThread:[NSThread mainThread]
               withObject:indexPath
            waitUntilDone:NO
                    modes:@[NSDefaultRunLoopMode]];
});
```

这样，每个任务都被分配到下个“空闲” RunLoop 迭代中执行，其间但凡有滑动事件开始，Mode 切换成 UITrackingRunLoopMode，所有的“预缓存”任务的分发和执行都会自动暂定，最大程度保证滑动流畅。

PS: 预缓存功能因为下拉刷新的冲突和不明显的收益已经废弃

---

# [#开始使用UITableView-FDTemplateLayoutCell](#开始使用UITableView-FDTemplateLayoutCell)开始使用UITableView+FDTemplateLayoutCell

如果你觉得这个工具能帮得到你，整合到工程也十分简单。  
使用 cocoapods：

```plain
pod search UITableView+FDTemplateLayoutCell
```

写这篇文章时的最新版本为 1.2，去除了前一个版本的黑魔法，增加了预缓存功能。  
欢迎使用和支持这个工具，有 bug 请随时反馈哦~  
再复习下 github 地址： [https://github.com/forkingdog/UITableView-FDTemplateLayoutCell](https://github.com/forkingdog/UITableView-FDTemplateLayoutCell)

![](https://cloud.githubusercontent.com/assets/219689/7244961/4209de32-e816-11e4-87bc-b161c442d348.png)
