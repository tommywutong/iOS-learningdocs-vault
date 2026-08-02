---
title: 集合编程主题
apple_id: 10000034i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2010-09-01'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Collections/Articles/Arrays.html
archived_at: '2026-07-15T07:13:29.299410Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [集合编程主题](About%20Collections.md)


[下一页](Dictionaries-%20Collections%20of%20Keys%20and%20Values.md)[上一页](About%20Collections.md)

# 数组：有序集合

数组是任意类型对象的有序集合。例如，图 1 中数组所包含的对象可以是猫和狗对象的任意组合，如果该数组是可变的，你还可以再添加更多狗对象。集合中的内容并不要求是同质的。

__图 1__  数组示例

!

`NSArray` 对象管理的是一个不可变数组——也就是说，创建数组之后，你不能添加、移除或替换其中的对象。不过，你可以修改数组中各个元素本身（如果它们支持修改的话）。集合的可变性并不会影响集合内部对象的可变性。如果数组很少发生变化，或者只是整体替换，就应该使用不可变数组。

`NSMutableArray` 对象管理的是一个[可变](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectMutability.html#//apple_ref/doc/uid/TP40008195-CH42)数组，允许添加和删除条目，并按需分配内存。例如，给定一个只包含单个 dog 对象的 `NSMutableArray` 对象，你可以再添加一只狗、一只猫，或任何其他对象。同样地，你也可以像操作 `NSArray` 对象那样修改这只狗的名字——一般来说，凡是你能对 `NSArray` 对象做的事情，也都能对 `NSMutableArray` 对象做。如果数组是逐步变化的，或者数组非常大——因为大型集合的[初始化](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Initialization.html#//apple_ref/doc/uid/TP40008195-CH21)需要更多时间——就应该使用可变数组。

你可以使用初始化方法 `initWithArray:` 或便捷构造方法 `arrayWithArray:`，轻松地[创建](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectCreation.html#//apple_ref/doc/uid/TP40008195-CH39)一种类型数组对应的另一种类型实例。例如，如果你有一个 `NSArray` 实例 `myArray`，可以按如下方式创建它的可变拷贝：

```objc
NSMutableArray *myMutableArray = [NSMutableArray arrayWithArray:myArray];
```

一般来说，你可以通过向 `NSArray` 或 `NSMutableArray` 类发送某个 `array...` [消息](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Message.html#//apple_ref/doc/uid/TP40008195-CH59)来实例化一个数组。`array...` 消息会返回一个包含你以参数形式传入的元素的数组。当你向 `NSMutableArray` 对象添加对象时，该对象并不会被[复制](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectCopying.html#//apple_ref/doc/uid/TP40008195-CH38)（除非你向 [initWithArray:copyItems:](https://developer.apple.com/documentation/foundation/nsarray/1408557-initwitharray) 传入 `YES` 作为参数）。取而代之的是，数组会保存一个指向该对象的强引用。关于复制和内存管理的更多信息，请参阅[复制集合](Copying%20Collections.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcnrsfvjvomi)。

在 `NSArray` 中，有两个主要方法——`count` 和 `objectAtIndex:`——构成了其接口中其他所有方法的基础：

- [count](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/count) 返回数组中元素的数量。
- [objectAtIndex:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/objectAtIndex:) 让你可以通过索引访问数组元素，索引值从 0 开始。

在 `NSMutableArray` 中，以下这些主要方法构成了其添加、替换和删除元素能力的基础：

- [addObject:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSMutableArray/addObject:)
- [insertObject:atIndex:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSMutableArray/insertObject:atIndex:)
- [removeLastObject](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSMutableArray/removeLastObject)
- [removeObjectAtIndex:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSMutableArray/removeObjectAtIndex:)
- [replaceObjectAtIndex:withObject:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSMutableArray/replaceObjectAtIndex:withObject:)

如果你不需要把对象放在数组中的特定位置，也不需要从集合中间移除对象，就应该使用 `addObject:` 和 `removeLastObject` 方法，因为在数组末尾添加和移除比在中间操作更快。

`NSMutableArray` 中的其他方法提供了便捷的方式，可以将对象插入数组中的某个位置，也可以根据对象的身份或位置从数组中移除对象，如清单 1 所示。

__清单 1__  在数组中添加和移除元素

```objc
NSMutableArray *array = [NSMutableArray array];
[array addObject:[NSColor blackColor]];
[array insertObject:[NSColor redColor] atIndex:0];
[array insertObject:[NSColor blueColor] atIndex:1];
[array addObject:[NSColor whiteColor]];
[array removeObjectsInRange:(NSMakeRange(1, 2))];
// array now contains redColor and whiteColor
```


你可以使用 [objectAtIndex:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/objectAtIndex:) 方法按索引访问数组中的对象。例如，如果你有一个 `NSString` 对象数组，可以按如下方式访问数组中的第三个字符串：

```objc
NSString *someString = [arrayOfStrings objectAtIndex:2];
```

`NSArray` 的 `objectEnumerator` 和 `reverseObjectEnumerator` 方法提供了对数组元素的顺序访问能力，二者仅在遍历方向上有所不同。类似地，`NSArray` 的 `makeObjectsPerformSelector:` 和 `makeObjectsPerformSelector:withObject:` 方法可以让你向数组中的所有对象发送消息。在大多数情况下，应当优先使用快速枚举，因为它比使用 `NSEnumerator` 或 `makeObjectsPerformSelector:` 方法更快、也更灵活。关于遍历的更多内容，请参阅[枚举：遍历集合的元素](Enumeration-%20Traversing%20a%20Collection%E2%80%99s%20Elements.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgeztklkcijbumqkcinba)。

你可以提取数组的一个子集（`subarrayWithRange:`），也可以将一个由 `NSString` 对象组成的数组的各元素拼接成一个字符串（`componentsJoinedByString:`）。此外，你还可以使用 `isEqualToArray:` 和 `firstObjectCommonWithArray:` 方法比较两个数组。最后，你可以使用 `arrayByAddingObject:` 或 `arrayByAddingObjectsFromArray:` 创建一个新数组，其中包含现有数组中的对象以及一个或多个额外对象。

有两个主要方法可用于判断某个对象是否存在于数组中，即 [indexOfObject:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/indexOfObject:) 和 [indexOfObjectIdenticalTo:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/indexOfObjectIdenticalTo:)。此外还有两个变体方法，[indexOfObject:inRange:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/indexOfObject:inRange:) 和 [indexOfObjectIdenticalTo:inRange:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/indexOfObjectIdenticalTo:inRange:)，可用于在数组的某个范围内进行搜索。`indexOfObject:` 系列方法通过向数组元素发送 `isEqual:` 消息来判断相等性；`indexOfObjectIdenticalTo:` 系列方法则使用指针比较来判断相等性。二者的区别如清单 2 所示。

__清单 2__  在数组中查找对象

```objc
NSString *yes0 = @"yes";
NSString *yes1 = @"YES";
NSString *yes2 = [NSString stringWithFormat:@"%@", yes1];

NSArray *yesArray = [NSArray arrayWithObjects:yes0, yes1, yes2, nil];

NSUInteger index;

index = [yesArray indexOfObject:yes2];
// index is 1

index = [yesArray indexOfObjectIdenticalTo:yes2];
// index is 2
```


有时你可能需要按某种标准对数组进行排序。例如，你可能需要将一系列用户创建的字符串按字母顺序排列，或者需要将数字按升序或降序排列。图 2 展示了一个先按姓氏、再按名字排序的数组。Cocoa 提供了多种便捷的方式来对数组内容排序，例如排序描述符（sort descriptor）、[块（block）](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Block.html#//apple_ref/doc/uid/TP40008195-CH3)以及[选择器（selector）](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Selector.html#//apple_ref/doc/uid/TP40008195-CH48)。

__图 2__  数组排序

!

排序描述符（[NSSortDescriptor](https://developer.apple.com/documentation/foundation/nssortdescriptor) 的实例）提供了一种便捷且抽象的方式来描述排序规则。排序描述符具备若干实用特性：你可以用极少的自定义代码完成绝大多数排序操作；你也可以将排序描述符与 Cocoa 绑定结合使用，例如对表视图的内容进行排序；还可以将它们与 Core Data 结合使用，对获取请求（fetch request）的结果排序。

如果使用 [sortedArrayUsingDescriptors:](https://developer.apple.com/documentation/foundation/nsarray/1415069-sortedarrayusingdescriptors) 或 [sortUsingDescriptors:](https://developer.apple.com/documentation/foundation/nsmutablearray/1410745-sortusingdescriptors) 方法，排序描述符提供了一种简便方式，可以根据对象的若干属性对一组对象进行排序。给定一个字典数组（自定义对象的原理相同），你可以先按姓氏、再按名字对其内容排序。清单 3 展示了如何创建该数组并使用描述符排序。（[图 2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgeztelktk4yte) 展示了此示例的效果图。）

__清单 3__  创建并排序一个字典数组

```objc
//First create the array of dictionaries
NSString *last = @"lastName";
NSString *first = @"firstName";

NSMutableArray *array = [NSMutableArray array];
NSArray *sortedArray;

NSDictionary *dict;
dict = [NSDictionary dictionaryWithObjectsAndKeys:
                     @"Jo", first, @"Smith", last, nil];
[array addObject:dict];

dict = [NSDictionary dictionaryWithObjectsAndKeys:
                     @"Joe", first, @"Smith", last, nil];
[array addObject:dict];

dict = [NSDictionary dictionaryWithObjectsAndKeys:
                     @"Joe", first, @"Smythe", last, nil];
[array addObject:dict];

dict = [NSDictionary dictionaryWithObjectsAndKeys:
                     @"Joanne", first, @"Smith", last, nil];
[array addObject:dict];

dict = [NSDictionary dictionaryWithObjectsAndKeys:
                     @"Robert", first, @"Jones", last, nil];
[array addObject:dict];

//Next we sort the contents of the array by last name then first name

// The results are likely to be shown to a user
// Note the use of the localizedStandardCompare: selector
NSSortDescriptor *lastDescriptor =
    [[NSSortDescriptor alloc] initWithKey:last
                               ascending:YES
                               selector:@selector(localizedStandardCompare:)];
NSSortDescriptor *firstDescriptor =
    [[NSSortDescriptor alloc] initWithKey:first
                               ascending:YES
                               selector:@selector(localizedStandardCompare:)];

NSArray *descriptors = [NSArray arrayWithObjects:lastDescriptor, firstDescriptor, nil];
sortedArray = [array sortedArrayUsingDescriptors:descriptors];
```

要修改排序规则、改为先按名字再按姓氏排列，无论在概念上还是编程实现上都很容易，如清单 4 所示。

__清单 4__  按名字、姓氏排序

```objc
NSSortDescriptor *lastDescriptor =
    [[NSSortDescriptor alloc] initWithKey:last
                               ascending:NO
                               selector:@selector(localizedStandardCompare:)];
NSSortDescriptor *firstDescriptor =
    [[NSSortDescriptor alloc] initWithKey:first
                               ascending:NO
                               selector:@selector(localizedStandardCompare:)];
NSArray *descriptors = [NSArray arrayWithObjects:firstDescriptor, lastDescriptor, nil];
sortedArray = [array sortedArrayUsingDescriptors:descriptors];
```

特别是，从用户输入创建排序描述符也非常直接简单。

相比之下，清单 5 展示了使用函数进行同样排序的方式。这种方式的灵活性要差得多。

__清单 5__  使用函数排序不够灵活

```objc
NSInteger lastNameFirstNameSort(id person1, id person2, void *reverse)
{
    NSString *name1 = [person1 valueForKey:last];
    NSString *name2 = [person2 valueForKey:last];

    NSComparisonResult comparison = [name1 localizedStandardCompare:name2];
    if (comparison == NSOrderedSame) {

        name1 = [person1 valueForKey:first];
        name2 = [person2 valueForKey:first];
        comparison = [name1 localizedStandardCompare:name2];
    }

    if (*(BOOL *)reverse == YES) {
        return 0 - comparison;
    }
    return comparison;
}

BOOL reverseSort = YES;
sortedArray = [array sortedArrayUsingFunction:lastNameFirstNameSort
        context:&reverseSort];
```


你可以使用[块](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Block.html#//apple_ref/doc/uid/TP40008195-CH3)来帮助基于自定义标准对数组排序。`NSArray` 的 [sortedArrayUsingComparator:](https://developer.apple.com/documentation/foundation/nsarray/1411195-sortedarray) 方法使用给定的块比较对象，将数组排序后返回一个新数组。`NSMutableArray` 的 [sortUsingComparator:](https://developer.apple.com/documentation/foundation/nsmutablearray/1414904-sortusingcomparator) 方法则使用给定的块比较对象，对数组进行原地排序。清单 6 展示了使用块排序的示例。

__清单 6__  使用块简化数组的自定义排序

```objc
NSArray *sortedArray = [array sortedArrayUsingComparator: ^(id obj1, id obj2) {

     if ([obj1 integerValue] > [obj2 integerValue]) {
          return (NSComparisonResult)NSOrderedDescending;
     }

     if ([obj1 integerValue] < [obj2 integerValue]) {
          return (NSComparisonResult)NSOrderedAscending;
     }
     return (NSComparisonResult)NSOrderedSame;
}];
```


清单 7 展示了 [sortedArrayUsingSelector:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/sortedArrayUsingSelector:)、[sortedArrayUsingFunction:context:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/sortedArrayUsingFunction:context:) 以及 [sortedArrayUsingFunction:context:hint:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/sortedArrayUsingFunction:context:hint:) 方法的用法。其中最复杂的是 [sortedArrayUsingFunction:context:hint:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/sortedArrayUsingFunction:context:hint:)。当你有一个已经排序过一次、之后只发生轻微变化（增加或删除了 P 个元素，且 P 远小于 N）的大型数组（N 个元素）时，这种带提示的排序方式效率最高。你可以通过在概念上对 N 个"旧"元素和 P 个"新"元素做一次归并排序，来复用之前排序时所做的工作。要获得合适的提示，需要在原数组排序完成后使用 [sortedArrayHint](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/sortedArrayHint)，并保留该提示，直到需要它时（即数组被修改后需要重新排序时）再使用。

__清单 7__  使用选择器和函数排序

```objc
NSInteger alphabeticSort(id string1, id string2, void *reverse)
{
    if (*(BOOL *)reverse == YES) {
        return [string2 localizedStandardCompare:string1];
    }
    return [string1 localizedStandardCompare:string2];
}

NSMutableArray *anArray =
    [NSMutableArray arrayWithObjects:@"aa", @"ab", @"ac", @"ad", @"ae", @"af", @"ag",
        @"ah", @"ai", @"aj", @"ak", @"al", @"am", @"an", @"ao", @"ap", @"aq", @"ar", @"as", @"at",
        @"au", @"av", @"aw", @"ax", @"ay", @"az", @"ba", @"bb", @"bc", @"bd", @"bf", @"bg", @"bh",
        @"bi", @"bj", @"bk", @"bl", @"bm", @"bn", @"bo", @"bp", @"bq", @"br", @"bs", @"bt", @"bu",
        @"bv", @"bw", @"bx", @"by", @"bz", @"ca", @"cb", @"cc", @"cd", @"ce", @"cf", @"cg", @"ch",
        @"ci", @"cj", @"ck", @"cl", @"cm", @"cn", @"co", @"cp", @"cq", @"cr", @"cs", @"ct", @"cu",
        @"cv", @"cw", @"cx", @"cy", @"cz", nil];
// note: anArray is sorted
NSData *sortedArrayHint = [anArray sortedArrayHint];

[anArray insertObject:@"be" atIndex:5];

NSArray *sortedArray;

// sort using a selector
sortedArray =
        [anArray sortedArrayUsingSelector:@selector(localizedStandardCompare:)];

// sort using a function
BOOL reverseSort = NO;
sortedArray =
        [anArray sortedArrayUsingFunction:alphabeticSort context:&reverseSort];

// sort with a hint
sortedArray =
        [anArray sortedArrayUsingFunction:alphabeticSort
                                  context:&reverseSort
                                     hint:sortedArrayHint];
```


`NSArray` 和 `NSMutableArray` 类都提供了用于过滤数组内容的方法。`NSArray` 提供了 [filteredArrayUsingPredicate:](https://developer.apple.com/documentation/foundation/nsarray/1411033-filtered)，它返回一个新数组，其中包含接收者中与指定谓词匹配的对象。`NSMutableArray` 额外提供了 [filterUsingPredicate:](https://developer.apple.com/documentation/foundation/nsmutablearray/1412085-filter)，它会根据指定谓词对接收者的内容求值，只保留与之匹配的对象。清单 8 展示了这些方法的用法。关于谓词的更多信息，请参阅《_[谓词编程指南](../Predicate%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytoobz)_》。

__清单 8__  使用谓词过滤数组

```objc
NSMutableArray *array =
    [NSMutableArray arrayWithObjects:@"Bill", @"Ben", @"Chris", @"Melissa", nil];

NSPredicate *bPredicate =
    [NSPredicate predicateWithFormat:@"SELF beginswith[c] 'b'"];
NSArray *beginWithB =
    [array filteredArrayUsingPredicate:bPredicate];
// beginWithB contains { @"Bill", @"Ben" }.

NSPredicate *sPredicate =
    [NSPredicate predicateWithFormat:@"SELF contains[c] 's'"];
[array filterUsingPredicate:sPredicate];
// array now contains { @"Chris", @"Melissa" }
```

你也可以使用 `NSIndexSet` 对象来过滤数组。`NSArray` 提供了 [objectsAtIndexes:](https://developer.apple.com/documentation/foundation/nsarray/1411296-objectsatindexes)，它返回一个新数组，包含索引集中所指定索引位置的对象。`NSMutableArray` 额外提供了 [removeObjectsAtIndexes:](https://developer.apple.com/documentation/foundation/nsmutablearray/1410154-removeobjects)，可用于使用索引集就地过滤数组。关于索引集的更多信息，请参阅[索引集：存储数组中的索引](Index%20Sets-%20Storing%20Indexes%20into%20an%20Array.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcnrvfvjvomi)。

`NSPointerArray` 类默认配置为像 `NSMutableArray` 那样持有对象，不同之处在于它可以存放 `nil` 值，并且 [count](https://developer.apple.com/documentation/foundation/nspointerarray/1418453-count) 方法会将这些 `nil` 值计算在内。它还允许你为特定场景定制额外的存储选项，例如需要高级[内存管理](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/MemoryManagement.html#//apple_ref/doc/uid/TP40008195-CH27)选项，或者需要持有特定类型的指针。例如，图 3 中的指针数组被配置为持有对其内容的弱引用。你还可以指定是否希望在对象加入数组时被复制。

__图 3__  指针数组的对象所有权

!

当你想要一个使用弱引用的有序集合时，可以使用 `NSPointerArray` 对象。例如，假设你有一个包含若干对象的全局数组。由于全局对象永远不会被回收，除非其内容是弱持有的，否则其中的对象都无法被释放。配置为弱持有对象的指针数组并不拥有其内容。如果这样的指针数组中的对象没有其他强引用，这些对象就可以被释放。例如，[图 3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgeztelktk4ytc) 中的指针数组对其内容持有弱引用，对象 D 和对象 E 将被释放。

要创建指针数组，可以使用 [pointerArrayWithOptions:](https://developer.apple.com/documentation/foundation/nspointerarray/1564845-pointerarraywithoptions) 或 [initWithOptions:](https://developer.apple.com/documentation/foundation/nspointerarray/1408229-init) 并配合合适的 [NSPointerFunctionsOptions](https://developer.apple.com/documentation/foundation/nspointerfunctions/options) 选项来创建或初始化它。也可以使用 [initWithPointerFunctions:](https://developer.apple.com/documentation/foundation/nspointerarray/1416727-init) 并配合合适的 [NSPointerFunctions](https://developer.apple.com/documentation/foundation/nspointerfunctions) 实例来初始化。关于各种指针函数选项的更多信息，请参阅[指针函数选项](Pointer%20Function%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcojzfvjvomi)。

`NSPointerArray` 类还定义了若干便捷构造方法，用于创建对其内容持有强引用或弱引用的指针数组。例如，[pointerArrayWithWeakObjects](https://developer.apple.com/documentation/foundation/nspointerarray/1564846-pointerarraywithweakobjects) 创建一个对其内容持有弱引用的指针数组。这些便捷构造方法仅应在存储对象时使用。

要将指针数组配置为使用任意指针，可以同时使用 `NSPointerFunctionsOpaqueMemory` 和 `NSPointerFunctionsOpaquePersonality` 选项对其进行初始化。例如，你可以按照清单 9 所示的方式添加一个指向 `int` 值的指针。

__清单 9__  为非对象指针配置的指针数组

```objc
NSPointerFunctionsOptions options=(NSPointerFunctionsOpaqueMemory |
     NSPointerFunctionsOpaquePersonality);

NSPointerArray *ptrArray=[NSPointerArray pointerArrayWithOptions: options];

[ptrArray addPointer: someIntPtr];
```

随后你可以按如下方式访问该整数。

```objc
NSLog(@" Index 0 contains: %i", *(int *) [ptrArray pointerAtIndex: 0] );
```

当配置为使用任意指针时，指针数组也会带有使用指针本身所固有的风险。例如，如果这些指针指向某个函数内基于栈创建的数据，那么即使指针数组本身仍然有效，这些指针在函数之外也是无效的。尝试访问它们将导致未定义行为。

[下一页](Dictionaries-%20Collections%20of%20Keys%20and%20Values.md)[上一页](About%20Collections.md)
