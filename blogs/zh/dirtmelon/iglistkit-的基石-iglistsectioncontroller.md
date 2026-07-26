---
title: IGListKit 的基石 - IGListSectionController
source: dirtmelon
source_key: dirtmelon
source_url: 'https://dirtmelon.github.io/posts/iglistkit-second/'
original_language: zh
published: 2020-12-20
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:48a37f00228dde00'
translated: n/a
---

> 原文：[IGListKit 的基石 - IGListSectionController](https://dirtmelon.github.io/posts/iglistkit-second/)　·　dirtmelon

`IGListSectionController` 跟 `Object` 是一一对应的关系，在 `IGListAdapterDataSource` 的 `listAdapter:sectionControllerForObject:` 方法中，会根据不同的 `Object` 返回不同的 `IGListSectionController` 。它跟我们日常理解的 `UICollectinoView` 的 `Section` 不同，你无法将 `Object` 的数组和 `IGListSectionController` 绑定，如果要将数组绑定到一个 `IGListSectionController` 中，需要将 `Object` 的数组用一个 `Wrapper` 封装起来，再将其和 `IGListSectionController` 绑定。

一般情况下需要对 `IGListSectionController` 进行自定义，通过 `IGListSectionController` 的 `didUpdateToObject:` 方法更新自身的`Object` 。同时 `IGListSectionController` 也提供了与 `Cell` 进行交互的相关方法：

```objc
- (void)didSelectItemAtIndex:(NSInteger)index;
- (void)didDeselectItemAtIndex:(NSInteger)index;
- (void)didHighlightItemAtIndex:(NSInteger)index;
- (void)didUnhighlightItemAtIndex:(NSInteger)index;
```

由于 `IGListSectionController` 自己包含了 `Cell` 的配置（如 `size` ，类型等）和交互，所以 `IGListSectionController` 可以作为一个模块来复用，对于相同的 `Object` ，如果交互和界面都一致，则可以返回相同的 `IGListSectionController` 。同时 `IGListSectionController` 也提供了一些 `Delegate` 和 `DataSource` ，在对应的时机会进行调用。

`id <IGListSupplementaryViewSource> supplementaryViewSource` ，用于配置 `UICollectionView` 每个 `section` 的 `supplementary views` ：

```objc
- (NSArray<NSString *> *)supportedElementKinds;
- (__kindof UICollectionReusableView *)viewForSupplementaryElementOfKind:(NSString *)elementKind
                                                                 atIndex:(NSInteger)index;
- (CGSize)sizeForSupplementaryViewOfKind:(NSString *)elementKind
                                 atIndex:(NSInteger)index;
```

也可以设置 `supplementaryViewSource` 为 `IGListSectionController` 它自己，这样在 `IGListSectionController` 就内部就可以完成 `supplementary views` 的配置，复用时更加方便。

### IGListSectionControllerThreadContext

`IGListSectionController` 在初始化时需要获取到当前的 `UIViewController *viewController` 和 `id <IGListCollectionContext> collectionContext` 。

1. `viewController` 可用于 `push` ， `pop` ， `present` 或者其它自定义转场，对于 `IGListSectionController` 来说，它只知道这是一个 `UIViewController` ，不知道它的具体类型，因为 `IGListSectionController` 是可复用的，我们有可能将其和不同的 `UIViewController` 连接起来，所以其 `viewController` 的类型是不确定的；
2. `collectionContext` 为了对接口进行收敛，限制可以调用的接口，使用了 `protocol` 对其进行抽象， `collectionContext` 本质上是一个 `IGListAdapter` ，但是 `IGListAdapter` 可能有一些我们不需要也不想提供给外界访问的接口，所以借由 `protocol` 来进行抽象。

`IGListKit` 定义了 `IGListSectionControllerThreadContext` ，在 `IGListSectionController` 初始化时对 `viewController` 和 `collectionContext` 进行设置：

```objc
- (instancetype)init {
    if (self = [super init]) {
        IGListSectionControllerThreadContext *context = [threadContextStack() lastObject];
        _viewController = context.viewController;
        _collectionContext = context.collectionContext;

        if (_collectionContext == nil) {
            IGLKLog(@"Warning: Creating %@ outside of -[IGListAdapterDataSource listAdapter:sectionControllerForObject:]. Collection context and view controller will be set later.",
                    NSStringFromClass([self class]));
        }
		  /// ...
    }
    return self;
}
```

由于 `IGListSectionController` 的初始化方法是交给调用方来定义的， `IGListKit` 无法确定 `IGListSectionController` 的初始化参数，同时也为了使得初始化方法尽量简洁，不包含太多参数，使用了 `Thread Dictionary` 来存储所对应的对象，从上面的方法可以看到是通过 `threadContextStack()` 来获取最新的 `IGListSectionControllerThreadContext` ：

```objc
static NSString * const kIGListSectionControllerThreadKey = @"kIGListSectionControllerThreadKey";

static NSMutableArray<IGListSectionControllerThreadContext *> *threadContextStack(void) {
    IGAssertMainThread();
    NSMutableDictionary *threadDictionary = [[NSThread currentThread] threadDictionary];
    NSMutableArray *stack = threadDictionary[kIGListSectionControllerThreadKey];
    if (stack == nil) {
        stack = [NSMutableArray new];
        threadDictionary[kIGListSectionControllerThreadKey] = stack;
    }
    return stack;
}
```

`threadContextStack()` 通过 `[[NSThread currentThread] threadDictionary]` 来获取对应的 `stack` ，而 `push` 和 `pop` 方法则是在 `IGListAdapter` 初始化 `IGListSectionController` 前后调用：

```objc
void IGListSectionControllerPushThread(UIViewController *viewController, id<IGListCollectionContext> collectionContext) {
    IGListSectionControllerThreadContext *context = [IGListSectionControllerThreadContext new];
    context.viewController = viewController;
    context.collectionContext = collectionContext;

    [threadContextStack() addObject:context];
}

void IGListSectionControllerPopThread(void) {
    NSMutableArray *stack = threadContextStack();
    IGAssert(stack.count > 0, @"IGListSectionController thread stack is empty");
    [stack removeLastObject];
}
```

## 子类

### GenericSection

~~为了更好地和 `Swift` 进行交互， `Objective-C` 在 WWDC2015 后也支持了轻量级的范型。~~ 基础的使用方法是指定容器类中对象的类型：

```objc
NSArray <NSString *> strings;
NSDictionary <NSString *, NSNumber *> *dictionary;
```

如果往上面两个指定了类型的容器类对象中添加别的类型的对象，编译器就会显示警告，这更有利于我们写出更加安全和可读的代码。同时，也支持我们自定义自己的范型类， `IGListGenericSectionController` 提供了特定类型的 `IGListSectionController` :

```objc
@interface IGListGenericSectionController<__covariant ObjectType> : IGListSectionController

@property (nonatomic, strong, nullable, readonly) ObjectType object;

- (void)didUpdateToObject:(ObjectType)object NS_REQUIRES_SUPER;

@end
```

作用相当于一个强类型的 `IGListSectionController` ，相关 `issue` ：[Assert generic type in IGListGenericSectionController](https://github.com/Instagram/IGListKit/issues/682)

### SingleSection

对于只有单个 `Cell` 的 `Section` ， `IGListKit` 提供了 `IGListSingleSectionController` ，它通过 `block` 配置 `Cell` 和通过 `Delegate` 来获取点击事件的回调。

```objc
@protocol IGListSingleSectionControllerDelegate <NSObject>

- (void)didSelectSectionController:(IGListSingleSectionController *)sectionController
                        withObject:(id)object;

@optional

- (void)didDeselectSectionController:(IGListSingleSectionController *)sectionController
                          withObject:(id)object;

@end

@interface IGListSingleSectionController : IGListSectionController

- (instancetype)initWithCellClass:(Class)cellClass
                   configureBlock:(IGListSingleSectionCellConfigureBlock)configureBlock
                        sizeBlock:(IGListSingleSectionCellSizeBlock)sizeBlock;

- (instancetype)initWithNibName:(NSString *)nibName
                         bundle:(nullable NSBundle *)bundle
                 configureBlock:(IGListSingleSectionCellConfigureBlock)configureBlock
                      sizeBlock:(IGListSingleSectionCellSizeBlock)sizeBlock;

- (instancetype)initWithStoryboardCellIdentifier:(NSString *)identifier
                                  configureBlock:(IGListSingleSectionCellConfigureBlock)configureBlock
                                       sizeBlock:(IGListSingleSectionCellSizeBlock)sizeBlock;

@property (nonatomic, weak, nullable) id<IGListSingleSectionControllerDelegate> selectionDelegate;
```

### BindingSection

对于 `Section` 的数据流绑定， `IGListKit` 则提供了 `IGListBindingSectionController` 。 `IGListBindingSectionController` 通过 `id<IGListBindingSectionControllerDataSource> dataSource` 的方式把顶层的 `Object` 转换为 `NSArray<id<IGListDiffable>> viewModels` ，然后调用支持 `IGListBindable` 协议的 `Cell` 中的 `bindViewModel:` 方法来刷新 `Cell` 。

如果 `Object` 是跟 `IGListBindingSectionController` 匹配，那么在处理 `IGListDiffable` 协议的方法时需要非常小心。 `IGListDiffable` 通过 `-diffIdentifier` 来判断两个 `Object` 是否为同一个，再通过 `-isEqualToDiffableObject:` 方法来判断 `Object` 是否有更新。由于 `IGListBindingSectionController` 已经在内部消化了 `Object` 的更新逻辑，所以如果是跟 `IGListBindingSectionController` 绑定的 `Object` ，其对应的 `-isEqualToDiffableObject:` 方法应该一直返回 `YES` ：

```objc
- (BOOL)isEqualToDiffableObject:(id)object {
  return YES;
}
```

```swift
 func isEqual(toDiffableObject object: IGListDiffable?) -> Bool {
   return true
 }
```

`IGListBindingSectionController` 内部重写了一些方法，通过 `IGListBindingSectionControllerDataSource` 和 `IGListBindingSectionControllerSelectionDelegate` 来和外部进行交互。

```objc
- (void)didUpdateToObject:(id)object {
    id oldObject = self.object;
    self.object = object;

    if (oldObject == nil) {
        NSArray *viewModels = [self.dataSource sectionController:self viewModelsForObject:object];
        self.viewModels = objectsWithDuplicateIdentifiersRemoved(viewModels);
    } else {
#if defined(IGLK_LOGGING_ENABLED) && IGLK_LOGGING_ENABLED
        if (![oldObject isEqualToDiffableObject:object]) {
            IGLKLog(@"Warning: Unequal objects %@ and %@ will cause IGListBindingSectionController to reload the entire section",
                    oldObject, object);
        }
#endif
        [self updateAnimated:YES completion:nil];
    }
}
```

在 `didUpdateToObject:` 方法中，通过 `dataSource` 返回 `viewModels` ，移除重复部分后设置为 `self.viewModels` 。由于 `IGListBindingSectionController` 在内部处理了 `Object` 的更新逻辑，所以 `didUpdateToObject:` 只会调用一次，如果多次调用且新旧 `Object` 不相等，则表示设置错误，打印一个 `warning` ，但是同时也调用 `updateAnimated:completion:` 更新 `Cell` 。

当对 `Object` 进行修改后，如果需要更新 `Cell` ，调用 `IGListBindingSectionController` 的 `updateAnimated:completion:` 方法：

```objc
- (void)updateAnimated:(BOOL)animated completion:(void (^)(BOOL))completion {
    // 1. 如果不是空闲状态，则直接返回，调用 `completion(NO)` ；
    if (self.state != IGListDiffingSectionStateIdle) {
        if (completion != nil) {
            completion(NO);
        }
        return;
    }
    self.state = IGListDiffingSectionStateUpdateQueued;

    __block IGListIndexSetResult *result = nil;
    __block NSArray<id<IGListDiffable>> *oldViewModels = nil;

    id<IGListCollectionContext> collectionContext = self.collectionContext;
    [self.collectionContext performBatchAnimated:animated updates:^(id<IGListBatchContext> batchContext) {
        if (self.state != IGListDiffingSectionStateUpdateQueued) {
            return;
        }

        oldViewModels = self.viewModels;

        id<IGListDiffable> object = self.object;
        NSArray *newViewModels = [self.dataSource sectionController:self viewModelsForObject:object];
        self.viewModels = objectsWithDuplicateIdentifiersRemoved(newViewModels);
        // 2. 通过 IGListDiff 的算法计算出需要操作的位置
        result = IGListDiff(oldViewModels, self.viewModels, IGListDiffEquality);
        // 3. 遍历 `updates` ，首先获取 `Cell` 所对应的 `index` ，
        // 也就是旧的 `viewModels` 中的 `index` ，通过 `index` 获取到 `Cell` ，
        // 然后使用新的 `index` 获取到新的 `viewModel` ，`Cell` 通过新的 `viewModel` 进行更新
        [result.updates enumerateIndexesUsingBlock:^(NSUInteger oldUpdatedIndex, BOOL *stop) {
            id identifier = [oldViewModels[oldUpdatedIndex] diffIdentifier];
            const NSInteger indexAfterUpdate = [result newIndexForIdentifier:identifier];
            if (indexAfterUpdate != NSNotFound) {
                UICollectionViewCell<IGListBindable> *cell = [collectionContext cellForItemAtIndex:oldUpdatedIndex
                                                                                 sectionController:self];
                [cell bindViewModel:self.viewModels[indexAfterUpdate]];
            }
        }];

        if (IGListExperimentEnabled(self.collectionContext.experiments, IGListExperimentInvalidateLayoutForUpdates)) {
            [batchContext invalidateLayoutInSectionController:self atIndexes:result.updates];
        }
        // 4. 通过 result 进行 `Cell` 的删除/插入
        [batchContext deleteInSectionController:self atIndexes:result.deletes];
        [batchContext insertInSectionController:self atIndexes:result.inserts];

        for (IGListMoveIndex *move in result.moves) {
            [batchContext moveInSectionController:self fromIndex:move.from toIndex:move.to];
        }

        self.state = IGListDiffingSectionStateUpdateApplied;
    } completion:^(BOOL finished) {
        self.state = IGListDiffingSectionStateIdle;
        if (completion != nil) {
            completion(YES);
        }
    }];
}
```

在获取 `Cell` 时， `IGListBindingSectionController` 也会自行进行 `Cell` 和 `Object` 的绑定， `Cell` 需要遵循 `IGListBindable` 协议：

```objc
// protocol IGListBindable
@protocol IGListBindable <NSObject>

- (void)bindViewModel:(id)viewModel;

@end

- (UICollectionViewCell *)cellForItemAtIndex:(NSInteger)index {
    id<IGListDiffable> viewModel = self.viewModels[index];
    UICollectionViewCell<IGListBindable> *cell = [self.dataSource sectionController:self cellForViewModel:viewModel atIndex:index];
    [cell bindViewModel:viewModel];
    return cell;
}
```

从上面的代码可以看到 `IGListBindingSectionController` 也提供了基于 `Cell` 进行局部刷新的能力。

## IGListSectionMap

`IGListSectionMap` 提供了一种在常数时间内对 `Object` 和 `SectionController` 进行互相映射的方式。 主要方法有以下几种：

1. 根据 `section` 返回对应的 `IGListSectionController` ：

```objc
/// 根据 section 返回对应的 IGListSectionController
- (nullable IGListSectionController *)sectionControllerForSection:(NSInteger)section;
/// 根据 section 返回对应的 Object
- (nullable id)objectForSection:(NSInteger)section;
/// 根据 object 返回对应的 IGListSectionController
- (nullable id)sectionControllerForObject:(id)object;
/// 根据 sectionController 返回对应的 Section Index
- (NSInteger)sectionForSectionController:(id)sectionController;
/// 根据 object 返回对应的 Section Index
- (NSInteger)sectionForObject:(id)object;
```

`IGListSectionMap` 内部实现：

```objc
@interface IGListSectionMap ()

@property (nonatomic, strong, readonly, nonnull) NSMapTable<id, IGListSectionController *> *objectToSectionControllerMap;
@property (nonatomic, strong, readonly, nonnull) NSMapTable<IGListSectionController *, NSNumber *> *sectionControllerToSectionMap;

@property (nonatomic, strong, nonnull) NSMutableArray *mObjects;

@end
```

`objectToSectionControllerMap` 提供了 `Object` 到 `sectionController` 的映射， `sectionControllerToSectionMap` 提供了 `sectionController` 到 `section` 的映射， `mObjects` 提供了根据 `section` 返回 `index` 的方法。

`IGListSectionMap` 也提供了接口对属性进行批量更新：

```objc
- (void)updateWithObjects:(NSArray *)objects sectionControllers:(NSArray *)sectionControllers {

    [self reset];

    self.mObjects = [objects mutableCopy];

    id firstObject = objects.firstObject;
    id lastObject = objects.lastObject;

    [objects enumerateObjectsUsingBlock:^(id object, NSUInteger idx, BOOL *stop) {
        IGListSectionController *sectionController = sectionControllers[idx];

        [self.sectionControllerToSectionMap setObject:@(idx) forKey:sectionController];
        [self.objectToSectionControllerMap setObject:sectionController forKey:object];

        sectionController.isFirstSection = (object == firstObject);
        sectionController.isLastSection = (object == lastObject);
        sectionController.section = (NSInteger)idx;
    }];
}
```

清空现有数据主要是对 `IGListSectionController` 相关属性的清理：

```objc
- (void)reset {
    [self enumerateUsingBlock:^(id  _Nonnull object, IGListSectionController * _Nonnull sectionController, NSInteger section, BOOL * _Nonnull stop) {
        sectionController.section = NSNotFound;
        sectionController.isFirstSection = NO;
        sectionController.isLastSection = NO;
    }];

    [self.sectionControllerToSectionMap removeAllObjects];
    [self.objectToSectionControllerMap removeAllObjects];
}
```

## WorkingRange

![workingrange](https://raw.githubusercontent.com/dirtmelon/blog-images/main/workingrange.png)

`Working range` 表示还没出现在屏幕上，但是已经在附近的 `IGListSectionController` ， `IGListSectionController` 可以在进入或者退出 `Working range` 时获取对应的通知，借此可以进行一些准备工作，比如说预先下载图片。 `IGListAdapter` 可以在初始化时指定 `Working range` 的大小：

```swift
let adapter = ListAdapter(updater: ListAdapterUpdater(),
                   viewController: self,
                 workingRangeSize: 1) // 1 before/after visible objects
```

你可以给 `IGListSectionController` 设置 `workingRangeDelegate` 来获取对应的回调。 下面来看看对应的实现， `IGListKit` 内部提供了一个 `IGListWorkingRangeHandler` ，在 `UICollectionViewDelegate` 的 `willDisplay/didEndDisplaying` 方法中调用 `IGListWorkingRangeHandler` 对应的方法：

```objc
- (void)willDisplayItemAtIndexPath:(NSIndexPath *)indexPath
                    forListAdapter:(IGListAdapter *)listAdapter;
- (void)didEndDisplayingItemAtIndexPath:(NSIndexPath *)indexPath
                         forListAdapter:(IGListAdapter *)listAdapter;
```

为了效率更高， `IGListWorkingRangeHandler` 内部是基于 C++ 实现的，内部定义了 `_visibleSectionIndices` 和 `_workingRangeSectionControllers` 两个 `std::unordered_set` 的变量。

```objc
- (void)willDisplayItemAtIndexPath:(NSIndexPath *)indexPath
                    forListAdapter:(IGListAdapter *)listAdapter {
    _visibleSectionIndices.insert({
        .section = indexPath.section,
        .row = indexPath.row,
        .hash = indexPath.hash
    });

    [self _updateWorkingRangesWithListAdapter:listAdapter];
}

- (void)didEndDisplayingItemAtIndexPath:(NSIndexPath *)indexPath
                         forListAdapter:(IGListAdapter *)listAdapter {
    _visibleSectionIndices.erase({
        .section = indexPath.section,
        .row = indexPath.row,
        .hash = indexPath.hash
    });

    [self _updateWorkingRangesWithListAdapter:listAdapter];
}
```

每次更新 `Cell` 的显示隐藏状态时都会更新 `_visibleSectionIndices` ，然后再调用 `_updateWorkingRangesWithListAdapter:` 方法：

```objc
- (void)_updateWorkingRangesWithListAdapter:(IGListAdapter *)listAdapter {
    // 1. 由于需要顺序的 `set` ，所以这里使用了 `std::set` ；
    std::set<NSInteger> visibleSectionSet = std::set<NSInteger>();
    // 2. 插入所有可见的 `section` ；
    for (const _IGListWorkingRangeHandlerIndexPath &indexPath : _visibleSectionIndices) {
        visibleSectionSet.insert(indexPath.section);
    }

    NSInteger start;
    NSInteger end;
    // 3. 计算出开始和结束位置；
    if (visibleSectionSet.size() == 0) {
        start = 0;
        end = 0;
    } else {
        start = MAX(*visibleSectionSet.begin() - _workingRangeSize, 0);
        end = MIN(*visibleSectionSet.rbegin() + 1 + _workingRangeSize, (NSInteger)listAdapter.objects.count);
    }

    // 4. 创建新的 `workingRangeSectionControllers` ；
    _IGListWorkingRangeSectionControllerSet workingRangeSectionControllers (visibleSectionSet.size());
    for (NSInteger idx = start; idx < end; idx++) {
        id item = [listAdapter objectAtSection:idx];
        IGListSectionController *sectionController = [listAdapter sectionControllerForObject:item];
        workingRangeSectionControllers.insert({sectionController});
    }

    // 5. 遍历新的 `workingRangeSectionControllers` ，如果不在旧的 `_workingRangeSectionControllers` 中，
    // 则表示这个 `sectionController` 是新加入的，调用 `sectionControllerWillEnterWorkingRange` ；
    for (const _IGListWorkingRangeHandlerSectionControllerWrapper &wrapper : workingRangeSectionControllers) {
        auto it = _workingRangeSectionControllers.find(wrapper);
        if (it == _workingRangeSectionControllers.end()) {
            id <IGListWorkingRangeDelegate> workingRangeDelegate = wrapper.sectionController.workingRangeDelegate;
            [workingRangeDelegate listAdapter:listAdapter sectionControllerWillEnterWorkingRange:wrapper.sectionController];
        }
    }

    // 6. 遍历旧的 `_workingRangeSectionControllers` ，如果不在新的 `workingRangeSectionControllers` 中，
    // 则表示这个 `sectionController` 是已退出的，调用 `sectionControllerDidExitWorkingRange` ；
    for (const _IGListWorkingRangeHandlerSectionControllerWrapper &wrapper : _workingRangeSectionControllers) {
        auto it = workingRangeSectionControllers.find(wrapper);
        if (it == workingRangeSectionControllers.end()) {
            id <IGListWorkingRangeDelegate> workingRangeDelegate = wrapper.sectionController.workingRangeDelegate;
            [workingRangeDelegate listAdapter:listAdapter sectionControllerDidExitWorkingRange:wrapper.sectionController];
        }
    }

    _workingRangeSectionControllers = workingRangeSectionControllers;
}
```

可以看到由于 workingRange 是以 Section 为单位，所以无法提供精细到 Cell 级别的预处理。这也是基于 SectionController 进行处理的缺点。

## DisplayHandler

`IGListDisplayHandler` 是 `IGListKit` 内部用于处理 `Cell` 显示/消失在屏幕上的相关事件。 `IGListAdapter` 在 `UICollectionViewDelegate` 的 `willDisplay/didEndDisplaying` 方法中调用 `IGListDisplayHandler` 对应的方法：

```objc
- (void)willDisplayCell:(UICollectionViewCell *)cell
         forListAdapter:(IGListAdapter *)listAdapter
      sectionController:(IGListSectionController *)sectionController
                 object:(id)object
              indexPath:(NSIndexPath *)indexPath;
- (void)didEndDisplayingCell:(UICollectionViewCell *)cell
              forListAdapter:(IGListAdapter *)listAdapter
           sectionController:(IGListSectionController *)sectionController
                   indexPath:(NSIndexPath *)indexPath;
- (void)willDisplaySupplementaryView:(UICollectionReusableView *)view
                      forListAdapter:(IGListAdapter *)listAdapter
                   sectionController:(IGListSectionController *)sectionController
                              object:(id)object
                           indexPath:(NSIndexPath *)indexPath;
- (void)didEndDisplayingSupplementaryView:(UICollectionReusableView *)view
                           forListAdapter:(IGListAdapter *)listAdapter
                        sectionController:(IGListSectionController *)sectionController
                                indexPath:(NSIndexPath *)indexPath;
```

`IGListDisplayHandler` 内部使用了 `NSCountedSet<IGListSectionController *> *visibleListSections` 来记录可见的 `IGListSectionController` ，跟 `NSMutableSet` 的不同之处在于， `NSCountedSet` 会记录每个 `Object` 添加的次数。 `IGListDisplayHandler` 还定义了一个 `NSMapTable *visibleViewObjectMap` 属性，用于处理 `UICollectionReusableView` 跟 `Object` 的对应关系。

`_pluckObjectForView:` 移除并返回 `UICollectionReusableView` 对应的 `Object` ：

```objc
- (id)_pluckObjectForView:(UICollectionReusableView *)view {
    NSMapTable *viewObjectMap = self.visibleViewObjectMap;
    id object = [viewObjectMap objectForKey:view];
    [viewObjectMap removeObjectForKey:view];
    return object;
}
```

`IGListDisplayHandler` 内部的 `willDisplay` 代码如下：

```objc
- (void)_willDisplayReusableView:(UICollectionReusableView *)view
                 forListAdapter:(IGListAdapter *)listAdapter
              sectionController:(IGListSectionController *)sectionController
                         object:(id)object
                      indexPath:(NSIndexPath *)indexPath {
    [self.visibleViewObjectMap setObject:object forKey:view];
    NSCountedSet *visibleListSections = self.visibleListSections;
    if ([visibleListSections countForObject:sectionController] == 0) {
        [sectionController willDisplaySectionControllerWithListAdapter:listAdapter];
        [listAdapter.delegate listAdapter:listAdapter willDisplayObject:object atIndex:indexPath.section];
    }
    [visibleListSections addObject:sectionController];
}
```

在 `willDisplay` 的处理中，如果 `countForObject` 为 0 则表示该 `sectionController` 即将要进入屏幕，随后调用 `sectionController` 和 `listAdapter.delegate` 的方法。然后可以看到调用 `[visibleListSections addObject:]` 添加对应的 `sectionController` ，由于 `visibleListSections` 是 `NSCountedSet` ，所以会记录 `sectionController` 的次数，可以配合后续的 `didEndingDisplay` 操作。

```objc
- (void)_didEndDisplayingReusableView:(UICollectionReusableView *)view
                      forListAdapter:(IGListAdapter *)listAdapter
                   sectionController:(IGListSectionController *)sectionController
                              object:(id)object
                           indexPath:(NSIndexPath *)indexPath {
    if (object == nil || sectionController == nil) {
        return;
    }

    const NSInteger section = indexPath.section;

    NSCountedSet *visibleSections = self.visibleListSections;
    [visibleSections removeObject:sectionController];

    if ([visibleSections countForObject:sectionController] == 0) {
        [sectionController didEndDisplayingSectionControllerWithListAdapter:listAdapter];
        [listAdapter.delegate listAdapter:listAdapter didEndDisplayingObject:object atIndex:section];
    }
}
```

可以看到在 `didEndDisplaying` 时， `visibleSections` 每次 `removeObject:sectionController` 都会使得 `sectionController` 的计数减一，只有当计数为 0 时才调用 `sectionController` 和 `listAdapter.delegate` 对应的方法。

`IGListDisplayHandler` 的内部实现为 `willDisplay/didEndDisplaying` 提供了两个层级的入口：

1. `IGListAdapter` 级别，通过设置 `adapter` 的 `id <IGListAdapterDelegate> delegate` ，可以获取整个 `UICollectionView` 的回调；
2. `IGListSectionController` ，通过设置 `id <IGListDisplayDelegate> displayDelegate` ，可以获取具体到某个 `sectionController` 的回调。也支持设置 `displayDelegate` 为 `IGListSectionController` 它自己，由于 `IGListSectionController` 跟 `Object` 是绑定的，所以在处理不同的 `ViewController` 中相同的 `Object` 时，我们不仅可以复用 `IGListSectionController` ，也可以复用 `displayDelegate` 的配置，进行一些曝光时长的统一配置。

## 总结

可以看到 `IGListSectionController` 作为 `IGListKit` 的基石，直接和数据层进行绑定，而且 `IGListKit` 还通过 `IGListSectionController` 进行各种扩展，支持以下特性：

- 支持范型特性，设置指定的数据类型；
- 支持快捷只显示单个 `Cell` 的 `Section` ；
- 支持数据流绑定， `Section` 内根据不同的数据刷新不同的 `Cell` ；
- 支持预处理，预处理的范围也可以进行设置；
- 支持设置显示时的相关回调，且可以基于 `IGListSectionController` 的层级进行操作。
