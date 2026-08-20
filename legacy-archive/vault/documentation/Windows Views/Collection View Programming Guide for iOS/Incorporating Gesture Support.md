---
title: iOS Collection View 编程指南
apple_id: TP40012334
resource_type: Guide
platform: tvOS|iOS
topic: User Experience
technology: UIKit
published: '2014-07-15'
source_url: https://developer.apple.com/library/archive/documentation/WindowsViews/Conceptual/CollectionViewPGforIOS/IncorporatingGestureSupport/IncorporatingGestureSupport.html
archived_at: '2026-07-18T02:22:42.080933Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [iOS Collection View 编程指南](About%20iOS%20Collection%20Views.md)


[下一页](Creating%20Custom%20Layouts.md)[上一页](Using%20the%20Flow%20Layout.md)

# 加入手势支持

你可以借助手势识别器为 collection view 增添更强的交互性。给 collection view 添加一个手势识别器，用它在相应手势发生时触发操作。对于 collection view，你可能想实现的操作通常有两类：

- 你想触发 collection view 布局信息的变化。
- 你想直接操作单元格和视图。

你应该始终把手势识别器附加到 collection view 本身，而不是某个特定的单元格或视图上。[UICollectionView](https://developer.apple.com/documentation/uikit/uicollectionview) 类是 `UIScrollView` 的后代，因此把手势识别器附加到 collection view 上，不太会干扰它必须跟踪的其他手势。此外，由于 collection view 能访问你的数据源和布局对象，你仍然可以拿到恰当操作单元格和视图所需的全部信息。

手势识别器提供了一种动态修改布局参数的简便方式。例如，你可以用捏合手势识别器来改变自定义布局中项目之间的间距。配置这样一个手势识别器的过程相对简单。

1. 创建手势识别器。
2. 把手势识别器附加到 collection view 上。
3. 在手势识别器的处理方法中更新布局参数，并使布局对象失效。

你可以用创建所有对象时都用的那套 `alloc/init` 流程来创建手势识别器。在初始化过程中，你要指定手势被触发时调用的目标对象和动作方法。然后调用 collection view 的 [addGestureRecognizer:](https://developer.apple.com/documentation/uikit/uiview/1622496-addgesturerecognizer) 方法把它附加到视图上。实际的工作大多发生在你在初始化时指定的那个动作方法里。

清单 4-1 展示了一个动作方法的例子，它由附加在 collection view 上的捏合手势识别器调用。在这个例子中，捏合数据被用来改变自定义布局中单元格之间的距离。布局对象实现了自定义的 `updateSpreadDistance` 方法，该方法校验新的距离值并把它保存下来，供之后的布局过程使用。随后，动作方法使布局失效，强制它根据新值更新各项目的位置。

__清单 4-1__  使用手势识别器改变布局取值

```objc
- (void)handlePinchGesture:(UIPinchGestureRecognizer *)sender {
    if ([sender numberOfTouches] != 2)
        return;

   // 获取捏合的两个触点。
   CGPoint p1 = [sender locationOfTouch:0 inView:[self collectionView]];
   CGPoint p2 = [sender locationOfTouch:1 inView:[self collectionView]];

   // 计算新的展开距离。
    CGFloat xd = p1.x - p2.x;
    CGFloat yd = p1.y - p2.y;
    CGFloat distance = sqrt(xd*xd + yd*yd);

   // 更新自定义布局参数并使布局失效。
   MyCustomLayout* myLayout = (MyCustomLayout*)[[self collectionView] collectionViewLayout];
   [myLayout updateSpreadDistance:distance];
   [myLayout invalidateLayout];
}
```

有关创建手势识别器并把它们附加到视图上的更多信息，请参阅 _Event Handling Guide for iOS_。

[UICollectionView](https://developer.apple.com/documentation/uikit/uicollectionview) 类会监听单次轻点，以触发它用于高亮和选中的委托方法。如果你想给 collection view 添加自定义的轻点或长按手势，请把手势识别器的取值配置成与 collection view 已经使用的取值不同。例如，你可以把轻点手势识别器配置成只响应双击。

清单 4-2 展示了如何让 collection view 响应你的手势，而不是去监听单元格的选中/高亮。由于 collection view 并不是用手势识别器来触发其委托方法的，你可以把手势识别器的 [delaysTouchesBegan](https://developer.apple.com/documentation/uikit/uigesturerecognizer/1624234-delaystouchesbegan) 属性设为 `YES` 来延迟其他触摸事件的登记，或者把手势识别器的 [cancelsTouchesInView](https://developer.apple.com/documentation/uikit/uigesturerecognizer/1624218-cancelstouchesinview) 属性设为 `YES` 来取消触摸事件，从而让你的自定义手势识别器优先于默认的选中监听。这样，每当一次轻点被登记时，系统都会先检查你的手势识别器是否应当优先。如果输入对你的手势识别器无效，那么委托方法就会像往常一样被调用。

__清单 4-2__  让你的手势识别器优先

```objc
UITapGestureRecognizer* tapGesture = [[UITapGestureRecognizer alloc] initWithTarget:self action:@selector(handleTapGesture:)];
tapGesture.delaysTouchesBegan = YES;
tapGesture.numberOfTapsRequired = 2;
[self.collectionView addGestureRecognizer:tapGesture];
```


你如何用手势识别器操作单元格和视图，取决于你打算做哪种操作。简单的插入和删除可以在标准手势识别器的动作方法内完成。但如果你打算做更复杂的操作，可能就需要定义一个自定义手势识别器来自行跟踪触摸事件。

有一类操作必须用自定义手势识别器才能完成，那就是把 collection view 中的某个单元格从一个位置移到另一个位置。移动单元格最直接的做法是：（暂时）把它从 collection view 中删除，用手势识别器拖动该单元格的一个可视替身，等触摸事件结束时再把该单元格插入到新位置。所有这些都要求你自行管理触摸事件，与布局对象紧密配合来确定新的插入位置，处理数据源的变更，然后把该项目插入到新位置。

有关创建自定义手势识别器的更多信息，请参阅 _Event Handling Guide for iOS_。

[下一页](Creating%20Custom%20Layouts.md)[上一页](Using%20the%20Flow%20Layout.md)

