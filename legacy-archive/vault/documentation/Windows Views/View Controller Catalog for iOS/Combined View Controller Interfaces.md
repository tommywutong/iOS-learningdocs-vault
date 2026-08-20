---
title: iOS View Controller 一览
apple_id: TP40011313
resource_type: Guide
platform: tvOS|iOS
topic: User Experience
technology: UIKit
published: '2014-11-15'
source_url: https://developer.apple.com/library/archive/documentation/WindowsViews/Conceptual/ViewControllerCatalog/Chapters/CombiningViewControllers.html
archived_at: '2026-07-18T02:22:58.108219Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [iOS View Controller 一览](About%20View%20Controllers.md)


[下一页](Document%20Revision%20History.md)[上一页](Popovers.md)

# 组合式 View Controller 界面

UIKit 框架提供的 View Controller，既可以单独使用，也可以与其他 View Controller 配合使用，构建出更复杂的界面。不过在组合 View Controller 时，包含的顺序很重要，只有特定的排列方式才是有效的。从子到父的包含顺序如下：

- 内容 View Controller，以及边界可变的容器 View Controller（例如 page view controller）
- navigation view controller
- tab bar controller
- split view controller

模态 View Controller 代表的是一次中断，它们遵循的规则略有不同。你几乎可以在任何时候以模态方式呈现任何 View Controller。从自定义 View Controller 中模态呈现 tab bar controller 或 navigation controller，造成的困惑要小得多。

下面几节介绍如何在 iOS app 中把 table view、navigation controller 和 tab bar controller 组合起来。要进一步了解如何在 iPad app 中使用 split view controller，请参阅 [Split View Controller](Split%20View%20Controllers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgmjtfvbuqnznknltc)。要进一步了解 table view，请参阅 _[Table View Programming Guide for iOS](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/TableView_iPhone/AboutTableViewsiPhone/AboutTableViewsiPhone.html#//apple_ref/doc/uid/TP40007451)_。

使用 tab bar controller 的 app 也可以在一个或多个标签页中使用 navigation controller。当在同一个用户界面中组合这两类 View Controller 时，始终由 tab bar controller 充当 navigation controller 的外层容器。

tab bar controller 最常见的用法，是把它的视图嵌入 app 的主窗口。下面几节介绍如何配置 app 的主窗口，让它包含一个 tab bar controller 和一个或多个 navigation controller。文中同时给出了以编程方式和使用 Interface Builder 两种做法的示例。

标签栏视图不支持半透明效果，tab bar controller 也绝不会在其关联的标签栏下方显示内容。因此，如果你的导航界面嵌在 tab bar controller 的某个标签页里，并且按[为导航视图采用全屏布局](Navigation%20Controllers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgmjtfvbuqmrnknlts)中所述采用了全屏布局，那么你的内容可能会延伸到导航栏下方，但不会延伸到标签栏下方。

在标签栏界面中嵌入 navigation controller 时，应当只嵌入 [UINavigationController](https://developer.apple.com/documentation/uikit/uinavigationcontroller) 类的实例，而不要嵌入那些属于 `UINavigationController` 子类的系统 View Controller。虽然系统提供了一些用于选择联系人、挑选图像以及实现其他行为的定制 navigation controller，但这些 View Controller 一般都是为模态呈现而设计的。要了解某个具体 View Controller 的用法，请参阅该类的参考文档。

要创建这样一个组合界面——其中三个标签页包含自定义 View Controller，另一个标签页包含 navigation controller——请执行以下操作：

1. 创建三个自定义 View Controller（每个标签页一个）和一个 navigation controller。
2. 选中这三个自定义 View Controller 和那个 navigation controller（只选 navigation controller 场景，不要选它的根 View Controller）。
3. 选择 Editor > Embed In > Tab Bar Controller。
4. 在 Attributes 检查器中勾选 Is Initial View Controller 选项，把 tab bar controller 显示为第一个 View Controller（或者用其他方式在你的用户界面中呈现该 View Controller）。

如果你要以编程方式为 app 的主窗口创建标签栏与导航的组合界面，最合适的位置是应用程序[委托](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14)的 [applicationDidFinishLaunching:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623053-applicationdidfinishlaunching) 方法。下面的步骤说明了如何创建这样一个组合界面：其中三个标签页包含自定义 View Controller，另一个包含 navigation controller。

1. [创建](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectCreation.html#//apple_ref/doc/uid/TP40008195-CH39) [UITabBarController](https://developer.apple.com/documentation/uikit/uitabbarcontroller) 对象。
2. 创建三个自定义根 View Controller 对象，每个标签页一个。
3. 再创建一个自定义 View Controller，用作导航界面的根 View Controller。
4. 创建 [UINavigationController](https://developer.apple.com/documentation/uikit/uinavigationcontroller) 对象，并用它的根 View Controller 来初始化它。
5. 把这个 navigation controller 和三个自定义 View Controller 添加到 tab bar controller 的 [viewControllers](https://developer.apple.com/documentation/uikit/uitabbarcontroller/1621185-viewcontrollers) 属性中。

清单 6-1 给出了模板代码，用于创建三个自定义 View Controller 和一个 navigation controller，并把它们作为标签页装入标签栏界面。代码中自定义 View Controller 的类名只是占位符，实际的类由你自己提供。每个自定义 View Controller 的 `init` 方法同样需要由你提供，用来[初始化](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Initialization.html#//apple_ref/doc/uid/TP40008195-CH21)这些 View Controller。`tabBarController` 和 `window` 变量是应用程序委托类的[声明属性](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/DeclaredProperty.html#//apple_ref/doc/uid/TP40008195-CH13)，该类对这些对象保持强引用。

__清单 6-1__  以编程方式创建 tab bar controller

```objc
- (void)applicationDidFinishLaunching:(UIApplication *)application {
    self.tabBarController = [[UITabBarController alloc] init];

    MyViewController1* vc1 = [[MyViewController1 alloc] init];
    MyViewController2* vc2 = [[MyViewController2 alloc] init];
    MyViewController3* vc3 = [[MyViewController3 alloc] init];
    MyNavRootViewController* vc4 = [[MyNavRootViewController alloc] init];
    UINavigationController* navController = [[UINavigationController alloc]
                            initWithRootViewController:vc4];

    NSArray* controllers = [NSArray arrayWithObjects:vc1, vc2, vc3, navController, nil];
    tabBarController.viewControllers = controllers;

    window = [[UIWindow alloc] initWithFrame:[[UIScreen mainScreen] bounds]];
    window.rootViewController = tabBarController;
    [window makeKeyAndVisible];
}
```

即使你是以编程方式创建自定义 View Controller，对每个 View Controller 的视图如何创建也没有任何限制。无论 View Controller 以何种方式创建，其视图管理周期都是一样的，因此你既可以用代码创建视图，也可以按 _[View Controller Programming Guide for iOS](https://developer.apple.com/library/archive/featuredarticles/ViewControllerPGforiPhoneOS/index.html#//apple_ref/doc/uid/TP40007457)_ 中 Creating Custom Content View Controllers 所述使用 Interface Builder 创建视图。

在 app 中以模态方式呈现 navigation controller 是完全合理的做法（而且相当常见）。事实上，许多标准系统 View Controller（包括 [UIImagePickerController](https://developer.apple.com/documentation/uikit/uiimagepickercontroller) 和 [ABPeoplePickerNavigationController](https://developer.apple.com/documentation/addressbookui/abpeoplepickernavigationcontroller)）本身就是专为模态呈现而设计的 navigation controller。

当你想以模态方式呈现自己的自定义导航界面时，始终要把 navigation controller 对象作为第一个参数传给 [presentModalViewController:animated:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621465-presentmodalviewcontroller) 方法。呈现之前必须先把这个 View Controller 配置妥当：至少，你的 navigation controller 应当有一个根 View Controller。而如果你希望用户一开始就处于导航层级中的其他位置，就必须在呈现该 navigation controller 之前，把相应的 View Controller（不带动画地）添加到导航栈中。

清单 6-2 展示了如何创建并配置一个 navigation controller 并以模态方式显示它。在这个例子中，压入导航栈的 View Controller 都是自定义对象，需要你自己定义并为它们配置视图；而 `currentViewController` 对象是对当前可见 View Controller 的引用，同样需要由你提供。

__清单 6-2__  以模态方式显示 navigation controller

```objc
MyViewController1*  rootVC = [[MyViewController1 alloc] init];
MyViewController2*  nextVC = [[MyViewController2 alloc] init];
NSArray * viewControllers = [NSArray arrayWithObjects:rootVC, nextVC, nil];

// 创建 nav controller 并设置它的 View Controller。
UINavigationController*  theNavController = [[UINavigationController alloc]
                          initWithRootViewController:rootVC];
[theNavController setViewControllers:viewControllers animated:NO];

// 以模态方式显示 nav controller。
[currentViewController presentModalViewController:theNavController animated:YES];
```

与其他所有模态呈现的 View Controller 一样，呈现方 View Controller 负责在用户执行相应操作时消除它模态呈现的子 View Controller。不过要记住，消除一个 navigation controller 时，被移除的不只是 navigation controller 对象本身，还包括它导航栈上当前的那些 View Controller。其中不可见的 View Controller 只是被从导航栈中移除，而位于栈顶的那个 View Controller 还会照常收到 [viewWillDisappear:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621485-viewwilldisappear) 消息。

要了解如何以模态方式呈现 View Controller（包括 navigation controller），请参阅 _[View Controller Programming Guide for iOS](https://developer.apple.com/library/archive/featuredarticles/ViewControllerPGforiPhoneOS/index.html#//apple_ref/doc/uid/TP40007457)_ 中的 Presenting View Controllers from Other View Controllers。要进一步了解如何配置 navigation controller 以便在 app 中使用，请参阅 [Navigation Controller](Navigation%20Controllers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgmjtfvbuqmrnknltc)。

在 app 中以模态方式呈现 tab bar controller 是可行的（尽管并不常见）。标签栏界面通常安装在 app 的主窗口中，只在需要时更新。不过，如果界面设计确实有这样的需要，你也可以模态呈现 tab bar controller。例如，要从 app 的主操作模式切换到另一种完全不同的、使用标签栏界面的模式，你可以用交叉淡入淡出的转场，把第二个 tab bar controller 模态呈现出来。

以模态方式呈现 tab bar controller 时，始终要把 tab bar controller 对象作为第一个参数传给 [presentModalViewController:animated:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621465-presentmodalviewcontroller) 方法。在呈现之前，tab bar controller 必须已经配置完毕。因此，你必须先创建各个根 View Controller、把它们配置好，再添加到 tab bar controller 中，就像在主窗口中安装标签栏界面时那样。

与其他所有模态呈现的 View Controller 一样，父 View Controller 负责在用户执行相应操作时消除它模态呈现的子 View Controller。不过要记住，消除一个 tab bar controller 时，被移除的不只是 tab bar controller 对象本身，还包括与每个标签页关联的 View Controller。其中不可见的 View Controller 只是被直接移除，而当前可见标签页中显示的那个 View Controller 还会照常收到 [viewWillDisappear:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621485-viewwilldisappear) 消息。

要了解如何以模态方式呈现 View Controller（包括 navigation controller），请参阅 _[View Controller Programming Guide for iOS](https://developer.apple.com/library/archive/featuredarticles/ViewControllerPGforiPhoneOS/index.html#//apple_ref/doc/uid/TP40007457)_ 中的 Presenting View Controllers from Other View Controllers。要了解如何配置 tab bar controller 以便在 app 中使用，请参阅 [Tab Bar Controller](Tab%20Bar%20Controllers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgmjtfvbuqmznknltc)。

把 table view 与 navigation controller 组合起来构建导航界面，是非常常见的做法。由于 navigation controller 便于在数据层级中导航，表格常被用来让用户选择下一步要去往何处。点按表格中的某一行，会把用户带到显示该行相关数据的新屏幕。例如，在 iPod app 中选中一个播放列表，就会把用户带到该播放列表中的歌曲列表。

管理表格的方式之一，是使用 [UITableViewController](https://developer.apple.com/documentation/uikit/uitableviewcontroller) 对象。虽然这个类让表格数据的管理简单了很多，但你仍然需要编写自定义代码来实现导航。具体来说，当用户点按表格中的某一行时，你需要把一个合适的新 View Controller 对象压入导航栈。

清单 6-3 展示了如何在导航界面中前往下一层数据。每当用户点按当前表格中的某一行时，你就用与该行关联的信息初始化一个新的 View Controller，然后把它压入导航栈。`initWithTable:andDataAtIndexPath:` 是需要你自己实现的自定义方法，它的职责是取出该行对应的数据对象，并用它初始化下一层的 View Controller。

__清单 6-3__  使用 table view 浏览数据

```objc
// 在你的 UITableViewController 子类中，或者在你用来管理表格的
// 委托对象中，实现类似下面这样的代码。
- (void)tableView:(UITableView *)tableView didSelectRowAtIndexPath:(NSIndexPath *)indexPath
{
   // 创建一个 View Controller，用标题作为它的
   // 导航标题，然后把它压入栈中。
   NSUInteger row = indexPath.row;
   if (row != NSNotFound)
   {
      // 创建 View Controller，并用下一层的
      // 数据来初始化它。
      MyViewController *viewController = [[MyViewController alloc]
                   initWithTable:tableView andDataAtIndexPath:indexPath];
      [[self navigationController] pushViewController:viewController
                   animated:YES];
   }
}
```

要更详细地了解如何管理表格以及如何使用 table view controller，请参阅 _[Table View Programming Guide for iOS](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/TableView_iPhone/AboutTableViewsiPhone/AboutTableViewsiPhone.html#//apple_ref/doc/uid/TP40007451)_。

[下一页](Document%20Revision%20History.md)[上一页](Popovers.md)

