---
title: Texture-基本概念
source: dirtmelon
source_key: dirtmelon
source_url: 'https://dirtmelon.github.io/posts/texture-basic-concepts/'
original_language: zh
published: 2019-02-19
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:1886118ced705e28'
translated: n/a
---

> 原文：[Texture-基本概念](https://dirtmelon.github.io/posts/texture-basic-concepts/)　·　dirtmelon

原文：[Core Concepts](https://texturegroup.org/docs/intelligent-preloading.html)

Texture 基本单位为 `node` ， `ASDisplayNode` 是建立在 `UIView` 上的抽象层，如同 `UIView` 与 `CALayer` 的关系。`ASDiplayNode` 是线程安全的，你可以在后台线程进行初始化和配置。

## Nodes

`Node` 的用法跟 `UIView` 类似，且 `Node` 提供了 `UIView` 和 `CALayer` 属性。 Texture 提供了丰富的 Node 子类 ，用于取代 UIKit 组建。

- ASDipslayNode -\> UIView
- ASCellNode -\> UITableViewCell/UICollectionViewCell
- ASScrollNode -\> UIScrollView
- ASEditableTextNode -\> UITextView
- ASTextNode, ASTextNode2 -\> UILabel
- ASImageNode, ASNetworkImageNode, ASMultiplexImageNode -\> UIImageView
- ASVideoNode -\> AVPlayerLayer
- ASVideoPlayerNode -\> UIMoviePlayer
- ASControlNode -\> UIControl
- ASButtonNode -\> UIButton
- ASMapNode -\> MKMapView

![node-hierarchy](https://raw.githubusercontent.com/dirtmelon/blog-images/main/node-hierarchy.png)

### Node Containers

推荐使用 Node Container 来包含 Nodes，Texture 提供以下 Node Containers：

- ASCollectionNode -\> UICollectionView
- ASPagerNode -\> UIPageViewController
- ASTableNode -\> UITableView
- ASViewController -\> UIViewController
- ASNavigationController -\> UINavigationController
- ASTabBarController -\> UITabBarController

Node Containers 好处都有啥？ 智能预加载。这意味所有 Node 相关的布局计算，数据获取，解码和渲染都可以异步完成。

### Subclassing

#### ASDisplayNode

- `-init` ASDisplayNode 的 -init 方法可以在后台线程中调用，所以不要在该方法中获取或者初始化任何 UIKit 的相关对象，例如 添加手势。
- `-didLoad` 该方法跟 UIViewController `-viewDidLoad` 方法类似，当后台 View 加载完成时就会调用，且只会在主线程中调用，用于进行与 UIKit 相关的操作
- `-layoutSpecThatFits:` 用于生成 `ASLayoutSpec` 对象，在后台线程中运行，而 `ASLayoutSpec` 则包含了 Node 的大小 以及所有 subnodes 的位置及大小。除非你明确知道你正在做什么，否则不要在该方法中创建 Node
- `-layout` `-layout` 与 UIViewController `-viewWillLayoutSubviews` 类似。可以设置 view 的一些不需要进行布局的基础属性。如果在 Node 使用了 UIView，则可以在该方法中设置 frame 。 该方法在主线程中调用，但是如果你正在使用 ASLayoutSpec ，则不应该太过依赖该方法。 一个很好的用法是你想要设置 subnode 为确切的 size ，则可以在 `-layout` 中直接设置。

  ```objc
  subnode.frame = self.bounds;
  ```

#### ASViewController

- `-init` 该方法中不要过早访问 `self.view` 或者 `self.node.view` ，这会强制 view 提早生成。 ASViewController 的指定初始化方法是 `-initWithNode:`
- `-loadView` 不建议使用该方法
- `-viewDidLoad` 用法与 UIViewController 的类似
- `-viewWillLayoutSubviews` 用于进行布局计算。

## 智能预加载

Node 的能力是异步并行地进行渲染和计算，与此同样要的是智能预加载 Node 对于它们当前的界面状态都有标志来说明。 `interfaceState` 属性由创建和维护 containers 的 `ASRangeController` 负责更新。

### Interface State Ranges

![intelligent-preloading-ranges-with-names](https://raw.githubusercontent.com/dirtmelon/blog-images/main/intelligent-preloading-ranges-with-names.png)

当 scrollView 滚动时，scrollView 中的 node 就会更新至对应状态

- Preload: 距离屏幕较远，准备所需要的数据
- Display：即将进入屏幕，文字渲染，图片解码渲染等
- Visible：至少有 1 像素进入屏幕

### ASRangeTuningParameters

```c
typedef struct {
	CGFloat leadingBufferScreenfuls;
  CGFloat trailingBufferScreenfuls;
} ASRangeTuningParameters;
```

![intelligent-preloading-ranges-screenfuls](https://raw.githubusercontent.com/dirtmelon/blog-images/main/intelligent-preloading-ranges-screenfuls.png)

ASRangeTuningParameters 定义了各个区域大小，一般来说即将进入的区域比离开的区域要大一些

### Interface State Callbacks

通过以下可以在相关的状态中进行不同的操作：

- ```objc
  -didEnterVisibleState
  -didExitVisibleState
  ```
- ```objc
  -didEnterDisplayState
  -didExitDisplayState
  ```
- ```objc
  -didEnterPreloadState
  -didExitPreloadState
  ```

## FAQ

[Texture | FAQ](http://texturegroup.org/docs/faq.html)
