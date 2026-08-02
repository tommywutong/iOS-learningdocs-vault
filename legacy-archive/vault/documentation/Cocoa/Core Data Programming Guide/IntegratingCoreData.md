---
title: Core Data 编程指南
apple_id: TP40001075
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreData
published: '2017-03-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/IntegratingCoreData.html
archived_at: '2026-07-15T07:14:21.045124Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Core Data 编程指南](index.md)



## 在 iOS 启动时集成 Core Data

在 iOS 和 macOS 中，应用程序生命周期的起始阶段存在细微的差别。

当 macOS 应用程序启动耗时异常长、变得无响应时，操作系统会改变光标以指示这种状态。用户可以选择等待应用程序启动完成，或者直接退出该应用程序。

在 iOS 中，不存在这样的概念。如果一个应用没有在有限的时间内完成启动，操作系统会终止该应用程序。因此，应用程序尽快完成启动流程至关重要。

另一方面，你也希望应用程序能够尽快访问 Core Data 中的数据，这通常意味着要在应用程序生命周期的最早阶段之一就初始化 Core Data。尽管并不常见，但 Core Data 有时完成初始化所需的时间会比平常更长。

因此，建议将 iOS 应用的启动流程拆分为两个阶段，以避免应用被终止：

1. 一个最小化的启动阶段，向用户表明应用程序正在启动
2. 在 Core Data 完成初始化之后，再完成应用程序界面的加载

### 在 iOS 中初始化 Core Data

第一步是改变 [application:didFinishLaunchingWithOptions:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application) 方法的实现方式。在 `application:didFinishLaunchingWithOptions:` 方法中，考虑只初始化 Core Data，而尽量不做其他事情。如果你使用的是 storyboard，可以在这个方法执行期间继续显示启动图。

作为 Core Data 初始化的一部分，将持久化存储（[NSPersistentStore](https://developer.apple.com/documentation/coredata/nspersistentstore)）添加到持久化存储协调器（[NSPersistentStoreCoordinator](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator)）的操作，应交由后台队列执行。这个操作耗时不定，如果在主队列上执行，可能会阻塞用户界面，甚至可能导致应用程序被终止。

一旦持久化存储被添加到持久化存储协调器中，你就可以回调到主队列，请求完成并显示用户界面。

### 将 Core Data 与应用程序委托分离

在早期的 iOS 中，Core Data 栈通常在应用程序委托内部进行初始化。然而，这样做会导致大量代码与应用程序生命周期事件混杂在一起。

在自己的顶层控制器对象中创建 Core Data 栈，并配置应用程序去初始化该控制器对象并持有一个对它的引用。这样做有助于将 Core Data 相关代码整合到其自身的控制器中，同时使应用程序委托保持相对整洁。这种独立控制器的设计方式在 [初始化 Core Data 栈](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/InitializingtheCoreDataStack.html#//apple_ref/doc/uid/TP40001075-CH4-SW1) 中有详细说明。

要将 [初始化 Core Data 栈](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/InitializingtheCoreDataStack.html#//apple_ref/doc/uid/TP40001075-CH4-SW1) 一节中的代码整合到 iOS 应用中，需要在应用程序委托中添加一个属性，并在 `applicationDidFinishLaunching` 生命周期方法中初始化该控制器：

Objective-C

1. `@interface AppDelegate : UIResponder <UIApplicationDelegate>`
3. `@property (strong, nonatomic) UIWindow *window;`
4. `@property (strong, nonatomic) DataController *dataController;`
6. `@end`
8. `@implementation AppDelegate`
10. `- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions`
11. `{`
12. `[self setDataController:[[DataController alloc] initWithCompletionBlock:^{`
13. `//Complete user interface initialization`
14. `}]];`
15. `return YES;`
16. `}`
18. `@end`

Swift

1. `class AppDelegate: UIResponder, UIApplicationDelegate {`
3. `var window: UIWindow?`
4. `var dataController: DataController!`
6. `func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey : Any]? = nil) -> Bool {`
7. `dataController = DataController() {`
8. `//Complete user interface initialization`
9. `}`
10. `return true`
11. `}`

通过初始化一个独立的控制器对象，你将 Core Data 栈移出了应用程序委托，同时仍然允许应用程序的各处访问 Core Data。

[将模型连接到视图](nsfetchedresultscontroller.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzvfvbuqobnknltc)

[将 Core Data 与 Storyboard 集成](CoreDataandStoryboards.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzvfvbuqmjqfvjvomi)
