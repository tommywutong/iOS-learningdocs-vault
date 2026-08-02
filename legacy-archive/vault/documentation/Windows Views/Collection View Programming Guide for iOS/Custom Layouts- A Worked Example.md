---
title: iOS Collection View 编程指南
apple_id: TP40012334
resource_type: Guide
platform: tvOS|iOS
topic: User Experience
technology: UIKit
published: '2014-07-15'
source_url: https://developer.apple.com/library/archive/documentation/WindowsViews/Conceptual/CollectionViewPGforIOS/AWorkedExample/AWorkedExample.html
archived_at: '2026-07-18T02:22:34.839103Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [iOS Collection View 编程指南](About%20iOS%20Collection%20Views.md)


[下一页](Document%20Revision%20History.md)[上一页](Creating%20Custom%20Layouts.md)

# 自定义布局：一个完整示例

创建自定义的 collection view 布局很简单，要求也很直接，但实现的细节可能各不相同。你的布局必须为 collection view 所包含的每一个视图生成布局属性对象。这些属性的创建顺序取决于你应用的性质。如果 collection view 中容纳着成千上万个项目，预先计算并缓存布局属性是一个耗时的过程，那么只在某个特定项目的属性被请求时才创建它就更合理。而对于项目较少的应用，把布局信息计算一次并缓存起来，在每次有属性请求时直接引用，可以为你的应用省去大量不必要的重新计算。本章的完整示例属于后一类。

请记住，这里提供的示例代码绝不是创建自定义布局的唯一正确方式。在开始创建你的自定义布局之前，请花时间设计一套最适合你的应用、能获得最佳性能的实现结构。有关自定义布局过程的概念性综述，请参阅[创建自定义布局](Creating%20Custom%20Layouts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdgmzufvbuqnjnknltc)。

由于本章是按特定顺序呈现这个自定义布局实现的，请带着明确的实现目标从头到尾跟着示例走。本章的重点是创建自定义布局，而不是实现一个完整的应用。因此，构建最终成品所用到的视图和 controller 的实现并未给出。该布局使用自定义的 collection view 单元格作为它的单元格，并用一个自定义视图来绘制连接各单元格的连线。为 collection view 创建自定义单元格和视图、以及使用 collection view 的各项要求，都已在前面几章讲过。要回顾这些内容，请参阅 [Collection View 基础](Collection%20View%20Basics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdgmzufvbuqmrnknltc)和[设计数据源与委托](Designing%20Your%20Data%20Source%20and%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdgmzufvbuqnznknltc)。

这个完整示例的目的，是实现一个用于展示层级树状信息的自定义布局，就像图 6-1 中的示意图那样。示例会先给出一段段代码，随后解释这些代码，并说明你在自定义过程中已经进行到哪一步。Collection view 的每个 section 对应树中的一层深度：Section 0 只包含 NSObject 单元格。Section 1 包含 NSObject 的所有子类单元格。Section 2 包含那些子类的所有子类单元格，依此类推。每个单元格都是自定义单元格，带有一个显示对应类名的标签，而单元格之间的连线则是补充视图。由于连线视图类必须判断要绘制多少条连线，它需要访问我们数据源中的数据。因此，把这些连线实现为补充视图而不是装饰视图才合理。

__图 6-1__  类的层级结构

!!

创建自定义布局的第一步，是对 [UICollectionViewLayout](https://developer.apple.com/documentation/uikit/uicollectionviewlayout) 类派生子类。这样做能为你提供构建自定义布局所必需的基础。

在本例中，需要一个自定义协议来告知布局某些项目之间的间距。如果特定项目的属性需要来自数据源的额外信息，那么为自定义布局实现一个[协议](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Protocol.html#//apple_ref/doc/uid/TP40008195-CH45)，要比直接与数据源建立连接更好。这样得到的布局更健壮、更可复用；它不会被绑死在某个特定的数据源上，而是能响应任何实现了其协议的对象。

清单 6-1 展示了这个自定义布局头文件中所需的代码。这样一来，任何实现了 _MyCustomProtocol_ 协议的类都可以使用这个自定义布局，而布局也能向该类查询它所需要的信息。

__清单 6-1__  连接到自定义协议

```objc
@interface MyCustomLayout : UICollectionViewLayout
@property (nonatomic, weak) id<MyCustomProtocol> customDataSource;
@end
```

接下来，由于 collection view 要管理的项目数量相对较少，这个自定义布局采用了一套缓存机制：在准备布局时存下它所生成的布局属性，之后每当 collection view 索取时再取回这些存好的值。清单 6-2 展示了我们的布局需要维护的三个私有属性以及 `init` 方法。`layoutInformation` 字典存放着我们 collection view 中所有类型视图的全部布局属性，`maxNumRows` 属性则记录着填满树中最高的那一列需要多少行。`insets` 对象控制单元格之间的间距，用于设置各视图的 frame 和内容尺寸。前两个属性的值在准备布局时设置，而 `insets` 对象应当用 `init` 方法来设置。在这里，`INSET_TOP`、`INSET_LEFT`、`INSET_BOTTOM` 和 `INSET_RIGHT` 指的是你为每个参数定义的常量。

__清单 6-2__  初始化变量

```objc
@interface MyCustomLayout()

@property (nonatomic) NSDictionary *layoutInformation;
@property (nonatomic) NSInteger maxNumRows;
@property (nonatomic) UIEdgeInsets insets;

@end

-(id)init {
    if(self = [super init]) {
        self.insets = UIEdgeInsetsMake(INSET_TOP, INSET_LEFT, INSET_BOTTOM, INSET_RIGHT);
    }
    return self;
}
```

这个自定义布局的最后一步是创建自定义布局属性。虽然这一步并非总是必要，但在本例中，当单元格被摆放时，代码需要访问当前单元格各个子单元格的索引路径，以便调整这些子单元格的 frame 来与其父单元格对齐。因此，对 [UICollectionViewLayoutAttributes](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes) 派生子类、用它存储该单元格的子单元格数组，就能提供这一信息。你对 `UICollectionViewLayoutAttributes` 派生子类，并在头文件中添加以下代码：

```objc
@property (nonatomic) NSArray *children;
```

正如 `UICollectionViewLayoutAttributes` 类参考中所解释的，在 iOS 7 及更高版本中，对布局属性派生子类要求你重写继承来的 [isEqual:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/isEqual:) 方法。有关原因的更多信息，请参阅 _[UICollectionViewLayoutAttributes Class Reference](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes)_。

在本例中，`isEqual:` 方法的实现很简单，因为只有一个字段需要比较——children 数组的内容。如果两个布局属性对象的数组相同，那么它们必定相等，因为子类只能属于一个类。清单 6-3 展示了 `isEqual:` 方法的实现。

__清单 6-3__  满足派生布局属性子类的要求

```objc
-(BOOL)isEqual:(id)object {
    MyCustomAttributes *otherAttributes = (MyCustomAttributes *)object;
    if ([self.children isEqualToArray:otherAttributes.children]) {
        return [super isEqual:object];
    }
    return NO;
}
```

记得在自定义布局文件中引入自定义布局属性的头文件。

到了这一步，你已经打好基础，可以开始实现自定义布局的主体部分了。

既然所有必要的组件都已初始化完毕，你就可以准备布局了。在布局过程中，collection view 首先调用 [prepareLayout](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617752-preparelayout) 方法。在本例中，`prepareLayout` 方法用于为 collection view 中的每一个视图实例化全部布局属性对象，然后把这些属性缓存进我们的 `layoutInformation` 字典中，供之后使用。有关 `prepareLayout` 方法的更多信息，请参阅[准备布局](Creating%20Custom%20Layouts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdgmzufvbuqnjnknltcoi)。

示例中 `prepareLayout` 方法的实现被拆成了两部分。图 6-2 展示了该方法前半部分的目标。这段代码会遍历每一个单元格，如果该单元格有子单元格，就把这些子单元格与父单元格关联起来。正如图中所示，这一过程会对每个单元格执行，包括那些本身就是其他父单元格的子单元格的单元格。

__图 6-2__  连接父索引路径与子索引路径

!

清单 6-4 展示了 `prepareLayout` 方法实现的前半部分。代码开头初始化的两个可变字典构成了缓存机制的基础。第一个 `layoutInformation` 是 `layoutInformation` 属性的局部对应物。创建一个局部可变副本，可以让实例变量保持为不可变的——这在这个自定义布局的实现中是合理的，因为布局属性在 `prepareLayout` 方法运行结束之后就不应再被修改。接着，代码按递增顺序遍历每一个 section，再遍历每个 section 内的每一个项目，为每个单元格创建属性。自定义方法 `attributesWithChildrenForIndexPath:` 返回一个自定义布局属性的实例，其 `children` 属性中填入的是当前索引路径处项目的各个子项的索引路径。随后，这个属性对象会以其索引路径为键，存入局部的 `cellInformation` 字典中。这次对所有项目的初始遍历，让代码能够先为每个项目设置好子项，再去设置该项目的 frame。

__清单 6-4__  创建布局属性

```objc
- (void)prepareLayout {
    NSMutableDictionary *layoutInformation = [NSMutableDictionary dictionary];
    NSMutableDictionary *cellInformation = [NSMutableDictionary dictionary];
    NSIndexPath *indexPath;
    NSInteger numSections = [self.collectionView numberOfSections;]
    for(NSInteger section = 0; section < numSections; section++){
        NSInteger numItems = [self.collectionView numberOfItemsInSection:section];
        for(NSInteger item = 0; item < numItems; item++){
            indexPath = [NSIndexPath indexPathForItem:item inSection:section];
            MyCustomAttributes *attributes =
            [self attributesWithChildrenAtIndexPath:indexPath];
            [cellInformation setObject:attributes forKey:indexPath];
        }
    }
    //第一部分结束
```


图 6-3 描绘了 `prepareLayout` 方法后半部分所发生的过程：树的层级结构是从最后一行向第一行反向构建的。这种做法乍看可能有些古怪，但它其实是一种巧妙的手法，能消除调整子单元格 frame 所带来的复杂性。因为子单元格的 frame 需要与其父单元格对齐，而逐行之间单元格的间距又取决于某个单元格有多少子单元格（还包括每个子单元格各自又有多少子单元格，依此类推），所以你会想先设置子单元格的 frame，再设置父单元格的。这样一来，子单元格及其全部子单元格就都能被调整到与它们总的父单元格对齐。

在第 1 步中，最后一列的各单元格已按顺序摆放完毕。在第 2 步中，布局正在确定第二列各单元格的 frame。在这一列中，由于没有任何单元格拥有超过一个子单元格，这些单元格可以顺序排布。不过，绿色单元格的 frame 必须与其父单元格对齐，因此它被向下移动了一格。在最后一步中，第一列的各单元格正在被摆放。第二列的前三个单元格是第一列第一个单元格的子单元格，所以第一列中位于第一个单元格之后的那些单元格被向下移动了。在本例中，其实并不需要这么做，因为跟在第一个之后的那两个单元格自身并没有子单元格，但布局对象并没有聪明到能看出这一点。相反，它总是预留出这段空间，以防跟在有子单元格的单元格之后的任何单元格自身也有子单元格。同样，两个绿色单元格现在都已向下移动，与它们各自的父单元格对齐。

__图 6-3__  确定 frame 的过程

!

清单 6-5 展示了 `prepareLayout` 方法的后半部分，其中设置了每个项目的 frame。某些代码行后面注释的编号，对应代码之后按编号给出的解释。

__清单 6-5__  存储布局属性

```objc
    //prepareLayout 实现的后续部分
    for(NSInteger section = numSections - 1; section >= 0; section—-){
        NSInteger numItems = [self.collectionView numberOfItemsInSection:section];
        NSInteger totalHeight = 0;
        for(NSInteger item = 0; item < numItems; item++){
            indexPath = [NSIndexPath indexPathForItem:item inSection:section];
            MyCustomAttributes *attributes = [cellInfo objectForKey:indexPath]; // 1
            attributes.frame = [self frameForCellAtIndexPath:indexPath
                                withHeight:totalHeight];
            [self adjustFramesOfChildrenAndConnectorsForClassAtIndexPath:indexPath]; // 2
            cellInfo[indexPath] = attributes;
            totalHeight += [self.customDataSource
                            numRowsForClassAndChildrenAtIndexPath:indexPath]; // 3
        }
        if(section == 0){
            self.maxNumRows = totalHeight; // 4
        }
    }
    [layoutInformation setObject:cellInformation forKey:@"MyCellKind"]; // 5
    self.layoutInformation = layoutInformation
}
```

在清单 6-5 中，代码按递减顺序遍历各个 section，从后向前构建这棵树。`totalHeight` 变量记录着当前项目需要向下偏移多少行。这个实现并没有精细地处理间距，而是简单地在有子单元格的单元格下方留出空白，以保证两个单元格的子单元格永远不会重叠，`totalHeight` 变量正是用来实现这一点的。代码按以下顺序完成这些工作：

1. 在设置单元格的 frame 之前，先从局部字典中取回我们第一次遍历数据时创建的布局属性。
2. 自定义方法 `adjustFramesOfChildrenAndConnectorsForClassAtIndexPath:` 会递归地调整该单元格的所有子单元格、孙单元格等等的 frame，使它们与该单元格的 frame 对齐。
3. 把调整后的属性放回字典之后，`totalHeight` 变量会被更新，以反映下一个项目的 frame 应该在什么位置。这里正是代码利用自定义协议之处。任何实现了该协议的对象都必须实现 `numRowsForClassAndChildrenAtIndexPath:` 方法，该方法根据某个类拥有多少子类，返回它需要占据多少行。
4. `maxNumRows` 属性（稍后用于设置内容尺寸）被设为 section 0 的总高度。高度最大的那一列始终是 section 0，因为这个实现没有包含精细的空间调整，它的高度是按树中所有子项调整过的。
5. 该方法的最后，把包含全部单元格属性的这个字典，以一个唯一的字符串标识符为键，插入到局部的 `layoutInformation` 字典中。

在最后一步中用于插入字典的那个字符串标识符，会贯穿这个自定义布局的其余部分，用来取回单元格对应的正确属性。等到示例后面引入补充视图时，它会变得更加重要。

在准备布局的过程中，代码把 `maxNumRows` 的值设成了布局中最大 section 的行数。这一信息可以用来设置合适的内容尺寸，而这正是布局过程的下一步。清单 6-6 展示了 [collectionViewContentSize](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617796-collectionviewcontentsize) 的实现。它依赖 `ITEM_WIDTH` 和 `ITEM_HEIGHT` 这两个常量，我们假定它们在整个应用中是全局的（例如，自定义单元格的实现中也需要用它们来正确设置单元格标签的尺寸）。

__清单 6-6__  设定内容区域的尺寸

```objc
- (CGSize)collectionViewContentSize {
    CGFloat width = self.collectionView.numberOfSections * (ITEM_WIDTH + self.insets.left + self.insets.right);
    CGFloat height = self.maxNumRows * (ITEM_HEIGHT + _insets.top + _insets.bottom);
    return CGSizeMake(width, height);
}
```


在所有布局属性对象都已初始化并缓存之后，代码就完全有能力提供 [layoutAttributesForElementsInRect:](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617769-layoutattributesforelementsinrec) 方法中所请求的全部布局信息了。这个方法是布局过程的第二步，而且与 `prepareLayout` 方法不同，它是必需的。该方法给出一个矩形，并期望得到一个数组，包含该矩形内所有视图的布局属性对象。在某些情况下，容纳着成千上万个项目的 collection view 可能会等到这个方法被调用时，才只为该矩形内所包含的元素初始化布局属性对象，但本实现依赖的是缓存。因此，`layoutAttributesForElementsInRect:` 方法只需遍历所有存好的属性，把它们收集到一个数组中返回给调用方即可。

清单 6-7 展示了 `layoutAttributesForElementsInRect:` 方法的实现。代码遍历主字典 `_layoutInformation` 中那些分别存放特定类型视图布局属性对象的子字典。如果在子字典中检查到的属性位于给定矩形内，就把它们加入一个存放该矩形内全部属性的数组；等所有存好的属性都检查完毕后，返回这个数组。

__清单 6-7__  收集并处理已存储的属性

```objc
- (NSArray*)layoutAttributesForElementsInRect:(CGRect)rect {
    NSMutableArray *myAttributes [NSMutableArray arrayWithCapacity:self.layoutInformation.count];
    for(NSString *key in self.layoutInformation){
        NSDictionary *attributesDict = [self.layoutInformation objectForKey:key];
        for(NSIndexPath *key in attributesDict){
            UICollectionViewLayoutAttributes *attributes =
            [attributesDict objectForKey:key];
            if(CGRectIntersectsRect(rect, attributes.frame)){
                [attributes addObject:attributes];
            }
        }
    }
    return myAttributes;
}
```


正如[按需提供布局属性](Creating%20Custom%20Layouts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdgmzufvbuqnjnknlte)一节中所讨论的，一旦布局过程完成，布局对象就必须做好准备，随时为你 collection view 中任何一种视图的任何单个项目返回布局属性。三种视图（单元格、补充视图和装饰视图）都有对应的方法，但目前这个应用只使用了单元格，所以眼下唯一需要实现的方法就是 [layoutAttributesForItemAtIndexPath:](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617797-layoutattributesforitematindexpa)。

清单 6-8 展示了这个方法的实现。它进入存放单元格的那个字典，并在该子字典中返回以指定索引路径为键存储的属性对象。

__清单 6-8__  为特定项目提供属性

```objc
- (UICollectionViewLayoutAttributes *)layoutAttributesForItemAtIndexPath:(NSIndexPath *)indexPath {
    return self.layoutInfo[@"MyCellKind"][indexPath];
}
```

图 6-4 展示了代码进行到这里时布局的样子。所有单元格都已摆放好，并被正确地调整到与它们的父单元格对齐，但连接它们的连线还没有绘制出来。

__图 6-4__  目前为止的布局

!!

以现在的状态，这个应用已经能在层级意义上正确地显示所有单元格，但由于没有连线把父单元格和子单元格连起来，这张类图很难看懂。为了绘制连接类单元格与其子单元格的连线，这个应用的实现依赖于一个可以作为补充视图整合进布局的自定义视图。有关设计补充视图的更多信息，请参阅[用补充视图衬托内容](Creating%20Custom%20Layouts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdgmzufvbuqnjnknltemq)。

清单 6-9 展示了可以整合进 `prepareLayout` 实现中、用来纳入补充视图的那些代码行。为单元格创建属性对象与为补充视图创建属性对象之间的细微差别在于，补充视图对应的方法需要一个字符串标识符，用来说明这个属性对象是给哪一种补充视图的。这是因为一个自定义布局可以有多种不同类型的补充视图，而每个布局只能有一种类型的单元格。

__清单 6-9__  为补充视图创建属性对象

```objc
// 再创建一个字典，专门存放补充视图的属性
NSMutableDictionary *supplementaryInfo = [NSMutableDictionary dictionary];
…
// 在对数据的第一次遍历中，同时为补充视图创建一组属性
UICollectionViewLayoutAttributes *supplementaryAttributes = [UICollectionViewLayoutAttributes layoutAttributesForSupplementaryViewOfKind:@"ConnectionViewKind" withIndexPath:indexPath];
[supplementaryInfo setObject: supplementaryAttributes forKey:indexPath];
…
// 在对数据的第二次遍历中，像为单元格所做的那样为补充视图设置 frame
UICollectionViewLayoutAttributes *supplementaryAttributes = [supplementaryInfo objectForKey:indexPath];
supplementaryAttributes.frame = [self frameForSupplementaryViewOfKind:@"ConnectionViewKind" AtIndexPath:indexPath];
[supplementaryInfo setObject:supplementaryAttributes ForKey:indexPath];
...
// 在设置 _layoutInformation 的实例版本之前，把局部的 supplementaryInfo 字典插入局部的 layoutInformation 字典
[layoutInformation setObject:supplementaryInfo forKey:@"ConnectionViewKind"];
```

由于补充视图的代码与单元格的代码类似，把这些代码整合进 `prepareLayout` 方法很简单。代码对补充视图采用了与单元格相同的缓存机制，用了另一个专门对应 _ConnectionViewKind_ 补充视图的字典。如果你打算添加不止一种补充视图，就要为那种视图再创建一个字典，并同样为那种视图添加上面这些代码行。不过在本例中，布局只需要一种补充视图。与初始化单元格布局属性的代码一样，这个实现使用了自定义方法 `frameForSupplementaryViewOfKind:AtIndexPath:`，根据视图的种类来确定补充视图的 frame。记住，`prepareLayout` 方法实现中出现的自定义方法 `adjustFramesOfChildrenAndConnectorsForClassAtIndexPath:` 也需要把与这个类层级布局相关的所有补充视图的调整纳入进来。

在这段示例代码中，`layoutAttributesForElementsInRect:` 的实现不需要做任何修改，因为它本来就被设计成遍历主字典中存储的全部属性。只要补充视图的属性被加入了主字典，前面给出的 `layoutAttributesForElementsInRect:` 实现就能按预期工作。

最后，和单元格的情况一样，collection view 可能随时请求特定视图的补充视图属性。因此，必须实现 [layoutAttributesForSupplementaryElementOfKind:atIndexPath:](https://developer.apple.com/documentation/uikit/uicollectionview/1618012-layoutattributesforsupplementary)。

清单 6-10 展示了该方法的实现，它与 `layoutAttributesForItemAtIndexPath:` 的实现几乎相同。不同之处在于，使用传入的 `kind` 字符串、而不是把某种视图硬编码进返回值，能让你在自定义布局中使用多种补充视图。

__清单 6-10__  按需提供补充视图属性

```objc
- (UICollectionViewLayoutAttributes *) layoutAttributesForSupplementaryViewOfKind:(NSString *)kind atIndexPath:(NSIndexPath *)indexPath {
    return self.layoutInfo[kind][indexPath];
}
```


加入补充视图之后，你现在就有了一个能够充分再现类层级示意图的布局对象。在最终的实现中，你或许还想在自定义布局中加入一些调整以节省空间。这个示例探讨了一个真实的、基础的自定义 collection view 布局实现大致是什么样子。Collection view 极其强大，能提供的能力远不止这里所展示的。在单元格被移动、插入或删除时对其进行高亮和选中（甚至添加动画），都是可以轻松整合进你应用的增强功能。要把你的自定义布局提升到新的层次，请看看[创建自定义布局](Creating%20Custom%20Layouts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdgmzufvbuqnjnknltc)最后几节的内容。

[下一页](Document%20Revision%20History.md)[上一页](Creating%20Custom%20Layouts.md)

