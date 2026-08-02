---
title: Core Data 编程指南
apple_id: TP40001075
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreData
published: '2017-03-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/nsfetchedresultscontroller.html
archived_at: '2026-07-15T07:14:28.880229Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Core Data 编程指南](index.md)



## 将模型连接到视图

在 macOS 中，Core Data 被设计为通过 Cocoa Bindings 与用户界面协作。但在 iOS 中，Cocoa Bindings 并不属于用户界面的一部分。在 iOS 中，你使用 [NSFetchedResultsController](https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller) 将模型（Core Data）与视图（storyboard）连接起来。

### 创建结果获取控制器

当你在基于 UITableView 的布局中使用 Core Data 时，你数据的 `NSFetchedResultsController` 通常由将要使用该数据的 [UITableViewController](https://developer.apple.com/documentation/uikit/uitableviewcontroller) 实例进行初始化。这个初始化过程可以放在 [viewDidLoad](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621495-viewdidload) 或 [viewWillAppear:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621510-viewwillappear) 方法中，或者放在该视图控制器生命周期中其他合适的时机。

以下示例展示了 `NSFetchedResultsController` 的初始化过程。

Objective-C

1. `@property (nonatomic, strong) NSFetchedResultsController *fetchedResultsController;`
3. `- (void)initializeFetchedResultsController`
4. `{`
5. `NSFetchRequest *request = [NSFetchRequest fetchRequestWithEntityName:@"Person"];`
7. `NSSortDescriptor *lastNameSort = [NSSortDescriptor sortDescriptorWithKey:@"lastName" ascending:YES];`
9. `[request setSortDescriptors:@[lastNameSort]];`
11. `NSManagedObjectContext *moc = …; //Retrieve the main queue NSManagedObjectContext`
13. `[self setFetchedResultsController:[[NSFetchedResultsController alloc] initWithFetchRequest:request managedObjectContext:moc sectionNameKeyPath:nil cacheName:nil]];`
14. `[[self fetchedResultsController] setDelegate:self];`
16. `NSError *error = nil;`
17. `if (![[self fetchedResultsController] performFetch:&error]) {`
18. `NSLog(@"Failed to initialize FetchedResultsController: %@\n%@", [error localizedDescription], [error userInfo]);`
19. `abort();`
20. `}`
21. `}`

Swift

1. `var fetchedResultsController: NSFetchedResultsController!`
3. `func initializeFetchedResultsController() {`
4. `let request = NSFetchRequest(entityName: "Person")`
5. `let departmentSort = NSSortDescriptor(key: "department.name", ascending: true)`
6. `let lastNameSort = NSSortDescriptor(key: "lastName", ascending: true)`
7. `request.sortDescriptors = [departmentSort, lastNameSort]`
9. `let moc = dataController.managedObjectContext`
10. `fetchedResultsController = NSFetchedResultsController(fetchRequest: request, managedObjectContext: moc, sectionNameKeyPath: nil, cacheName: nil)`
11. `fetchedResultsController.delegate = self`
13. `do {`
14. `try fetchedResultsController.performFetch()`
15. `} catch {`
16. `fatalError("Failed to initialize FetchedResultsController: \(error)")`
17. `}`
18. `}`

在上面这个位于控制该表格的 `UITableViewController` 实例内部的 `initializeFetchedResultsController` 方法中，你首先构造了一个获取请求（`NSFetchRequest`），它是 `NSFetchedResultsController` 的核心所在。请注意，该获取请求包含一个排序描述符（[NSSortDescriptor](https://developer.apple.com/documentation/foundation/nssortdescriptor)）。`NSFetchedResultsController` 至少需要一个排序描述符，来控制所展示数据的顺序。

在初始化好获取请求后，你就可以初始化 `NSFetchedResultsController` 实例。该结果获取控制器要求你向其传入一个 `NSFetchRequest` 实例，以及要在其上执行该获取的托管对象上下文（[NSManagedObjectContext](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext)）的引用。[sectionNameKeyPath](https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller/1622285-sectionnamekeypath) 和 [cacheName](https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller/1622280-cachename) 这两个属性都是可选的。

在结果获取控制器初始化完成后，你需要为它指定一个委托。当底层数据结构发生任何变化时，该委托会通知表格视图控制器。通常，表格视图控制器同时也是该结果获取控制器的委托，这样它就可以在底层数据发生变化时接收到相应的回调。

接下来，通过调用 [performFetch:](https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller/1622305-performfetch) 来启动 `NSFetchedResultsController`。该调用会获取要展示的初始数据，并使 `NSFetchedResultsController` 实例开始监控该托管对象上下文的变化。

### 将结果获取控制器与表格视图数据源集成

在完成结果获取控制器的初始化、并准备好要在表格视图中展示的数据后，你需要将该结果获取控制器与表格视图数据源（[UITableViewDataSource](https://developer.apple.com/documentation/uikit/uitableviewdatasource)）集成起来。

Objective-C

1. `#pragma mark - UITableViewDataSource`
3. `- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath`
4. `{`
5. `id cell = [tableView dequeueReusableCellWithIdentifier:CellReuseIdentifier];`
7. `NSManagedObject *object = [self.fetchedResultsController objectAtIndexPath:indexPath];`
8. `// Configure the cell from the object`
9. `return cell;`
10. `}`
12. `- (NSInteger)numberOfSectionsInTableView:(UITableView *)tableView`
13. `{`
14. `return [[[self fetchedResultsController] sections] count];`
15. `}`
17. `- (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section`
18. `{`
19. `id< NSFetchedResultsSectionInfo> sectionInfo = [[self fetchedResultsController] sections][section];`
20. `return [sectionInfo numberOfObjects];`
21. `}`

Swift

1. `override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {`
2. `guard let cell = tableView.dequeueReusableCell(withIdentifier: "cellIdentifier", for: indexPath) else {`
3. `fatalError("Wrong cell type dequeued")`
4. `}`
5. `// Set up the cell`
6. `guard let object = self.fetchedResultsController?.object(at: indexPath) else {`
7. `fatalError("Attempt to configure cell without a managed object")`
8. `}`
9. `//Populate the cell from the object`
10. `return cell`
11. `}`
13. `override func numberOfSectionsInTableView(tableView: UITableView) -> Int {`
14. `return fetchedResultsController.sections!.count`
15. `}`
17. `override func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -> Int {`
18. `guard let sections = fetchedResultsController.sections else {`
19. `fatalError("No sections in fetchedResultsController")`
20. `}`
21. `let sectionInfo = sections[section]`
22. `return sectionInfo.numberOfObjects`
23. `}`

正如上面每个 `UITableViewDataSource` 方法所示，与结果获取控制器的集成，都被简化为对某个专门为集成表格视图数据源而设计的方法的单次调用。

### 将数据变化通知给表格视图

除了大大简化了 Core Data 与表格视图数据源的集成之外，`NSFetchedResultsController` 还会在数据发生变化时，负责与 `UITableViewController` 实例进行通信。要启用这一特性，需要实现 [NSFetchedResultsControllerDelegate](https://developer.apple.com/documentation/coredata/nsfetchedresultscontrollerdelegate) 协议：

Objective-C

1. `#pragma mark - NSFetchedResultsControllerDelegate`
2. `- (void)controllerWillChangeContent:(NSFetchedResultsController *)controller`
3. `{`
4. `[[self tableView] beginUpdates];`
5. `}`
6. `- (void)controller:(NSFetchedResultsController *)controller didChangeSection:(id <NSFetchedResultsSectionInfo>)sectionInfo atIndex:(NSUInteger)sectionIndex forChangeType:(NSFetchedResultsChangeType)type`
7. `{`
8. `switch(type) {`
9. `case NSFetchedResultsChangeInsert:`
10. `[[self tableView] insertSections:[NSIndexSet indexSetWithIndex:sectionIndex] withRowAnimation:UITableViewRowAnimationFade];`
11. `break;`
12. `case NSFetchedResultsChangeDelete:`
13. `[[self tableView] deleteSections:[NSIndexSet indexSetWithIndex:sectionIndex] withRowAnimation:UITableViewRowAnimationFade];`
14. `break;`
15. `case NSFetchedResultsChangeMove:`
16. `case NSFetchedResultsChangeUpdate:`
17. `break;`
18. `}`
19. `}`
20. `- (void)controller:(NSFetchedResultsController *)controller didChangeObject:(id)anObject atIndexPath:(NSIndexPath *)indexPath forChangeType:(NSFetchedResultsChangeType)type newIndexPath:(NSIndexPath *)newIndexPath`
21. `{`
22. `switch(type) {`
23. `case NSFetchedResultsChangeInsert:`
24. `[[self tableView] insertRowsAtIndexPaths:@[newIndexPath] withRowAnimation:UITableViewRowAnimationFade];`
25. `break;`
26. `case NSFetchedResultsChangeDelete:`
27. `[[self tableView] deleteRowsAtIndexPaths:@[indexPath] withRowAnimation:UITableViewRowAnimationFade];`
28. `break;`
29. `case NSFetchedResultsChangeUpdate:`
30. `[self.tableView reloadRowsAtIndexPaths:@[indexPath] withRowAnimation:UITableViewRowAnimationFade];`
31. `break;`
32. `case NSFetchedResultsChangeMove:`
33. `[[self tableView] deleteRowsAtIndexPaths:@[indexPath] withRowAnimation:UITableViewRowAnimationFade];`
34. `[[self tableView] insertRowsAtIndexPaths:@[newIndexPath] withRowAnimation:UITableViewRowAnimationFade];`
35. `break;`
36. `}`
37. `}`
38. `- (void)controllerDidChangeContent:(NSFetchedResultsController *)controller`
39. `{`
40. `[[self tableView] endUpdates];`
41. `}`

Swift

1. `func controllerWillChangeContent(_ controller: NSFetchedResultsController<NSFetchRequestResult>) {`
2. `tableView.beginUpdates()`
3. `}`
5. `func controller(_ controller: NSFetchedResultsController<NSFetchRequestResult>, didChange sectionInfo: NSFetchedResultsSectionInfo, atSectionIndex sectionIndex: Int, for type: NSFetchedResultsChangeType) {`
6. `switch type {`
7. `case .insert:`
8. `tableView.insertSections(IndexSet(integer: sectionIndex), with: .fade)`
9. `case .delete:`
10. `tableView.deleteSections(IndexSet(integer: sectionIndex), with: .fade)`
11. `case .move:`
12. `break`
13. `case .update:`
14. `break`
15. `}`
16. `}`
18. `func controller(_ controller: NSFetchedResultsController<NSFetchRequestResult>, didChange anObject: Any, at indexPath: IndexPath?, for type: NSFetchedResultsChangeType, newIndexPath: IndexPath?) {`
19. `switch type {`
20. `case .insert:`
21. `tableView.insertRows(at: [newIndexPath!], with: .fade)`
22. `case .delete:`
23. `tableView.deleteRows(at: [indexPath!], with: .fade)`
24. `case .update:`
25. `tableView.reloadRows(at: [indexPath!], with: .fade)`
26. `case .move:`
27. `tableView.moveRow(at: indexPath!, to: newIndexPath!)`
28. `}`
29. `}`
31. `func controllerDidChangeContent(_ controller: NSFetchedResultsController<NSFetchRequestResult>) {`
32. `tableView.endUpdates()`
33. `}`

实现上面这四个协议方法后，每当底层数据发生变化时，相关联的 `UITableView` 就会自动获得更新。

### 添加分区

到目前为止，你一直在处理的是只有一个分区（section）的表格视图，这个分区代表了需要在该表格视图中展示的全部数据。如果你处理的是大量的 Employee 对象，把表格视图划分为多个分区会更有优势。按部门对员工进行分组，能让员工列表更便于管理。如果不使用 Core Data，一个具有多个分区的表格视图，将需要用到一个"数组的数组"，或者更复杂的数据结构。而使用 Core Data，你只需对结果获取控制器的构造方式做一个简单的修改即可。

Objective-C

1. `- (void)initializeFetchedResultsController`
2. `{`
3. `NSFetchRequest *request = [NSFetchRequest fetchRequestWithEntityName:@"Person"];`
4. `NSSortDescriptor *departmentSort = [NSSortDescriptor sortDescriptorWithKey:@"department.name" ascending:YES];`
5. `NSSortDescriptor *lastNameSort = [NSSortDescriptor sortDescriptorWithKey:@"lastName" ascending:YES];`
6. `[request setSortDescriptors:@[departmentSort, lastNameSort]];`
7. `NSManagedObjectContext *moc = [[self dataController] managedObjectContext];`
8. `[self setFetchedResultsController:[[NSFetchedResultsController alloc] initWithFetchRequest:request managedObjectContext:moc sectionNameKeyPath:@"department.name" cacheName:nil]];`
9. `[[self fetchedResultsController] setDelegate:self];`
10. `}`

Swift

1. `func initializeFetchedResultsController() {`
2. `let request = NSFetchRequest(entityName: "Person")`
3. `let departmentSort = NSSortDescriptor(key: "department.name", ascending: true)`
4. `let lastNameSort = NSSortDescriptor(key: "lastName", ascending: true)`
5. `request.sortDescriptors = [departmentSort, lastNameSort]`
6. `let moc = dataController.managedObjectContext`
7. `fetchedResultsController = NSFetchedResultsController(fetchRequest: request, managedObjectContext: moc, sectionNameKeyPath: "department.name", cacheName: nil)`
8. `fetchedResultsController.delegate = self`
9. `do {`
10. `try fetchedResultsController.performFetch()`
11. `} catch {`
12. `fatalError("Failed to initialize FetchedResultsController: \(error)")`
13. `}`
14. `}`

在这个例子中，你为 `NSFetchRequest` 实例又添加了一个 `NSSortDescriptor` 实例。你在初始化 `NSFetchedResultsController` 时，将这个新排序描述符所使用的同一个键，设置为 `sectionNameKeyPath`。结果获取控制器会使用这个初始排序描述符，将数据拆分为多个分区，因此要求这两处的键必须一致。

这个改动会使结果获取控制器根据每个 Person 实例所关联部门的名称，将返回的 Person 实例拆分到多个分区中。使用这一特性只有以下几个条件：

- `sectionNameKeyPath` 属性所对应的必须也是一个 `NSSortDescriptor` 实例。
- 该 `NSSortDescriptor` 必须是传给获取请求的数组中的第一个描述符。

### 添加缓存以提升性能

在许多情况下，表格视图所表示的数据相对静态。获取请求是在表格视图控制器创建时定义的，并且在应用程序的整个生命周期中都不会改变。在这类情况下，为 `NSFetchedResultsController` 实例添加缓存会很有优势，这样当应用程序再次启动、且数据未发生变化时，表格视图就能瞬间完成初始化。缓存对于展示异常庞大的数据集尤其有用。

Objective-C

1. `[self setFetchedResultsController:[[NSFetchedResultsController alloc] initWithFetchRequest:request managedObjectContext:moc sectionNameKeyPath:@"department.name" cacheName:@"rootCache"]];`

Swift

1. `fetchedResultsController = NSFetchedResultsController(fetchRequest: request, managedObjectContext: moc, sectionNameKeyPath: "department.name", cacheName: "rootCache")`

如上所示，`cacheName` 属性是在初始化 `NSFetchedResultsController` 实例时设置的，此后该结果获取控制器会自动获得一个缓存。此后再加载数据时，几乎可以瞬间完成。

> [!NOTE]
> 

[Creating and Modifying Custom Managed Objects](LifeofaManagedObject.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzvfvbuqmjwfvjvomi)

[Integrating Core Data at iOS Startup](IntegratingCoreData.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzvfvbuqojnknltc)
