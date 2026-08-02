---
title: Core Data 编程指南
apple_id: TP40001075
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreData
published: '2017-03-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/CoreDataandStoryboards.html
archived_at: '2026-07-15T07:14:13.015358Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Core Data 编程指南](index.md)



## 将 Core Data 与 Storyboard 集成

Core Data 能与你用来构建界面的 Xcode storyboard 功能很好地集成。这种集成让你能够利用依赖注入这一模式。依赖注入是一种控制反转；它允许框架的调用者通过向被调用的对象传入引用来控制流程。依赖注入是 Cocoa 开发（尤其是 iOS Cocoa 开发）中偏好使用的模式之一。

### 通过 Storyboard Segue 集成 Core Data

Core Data 与 storyboard 集成中一个较为复杂的环节，是从显示大量数据对象的表视图，过渡到展示其中某一项详情的子视图控制器。如果不使用 storyboard，你会通过重写 [UITableViewDelegate](https://developer.apple.com/documentation/uikit/uitableviewdelegate) 的 [tableView:didSelectRowAtIndexPath:](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614877-tableview) 方法来完成这一过渡。但如果使用 storyboard，就不应使用这个方法，过渡应改为在 [prepareForSegue:sender:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621490-prepareforsegue) 方法中处理。

为了演示如何将 Core Data 与 storyboard segue 集成，来看下面这个示例：一个主视图控制器是包含员工列表的表视图。当列表中的某个员工被选中时，你希望展示该员工的详情视图。这里假设 segue 所指向的视图控制器有一个属性用来接收被选中的 [NSManagedObject](https://developer.apple.com/documentation/coredata/nsmanagedobject)。

Objective-C

1. `@interface DetailViewController : UIViewController`
3. `@property (weak) AAAEmployeeMO *employee;`
5. `@end`

Swift

1. `class DetailViewController: UIViewController {`
3. `weak var employee: EmployeeMO?`
5. `}`

> [!NOTE]
> 

接下来，你要在主视图控制器中实现 [prepareForSegue:sender:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621490-prepareforsegue) 方法，以便在 segue 过程中传递相应的 `NSManagedObject` 实例：

Objective-C

1. `#define CellDetailIdentifier @"CellDetailIdentifier"`
3. `- (void)prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender`
4. `{`
5. `id destination = [segue destinationViewController];`
6. `if ([[segue identifier] isEqualToString:CellDetailIdentifier]) {`
7. `NSIndexPath *indexPath = [[self tableView] indexPathForSelectedRow];`
8. `id selectedObject = [[self fetchedResultsController] objectAtIndexPath:indexPath];`
9. `[destination setEmployee:selectedObject];`
10. `return;`
11. `}`
12. `}`

Swift

1. `let CellDetailIdentifier = "CellDetailIdentifier"`
3. `override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {`
4. `switch segue.identifier! {`
5. `case CellDetailIdentifier:`
6. `let destination = segue.destinationViewController as! DetailViewController`
7. `let indexPath = tableView.indexPathForSelectedRow!`
8. `let selectedObject = fetchedResultsController.objectAtIndexPath(indexPath) as! EmployeeMO`
9. `destination.employee = selectedObject`
10. `default:`
11. `print("Unknown segue: \(segue.identifier)")`
12. `}`
13. `}`

从 segue 中取得 segue 标识符（在一个 storyboard 中，每个 segue 的标识符都要求是唯一的）之后，你就可以确信目标视图控制器是什么类型，并把被选中的 Employee 实例的引用传递给目标视图控制器。目标视图控制器随后会在其生命周期的加载阶段获得这个引用，并展示与之关联的数据。这就是依赖注入的体现：父视图控制器通过决定把哪个 Employee 实例交给目标视图控制器，来控制应用的流程。

[Integrating Core Data at iOS Startup](IntegratingCoreData.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzvfvbuqojnknltc)

[Using Core Data with Cocoa Bindings](CocoaBindings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzvfvbuqmjsfvjvomi)
