---
title: 资源编程指南
apple_id: 10000051i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/LoadingResources/CocoaNibs/CocoaNibs.html
archived_at: '2026-07-15T07:16:32.504080Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [资源编程指南](About%20Resources.md)


[下一页](String%20Resources.md)[上一页](About%20Resources.md)

# Nib 文件

nib 文件在 OS X 和 iOS 应用程序的开发中扮演着重要角色。借助 nib 文件，你可以使用 Xcode 以图形化方式创建和调整用户界面，而不必通过编写代码来完成。由于改动的结果立刻可见，你可以非常快速地尝试不同的布局和配置。你还可以在之后修改用户界面的许多方面，而无需重写任何代码。

对于使用 AppKit 或 UIKit [框架](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Framework.html#//apple_ref/doc/uid/TP40008195-CH56)构建的应用程序来说，nib 文件还有一层额外的意义。这两个框架都支持用 nib 文件来布局窗口、视图和控件，并把这些元素与应用程序的事件处理代码整合起来。Xcode 与这些框架协同工作，帮助你把用户界面中的控件连接到项目中负责响应这些控件的对象上。这种整合大幅减少了 nib 文件加载之后所需的设置工作，也让你日后修改代码与用户界面之间的关系变得很容易。

nib 文件描述了应用程序用户界面的可视元素，包括窗口、视图、控件等等。它也可以描述非可视元素，比如应用程序中管理窗口和视图的那些对象。最重要的是，nib 文件对这些对象的描述与它们在 Xcode 中被配置的样子完全一致。在运行时，这些描述被用来在应用程序内部重建这些对象及其配置。当你在运行时加载一个 nib 文件时，得到的是 Xcode 文档中那些对象的精确副本。nib 加载代码会实例化这些对象、完成配置，并重新建立你在 nib 文件中创建的所有对象间连接。

以下各节介绍与 AppKit 和 UIKit 框架配合使用的 nib 文件是如何组织的、其中包含哪些类型的对象，以及如何有效地使用这些对象。

界面对象（interface object）就是你为实现用户界面而添加到 nib 文件中的那些对象。当 nib 在运行时被加载时，界面对象就是 nib 加载代码实际实例化出来的对象。大多数新建的 nib 文件默认至少包含一个界面对象，通常是一个窗口或菜单资源；在设计界面的过程中，你会往 nib 文件里添加更多界面对象。这是 nib 文件中最常见的对象类型，通常也正是你创建 nib 文件的初衷。

除了表示窗口、视图、控件和菜单这类可视对象之外，界面对象也可以表示非可视对象。几乎在所有情况下，你添加到 nib 文件中的非可视对象都是应用程序用来管理可视对象的额外[控制器对象](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ControllerObject.html#//apple_ref/doc/uid/TP40008195-CH11)。虽然你也可以在应用程序代码中创建这些对象，但把它们添加到 nib 文件中并在那里完成配置往往更方便。Xcode 提供了一个通用对象，专门用于向 nib 文件添加控制器以及其他非可视对象。它还提供了通常用于管理 Cocoa 绑定的控制器对象。

nib 文件中最重要的对象之一是 File’s Owner 对象。与界面对象不同，File’s Owner 是一个占位符对象，它不会在 nib 文件加载时被创建。相反，你要在自己的代码中创建这个对象，再把它传给 nib 加载代码。这个对象之所以如此重要，是因为它是应用程序代码与 nib 文件内容之间的主要纽带。更确切地说，它是负责管理 nib 文件内容的控制器对象。

在 Xcode 中，你可以在 File’s Owner 与 nib 文件中的其他界面对象之间建立连接。当你加载该 nib 文件时，nib 加载代码会使用你指定的替换对象来重建这些连接。这使得你的对象能够引用 nib 文件中的对象，并自动接收来自界面对象的[消息](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Message.html#//apple_ref/doc/uid/TP40008195-CH59)。

在 nib 文件中，First Responder 是一个占位符对象，代表应用程序动态确定的响应者链中的第一个对象。由于应用程序的响应者链无法在设计时确定，First Responder 占位符便充当了所有需要投递给应用程序响应者链的 action 消息的替身目标。菜单项通常以 First Responder 占位符为目标。例如，Window 菜单中的 Minimize 菜单项隐藏的是应用程序最前面的窗口，而不只是某个特定窗口；Copy 菜单项应当复制当前选中的内容，而不只是某个控件或视图中的选中内容。应用程序中的其他对象同样可以把 First Responder 作为目标。

把 nib 文件加载到内存中时，你无需为管理或替换 First Responder 占位符对象做任何事情。AppKit 和 UIKit 框架会根据应用程序当前的配置自动设置并维护第一响应者。

关于响应者链以及它在基于 AppKit 的应用程序中如何分发事件的更多信息，请参阅 [Event Architecture](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/EventOverview/EventArchitecture/EventArchitecture.html#//apple_ref/doc/uid/10000060i-CH3)（见 _[Cocoa 事件处理指南](../Cocoa%20Event%20Handling%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3da2i)_）。关于 iPhone 应用程序中响应者链和 action 处理的信息，请参阅 _iOS 事件处理指南_。

当程序加载 nib 文件时，Cocoa 会重建你在 Xcode 中创建的整个对象图。这个[对象图](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectGraph.html#//apple_ref/doc/uid/TP40008195-CH54)包含 nib 文件中的所有窗口、视图、控件、单元格、菜单和自定义对象。_顶层对象_（top-level object）是这些对象中没有父对象的那一部分。顶层对象通常只包括你添加到 nib 文件中的窗口、菜单栏和自定义控制器对象。（File’s Owner、First Responder 和 Application 这类对象属于占位符对象，不算顶层对象。）

通常，你会用 File’s Owner 对象中的 outlet 来保存对 nib 文件顶层对象的引用。不过，如果你不使用 outlet，也可以直接从 nib 加载例程中取回顶层对象。你应该始终在某处保留指向这些对象的指针，因为应用程序有责任在用完它们之后将其释放。关于 nib 对象在加载时的行为的更多信息，请参阅[管理 nib 文件中对象的生命周期](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2tc2jninedilktk43a)。

在 Xcode 中，你可以在 nib 文件的内容里引用外部的图像和声音资源。某些控件和视图能够在其默认配置中显示图像或播放声音。Xcode 库提供了对 Xcode 工程中图像和声音资源的访问途径，因此你可以把 nib 文件链接到这些资源上。nib 文件并不直接存储这些资源，而是存储资源文件的名称，以便 nib 加载代码之后能够找到它。

当你加载一个引用了图像或声音资源的 nib 文件时，nib 加载代码会把实际的图像或声音文件读入内存并缓存起来。在 OS X 中，图像和声音资源存放在具名缓存里，之后你可以按需访问它们。在 iOS 中，只有图像资源会存放在具名缓存中。要访问图像，请根据所在平台使用 [NSImage](https://developer.apple.com/documentation/appkit/nsimage) 或 [UIImage](https://developer.apple.com/documentation/uikit/uiimage) 的 `imageNamed:` 方法。要访问 OS X 中缓存的声音，请使用 [NSSound](https://developer.apple.com/documentation/appkit/nssound) 的 [soundNamed:](https://developer.apple.com/documentation/appkit/nssound/1477318-soundnamed) 方法。

创建 nib 文件时，务必仔细考虑你打算如何使用文件中的对象。非常简单的应用程序或许可以把全部用户界面组件都放在一个 nib 文件里，但对大多数应用程序而言，把组件分散到多个 nib 文件中更好。创建较小的 nib 文件可以让你只加载当下立即需要的那部分界面。这样也更容易调试你可能遇到的问题，因为需要排查的地方更少。

创建 nib 文件时，请记住以下几条准则：

- 设计 nib 文件时要考虑延迟加载。规划好让所加载的 nib 文件只包含你马上就需要的对象。
- 对于 OS X 应用程序的主 nib 文件，考虑只在其中存放应用程序菜单栏和一个可选的应用程序[委托对象](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14)。避免包含那些直到应用程序启动之后才会用到的窗口或用户界面元素。应当把这些资源放到单独的 nib 文件中，在启动后按需加载。
- 把重复使用的用户界面组件（比如文档窗口）存放在单独的 nib 文件中。
- 对于只是偶尔用到的窗口或菜单，把它存放在单独的 nib 文件中。这样只有在真正用到时，该资源才会被加载进内存。
- 让 File’s Owner 成为 nib 文件与外界之间唯一的联系点；参阅[访问 nib 文件的内容](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2tc2jninedilktk43q)。

当 nib 文件被加载到内存中时，nib 加载代码会执行若干步骤，以确保 nib 文件中的对象被正确创建和初始化。理解这些步骤有助于你写出更好的控制器代码来管理用户界面。

当你使用 [NSNib](https://developer.apple.com/documentation/appkit/nsnib) 或 [NSBundle](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSBundle/Description.html#//apple_ref/occ/cl/NSBundle) 的方法来加载并实例化 nib 文件中的对象时，底层的 nib 加载代码会执行以下操作：

1. 它把 nib 文件的内容以及所有被引用的资源文件加载到内存中：

   - 整个 nib [对象图](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectGraph.html#//apple_ref/doc/uid/TP40008195-CH54)的原始数据被载入内存，但尚未[解归档](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Archiving.html#//apple_ref/doc/uid/TP40008195-CH1)。
   - 与该 nib 文件关联的所有自定义图像资源被加载并加入 Cocoa 图像缓存；参阅[关于图像和声音资源](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2tc2jninedilktk44q)。
   - 与该 nib 文件关联的所有自定义声音资源被加载并加入 Cocoa 声音缓存；参阅[关于图像和声音资源](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2tc2jninedilktk44q)。
2. 它对 nib 对象图数据进行解归档，并实例化其中的对象。每个新对象如何[初始化](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Initialization.html#//apple_ref/doc/uid/TP40008195-CH21)取决于对象的类型以及它在归档中的编码方式。nib 加载代码依次按以下规则来决定使用哪个初始化方法。

   1. 默认情况下，对象会收到 `initWithCoder:` 消息。

      在 OS X 中，标准对象包括系统提供、可在默认 Xcode 库中找到的视图、单元格、菜单和视图控制器。它也包括通过自定义插件添加到库中的任何第三方对象。即使你改变了这类对象的类，Xcode 仍会把标准对象编码进 nib 文件，然后告诉归档器在该对象被解归档时替换成你的自定义类。

      在 iOS 中，任何遵循 [NSCoding](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSCoding/Description.html#//apple_ref/occ/intf/NSCoding) 协议的对象都使用 `initWithCoder:` 方法初始化。这包括 [UIView](https://developer.apple.com/documentation/uikit/uiview) 和 [UIViewController](https://developer.apple.com/documentation/uikit/uiviewcontroller) 的所有子类，无论它们属于默认 Xcode 库还是你自己定义的自定义类。
   2. OS X 中的自定义视图会收到 `initWithFrame:` 消息。

      自定义视图是指 Xcode 没有现成实现可用的 [NSView](https://developer.apple.com/documentation/appkit/nsview) 子类。通常，这些视图由你在应用程序中定义，用来提供自定义的可视内容。自定义视图不包括属于默认库或集成的第三方插件的标准系统视图（比如 [NSSlider](https://developer.apple.com/documentation/appkit/nsslider)）。

      遇到自定义视图时，Xcode 会向你的 nib 文件中编码一个特殊的 `NSCustomView` 对象。该自定义视图对象包含构建你所指定的真实视图子类所需的信息。在加载时，`NSCustomView` 对象会向真实的视图类发送 `alloc` 和 `initWithFrame:` 消息，然后用得到的视图对象把自己替换掉。最终效果是，由真实的视图对象来处理 nib 加载过程中后续的交互。

      iOS 中的自定义视图不使用 `initWithFrame:` 方法进行初始化。
   3. 除上述几种情形之外的自定义对象会收到 `init` 消息。
3. 它重新建立 nib 文件中各对象之间的所有连接（action、outlet 和绑定）。这包括与 File’s Owner 以及其他占位符对象之间的连接。建立连接的方式因平台而异：

   - outlet 连接

     - 在 OS X 中，nib 加载代码会先尝试用对象自身的方法来重新连接 outlet。对每一个 outlet，Cocoa 会查找形如 `set`_OutletName_`:` 的方法，若存在则调用它。如果找不到这样的方法，Cocoa 会在该对象中查找与 outlet 同名的实例变量，并尝试直接设置其值。如果连实例变量也找不到，则不会建立连接。

       设置 outlet 还会为所有已注册的观察者生成一条[键值观察](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/KVO.html#//apple_ref/doc/uid/TP40008195-CH16)（KVO）通知。这些通知可能在所有对象间连接重新建立完毕之前就发出，而且必定发生在任何对象的 `awakeFromNib` 方法被调用之前。
     - 在 iOS 中，nib 加载代码使用 [setValue:forKey:](https://developer.apple.com/documentation/objectivec/nsobject/1415969-setvalue) 方法来重新连接每一个 outlet。该方法同样会先查找合适的存取方法，失败时再回退到其他方式。关于该方法如何设置值的更多信息，请参阅 _[NSKeyValueCoding Protocol Reference](https://developer.apple.com/documentation/foundation/object_runtime/nskeyvaluecoding)_ 中对它的说明。

       在 iOS 中设置 outlet 同样会为所有已注册的观察者生成 KVO 通知。这些通知可能在所有对象间连接重新建立完毕之前就发出，而且必定发生在任何对象的 `awakeFromNib` 方法被调用之前。
   - action 连接

     - 在 OS X 中，nib 加载代码使用源对象的 [setTarget:](https://developer.apple.com/documentation/appkit/nscontrol/1428885-target) 和 [setAction:](https://developer.apple.com/documentation/appkit/nscontrol/1428956-action) 方法来建立与目标对象的连接。如果目标对象不响应该 action 方法，则不会建立连接。如果目标对象为 `nil`，该 action 由响应者链处理。
     - 在 iOS 中，nib 加载代码使用 [UIControl](https://developer.apple.com/documentation/uikit/uicontrol) 对象的 [addTarget:action:forControlEvents:](https://developer.apple.com/documentation/uikit/uicontrol/1618259-addtarget) 方法来配置 action。如果目标为 `nil`，该 action 由响应者链处理。
   - 绑定

     - 在 OS X 中，Cocoa 使用源对象的 [bind:toObject:withKeyPath:options:](https://developer.apple.com/documentation/objectivec/nsobject/1458185-bind) 方法来建立它与目标对象之间的连接。
     - iOS 不支持绑定。
4. 它向 nib 文件中定义了相应[选择器](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Selector.html#//apple_ref/doc/uid/TP40008195-CH48)的相关对象发送 `awakeFromNib` 消息：

   - 在 OS X 中，该消息会发送给所有定义了此方法的界面对象。它同样会发送给 File’s Owner 以及任何定义了该方法的占位符对象。
   - 在 iOS 中，该消息只发送给由 nib 加载代码实例化出来的界面对象，不会发送给 File’s Owner、First Responder 或任何其他占位符对象。
5. 它显示所有在 nib 文件中启用了 “Visible at launch time” 属性的窗口。

nib 加载代码调用各对象 `awakeFromNib` 方法的顺序是没有保证的。在 OS X 中，Cocoa 会尽量最后调用 File’s Owner 的 `awakeFromNib` 方法，但并不保证一定如此。如果你需要在加载时对 nib 文件中的对象做进一步配置，最合适的时机是在 nib 加载调用返回之后。到那时，所有对象都已创建、初始化完毕，可以直接使用。

每当你请求 [NSBundle](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSBundle/Description.html#//apple_ref/occ/cl/NSBundle) 或 [NSNib](https://developer.apple.com/documentation/appkit/nsnib) 类加载一个 nib 文件时，底层代码都会为该文件中的对象创建一份新的[副本](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectCopying.html#//apple_ref/doc/uid/TP40008195-CH38)并返回给你。（nib 加载代码不会复用上一次加载得到的 nib 文件对象。）你需要确保在必要的时间内一直持有这个新的对象图，并在用完之后放弃对它的持有。通常你需要对顶层对象持有强引用，以确保它们不会被释放；而对象图中层级更低的对象则不需要强引用，因为它们由各自的父对象持有，同时你也应尽量降低产生强引用循环的风险。

从实践角度看，在 iOS 和 OS X 中，outlet 都应该定义为[声明属性](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/DeclaredProperty.html#//apple_ref/doc/uid/TP40008195-CH13)。outlet 一般应当是 `weak` 的，但从 File’s Owner 指向 nib 文件（在 iOS 中还包括 storyboard 场景）中顶层对象的那些 outlet 除外，它们应当是 `strong` 的。因此，你自己创建的 outlet 通常应该是 `weak` 的，原因如下：

- 举例来说，你为视图控制器的视图或窗口控制器的窗口的子视图所创建的 outlet，只是对象之间的任意引用，并不意味着持有关系。
- 强 outlet 通常由框架类来指定（例如 `UIViewController` 的 `view` outlet，或 `NSWindowController` 的 `window` outlet）。

```objc
@property (weak) IBOutlet MyView *viewContainerSubview;
@property (strong) IBOutlet MyOtherClass *topLevelObject;
```

outlet 通常被视为定义它的类的私有成员；除非有理由把该属性公开出去，否则应把属性声明隐藏在类扩展中。例如：

```objc
// MyClass.h

@interface MyClass : MySuperclass
@end

// MyClass.m

@interface MyClass ()
@property (weak) IBOutlet MyView *viewContainerSubview;
@property (strong) IBOutlet MyOtherClass *topLevelObject;
@end
```

这些模式同样适用于从容器视图到其子视图的引用，此时你需要考虑对象图的内部一致性。例如，对于表格视图单元格，指向特定子视图的 outlet 同样通常应该是 weak 的。如果一个表格视图包含一个图像视图和一个文本视图，那么只要它们仍是该表格视图单元格自身的子视图，这些引用就一直有效。

当 outlet 应当被视为拥有所引用的对象时，就应该把它改成 `strong`：

- 如前所述，File’s Owner 常常属于这种情况——nib 文件中的顶层对象通常被认为归 File’s Owner 所有。
- 在某些情况下，你可能需要让来自 nib 文件的某个对象在其原始容器之外继续存在。例如，你可能有一个指向视图的 outlet，而该视图可以被临时从初始视图层次结构中移除，因此必须独立地维持它。

对于你预期会被派生子类的类（尤其是抽象类），应当公开暴露 outlet，以便子类能够恰当地使用它们（例如 `UIViewController` 的 `view` outlet）。如果预期该类的使用者需要与某个属性交互，也可以把 outlet 暴露出来；例如表格视图单元格可能会暴露其子视图。在后一种情况下，比较合适的做法是暴露一个只读的公开 outlet，并在私有处把它重定义为可读写，例如：

```objc
// MyClass.h

@interface MyClass : UITableViewCell
@property (weak, readonly) MyType *outletName;
@end

// MyClass.m

@interface MyClass ()
@property (weak, readwrite) IBOutlet MyType *outletName;
@end
```


由于历史原因，在 OS X 中，nib 文件的顶层对象在创建时会带有一个额外的引用计数。Application Kit 提供了几项特性，帮助确保 nib 对象被正确释放：

- `NSWindow` 对象（包括面板）有一个 [isReleasedWhenClosed](https://developer.apple.com/documentation/appkit/nswindow/1419062-isreleasedwhenclosed) 特性，如果设置为 `YES`，就会指示该窗口在关闭时释放自身（以及其视图层次结构中所有依赖的对象）。在 nib 文件中，你可以通过 Xcode 检查器 Attributes 面板中的 “Release when closed” 复选框来设置该选项。
- 如果某个 nib 文件的 File’s Owner 是 [NSWindowController](https://developer.apple.com/documentation/appkit/nswindowcontroller) 对象（在基于文档的应用程序中，文档 nib 默认就是如此——回想一下 `NSDocument` 会管理一个 `NSWindowController` 实例）或 [NSViewController](https://developer.apple.com/documentation/appkit/nsviewcontroller) 对象，那么它会自动处置它所管理的窗口。

_如果 File’s Owner 不是_  `NSWindowController`  _或_  `NSViewController` 的实例，那么你需要自己递减顶层对象的引用计数。你必须把对顶层对象的引用强制转换为 Core Foundation 类型，并使用 [CFRelease](https://developer.apple.com/documentation/corefoundation/1521153-cfrelease)。（如果你不想为所有顶层对象都建立 outlet，可以使用 `NSNib` 类的 [instantiateNibWithOwner:topLevelObjects:](https://developer.apple.com/documentation/appkit/nsnib/1547297-instantiatenibwithowner) 方法来获取 nib 文件顶层对象的数组。）

宽泛地说，action 方法（参阅 [Target-Action](https://developer.apple.com/library/archive/documentation/General/Devpedia-CocoaApp-MOSX/TargetAction.html#//apple_ref/doc/uid/TP40009448-CH3)，适用于 OS X；iOS 平台参阅 [Target-Action](https://developer.apple.com/library/archive/documentation/General/Conceptual/Devpedia-CocoaApp/TargetAction.html#//apple_ref/doc/uid/TP40009071-CH3)）是通常由 nib 文件中另一个对象来调用的方法。action 方法用类型限定符 `IBAction` 代替 `void` 返回类型，把所声明的方法标记为 action，以便 Xcode 能够识别它。

```objc
@interface MyClass
- (IBAction)myActionMethod:(id)sender;
@end
```

你可以把 action 方法视为类的私有方法，因而不在公开的 `@interface` 中声明它们。（因为 Xcode 会解析实现文件，所以不必在头文件中声明它们。）

```objc
// MyClass.h

@interface MyClass
@end

// MyClass.m

@implementation MyClass
- (IBAction)myActionMethod:(id)sender {
    // 实现代码。
}
@end
```

通常不应该以编程方式调用 action 方法。如果你的类需要执行与某个 action 方法相关的工作，应当把实现抽取到另一个方法中，再由该 action 方法来调用它。

```objc
// MyClass.h

@interface MyClass
@end

// MyClass.m

@interface MyClass (PrivateMethods)
- (void)doSomething;
- (void)doWorkThatRequiresMeToDoSomething;
@end

@implementation MyClass
- (IBAction)myActionMethod:(id)sender {
    [self doSomething];
}

- (void)doSomething {
    // 实现代码。
}

- (void)doWorkThatRequiresMeToDoSomething {
    // 前置处理。
    [self doSomething];
    // 后续处理。
}

@end
```


AppKit 和 UIKit 框架都为应用程序中 nib 文件的加载与管理提供了一定程度的自动化行为。两个框架都提供了加载应用程序主 nib 文件的基础设施。此外，AppKit 框架还通过 [NSDocument](https://developer.apple.com/documentation/appkit/nsdocument) 和 [NSWindowController](https://developer.apple.com/documentation/appkit/nswindowcontroller) 类支持加载其他 nib 文件。以下各节介绍这些针对 nib 文件的内建支持、你如何利用它们，以及在自己的应用程序中修改这些支持的方式。

Xcode 中大多数应用程序工程模板都预先配置好了一个主 nib 文件。你要做的只是修改这个默认的 nib 文件，然后构建应用程序。启动时，应用程序的默认配置数据会告诉应用程序对象到哪里去找这个 nib 文件，以便加载它。在基于 AppKit 和基于 UIKit 的应用程序中，这些配置数据都位于应用程序的 `Info.plist` 文件里。应用程序首次被加载时，默认的应用程序启动代码会在 `Info.plist` 文件中查找 `NSMainNibFile` 键。如果找到该键，它会在应用程序 bundle 中查找名称（带或不带文件扩展名）与该键的值相匹配的 nib 文件并加载它。

[UIViewController](https://developer.apple.com/documentation/uikit/uiviewcontroller)（iOS）和 [NSViewController](https://developer.apple.com/documentation/appkit/nsviewcontroller)（OS X）类支持自动加载与之关联的 nib 文件。如果你在创建 View Controller 时指定了一个 nib 文件，那么当你尝试访问该 View Controller 的视图时，这个 nib 文件会被自动加载。View Controller 与 nib 文件中各对象之间的连接会自动建立；在 iOS 中，`UIViewController` 对象还会在视图最终加载并显示到屏幕上时收到额外的通知。为了更好地管理内存，`UIViewController` 类还会在低内存情况下（视情况）处理其 nib 文件的卸载。

关于如何使用和配置 `UIViewController` 类的更多信息，请参阅 _[iOS View Controller 编程指南](https://developer.apple.com/library/archive/featuredarticles/ViewControllerPGforiPhoneOS/index.html#//apple_ref/doc/uid/TP40007457)_。

在 AppKit 框架中，[NSDocument](https://developer.apple.com/documentation/appkit/nsdocument) 类会与默认的窗口控制器配合，加载包含文档窗口的 nib 文件。`NSDocument` 的 [windowNibName](https://developer.apple.com/documentation/appkit/nsdocument/1515174-windownibname) 方法是一个便捷方法，你可以用它来指定包含相应文档窗口的 nib 文件。当创建新文档时，文档对象会把你指定的 nib 文件名传给默认的窗口控制器对象，由后者加载并管理该 nib 文件的内容。如果你使用 Xcode 提供的标准模板，唯一需要做的就是把文档窗口的内容添加到 nib 文件中。

[NSWindowController](https://developer.apple.com/documentation/appkit/nswindowcontroller) 类同样为加载 nib 文件提供了自动支持。如果你以编程方式创建自定义窗口控制器，可以选择用一个 [NSWindow](https://developer.apple.com/documentation/appkit/nswindow) 对象来初始化它，也可以用一个 nib 文件名来初始化。如果选择后者，`NSWindowController` 类会在客户端首次尝试访问该窗口时自动加载指定的 nib 文件。在那之后，窗口控制器会把窗口一直保留在内存中；即使窗口的 “Release when closed” 特性被设置了，它也不会再从 nib 文件重新加载。

OS X 和 iOS 都提供了把 nib 文件加载到应用程序中的便捷方法。AppKit 和 UIKit 框架都在 [NSBundle](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSBundle/Description.html#//apple_ref/occ/cl/NSBundle) 类上定义了额外的方法来支持加载 nib 文件。此外，AppKit 框架还提供了 [NSNib](https://developer.apple.com/documentation/appkit/nsnib) 类，它提供与 `NSBundle` 类似的 nib 加载行为，但在某些特定场景下还有一些额外的优势。

在规划应用程序时，要确保你打算手动加载的 nib 文件配置得当，以简化加载过程。为 File’s Owner 选择合适的对象、并保持 nib 文件小巧，可以大大提升它们的易用性和内存效率。关于配置 nib 文件的更多建议，请参阅 [nib 文件设计准则](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2tc2jninedilktk42a)。

AppKit 和 UIKit 框架（通过 Objective-C 分类）在 [NSBundle](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSBundle/Description.html#//apple_ref/occ/cl/NSBundle) 类上定义了额外的方法，用于支持加载 nib 文件资源。这些方法在两个平台上的使用语义不同，方法的写法也不同。在 AppKit 中，访问 bundle 的方式总体上更多，因此从这些 bundle 加载 nib 文件的方法相应地也更多。在 UIKit 中，应用程序只能从主 bundle 加载 nib 文件，所需的选项因而更少。两个平台上可用的方法如下：

- AppKit

  - [loadNibNamed:owner:](https://developer.apple.com/documentation/foundation/nsbundle/1402904-loadnibnamed) [类方法](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ClassMethod.html#//apple_ref/doc/uid/TP40008195-CH8)
  - [loadNibFile:externalNameTable:withZone:](https://developer.apple.com/documentation/foundation/nsbundle/1402910-loadnibfile) 类方法
  - [loadNibFile:externalNameTable:withZone:](https://developer.apple.com/documentation/foundation/nsbundle/1402906-loadnibfile) 实例方法
- UIKit

  - [loadNibNamed:owner:options:](https://developer.apple.com/documentation/foundation/bundle/1618147-loadnibnamed) 实例方法

每当加载 nib 文件时，你都应该指定一个对象来充当该 nib 文件的 File’s Owner。File’s Owner 的角色非常重要。它是你正在运行的代码与即将在内存中创建的新对象之间的主要接口。所有 nib 加载方法都提供了指定 File’s Owner 的途径，要么直接指定，要么作为选项字典中的一个参数。

AppKit 和 UIKit 框架处理 nib 加载时的语义差异之一，在于顶层 nib 对象返回给应用程序的方式。在 AppKit 框架中，你必须使用某个 [loadNibFile:externalNameTable:withZone:](https://developer.apple.com/documentation/foundation/nsbundle/1402910-loadnibfile) 方法显式地请求它们。在 UIKit 中，[loadNibNamed:owner:options:](https://developer.apple.com/documentation/foundation/bundle/1618147-loadnibnamed) 方法会直接返回这些对象的数组。无论哪种情况，最简单的省心办法都是把顶层对象存放到 File’s Owner 对象的 outlet 中（参阅[管理 nib 文件中对象的生命周期](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2tc2jninedilktk43a)）。

清单 1-1 展示了在基于 AppKit 的应用程序中使用 `NSBundle` 类加载 nib 文件的一个简单示例。[loadNibNamed:owner:](https://developer.apple.com/documentation/foundation/nsbundle/1402904-loadnibnamed) 方法一返回，你就可以开始使用任何指向 nib 文件对象的 outlet 了。换句话说，整个 nib 加载过程都在这一次调用之内完成。AppKit 框架中的 nib 加载方法返回一个布尔值，表示加载操作是否成功。

__清单 1-1__  从当前 bundle 加载 nib 文件

```objc
- (BOOL)loadMyNibFile
{
    // myNib 文件必须位于定义 self 所属类的那个 bundle 中。
    if (![NSBundle loadNibNamed:@"myNib" owner:self])
    {
        NSLog(@"Warning! Could not load myNib file.\n");
        return NO;
    }
    return YES;
}
```

清单 1-2 展示了在基于 UIKit 的应用程序中加载 nib 文件的示例。在这个例子中，方法会检查返回的数组，判断 nib 对象是否加载成功。（每个 nib 文件都至少应该有一个代表其内容的顶层对象。）这个示例展示的是 nib 文件中除 File’s Owner 对象外没有其他占位符对象的简单情形。关于如何指定额外占位符对象的示例，请参阅[在加载时替换代理对象](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2tc2jninedilktk4zta)。

__清单 1-2__  在 iPhone 应用程序中加载 nib

```objc
- (BOOL)loadMyNibFile
{
    NSArray*    topLevelObjs = nil;

    topLevelObjs = [[NSBundle mainBundle] loadNibNamed:@"myNib" owner:self options:nil];
    if (topLevelObjs == nil)
    {
        NSLog(@"Error! Could not load myNib file.\n");
        return NO;
    }
    return YES;
}
```


获取 nib 文件顶层对象最简单的方式，是在 File’s Owner 对象中定义 outlet，并为访问这些对象提供 setter 方法（更好的做法是使用属性）。这种做法确保顶层对象被你的对象保留，并且你始终持有对它们的引用。

清单 1-3 展示了一个简化的 Cocoa 类的接口与实现，它用一个 outlet 来保留 nib 文件中唯一的顶层对象。在这个例子中，nib 文件里唯一的顶层对象是一个 [NSWindow](https://developer.apple.com/documentation/appkit/nswindow) 对象。由于 Cocoa 中顶层对象的初始保留计数为 1，代码里额外加了一次 release。这样做没有问题，因为执行 release 调用时，属性已经保留了该窗口。在 iPhone 应用程序中，你不应该以这种方式释放顶层对象。

__清单 1-3__  使用 outlet 获取顶层对象

```objc
// 类接口。
@interface MyController : NSObject
- (void)loadMyWindow;
@end

// 私有类扩展。
@interface MyController ()
@property (strong) IBOutlet NSWindow *window;
@end


// 类实现
@implementation MyController

- (void)loadMyWindow {
    [NSBundle loadNibNamed:@"myNib" owner:self];

    // 窗口的初始保留计数为 1，
    // 之后又被属性保留，因此额外加一次 release。
    NSWindow *window = self.window;
    CFRelease(__bridge window);
}
@end
```

如果你不想用 outlet 来保存对 nib 文件顶层对象的引用，就必须在代码中手动取回这些对象。获取顶层对象的技术因目标平台而异。在 OS X 中，你必须显式地请求这些对象；而在 iOS 中，它们会自动返回给你。

清单 1-4 展示了在 OS X 中获取 nib 文件顶层对象的过程。这个方法把一个可变数组放进 `nameTable` 字典，并把它与 [NSNibTopLevelObjects](https://developer.apple.com/documentation/appkit/nsnibtoplevelobjects) 键关联起来。nib 加载代码会查找这个数组对象，如果存在，就把顶层对象放进去。由于每个对象在被加入数组之前保留计数就是 1，仅仅释放数组并不足以同时释放数组中的对象。因此，这个方法向每个对象都发送了一条 release 消息，以确保数组是唯一持有它们引用的实体。

__清单 1-4__  在运行时获取 nib 文件的顶层对象

```objc
- (NSArray*)loadMyNibFile
{
    NSBundle*            aBundle = [NSBundle mainBundle];
    NSMutableArray*      topLevelObjs = [NSMutableArray array];
    NSDictionary*        nameTable = [NSDictionary dictionaryWithObjectsAndKeys:
                                            self, NSNibOwner,
                                            topLevelObjs, NSNibTopLevelObjects,
                                            nil];

    if (![aBundle loadNibFile:@"myNib" externalNameTable:nameTable withZone:nil])
    {
        NSLog(@"Warning! Could not load myNib file.\n");
        return nil;
    }

    // 释放这些对象，使它们仅由数组持有。
    [topLevelObjs makeObjectsPerformSelector:@selector(release)];
    return topLevelObjs;
}
```

在 iPhone 应用程序中获取顶层对象要简单得多，[清单 1-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2tc2jninedilktk4ytc) 已经展示过。在 UIKit 框架中，[NSBundle](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSBundle/Description.html#//apple_ref/occ/cl/NSBundle) 的 [loadNibNamed:owner:options:](https://developer.apple.com/documentation/foundation/bundle/1618147-loadnibnamed) 方法会自动返回一个包含顶层对象的数组。此外，在数组返回时，这些对象的保留计数已经调整好，你不需要再向每个对象发送额外的 release 消息。返回的数组是这些对象唯一的持有者。

当你想创建 nib 文件内容的多份[副本](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectCopying.html#//apple_ref/doc/uid/TP40008195-CH38)时，[UINib](https://developer.apple.com/documentation/uikit/uinib)（iOS）和 [NSNib](https://developer.apple.com/documentation/appkit/nsnib)（OS X）类能提供更好的性能。常规的 nib 加载过程是先从磁盘读取 nib 文件，然后实例化其中包含的对象。而使用 `UINib` 和 `NSNib` 类时，nib 文件只从磁盘读取一次，内容被保存在内存中。由于内容已在内存里，后续每次创建对象集合所花的时间更少，因为不再需要访问磁盘。

使用 `UINib` 和 `NSNib` 类总是分两步进行。第一步，创建该类的实例，并用 nib 文件的位置信息初始化它。第二步，实例化 nib 文件的内容，把对象加载到内存中。每次实例化 nib 文件时，你都可以指定不同的 File’s Owner 对象，并得到一组新的顶层对象。

清单 1-5 展示了在 OS X 中使用 `NSNib` 类加载 nib 文件内容的一种方式。[instantiateNibWithOwner:topLevelObjects:](https://developer.apple.com/documentation/appkit/nsnib/1547297-instantiatenibwithowner) 方法返回给你的数组已经是自动释放的。如果你打算在一段时间内继续使用该数组，应当自己复制一份。

__清单 1-5__  使用 NSNib 加载 nib 文件

```objc
- (NSArray*)loadMyNibFile
{
    NSNib*      aNib = [[NSNib alloc] initWithNibNamed:@"MyPanel" bundle:nil];
    NSArray*    topLevelObjs = nil;

    if (![aNib instantiateNibWithOwner:self topLevelObjects:&topLevelObjs])
    {
        NSLog(@"Warning! Could not load nib file.\n");
        return nil;
    }
    // 释放原始的 nib 数据。
    [aNib release];

    // 释放顶层对象，使它们仅由数组持有。
    [topLevelObjs makeObjectsPerformSelector:@selector(release)];

    // 不要对 topLevelObjs 调用 autorelease。
    return topLevelObjs;
}
```


在 iOS 中，可以创建包含 File’s Owner 之外其他占位符对象的 nib 文件。代理对象（proxy object）代表在 nib 文件之外创建、但与 nib 文件内容存在某种连接的对象。代理对象常用于支持 iPhone 应用程序中的导航控制器。使用导航控制器时，你通常会把 File’s Owner 对象连接到某个公共对象上，比如应用程序委托。因此，代理对象代表的是导航控制器对象层次结构中那些已经载入内存的部分，它们要么是以编程方式创建的，要么是从另一个 nib 文件加载的。

你添加到 nib 文件中的每个占位符对象都必须有唯一的名称。要给对象命名，请在 Xcode 中选中该对象并打开检查器窗口。检查器的 Attributes 面板中有一个 Name 字段，用它来为占位符对象指定名称。所取的名称应当能描述该对象的行为或类型，不过实际上你可以随意命名。

当你准备加载包含占位符对象的 nib 文件时，必须在调用 [loadNibNamed:owner:options:](https://developer.apple.com/documentation/foundation/bundle/1618147-loadnibnamed) 方法时为所有代理对象指定替换对象。该方法的 _options_ 参数接受一个包含额外信息的字典。你用这个字典传入占位符对象的信息。该字典必须包含 [UINibExternalObjects](https://developer.apple.com/documentation/uikit/uinibexternalobjects) 键，其值是另一个字典，为每个占位符替换提供名称和对象。

清单 1-6 展示了一个 `applicationDidFinishLaunching:` 方法的示例版本，它手动加载应用程序的主 nib 文件。由于应用程序的委托对象是由 [UIApplicationMain](https://developer.apple.com/documentation/uikit/1622933-uiapplicationmain) 函数创建的，这个方法在主 nib 文件中使用了一个名为 “AppDelegate” 的占位符来代表该对象。proxies 字典保存占位符对象的信息，options 字典再把这个字典包装起来。

__清单 1-6__  替换 nib 文件中的占位符对象

```objc
- (void)applicationDidFinishLaunching:(UIApplication *)application
{
    NSArray*    topLevelObjs = nil;
    NSDictionary*    proxies = [NSDictionary dictionaryWithObject:self forKey:@"AppDelegate"];
    NSDictionary*    options = [NSDictionary dictionaryWithObject:proxies forKey:UINibExternalObjects];

    topLevelObjs = [[NSBundle mainBundle] loadNibNamed:@"Main" owner:self options:options];
    if ([topLevelObjs count] == 0)
    {
        NSLog(@"Warning! Could not load myNib file.\n");
        return;
    }

    // 显示窗口
    [window makeKeyAndVisible];
}
```

关于 `loadNibNamed:owner:options:` 方法的 options 字典的更多信息，请参阅 _NSBundle UIKit Additions Reference_。

nib 文件加载成功后，其内容立即就可以使用。如果你在 File’s Owner 中配置了指向 nib 文件对象的 outlet，现在就可以使用这些 outlet 了。如果没有为 File’s Owner 配置任何 outlet，则应当确保以某种方式获取到顶层对象的引用，以便之后能够释放它们。

由于 outlet 会在 nib 文件加载时被填入真实对象，之后你可以像使用任何以编程方式创建的对象一样使用它们。例如，如果你有一个指向窗口的 outlet，就可以给该窗口发送 [makeKeyAndOrderFront:](https://developer.apple.com/documentation/appkit/nswindow/1419208-makekeyandorderfront) 消息，把它显示到用户屏幕上。当你用完 nib 文件中的对象后，必须像释放其他对象一样释放它们。

OS X 应用程序菜单栏中的菜单项常常需要与许多不同的对象交互，包括应用程序的文档和窗口。问题在于，其中许多对象无法（也不应该）从主 nib 文件直接访问。主 nib 文件的 File’s Owner 总是被设置为 [NSApplication](https://developer.apple.com/documentation/appkit/nsapplication) 类的一个实例。虽然你可以在主 nib 文件中实例化若干自定义对象，但这样做既不实际也没有必要。对于文档对象而言，直接连接到某个特定的文档对象甚至是不可能的，因为文档对象的数量会动态变化，甚至可能为零。

大多数菜单项把 action 消息发送给下列之一：

- 始终处理该命令的固定对象
- 动态对象，比如文档或窗口

给固定对象发送消息是相对直接的过程，通常最好通过应用程序委托来处理。应用程序[委托对象](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14)协助 `NSApplication` 对象运行应用程序，是少数几个理应放在主 nib 文件中的对象之一。如果菜单项对应的是应用程序级别的命令，你可以直接在应用程序委托中实现该命令，或者让委托把消息转发给应用程序中其他合适的对象。

如果某个菜单项作用于最前面窗口的内容，你需要把该菜单项连接到 First Responder 占位符对象上。如果与该菜单项关联的 action 方法是你自己某个对象特有的（而不是由 Cocoa 定义的），你必须先把该 action 添加到 First Responder 上，然后才能建立连接。

建立连接之后，你需要在自定义类中实现该 action 方法。该对象还应当实现 [validateMenuItem:](https://developer.apple.com/documentation/objectivec/nsobject/1518160-validatemenuitem) 方法，以便在恰当的时机启用菜单项。关于响应者链如何处理命令的更多信息，请参阅 _[Cocoa 事件处理指南](../Cocoa%20Event%20Handling%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3da2i)_。

[下一页](String%20Resources.md)[上一页](About%20Resources.md)

