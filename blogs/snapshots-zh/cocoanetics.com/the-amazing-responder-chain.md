---
title: 令人惊叹的响应者链
source_url: 'https://www.cocoanetics.com/2012/09/the-amazing-responder-chain/'
source_domain: cocoanetics.com
source_group: single-site
original_language: en
published: 2012-09-29
archived_at: 2026-07-27
content_hash: 'sha256:8b5caa2a96213412'
plan_ref: 第五周：RunLoop、AutoreleasePool、响应者链与生命周期 / Day 4｜事件先命中视图，再沿响应者链寻找处理者（对应 W4-07、W5-01）
plan_week: 第五周：RunLoop、AutoreleasePool、响应者链与生命周期
plan_day: Day 4｜事件先命中视图，再沿响应者链寻找处理者（对应 W4-07、W5-01）
container: '//div[@id=''content'']'
container_source: guess
translated: true
---

> 原文：[The Amazing Responder Chain](https://www.cocoanetics.com/2012/09/the-amazing-responder-chain/)

# 令人惊叹的响应者链

[Sep 29, 2012](https://www.cocoanetics.com/2012/09/the-amazing-responder-chain/)

还记得你第一次打开 Interface Builder 的时候吗？

[![](https://i0.wp.com/www.cocoanetics.com/files/Screen-Shot-2012-09-29-at-13.06.42.png?resize=397%2C71)](https://i0.wp.com/www.cocoanetics.com/files/Screen-Shot-2012-09-29-at-13.06.42.png)

你花了多长时间才理解 **File's Owner** 的用途？

它是加载这个 NIB 的对象的代理，通常是一个 `UIViewController`。这样一来，你就可以将 IBOutlet 和 IBAction 与 NIB 文件中包含的元素连接起来。Interface Builder 之所以了解这些，是因为你告诉了它 File's Owner 的类是什么，并通过解析这个类的头文件，找到了所有可以用 IBOutlet 和 IBAction 关键字连接的内容。

这个很简单。第二个问题：你花了多长时间才理解 **First Responder** 的用途？

如果你和我一样，最开始是为 iPhone 和其他 iOS 设备开发。那么你可能也学会了忽略这个代理对象，因为在 iOS 上它没有明显的用途。事实上，你可以在 iOS 应用开发中多年不使用它。我知道我就是这样。

直到我开始尝试为 Mac 开发时，才不得不开始理解和重视响应者链。所以最终我理解了“First Responder”对象的用途和好处，并想与你分享。

你可能听说过或阅读过关于响应者链（Responder Chain）的存在。通常最接近使用它的时候，是你想关闭 `UITextField` 的键盘，通过调用 `resignFirstResponder` 来实现。第二次常见的情况是，当你实现剪切/复制/粘贴时，需要让一个 `UIView` 能够成为第一响应者（first responder），然后实现 `cut:`、`copy:` 和 `paste:` 方法，让它们出现在 `UIMenuController` 的弹出窗口（popover）中。

### 为什么你之前没有使用它

在 iOS 上，你通常只需要处理一个充满信息的单个屏幕。这个屏幕，尤其是在 iPhone 上，通常包含在一个单独的 `UIViewController` 中。因此，你可以轻松地将所有动作连接到 File's Owner 中的 outlet。说真的，为什么会有人想让当前 NIB 之外的对象来响应像按钮点击或复制命令这样的操作呢？

嗯，在 Mac 上情况更复杂，因为你可以同时打开多个窗口。你可以同时处理 3 个文稿。但是这些窗口中，哪一个应该响应用户在菜单中选择“复制”呢？我花了大约一个小时才摆脱将菜单项连接到特定视图控制器的观念，并发现了那里不同的做法。

如果你将一个按钮连接到一个 outlet，这使用了目标/动作（target/action）范式。动作（action）由选择器（selector）的名称定义。目标（target）可以是具体对象，也可以是 `nil`。如果你连接到 File's Owner，那么目标就被设置为 File's Owner 所代理的具体实例。如果你在代码中这样做，你会调用 `addTarget:action:forControlEvents:`，实现完全相同的效果。

在 Mac 上，我们无法在 Interface Builder 的设计时说出谁会处理某个特定的动作。因此，我们需要使用响应者链的出色服务。

### 响应者链

你可以将响应者链视为回答“谁可能对这个事件 X 感兴趣？”这一问题的非常优雅的解决方案。

每当任何事件发生时，系统首先询问当前的 First Responder。在 iOS 上，任何 `UIResponder` 子类都可以成为第一响应者（first responder）。如果文本字段处于活动状态且光标在其内部闪烁以显示准备输入文本，那么它就拥有了第一响应者状态。因此，它优先获得所有事件。

然而，可能存在一些文本字段不知道如何响应的动作。对于这些情况，系统会沿着响应者链向上遍历，并持续询问链中的每个对象是否对处理此动作感兴趣。例如，考虑标准动作 **copy:**，默认情况下假设如果响应者的实现中存在这样的选择器，则响应者想要处理复制动作。这可以通过实现 **canPerformAction:withSender:** 并返回 NO 来覆盖。然后，下一个响应者将被询问。

对每个动作和整个链都会执行这种询问每个响应者的过程。如果系统想要显示菜单项（在 OS X 上）或弹出菜单（在 iOS 上），则会发生此过程的一个变体。如果没有响应者愿意处理，那么菜单选项将被禁用或隐藏。这非常有用，因为你不必实现启用/禁用菜单选项的逻辑，系统会为你完成。如果有响应者愿意处理某个动作，那么它将被启用，否则将被禁用。

让我们快速了解一下响应者链在 iOS 和 OS X 上的样子。

[![](https://i0.wp.com/www.cocoanetics.com/files/Screen-Shot-2012-09-29-at-14.55.58.png?resize=384%2C356)](https://i0.wp.com/www.cocoanetics.com/files/Screen-Shot-2012-09-29-at-14.55.58.png)

Apple [解释了](http://developer.apple.com/library/ios/#DOCUMENTATION/EventHandling/Conceptual/EventHandlingiPhoneOS/EventsiPhoneOS/EventsiPhoneOS.html) 沿着链传递的规则，如下所示：

1. **命中测试视图（hit-test view）或第一响应者** 将事件或消息传递给其**视图控制器（view controller）**（如果有的话）；如果视图没有视图控制器，则将事件或消息传递给其**父视图（superview）**。
2. 如果视图或其视图控制器无法处理事件或消息，则将其传递给视图的**父视图**。
3. 层级结构中的每个后续父视图，如果无法处理事件或消息，则遵循前两步中描述的模式。
4. 视图层级结构中的最顶层视图，如果它不处理事件或消息，则将其传递给**窗口（window）**对象进行处理。
5. `UIWindow` 对象，如果它不处理事件或消息，则将其传递给单例**应用程序（application）**对象。

从 iOS 5 开始，还有第 6 步：应用程序委托（app delegate）对事件有最终决定权。从 iOS 5 开始，**应用程序委托**继承自 `UIResponder`，不再像以前那样继承自 `NSObject`。

简而言之：首先是视图，如果视图有视图控制器，则接下来是视图控制器，然后是父视图，直到层级结构的顶部，即窗口。从那里到应用程序，最后到应用程序委托。

将应用程序委托添加为潜在响应者是一个受欢迎的补充，因为我们很少（如果不是从来没有）会子类化 `UIApplication` 或 `UIWindow`。但我们总是有_我们自己的应用程序委托_，即使只是为了在 `application:didFinishLaunching...` 委托方法中创建窗口和添加 `rootViewController`。因此，这恰好是整个视图层级结构中没有响应者时，响应者可以回退到的事实上的最佳位置。

看下面的对比，你可以看到这个概念在 iOS（左）和 Mac（右）上几乎是相同的。

[![](https://i0.wp.com/www.cocoanetics.com/files/iOS_and_OSX_responder_chain_2x.png?resize=633%2C371)](https://i0.wp.com/www.cocoanetics.com/files/iOS_and_OSX_responder_chain_2x.png)

这里唯一明显的区别是，视图控制器（view controller）在 OS X 上似乎是一个相对较新的概念。我推测这是因为视图控制器在 OS X 上的使用比在 iOS 上少得多。它们也从一个 NIB 加载视图。我见过 `NSViewController` 被用作文件打开对话框中的辅助视图（accessory view）的一种情况。

在 OS X 上，顶层控制对象通常是 `NSWindowController`，再次负责管理从 NIB 加载的窗口。在 iOS 上，视图控制器扮演着更重要的角色，因为像 `UITabBarController` 或 `UINavigationController` 这样的容器视图控制器（container view controller）会使用它们来分组视图。

长话短说，目前视图控制器不是 Mac 上响应者链的一部分，但它们是 iOS 上的一部分。

但是，如果你的 Mac 应用程序是基于文稿（document-based）的，故事并没有结束，因为那里响应者链被扩展，也包含多个与文稿相关的对象。

[![](https://i0.wp.com/www.cocoanetics.com/files/doc_based.jpg?resize=613%2C133)](https://i0.wp.com/www.cocoanetics.com/files/doc_based.jpg)

根据我目前在 Mac 上看到的，你可以在不子类化 `NSApplication`、`NSDocumentController` 甚至不提供应用程序委托的情况下走得很远。这个链中必须子类的元素是 `NSDocument`。

考虑一个 **import:** 动作，它允许用户将内容导入到打开的文稿中。如果没有文稿窗口打开，则该动作应显示为灰色。当然，`NSDocument` 子类是实现的理想位置，因为此功能与特定文稿相关。

### 在 Mac 上实现响应者链动作

正如我之前提到的，我一开始在尝试为 Mac 应用实现导入菜单项时感到困惑。那里有一个 `MainMenu.xib`，其 File's Owner 类是 `NSApplication`。所以 `NSApplication` 在应用启动时从 NIB 加载菜单。因此，将动作连接到 File's Owner 是没有意义的，因为你很可能甚至没有自定义的 `NSApplication` 子类。

相反，你点击 First Responder，然后转到带有盾牌图标的检查器标签。在那里，你可以看到所有用户定义的动作，我们添加一个导入动作。

[![](https://i0.wp.com/www.cocoanetics.com/files/Screen-Shot-2012-09-29-at-16.16.58.png?resize=630%2C339)](https://i0.wp.com/www.cocoanetics.com/files/Screen-Shot-2012-09-29-at-16.16.58.png)

现在，你可以按住 Ctrl 键点击并从新插入的菜单项拖出一条线到 First Responder。

[![](https://i0.wp.com/www.cocoanetics.com/files/Screen-Shot-2012-09-29-at-16.20.23.png?resize=524%2C353)](https://i0.wp.com/www.cocoanetics.com/files/Screen-Shot-2012-09-29-at-16.20.23.png)

在随后出现的弹出窗口中，你可以选择要连接到的动作。除了刚定义的 `import`，你还可以看到所有系统定义的动作。

[![](https://i0.wp.com/www.cocoanetics.com/files/Screen-Shot-2012-09-29-at-16.20.30.png?resize=254%2C255)](https://i0.wp.com/www.cocoanetics.com/files/Screen-Shot-2012-09-29-at-16.20.30.png)

……当然，另一个方向的连接也同样有效。在 outlets 标签中，`import` 选择器也会出现。你也可以从其圆形 outlet 符号拖到菜单项。

接下来，你在文稿类中实现一个匹配的动作方法。

```
- (void)import:(id)sender
{
   // fancy importing action
}
```

这里不需要使用 `IBAction` 关键字来替代 `void`。与通过 File's Owner 的路线相比，我们不需要这个提示来告诉 Interface Builder 在头文件中哪些动作可用于链接。

仅此而已。如果你有一个文稿窗口打开，响应者链知道有某个对象能够处理 `import`，因此菜单选项变为可用。相反，如果你关闭所有文稿窗口，它会自动变为灰色。

“出色的服务！”这就是我们所说的。最好的代码永远是我们_不必编写_的代码。

[![](https://i0.wp.com/www.cocoanetics.com/files/Screen-Shot-2012-09-29-at-16.30.18.png?resize=182%2C282)](https://i0.wp.com/www.cocoanetics.com/files/Screen-Shot-2012-09-29-at-16.30.18.png)[![](https://i0.wp.com/www.cocoanetics.com/files/Screen-Shot-2012-09-29-at-16.30.33.png?resize=179%2C281)](https://i0.wp.com/www.cocoanetics.com/files/Screen-Shot-2012-09-29-at-16.30.33.png)

现在，在 iOS 上执行同样的技巧。

### 在 iOS 上实现响应者链动作

显然，这些用例在 iOS 上要少得多。正如我上面提到的，主要原因是你没有一个应用范围的菜单，用户可以通过它下达大多数命令，而是你会有一些控制（control）布置在由视图控制器控制的视图上。而这个视图控制器将是 File's Owner，为连接到这些控制提供 outlet。

然而，有一种场景下了解这个方法可以简化你的生活。考虑这样一种情况：你想要让子视图中的事件触发应用程序级别的事情。比如在两个视图控制器之间翻转。

当前的 Xcode 实用工具应用模板使用一个复杂的系统来实现翻转。有一个 `MainViewController`，它有一个信息按钮，该按钮呈现一个 `FlipsideViewController`。这个按钮通过 File's Owner 连接到视图控制器。

在对代码不做任何更改的情况下，我们也可以向 `MainViewController` 的 First Responder 定义一个用户定义的 `showInfo` 动作。然后，我们可以将信息按钮连接到那个动作，而不是 File's Owner。一切仍然有效。

考虑另一个例子。假设你有一个应用，其中包含多个平级的视图控制器。这些视图控制器将由一个容器视图控制器（类似于 `UITabBarController`）呈现。你可以在其中一个子视图控制器中有一个按钮，但响应的动作方法可能是容器视图控制器的一部分。

[![](https://i0.wp.com/www.cocoanetics.com/files/Screen-Shot-2012-09-29-at-17.27.20.png?resize=450%2C391)](https://i0.wp.com/www.cocoanetics.com/files/Screen-Shot-2012-09-29-at-17.27.20.png)

在那里，事件将沿着响应者链向上传递。视图、视图控制器、父视图（= 容器视图控制器的视图）、容器视图控制器，在那里它会找到这个动作。如果没有响应者链，你将不得不使用一些技巧来让按钮按下事件一直传递到容器视图控制器。

事实上，甚至 Apple 也经常使用委托协议（delegate protocol）来让视图控制器与其父级通信。例如，上述实用工具应用模板的 `FlipSideViewController` 有一个专门用于处理“完成”按钮的协议：

```
@protocol FlipsideViewControllerDelegate
- (void)flipsideViewControllerDidFinish:(FlipsideViewController *)controller;
@end
```

根据我们现在所知道的，我们可以很容易地使这个委托协议变得不必要，而是在响应者链上有一个 `flipBack` 动作，用更少的代码实现相同的效果。

在 First Responder 上创建一个 `flipBack:` 动作，并在断开与 File's Owner 的链接后，将“完成”按钮的动作链接到该动作。

[![](https://i0.wp.com/www.cocoanetics.com/files/Screen-Shot-2012-09-29-at-17.34.36.png?resize=588%2C282)](https://i0.wp.com/www.cocoanetics.com/files/Screen-Shot-2012-09-29-at-17.34.36.png)

然后在 `MainViewController` 中实现 `flipBack` 动作。

```
- (void)flipBack:(id)sender
{
	[self dismissViewControllerAnimated:YES completion:nil];
}
```

现在我们可以去掉委托协议、`FlipsideViewController` 上的委托属性以及调用委托的 `flipsideViewControllerDidFinish:` 方法的 `done:` 动作。

如果用户现在点击“完成”按钮，动作会传递：`FlipsideViewController`、`MainViewController` 的视图、`MainViewController`，然后在那里找到要执行的 `flipBack:` 动作。

诚然，有些场景下，你希望以模态方式呈现的子视图控制器向其委托传达成功或失败。但对于像这样简单的场景，使用响应者链要简单得多。

### 额外奖励：在不知道当前 First Responder 的情况下隐藏键盘

你也可以利用响应者链机制来触发那些你不知道或不关心响应者是谁的动作。例如，当你想要键盘消失，但又不愿意跟踪当前的第一响应者时。

每当一个实现了 `UIKeyInput` 或 `UITextInput` 协议的视图成为第一响应者时，iOS 键盘就会显示。如果你在屏幕上有多个 `UITextField` 实例，并且你想以编程方式关闭键盘，那么你必须跟踪当前哪一个是第一响应者。或者，众所周知，我也可以连续对所有文本字段调用 `resignFirstResponder`，因为其中任何一个都可能是。

了解响应者链使我们能够在没有任何先验知识的情况下关闭键盘。我们只需要知道如何沿着响应者链发送消息，就可以保证产生键盘的视图排在第一位。

Mac 大师 Sean Heber 教了我们如何做到：

> [[UIApplication sharedApplication] sendAction:@selector(resignFirstResponder) to:nil from:nil forEvent:nil];
>
> — Sean Heber (@BigZaphod) [August 1, 2012](https://twitter.com/BigZaphod/status/230744266509516800)

任何选择器都可以用作 `UIApplication` 用于向响应者链发送消息的 `sendAction` 方法的动作参数。如果接收者是 `nil`，那么它将开始在响应者链中传递，当然是从 First Responder 开始。哦，多巧啊！这个第一响应者也正是我们想要让其放弃此状态的文本字段。

### 结论

响应者链是一个伟大的概念，它简化了 Mac 上希望文稿响应动作的菜单操作。在 iOS 上，Apple 使用了完全相同的方法，尽管通过在链中插入视图控制器进行了改进。

理解如何利用响应者链可以为你避免一些架构上的难题，本文介绍的基本知识应该能让你在更好地理解如何利用它方面走得很远。

由于应用程序委托从 iOS 5 开始被提升为 `UIResponder`，甚至可能在某些场景下，你希望将响应动作放在那里。然后，你可以从视图层级结构的深处触发这些动作，而不必通过 `[UIApplication sharedApplication].delegate` 这个单例。承认吧，你以前不止一次这样做过，对吧？

---

**分类：**[食谱](https://www.cocoanetics.com/category/recipes/)

[← UTI 的乐趣](https://www.cocoanetics.com/2012/09/fun-with-uti/)

[漏洞报告：在 Storyboard 中使用时 First Responder 失效 →](https://www.cocoanetics.com/2012/09/radar-first-responder-defunct-when-used-in-storyboard/)

### 引用

1. [漏洞报告：在 Storyboard 中使用时 First Responder 失效 | Cocoanetics](http://www.cocoanetics.com/2012/09/radar-first-responder-defunct-when-used-in-storyboard/)
2. [Lion 的全屏模式 | Cocoanetics](http://www.cocoanetics.com/2012/11/the-lions-full-screen-mode/)
