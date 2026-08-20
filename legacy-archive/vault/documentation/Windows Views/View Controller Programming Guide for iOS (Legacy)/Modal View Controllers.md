---
title: iOS View Controller 编程指南（旧版）
apple_id: TP40011381
resource_type: Guide
platform: iOS
topic: User Experience
technology: UIKit
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/WindowsViews/Conceptual/ViewControllerPGforiOSLegacy/ModalViewControllers/ModalViewControllers.html
archived_at: '2026-07-18T02:23:49.687417Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [iOS View Controller 编程指南（旧版）](About%20View%20Controllers.md)


[下一页](Combined%20View%20Controller%20Interfaces.md)[上一页](iPad-Specific%20Controllers.md)

# 模态 View Controller

模态 View Controller 提供了一些有趣的方式来管理应用的流程。应用最常见的做法是把模态 View Controller 当作一种临时的打断手段，用来从用户那里获取关键信息。不过，你也可以借助以模态方式呈现的 View Controller，在特定时刻为应用实现另一套界面。

本章介绍模态视图在应用中的用途，并说明何时以及如何呈现它们。

模态 View Controller 是你可以用来打断当前工作流程、显示一组新视图的工具。模态 View Controller 并不像 `UITabBarController` 或 `UINavigationController` 那样，是 [UIViewController](https://developer.apple.com/documentation/uikit/uiviewcontroller) 的某个特定子类。相反，应用可以把任何 View Controller 都以模态方式呈现。不过，与 tab bar controller 和 navigation controller 一样，当你想要表达先前视图层级与新呈现的视图层级之间某种特定关系时，就应当以模态方式呈现 View Controller。

在应用中使用模态 View Controller 有以下几个原因：

- 用它们来立即从用户那里获取信息。
- 用它们来临时呈现某些内容。
- 用它们来临时更改工作模式。
- 用它们为不同的设备方向实现不同的界面。
- 用它们以某种特定类型的动画过渡（或不使用过渡）呈现一个新的视图层级。

上述大多数原因，都是为了临时打断应用的工作流程，以获取或显示某些信息。一旦你获得了所需的信息（或者已经向用户呈现了适当的信息），就应当消除该模态 View Controller，让应用回到之前的状态。即使是最后一种情形（实现另一套界面），也应当被当作一次临时的打断来处理。

当你呈现一个模态 View Controller 时，系统会在发起呈现的 View Controller 与被呈现的 View Controller 之间建立起父子关系。具体来说，发起呈现的 View Controller 会更新其 [modalViewController](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621479-modalviewcontroller) 属性，使其指向被呈现的（子）View Controller。同样，被呈现的 View Controller 也会更新其 [parentViewController](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621362-parent) 属性，使其反过来指向呈现它的那个 View Controller。图 6-1 展示了 Calendar 应用中管理主屏幕的 View Controller，与用于创建新事件的模态 View Controller 之间的关系。

__图 6-1__  Calendar 应用中的模态视图。

!

任何一个 View Controller 对象都可以将任何其他单个 View Controller 以模态方式呈现。即使是那些自身就是被模态呈现的 View Controller，这一点同样成立。换句话说，你可以按需把多个模态 View Controller 串联起来，根据需要在其他模态 View Controller 之上再呈现新的模态 View Controller。图 6-2 以可视化的方式展示了这一串联过程，以及触发它的各个操作。在这个例子中，当用户轻点相机视图中的图标时，应用会呈现一个包含用户照片的模态 View Controller。轻点照片库工具栏中的操作按钮，会提示用户选择合适的操作，然后根据该操作呈现另一个模态 View Controller（联系人选择器）。选择一个联系人（或取消联系人选择器）会消除该界面，把用户带回照片库。随后轻点「完成」按钮，则会消除照片库，把用户带回相机界面。

__图 6-2__  创建一条模态 View Controller 链

!

在一条由多个模态呈现的 View Controller 组成的链中，每个 View Controller 都持有指向链中其周围对象的指针。换句话说，一个呈现了另一个模态 View Controller 的模态 View Controller，其 `parentViewController` 和 `modalViewController` 属性都持有有效的对象。你可以借助这些关系按需追溯整条 View Controller 链。例如，如果用户取消了当前操作，你就可以通过消除链中第一个被模态呈现的 View Controller，来移除链中的所有对象。换句话说，消除一个模态 View Controller，不仅会消除该 View Controller 本身，还会消除它以模态方式呈现的所有 View Controller。

在[图 6-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjrgewvgvzy)中，一个值得注意的点是，这两个被模态呈现的 View Controller 都是 navigation controller。你可以像呈现自定义 View Controller 一样，以模态方式呈现 [UINavigationController](https://developer.apple.com/documentation/uikit/uinavigationcontroller) 对象。（在极少数情况下，你甚至可以以模态方式呈现一个 tab bar controller。）

以模态方式呈现 navigation controller 时，你呈现的始终是 `UINavigationController` 对象本身，而不是其导航栈上的任何一个 View Controller。不过，导航栈上的各个 View Controller 自身仍然可以以模态方式呈现其他 View Controller，包括其他 navigation controller。图 6-3 更详细地展示了前述示例中涉及的各个对象。可以看到，联系人选择器并不是由照片库的 navigation controller 呈现的，而是由其导航栈上的某个自定义 View Controller 呈现的。

__图 6-3__  以模态方式呈现 navigation controller

!

对于 iPad 应用，你可以使用几种不同的样式以模态方式呈现内容。在 iPhone 应用中，以模态方式呈现的视图总是会覆盖窗口的整个可见部分；但在 iPad 上运行时，View Controller 会使用其 [modalPresentationStyle](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621355-modalpresentationstyle) [属性](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/DeclaredProperty.html#//apple_ref/doc/uid/TP40008195-CH13)中的值，来决定它以模态方式呈现时的外观。该属性的不同取值可以让你决定呈现的 View Controller 是填满整个屏幕，还是只占据屏幕的一部分。

图 6-4 展示了可用的几种核心呈现样式。（[UIModalPresentationCurrentContext](https://developer.apple.com/documentation/uikit/uimodalpresentationstyle/uimodalpresentationcurrentcontext) 样式让一个 View Controller 采用其父级的呈现样式。）在每种模态视图中，变暗的区域显示的是底层内容，但不允许对该内容进行轻点操作。因此，与 popover 不同的是，你的模态视图仍然必须提供[控件](https://developer.apple.com/library/archive/documentation/General/Conceptual/Devpedia-CocoaApp/Control.html#//apple_ref/doc/uid/TP40009071-CH7)，让用户能够消除该模态视图。

__图 6-4__  模态呈现样式

!

关于何时应当使用不同的呈现样式，请参阅 Popover (iPad Only)。

要以模态方式呈现一个 View Controller，你必须完成以下步骤：

1. [创建](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectCreation.html#//apple_ref/doc/uid/TP40008195-CH39)你想要呈现的 View Controller。
2. 把该 View Controller 的 [modalTransitionStyle](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621388-modaltransitionstyle) [属性](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/DeclaredProperty.html#//apple_ref/doc/uid/TP40008195-CH13)设置为所需的值。
3. 在合适的情况下指定一个[委托对象](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14)。（委托主要供系统 View Controller 使用，用于在该 View Controller 准备好被消除时通知你的代码。更多信息请参阅[呈现标准系统模态 View Controller](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjrgewvgvzu)。）
4. 调用当前 View Controller 的 [presentModalViewController:animated:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621465-presentmodalviewcontroller) 方法，并传入你想要以模态方式呈现的 View Controller。

`presentModalViewController:animated:` 方法会呈现指定 View Controller 对象的视图，并在该模态 View Controller 与当前 View Controller 之间建立父子关系。除非你是要把应用恢复到之前的某个状态，否则通常都希望为模态 View Controller 的出现添加动画效果。你应当使用的过渡样式取决于你打算如何使用被呈现的 View Controller。表 6-1 列出了你可以为被呈现 View Controller 的 [modalTransitionStyle](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621388-modaltransitionstyle) 属性所指定的过渡样式，以及每种样式的使用方式。

__表 6-1__  模态 View Controller 的过渡样式

| 过渡样式 | 用法 |
| --- | --- |
| [UIModalTransitionStyleCoverVertical](https://developer.apple.com/documentation/uikit/uimodaltransitionstyle/uimodaltransitionstylecoververtical) | 当你想打断当前工作流程，以从用户处收集信息时，使用此样式。你也可以用它来呈现用户可能会修改、也可能不会修改的内容。使用这种过渡样式时，自定义 View Controller 应当提供按钮，让用户明确地消除该 View Controller。通常，这会是一个「完成」按钮和一个可选的「取消」按钮。如果你没有显式设置过渡样式，系统默认会使用这种样式。 |
| [UIModalTransitionStyleFlipHorizontal](https://developer.apple.com/documentation/uikit/uimodaltransitionstyle/fliphorizontal) | 使用此样式来临时更改应用的工作模式。这种样式最常见的用途，是显示可能经常变化的设置，例如 Stocks 和 Weather 应用中的做法。这些设置可能针对整个应用，也可能只针对当前屏幕。使用这种过渡样式时，你通常会提供某种按钮，让用户返回应用的正常运行模式。 |
| [UIModalTransitionStyleCrossDissolve](https://developer.apple.com/documentation/uikit/uimodaltransitionstyle/crossdissolve) | 当设备改变方向时，使用此样式来呈现一套替代界面。在这种情况下，你的应用需要负责在收到方向变化通知时呈现和消除这套替代界面。基于媒体的应用也可以使用这种样式，以淡入方式显示展示媒体内容的屏幕。关于如何实现响应设备方向变化的替代界面的示例，请参阅[创建横屏替代界面](Custom%20View%20Controllers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjqgewvgvzsgy)。 |

清单 6-1 展示了一个来自自定义 recipes 应用的示例，演示了如何呈现一个模态控制器。当用户添加一份新食谱时，应用会以模态方式呈现一个 navigation controller，来提示用户输入该食谱的基本信息。之所以选择 navigation controller，是为了有一个放置「取消」和「完成」按钮的标准位置。使用 navigation controller 还能让将来扩展新食谱界面变得更容易——你只需在导航栈上压入新的 View Controller 即可。

__清单 6-1__  以模态方式呈现一个 View Controller

```objc
- (void)add:(id)sender {
   // 为 navigation controller 创建根 View Controller。
   // 这个新的 View Controller 会为导航栏配置
   // 一个「取消」按钮和一个「完成」按钮。
   RecipeAddViewController *addController = [[RecipeAddViewController alloc]
                       initWithNibName:@"RecipeAddView" bundle:nil];

   // 配置 RecipeAddViewController。在这个例子中，它会把任何更改
   // 报告给一个自定义的委托对象。
   addController.delegate = self;

   // 创建 navigation controller 并以模态方式呈现它。
   UINavigationController *navigationController = [[UINavigationController alloc]
                             initWithRootViewController:addController];
   [self presentModalViewController:navigationController animated:YES];

   // 此时 navigation controller 归当前 View Controller 所有，
   // 而根 View Controller 归 navigation controller 所有，
   // 因此应当释放这两个对象，以避免过度保留（over-retention）。
   [navigationController release];
   [addController release];
}
```

当用户在新食谱录入界面中轻点「完成」或「取消」按钮时，应用会消除该 View Controller，并把用户带回主视图。虽然你可以直接在这两个按钮各自关联的动作方法中调用 [dismissModalViewControllerAnimated:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621369-dismissmodalviewcontrolleranimat) 方法，但更稳妥的做法是使用一个委托对象，如[消除一个模态 View Controller](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjrgewvgvzrgq)中所述。

到了需要消除一个模态 View Controller 的时候，首选的做法是让父 View Controller 来负责消除它。换句话说，只要可能，呈现该模态 View Controller 的那个 View Controller，也应当负责消除它。虽然有几种技术可以通知父 View Controller 应当消除其以模态方式呈现的子 View Controller，但首选的技术是[委托机制](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14)。

在基于委托的模型中，被模态呈现的 View Controller 必须定义一个[协议](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Protocol.html#//apple_ref/doc/uid/TP40008195-CH45)，供其委托实现。该协议定义了一些方法，这些方法会在响应特定操作（例如轻点「完成」按钮）时被该模态 View Controller 调用。委托则负责实现这些方法，并提供恰当的响应。当父 View Controller 充当其模态子 View Controller 的委托时，其响应就应当包括在适当的时候消除该子 View Controller。

相比其他技术，使用委托机制来管理与模态 View Controller 的交互有以下几个关键优势：

- 委托对象有机会在该模态 View Controller 被消除之前，验证或整合来自它的更改。
- 使用委托能带来更好的封装性，因为该模态 View Controller 完全不需要知道呈现它的父对象的任何信息。这使你能够在应用的其他部分重用这个模态 View Controller。

为了说明委托协议的实现方式，我们来看一下在[以模态方式呈现一个 View Controller](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgobrfvbuqmjrgewvgvzt)中所用的食谱 View Controller 示例。在那个示例中，一个 recipes 应用在用户想要添加新食谱时，呈现了一个模态 View Controller。在呈现该模态 View Controller 之前，当前 View Controller 把自己设为 `RecipeAddViewController` 对象的委托。清单 6-2 展示了 `RecipeAddViewController` 对象的委托协议的定义。

__清单 6-2__  用于消除模态 View Controller 的委托协议

```objc
@protocol RecipeAddDelegate <NSObject>
// 取消时 recipe 为 nil
- (void)recipeAddViewController:(RecipeAddViewController *)recipeAddViewController
                   didAddRecipe:(MyRecipe *)recipe;
@end
```

当用户在新食谱界面中轻点「取消」或「完成」按钮时，`RecipeAddViewController` 对象会在其委托对象上调用上述方法。随后由该委托负责决定要采取的行动方案。

清单 6-3 展示了处理新增食谱的委托方法的实现。该方法由以模态方式呈现 `RecipeAddViewController` 对象的那个 View Controller 实现。如果用户接受了新食谱——即 recipe 对象不是 `nil`——该方法就会把这份食谱添加到自己的内部数据结构中，并通知其 table view 刷新自身。（该 table view 随后会从这里所示的同一个 `recipesController` 对象中重新加载食谱数据。）作为最后一步，该委托方法会消除这个模态 View Controller。

__清单 6-3__  使用委托消除一个模态 View Controller

```objc
- (void)recipeAddViewController:(RecipeAddViewController *)recipeAddViewController
                   didAddRecipe:(Recipe *)recipe {
   if (recipe) {
      // 把这份食谱添加到 recipes controller 中。
      int recipeCount = [recipesController countOfRecipes];
      UITableView *tableView = [self tableView];
      [recipesController insertObject:recipe inRecipesAtIndex:recipeCount];

      [tableView reloadData];
   }
   [self dismissModalViewControllerAnimated:YES];
}
```


在 iOS 中，有若干标准的系统 View Controller，它们的设计目的就是供应用以模态方式呈现。呈现这些 View Controller 的基本规则与呈现自定义 View Controller 相同。不过，由于应用无法访问由这些系统 View Controller 所管理的视图层级，你无法直接为视图中的控件实现动作方法。与系统 View Controller 的交互通常是通过一个[委托对象](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14)来进行的。

每个系统 View Controller 都定义了一个对应的[协议](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Protocol.html#//apple_ref/doc/uid/TP40008195-CH45)，你需要在你的委托对象中实现该协议的方法。每个委托通常都会实现一个方法，用来接受所选中的任意项目，或者取消该操作。你的委托对象应当随时准备好处理这两种情况。委托必须完成的最重要的事情之一，就是通过调用发起呈现的那个 View Controller（也就是该模态 View Controller 的父级）的 [dismissModalViewControllerAnimated:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621369-dismissmodalviewcontrolleranimat) 方法，来消除被呈现的 View Controller。

表 6-2 列出了 iOS 中若干标准系统 View Controller。关于这些类的更多信息，包括它们各自提供的功能，请参阅对应的类参考文档。

__表 6-2__  标准系统 View Controller

| 框架 | View Controller |
| --- | --- |
| Address Book UI | [ABNewPersonViewController](https://developer.apple.com/documentation/addressbookui/abnewpersonviewcontroller)  [ABPeoplePickerNavigationController](https://developer.apple.com/documentation/addressbookui/abpeoplepickernavigationcontroller)  [ABPersonViewController](https://developer.apple.com/documentation/addressbookui/abpersonviewcontroller)  [ABUnknownPersonViewController](https://developer.apple.com/documentation/addressbookui/abunknownpersonviewcontroller) |
| Event Kit UI | [EKEventViewController](https://developer.apple.com/documentation/eventkitui/ekeventviewcontroller)  [EKEventEditViewController](https://developer.apple.com/documentation/eventkitui/ekeventeditviewcontroller) |
| Game Kit | [GKPeerPickerController](https://developer.apple.com/documentation/gamekit/gkpeerpickercontroller)  [GKAchievementViewController](https://developer.apple.com/documentation/gamekit/gkachievementviewcontroller)  [GKMatchmakerViewController](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontroller)  [GKLeaderboardViewController](https://developer.apple.com/documentation/gamekit/gkleaderboardviewcontroller) |
| Message UI | [MFMailComposeViewController](https://developer.apple.com/documentation/messageui/mfmailcomposeviewcontroller)  [MFMessageComposeViewController](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller) |
| Media Player | [MPMediaPickerController](https://developer.apple.com/documentation/mediaplayer/mpmediapickercontroller)  [MPMoviePlayerViewController](https://developer.apple.com/documentation/mediaplayer/mpmovieplayerviewcontroller) |
| UIKit | [UIImagePickerController](https://developer.apple.com/documentation/uikit/uiimagepickercontroller)  [UIVideoEditorController](https://developer.apple.com/documentation/uikit/uivideoeditorcontroller) |

[下一页](Combined%20View%20Controller%20Interfaces.md)[上一页](iPad-Specific%20Controllers.md)

