---
title: iOS View Controller 一览
apple_id: TP40011313
resource_type: Guide
platform: tvOS|iOS
topic: User Experience
technology: UIKit
published: '2014-11-15'
source_url: https://developer.apple.com/library/archive/documentation/WindowsViews/Conceptual/ViewControllerCatalog/Chapters/Popovers.html
archived_at: '2026-07-18T02:23:23.225857Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [iOS View Controller 一览](About%20View%20Controllers.md)


[下一页](Combined%20View%20Controller%20Interfaces.md)[上一页](Split%20View%20Controllers.md)

# Popover

尽管 [UIPopoverController](https://developer.apple.com/documentation/uikit/uipopovercontroller) 类本身并不是一个 View Controller，但它负责管理 View Controller 的呈现。你用 popover controller 对象通过 _popover_ 来呈现内容，popover 是一个浮动在 app 窗口之上的视觉层。popover 提供了一种轻量的方式来向用户展示信息或从用户那里收集信息，常见于以下场景：

- 显示屏幕上某个对象的相关信息
- 管理经常访问的工具或配置选项
- 呈现一组可以对你某个视图内的对象执行的操作
- 当设备处于竖屏方向时，呈现 split view controller 中的一个面板

相比模态视图，用 popover 来完成上述操作对用户的打扰更小、也不那么笨重。在 iPad app 中，模态视图应当只留给那些必须让用户明确接受或取消某项操作或某条信息的场合。例如，你会用模态视图要求用户输入密码，从而获准访问 app 的其余部分。而在大多数其他情况下，你应当改用 popover。popover 的优势在于它不会覆盖整个屏幕，只要在 popover 视图之外轻点一下就能把它消除。因此，当并不要求用户与你的内容交互，而只是为用户提供信息或附加功能时，popover 是绝佳的选择。

图 5-1 展示了用 popover 显示 split view 界面中某个面板的例子。在 popover 中选中一出剧目，会让 app 的主视图显示该剧目的相关信息。（关于创建 split view 界面的更多信息，参见 [Split View Controllers](Split%20View%20Controllers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgmjtfvbuqnznknltc)。）

__图 5-1__  用 popover 显示主面板

!!

popover 的内容来自你提供的 [View Controller 对象](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ControllerObject.html#//apple_ref/doc/uid/TP40008195-CH11)。popover 能够呈现大多数类型的 View Controller。当你准备好在 popover 中呈现该 View Controller 时，执行以下步骤：

1. [创建](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectCreation.html#//apple_ref/doc/uid/TP40008195-CH39)一个 [UIPopoverController](https://developer.apple.com/documentation/uikit/uipopovercontroller) 类的实例，并用你的 View Controller 对象对它进行[初始化](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Initialization.html#//apple_ref/doc/uid/TP40008195-CH21)。
2. 指定 popover 的尺寸，有两种做法：

   - 给你想在 popover 中显示的 View Controller 的 [contentSizeForViewInPopover](https://developer.apple.com/documentation/uikit/uiviewcontroller/1619323-contentsizeforviewinpopover) 属性赋值。
   - 给 popover controller 自身的 [popoverContentSize](https://developer.apple.com/documentation/uikit/uipopovercontroller/1624667-contentsize) [属性](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/DeclaredProperty.html#//apple_ref/doc/uid/TP40008195-CH13)赋值。
3. （可选）给 popover 指定一个[委托](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14)。关于委托的职责，参见[实现 popover 委托](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgmjtfvbuqnjnknltcma)。
4. 呈现 popover。

呈现 popover 时，你要把它与用户界面的某个特定部分关联起来。popover 通常与工具栏按钮关联，因此 [presentPopoverFromBarButtonItem:permittedArrowDirections:animated:](https://developer.apple.com/documentation/uikit/uipopovercontroller/1624668-presentpopoverfrombarbuttonitem) 方法是从 app 工具栏呈现 popover 的便捷做法。你也可以用 [presentPopoverFromRect:inView:permittedArrowDirections:animated:](https://developer.apple.com/documentation/uikit/uipopovercontroller/1624660-present) 方法把 popover 关联到某个视图的特定区域。

popover 通常从被呈现的 View Controller 的 [contentSizeForViewInPopover](https://developer.apple.com/documentation/uikit/uiviewcontroller/1619323-contentsizeforviewinpopover) 属性获取初始尺寸。该属性存储的默认尺寸是宽 320 像素、高 1100 像素。你可以给 `contentSizeForViewInPopover` 属性赋新值来自定义这个默认值。或者，你也可以给 popover controller 自身的 `popoverContentSize` 属性赋值。如果你更换了 popover 所显示的 View Controller，你放进 `popoverContentSize` 属性的任何自定义尺寸信息都会被新 View Controller 的尺寸取代。在 popover 可见期间，对内容 View Controller 或其尺寸所做的更改会自动以动画形式呈现。你也可以用 [setPopoverContentSize:animated:](https://developer.apple.com/documentation/uikit/uipopovercontroller/1624670-setpopovercontentsize) 方法更改尺寸（可以带动画，也可以不带）。

清单 5-1 展示了一个简单的[动作方法](https://developer.apple.com/library/archive/documentation/General/Conceptual/Devpedia-CocoaApp/TargetAction.html#//apple_ref/doc/uid/TP40009071-CH3)，它在用户轻点工具栏按钮时呈现一个 popover。popover 被保存在一个属性中（由拥有它的类定义），该属性对 popover 对象保持强引用。这里把 popover 的尺寸设成了 View Controller 视图的尺寸，但两者不必相同。当然，如果两者不同，你就必须用滚动视图来确保用户能看到 popover 的全部内容。

__清单 5-1__  以编程方式呈现 popover

```objc
- (IBAction)toolbarItemTapped:(id)sender
{
   MyViewController* content = [[MyViewController alloc] init];
   UIPopoverController* aPopover = [[UIPopoverController alloc]
        initWithContentViewController:content];
   aPopover.delegate = self;

   // 把 popover 保存到自定义属性中，供之后使用。
   self.popoverController = aPopover;

   [self.popoverController presentPopoverFromBarButtonItem:sender
        permittedArrowDirections:UIPopoverArrowDirectionAny animated:YES];
}
```

当用户在 popover 视图外部轻点时，popover 会被自动消除。在 popover 内部轻点不会导致它被自动消除，但你可以用 [dismissPopoverAnimated:](https://developer.apple.com/documentation/uikit/uipopovercontroller/1624662-dismisspopoveranimated) 方法以编程方式把它消除。当用户在你的 View Controller 内容中选中了某一项，或者执行了某个应当让 popover 从屏幕上移除的操作时，你就可以这么做。如果你确实要以编程方式消除 popover，就需要把 popover controller 对象的引用保存在你的 View Controller 能访问到的地方。系统不会提供指向当前活动 popover controller 的引用。

当 popover 因用户在其外部轻点而被消除时，popover 会自动把这一操作通知它的[委托](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14)。如果你提供了委托，就可以用这个对象阻止 popover 被消除，或者在消除时执行额外的操作。[popoverControllerShouldDismissPopover:](https://developer.apple.com/documentation/uikit/uipopovercontrollerdelegate/1624661-popovercontrollershoulddismisspo) 委托方法让你控制 popover 是否真的应该被消除。如果你的委托没有实现该方法，或者你的实现返回 `YES`，控制器就会消除 popover，并向委托发送 [popoverControllerDidDismissPopover:](https://developer.apple.com/documentation/uikit/uipopovercontrollerdelegate/1624671-popovercontrollerdiddismisspopov) 消息。

在大多数情况下，你根本不需要重写 `popoverControllerShouldDismissPopover:` 方法。提供这个方法是为了应对消除 popover 可能给 app 带来问题的场合。不过，与其从该方法返回 `NO`，不如从一开始就避免那种需要让 popover 一直保持活动的设计。例如，更好的做法可能是以模态方式呈现你的内容，强制用户输入必需的信息，或者接受或取消所做的更改。

当你的委托的 `popoverControllerDidDismissPopover:` 方法被调用时，popover 本身已经从屏幕上移除了。此时，如果你不打算再使用它，就可以安全地移除对该 popover controller 的现有引用。你也可以在这个方法里刷新用户界面或更新 app 的状态。

为你的 app 编写与 popover 相关的代码时，请考虑以下几点：

- 以编程方式消除 popover 需要一个指向 popover controller 的指针。得到这种指针的唯一办法就是自己把它存起来，通常存在内容 [View Controller](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ControllerObject.html#//apple_ref/doc/uid/TP40008195-CH11) 里。这样才能保证内容 View Controller 有能力在用户执行相应操作时消除 popover。
- 你可以缓存 popover controller 并复用它们，而不必每次都从头创建新的。popover controller 的可塑性很强，每次使用时你都可以为它指定不同的 View Controller 和配置选项。
- 呈现 popover 时，尽可能为允许的箭头方向指定 [UIPopoverArrowDirectionAny](https://developer.apple.com/documentation/uikit/uipopoverarrowdirection/uipopoverarrowdirectionany) 常量。指定这个常量能让 UIKit 在定位和调整 popover 尺寸时拥有最大的灵活性。如果你只指定了有限的几个允许箭头方向，popover controller 可能不得不先把 popover 的尺寸缩小，然后再显示它。

[下一页](Combined%20View%20Controller%20Interfaces.md)[上一页](Split%20View%20Controllers.md)

