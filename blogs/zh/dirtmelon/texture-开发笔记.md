---
title: Texture 开发笔记
source: dirtmelon
source_key: dirtmelon
source_url: 'https://dirtmelon.github.io/posts/texture-notes/'
original_language: zh
published: 2018-01-07
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:b06d953475c05e71'
translated: n/a
---

> 原文：[Texture 开发笔记](https://dirtmelon.github.io/posts/texture-notes/)　·　dirtmelon

## ASImageNode

ASImageNode 不支持直接设置 `tintColor` ，如果需要设置 tintColor需要通过 `imageModificationBlock` 进行设置：

```swift
imageNode.imageModificationBlock = ASImageNodeTintColorModificationBlock(UIColor.white)
```

github上的相关讨论： https://github.com/facebookarchive/AsyncDisplayKit/issues/426

还有就是如果需要改变ASButtonNode 的 imageNode 的 tintColor，是改不了的，需要通过设置不同状态的图片，然后通过改变buttonNode的状态来改变图片。

```swift
buttonNode.setImage(image, for: .normal)
buttonNode.setImage(image.tinted(with: UIColor.red), for: .selected)
// https://gist.github.com/ImJCabus/3e6c80ca1a5dd23f8f9866c730e1f1c7 tintColor代码
```

## ASLayoutSpec

当 spaceBetween 没有达到两端对齐的效果，尝试设置当前 layoutSpec 的 width（如注释）或它的上一级布局对象的 alignItems，在例子中就是 stackLayout.alignItems = .stretch。 [Texture 布局篇](https://bawn.github.io/2017/12/Texture-Layout/)

## ASDisplayNode的高度计算

如果在 UIView 或者UITableViewCell中添加ASDisplayNode，而且需要计算ASDisplayNode的高度，在 ASDisplayNode 实现了 `- (ASLayoutSpec *)layoutSpecThatFits:(ASSizeRange)constrainedSize` 情况下，可以调用 `- (ASLayout *)layoutThatFits:(ASSizeRange)constrainedSize` 方法计算出大小。

```swift
_ = node.layoutThatFits(ASSizeRangeMake(CGSize.zero,
						  CGSize(width: view.frame.width,								  		 height: CGFloat.greatestFiniteMagnitude)))
print(node.calculatedSize.height)
```

## 给 ASDisplayNode 的 View 添加手势

> -didLoad This method is conceptually similar to UIViewController’s -viewDidLoad method; it’s called once and is the point where the backing view has been loaded. It is guaranteed to be called on the main thread and is the appropriate place to do any UIKit things (such as adding gesture recognizers, touching the view / layer, initializing UIKit objects).

需要在didLoad中添加

```swift
/** @name View Lifecycle */
    
    /**
     * @abstract Called on the main thread immediately after self.view is created.
     *
     * @discussion This is the best time to add gesture recognizers to the view.
     */
open func didLoad()
```

## ASDisplayNode 使用 initWithViewBlock 方法进行初始化

需要注意 `retain cycle` 的问题，持有 self 变量要设置为 `weak`。另外ASDisplayNode 并不知道自己持有的View的大小，需要对 `style.preferredSize` 进行设置。

## ASTextNode2 attachment的问题

ASTextNode2 目前尚未支持通过添加 NSTextAttachment 的方式在 NSAttributedString 后面添加图片，如果需要实现上面的需求要使用ASTextNode。

## ASCellNode里面再嵌套UITableViewCell

为了复用一些布局，比如个人界面的设置Cell，采用了在ASCellNode使用viewBlock方法来复用Cell。

```swift
let cellNode = ASCellNode(viewBlock: { () -> UIView in
						let cell = UITableViewCell(style: .default, reuseIdentifier: nil)
	//					cell.isUserInteractionEnabled = false
						return cell
					})
```

显示出来的布局是正常的，在iOS 11上点击也可以跳转，但是今天在iOS 10上测试的时候发现无法响应点击事件，如果是用UIView生成也可以响应点击事件，怀疑是UITableViewCell拦截了点击事件，但是为什么在iOS 11上可以，iOS 10上就不可以？不知道。加上 ：

```swift
cell.isUserInteractionEnabled = false
```

在iOS 10也可以响应点击事件了。

## ASEditableTextNode

ASEditableTextNode 默认高度只能适应英文字母，如果输入中文会发现被裁了一截，所以在初始化时需要指定一下 ASEditableTextNode 的高度

```swift
let editableTextNode = ASEditableTextNode()
editableTextNode.style.height = ASDimensionMake(44)
```

## ASTableNode 和 ASCollectionNode

### ASTableNode，ASCollectionNode调用reloadData时闪烁的问题。

在ASTableNode和ASCollectionNode需要刷新时不推荐直接使用 `reloadData` ，直接调用 `reloadData` 时会发现整个node都会闪一下。 一个比较好的解决方法是每次刷新算出需要添加，删除或者刷新的 `indexPath` 或者 `section`，再对这部分调用对应的局部刷新方法。

```objective
// indexPaths
- (void)insertRowsAtIndexPaths:(NSArray *)indexPaths withRowAnimation:(UITableViewRowAnimation)animation;
- (void)deleteRowsAtIndexPaths:(NSArray *)indexPaths withRowAnimation:(UITableViewRowAnimation)animation;
- (void)reloadRowsAtIndexPaths:(NSArray *)indexPaths withRowAnimation:(UITableViewRowAnimation)animation;

// sections
- (void)insertSections:(NSIndexSet *)sections withRowAnimation:(UITableViewRowAnimation)animation;
- (void)deleteSections:(NSIndexSet *)sections withRowAnimation:(UITableViewRowAnimation)animation;
- (void)reloadSections:(NSIndexSet *)sections withRowAnimation:(UITableViewRowAnimation)animation;
```
