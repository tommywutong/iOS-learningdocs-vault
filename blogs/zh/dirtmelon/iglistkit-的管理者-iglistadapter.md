---
title: IGListKit 的管理者 - IGListAdapter
source: dirtmelon
source_key: dirtmelon
source_url: 'https://dirtmelon.github.io/posts/iglistkit-third/'
original_language: zh
published: 2020-12-27
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:78e032804a85fc18'
translated: n/a
---

> 原文：[IGListKit 的管理者 - IGListAdapter](https://dirtmelon.github.io/posts/iglistkit-third/)　·　dirtmelon

## 初始化

`IGListAdapter` 负责处理 `UICollectionView` 的 `DataSource` 和 `Delegate` ，所有 `DataSource/Delegate` 的相关方法都会在 `IGListAdapter` 内部消化完毕，调用方只需要设置 `IGListAdapter` 的 `dataSource` 和 `collectionView` 即可， `IGListAdapterDataSource ` 则负责给 `IGListAdapter` 提供数据源：

```objc
@protocol IGListAdapterDataSource <NSObject>

/// 根据不同的 adapter 返回需要展示在列表中的数据，一般情况下每个 UIViewController 只有一个 adapter
- (NSArray<id <IGListDiffable>> *)objectsForListAdapter:(IGListAdapter *)listAdapter;

/// 根据数据来返回新生成的对应的 IGListSectionController
/// IGListSectionController 应该在这里进行初始化，你也可以在这里传递其它数据给 IGListSectionController 。
/// 当 IGListAdapter 被创建，更新或者重新加载（ reloaded ）时，会初始化所有数据对应的 IGListSectionController 。
/// IGListSectionController 会进行复用，可以通过 `-[IGListDiffable diffIdentifier]` 来阻止。
- (IGListSectionController *)listAdapter:(IGListAdapter *)listAdapter sectionControllerForObject:(id)object;

/// 当 UICollectionView 数据为空时就会显示这个方法返回的 UIView ，如果不想显示，可以直接返回 `nil` 。
- (nullable UIView *)emptyViewForListAdapter:(IGListAdapter *)listAdapter;

@end
```

`IGListAdapterDataSource` 作用和 `UICollectionViewDataSource` 类似，只不过设置对象变成了 `IGListAdapterDataSource` ，而且只需要提供数据源和 `IGListSectionController` 即可，不需要进行其它配置。

下面来看下 `IGListAdapter` 的初始化方法：

```objc
- (instancetype)initWithUpdater:(id <IGListUpdatingDelegate>)updater
                 viewController:(UIViewController *)viewController
               workingRangeSize:(NSInteger)workingRangeSize {
    IGAssertMainThread();
    IGParameterAssert(updater);

    if (self = [super init]) {
		  // 1. 使用了 `NSMapTable` 而不是 `NSDictionary` ，因为这里的 `key` 是 `id<IGListDiffable>`  对象，不支持 `NSCopying` 协议，
        // 所以使用 `NSMapTable` ，通过 `id <IGListUpdatingDelegate>` 的 `objectLookupPointerFunctions` 方法来自定义 `hashFunction` 和 `isEqualFunction` ：
        NSPointerFunctions *keyFunctions = [updater objectLookupPointerFunctions];
        NSPointerFunctions *valueFunctions = [NSPointerFunctions pointerFunctionsWithOptions:NSPointerFunctionsStrongMemory];
        NSMapTable *table = [[NSMapTable alloc] initWithKeyPointerFunctions:keyFunctions valuePointerFunctions:valueFunctions capacity:0];
        _sectionMap = [[IGListSectionMap alloc] initWithMapTable:table];
	      // 2. `IGListDisplayHandler` ，提供 `UICollectionViewCell` 和  `UICollectionReusableView` 显示/隐藏相关的生命周期方法，内部调用 `IGListSectionController` 对应的方法
        _displayHandler = [IGListDisplayHandler new];
        // 3. `IGListWorkingRangeHandler` ，通过设置 `workingRangeSize` ，可以在 `UICollectionView` 滑动时做一些预处理工作
        _workingRangeHandler = [[IGListWorkingRangeHandler alloc] initWithWorkingRangeSize:workingRangeSize];
        // 4. `NSHashTable<id<IGListAdapterUpdateListener>> *_updateListeners` ，在 `UICollectionView` 完成更新操作后调用
        _updateListeners = [NSHashTable weakObjectsHashTable];
        // 5.  `NSMapTable<UICollectionReusableView *, IGListSectionController *> *_viewSectionControllerMap` ，
		  // 维护 `sectionController` 和 `UICollectionReusableView` 映射关系。
        _viewSectionControllerMap = [NSMapTable mapTableWithKeyOptions:NSMapTableObjectPointerPersonality | NSMapTableStrongMemory
                                                          valueOptions:NSMapTableStrongMemory];

        _updater = updater;
        _viewController = viewController;

        [IGListDebugger trackAdapter:self];
    }
    return self;
}
```

`objectLookupPointerFunctions` 的自定义 `hashFunction` 和 `isEqualFunction` ，由于 `object` 已经有了 `-diffIdentifier` ，所以可以基于这个方法进行判断：

```objc
static BOOL IGListIsEqual(const void *a, const void *b, NSUInteger (*size)(const void *item)) {
    const id<IGListDiffable, NSObject> left = (__bridge id<IGListDiffable, NSObject>)a;
    const id<IGListDiffable, NSObject> right = (__bridge id<IGListDiffable, NSObject>)b;
    return [left class] == [right class]
    && [[left diffIdentifier] isEqual:[right diffIdentifier]];
}

// 因为 diff 算法是基于 `-diffIdentifier` 进行计算，所以我们的映射表需要精确匹配这种行为
static NSUInteger IGListIdentifierHash(const void *item, NSUInteger (*size)(const void *item)) {
    return [[(__bridge id<IGListDiffable>)item diffIdentifier] hash];
}

- (NSPointerFunctions *)objectLookupPointerFunctions {
    NSPointerFunctions *functions = [NSPointerFunctions pointerFunctionsWithOptions:NSPointerFunctionsStrongMemory];
    functions.hashFunction = IGListIdentifierHash;
    functions.isEqualFunction = IGListIsEqual;
    return functions;
}
```

`IGListAdapter` 作为 `IGListKit` 的中心调度器，负责串联起 `IGListSectionController` ， `Model` ， `UICollectionView` 和 `UICollectionReusableView` 之间的关系，在设置 `UICollectionView` 时， `IGListAdapter` 就会进行对应的处理：

```objc
- (void)setCollectionView:(UICollectionView *)collectionView {
    IGAssertMainThread();

    // 1. 如果在 `Cell` 中设置 `UICollectionView` 时有可能会多次设置 `IGListAdapter` 的 `colleciontView` ，这里做一下判断，防止重复设置；
    if (_collectionView != collectionView || _collectionView.dataSource != self) {
        // 2. 每次关联 `UICollectionView` 和 `IGListAdapter` ，都需要清空之前的关联，
		  // 防止旧的 `IGListAdapter` 对 `UICollectionView` 进行更新，
        // 相关的 PR 在这里 [Prevent stale adapter:collectionView corruptions](https://github.com/Instagram/IGListKit/pull/517)
        // 当在 `Cell` 中进行设置时： `adapter.collectionView = cell.collectionView` ，
        // 有可能会有多个 `adapter` 链接到同一个 `collectionView` ，
        // 那么就可能会发生旧的 `adapter` 对当前 `UICollectionView` 进行修改的 bug ，
        // 所以这里需要对之前的 `adapter` 设置 `collectionView` 为 `nil` ；
        static NSMapTable<UICollectionView *, IGListAdapter *> *globalCollectionViewAdapterMap = nil;
        if (globalCollectionViewAdapterMap == nil) {
            globalCollectionViewAdapterMap = [NSMapTable weakToWeakObjectsMapTable];
        }
        [globalCollectionViewAdapterMap removeObjectForKey:_collectionView];
        [[globalCollectionViewAdapterMap objectForKey:collectionView] setCollectionView:nil];
        [globalCollectionViewAdapterMap setObject:self forKey:collectionView];

        // 3. 清空已注册的 `Cell` ， `Nib` 等；
        _registeredCellIdentifiers = [NSMutableSet new];
        _registeredNibNames = [NSMutableSet new];
        _registeredSupplementaryViewIdentifiers = [NSMutableSet new];
        _registeredSupplementaryViewNibNames = [NSMutableSet new];

        const BOOL settingFirstCollectionView = _collectionView == nil;

        _collectionView = collectionView;
        _collectionView.dataSource = self;

        if (@available(iOS 10.0, tvOS 10, *)) {
            _collectionView.prefetchingEnabled = NO;
        }

        [_collectionView.collectionViewLayout ig_hijackLayoutInteractiveReorderingMethodForAdapter:self];
        [_collectionView.collectionViewLayout invalidateLayout];
        // 4. 设置 `collectionView` 的 `delegate` ；
        [self _updateCollectionViewDelegate];

        // 5. 如果是第一次设置 `collectionView` 则需要进行一些设置。
        if (settingFirstCollectionView) {
            [self _updateAfterPublicSettingsChange];
        }
    }
}
```

`_updateAfterPublicSettingsChange` 首先调用 `NSArray *objectsWithDuplicateIdentifiersRemoved(NSArray<id<IGListDiffable>> *objects)` 去除重复的 `Objects` ：

```objc
- (void)_updateAfterPublicSettingsChange {
    id<IGListAdapterDataSource> dataSource = _dataSource;
    if (_collectionView != nil && dataSource != nil) {
        NSArray *uniqueObjects = objectsWithDuplicateIdentifiersRemoved([dataSource objectsForListAdapter:self]);
        [self _updateObjects:uniqueObjects dataSource:dataSource];
    }
}
```

`IGListKit` 不支持 `Object` 间有相同的 `diffIdentifier` ，所以需要进行过滤，使用 `NSMapTable` 来进行记录，以 `diffIdentifier` 为 `key` 进行记录，如果 `identifierMap` 有记录，则不添加到 `uniqueObjects` 中：

```objc
static NSArray *objectsWithDuplicateIdentifiersRemoved(NSArray<id<IGListDiffable>> *objects) {
    if (objects == nil) {
        return nil;
    }

    NSMapTable *identifierMap = [NSMapTable strongToStrongObjectsMapTable];
    NSMutableArray *uniqueObjects = [NSMutableArray new];
    for (id<IGListDiffable> object in objects) {
        id diffIdentifier = [object diffIdentifier];
        id previousObject = [identifierMap objectForKey:diffIdentifier];
        if (diffIdentifier != nil
            && previousObject == nil) {
            [identifierMap setObject:object forKey:diffIdentifier];
            [uniqueObjects addObject:object];
        } else {
            IGLKLog(@"Duplicate identifier %@ for object %@ with object %@", diffIdentifier, object, previousObject);
        }
    }
    return uniqueObjects;
}
```

去除重复的 `Model` 后，再调用 `_updateObjects: dataSource:` 获取对应的 `IGListSectionController` ，并将 `IGListSectionController` 和 `Object` 串联起来：

```objc
- (void)_updateObjects:(NSArray *)objects dataSource:(id<IGListAdapterDataSource>)dataSource {
    // 1. 状态标记，防止在更新数据源过程中刷新 `collectionView`
    _isInObjectUpdateTransaction = YES;

	  // 2. 更新数据源过程中所需要用到的数据组合
    NSMutableArray<IGListSectionController *> *sectionControllers = [NSMutableArray new];
    NSMutableArray *validObjects = [NSMutableArray new];
    IGListSectionMap *map = self.sectionMap;
    NSMutableSet *updatedObjects = [NSMutableSet new];

    // 3. 把当前的 `viewController` 和 `adapter` 存储到 `local thread dictionary` 中，以便在初始化 `IGListSectionController` 时使用
    IGListSectionControllerPushThread(self.viewController, self);

    for (id object in objects) {
        // 4. 从 `map` 中获取对应的 `IGListSectionController` ，如果没有，则从 `dataSource` 生成的新的
        IGListSectionController *sectionController = [map sectionControllerForObject:object];

        if (sectionController == nil) {
            sectionController = [dataSource listAdapter:self sectionControllerForObject:object];
        }

        if (sectionController == nil) {
            IGLKLog(@"WARNING: Ignoring nil section controller returned by data source %@ for object %@.",
                    dataSource, object);
            continue;
        }

        // 5. 设置 `sectionController` 的 `collectionContext` 和 `viewController` ，
		  // 防止 `sectioncontroller` 不是在 `-listAdapter:sectionControllerForObject:` 方法中创建的，
        // 导致 `collectionContext` 和 `viewController` 没有更新
        sectionController.collectionContext = self;
        sectionController.viewController = self.viewController;

        // 6.  如果找不到 `oldSection` ，则表示 `object` 是新增加的。如果新旧 `object` 不相等，则说明 `object` 有更新
        const NSInteger oldSection = [map sectionForObject:object];
        if (oldSection == NSNotFound || [map objectForSection:oldSection] != object) {
            [updatedObjects addObject:object];
        }

        [sectionControllers addObject:sectionController];
        [validObjects addObject:object];
    }

    // 7. 清除 `local thread dictionary` 的数据
    IGListSectionControllerPopThread();

	  // 9. 更新 `validObjects` 和 `sectionControllers` 的绑定关系
    [map updateWithObjects:validObjects sectionControllers:sectionControllers];

    // 10. 所有 `sectionControllers` 都已经加载完成，进行 `object` 更新工作
    for (id object in updatedObjects) {
        [[map sectionControllerForObject:object] didUpdateToObject:object];
    }
    [self _updateBackgroundViewShouldHide:![self _itemCountIsZero]];
    _isInObjectUpdateTransaction = NO;
}
```

至此，使用 `IGListKit` 的初始化流程已完成。

## 更新数据

`IGListKit` 在数据更新时刷新界面的流程和普通的 `UICollectionView` 使用方式类似，首先是根据用户操作/网络请求等对数据进行调整，然后调用 `reloadData/performUpdates` 刷新 `UICollectionView` ，但是与系统的 `UICollectionView` 不同，我们不再需要手动去计算哪些 `Cell` 进行了刷新/删除/插入/移动和进行相关操作， `IGListKit` 会自动帮我们完成这件事，我们所需要做的只是更新数据，然后调用 `IGListAdapter` 的对应方法即可。 而 `IGListAdapter` 提供了三种刷新方式，下面具体展开说说。

### performUpdatesAnimated:completion:

`performUpdatesAnimated:completion:` ，等价于 `UICollectionView` 的 `performBatchUpdates:completion:` 方法，当数据源更新后，可以调用这个方法来进行局部刷新， `IGListAdapter` 内部会计算出新增/删除/更新的 `Object` 所对应的 `Section` 和位置，调用 `UICollectionView` 对应的方法。

```objc
- (void)performUpdatesAnimated:(BOOL)animated completion:(IGListUpdaterCompletion)completion {

    id<IGListAdapterDataSource> dataSource = self.dataSource;
    UICollectionView *collectionView = self.collectionView;
    // 1. 如果 `dataSource` 或者 `collectionView` 为 `nil` ，直接返回，调用 `completion(NO)`
    if (dataSource == nil || collectionView == nil) {
        if (completion) {
            completion(NO);
        }
        return;
    }

    // 2. 获取旧的 `objects` ，定义如何获取新的 `objects` 的 `block` ，
    // 延迟执行 `dataSource` 的 `objectsForListAdapter:` 方法，等到需要时再执行，保证获取到的  `objects` 是最新的
    NSArray *fromObjects = self.sectionMap.objects;

    __weak __typeof__(self) weakSelf = self;
    IGListToObjectBlock toObjectsBlock = ^NSArray *{
        __typeof__(self) strongSelf = weakSelf;
        if (strongSelf == nil) {
            return nil;
        }
        return [dataSource objectsForListAdapter:strongSelf];
    };
    // 3. 这里在局部刷新布局信息时会用到，标记一下进入局部刷新流程
    [self _enterBatchUpdates];
    // 4. 调用 `id <IGListUpdatingDelegate> updater` 对应的方法更新 `collectionView` ，
    // 通过 `_collectionViewBlock ` 来获取 `collectionView` 延迟到真正更新时才执行 block，确保获取到的 `collectionView` 是正确的
    [self.updater performUpdateWithCollectionViewBlock:[self _collectionViewBlock]
                                           fromObjects:fromObjects
                                        toObjectsBlock:toObjectsBlock
                                              animated:animated
                                 objectTransitionBlock:^(NSArray *toObjects) {
                                     // 5. 这里的 `toObjects` 是由 `update` 进行计算后得出的新的数据源，设置 `previousSectionMap` ，更新数据源
                                     weakSelf.previousSectionMap = [weakSelf.sectionMap copy];
                                     [weakSelf _updateObjects:toObjects dataSource:dataSource];
                                 } completion:^(BOOL finished) {
                                     // 6. 完成刷新，复原标记
                                     weakSelf.previousSectionMap = nil;

                                     [weakSelf _notifyDidUpdate:IGListAdapterUpdateTypePerformUpdates animated:animated];
                                     if (completion) {
                                         completion(finished);
                                     }
                                     [weakSelf _exitBatchUpdates];
                                 }];
}
```

### reloadDataWithCompletion:

`reloadDataWithCompletion:` 全局刷新，作用跟 `UICollectionView` 的 `reloadData` 方法类似，会移除掉所有旧的 `objects` 和 `IGListSectionController` ，需要注意的是会重新生成所有 `IGListSectionController` ，所以是个有可能非常耗时的操作，在调用这个方法前必须清楚知道这一前提，一般情况下推荐使用 `performUpdatesAnimated:completion:` 来进行刷新。`reloadData` 的实现比 `performUpdates` 的要简单很多，只需要调用 `update` 对应的方法，清空 `sectionMap` ，更新 `objects` 即可。

```objc
- (void)reloadDataWithCompletion:(nullable IGListUpdaterCompletion)completion {
    id<IGListAdapterDataSource> dataSource = self.dataSource;
    UICollectionView *collectionView = self.collectionView;
    if (dataSource == nil || collectionView == nil) {
        if (completion) {
            completion(NO);
        }
        return;
    }

    NSArray *uniqueObjects = objectsWithDuplicateIdentifiersRemoved([dataSource objectsForListAdapter:self]);

    __weak __typeof__(self) weakSelf = self;
    [self.updater reloadDataWithCollectionViewBlock:[self _collectionViewBlock]
                                  reloadUpdateBlock:^{
                                      [weakSelf.sectionMap reset];
                                      [weakSelf _updateObjects:uniqueObjects dataSource:dataSource];
                                  } completion:^(BOOL finished) {
                                      [weakSelf _notifyDidUpdate:IGListAdapterUpdateTypeReloadData animated:NO];
                                      if (completion) {
                                          completion(finished);
                                      }
                                  }];
}
```

### reloadObjects:

`reloadObjects:` 刷新 `objects` 所对应的 `section` ，在 `object` 有更新时进行调用，可以直接更新所对应的 `sections` ：

```objc
- (void)reloadObjects:(NSArray *)objects {
    NSMutableIndexSet *sections = [NSMutableIndexSet new];
    // 1. 使用 `_sectionMapUsingPreviousIfInUpdateBlock` 获取 `sectionMap` ，
    // 因为 `reloadObjects` 是有可能在 `batch update` 过程中调用，如果是在 `batch update` 则使用旧的 `sectionMap`
    IGListSectionMap *map = [self _sectionMapUsingPreviousIfInUpdateBlock:YES];

    for (id object in objects) {
        // 2. 根据 `object` 找到 `section` ，如果找不到则直接跳过
        const NSInteger section = [map sectionForObject:object];
        const BOOL notFound = section == NSNotFound;
        if (notFound) {
            continue;
        }
        [sections addIndex:section];
        // 3.  根据 `section` 找一下 `object` ，如果新旧 `object` 不相等，`map` 则更新 `object` ，
        // 同时更新 `sectionController` 的 `object`
        if (object != [map objectForSection:section]) {
            [map updateObject:object];
            [[map sectionControllerForSection:section] didUpdateToObject:object];
        }
    }

    UICollectionView *collectionView = self.collectionView;
    [self.updater reloadCollectionView:collectionView sections:sections];
}
```

## 协议

`IGListKit` 围绕 `IGListAdapter` 定义了了大量协议，提供了良好的扩展性和接口封装。下面逐一来进行分析。

### IGListAdapterDelegate

当 `object` 在屏幕上出现/消失，会调用 `IGListKit` 的 `id <IGListAdapterDelegate> delegate` 的相关方法，但是由于是基于 `object` 的，所以粒度没有办法精确到每个 `Cell` ，所以需要 `Cell` 级别的粒度，可以使用 `IGListSectionController` 的 `id <IGListDisplayDelegate> displayDelegate` 。

```objc
NS_SWIFT_NAME(ListAdapterDelegate)
@protocol IGListAdapterDelegate <NSObject>

- (void)listAdapter:(IGListAdapter *)listAdapter willDisplayObject:(id)object atIndex:(NSInteger)index;

- (void)listAdapter:(IGListAdapter *)listAdapter didEndDisplayingObject:(id)object atIndex:(NSInteger)index;

@end
```

### UICollectionViewDelegate & UIScrollViewDelegate

这两个需要放在一起说说，因为 `IGListKit` 对 `IGListAdapter` 的这两个 `delegate` 做了处理：

```objc
// 只接收 `UICollectionViewDelegate` 的回调，不接收 `UIScrollViewDelegate` 的回调
@property (nonatomic, nullable, weak) id <UICollectionViewDelegate> collectionViewDelegate;

// 只接收 `UIScrollViewDelegate ` 的回调
@property (nonatomic, nullable, weak) id <UIScrollViewDelegate> scrollViewDelegate;
```

因为 `UICollectionViewDelegate` 是继承自 `UIScrollViewDelegate` ，所以 `id <UICollectionViewDelegate> collectionViewDelegate` 也会接收到 `UIScrollViewDelegate` 的回调，所以 `IGListKit` 使用一个 `NSProxy` 子类 `IGListAdapterProxy` 来对不同 `delegate` 的回调进行区分：

```objc
- (void)_createProxyAndUpdateCollectionViewDelegate {
    _collectionView.delegate = nil;

    self.delegateProxy = [[IGListAdapterProxy alloc] initWithCollectionViewTarget:_collectionViewDelegate
                                                                 scrollViewTarget:_scrollViewDelegate
                                                                      interceptor:self];
    [self _updateCollectionViewDelegate];
}

- (void)_updateCollectionViewDelegate {
    _collectionView.delegate = (id<UICollectionViewDelegate>)self.delegateProxy ?: self;
}
```

```objc
- (instancetype)initWithCollectionViewTarget:(nullable id<UICollectionViewDelegate>)collectionViewTarget
                            scrollViewTarget:(nullable id<UIScrollViewDelegate>)scrollViewTarget
                                 interceptor:(IGListAdapter *)interceptor {
    IGParameterAssert(interceptor != nil);
    if (self) {
        _collectionViewTarget = collectionViewTarget;
        _scrollViewTarget = scrollViewTarget;
        _interceptor = interceptor;
    }
    return self;
}

- (BOOL)respondsToSelector:(SEL)aSelector {
    // 先判断是否经过 `IGListAdapter` 进行处理，然后再判断 `_collectionViewTarget` 或者 `_scrollViewTarget` 是否可以响应
    return isInterceptedSelector(aSelector)
    || [_collectionViewTarget respondsToSelector:aSelector]
    || [_scrollViewTarget respondsToSelector:aSelector];
}

- (id)forwardingTargetForSelector:(SEL)aSelector {
    // 先判断 _interceptor 是否可以处理，如果可以，就转发给 _interceptor
    if (isInterceptedSelector(aSelector)) {
        return _interceptor;
    }

    // 因为 `UICollectionViewDelegate` 是 `UIScrollViewDelegate` 的子类，所以先检查 `_scrollViewTarget` 是否可以响应，
    // 否则使用 _collectionViewTarget
    return [_scrollViewTarget respondsToSelector:aSelector] ? _scrollViewTarget : _collectionViewTarget;
}
```

### IGListAdapterPerformanceDelegate

`id <IGListAdapterPerformanceDelegate> performanceDelegate` 是为调用方提供了 `UICollectionView` 在滑动时会调用的方法耗时的回调，比如说监听获取 `Cell` 的耗时。

```objc
// 性能相关的 delegate ，
@property (nonatomic, nullable, weak) id <IGListAdapterPerformanceDelegate> performanceDelegate;
```

```objc
- (UICollectionViewCell *)collectionView:(UICollectionView *)collectionView cellForItemAtIndexPath:(NSIndexPath *)indexPath {
    id<IGListAdapterPerformanceDelegate> performanceDelegate = self.performanceDelegate;
    [performanceDelegate listAdapterWillCallDequeueCell:self];

    IGListSectionController *sectionController = [self sectionControllerForSection:indexPath.section];

    UICollectionViewCell *cell = [sectionController cellForItemAtIndex:indexPath.item];
    /// ....

    [performanceDelegate listAdapter:self didCallDequeueCell:cell onSectionController:sectionController atIndex:indexPath.item];
    return cell;
}
```

这里去除其它代码，只保留 `performanceDelegate` 部分，可以看到在 `cellForItemAtIndexPath` 的开头和结尾调用了 `performanceDelegate` 的方法。

### IGListBatchContext

支持 `IGListBatchContext` 协议的对象为 `IGListSectionController` 提供了 `reload/insert/delete/move` 等方法，在 `IGListKit` 中，这个对象是 `IGListAdapter` ，只是 `IGListSectionController` 不知道这个对象的具体类型，只知道是 `id <IGListBatchContext>` 。

`-reloadInSectionController:atIndexes:` 方法负责重新加载 `IGListSectionController` 中 `indexes` 所对应的 `Cell` 。 `UICollectionView` 并不支持在 `batch updates` 中 `-reloadSections` 或者 `-reloadItemsAtIndexPaths:` ，内部实现为通过 `delete` 和 `insert` 操作实现，这块的实现在某些操作下可能会导致异常。 假设有个 `object` ， 对应的 `section` 为 2 ，`items` 数量为 4 ，如果需要对 `index` 为 1 的 `item` 进行 `reload` ，先要创建一个 `NSIndexPath` ，`item` 为 1， `section` 为 2 ，当执行 `-performBatchUpdates:` 时， `UICollectionView` 会删除和插入这个 `NSIndexPath` 。如果这时我们在 `position` 为 2 中插入了一个 `section` ，原有的 `seciton 2` 就会变成 `section 3` 。然而，插入的 `indexPath` 的 `section` 还是 2 。那么 `UICollectionView` 就会在 `section: 2 item: 1` 执行一个插入动画，这时候就会抛出一个异常。 为了避免这个问题， `IGListAdapter` 会根据 `sectionController` 的新旧来获取不同的 `NSIndexPath` ：

```objc
- (void)reloadInSectionController:(IGListSectionController *)sectionController atIndexes:(NSIndexSet *)indexes {
    UICollectionView *collectionView = self.collectionView;

    if (indexes.count == 0) {
        return;
    }
    [indexes enumerateIndexesUsingBlock:^(NSUInteger index, BOOL *stop) {
        NSIndexPath *fromIndexPath = [self indexPathForSectionController:sectionController index:index usePreviousIfInUpdateBlock:YES];
        NSIndexPath *toIndexPath = [self indexPathForSectionController:sectionController index:index usePreviousIfInUpdateBlock:NO];
        if (fromIndexPath != nil && toIndexPath != nil) {
            [self.updater reloadItemInCollectionView:collectionView fromIndexPath:fromIndexPath toIndexPath:toIndexPath];
        }
    }];
}
```

可以看到 `fromIndexPath` 是根据旧的数据源获取， `toIndexPath` 是新的数据源，同时还需要进行是否为 `nil` 的检查，因为 `sectionController` 有可能在批量更新中被删除了。

`-invalidateLayoutInSectionController:atIndexes:` 让 `IGListSectionController` 指定 `Cell` 布局信息失效：

```objc
- (void)invalidateLayoutInSectionController:(IGListSectionController *)sectionController atIndexes:(NSIndexSet *)indexes {
    UICollectionView *collectionView = self.collectionView;

    if (indexes.count == 0) {
        return;
    }

    NSArray *indexPaths = [self indexPathsFromSectionController:sectionController indexes:indexes usePreviousIfInUpdateBlock:NO];
    UICollectionViewLayout *layout = collectionView.collectionViewLayout;
    UICollectionViewLayoutInvalidationContext *context = [[[layout.class invalidationContextClass] alloc] init];
    [context invalidateItemsAtIndexPaths:indexPaths];
    [layout invalidateLayoutWithContext:context];
}
```

获取到 `indexPaths` 为新的 `objects` 所对应的 `indexPaths` ，这里是通过 `[layout.class invalidationContextClass]` ，因为 `layout` 有可能使用的是自定义的 `UICollectionViewLayoutInvalidationContext` 子类。

### IGListCollectionContext

`IGListCollectionContext` 为 `IGListSectionController` 提供了 `UICollectionView` 的相关信息，如大小，复用，插入，删除，重新加载等。通过协议的方式可以把接口统一起来， `IGListSectionController`只能使用 `IGListCollectionContext` 提供的接口，它不知道也不需要知道 `IGListAdapter` 的存在。

```objc
- (__kindof UICollectionViewCell *)dequeueReusableCellOfClass:(Class)cellClass
                                          withReuseIdentifier:(NSString *)reuseIdentifier
                                         forSectionController:(IGListSectionController *)sectionController
                                                      atIndex:(NSInteger)index {
    UICollectionView *collectionView = self.collectionView;
    NSString *identifier = IGListReusableViewIdentifier(cellClass, nil, reuseIdentifier);
    NSIndexPath *indexPath = [self indexPathForSectionController:sectionController index:index usePreviousIfInUpdateBlock:NO];
    if (![self.registeredCellIdentifiers containsObject:identifier]) {
        [self.registeredCellIdentifiers addObject:identifier];
        [collectionView registerClass:cellClass forCellWithReuseIdentifier:identifier];
    }
    return [collectionView dequeueReusableCellWithReuseIdentifier:identifier forIndexPath:indexPath];
}
```

在复用 `Cell` 时， `IGListKit` 不需要先调用 `register` 方法来注册 `Cell` ， `IGListAdapter` 内部记录了已经注册过的 `Cell` ，如果没有注册过，就先调用 `UICollectionView` 的 `register` 方法来进行注册，然后再调用 `dequeueReusableCell` 方法来从复用池中获取 `Cell` 。这是一个非常舒服的特性，如果每次使用都需要注册 `Cell` ，那么当业务变得非常复杂时，可能需要注册大量的 `Cell` ，会出现一个屏幕都无法完全显示注册 `Cell` 的方法。同时 `UICollectionView` 或者 `UIViewController` 也不需要和 `Cell` 进行交互，当 `Cell` 需要调整时，我们只需要在 `IGListSectionController` 中进行处理，或者直接替换对应的 `IGListSectionController` 。 上面说到在获取 `Cell` 时， `IGListKit` 会自动帮我们判断是否需要注册对应的 `Cell` ，下面来看下具体是如何实现的：

```objc
NS_INLINE NSString *IGListReusableViewIdentifier(Class viewClass, NSString * _Nullable kind, NSString * _Nullable givenReuseIdentifier) {
    return [NSString stringWithFormat:@"%@%@%@", kind ?: @"", givenReuseIdentifier ?: @"", NSStringFromClass(viewClass)];
}

- (__kindof UICollectionViewCell *)dequeueReusableCellOfClass:(Class)cellClass
                                          withReuseIdentifier:(NSString *)reuseIdentifier
                                         forSectionController:(IGListSectionController *)sectionController
                                                      atIndex:(NSInteger)index {
    UICollectionView *collectionView = self.collectionView;
    NSString *identifier = IGListReusableViewIdentifier(cellClass, nil, reuseIdentifier);
    NSIndexPath *indexPath = [self indexPathForSectionController:sectionController index:index usePreviousIfInUpdateBlock:NO];
    if (![self.registeredCellIdentifiers containsObject:identifier]) {
        [self.registeredCellIdentifiers addObject:identifier];
        [collectionView registerClass:cellClass forCellWithReuseIdentifier:identifier];
    }
    return [collectionView dequeueReusableCellWithReuseIdentifier:identifier forIndexPath:indexPath];
}
```

这个方法是在 `IGListAdapter` 内， `IGListAdapter` 会使用 `NSMutableSet` 来记录所有注册过的 `Cell` 对应的 `reuseIdentifier` ，在调用 `dequeueReusableCellWithReuseIdentifier:forIndexPath:` 前会先判断 `registeredCellIdentifiers` 是否有包含这个 `identifier` ，如果没有则进行注册，而 `IGListReusableViewIdentifier` 会采用 `kind` ， `givenReuseIdentifier` 和 `viewClass` 进行拼接的方式，生成新的 `identifier` ，也就不可能存在相同的 `identifier` 。

如果需要在 `IGListSectionController` 内部对数据源进行修改和刷新视图， `IGListCollectionContext` 也提供了如下方法：

```objc
- (void)performBatchAnimated:(BOOL)animated updates:(void (^)(id<IGListBatchContext>))updates completion:(void (^)(BOOL))completion {
    [self _enterBatchUpdates];
    __weak __typeof__(self) weakSelf = self;
    [self.updater performUpdateWithCollectionViewBlock:[self _collectionViewBlock] animated:animated itemUpdates:^{
        // 更新 `isInUpdateBlock` ，执行 `block`
        weakSelf.isInUpdateBlock = YES;
        updates(weakSelf);
        weakSelf.isInUpdateBlock = NO;
    } completion: ^(BOOL finished) {
        // 判断是否需要显示 emptyView
        [weakSelf _updateBackgroundViewShouldHide:![weakSelf _itemCountIsZero]];
        [weakSelf _notifyDidUpdate:IGListAdapterUpdateTypeItemUpdates animated:animated];
        if (completion) {
            completion(finished);
        }
        [weakSelf _exitBatchUpdates];
    }];
}
```

`-performBatchAnimated:updates:completion:` 支持在执行多个 `Cell` 的相关操作。在 `updates block` 中更新 `sectionController` 的 `dataSource` ，然后调用 `IGListBatchContext` 的方法来插入/删除 `items` ：

```objc
// self 为 IGListSectionController
[self.collectionContext performBatchItemUpdates:^ (id<IGListBatchContext> batchContext>){
   [self.items addObject:newItem];
   [self.items removeObjectAtIndex:0];

   NSIndexSet *inserts = [NSIndexSet indexSetWithIndex:[self.items count] - 1];
   [batchContext insertInSectionController:self atIndexes:inserts];

   NSIndexSet *deletes = [NSIndexSet indexSetWithIndex:0];
   [batchContext deleteInSectionController:self atIndexes:deletes];
 } completion:nil];
```

### IGListAdapterUpdateListener

`IGListKit` 支持上面提到的几种刷新方式， `IGListAdapterUpdateListener` 则提供了相关回调：

```objc
typedef NS_ENUM(NSInteger, IGListAdapterUpdateType) {
    // 调用 `-[IGListAdapter performUpdatesAnimated:completion:]`
    IGListAdapterUpdateTypePerformUpdates,
    // 调用 `-[IGListAdapter reloadDataWithCompletion:]`
    IGListAdapterUpdateTypeReloadData,
    // 在 `IGListSectionController` 中调用 `-[IGListCollectionContext performBatchAnimated:updates:completion:]`
    IGListAdapterUpdateTypeItemUpdates,
};

@protocol IGListAdapterUpdateListener <NSObject>

- (void)listAdapter:(IGListAdapter *)listAdapter
    didFinishUpdate:(IGListAdapterUpdateType)update
           animated:(BOOL)animated;

@end
```

这个方法会在以下几种情况下调用：

1. 的

  前调用；
2. 后调用；
3. 执行

  方法后。

`IGListAdapter` 支持设置多个 `Listener` ，对外提供了两个方法来添加和移除 `Listener` :

```objc
- (void)addUpdateListener:(id<IGListAdapterUpdateListener>)updateListener;

- (void)removeUpdateListener:(id<IGListAdapterUpdateListener>)updateListener;
```

## 总结

`IGListAdapter` 作为 `IGListKit` 的适配器，对外提供相关的刷新接口和一些通用方法，对内负责管理 `IGListSectionController` 和 `UICollectionView` ，调用 `dataSource` 和 `delegate` 。

![IGListAdapter](https://raw.githubusercontent.com/dirtmelon/blog-images/main/IGListAdapter.png)
