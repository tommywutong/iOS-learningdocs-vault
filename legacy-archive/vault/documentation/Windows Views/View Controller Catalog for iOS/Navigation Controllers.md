---
title: iOS View Controller 一览
apple_id: TP40011313
resource_type: Guide
platform: tvOS|iOS
topic: User Experience
technology: UIKit
published: '2014-11-15'
source_url: https://developer.apple.com/library/archive/documentation/WindowsViews/Conceptual/ViewControllerCatalog/Chapters/NavigationControllers.html
archived_at: '2026-07-18T02:23:04.928501Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [iOS View Controller 一览](About%20View%20Controllers.md)


[下一页](Tab%20Bar%20Controllers.md)[上一页](About%20View%20Controllers.md)

# Navigation Controller

navigation controller 管理着一个 View Controller 栈，为层级化的内容提供逐级深入的界面。navigation controller 的视图层级是自包含的，它由 navigation controller 直接管理的视图和你提供的内容 View Controller 所管理的视图共同组成。每个内容 View Controller 管理一套各自独立的视图层级，而 navigation controller 负责协调这些视图层级之间的导航。

尽管导航界面的绝大部分内容都是你的自定义内容，仍有一些地方需要你的代码直接与 navigation controller 对象打交道。除了告诉 navigation controller 何时显示新视图之外，你还要负责配置导航栏——即屏幕顶部那个用于说明用户当前位于导航层级中何处的视图。此外，你也可以为 navigation controller 所管理的工具栏提供条目。

本章介绍如何在 app 中配置和使用 navigation controller。关于把 navigation controller 与其他类型的 View Controller 对象组合起来使用的方式，请参阅[组合 View Controller 界面](Combined%20View%20Controller%20Interfaces.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgmjtfvbuqnrnknltc).

navigation controller 的首要工作是管理内容 View Controller 的呈现，同时它也负责呈现自己的一些定制视图。具体来说，它会呈现一个导航栏，其中包含一个返回按钮以及若干你可以自定义的按钮。navigation controller 还可以选择性地呈现一个导航工具栏视图，并在其中填充自定义按钮。

图 1-1 展示了一个导航界面。图中的导航视图就是存放在 navigation controller 的 [view](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621460-view) 属性中的那个视图。界面中其余所有视图都属于由 navigation controller 管理的、对外不透明的视图层级。

__图 1-1__  导航界面中的各个视图

!

尽管导航栏和工具栏都是可定制的视图，你也绝不能直接修改导航层级中的这些视图。定制它们的唯一途径是使用 [UINavigationController](https://developer.apple.com/documentation/uikit/uinavigationcontroller) 和 [UIViewController](https://developer.apple.com/documentation/uikit/uiviewcontroller) 类的方法。关于如何定制导航栏的内容，请参阅[定制导航栏外观](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgmjtfvbuqmrnknltg)。关于如何在导航界面中显示和配置自定义工具栏条目，请参阅[显示导航工具栏](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgmjtfvbuqmrnknlti)。

navigation controller 借助若干对象来实现导航界面。其中一部分对象由你负责提供，其余的则由 navigation controller 自行创建。具体来说，你要负责提供承载待展示内容的 View Controller。如果你想响应来自 navigation controller 的通知，还可以提供一个[委托对象](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14)。导航界面所用的视图——例如导航栏和工具栏——由 navigation controller 创建，并且由它负责管理。图 1-2 展示了 navigation controller 与这些关键对象之间的关系。

__图 1-2__  由 navigation controller 管理的对象

!

对于与 navigation controller 关联的导航栏和工具栏对象，你只能定制其外观和行为的部分方面，配置和显示它们的工作完全由 navigation controller 负责。此外，navigation controller 对象会自动把自己设为其 [UINavigationBar](https://developer.apple.com/documentation/uikit/uinavigationbar) 对象的委托，并阻止其他对象改变这一关系。

你可以修改委托，也可以修改导航栈上的其他 View Controller。_导航栈_ 是一个由 navigation controller 管理的、后进先出的自定义 View Controller 对象集合。第一个加入栈中的条目会成为_根 View Controller_，它永远不会被弹出栈。其他条目可以通过 [UINavigationController](https://developer.apple.com/documentation/uikit/uinavigationcontroller) 类的方法加入栈中。

图 1-3 展示了 navigation controller 与导航栈上各对象之间的相关关系。（注意，栈顶 View Controller 与当前可见的 View Controller 不一定是同一个。例如，如果你以模态方式呈现一个 View Controller，`visibleViewController` 属性的值会变成被呈现的那个模态 View Controller，而 `topViewController` 属性则不会改变。）

__图 1-3__  导航栈

!

navigation controller 的首要职责是响应用户操作，把新的内容 View Controller 压入栈中，或者把内容 View Controller 从栈中弹出。你压入导航栈的每个 View Controller 都负责呈现 app 数据的某一部分。通常，当用户在当前可见的视图中选中某个条目时，你就创建一个包含该条目详情的 View Controller，并把它压入导航栈。例如，当用户在“照片”app 中选中某个相簿时，app 就会压入一个用于显示该相簿中照片的 View Controller。

这个过程遵循一个简单的设计模式——栈中的每个内容 View Controller 负责配置并压入位于它上方的那个内容 View Controller。你应当避免让某个 View Controller 依赖于“必须由某个特定类的实例把它压入栈中”这一前提。相反，若要在弹出 View Controller 的同时把数据回传给栈的下层，应把位于栈中较低位置的 View Controller 设为其上方那个 View Controller 的委托。

大多数情况下，你不需要以编程方式把 View Controller 弹出栈。navigation controller 会在导航栏上提供一个返回按钮，用户点按它时会自动弹出最顶层的 View Controller。

关于如何定制导航栏的更多信息，请参阅[定制导航栏外观](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgmjtfvbuqmrnknltg)。关于把 View Controller 压入导航栈（以及之后将其移除）的信息，请参阅[修改导航栈](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgmjtfvbuqmrnknltcmq)。关于如何定制工具栏的内容，请参阅[显示导航工具栏](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgmjtfvbuqmrnknlti)。

创建导航界面时，你需要先想清楚打算怎样使用它。由于导航界面会给你的数据强加一种总体的组织方式，你只应按以下这几种特定方式使用它：

- 直接把它安装为窗口的根 View Controller。
- 把它安装为标签栏界面中某个标签的 View Controller。
- 把它安装为分栏视图界面中两个根 View Controller 之一。（仅限 iPad）
- 从另一个 View Controller 以模态方式呈现它。
- 在 popover 中显示它。（仅限 iPad）

在前三种场景中，navigation controller 构成了你基本界面的关键部分，并会一直存在到 app 退出。后两种场景则体现了 navigation controller 更为临时的用法，此时使用 navigation controller 的流程与使用其他内容 View Controller 的流程完全相同，唯一的区别是 navigation controller 还会继续提供单个内容 View Controller 所不具备的额外导航功能。虽然接下来几节着重讲解如何创建较为持久的那类导航界面，但其中大部分定制步骤和通用信息对所有 navigation controller 都适用，无论你打算如何使用它们。

每个导航界面都有一层数据代表根层级，这一层是你界面的起点。例如，“照片”app 在其数据层级的根层级显示可用相簿的列表；选中某个相簿后会显示该相簿中的照片，再选中某张照片则会显示这张照片的放大版本。

__图 1-4__  为每一层数据定义 View Controller

!

要实现导航界面，你必须先确定在数据层级的每一层展示什么数据。对于每一层，你都必须提供一个内容 View Controller 来管理和展示该层的数据。如果多个层级的展示方式相同，你可以创建同一个 View Controller 类的多个实例，并分别配置它们各自管理的数据。例如，如图 1-4 所示，“照片”app 有三种不同的展示类型，因此它需要使用三个不同的 View Controller 类。

除了管理叶子数据的 View Controller 之外，每个内容 View Controller 都必须为用户提供一种进入下一层数据层级的方式。展示条目列表的 View Controller 可以利用用户在某个表格单元格上的点按来显示下一层数据。例如，当用户从顶层列表中选中某个相簿时，“照片”app 会创建一个新的相簿 View Controller，并用足够的相簿信息初始化这个新的 View Controller，使它能够展示相应的照片。

关于定义自定义 View Controller 的一般信息和指导，请参阅 _[iOS View Controller 编程指南](https://developer.apple.com/library/archive/featuredarticles/ViewControllerPGforiPhoneOS/index.html#//apple_ref/doc/uid/TP40007457)_ 中的“创建自定义内容 View Controller”。

如果你正在创建一个新的 Xcode 项目，Master-Detail Application 模板会在 storyboard 中为你提供一个 navigation controller，并把它设为第一个场景。

要在 storyboard 中创建 navigation controller，请执行以下操作：

1. 从库中拖出一个 navigation controller。
2. Interface Builder 会创建一个 navigation controller 和一个 View Controller，并在二者之间建立关系。这一关系把新创建的 View Controller 标识为该 navigation controller 的根 View Controller。
3. 在 Attributes 检查器中勾选 Is Initial View Controller 选项，让它作为第一个 View Controller 显示（或者用其他方式在你的用户界面中呈现这个 View Controller）。

如果你更愿意以编程方式创建 navigation controller，可以在代码中任何合适的位置这样做。例如，如果 navigation controller 为你的 app 窗口提供根视图，你就可以在应用[委托](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14)的 [applicationDidFinishLaunching:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623053-applicationdidfinishlaunching) 方法中创建它。

[创建](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectCreation.html#//apple_ref/doc/uid/TP40008195-CH39) navigation controller 时，你必须完成以下工作：

1. 为导航界面创建根 View Controller。

   这个对象是导航栈中层级最高的 View Controller。显示它的视图时，导航栏不会显示返回按钮，而且这个 View Controller 无法从导航栈中弹出。
2. 创建 navigation controller，并使用 [initWithRootViewController:](https://developer.apple.com/documentation/uikit/uinavigationcontroller/1621858-initwithrootviewcontroller) 方法对它进行[初始化](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Initialization.html#//apple_ref/doc/uid/TP40008195-CH21)。
3. 把这个 navigation controller 设为窗口的根 View Controller（或以其他方式在界面中呈现它）。

清单 1-1 展示了 `applicationDidFinishLaunching:` 方法的一个简单实现，它创建一个 navigation controller，并把它设为 app 主窗口的根 View Controller。其中 `navigationController` 和 `window` 是应用委托的成员变量，`MyRootViewController` 则是一个自定义的 View Controller 类。当这个例子中的窗口显示出来时，导航界面会呈现该导航界面中根 View Controller 的视图。

__清单 1-1__  以编程方式创建 navigation controller

```objc
- (void)applicationDidFinishLaunching:(UIApplication *)application
{
    UIViewController *myViewController = [[MyViewController alloc] init];
    navigationController = [[UINavigationController alloc]
                                initWithRootViewController:myViewController];

    window = [[UIWindow alloc] initWithFrame:[[UIScreen mainScreen] bounds]];
    window.rootViewController = navigationController;
    [window makeKeyAndVisible];
}
```


通常，导航界面会把你的自定义内容显示在导航栏底部与工具栏（或标签栏）顶部之间的空隙里（参见[图 1-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgmjtfvbuqmrnknltcmy)）。不过，View Controller 也可以要求以全屏布局显示自己的视图。在全屏布局中，内容视图会被配置成按需延伸到导航栏、状态栏和工具栏的下方。这种安排能让用户看到尽可能多的内容，对照片展示或其他需要更大空间的场合很有用。

在判断某个视图是否应当调整为填满整个屏幕或屏幕的大部分时，navigation controller 会考虑若干因素，包括：

- 底层窗口（或父视图）的尺寸是否填满了整个屏幕范围？
- 导航栏是否被配置为半透明？
- 导航工具栏（如果用到的话）是否被配置为半透明？
- 底层 View Controller 的 [wantsFullScreenLayout](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621390-wantsfullscreenlayout) 属性是否设为了 `YES`？

这些因素共同决定自定义视图的最终尺寸。上面列表中各项的排列顺序也反映了它们被考虑的优先次序。窗口尺寸是首要的限制因素：如果 app 的主窗口（对于以模态方式呈现的 View Controller，则是包含它的父视图）没有铺满屏幕，其中包含的视图自然也做不到。同样，如果导航栏或工具栏可见但并非半透明，那么 View Controller 是否希望以全屏布局显示自己的视图就无关紧要了——navigation controller 绝不会把内容显示在不透明的导航栏下方。

如果你要创建导航界面，并希望自定义内容占据屏幕的大部分或全部，应当执行以下步骤：

1. 把自定义视图的 frame 配置为填满屏幕范围。

   同时别忘了配置视图的自动调整尺寸（autoresizing）特性。这些特性可确保视图在需要调整尺寸时相应地调整其内容。或者，当视图尺寸发生变化时，你也可以调用视图的 [setNeedsLayout](https://developer.apple.com/documentation/uikit/uiview/1622601-setneedslayout) 方法，表明其子视图的位置需要重新调整。
2. 要延伸到导航栏下方，请把 navigation controller 的 [translucent](https://developer.apple.com/documentation/uikit/uinavigationbar/1624928-istranslucent) [属性](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/DeclaredProperty.html#//apple_ref/doc/uid/TP40008195-CH13)设为 `YES`。
3. 要延伸到可选的工具栏下方，请把工具栏的 [translucent](https://developer.apple.com/documentation/uikit/uitoolbar/1618001-istranslucent) 属性设为 `YES`。
4. 要延伸到状态栏下方，请把 View Controller 的 [wantsFullScreenLayout](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621390-wantsfullscreenlayout) 属性设为 `YES`。

呈现导航界面时，你添加导航视图的那个窗口或视图也必须有合适的尺寸。如果 app 以 navigation controller 作为主界面，那么主窗口的尺寸就应当与屏幕尺寸一致。换句话说，你应当把它的尺寸设为 `UIScreen` 类的 [bounds](https://developer.apple.com/documentation/uikit/uiscreen/1617838-bounds) 属性的值（而不是 `applicationFrame` 属性的值）。事实上，对于导航界面，无论何种情形，通常都最好用全屏范围来创建窗口，因为 navigation controller 本来就会自动调整其视图的尺寸以适配状态栏。

如果你以模态方式呈现 navigation controller，那么该 navigation controller 所呈现的内容会受到执行呈现操作的那个 View Controller 的限制。如果那个 View Controller 不希望延伸到状态栏下方，那么以模态方式呈现的 navigation controller 也不会被允许延伸到状态栏下方。换句话说，父视图总会对其模态呈现的视图如何显示产生一定影响。

关于如何配置界面以支持全屏布局的更多信息，请参阅 _[iOS View Controller 编程指南](https://developer.apple.com/library/archive/featuredarticles/ViewControllerPGforiPhoneOS/index.html#//apple_ref/doc/uid/TP40007457)_ 中的“创建自定义内容 View Controller”。

你负责创建驻留在导航栈上的那些对象。初始化 navigation controller 对象时，你必须提供一个内容 View Controller 来显示数据层级的根内容。你可以以编程方式添加或移除 View Controller，也可以响应用户交互来添加或移除。navigation controller 类为管理导航栈的内容提供了多种方案，涵盖了你在 app 中可能遇到的各种场景。表 1-1 列出了这些场景以及相应的应对方式。

__表 1-1__  管理导航栈的各种方案

| 场景 | 说明 |
| --- | --- |
| 显示下一层的层级数据。 | 当用户选中最顶层 View Controller 所显示的某个条目时，你可以使用 segue 或 [pushViewController:animated:](https://developer.apple.com/documentation/uikit/uinavigationcontroller/1621887-pushviewcontroller) 方法把一个新的 View Controller 压入导航栈。这个新的 View Controller 负责呈现所选条目的内容。 |
| 在层级中回退一级。 | navigation controller 通常会提供一个返回按钮，用于把最顶层的 View Controller 从栈中移除并返回上一个屏幕。你也可以使用 [popViewControllerAnimated:](https://developer.apple.com/documentation/uikit/uinavigationcontroller/1621886-popviewcontroller) 方法以编程方式移除最顶层的 View Controller。 |
| 把导航栈恢复到之前的状态。 | app 启动时，你可以使用 [setViewControllers:animated:](https://developer.apple.com/documentation/uikit/uinavigationcontroller/1621861-setviewcontrollers) 方法把 navigation controller 恢复到之前的状态。例如，你可以用这个方法让用户回到上次退出 app 时正在查看的那个屏幕。  为了把 app 恢复到之前的状态，你必须先保存足够的状态信息，以便重新创建所需的 View Controller。当用户退出 app 时，你需要保存一些标记或其他信息来记录用户在数据层级中所处的位置。到下次启动时，再读取这些状态信息，用它们重新创建所需的 View Controller，然后调用 `setViewControllers:animated:` 方法。关于保存和恢复状态的更多信息，请参阅 _[iOS App 编程指南](https://developer.apple.com/library/archive/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40007072)_ 中的 [App 状态与多任务](https://developer.apple.com/library/archive/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/BackgroundExecution/BackgroundExecution.html#//apple_ref/doc/uid/TP40007072-CH4)。  你也可以用这个方法跳转到数据层级中的任意位置。不过跳转到任意位置很容易让用户困惑，因此你应当格外注意把正在发生的事情清楚地传达给用户。 |
| 让用户返回根 View Controller。 | 要回到导航界面的最顶层，请使用 [popToRootViewControllerAnimated:](https://developer.apple.com/documentation/uikit/uinavigationcontroller/1621855-poptorootviewcontrolleranimated) 方法。该方法会把导航栈中除根 View Controller 之外的所有 View Controller 全部移除。 |
| 在层级中一次回退任意多级。 | 要一次回退多级，请使用 [popToViewController:animated:](https://developer.apple.com/documentation/uikit/uinavigationcontroller/1621871-poptoviewcontroller) 方法。当你用 navigation controller 来管理自定义内容的编辑流程（而不是以模态方式呈现内容）时，可能会用到这个方法。如果用户在你压入多个编辑屏幕之后决定取消操作，你可以用这个方法一次性移除所有编辑屏幕，而不必一个一个地移除。 |

当你以动画方式压入或弹出 View Controller 时，navigation controller 会自动生成最合理的动画。例如，如果你用 `popToViewController:animated:` 方法一次把多个 View Controller 弹出栈，navigation controller 只会为最顶层的那个 View Controller 使用动画，其余中间的 View Controller 都会在没有动画的情况下被撤销。如果你以动画方式压入或弹出某一项，必须等这个动画完成之后，才能再去压入或弹出另一个 View Controller。

每当你压入或弹出 View Controller 时，navigation controller 都会向受影响的 View Controller 发送消息。当栈发生变化时，navigation controller 还会向它的[委托](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14)发送消息。图 1-5 展示了压入或弹出操作过程中发生的事件顺序，以及在各个阶段发送给你的自定义对象的相应消息。图中的“新 View Controller”指的是即将成为栈顶 View Controller 的那个 View Controller。

__图 1-5__  栈发生变化时发送的消息

!

你可以利用 navigation controller 委托的方法在各内容 View Controller 之间进行协调，比如更新它们之间共享的状态。如果你一次压入或弹出多个 View Controller，只有原先可见的那个 View Controller 和即将变为可见的那个 View Controller 会被调用这些方法；中间的那些 View Controller 不会被调用，除非这种连锁发生在某个回调内部（例如你在 `viewWillAppear:` 的实现中调用了 `pushViewController:animated:`）。

你可以使用 `UIViewController` 的 `isMovingToParentViewController` 和 `isMovingFromParentViewController` 方法，来判断某个 View Controller 的出现或消失是否由压入或弹出操作引起。

导航栏是在导航界面中管理各种控件的视图，当它由 navigation controller 对象管理时会承担一种特殊的角色。为了保证一致性并减少构建导航界面所需的工作量，每个 navigation controller 对象都会创建自己的导航栏，并承担管理该导航栏内容的大部分职责。必要时，navigation controller 会与其他对象（比如你的内容 View Controller）协作来完成这一过程。

导航栏的结构在很多方面都与 navigation controller 的结构相似。和 navigation controller 一样，导航栏也是一个容器，承载由其他对象提供的内容。就导航栏而言，其内容由一个或多个 [UINavigationItem](https://developer.apple.com/documentation/uikit/uinavigationitem) 对象提供，这些对象存放在一个称为导航项栈的栈式数据结构中。每个导航项都提供一整套要在导航栏中显示的视图和内容。

图 1-6 展示了运行时与导航栏相关的一些关键对象。导航栏的拥有者（无论它是 navigation controller 还是你自己的代码）负责按需把导航项压入栈中或从栈中弹出。为了提供正确的导航，导航栏会保留指向栈中若干特定对象的指针。虽然导航栏的大部分内容取自栈顶的导航项，但它同时还保留了一个指向返回项的指针，以便创建返回按钮（其标题取自前一个导航项）。

__图 1-6__  与导航栏关联的对象

!

在导航界面中，导航栈上的每个内容 View Controller 都通过其 [navigationItem](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621851-navigationitem) 属性提供一个导航项。导航栈与导航项栈始终是平行的：对于导航栈上的每个内容 View Controller，它的导航项在导航项栈中处于相同的位置。

导航栏把条目放置在三个主要位置：左侧、右侧和中间。表 1-2 列出了 [UINavigationItem](https://developer.apple.com/documentation/uikit/uinavigationitem) 类中用于配置这三个位置的[属性](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/DeclaredProperty.html#//apple_ref/doc/uid/TP40008195-CH13)。在配置导航项以配合 navigation controller 使用时要注意，某些位置上的自定义控件可能会被忽略，转而使用预期的控件。每个位置的说明中都包含了你的自定义对象将如何被使用的信息。

__表 1-2__  导航栏上的条目位置

| 位置 | 属性 | 说明 |
| --- | --- | --- |
| 左侧 | [backBarButtonItem](https://developer.apple.com/documentation/uikit/uinavigationitem/1624958-backbarbuttonitem)  [leftBarButtonItem](https://developer.apple.com/documentation/uikit/uinavigationitem/1624936-leftbarbuttonitem) | 在导航界面中，navigation controller 默认会在左侧位置放置一个返回按钮。要获取 navigation controller 提供的默认返回按钮，请读取 `backBarButtonItem` 属性的值。  要在左侧位置放置自定义按钮或视图，从而替换默认的返回按钮，请把一个 [UIBarButtonItem](https://developer.apple.com/documentation/uikit/uibarbuttonitem) 对象赋给 `leftBarButtonItem` 属性。 |
| 中间 | [titleView](https://developer.apple.com/documentation/uikit/uinavigationitem/1624935-titleview) | 在导航界面中，navigation controller 默认会显示一个带有你的内容 View Controller 标题的自定义视图。你可以按需用自己的自定义视图替换这个视图。  如果你没有提供自定义标题视图，导航栏会显示一个带有导航项标题字符串的自定义视图；如果导航项也没有提供标题，导航栏就使用 View Controller 的标题。 |
| 右侧 | [rightBarButtonItem](https://developer.apple.com/documentation/uikit/uinavigationitem/1624957-rightbarbuttonitem) | 这个位置默认为空，通常用于放置编辑或修改当前屏幕的按钮。你也可以把视图包装在 `UIBarButtonItem` 对象中，从而把自定义视图放到这里。 |

图 1-7 展示了在导航界面中导航栏内容的组装方式。与当前 View Controller 关联的导航项提供导航栏中间和右侧位置的内容，而前一个 View Controller 的导航项提供左侧位置的内容。虽然左侧和右侧条目要求你指定 [UIBarButtonItem](https://developer.apple.com/documentation/uikit/uibarbuttonitem) 对象，但你可以像图中那样把视图包装进一个 bar button item 里。如果你没有提供自定义标题视图，导航项会用当前 View Controller 的标题为你创建一个。

__图 1-7__  导航栏的结构

!

当导航栏与 navigation controller 配合使用时，你必须始终使用 `UINavigationController` 的 [setNavigationBarHidden:animated:](https://developer.apple.com/documentation/uikit/uinavigationcontroller/1621885-setnavigationbarhidden) 方法来显示和隐藏导航栏，绝不能通过直接修改 `UINavigationBar` 对象的 [hidden](https://developer.apple.com/documentation/uikit/uiview/1622585-hidden) [属性](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/DeclaredProperty.html#//apple_ref/doc/uid/TP40008195-CH13)来隐藏导航栏。除了显示或隐藏导航栏之外，使用 navigation controller 的方法还能免费获得更完善的行为。具体来说，如果某个 View Controller 在它的 [viewWillAppear:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621510-viewwillappear) 方法中显示或隐藏导航栏，navigation controller 会为导航栏的出现或消失添加动画，使其与新 View Controller 的出现同步。

由于用户需要借助导航栏上的返回按钮回到上一个屏幕，所以在隐藏导航栏时，你绝不能不给用户留下任何返回上一屏的途径。提供导航支持最常见的做法是拦截触摸事件，用它们来切换导航栏的可见性。例如，“照片”app 在全屏显示单张图片时就是这么做的。你也可以检测轻扫手势，用它把当前 View Controller 弹出栈，但这种行为不如直接切换导航栏可见性那样容易被用户发现。

在导航界面中，navigation controller 拥有自己的 [UINavigationBar](https://developer.apple.com/documentation/uikit/uinavigationbar) 对象，并负责管理它。你不能替换这个导航栏对象，也不能直接修改它的 bounds、frame 或 alpha 值。不过，有几个[属性](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/DeclaredProperty.html#//apple_ref/doc/uid/TP40008195-CH13)是可以修改的，包括：

- [barStyle](https://developer.apple.com/documentation/uikit/uinavigationbar/1624955-barstyle) 属性
- [translucent](https://developer.apple.com/documentation/uikit/uinavigationbar/1624928-istranslucent) 属性
- [tintColor](https://developer.apple.com/documentation/uikit/uinavigationbar/1624937-tintcolor) 属性

图 1-8 展示了 `barStyle` 和 `translucent` 属性对导航栏外观的影响。对于半透明样式，值得注意的是：如果底层 View Controller 的主视图是滚动视图，导航栏会自动调整 content inset 的值，使内容能够从导航栏下方滚出来；对于其他类型的视图，它不会做这种调整。

__图 1-8__  导航栏样式

!

如果你想显示或隐藏整个导航栏，同样应当使用 navigation controller 的 [setNavigationBarHidden:animated:](https://developer.apple.com/documentation/uikit/uinavigationcontroller/1621885-setnavigationbarhidden) 方法，而不是直接修改导航栏。关于显示和隐藏导航栏的更多信息，请参阅[显示与隐藏导航栏](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgmjtfvbuqmrnknltcni)。

要为某个特定的 View Controller 定制导航栏的外观，请修改与它关联的 [UINavigationItem](https://developer.apple.com/documentation/uikit/uinavigationitem) 对象的特性。你可以通过 View Controller 的 [navigationItem](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621851-navigationitem) [属性](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/DeclaredProperty.html#//apple_ref/doc/uid/TP40008195-CH13)获取它的导航项。View Controller 在你请求之前不会创建自己的导航项，因此只有当你打算把这个 View Controller 装入导航界面时，才应该去请求这个对象。

如果你选择不修改 View Controller 的导航项，导航项会提供一组默认对象，它们在很多情况下已经够用。你所做的任何定制都优先于这些默认对象。

对于最顶层的 View Controller，显示在导航栏左侧的条目按以下规则确定：

- 如果你为最顶层 View Controller 的导航项的 [leftBarButtonItem](https://developer.apple.com/documentation/uikit/uinavigationitem/1624936-leftbarbuttonitem) 属性指定了自定义 bar button item，这个条目的优先级最高。
- 如果你没有提供自定义 bar button item，而导航栈上下一级的那个 View Controller 的导航项在其 [backBarButtonItem](https://developer.apple.com/documentation/uikit/uinavigationitem/1624958-backbarbuttonitem) 属性中有一个有效条目，导航栏就显示该条目。
- 如果这两个 View Controller 都没有指定 bar button item，就使用默认的返回按钮，其标题设为前一个 View Controller（也就是导航栈上下一级的那个 View Controller）的 title 属性值。（如果最顶层的 View Controller 本身就是根 View Controller，则不显示默认的返回按钮。）

对于最顶层的 View Controller，显示在导航栏中间的条目按以下规则确定：

- 如果你为最顶层 View Controller 的导航项的 [titleView](https://developer.apple.com/documentation/uikit/uinavigationitem/1624935-titleview) 属性指定了自定义视图，导航栏就显示该视图。
- 如果没有设置自定义标题视图，导航栏会显示一个包含 View Controller 标题的自定义视图。该视图所用的字符串取自 View Controller 导航项的 [title](https://developer.apple.com/documentation/uikit/uinavigationitem/1624965-title) 属性；如果该属性的值为 `nil`，则使用 View Controller 自身 [title](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621364-title) 属性中的字符串。

对于最顶层的 View Controller，显示在导航栏右侧的条目按以下规则确定：

- 如果新的顶层 View Controller 有自定义的右侧 bar button item，就显示该条目。要指定自定义的右侧 bar button item，请设置导航项的 [rightBarButtonItem](https://developer.apple.com/documentation/uikit/uinavigationitem/1624957-rightbarbuttonitem) 属性。
- 如果没有指定自定义的右侧 bar button item，导航栏在右侧不显示任何内容。

要在导航栏控件上方添加自定义提示文字，请为导航项的 [prompt](https://developer.apple.com/documentation/uikit/uinavigationitem/1624930-prompt) 属性赋值。

图 1-9 展示了各种导航栏配置，其中有几个使用了自定义视图和提示文字。图中的这些导航栏来自示例项目 _[NavBar：定制 UINavigationBar 的外观](../../../samplecode/NavBar-%20Customizing%20UINavigationBar%27s%20appearance/NavBar-%20Customizing%20UINavigationBar%27s%20appearance.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydonbrha)_.

__图 1-9__  导航栏中的自定义按钮

!

清单 1-2 展示了 NavBar app 中创建图 1-9 里第三个导航栏所需的代码，也就是右侧 bar button item 带有自定义视图的那个导航栏。因为它位于导航栏的右侧位置，所以在把自定义视图赋给 `rightBarButtonItem` 属性之前，必须先用一个 [UIBarButtonItem](https://developer.apple.com/documentation/uikit/uibarbuttonitem) 对象把它包装起来。

__清单 1-2__  创建自定义 bar button item

```objc
// 视图 3 —— 带自定义视图的右侧 bar button
UISegmentedControl *segmentedControl = [[UISegmentedControl alloc] initWithItems:
                                      [NSArray arrayWithObjects:
                                          [UIImage imageNamed:@"up.png"],
                                          [UIImage imageNamed:@"down.png"],
                                          nil]];

[segmentedControl addTarget:self action:@selector(segmentAction:) forControlEvents:UIControlEventValueChanged];
segmentedControl.frame = CGRectMake(0, 0, 90, kCustomButtonHeight);
segmentedControl.segmentedControlStyle = UISegmentedControlStyleBar;
segmentedControl.momentary = YES;

defaultTintColor = segmentedControl.tintColor;    // 如果之后还需要用到它，记得保存下来。
UIBarButtonItem *segmentBarItem = [[UIBarButtonItem alloc] initWithCustomView:segmentedControl];
self.navigationItem.rightBarButtonItem = segmentBarItem;
```

对大多数 app 来说，以编程方式配置 View Controller 的导航项是最常见的做法。虽然你也可以用 Interface Builder 创建 bar button item，但以编程方式创建往往简单得多。你应当在 View Controller 的 [viewDidLoad](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621495-viewdidload) 方法中创建这些条目。

支持就地编辑的视图可以在导航栏中放置一种特殊按钮，让用户在显示模式和编辑模式之间来回切换。`UIViewController` 的 [editButtonItem](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621471-editbuttonitem) 方法返回一个预先配置好的按钮，按下它时会在 Edit 和 Done 之间切换，并以相应的参数调用 View Controller 的 [setEditing:animated:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621378-setediting) 方法。要把这个按钮添加到 View Controller 的导航栏中，可以使用类似下面的代码：

```objc
myViewController.navigationItem.rightBarButtonItem = [myViewController editButtonItem];
```

如果你在导航栏中加入了这个按钮，还必须重写 View Controller 的 `setEditing:animated:` 方法，并在其中调整你的视图层级。关于实现该方法的更多信息，请参阅 _[iOS View Controller 编程指南](https://developer.apple.com/library/archive/featuredarticles/ViewControllerPGforiPhoneOS/index.html#//apple_ref/doc/uid/TP40007457)_ 中的“创建自定义内容 View Controller”。

在 iOS 3.0 及以后的版本中，导航界面可以显示一个工具栏，并用当前可见的 View Controller 所提供的条目填充它。工具栏本身由 navigation controller 对象管理。在这一层级支持工具栏，是实现屏幕之间平滑过渡所必需的。当导航栈上最顶层的 View Controller 发生变化时，navigation controller 会为不同工具栏条目集合之间的切换添加动画；当你想切换某个特定 View Controller 的工具栏可见性时，它同样能生成平滑的动画。

要为导航界面配置工具栏，你必须完成以下工作：

- 把 navigation controller 对象的 [toolbarHidden](https://developer.apple.com/documentation/uikit/uinavigationcontroller/1621875-toolbarhidden) [属性](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/DeclaredProperty.html#//apple_ref/doc/uid/TP40008195-CH13)设为 `NO`，以显示工具栏。
- 为每个内容 View Controller 的 [toolbarItems](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621867-toolbaritems) 属性指定一个 `UIBarButtonItem` 对象数组，具体做法参见[指定工具栏条目](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgmjtfvbuqmrnknltenq)。

  如果你不想为某个特定的内容 View Controller 显示工具栏，可以按[显示与隐藏工具栏](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgmjtfvbuqmrnknlteni)中的说明把工具栏隐藏起来。

图 1-10 举例说明了你与内容 View Controller 关联的对象如何反映到工具栏上。条目在工具栏中的显示顺序与它们在数组中的顺序一致。数组中可以包含各种类型的 bar button item，包括固定间距条目和弹性间距条目、系统按钮条目，以及你提供的任何自定义按钮条目。在这个例子中，五个条目全都是“邮件”app 中的按钮条目。

__图 1-10__  导航界面中的工具栏条目

!

配置 bar button item 时，记得为按钮关联合适的目标和动作。你正是依靠这些目标-动作信息来响应工具栏中的点按操作。大多数情况下，目标应当是 View Controller 自身，因为正是它负责提供这些工具栏条目。图 1-11 展示了一个带有居中分段控件的工具栏示例。

要使用 storyboard 指定工具栏条目：

1. 从库中拖出一个工具栏。
2. 从库中拖出两个弹性间距 bar button item，添加到工具栏中。
3. 从库中拖出一个分段控件，添加到两个弹性间距 bar button 之间。

   使用检查器配置这个分段控件。

__图 1-11__  工具栏中居中的分段控件

!

清单 1-3 展示了以编程方式指定工具栏条目所需的代码。你应当在自己的 View Controller 中实现这个方法，并在[初始化](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Initialization.html#//apple_ref/doc/uid/TP40008195-CH21)时调用它。

__清单 1-3__  配置带有居中分段控件的工具栏

```objc
- (void)configureToolbarItems
{
   UIBarButtonItem *flexibleSpaceButtonItem = [[UIBarButtonItem alloc]
                        initWithBarButtonSystemItem:UIBarButtonSystemItemFlexibleSpace
                        target:nil action:nil];

   // 创建并配置分段控件
   UISegmentedControl *sortToggle = [[UISegmentedControl alloc]
                        initWithItems:[NSArray arrayWithObjects:@"Ascending",
                                        @"Descending", nil]];
   sortToggle.segmentedControlStyle = UISegmentedControlStyleBar;
   sortToggle.selectedSegmentIndex = 0;
   [sortToggle addTarget:self action:@selector(toggleSorting:)
               forControlEvents:UIControlEventValueChanged];

   // 为分段控件创建 bar button item
   UIBarButtonItem *sortToggleButtonItem = [[UIBarButtonItem alloc]
                                    initWithCustomView:sortToggle];

   // 设置我们的工具栏条目
   self.toolbarItems = [NSArray arrayWithObjects:
                         flexibleSpaceButtonItem,
                         sortToggleButtonItem,
                         flexibleSpaceButtonItem,
                         nil];
}
```

除了在初始化时设置工具栏条目之外，View Controller 还可以使用 [setToolbarItems:animated:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621874-settoolbaritems) 方法动态更改现有的工具栏条目集合。当你想更新工具栏中的命令以反映其他某种用户操作时，这个方法很有用。例如，你可以用它实现一组层级式的工具栏条目：点按工具栏上的某个按钮，就显示一组与之相关的子按钮。

要为某个特定的 View Controller 隐藏工具栏，请把该 View Controller 的 [hidesBottomBarWhenPushed](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621863-hidesbottombarwhenpushed) 属性设为 `YES`。当 navigation controller 遇到该属性为 `YES` 的 View Controller 时，只要这个 View Controller 被压入导航栈（或从中移除），它就会生成相应的过渡动画。

如果你只想在某些时候（而不是始终）隐藏工具栏，可以随时调用 navigation controller 的 [setToolbarHidden:animated:](https://developer.apple.com/documentation/uikit/uinavigationcontroller/1621888-settoolbarhidden) 方法。这个方法的一种常见用法是与 `setNavigationBarHidden:animated:` 的调用结合，创建临时的全屏视图。例如，“照片”app 在显示单张照片且用户点按屏幕时，就会同时切换这两个栏的可见性。

[下一页](Tab%20Bar%20Controllers.md)[上一页](About%20View%20Controllers.md)

