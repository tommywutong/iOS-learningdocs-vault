---
title: 集合编程主题
apple_id: 10000034i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2010-09-01'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Collections/Articles/index.html
archived_at: '2026-07-15T07:13:36.859965Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [集合编程主题](About%20Collections.md)


[下一页](Index%20Paths-%20Storing%20a%20Path%20Through%20Nested%20Arrays.md)[上一页](Sets-%20Unordered%20Collections%20of%20Objects.md)

# 索引集：存储数组中的索引

索引集（index set）用于存储指向其他数据结构（例如 `NSArray` 对象）的索引。索引集中的每个索引只能出现一次，这也是为什么索引集不适合用来存储任意整数集合的原因。由于索引集（如图 1 所示）使用范围来存储索引，它们通常比数组这样存储一组整数值的方式更高效。

__图 1__  索引集与数组的交互

!

`NSIndexSet` 对象管理一个不可变的索引集——也就是说，一旦你创建了该索引集，就不能再向其中添加索引，也不能从中移除索引。

`NSMutableIndexSet` 对象管理一个[可变](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectMutability.html#//apple_ref/doc/uid/TP40008195-CH42)索引集，允许随时添加和删除索引，并按需自动分配内存。

你可以使用初始化方法 [initWithIndexSet:](https://developer.apple.com/documentation/foundation/nsindexset/1415602-initwithindexset) 轻松地从一种类型的索引集[创建](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectCreation.html#//apple_ref/doc/uid/TP40008195-CH39)另一种类型的实例。如果你想创建一个包含不相交索引集合的不可变索引集（这类集合通常是用可变索引集创建的），这个方法尤其有用。例如，如果你有一个名为 `myIndexes` 的 `NSMutableIndexSet` 对象，已经向其中添加了索引，你可以按如下方式创建一个不可变的拷贝：

```objc
NSIndexSet *myImmutableIndexes=[[NSIndexSet alloc] initWithIndexSet: myIndexes];
```

你也可以使用 [initWithIndex:](https://developer.apple.com/documentation/foundation/nsindexset/1416501-init) 或 [initWithIndexesInRange:](https://developer.apple.com/documentation/foundation/nsindexset/1414013-initwithindexesinrange) 方法，从单个索引或一个索引范围来初始化索引集。

`NSMutableIndexSet` 类的方法允许你添加或移除额外的索引或索引范围。例如，你可以存储不相交的索引集合，并按需修改已有的索引集合。以下是其中一些方法：

- [addIndex:](https://developer.apple.com/documentation/foundation/nsmutableindexset/1410712-addindex)
- [addIndexesInRange:](https://developer.apple.com/documentation/foundation/nsmutableindexset/1408251-addindexesinrange)
- [removeIndex:](https://developer.apple.com/documentation/foundation/nsmutableindexset/1410650-remove)
- [removeIndexesInRange:](https://developer.apple.com/documentation/foundation/nsmutableindexset/1415791-removeindexesinrange)

如果你有一个名为 `myDisjointIndexes` 的空 `NSMutableIndexSet` 对象，可以像清单 1 那样，向其中填入索引 1、2、5、6、7 和 10。

__清单 1__  向可变索引集添加索引

```objc
[myDisjointIndexes addIndexesInRange: NSMakeRange(1,2)];
[myDisjointIndexes addIndexesInRange: NSMakeRange(5,3)];
[myDisjointIndexes addIndex: 10];
```


要访问某个索引集所索引的全部对象，按顺序遍历该索引集可能会比较方便。相较于遍历对应的数组，遍历索引集效率更高，因为它只需要你检查感兴趣的那些索引。如果你有一个名为 `anArray` 的 `NSArray` 对象和一个名为 `anIndexSet` 的 `NSIndexSet` 对象，可以像清单 2 那样正向遍历索引集。

__清单 2__  正向遍历索引集

```objc
NSUInteger index=[anIndexSet firstIndex];

while(index != NSNotFound)
{

     NSLog(@" %@",[anArray objectAtIndex:index]);
     index=[anIndexSet indexGreaterThanIndex: index];
}
```

有时可能需要反向遍历索引集，例如当你想有选择地从 `NSMutableArray` 对象中移除某些索引处的对象时。你可以像清单 3 那样反向遍历索引集。

__清单 3__  反向遍历索引集

```objc
NSUInteger index=[anIndexSet lastIndex];

while(index != NSNotFound)
{

     if([[aMutableArray objectAtIndex: index] isEqualToString:@"G"]){
          [aMutableArray removeObjectAtIndex:index];
     }
     index=[anIndexSet indexLessThanIndex: index];
}
```

只有当你想有选择地移除某个索引集所指向的部分对象时，才应使用上述方法。如果你想移除索引集中所有索引处的对象，应改用 [removeObjectsAtIndexes:](https://developer.apple.com/documentation/foundation/nsmutablearray/1410154-removeobjects)。

索引集与 [block](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Block.html#//apple_ref/doc/uid/TP40008195-CH3) 结合使用时尤为强大。使用 block，你可以创建一个索引集，用于标记数组中通过了某个测试的成员。例如，如果你有一个未排序的数字数组，想创建一个索引集，其中包含所有小于 20 的数字对应的索引，可以采用类似清单 4 的方式。

__清单 4__  使用 block 从数组创建索引集

```objc
NSIndexSet *lessThan20=[someArray indexesOfObjectsPassingTest:^(id obj, NSUInteger index, BOOL *stop){
     if ([obj isLessThan:[NSNumber numberWithInt:20]]){
          return YES;
     }
     return NO;
}];
```

索引集也可以用于对数组进行基于 block 的枚举。要只枚举数组中索引集所包含的那些索引对应的元素，可以使用 [enumerateObjectsAtIndexes:options:usingBlock:](https://developer.apple.com/documentation/foundation/nsarray/1417577-enumerateobjectsatindexes) 方法。

另外，也可以使用 [enumerateIndexesUsingBlock:](https://developer.apple.com/documentation/foundation/nsindexset/1411395-enumerateindexesusingblock) 方法，通过 block 来枚举索引集本身。例如，你可以对索引在该索引集中的每个对象执行某个任务。只要索引集对所使用的多个数组都有效，你甚至可以从多个数组中访问对象，如清单 5 所示。

__清单 5__  枚举索引集以访问多个数组

```objc
[anIndexSet enumerateIndexesUsingBlock:^(NSUInteger idx, BOOL *stop){
     if([[firstArray objectAtIndex: idx] isEqual:[secondArray objectAtIndex: idx]]){
          NSLog(@"Objects at %i Equal",idx);
     }
}];
```

[下一页](Index%20Paths-%20Storing%20a%20Path%20Through%20Nested%20Arrays.md)[上一页](Sets-%20Unordered%20Collections%20of%20Objects.md)
