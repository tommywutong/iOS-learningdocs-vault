---
title: Cocoa 编码规范
apple_id: 10000146i
resource_type: Guide
platform: watchOS|iOS|macOS
topic: General
technology: null
published: '2013-10-22'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CodingGuidelines/Articles/NamingMethods.html
archived_at: '2026-07-15T07:13:28.303066Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [Cocoa 编码规范](Introduction%20to%20Coding%20Guidelines%20for%20Cocoa.md)


[下一页](Naming%20Functions.md)[上一页](Code%20Naming%20Basics.md)

# 方法命名

方法大概是编程接口中最常见的元素，所以你在给它们命名时要格外用心。本节讨论方法命名的以下几个方面：

给方法命名时，请记住以下几条通用准则：

- 以小写字母开头，内嵌单词的首字母大写。不要使用前缀（prefix）。参见[排版约定](Code%20Naming%20Basics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi4dcljrgaydeojtge)。

  这些准则有两个具体的例外。你可以用大写的知名首字母缩略词（acronym）作为方法名的开头（比如 TIFF 或 PDF），也可以用前缀来归类和标识私有方法（参见[私有方法](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi4deljrgaydgobshe)）。
- 对于表示对象所执行动作的方法，以动词开头：

```objc
- (void)invokeWithTarget:(id)target;
- (void)selectTabViewItem:(NSTabViewItem *)tabViewItem
```

  不要把“do”或“does”放进方法名，因为这些助动词几乎不增加任何含义。另外，绝不要在动词前面加副词或形容词。
- 如果方法返回的是接收者的某个属性，就以该属性来命名方法。除非有一个或多个值是间接返回的，否则没必要用“get”。

|  |  |
| --- | --- |
| `- (NSSize)cellSize;` | 正确。 |
| `- (NSSize)calcCellSize;` | 错误。 |
| `- (NSSize)getCellSize;` | 错误。 |

  另请参阅[存取方法](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi4deljrgaydimrqgi)。
- 在所有参数前面都加上关键字。

|  |  |
| --- | --- |
| `- (void)sendAction:(SEL)aSelector toObject:(id)anObject forAllCells:(BOOL)flag;` | 正确。 |
| `- (void)sendAction:(SEL)aSelector :(id)anObject :(BOOL)flag;` | 错误。 |
- 参数前面的那个词要能描述该参数。

|  |  |
| --- | --- |
| `- (id)viewWithTag:(NSInteger)aTag;` | 正确。 |
| `- (id)taggedView:(int)aTag;` | 错误。 |
- 当你创建的方法比继承来的方法更具体时，在已有方法名的末尾追加新的关键字。

|  |  |
| --- | --- |
| `- (id)initWithFrame:(CGRect)frameRect;` | `NSView`、`UIView`。 |
| `- (id)initWithFrame:(NSRect)frameRect mode:(int)aMode cellClass:(Class)factoryId numberOfRows:(int)rowsHigh numberOfColumns:(int)colsWide;` | NSMatrix，NSView 的子类 |
- 不要用“and”去连接那些同为接收者属性的关键字。

|  |  |
| --- | --- |
| `- (int)runModalForDirectory:(NSString *)path file:(NSString *) name types:(NSArray *)fileTypes;` | 正确。 |
| `- (int)runModalForDirectory:(NSString *)path andFile:(NSString *)name andTypes:(NSArray *)fileTypes;` | 错误。 |

  在这个例子里“and”听起来似乎不错，但当你写出关键字越来越多的方法时，它就会带来麻烦。
- 如果方法描述的是两个彼此独立的动作，就用“and”把它们连起来。

|  |  |
| --- | --- |
| `- (BOOL)openFile:(NSString *)fullPath withApplication:(NSString *)appName andDeactivate:(BOOL)flag;` | `NSWorkspace`。 |

[存取方法](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/AccessorMethod.html#//apple_ref/doc/uid/TP40008195-CH2)（accessor method）是用来设置和返回对象某个属性值的方法。根据属性的表达方式不同，它们有几种推荐的形式：

- 如果属性用名词表达，形式为：

  `- (`_type_`)`_noun_`;`

  `- (void)set`_Noun_:`(`_type_`)`_aNoun_;

  例如：

```objc
- (NSString *)title;
- (void)setTitle:(NSString *)aTitle;
```
- 如果属性用形容词表达，形式为：

  `- (BOOL)is`_Adjective_`;`

  `- (void)set`_Adjective_:`(BOOL)flag`;

  例如：

```objc
- (BOOL)isEditable;
- (void)setEditable:(BOOL)flag;
```
- 如果属性用动词表达，形式为：

  `- (BOOL)`_verbObject_`;`

  `- (void)set`_VerbObject_:`(BOOL)flag`;

  例如：

```objc
- (BOOL)showsAlpha;
- (void)setShowsAlpha:(BOOL)flag;
```

  动词应当用一般现在时。
- 不要用分词把动词硬掰成形容词：

|  |  |
| --- | --- |
| `- (void)setAcceptsGlyphInfo:(BOOL)flag;` | 正确。 |
| `- (BOOL)acceptsGlyphInfo;` | 正确。 |
| `- (void)setGlyphInfoAccepted:(BOOL)flag;` | 错误。 |
| `- (BOOL)glyphInfoAccepted;` | 错误。 |
- 你可以用情态动词（前面带“can”“should”“will”等的动词）来让含义更清楚，但不要用“do”或“does”。

|  |  |
| --- | --- |
| `- (void)setCanHide:(BOOL)flag;` | 正确。 |
| `- (BOOL)canHide;` | 正确。 |
| `- (void)setShouldCloseDocument:(BOOL)flag;` | 正确。 |
| `- (BOOL)shouldCloseDocument;` | 正确。 |
| `- (void)setDoesAcceptGlyphInfo:(BOOL)flag;` | 错误。 |
| `- (BOOL)doesAcceptGlyphInfo;` | 错误。 |
- 只有在方法间接返回对象和值时才使用“get”。只有当需要返回多个项时，才应该采用这种形式。

|  |  |
| --- | --- |
| `- (void)getLineDash:(float *)pattern count:(int *)count phase:(float *)phase;` | `NSBezierPath`。 |

  在这类方法的实现中，应当允许这些输入输出参数传入 `NULL`，以此表示调用者对其中一个或多个返回值不感兴趣。

委托方法（delegate method，也叫 delegation method）是指当某些事件发生时，对象在其[委托](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14)（delegate）上调用的方法（前提是委托实现了它们）。它们有一套独特的形式，这套形式同样适用于在对象的数据源上调用的方法：

- 名称以发送[消息](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Message.html#//apple_ref/doc/uid/TP40008195-CH59)的那个对象的类名开头：

```objc
- (BOOL)tableView:(NSTableView *)tableView shouldSelectRow:(int)row;
- (BOOL)application:(NSApplication *)sender openFile:(NSString *)filename;
```

  类名要去掉前缀，并且首字母小写。
- 类名后面要加冒号（该参数是对发出委托的对象的引用），除非该方法只有一个参数，即发送者本身。

```objc
- (BOOL)applicationOpenUntitledFile:(NSApplication *)sender;
```
- 因通知被发布而调用的方法是个例外。这种情况下，唯一的参数是通知对象。

```objc
- (void)windowDidChangeScreen:(NSNotification *)notification;
```
- 对于用来通知委托某事已经发生或即将发生的方法，使用“did”或“will”。

```objc
- (void)browserDidScroll:(NSBrowser *)sender;
- (NSUndoManager *)windowWillReturnUndoManager:(NSWindow *)window;
```
- 对于用来请求委托代表另一个对象做某事的方法，虽然也可以用“did”或“will”，但更推荐用“should”。

```objc
- (BOOL)windowShouldClose:(id)sender;
```


对于管理一组对象[集合](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Collection.html#//apple_ref/doc/uid/TP40008195-CH10)的对象（集合中的每个对象称为一个元素），惯例是提供如下形式的方法：

`- (void)add`_Element_`:(`_elementType_`)`_anObj_`;`

`- (void)remove`_Element_`:(`_elementType_`)`_anObj_`;`

`- (NSArray *)`_elements_`;`

例如：

```objc
- (void)addLayoutManager:(NSLayoutManager *)obj;
- (void)removeLayoutManager:(NSLayoutManager *)obj;
- (NSArray *)layoutManagers;
```

对这条准则还有一些限定和细化：

- 如果集合确实是无序的，就返回 NSSet 对象而不是 NSArray 对象。
- 如果需要把元素插入到集合中的特定位置，就使用类似下面这样的方法，用它们替代上面那些方法或作为补充：

```objc
- (void)insertLayoutManager:(NSLayoutManager *)obj atIndex:(int)index;
- (void)removeLayoutManagerAtIndex:(int)index;
```

关于集合方法，有几个实现细节需要留意：

- 这些方法通常意味着对被插入对象的所有权，所以添加或插入它们的代码必须保留（retain）它们，移除它们的代码也必须释放（release）它们。
- 如果被插入的对象需要有一个指回主对象的指针，通常的做法是用一个 `set...` 方法来设置这个回指指针，但不保留它。以 `insertLayoutManager:atIndex:` 方法为例，NSLayoutManager 类就是通过下面这些方法做到的：

```objc
- (void)setTextStorage:(NSTextStorage *)textStorage;
- (NSTextStorage *)textStorage;
```

  正常情况下你不会直接调用 `setTextStorage:`，但可能想要[覆写](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/MethodOverriding.html#//apple_ref/doc/uid/TP40008195-CH57)它。

上述集合方法约定的另一个例子来自 NSWindow 类：

```objc
- (void)addChildWindow:(NSWindow *)childWin ordered:(NSWindowOrderingMode)place;
- (void)removeChildWindow:(NSWindow *)childWin;
- (NSArray *)childWindows;

- (NSWindow *)parentWindow;
- (void)setParentWindow:(NSWindow *)window;
```


关于方法参数的命名，有几条通用规则：

- 和方法一样，参数以小写字母开头，后续各单词的首字母大写（例如 `removeObject:(id)anObject`）。
- 名称中不要出现“pointer”或“ptr”。是不是指针，应该由参数的类型而不是名称来说明。
- 避免用一两个字母的参数名。
- 避免只省下几个字母的缩写。

按照（[Cocoa](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Cocoa.html#//apple_ref/doc/uid/TP40008195-CH9) 的）传统，下列关键字和参数是搭配使用的：

```objc
...action:(SEL)aSelector
...alignment:(int)mode
...atIndex:(int)index
...content:(NSRect)aRect
...doubleValue:(double)aDouble
...floatValue:(float)aFloat
...font:(NSFont *)fontObj
...frame:(NSRect)frameRect
...intValue:(int)anInt
...keyEquivalent:(NSString *)charCode
...length:(int)numBytes
...point:(NSPoint)aPoint
...stringValue:(NSString *)aString
...tag:(int)anInt
...target:(id)anObject
...title:(NSString *)aString
```


大多数情况下，私有方法的命名规则与公开方法基本相同。不过常见的做法是给私有方法加一个前缀，好让它们容易与公开方法区分开。即便有了这条约定，私有方法的命名仍可能引出一类特殊的问题：当你为某个 Cocoa 框架类派生子类时，你无法知道自己的私有方法会不会在无意中覆写了框架中同名的私有方法。

Cocoa 框架中大多数私有方法的名称都带有下划线前缀（例如 `_fooData`），以此标记它们是私有的。由此可以得出两条建议。

- 不要用下划线作为你自己私有方法的前缀。Apple 保留了这一约定。
- 如果你正在为一个庞大的 Cocoa 框架类（比如 `NSView` 或 `UIView`）派生子类，并且想绝对确保自己的私有方法与超类中的方法不重名，那就给私有方法加上你自己的前缀。这个前缀应当尽可能独特，可以基于你的公司或项目来取，形式为 "XX_"。所以，如果你的项目叫 Byte Flogger，前缀就可以是 `BF_addObject:`。

给私有方法加前缀的建议，看上去似乎与前面“方法存在于其类的命名空间中”的说法相矛盾，但这里的意图不同：是为了防止无意中覆写超类的私有方法。

[下一页](Naming%20Functions.md)[上一页](Code%20Naming%20Basics.md)

