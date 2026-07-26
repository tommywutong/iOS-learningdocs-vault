---
title: 'IGListKit 的数据处理 - Updater&Diff'
source: dirtmelon
source_key: dirtmelon
source_url: 'https://dirtmelon.github.io/posts/iglistkit-fourth/'
original_language: zh
published: 2021-01-02
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:22cff0d1144950cf'
translated: n/a
---

> 原文：[IGListKit 的数据处理 - Updater&Diff](https://dirtmelon.github.io/posts/iglistkit-fourth/)　·　dirtmelon

## IGListAdapterUpdater

在初始化 `IGListAdapter` 时提供了一个 `id<IGListUpdatingDelegate> updater` 参数，调用者可以自己自定义一个支持 `IGListUpdatingDelegate` 协议的类，来实现 `IGListUpdatingDelegate` 的方法。 `IGListAdapter` 在更新 `UICollectionView` 和数据源时都是通过 `updater` 来进行操作， `IGListKit` 为我们提供了一个默认的 `updater` ： `IGListAdapterUpdater` ， `IGListAdapter` 支持 `UICollectionView` 的局部更新操作。

```objc
// 当更新逻辑执行完成时调用的 `block` ， `finished` 表示更新是否完成。
typedef void (^IGListUpdatingCompletion)(BOOL finished);

// 当 `adapter` 对 `UICollectionView` 进行改动时调用， `toObjects` 表示新的 `objects`
typedef void (^IGListObjectTransitionBlock)(NSArray *toObjects);

// 包含所有更新的 `block`
typedef void (^IGListItemUpdateBlock)(void);

// `adapter` 对 `UICollectionView` 进行 `reload` 是调用
typedef void (^IGListReloadUpdateBlock)(void);

// 返回转换后的 `objects`
typedef NSArray * _Nullable (^IGListToObjectBlock)(void);

// 获取执行更新的 `UICollectionView`
typedef UICollectionView * _Nullable (^IGListCollectionViewBlock)(void);

// `IGListUpdatingDelegate` 用于处理 `section` 和 `row` 级别的更新，接口的实现需要对集合处理或者转发。
@protocol IGListUpdatingDelegate <NSObject>

// 用于在集合中寻找 `object` 。
- (NSPointerFunctions *)objectLookupPointerFunctions;

/*
用于判断如何在 `objects` 进行转换。可以在 `objects` 直接执行 diff ， reload 每个 section ，或者直接调用 `UICollectionView` 的 `-reloadData` 方法。
最后， `UICollectionView` 必须要配置好 `toObjects` 数组中对应的每个 `section` 。
*/
- (void)performUpdateWithCollectionViewBlock:(IGListCollectionViewBlock)collectionViewBlock
                                 fromObjects:(nullable NSArray<id <IGListDiffable>> *)fromObjects
                              toObjectsBlock:(nullable IGListToObjectBlock)toObjectsBlock
                                    animated:(BOOL)animated
                       objectTransitionBlock:(IGListObjectTransitionBlock)objectTransitionBlock
                                  completion:(nullable IGListUpdatingCompletion)completion;

// 插入对应的 indexPaths
- (void)insertItemsIntoCollectionView:(UICollectionView *)collectionView indexPaths:(NSArray <NSIndexPath *> *)indexPaths;

// 删除对应的 indexPaths
- (void)deleteItemsFromCollectionView:(UICollectionView *)collectionView indexPaths:(NSArray <NSIndexPath *> *)indexPaths;

// 移动对应的 indexPath
- (void)moveItemInCollectionView:(UICollectionView *)collectionView
                   fromIndexPath:(NSIndexPath *)fromIndexPath
                     toIndexPath:(NSIndexPath *)toIndexPath;

// reload 对应的 fromIndexPath 和 toIndexPath
- (void)reloadItemInCollectionView:(UICollectionView *)collectionView
                     fromIndexPath:(NSIndexPath *)fromIndexPath
                       toIndexPath:(NSIndexPath *)toIndexPath;

// section 级别的处理，移动 index 对应的 section
- (void)moveSectionInCollectionView:(UICollectionView *)collectionView
                          fromIndex:(NSInteger)fromIndex
                            toIndex:(NSInteger)toIndex;

// 执行 reload data
- (void)reloadDataWithCollectionViewBlock:(IGListCollectionViewBlock)collectionViewBlock
                        reloadUpdateBlock:(IGListReloadUpdateBlock)reloadUpdateBlock
                               completion:(nullable IGListUpdatingCompletion)completion;

// reload 对应的 sections
- (void)reloadCollectionView:(UICollectionView *)collectionView sections:(NSIndexSet *)sections;

// 执行 `IGListItemUpdateBlock`
- (void)performUpdateWithCollectionViewBlock:(IGListCollectionViewBlock)collectionViewBlock
                                    animated:(BOOL)animated
                                 itemUpdates:(IGListItemUpdateBlock)itemUpdates
                                  completion:(nullable IGListUpdatingCompletion)completion;

@end
```

`IGListAdapterUpdater` 内部提供了一套队列刷新机制，使用 `IGListBatchUpdates` 记录批量刷新的 `block` ：

```objc
@property (nonatomic, strong, readonly) NSMutableArray<void (^)(void)> *itemUpdateBlocks;
@property (nonatomic, strong, readonly) NSMutableArray<void (^)(BOOL)> *itemCompletionBlocks;
```

### 批量与全局

`IGListAdapterUpdater` 提供的方法可以分为两种：

1.批量刷新，通过 `diff` 算法计算出需要进行操作的 `Cell` 或者 `Section` 。 `IGListCollectionViewBlock` 用于提供 `UICollectionView` ，通过 `block` 的方式来获取，可以保证在调用 `block` 时获取到 `UICollectionView` 是最新设置的。 `IGListToObjectBlock` 的作用也是一样的，保证获取的到 `toObjects` 是最新的：

```objc
- (void)performUpdateWithCollectionViewBlock:(IGListCollectionViewBlock)collectionViewBlock
                            		fromObjects:(NSArray *)fromObjects
                         		 toObjectsBlock:(IGListToObjectBlock)toObjectsBlock
                               	   animated:(BOOL)animated
                       objectTransitionBlock:(IGListObjectTransitionBlock)objectTransitionBlock
                                  completion:(IGListUpdatingCompletion)completion {
    self.fromObjects = self.fromObjects ?: self.pendingTransitionToObjects ?: fromObjects;
    self.toObjectsBlock = toObjectsBlock;

    self.queuedUpdateIsAnimated = self.queuedUpdateIsAnimated && animated;

    self.objectTransitionBlock = objectTransitionBlock;

    IGListUpdatingCompletion localCompletion = completion;
    if (localCompletion) {
        [self.completionBlocks addObject:localCompletion];
    }

    [self _queueUpdateWithCollectionViewBlock:collectionViewBlock];
}
```

`self.fromObjects = self.fromObjects ?: self.pendingTransitionToObjects ?: fromObjects` 和 `self.queuedUpdateIsAnimated = self.queuedUpdateIsAnimated && animated` 的作用在下文会说到。

2.全局刷新，作用类似于 `UICollectionView` 的 `reloadData` 方法：

```objc
- (void)reloadDataWithCollectionViewBlock:(IGListCollectionViewBlock)collectionViewBlock
                   reloadUpdateBlock:(IGListReloadUpdateBlock)reloadUpdateBlock
                          completion:(nullable IGListUpdatingCompletion)completion {
    IGListUpdatingCompletion localCompletion = completion;
    if (localCompletion) {
        [self.completionBlocks addObject:localCompletion];
    }

    self.reloadUpdates = reloadUpdateBlock;
    self.queuedReloadData = YES;
    [self _queueUpdateWithCollectionViewBlock:collectionViewBlock];
}
```

可以看到批量刷新和全局刷新的实现到最后都会调用 `_queueUpdateWithCollectionViewBlock` ，而在 `_queueUpdateWithCollectionViewBlock` 方法中会根据是否为 `reloadData` 来调用不同的方法：

```objc
- (void)_queueUpdateWithCollectionViewBlock:(IGListCollectionViewBlock)collectionViewBlock {
    __weak __typeof__(self) weakSelf = self;
    // 这里在 `main_queue` 上使用`dispatch_async` 的原因是如果在短时间内多次调用批量刷新的方法，
    // 可以去掉多余的 `diff` 计算和页面刷新，只需要执行一次。
    dispatch_async(dispatch_get_main_queue(), ^{
        // 如果 `updater` 不是在 `IGListBatchUpdateStateIdle` 状态或者没有改变，则直接返回。
        if (weakSelf.state != IGListBatchUpdateStateIdle
            || ![weakSelf hasChanges]) {
            return;
        }
        // 判断是否 hasQueuedReloadData 来调用不同的刷新方法
        if (weakSelf.hasQueuedReloadData) {
            [weakSelf performReloadDataWithCollectionViewBlock:collectionViewBlock];
        } else {
            [weakSelf performBatchUpdatesWithCollectionViewBlock:collectionViewBlock];
        }
    });
}
```

在进行批量更新操作时，如果 `state` 是 `IGListBatchUpdateStateExecutingBatchUpdateBlock` ，执行批量更新 `block` 的状态，则直接执行 `block` 即可，不需要添加到 `itemUpdateBlocks` 中：

```objc
if (self.state == IGListBatchUpdateStateExecutingBatchUpdateBlock) {
    itemUpdates();
} else {
    [batchUpdates.itemUpdateBlocks addObject:itemUpdates];
    self.queuedUpdateIsAnimated = self.queuedUpdateIsAnimated && animated;

    [self _queueUpdateWithCollectionViewBlock:collectionViewBlock];
}
```

### 状态配置

在看 `perform` 方法实现前先看下状态的相关定义，以便更好理解整体流程。

```objc
typedef NS_ENUM (NSInteger, IGListBatchUpdateState) {
    IGListBatchUpdateStateIdle,
    IGListBatchUpdateStateQueuedBatchUpdate,
    IGListBatchUpdateStateExecutingBatchUpdateBlock,
    IGListBatchUpdateStateExecutedBatchUpdateBlock,
};
```

1. `IGListBatchUpdateStateIdle` ，空闲状态，即当前无 `perform` 任务；
2. `IGListBatchUpdateStateQueuedBatchUpdate` ，已加入到批量更新的状态中，防止内部在同一时间内多次调用 `performBatchUpdatesWithCollectionViewBlock:` 方法；
3. `IGListBatchUpdateStateExecutingBatchUpdateBlock` 正在执行批量更新操作；
4. `IGListBatchUpdateStateExecutedBatchUpdateBlock` 已经完成批量更新操作。

在整个更新流程中， `updater.state` 会在这四种状态间切换，在不同状态间执行重复刷新操作时， `updater` 会因应不同的状态调用不同的方法，这块的处理是为了保证 `UI` 跟数据源之间的一致性和减少多余的刷新操作。

在每次开始进行刷新操作前，都会记录复制一份 `updater` 的相关属性到本地变量中，同时会调用 `cleanStateBeforeUpdates` 方法清空属性，这样同时调用刷新方法也不会互相覆盖掉，彼此间的状态也不会互相影响：

```objc
- (void)cleanStateBeforeUpdates {
    self.queuedUpdateIsAnimated = YES;
    self.fromObjects = nil;
    self.toObjectsBlock = nil;
    self.reloadUpdates = nil;
    self.queuedReloadData = NO;
    self.objectTransitionBlock = nil;
    [self.completionBlocks removeAllObjects];
}
```

`updater` 提供了 `hasChanges` 来判断是否有改动，避免多余的操作和一直执行 `perform` 操作：

```objc
- (BOOL)hasChanges {
    return self.hasQueuedReloadData
    || [self.batchUpdates hasChanges]
    || self.fromObjects != nil
    || self.toObjectsBlock != nil;
}
```

### 全局刷新

`performReloadDataWithCollectionViewBlock` 为 `reloadData` 时调用，不需要进行 `diff` 的计算，处理起来也简单一点。方法首先初始化相关本地变量，然后调用 `cleanStateBeforeUpdates` 方法清空属性，防止和其它刷新任务互相影响：

```objc
- (void)performReloadDataWithCollectionViewBlock:(IGListCollectionViewBlock)collectionViewBlock {
    id<IGListAdapterUpdaterDelegate> delegate = self.delegate;
    void (^reloadUpdates)(void) = self.reloadUpdates;
    IGListBatchUpdates *batchUpdates = self.batchUpdates;
    NSMutableArray *completionBlocks = [self.completionBlocks mutableCopy];

    [self cleanStateBeforeUpdates];
	  ...
}
```

设置 `executeCompletionBlocks` ，遍历 `completionBlocks` ，执行完毕后恢复 `state` 为 `IGListBatchUpdateStateIdle` ：

```objc
void (^executeCompletionBlocks)(BOOL) = ^(BOOL finished) {
    for (IGListUpdatingCompletion block in completionBlocks) {
        block(finished);
    }

    self.state = IGListBatchUpdateStateIdle;
};
```

判断 `collectionView` 是否为 `nil` ，如果为 `nil` 则直接返回：

```objc
UICollectionView *collectionView = collectionViewBlock();
if (collectionView == nil) {
    [self _cleanStateAfterUpdates];
    executeCompletionBlocks(NO);
    [_delegate listAdapterUpdater:self didFinishWithoutUpdatesWithCollectionView:collectionView];
    return;
}
```

设置 `state` 为 `IGListBatchUpdateStateExecutingBatchUpdateBlock` ，进入执行 `updateBlock` 的流程，如果有设置 `reloadUpdates` ，则执行 `reloadUpdates` 。即使是在 `reloadData` 流程中，也需要调用所有 `itemUpdateBlocks` ，因为调用方有可能在 `itemUpdateBlock` 中对数据进行修改，必须要保证数据源和 `UI` 一致。把 `batchUpdates.itemCompletionBlocks` 添加到 `completionBlocks` 中，保证所有的 `completionBlocks` 都会被执行。最后调用定义好的 `executeCompletionBlocks` ：

```objc
self.state = IGListBatchUpdateStateExecutingBatchUpdateBlock;

if (reloadUpdates) {
    reloadUpdates();
}

for (IGListItemUpdateBlock itemUpdateBlock in batchUpdates.itemUpdateBlocks) {
    itemUpdateBlock();
}

[completionBlocks addObjectsFromArray:batchUpdates.itemCompletionBlocks];

self.state = IGListBatchUpdateStateExecutedBatchUpdateBlock;

[self _cleanStateAfterUpdates];

[delegate listAdapterUpdater:self willReloadDataWithCollectionView:collectionView isFallbackReload:NO];
[collectionView reloadData];
[collectionView.collectionViewLayout invalidateLayout];
[collectionView layoutIfNeeded];
[delegate listAdapterUpdater:self didReloadDataWithCollectionView:collectionView isFallbackReload:NO];

executeCompletionBlocks(YES);
```

### 批量刷新

`performBatchUpdatesWithCollectionViewBlock` 进行批量更新时，需要处理各个状态的边界逻辑，所以比 `performReloadDataWithCollectionViewBlock` 更加复杂，在代码中是个 204 行的函数，下面拆开来说下具体的实现：

1.首先创建本地变量来记录所有的相关的属性，防止在执行批量更新过程中，又再次调用了 `performBatchUpdatesWithCollectionViewBlock` 接口，导致原有的属性被覆盖， `cleanStateBeforeUpdates` 会将相关属性复原，确保对更新过程中的其它 `performBatchUpdatesWithCollectionViewBlock` 调用没影响：

```objc
- (void)performBatchUpdatesWithCollectionViewBlock:(IGListCollectionViewBlock)collectionViewBlock {
    id<IGListAdapterUpdaterDelegate> delegate = self.delegate;
    NSArray *fromObjects = [self.fromObjects copy];
    IGListToObjectBlock toObjectsBlock = [self.toObjectsBlock copy];
    NSMutableArray *completionBlocks = [self.completionBlocks mutableCopy];
    void (^objectTransitionBlock)(NSArray *) = [self.objectTransitionBlock copy];
    const BOOL animated = self.queuedUpdateIsAnimated;
    const BOOL allowsReloadingOnTooManyUpdates = self.allowsReloadingOnTooManyUpdates;
    const IGListExperiment experiments = self.experiments;
    IGListBatchUpdates *batchUpdates = self.batchUpdates;

    [self cleanStateBeforeUpdates];

}
```

2.如果 `collectionView` 为 `nil` 就直接返回，这块的处理和 `performReloadDataWithCollectionViewBlock` 是一致的，通过 `toObjectsBlock` 来获取 `toObjects` ，这里使用 `block` 的原因是可以保证在获取 `toObjects` 时对应的数据源是最新的：

```objc
UICollectionView *collectionView = collectionViewBlock();
if (collectionView == nil) {
    [self _cleanStateAfterUpdates];
    executeCompletionBlocks(NO);
    [_delegate listAdapterUpdater:self didFinishWithoutUpdatesWithCollectionView:collectionView];
    return;
}

NSArray *toObjects = nil;
if (toObjectsBlock != nil) {
    toObjects = objectsWithDuplicateIdentifiersRemoved(toObjectsBlock());
}
```

3.定义 `executeUpdateBlocks` ，首先设置 `state` 为 `IGListBatchUpdateStateExecutingBatchUpdateBlock` ，防止多次执行。然后在执行 `itemUpdateBlock` 前先调用 `objectTransitionBlock` ，使得数据源更新到最新的 `toObjects` ，以保证数据源跟 UI 一致。执行 `itemUpdateBlock` ，在 `itemUpdateBlock` 中处理 `NSIndexPath` 对应的插入，删除和刷新操作。最后把 `batchUpdates.itemCompletionBlocks` 添加到 `completionBlocks` 中：

```objc
void (^executeUpdateBlocks)(void) = ^{
    self.state = IGListBatchUpdateStateExecutingBatchUpdateBlock;

    if (objectTransitionBlock != nil) {
        objectTransitionBlock(toObjects);
    }

    for (IGListItemUpdateBlock itemUpdateBlock in batchUpdates.itemUpdateBlocks) {
        itemUpdateBlock();
    }

    [completionBlocks addObjectsFromArray:batchUpdates.itemCompletionBlocks];

    self.state = IGListBatchUpdateStateExecutedBatchUpdateBlock;
};
```

4.定义 `reloadDataFallback` ，如果 `collectionView` 所在的 `window` 不可见，则直接 `reloadData` ，跳过 `diff` 操作。在 `reloadDataFallback` 的最后，调用 `_queueUpdateWithCollectionViewBlock:` ，防止丢失一些批量更新过程中进行的更新操作，如果在下一个 Runloop 过程中没有更新操作， `_queueUpdateWithCollectionViewBlock` 会直接退出。设置 `pendingTransitionToObjects` 为 `toObjects` ，在后续的更新中 `pendingTransitionToObjects` 作为 `fromObjects` 使用：

```objc
void (^reloadDataFallback)(void) = ^{
    [delegate listAdapterUpdater:self willReloadDataWithCollectionView:collectionView isFallbackReload:YES];
    executeUpdateBlocks();
    [self _cleanStateAfterUpdates];
    [self _performBatchUpdatesItemBlockApplied];
    [collectionView reloadData];
    [collectionView layoutIfNeeded];
    executeCompletionBlocks(YES);
    [delegate listAdapterUpdater:self didReloadDataWithCollectionView:collectionView isFallbackReload:YES];

    [self _queueUpdateWithCollectionViewBlock:collectionViewBlock];
};

[self _beginPerformBatchUpdatesToObjects:toObjects];

if (self.allowsBackgroundReloading && collectionView.window == nil) {
    reloadDataFallback();
    return;
}
```

5.定义 `batchUpdatesBlock` ，放到 `-[UICollectionView performBatchUpdates:completion:]` 第一个 `block` 参数中，如果 `singleItemSectionUpdates` 为 `YES` ，即每个 `section` 中只有 1 个 `item` ，那么可以在 `section` 层面进行处理，直接调用 `UICollectionView` 的操作 `section` 的相关方法即可：

```objc
void (^batchUpdatesBlock)(IGListIndexSetResult *result) = ^(IGListIndexSetResult *result){
    executeUpdateBlocks();
    if (self.singleItemSectionUpdates) {
        [collectionView deleteSections:result.deletes];
        [collectionView insertSections:result.inserts];
        for (IGListMoveIndex *move in result.moves) {
            [collectionView moveSection:move.from toSection:move.to];
        }

        self.applyingUpdateData = [[IGListBatchUpdateData alloc]
                                   initWithInsertSections:result.inserts
                                   deleteSections:result.deletes
                                   moveSections:[NSSet setWithArray:result.moves]
                                   insertIndexPaths:@[]
                                   deleteIndexPaths:@[]
                                   updateIndexPaths:@[]
                                   moveIndexPaths:@[]];
    } else {
        self.applyingUpdateData = IGListApplyUpdatesToCollectionView(collectionView,
                                                                     result,
                                                                     self.batchUpdates,
                                                                     fromObjects,
                                                                     experiments,
                                                                     self.sectionMovesAsDeletesInserts,
                                                                     self.preferItemReloadsForSectionReloads);
    }

    [self _cleanStateAfterUpdates];
    [self _performBatchUpdatesItemBlockApplied];
};
```

6.在 `IGListApplyUpdatesToCollectionView` 中针对 `reload` 操作进行特殊处理。`sectionReloads` 在手动调用 `reload` 方法时会记录对应的 `section` ，合并 `diff` 和手动 `reloads` 的 `section` 到 `reloads` 中，同时如果有需要的话使用 `delete + insert` 代替 `move` ：

```objc
NSMutableIndexSet *reloads = [diffResult.updates mutableCopy];
[reloads addIndexes:batchUpdates.sectionReloads];

NSMutableIndexSet *inserts = [diffResult.inserts mutableCopy];
NSMutableIndexSet *deletes = [diffResult.deletes mutableCopy];
NSMutableArray<NSIndexPath *> *itemUpdates = [NSMutableArray new];
if (sectionMovesAsDeletesInserts) {
    for (IGListMoveIndex *move in moves) {
        [deletes addIndex:move.from];
        [inserts addIndex:move.to];
    }
    moves = [NSSet new];
}
```

如之前提到的在 `performBatchUpdates` 中 `reload` 是不安全的，所以只有在 `moves/inserts/deletes` 都为 0 时才执行 `reload` 操作，否则使用 `delete + insert` 代替：

```objc
if (preferItemReloadsForSectionReloads
    && moves.count == 0 && inserts.count == 0 && deletes.count == 0 && reloads.count > 0) {
    [reloads enumerateIndexesUsingBlock:^(NSUInteger sectionIndex, BOOL * _Nonnull stop) {
        NSMutableIndexSet *localIndexSet = [NSMutableIndexSet indexSetWithIndex:sectionIndex];
        if (sectionIndex < [collectionView numberOfSections]
            && sectionIndex < [collectionView.dataSource numberOfSectionsInCollectionView:collectionView]
            && [collectionView numberOfItemsInSection:sectionIndex] == [collectionView.dataSource collectionView:collectionView numberOfItemsInSection:sectionIndex]) {
            [itemUpdates addObjectsFromArray:convertSectionReloadToItemUpdates(localIndexSet, collectionView)];
        } else {
            IGListConvertReloadToDeleteInsert(localIndexSet, deletes, inserts, diffResult, fromObjects);
        }
    }];
} else {
    IGListConvertReloadToDeleteInsert(reloads, deletes, inserts, diffResult, fromObjects);
}
```

将 itemReloads 转换为 `itemDeletes` + `itemInserts` ，生成最后的 `updateData` ，`collectionView` 根据 `updateData` 对 `item` 进行操作， `ig_applyBatchUpdateData:` 内部调用对应的 `delete/insert/move/reload` 方法：

```objc
NSMutableArray<NSIndexPath *> *itemInserts = batchUpdates.itemInserts;
NSMutableArray<NSIndexPath *> *itemDeletes = batchUpdates.itemDeletes;
NSMutableArray<IGListMoveIndexPath *> *itemMoves = batchUpdates.itemMoves;

NSSet<NSIndexPath *> *uniqueDeletes = [NSSet setWithArray:itemDeletes];
NSMutableSet<NSIndexPath *> *reloadDeletePaths = [NSMutableSet new];
NSMutableSet<NSIndexPath *> *reloadInsertPaths = [NSMutableSet new];
for (IGListReloadIndexPath *reload in batchUpdates.itemReloads) {
    if (![uniqueDeletes containsObject:reload.fromIndexPath]) {
        [reloadDeletePaths addObject:reload.fromIndexPath];
        [reloadInsertPaths addObject:reload.toIndexPath];
    }
}
[itemDeletes addObjectsFromArray:[reloadDeletePaths allObjects]];
[itemInserts addObjectsFromArray:[reloadInsertPaths allObjects]];

IGListBatchUpdateData *updateData = [[IGListBatchUpdateData alloc] initWithInsertSections:inserts
                                                                           deleteSections:deletes
                                                                             moveSections:moves
                                                                         insertIndexPaths:itemInserts
                                                                         deleteIndexPaths:itemDeletes
                                                                         updateIndexPaths:itemUpdates
                                                                           moveIndexPaths:itemMoves];
[collectionView ig_applyBatchUpdateData:updateData];
return updateData;
```

7.设置 `fallbackWithoutUpdates` ，在 `collectionView.dataSource` 为 `nil` 时调用：

```objc
void (^fallbackWithoutUpdates)(void) = ^(void) {
    executeCompletionBlocks(NO);
    [delegate listAdapterUpdater:self didFinishWithoutUpdatesWithCollectionView:collectionView];
    [self _queueUpdateWithCollectionViewBlock:collectionViewBlock];
};
```

8.设置 `batchUpdatesCompletionBlock` ，放到 `-[UICollectionView performBatchUpdates:completion:]` 第二个 `block` 参数中：

```objc
void (^batchUpdatesCompletionBlock)(BOOL) = ^(BOOL finished) {
    IGListBatchUpdateData *oldApplyingUpdateData = self.applyingUpdateData;
    executeCompletionBlocks(finished);
    [delegate listAdapterUpdater:self didPerformBatchUpdates:oldApplyingUpdateData collectionView:collectionView];
    [self _queueUpdateWithCollectionViewBlock:collectionViewBlock];
};
```

9.把 `[UICollectionView performBatchUpdates` 封装起来，如果在 `batchUpdatesBlock` 处理时崩溃的了，显示出来的第一行 App 符号就不是 `block` 了。 `block` 生成的名字会包含行数，如果行数调整了，就会被标记为不同的崩溃，这会对崩溃记录造成影响：

```objc
void (^performUpdate)(IGListIndexSetResult *) = ^(IGListIndexSetResult *result){
    [delegate listAdapterUpdater:self
willPerformBatchUpdatesWithCollectionView:collectionView
                     fromObjects:fromObjects
                       toObjects:toObjects
              listIndexSetResult:result
                        animated:animated];
    IGListAdapterUpdaterPerformBatchUpdate(collectionView, animated, ^{
        batchUpdatesBlock(result);
    }, batchUpdatesCompletionBlock);
};
```

10.初始化 `tryToPerformUpdate` ， `tryToPerformUpdate` 会把之前设置好的 `block` ，设置一个 `try-catch` ，防止崩溃，根据边界情况判断是否需要 `fallback` ：

```objc
void (^tryToPerformUpdate)(IGListIndexSetResult *) = ^(IGListIndexSetResult *result){
    if (!IGListExperimentEnabled(experiments, IGListExperimentSkipLayoutBeforeUpdate)) {
        [collectionView layoutIfNeeded];
    }

    @try {
        if (collectionView.dataSource == nil) {
            fallbackWithoutUpdates();
        } else if (result.changeCount > 100 && allowsReloadingOnTooManyUpdates) {
            reloadDataFallback();
        } else {
            performUpdate(result);
        }
    } @catch (NSException *exception) {
        [delegate listAdapterUpdater:self
                      collectionView:collectionView
              willCrashWithException:exception
                         fromObjects:fromObjects
                           toObjects:toObjects
                          diffResult:result
                             updates:(id)self.applyingUpdateData];
        @throw exception;
    }
};
```

11.最后通过 `diff` 算法计算出 `IGListIndexSetResult` ，调用 `tryToPerformUpdate(result)` ：

```objc
const BOOL onBackgroundThread = IGListExperimentEnabled(experiments, IGListExperimentBackgroundDiffing);
[delegate listAdapterUpdater:self willDiffFromObjects:fromObjects toObjects:toObjects];
IGListAdapterUpdaterPerformDiffing(fromObjects, toObjects, IGListDiffEquality, experiments, onBackgroundThread, ^(IGListIndexSetResult *result){
    [delegate listAdapterUpdater:self didDiffWithResults:result onBackgroundThread:onBackgroundThread];
    tryToPerformUpdate(result);
});
```

调用顺序如下：

```objc
// 使用 fromObjects 和 toObjects 计算出 diff
IGListAdapterUpdaterPerformDiffing ->
// 判断是否需要执行更新，
tryToPerformUpdate ->
// 执行更新
performUpdate ->
// 调用 `UICollectionView` 的 `performBatchUpdates` 方法
IGListAdapterUpdaterPerformBatchUpdate ->
// batchUpdatesBlock 中执行 executeUpdateBlocks
batchUpdatesBlock ->
// 执行 UICollectionView section 和 items 的相关操作
[UICollectionView section 和 items 操作]
```

完成刷新后调用相关的 `block` ：

```objc
batchUpdatesCompletionBlock -> executeCompletionBlocks
```

## IGListReloadDataUpdater

除了支持批量刷新的 `IGListAdapterUpdater` ，`IGListKit` 还提供了仅支持全局刷新的 `IGListReloadDataUpdater` ，实现非常简单，且执行的是 `[UICollectionView reloadData]` 。其所有 `IGListUpdatingDelegate` 的相关方法都会调用 `_synchronousReloadDataWithCollectionView:` 方法进行更新：

```objc
- (void)performUpdateWithCollectionViewBlock:(IGListCollectionViewBlock)collectionViewBlock
                            fromObjects:(NSArray *)fromObjects
                         toObjectsBlock:(IGListToObjectBlock)toObjectsBlock
                               animated:(BOOL)animated
                  objectTransitionBlock:(IGListObjectTransitionBlock)objectTransitionBlock
                             completion:(IGListUpdatingCompletion)completion {
    if (toObjectsBlock != nil) {
        NSArray *toObjects = toObjectsBlock() ?: @[];
        objectTransitionBlock(toObjects);
    }
    [self _synchronousReloadDataWithCollectionView:collectionViewBlock()];
    if (completion) {
        completion(YES);
    }
}

- (void)_synchronousReloadDataWithCollectionView:(UICollectionView *)collectionView {
    [collectionView reloadData];
    [collectionView layoutIfNeeded];
}
```

可以看到实现非常简单，如果只需要进行 `reloadData` ，可以使用 `IGListReloadDataUpdater` 替换掉 `IGListAdapterUpdater` 。

## Diff

在 iOS 还没有系统级地支持 Diff 特性的年代，在使用 `UITableView/UICollectionView` 时，当数据源发生变化，我们就需要手动根据数据源计算出变化的 `NSIndexPaths` 并进行更新，这个方法的时间复杂度一般是 `O(n^2)` ，在遍历旧数据内对新数据进行遍历，或者说直接 `reloadData` ，在 `UITableView/UICollectionView` 的复用机制下，只需要重新生成显示在屏幕的 `Cell` ，所带来的影响只是丢失了动画。而 `IGListKit` 的 `IGListDiff` 可以在时间复杂度 `O(n)` 的前提下为我们计算出对应的 `NSIndexPaths` 简单易易用，再也不需要直接 `reloadData` 。下面来说说 `IGListDiff` 的核心实现。

```cpp
/// 记录 Diff 所需要的状态
struct IGListEntry {
    /// 记录旧数组中具有相同 hash 值的对象出现次数
    NSInteger oldCounter = 0;
    /// 记录新数组中具有相同 hash 值的对象出现次数
    NSInteger newCounter = 0;
    /// The indexes of the data in the old array
    /// 记录旧数组中当前 hash 对应的对象出现的位置
    stack<NSInteger> oldIndexes;
    /// 数据是否有更新
    BOOL updated = NO;
};

/// 记录 IGListEntry 和位置（ index ）， index 默认为 NSNotFound
struct IGListRecord {
    IGListEntry *entry;
    mutable NSInteger index;

    IGListRecord() {
        entry = NULL;
        index = NSNotFound;
    }
};
```

1.首先先获取新旧数据所对应的数量： `newCount` 和 `oldCount` ，然后创建新旧数据所对应的 `NSMapTable` ：

```objc
static id IGListDiffing(BOOL returnIndexPaths,
                        NSInteger fromSection,
                        NSInteger toSection,
                        NSArray<id<IGListDiffable>> *oldArray,
                        NSArray<id<IGListDiffable>> *newArray,
                        IGListDiffOption option) {
    const NSInteger newCount = newArray.count;
    const NSInteger oldCount = oldArray.count;

    NSMapTable *oldMap = [NSMapTable strongToStrongObjectsMapTable];
    NSMapTable *newMap = [NSMapTable strongToStrongObjectsMapTable];
```

2.如果 `newCount` 为 0 ，那么就是说 `oldArray` 的所有数据都需要进行删除，那么我们可以尽早返回，生成一个删除所有数据的 `IGListIndexPathResult/IGListIndexSetResult` ：

```objc
if (newCount == 0) {
    if (returnIndexPaths) {
        return [[IGListIndexPathResult alloc] initWithInserts:[NSArray new]
                                                      deletes:indexPathsAndPopulateMap(oldArray, fromSection, oldMap)
                                                      updates:[NSArray new]
                                                        moves:[NSArray new]
                                              oldIndexPathMap:oldMap
                                              newIndexPathMap:newMap];
    } else {
        [oldArray enumerateObjectsUsingBlock:^(id<IGListDiffable> obj, NSUInteger idx, BOOL *stop) {
            addIndexToMap(returnIndexPaths, fromSection, idx, obj, oldMap);
        }];
        return [[IGListIndexSetResult alloc] initWithInserts:[NSIndexSet new]
                                                     deletes:[NSIndexSet indexSetWithIndexesInRange:NSMakeRange(0, oldCount)]
                                                     updates:[NSIndexSet new]
                                                       moves:[NSArray new]
                                                 oldIndexMap:oldMap
                                                 newIndexMap:newMap];
    }
}
```

3.如果 `oldCount` 为 0 ，那么就是说 `newArray` 的所有数据都需要进行插入，那么我们可以尽早返回，生成一个插入所有数据的 `IGListIndexPathResult/IGListIndexSetResult` ：

```objc
if (oldCount == 0) {
    if (returnIndexPaths) {
        return [[IGListIndexPathResult alloc] initWithInserts:indexPathsAndPopulateMap(newArray, toSection, newMap)
                                                      deletes:[NSArray new]
                                                      updates:[NSArray new]
                                                        moves:[NSArray new]
                                              oldIndexPathMap:oldMap
                                              newIndexPathMap:newMap];
    } else {
        [newArray enumerateObjectsUsingBlock:^(id<IGListDiffable> obj, NSUInteger idx, BOOL *stop) {
            addIndexToMap(returnIndexPaths, toSection, idx, obj, newMap);
        }];
        return [[IGListIndexSetResult alloc] initWithInserts:[NSIndexSet indexSetWithIndexesInRange:NSMakeRange(0, newCount)]
                                                     deletes:[NSIndexSet new]
                                                     updates:[NSIndexSet new]
                                                       moves:[NSArray new]
                                                 oldIndexMap:oldMap
                                                 newIndexMap:newMap];
    }
}
```

4.如果 `newCount` 和 `oldCount` 都不为 0 ，那么就可以进行 Diff 计算，首先需要创建一个 `table` ，使用 `diffIdentifier` 为 `key` ， `IGListEntry` 为 `value` ，这里使用 `unordered_map` ，因为会比 `NSDictionary` 快很多。

```objc
unordered_map<id<NSObject>, IGListEntry, IGListHashID, IGListEqualID> table;
```

5.遍历 `newArray` 的数据，获取对应的 `entry` ， `entry` 的 `oldIndexes` 插入 `NSNotFound` ，且设置到 `newResultsArray` 中：

```objc
vector<IGListRecord> newResultsArray(newCount);
for (NSInteger i = 0; i < newCount; i++) {
    id<NSObject> key = IGListTableKey(newArray[i]);
    IGListEntry &entry = table[key];
    entry.newCounter++;

    entry.oldIndexes.push(NSNotFound);

    newResultsArray[i].entry = &entry;
}
```

6.遍历 `oldArray` 的数据，获取对应的 `entry` ， `entry` 的 `oldIndexes` 插入对应的位置 `i` ，且设置到 `oldResultsArray` 中：

```objc
vector<IGListRecord> oldResultsArray(oldCount);
for (NSInteger i = oldCount - 1; i >= 0; i--) {
    id<NSObject> key = IGListTableKey(oldArray[i]);
    IGListEntry &entry = table[key];
    entry.oldCounter++;

    entry.oldIndexes.push(i);

    oldResultsArray[i].entry = &entry;
}
```

7.处理那些在 `oldArray` 和 `newArray` 中都有出现的数据，遍历 `newResultsArray` ，根据 `entry` 的数据进行对比：

```objc
for (NSInteger i = 0; i < newCount; i++) {
    IGListEntry *entry = newResultsArray[i].entry;

    // 1. 获取原始位置 originalIndex , 如果 item 是插入的数据，那么 originalIndex 就为 NSNotFound
    const NSInteger originalIndex = entry->oldIndexes.top();
    entry->oldIndexes.pop();

    if (originalIndex < oldCount) {
        // 获取新旧数据的对象
        const id<IGListDiffable> n = newArray[i];
        const id<IGListDiffable> o = oldArray[originalIndex];
        switch (option) {
            case IGListDiffPointerPersonality:
                // 只通过指针进行比较
                if (n != o) {
                    entry->updated = YES;
                }
                break;
            case IGListDiffEquality:
                // 使用 `-[IGListDiffable isEqualToDiffableObject:]` 进行比较，以 n 和 o 指向的对象不同为前提
                if (n != o && ![n isEqualToDiffableObject:o]) {
                    entry->updated = YES;
                }
                break;
        }
    }
    if (originalIndex != NSNotFound
        && entry->newCounter > 0
        && entry->oldCounter > 0) {
        // 如果在 `newArray` 和 `oldArray` 中都出现，则进行位置的双向绑定
        newResultsArray[i].index = originalIndex;
        oldResultsArray[originalIndex].index = i;
    }
}
```

8.创建需要记录数据：

```objc
// 存储最后的 NSIndexPaths 或者 indexes
id mInserts, mMoves, mUpdates, mDeletes;
if (returnIndexPaths) {
    mInserts = [NSMutableArray<NSIndexPath *> new];
    mMoves = [NSMutableArray<IGListMoveIndexPath *> new];
    mUpdates = [NSMutableArray<NSIndexPath *> new];
    mDeletes = [NSMutableArray<NSIndexPath *> new];
} else {
    mInserts = [NSMutableIndexSet new];
    mMoves = [NSMutableArray<IGListMoveIndex *> new];
    mUpdates = [NSMutableIndexSet new];
    mDeletes = [NSMutableIndexSet new];
}
// 追踪删除的 items 的偏移量来计算 items 的移动位置vector<NSInteger> deleteOffsets(oldCount), insertOffsets(newCount);
NSInteger runningOffset = 0;
```

9.计算删除的数据：

```objective
for (NSInteger i = 0; i < oldCount; i++) {
    deleteOffsets[i] = runningOffset;
    const IGListRecord record = oldResultsArray[i];
    // 如果 `record.index` 为 `NSNotFound` ，则表示其没有在 `newArray` 中出现，已被删除
    if (record.index == NSNotFound) {
        addIndexToCollection(returnIndexPaths, mDeletes, fromSection, i);
        runningOffset++;
    }

    addIndexToMap(returnIndexPaths, fromSection, i, oldArray[i], oldMap);
}
```

11.最后的计算

```objc
for (NSInteger i = 0; i < newCount; i++) {
    insertOffsets[i] = runningOffset;
    const IGListRecord record = newResultsArray[i];
    const NSInteger oldIndex = record.index;
    // 如果 `record.index` 为 `NSNotFound` ，则表示其没有在 `oldArray` 中出现，是新插入的
    if (record.index == NSNotFound) {
        addIndexToCollection(returnIndexPaths, mInserts, toSection, i);
        runningOffset++;
    } else {
        // 如果 record.entry-> updated 为 YES ，则表示
        if (record.entry->updated) {
            addIndexToCollection(returnIndexPaths, mUpdates, fromSection, oldIndex);
        }
        // 计算 indexes 是否匹配，据此来判断是否需要移动
		  // oldIndex - deleteOffset + insertOffset != i ，则位置发生变化，需要移动。
        const NSInteger insertOffset = insertOffsets[i];
        const NSInteger deleteOffset = deleteOffsets[oldIndex];
        if ((oldIndex - deleteOffset + insertOffset) != i) {
            id move;
            if (returnIndexPaths) {
                NSIndexPath *from = [NSIndexPath indexPathForItem:oldIndex inSection:fromSection];
                NSIndexPath *to = [NSIndexPath indexPathForItem:i inSection:toSection];
                move = [[IGListMoveIndexPath alloc] initWithFrom:from to:to];
            } else {
                move = [[IGListMoveIndex alloc] initWithFrom:oldIndex to:i];
            }
            [mMoves addObject:move];
        }
    }

    addIndexToMap(returnIndexPaths, toSection, i, newArray[i], newMap);
}
```

12.完成计算，返回结果：

```objc
if (returnIndexPaths) {
    return [[IGListIndexPathResult alloc] initWithInserts:mInserts
                                                  deletes:mDeletes
                                                  updates:mUpdates
                                                    moves:mMoves
                                          oldIndexPathMap:oldMap
                                          newIndexPathMap:newMap];
} else {
    return [[IGListIndexSetResult alloc] initWithInserts:mInserts
                                                 deletes:mDeletes
                                                 updates:mUpdates
                                                   moves:mMoves
                                             oldIndexMap:oldMap
                                             newIndexMap:newMap];
}
```

从上面的计算可以看出需要 5 次 `for` 循环进行遍历，也就是时间复杂度为 `O(5n)` ，在 `n` 足够大的情况下可以忽略，时间复杂度可视作 `O(n)` 。

这篇文章有使用两个数组作为例子进行说明 `IGListDiff` 是如何进行计算的： [IGListKit diff 实现简析](https://xiangwangfeng.com/2017/03/16/IGListKit-diff-%E5%AE%9E%E7%8E%B0%E7%AE%80%E6%9E%90/) 。
