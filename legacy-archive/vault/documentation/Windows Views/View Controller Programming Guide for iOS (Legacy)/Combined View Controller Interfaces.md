---
title: iOS View Controller 编程指南（旧版）
apple_id: TP40011381
resource_type: Guide
platform: iOS
topic: User Experience
technology: UIKit
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/WindowsViews/Conceptual/ViewControllerPGforiOSLegacy/CombiningViewControllers/CombiningViewControllers.html
archived_at: '2026-07-18T02:23:48.890572Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [iOS View Controller 编程指南（旧版）](About%20View%20Controllers.md)


[下一页](Document%20Revision%20History.md)[上一页](Modal%20View%20Controllers.md)

# 组合 View Controller 界面

UIKit 框架仅提供了少数几种标准 View Controller，用来实现你的应用界面：

- 自定义 View Controller（或 table view controller）提供一组自成一体的视图来呈现。
- navigation controller 以层级方式呈现多个 View Controller。
- tab bar controller 把多个 View Controller 呈现为应用的不同操作模式。
- split view controller 在横屏方向下并排呈现两个 View Controller。（在竖屏方向下，其中一个 View Controller 会显示在 popover 中。）

你可以单独使用这些 View Controller，也可以将它们与其他 View Controller 结合使用，以创建更复杂的界面。不过，在组合 View Controller 时，前面列表中各项的顺序是有讲究的。一般规则是：每种 View Controller 都可以包含列表中排在它前面的那些 View Controller。因此，navigation controller 可以包含自定义 View Controller，而 tab bar controller 既可以包含 navigation controller，也可以包含自定义 View Controller。但是，navigation controller 不应该把 tab bar controller 作为其 navigation 界面的一部分来包含。这样得到的界面会让用户感到困惑，因为标签栏不会一直保持可见。

由于模态 View Controller 本身就代表某种打断，因此它们遵循略有不同的规则。你几乎可以在任何时候以模态方式呈现任意 View Controller。从自定义 View Controller 以模态方式呈现 tab bar controller 或 navigation controller，造成的困惑要小得多。新的界面样式会取代其父级的样式，不过这只是暂时的。

以下各节将展示如何在你的 iOS 应用中组合 table view、navigation controller 和 tab bar controller。有关在 iPad 应用中使用 split view controller 的更多信息，参见[iPad 专属控制器](iPad-Specific%20Controllers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqnrnknltc)。

使用 tab bar controller 的应用，也可以在一个或多个标签页中使用 navigation controller。在同一个用户界面中组合这两种 View Controller 时，tab bar controller 始终充当 navigation controller 的外层容器。你绝不应该把 tab bar controller 压入 navigation controller 的导航栈中。这样做会造成一种反常的情况：标签栏只有在某个特定 View Controller 位于导航栈顶部时才会出现。标签栏的设计初衷是持续存在的，因此这种临时性的做法会让用户感到困惑。

使用 tab bar controller 最常见的方式，是把它的视图嵌入到应用的主窗口中。因此，以下各节将展示如何配置应用的主窗口，以包含一个 tab bar controller 和一个或多个 navigation controller。文中同时给出了以编程方式和使用 Interface Builder 实现的示例。如果你需要以模态方式呈现 tab bar controller，通常建议以编程方式创建相关对象。

在 nib 文件中组合 tab bar controller 和 navigation controller 的过程相对直接。真正的区别只在于你如何建立 tab bar controller 与 navigation controller 之间的关系。单独使用这些对象时，每一个都会承担应用窗口根视图的角色。而组合使用时，只有 tab bar controller 承担这个角色。navigation controller 不再为窗口提供根视图，而是充当标签栏界面中某个标签页的根视图。

图 7-1 展示了你需要在 [nib 文件](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/NibFile.html#//apple_ref/doc/uid/TP40008195-CH34)中创建的对象配置。在这个示例中，标签栏界面的前三个标签页使用自定义 View Controller，而最后一个标签页使用 navigation controller。随后又添加了一个额外的 View Controller，作为该 navigation controller 的根 View Controller。为了更好地管理内存，每个自定义 View Controller（包括 navigation controller 的根 View Controller）都把各自对应的视图存储在不同的 nib 文件中。

__图 7-1__  在 nib 文件中混合使用 navigation controller 和 tab bar controller

!

假设你是从一个通用的主 nib 文件（不包含 tab bar controller 的那种）开始，可以按照以下步骤在 Interface Builder 中创建[图 7-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgqwvgvzx)中的对象：

1. 从库中把一个 tab bar controller 对象拖到你的 Interface Builder 文档窗口中。

   当你把一个 tab bar controller 添加到 nib 文件中时，Interface Builder 还会添加一个标签栏视图、两个根 View Controller，以及两个标签栏项（每个 View Controller 对应一个）。
2. 使用 outlet 保存对 tab bar controller 的引用。

   为了在运行时访问 tab bar controller，你要么需要使用 outlet，要么必须在加载 nib 文件时显式获取该 nib 文件的顶层对象。使用 outlet 通常要简单得多。要为 tab bar controller 和 window 都添加 outlet，你需要在应用委托的头文件中加入类似下面的代码：

```objc
@interface MyAppDelegate : NSObject <UIApplicationDelegate> {
   UITabBarController*  tabBarController;
   UIWindow *window;
}
@property (nonatomic, retain) IBOutlet UIWindow *window;
@property (nonatomic, retain) IBOutlet UITabBarController *tabBarController;
@end
```

   添加好 outlet 定义之后，从这个 outlet 创建一个到 tab bar controller 对象的连接。
3. 通过在应用委托类的实现文件中添加以下代码，来合成上一步中的属性：

```objc
@synthesize window;
@synthesize tabBarController;
```
4. 向 tab bar controller 中添加一个 View Controller 对象和一个 Navigation Controller 对象。

   嵌入在 tab bar controller 对象中的 View Controller 数量，决定了标签栏界面所显示的标签页数量。由于最初的 tab bar controller 已经带有两个通用的 View Controller，你需要再添加一个 View Controller 对象（`UIViewController`）和一个 Navigation Controller 对象（`UINavigationController`）。

   要添加一个 View Controller，可以执行以下操作之一：

   - 从库中把合适的对象拖到编辑界面中的标签栏上。
   - 从库中把对象拖到 Interface Builder 文档窗口中的 tab bar controller 上。此时窗口必须处于大纲模式。

   在添加 navigation controller 时，你应该从库中拖入相应的对象，或者选中 tab bar controller 对象并使用 Attributes 检查器配置 View Controller 的类型。这两种方式都会把正确类型的 View Controller 对象添加到你的 nib 文件中。你永远不应该通过把一个通用的 View Controller 对象拖入 nib 文件、再把它的类名改成所需的类类型，来添加 navigation controller。

   要删除一个 View Controller，请在编辑界面或文档窗口中选中该 View Controller 对象，然后按 Delete 键。
5. 按照你希望它们在标签栏界面中出现的顺序排列这些 View Controller。

   你可以通过拖动 tab bar controller 编辑界面上显示的标签页，或者在 Interface Builder 文档窗口（仅限大纲模式）中拖动这些 View Controller，来重新排列它们（以及对应的标签页）。虽然编辑界面会显示所有标签页，但运行时只会显示五个。如果你的 tab bar controller 包含六个或更多 View Controller，最初标签栏中只会显示前四个。标签栏上的最后一个位置留给 More view controller，用来呈现其余的 View Controller。
6. 配置这些 View Controller。

   对于每个根 View Controller，你应当配置以下属性：

   - 使用 Identity 检查器设置每个自定义 View Controller 对象的类。对于通用的 View Controller 对象，把类名改成你想用来显示该标签页内容的自定义子类。不要更改 Navigation Controller 对象本身的类，但要设置该 navigation controller 中嵌入的自定义 View Controller 的类。
   - 为每个自定义 View Controller 提供一个视图。首选的做法是把每个自定义 View Controller 的 NIB Name 属性配置为包含该视图的 nib 文件名。虽然你也可以把每个视图和 View Controller 放在同一个 nib 文件中，但不建议这样做。有关如何为自定义 View Controller 配置 nib 文件的信息，参见[将视图存储在独立的 Nib 文件中](Custom%20View%20Controllers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgewvgvztgm)。
   - 根据需要，为任意 View Controller 配置样式或外观信息。
7. 为每个 View Controller 配置标签栏项。

   你可以从 tab bar controller 编辑界面，或者处于大纲模式或浏览器模式下的 Interface Builder 文档窗口中选中标签栏项。使用 Interface Builder，你可以指定标签栏项的标题、图片和徽章。或者，你也可以通过在 Attributes 检查器中为 Identifier 属性赋值，把标签栏项设置为某个标准系统标签页。
8. 保存你的 nib 文件。

虽然前面的步骤配置好了标签栏界面，但它们并没有把它安装到应用的主窗口中。要做到这一点，你需要在应用[委托](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14)的 [applicationDidFinishLaunching:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623053-applicationdidfinishlaunching) 方法中添加一些代码，如清单 7-1 所示。这里正是你在应用委托中使用为 tab bar controller 创建的那个 outlet 的地方。

__清单 7-1__  在应用的窗口中安装组合界面

```objc
- (void)applicationDidFinishLaunching:(UIApplication *)application {
    [window addSubview:tabBarController.view];
}
```


如果你为应用的主窗口以编程方式创建一个组合了标签栏和 navigation 的界面，最合适的地方是在应用[委托](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14)的 [applicationDidFinishLaunching:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623053-applicationdidfinishlaunching) 方法中。以下步骤说明了如何创建一个组合界面，其中三个标签页包含自定义 View Controller，一个标签页包含 navigation controller：

1. [创建](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectCreation.html#//apple_ref/doc/uid/TP40008195-CH39) [UITabBarController](https://developer.apple.com/documentation/uikit/uitabbarcontroller) 对象。
2. 创建三个自定义根 View Controller 对象，每个标签页一个。
3. 再创建一个自定义 View Controller，作为你 navigation 界面的根 View Controller。
4. 创建 [UINavigationController](https://developer.apple.com/documentation/uikit/uinavigationcontroller) 对象，并用其根 View Controller 对其进行初始化。
5. 把这个 navigation controller 和三个自定义 View Controller 添加到 tab bar controller 的 [viewControllers](https://developer.apple.com/documentation/uikit/uitabbarcontroller/1621185-viewcontrollers) 属性中。
6. 把 tab bar controller 的视图添加到应用的主窗口中。

清单 4-1 展示了创建并安装三个自定义 View Controller 和一个 navigation controller、将它们作为标签栏界面中标签页所需的模板代码。这些自定义 View Controller 的类名只是占位符，代表你自己提供的类。每个自定义 View Controller 的 `init` 方法也是一个你需要自行提供的方法，用来[初始化](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Initialization.html#//apple_ref/doc/uid/TP40008195-CH21)这些 View Controller。`tabBarController` 和 `window` 变量是该类的[声明属性](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/DeclaredProperty.html#//apple_ref/doc/uid/TP40008195-CH13)，用来保留它们的值。

__清单 7-2__  从零开始创建 tab bar controller

```objc
- (void)applicationDidFinishLaunching:(UIApplication *)application {
   self.tabBarController = [[[UITabBarController alloc] init] autorelease];

   MyViewController1* vc1 = [[[MyViewController1 alloc] init] autorelease];
   MyViewController2* vc2 = [[[MyViewController2 alloc] init] autorelease];
   MyViewController3* vc3 = [[[MyViewController3 alloc] init] autorelease];
   MyNavRootViewController* vc4 = [[[MyNavRootViewController alloc] init] autorelease];
   UINavigationController* navController = [[[UINavigationController alloc]
                           initWithRootViewController:vc4] autorelease];

   NSArray* controllers = [NSArray arrayWithObjects:vc1, vc2, vc3, navController, nil];
   tabBarController.viewControllers = controllers;

   // 把 tab bar controller 当前的视图添加为窗口的子视图
   window = [[[UIWindow alloc] initWithFrame:[[UIScreen mainScreen] bounds]] autorelease];
   [window addSubview:tabBarController.view];
}
```

即便你以编程方式创建自定义 View Controller，也不会对如何为每一个创建视图有任何限制。无论一个 View Controller 是以何种方式创建的，它的视图管理周期都是相同的，因此你既可以按照[为你的 View Controller 创建视图](Custom%20View%20Controllers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgewvgvzs)中所述以编程方式创建视图，也可以使用 Interface Builder 来创建。

从应用中以模态方式呈现 navigation controller 完全合理（而且相当常见）。实际上，许多标准系统 View Controller（包括 [UIImagePickerController](https://developer.apple.com/documentation/uikit/uiimagepickercontroller) 和 [ABPeoplePickerNavigationController](https://developer.apple.com/documentation/addressbookui/abpeoplepickernavigationcontroller)）本身就是专门设计为以模态方式呈现的 navigation controller。

当你想以模态方式呈现自己的自定义 navigation 界面时，应始终把这个 navigation controller 对象作为第一个参数传给 [presentModalViewController:animated:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621465-presentmodalviewcontroller) 方法。在呈现之前，你必须始终对该 View Controller 进行适当的配置。至少，你的 navigation controller 应该有一个根 View Controller。而且，如果你想让用户从导航层级中的某个不同位置开始，就必须在呈现该 navigation controller 之前，把那些 View Controller（不带动画地）添加到导航栈中。

清单 7-3 展示了如何创建并配置一个 navigation controller、然后以模态方式显示它的示例。在这个示例中，被压入导航栈的 View Controller 是需要你自行定义并配置好视图的自定义对象。`currentViewController` 对象则是对当前可见 View Controller 的引用，同样需要你自行提供。

__清单 7-3__  以模态方式显示 navigation controller

```objc
MyViewController1*  rootVC = [[MyViewController1 alloc] init];
MyViewController2*  nextVC = [[MyViewController2 alloc] init];

// 创建 nav controller 并添加 View Controller。
UINavigationController*  theNavController = [[UINavigationController alloc]
                          initWithRootViewController:rootVC];
[theNavController pushViewController:nextVC animated:NO];

// 以模态方式显示 nav controller。
[currentViewController presentModalViewController:theNavController animated:YES];

// 释放这些 View Controller，防止过度保留。
[rootVC release];
[nextVC release];
[theNavController release];
```

与所有其他以模态方式呈现的 View Controller 一样，父 View Controller 负责在用户执行相应操作时，消除其以模态方式呈现的子 View Controller。不过在消除一个 navigation controller 时，请记住，这样做不仅会移除该 navigation controller 对象本身，还会移除其导航栈中当前所有的 View Controller。不可见的那些 View Controller 只会被简单地释放，但导航栈最顶部的 View Controller 还会收到常规的 [viewWillDisappear:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621485-viewwilldisappear) 消息。

有关如何以模态方式呈现 View Controller（包括 navigation controller）的信息，参见[以模态方式呈现 View Controller](Modal%20View%20Controllers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjrgewvgvzt)。有关如何为你的应用配置 navigation controller 的更多信息，参见[创建 navigation 界面](Navigation%20Controllers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgmwvgvzsg4)。

在你的应用中以模态方式呈现 tab bar controller 是可行的（尽管并不常见）。标签栏界面通常安装在应用的主窗口中，并只在需要时进行更新。不过，如果你界面的设计确实有此需要，你也可以以模态方式呈现 tab bar controller。例如，为了从应用的主要操作模式切换到使用标签栏界面的完全不同的模式，你可以使用交叉淡化过渡效果，以模态方式呈现次级 tab bar controller。

以模态方式呈现 tab bar controller 时，你应始终把这个 tab bar controller 对象作为第一个参数传给 [presentModalViewController:animated:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621465-presentmodalviewcontroller) 方法。在呈现该 tab bar controller 之前，必须先对其进行配置。这意味着你必须创建根 View Controller、对它们进行配置，并把它们添加到 tab bar controller 中，就像你在主窗口中安装标签栏界面时那样。

与所有其他以模态方式呈现的 View Controller 一样，父 View Controller 负责在用户执行相应操作时，消除其以模态方式呈现的子 View Controller。不过在消除一个 tab bar controller 时，请记住，这样做不仅会移除该 tab bar controller 对象本身，还会移除与每个标签页关联的 View Controller。不可见的那些 View Controller 只会被简单地释放，但当前可见标签页中显示的 View Controller 还会收到常规的 [viewWillDisappear:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621485-viewwilldisappear) 消息。

有关如何以模态方式呈现 View Controller（包括 navigation controller）的信息，参见[以模态方式呈现 View Controller](Modal%20View%20Controllers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjrgewvgvzt)。有关如何以编程方式配置 tab bar controller 的信息，参见[以编程方式创建标签栏界面](Tab%20Bar%20Controllers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgiwvgvzrgu)。

把 table view 与 navigation controller 组合起来创建 navigation 界面是非常常见的做法。由于 navigation controller 便于对数据层级进行导航，表格经常被用来让用户选择接下来要导航到哪里。点按某个表格中的一行，会把用户带到显示该行关联数据的新界面。例如，在 iPod 应用中选择某个播放列表，会把用户带到该播放列表中的歌曲列表。

在管理表格方面，一种方式是使用 [UITableViewController](https://developer.apple.com/documentation/uikit/uitableviewcontroller) 对象。虽然这个类让表格数据的管理容易了许多，但你仍然需要实现自定义代码来实现导航。具体来说，当用户点按表格中的一行时，你需要把一个合适的新 View Controller 对象压入导航栈中。

清单 7-4 展示了如何在 navigation 界面中导航到下一层数据的示例。每当用户点按当前表格中的某一特定行时，你需要使用与该行关联的信息来初始化一个新的 View Controller，然后把它压入导航栈中。`initWithTable:andDataAtIndexPath:` 方法是一个你必须自行实现的自定义方法；它的职责是获取该行的数据对象，并用它来初始化下一层的 View Controller。

__清单 7-4__  使用 table view 导航数据

```objc
// 在你的 UITableViewController 子类中，
// 或者在你用来管理表格的委托对象中，实现类似下面这样的代码。
- (void)tableView:(UITableView *)tableView didSelectRowAtIndexPath:(NSIndexPath *)indexPath
{
   // 创建一个以该标题作为其
   // navigation 标题的 View Controller，并将其压入导航栈。
   NSUInteger row = indexPath.row;
   if (row != NSNotFound)
   {
      // 创建该 View Controller，并用
      // 下一层数据对其进行初始化。
      MyViewController *viewController = [[MyViewController alloc]
                   initWithTable:tableView andDataAtIndexPath:indexPath];
      [[self navigationController] pushViewController:viewController
                   animated:YES];
   }
}
```

有关管理表格和使用 table view controller 的更多详细信息，参见 _[Table View Programming Guide for iOS](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/TableView_iPhone/AboutTableViewsiPhone/AboutTableViewsiPhone.html#//apple_ref/doc/uid/TP40007451)_。

[下一页](Document%20Revision%20History.md)[上一页](Modal%20View%20Controllers.md)

