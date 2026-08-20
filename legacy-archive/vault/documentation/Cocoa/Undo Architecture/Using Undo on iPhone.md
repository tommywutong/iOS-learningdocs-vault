---
title: 撤销架构
apple_id: 10000010i
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2011-06-03'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/UndoArchitecture/Articles/iPhoneUndo.html
archived_at: '2026-07-15T07:21:01.344972Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [撤销架构](Introduction%20to%20Undo%20Architecture.md)


[下一页](Document%20Revision%20History.md)[上一页](Using%20Undo%20in%20AppKit-Based%20Applications.md)

# 在 iPhone 上使用撤销

UIKit 通过建立一套在应用程序中分发和选取撤销管理器的机制，补充了 [NSUndoManager](https://developer.apple.com/documentation/foundation/undomanager) 类的行为。

默认情况下，用户通过摇晃设备来触发撤销操作。如果你不想要这种行为，就需要告诉应用程序不要把摇晃事件当作编辑请求来响应：

```objc
application.applicationSupportsShakeToEdit = NO;
```

你通常在应用程序启动时设置这个[属性](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/DeclaredProperty.html#//apple_ref/doc/uid/TP40008195-CH13)，也就是在应用程序[委托](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14)的 [applicationDidFinishLaunching:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623053-applicationdidfinishlaunching) 或 [application:didFinishLaunchingWithOptions:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application) 方法中。

一个应用程序可以有一个或多个撤销客户端——即在各自的局部上下文中注册和执行撤销操作的对象。这些对象各自拥有自己的 `NSUndoManager` 对象以及与之关联的撤销栈和重做栈。

这种情形的一个例子是自定义视图，每个视图都是某个撤销管理器的客户端。举例来说，你可以有一个包含两个自定义视图的窗口；每个视图都能以可变的[属性](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectModeling.html#//apple_ref/doc/uid/TP40008195-CH41)（如字体、颜色和字号）显示文本，而用户可以撤销（或重做）任一视图中对任一属性的每一次改动。`UIResponder` 能帮助你在视图层级中控制撤销操作的上下文。

[UIResponder](https://developer.apple.com/documentation/uikit/uiresponder) 类声明了 [undoManager](https://developer.apple.com/documentation/uikit/uiresponder/1621122-undomanager) [属性](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/DeclaredProperty.html#//apple_ref/doc/uid/TP40008195-CH13)，继承自它的对象（尤其是视图和[视图控制器](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ControllerObject.html#//apple_ref/doc/uid/TP40008195-CH11)）可以通过该属性向框架提供撤销管理器。当应用程序收到撤销事件时，`UIResponder` 会沿响应者链向上查找（从第一响应者开始），寻找一个能从 `undoManager` 返回 `NSUndoManager` 对象的响应者。找到的第一个撤销管理器会被用于该撤销或重做操作。

UIKit 会根据撤销管理器是否存在及其状态，自动为你创建合适的提示面板。如果用户选择执行撤销或重做操作，撤销管理器就会相应地收到 [undo](https://developer.apple.com/documentation/foundation/nsundomanager/1412189-undo) 或 [redo](https://developer.apple.com/documentation/foundation/nsundomanager/1417030-redo) 消息。

你通常在视图控制器中提供撤销管理器（参见[设计模式](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dimbqfvjvomq)）。如果你希望某个视图控制器提供撤销管理器，那么该视图控制器必须愿意成为第一响应者，并且必须在它的视图出现时成为第一响应者。反之，它应该在视图消失时放弃第一响应者身份。实现方式如下：

```objc
- (BOOL)canBecomeFirstResponder {
    return YES;
}

- (void)viewDidAppear:(BOOL)animated {
    [super viewDidAppear:animated];
    [self becomeFirstResponder];
}

- (void)viewWillDisappear:(BOOL)animated {
    [super viewWillDisappear:animated];
    [self resignFirstResponder];
}
```


在 iPhone 应用程序中，考虑撤销支持时会涉及到若干模式、惯例和约束：

- 用户每次只与一屏信息交互。

  用户在不同屏幕之间导航。每一屏包含一组不同的信息，并由不同的[视图控制器](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ControllerObject.html#//apple_ref/doc/uid/TP40008195-CH11)管理。
- 编辑模式有明确的界定，而状态的保存是隐式的。

  用户通常通过轻点“编辑”按钮进入编辑模式。在编辑模式下，他们往往可以选择取消已做的改动。当用户轻点“完成”时，他们所做的任何改动都被视为已提交——例如，用户不必再去选择“保存”菜单项。
- 撤销和重做消息是直接发送给撤销管理器的。

  框架不会提供供你重写的撤销和重做方法。
- 设备上的内存是受限的。

  你需要[避免占用过多内存](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/MemoryManagement.html#//apple_ref/doc/uid/TP40008195-CH27)，否则你的应用程序可能会被终止。

在支持撤销时，你应当留意这些设计模式、惯例和约束。

到处都支持撤销未必合理。用户的预期是：一旦某个动作已经执行，它就是不可逆的。而且，上下文也很重要。考虑这样一个应用程序：它显示一份书籍列表，并允许你导航到详情视图，在那里编辑单本书的各个[属性](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/DeclaredProperty.html#//apple_ref/doc/uid/TP40008195-CH13)（例如书名、作者和版权日期）。你可能从列表界面新建一本书，在另外两个界面之间来回导航以编辑它的属性，然后再返回最初的列表。如果在列表视图中执行撤销，撤销的却是两屏之外对作者姓名所做的改动，而不是删除整本书，这看起来就会很奇怪。

还有内存管理的问题。每个撤销动作都要求把执行该撤销所需的数据保留在内存中。在某些应用程序中，这可能成为一笔可观的开销。总的来说，最好尽量把内存占用控制在最小。如果你的应用程序支持编辑模式，那么合适的做法可能是：只在用户进入编辑模式时才创建撤销管理器，并在用户离开该模式时销毁它。

由于撤销和重做消息是直接发送给撤销管理器的，你应该把自己注册为撤销管理器变更[通知](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Notification.html#//apple_ref/doc/uid/TP40008195-CH35)的观察者。在通知回调中，你可以按需把改动反映到用户界面上。

由于用户可能在一次编辑操作过程中在不同界面之间导航，你可能需要提醒他们正在撤销的到底是什么。提供撤销动作标题很有用，这样用户就能清楚撤销或重做操作会产生什么效果。

下面的示例演示了在 `UITableView` 的子类中如何响应编辑状态的变化。如果开始编辑，你就创建一个撤销管理器来跟踪改动。你还把自己注册为撤销管理器变更通知的观察者，这样在执行撤销或重做操作时，表视图就能被重新加载。当编辑结束时，从通知中心注销并移除撤销管理器。

```objc
- (void)setEditing:(BOOL)editing animated:(BOOL)animated {

    [super setEditing:editing animated:animated];

    NSNotificationCenter *dnc = [NSNotificationCenter defaultCenter];

    if (editing) {
        NSUndoManager *anUndoManager = [[NSUndoManager alloc] init];
        self.undoManager = anUndoManager;
        [undoManager setLevelsOfUndo:3];
        [anUndoManager release];

        [dnc addObserver:self selector:@selector(undoManagerDidUndo:)
                    name:NSUndoManagerDidUndoChangeNotification object:undoManager];
        [dnc addObserver:self selector:@selector(undoManagerDidRedo:)
                    name:NSUndoManagerDidRedoChangeNotification object:undoManager];
    }
    else {
        [dnc removeObserver:self];
        self.undoManager = nil;
    }
}
```

[下一页](Document%20Revision%20History.md)[上一页](Using%20Undo%20in%20AppKit-Based%20Applications.md)

