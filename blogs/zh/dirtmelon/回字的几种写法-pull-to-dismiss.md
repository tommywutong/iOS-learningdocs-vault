---
title: 回字的几种写法 - Pull To Dismiss
source: dirtmelon
source_key: dirtmelon
source_url: 'https://dirtmelon.github.io/posts/Pull-To-Dismiss/'
original_language: zh
published: 2019-07-13
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:079ccd69d31f3efc'
translated: n/a
---

> 原文：[回字的几种写法 - Pull To Dismiss](https://dirtmelon.github.io/posts/Pull-To-Dismiss/)　·　dirtmelon

有些 App 在弹出评论列表，或者其它界面时，是从底部弹出的，且下拉对应的 ScrollView 也可以触发 dismiss 的动画，不需要去点击按钮，在交互上来说也是连续的。

在实现这个需求的过程，我发现这个需求有几种写法，这几种写法都需要先给对应的 `ViewController` 添加 `UIPanGestureRecognizer` 手势，只是对手势的处理方法不同，添加手势的方法如下：

```swift
 let panGestureRecognizer = UIPanGestureRecognizer(target: self,
                                                   action: #selector(handleDismissPanGesture(_:)))
 view.addGestureRecognizer(panGestureRecognizer)
```

下面说说这几种写法的具体实现。（文中的 UITableView 可以替换成 UICollectionView 或者 UIScrollView）

## 不继承 UITableView

不继承 UITableView 有两种写法，由手势是否连续进行区分。

### 连续的手势操作

这种写法不把 `UITableView` 的滑动手势和自己添加的手势分隔开来，在 `UITableView` 滑动到顶部时，如果再接着滑动，就会触发 `ViewController` 的消失动画。

首先给手势设置 delegate 和对应的 delegate 方法，使它可以接受其它手势，从而不影响 `UITableView` 的滑动：

```swift
func gestureRecognizer(_ gestureRecognizer: UIGestureRecognizer,
                       shouldRecognizeSimultaneouslyWith otherGestureRecognizer: UIGestureRecognizer) -> Bool {
    return true
}
```

接着，需要防止在 dismiss 过程中 `UITableView` 滑动：

```swift
func scrollViewDidScroll(_ scrollView: UIScrollView) {
    /// 防止在 dismiss 过程中 tableView 滑动
    if scrollView.contentOffset.y < 0 {
        scrollView.setContentOffset(.zero, animated: false)
    } else if let currentTableViewOffset = currentTableViewOffset {
        scrollView.setContentOffset(currentTableViewOffset, animated: false)
    }
}
```

接下来对自己添加的手势进行处理：

```swift
@objc private func handleDismissPanGesture(_ gestureRecognizer: UIPanGestureRecognizer) {
    let velocity = gestureRecognizer.velocity(in: gestureRecognizer.view)
    let translation = gestureRecognizer.translation(in: gestureRecognizer.view)
    if velocity.y > 0 && tableView.contentOffset.y <= -tableView.contentInset.top {
        if needToResetTranslation {
        /// 开始进行 dismiss ，且需要对 translation 进行复原，防止位置错乱
            dismiss(animated: true)
            needToResetTranslation = false
            gestureRecognizer.setTranslation(.zero, in: gestureRecognizer.view)
            currentTableViewOffset = tableView.contentOffset
        }
    }
    /// 如果已回滚到顶部，且在 dismiss 过程中，则复位 needToResetTranslation 和 currentTableViewOffset
    if translation.y < 0 && !needToResetTranslation {
        needToResetTranslation = true
        currentTableViewOffset = nil
    }
    /// 如果是在 dismiss 过程中，则进行 dismiss 的交互动画
    if !needToResetTranslation {
        interactiveDismissTransition?.didPan(with: gestureRecognizer)
    }
    /// 如果手势结束，则复位 needToResetTranslation
    if gestureRecognizer.state != .began && gestureRecognizer.state != .changed {
        needToResetTranslation = true
        currentTableViewOffset = nil
    }
}
```

优点：

1. 用户对 TableView 的滑动手势跟触发 dismiss 的手势是连续的，滚动到顶部时，再往上滑动即可触发 dismiss 的效果。
2. 不需要继承 UITableView

缺点：

1. 需要处理的边界情况较多
2. 用户在滑动到顶部时容易误触发 dismiss 的效果

### 不连续的手势操作

在添加手势后，需要设置在手势生效时，不触发 `UITableView` 的 `panGestureRecognizer` ：

```swift
tableView.panGestureRecognizer.require(toFail: panGestureRecognizer)
```

然后在手势是否开始设置条件，只有是上下滚动且 `UITableView` 已滚动到顶部时才开始：

```swift
func gestureRecognizerShouldBegin(_ gestureRecognizer: UIGestureRecognizer) -> Bool {
    guard let panGestureRecognizer = gestureRecognizer as? UIPanGestureRecognizer else {
        return false
        }
    let translation = panGestureRecognizer.translation(in: view)
    let velocityPoint = panGestureRecognizer.velocity(in: view)
    let isVerticalDrag = abs(velocityPoint.y) > abs(velocityPoint.x)
    if translation.y > 0 && tableView.contentOffset.y <= -tableView.contentInset.top {
        return true
    }
    return !isVerticalDrag
}
```

这种情况下手势的处理则比较简单了：

```swift
@objc private func handleDismissPanGesture(_ gesture: UIPanGestureRecognizer) {
    switch gesture.state {
    case .began:
        dismiss(animated: true)
    default: break
    }
    interactiveDismissTransition?.didPan(with: gesture)
}
```

优点：

1. ；
2. 不需要处理较多的边界情况

缺点：

1. 的滑动手势跟触发 dismiss 的手势不是连续的，滚动到顶部时，需要松开后然后再次向上滑动；

## 继承 UITableView

继承 `UITableView` 的写法比较简单，不需要对自己添加的手势进行处理，唯一的缺点就是需要继承对应的类。比如如果需要对 `UITableView` 进行处理，首先需要继承自 `UITableView` ，然后在子类中对 `UITableView` 的手势进行处理：

```swift
class TableView: UITableView {

    override func gestureRecognizerShouldBegin(_ gestureRecognizer: UIGestureRecognizer) -> Bool {
        /// 在手势开始时判断是否需要开始滑动
        if gestureRecognizer.state == .possible {
            let translation = panGestureRecognizer.translation(in: self)
            if translation.y > 0 && contentOffset.y <= -contentInset.top {
                return false
            }
        }
        return true
    }
}
```

## 总结

上面几种写法各有各的优点，可以根据具体的业务需求或者框架限制选择不同的写法。Demo 也放到了 github 上，[PullToDismiss](https://github.com/dirtmelon/PullToDismiss)
