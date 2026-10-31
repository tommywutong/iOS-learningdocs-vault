---
title: 值对象
source: objc.io
source_key: objcio
source_url: 'https://www.objc.io/issues/7-foundation/value-objects'
original_language: en
published: ''
status: frozen
license: 未声明（页面无版权声明，文章版权归各作者）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:1566d9838d0026d5'
translated: true
---

> 原文：[Value Objects](https://www.objc.io/issues/7-foundation/value-objects)　·　objc.io

本文将介绍如何在 Objective-C 中编写[值对象](http://en.wikipedia.org/wiki/Value_object)。在此过程中，我们会触及 Objective-C 中若干重要的协议与方法。值对象是保存若干值、并可比较相等性的对象。值对象常被用作模型对象。例如，考虑一个简单的 `Person` 对象：

```
@interface Person : NSObject

@property (nonatomic,copy) NSString* name;
@property (nonatomic) NSDate* birthDate;
@property (nonatomic) NSUInteger numberOfKids;

@end
```

创建这类对象是我们日常工作的基本功。这些对象看起来简单得有些骗人，其中其实有不少微妙之处。

许多人是用惨痛教训学到的：这些对象应当是不可变的。一旦创建了 `Person` 对象，就无法再修改它。本期稍后我们会讨论可变性。

## 属性

首先要注意的是，我们用属性来定义 `Person` 所具有的那些特性。创建属性相当机械：对普通属性，设为 `nonatomic`。默认情况下，对象属性是 `strong`，标量属性是 `assign`。有一个例外：对于存在可变对应类型的属性，你应将其定义为 `copy`。例如，`name` 属性的类型是 `NSString`。可能发生的情况是：有人创建了一个 `Person` 对象，并赋了一个 `NSMutableString` 类型的值。之后某时，他又修改了这个可变字符串。如果我们的属性是 `strong` 而不是 `copy`，我们的 `Person` 对象也会随之改变，这不是我们想要的。容器同理，例如数组或字典。

请注意，拷贝是浅拷贝；容器中仍可能包含可变对象。例如，若你有一个包含 `NSMutableDictionary` 元素的 `NSMutableArray* a`，则 `[a copy]` 会给你一个不可变数组，但元素仍是同一个 `NSMutableDictionary` 对象。如后文所述，对不可变对象执行 copy 是免费的，只是增加 retain 计数。

在较旧的代码中，你可能看不到属性，因为它们是 Objective-C 相对较新的补充。代替属性的，可能是自定义 getter/setter，或普通实例变量。对现代代码，多数人似乎都同意使用属性，我们也推荐这样做。

**延伸阅读：** [`NSString`：`copy` 还是 `retain`](http://stackoverflow.com/questions/387959/nsstring-property-copy-or-retain)

## 初始化方法

若我们想要不可变对象，就应确保创建之后无法再修改。做法是添加初始化方法，并在接口中把属性设为 readonly。接口于是如下所示：

```
@interface Person : NSObject

@property (nonatomic,readonly) NSString* name;
@property (nonatomic,readonly) NSDate* birthDate;
@property (nonatomic,readonly) NSUInteger numberOfKids;

- (instancetype)initWithName:(NSString*)name
                   birthDate:(NSDate*)birthDate
                numberOfKids:(NSUInteger)numberOfKids;

@end
```

然后在实现中，我们必须使用实例变量而不是属性：

```
@implementation Person

- (instancetype)initWithName:(NSString*)name
                   birthDate:(NSDate*)birthDate
                numberOfKids:(NSUInteger)numberOfKids
{
    self = [super init];
    if (self) {
        _name = [name copy];
        _birthDate = birthDate;
        _numberOfKids = numberOfKids;
    }
    return self;
}

@end
```

现在我们可以构造新的 `Person` 对象，但无法再修改它们。这非常有帮助：在编写与 `Person` 对象协作的其他类时，我们知道这些值在使用过程中不会改变。另请注意，`copy` 已不再出现在接口中：它现在是实现细节。

## 相等性比较

要比较相等性，必须实现 `isEqual:` 方法。我们希望当且仅当所有属性都相等时，`isEqual:` 为真。Mike Ash（[Implement Equality and Hashing](http://www.mikeash.com/pyblog/friday-qa-2010-06-18-implementing-equality-and-hashing.html)）和 NSHipster（[Equality](http://nshipster.com/equality/)）有两篇不错的文章解释如何做。首先来写 `isEqual:`：

```
- (BOOL)isEqual:(id)obj
{
    if(![obj isKindOfClass:[Person class]]) return NO;
    
    Person* other = (Person*)obj;

    BOOL nameIsEqual = self.name == other.name || [self.name isEqual:other.name];
    BOOL birthDateIsEqual = self.birthDate == other.birthDate || [self.birthDate isEqual:other.birthDate];
    BOOL numberOfKidsIsEqual = self.numberOfKids == other.numberOfKids;
    return nameIsEqual && birthDateIsEqual && numberOfKidsIsEqual;
}
```

现在我们检查是否是同一种类。若不是，肯定不相等。然后对每个对象属性，检查指针是否相等。`||` 的左操作数看似多余，但它是为了在两个属性都是 `nil` 时返回 `YES`。要比较如 `NSUInteger` 这样的标量是否相等，直接用 `==` 即可。

值得注意的一点：这里我们把不同属性拆成各自的 `BOOL`。实践中，把它们合并成一个大子句可能更合理，因为那样可以免费获得惰性求值。在上面的例子中，若 `name` 不相等，就不需要再检查其他属性。把所有条件合并到一个 if 语句中，就能免费获得该优化。

接下来，[按文档要求](https://developer.apple.com/library/mac/documentation/cocoa/reference/foundation/Protocols/NSObject_Protocol/Reference/NSObject.html#//apple_ref/occ/intfm/NSObject/isEqual:)，我们还需要实现 hash 函数。Apple 说：

> 若两个对象相等，它们必须具有相同的哈希值。若你在子类中定义了 isEqual:，并打算将该子类的实例放入集合，这一点尤为重要。务必也在子类中定义 hash。

首先，我们可以在没有实现 `hash` 函数的情况下，尝试运行以下代码：

```
Person* p1 = [[Person alloc] initWithName:name birthDate:start numberOfKids:0];
Person* p2 = [[Person alloc] initWithName:name birthDate:start numberOfKids:0];
NSDictionary* dict = @{p1: @"one", p2: @"two"};
NSLog(@"%@", dict);
```

我第一次跑上面的代码时，一切还算正常，字典里有两项。第二次就只剩一项了。事情变得非常不可预测，所以还是按文档说的做吧。

你可能还记得计算机课上的内容：写一个好的哈希函数并不容易。好的哈希函数需要是*确定性的*且*均匀的*。确定性意味着相同输入必须生成相同的哈希值。均匀意味着哈希函数的结果应把输入均匀映射到输出范围上。输出越均匀，在集合中使用这些对象时性能越好。

先来看看——纯粹为了好玩——没有哈希函数时，把 `Person` 对象用作字典的键会发生什么：

```
NSMutableDictionary* dictionary = [NSMutableDictionary dictionary];

NSDate* start = [NSDate date];
for (int i = 0; i < 50000; i++) {
    NSString* name = randomString();
    Person* p = [[Person alloc] initWithName:name birthDate:[NSDate date] numberOfKids:i++];
    [dictionary setObject:@"value" forKey:p];
}
NSLog(@"%f", [[NSDate date] timeIntervalSinceDate:start]);
```

在我的机器上这花了 29 秒。相比之下，实现一个基本的 `hash` 函数后，同样的代码只需 0.4 秒。这些不是严谨的基准测试，但足以很好地说明为何实现正确的 `hash` 函数很重要。对 `Person` 类，我们可以从这样的哈希函数开始：

```
- (NSUInteger)hash
{
    return self.name.hash ^ self.birthDate.hash ^ self.numberOfKids;
}
```

这会取三个属性的哈希并用 `XOR` 组合。在这种情况下，对我们的用途已经够好了，因为 `NSString` 的哈希函数对短字符串表现不错（它曾经只对[最多 96 个字符](http://www.abakia.de/blog/2012/12/05/nsstring-hash-is-bad/)的字符串表现良好，但现在已有改变。见 [CFString.c](http://www.opensource.apple.com/source/CF/CF-855.11/CFString.c)，搜索 `hash`）。对于严肃的哈希，你的哈希函数取决于你拥有的数据。这在 [Mike Ash 的文章](http://www.mikeash.com/pyblog/friday-qa-2010-06-18-implementing-equality-and-hashing.html)和[其他地方](http://www.burtleburtle.net/bob/hash/spooky.html)有所讨论。

在 `hash` 的[文档](https://developer.apple.com/library/mac/documentation/cocoa/Reference/Foundation/Protocols/NSObject_Protocol/Reference/NSObject.html#//apple_ref/occ/intfm/NSObject/hash)中有如下段落：

> 若一个可变对象被添加到使用哈希值确定对象在集合中位置的集合中，该对象的 hash 方法返回的值在对象留在集合中期间不得改变。因此，要么 hash 方法不得依赖对象的任何内部状态信息，要么你必须确保对象在集合中时内部状态信息不改变。于是，例如，可以把一个可变字典放入哈希表，但在它在里面时不得修改它。（注意，要知道某个给定对象是否在集合中可能很困难。）

这是确保对象不可变的另一个非常重要的理由。那样你根本不必担心这个问题。

**延伸阅读：**

- [A hash function for CGRect](https://gist.github.com/steipete/6133152)
- [A Hash Function for Hash Table Lookup](http://www.burtleburtle.net/bob/hash/doobs.html)
- [SpookyHash: a 128-bit noncryptographic hash](http://www.burtleburtle.net/bob/hash/spooky.html)
- [Why do hash functions use prime numbers?](http://computinglife.wordpress.com/2008/11/20/why-do-hash-functions-use-prime-numbers/)

## NSCopying

为确保对象好用，实现 `NSCopying` 协议很方便。例如，这让我们可以在容器类中使用它们。对我们类的可变变体，`NSCopying` 可以这样实现：

```
- (id)copyWithZone:(NSZone *)zone
{
    Person* p = [[Person allocWithZone:zone] initWithName:self.name
                                                birthDate:self.birthDate
                                             numberOfKids:self.numberOfKids];
    return p;
}
```

不过，协议文档中还提到了另一种实现 `NSCopying` 的方式：

> 当类及其内容都是不可变的时，通过 retain 原始对象而不是创建新拷贝来实现 NSCopying。

因此，对我们的不可变版本，可以只做这样：

```
- (id)copyWithZone:(NSZone *)zone
{
    return self;
}
```

## NSCoding

若要序列化对象，可以通过实现 `NSCoding` 来完成。该协议由两个必需方法组成：

```
- (id)initWithCoder:(NSCoder *)decoder
- (void)encodeWithCoder:(NSCoder *)encoder
```

实现它与实现相等性方法同样直截了当，同样相当机械：

```
- (id)initWithCoder:(NSCoder *)aDecoder
{
    self = [super init];
    if (self) {
        _name = [aDecoder decodeObjectForKey:@"name"];
        _birthDate = [aDecoder decodeObjectForKey:@"birthDate"];
        _numberOfKids = [aDecoder decodeIntegerForKey:@"numberOfKids"];
    }
    return self;
}

- (void)encodeWithCoder:(NSCoder *)aCoder
{
    [aCoder encodeObject:self.name forKey:@"name"];
    [aCoder encodeObject:self.birthDate forKey:@"birthDate"];
    [aCoder encodeInteger:self.numberOfKids forKey:@"numberOfKids"];
}
```

更多内容见 [NSHipster](http://nshipster.com/nscoding/) 和 [Mike Ash 的博客](http://www.mikeash.com/pyblog/friday-qa-2013-08-30-model-serialization-with-property-lists.html)。顺便说，处理不可信来源（例如来自网络的数据）时不要使用 `NSCoding`，因为数据可能被篡改。通过[修改归档数据](https://developer.apple.com/library/mac/documentation/security/conceptual/securecodingguide/Articles/ValidatingInput.html#//apple_ref/doc/uid/TP40007246-SW9)，完全可能发动远程代码执行攻击。应改用 [`NSSecureCoding`](http://nshipster.com/nssecurecoding/) 或像 JSON 这样的自定义格式。

## Mantle

现在留下的问题是：我们能自动化这些吗？事实证明可以。一种方式是代码生成，但幸运的是有更好的替代方案：[Mantle](https://github.com/github/Mantle)。Mantle 利用自省来生成 `isEqual:` 和 `hash`。此外，它还提供帮助你创建字典的方法，这些字典随后可用于读写 JSON。当然，以通用方式在运行时做这些不会像自己手写那样高效，但另一方面，自动完成这一过程出错的可能性小得多。

## 可变性

在 C 中，以及在 Objective-C 中，可变值是默认的。某种程度上它们非常方便，因为你可以随时改变任何东西。构建较小系统时，这通常不是问题。然而，正如许多人用惨痛教训学到的，构建较大系统时，事物不可变会容易得多。在 Objective-C 中，我们早已有了不可变对象，现在其他语言也开始加入这一点。

我们来看可变对象的两个问题。一是它们可能在你不期望时发生变化，二是在多线程上下文中使用可变对象的问题。

### 意外的变化

假设我们有一个 table view controller，带有 `people` 属性：

```
@interface ViewController : UITableViewController

@property (nonatomic) NSArray* people;

@end
```

在实现中，我们只是把每个数组元素映射到一个 cell：

```
 - (NSInteger)numberOfSectionsInTableView:(UITableView*)tableView
 {
     return 1;
 }
 
 - (NSInteger)tableView:(UITableView*)tableView numberOfRowsInSection:(NSInteger)section
 {
     return self.people.count;
 }
```

现在，在设置上述 view controller 的代码中，我们可能有这样的代码：

```
self.items = [NSMutableArray array];
[self loadItems]; // Add 100 items to the array
tableVC.people = self.items;
[self.navigationController pushViewController:tableVC animated:YES];
```

table view 会开始触发如 `tableView:numberOfRowsInSection:` 这样的方法，起初一切正常。但假设在某个时刻我们做了如下操作：

```
[self.items removeObjectAtIndex:1];
```

这改变了我们的 `items` 数组，但*同时也*改变了 table view controller 中的 `people` 数组。若我们在没有进一步与 table view controller 通信的情况下这样做，table view 仍会认为有 100 项，而我们的数组只剩 99 项。坏事就会发生。相反，我们本应把属性声明为 `copy`：

```
 @interface ViewController : UITableViewController
 
 @property (nonatomic, copy) NSArray* items;
 
 @end
```

现在，每当我们把可变数组赋给 items 时，都会制作一份不可变拷贝。若赋的是普通（不可变）数组值，copy 操作是免费的，只是增加 retain 计数。

### 多线程

假设我们有一个可变对象 `Account`，表示银行账户，带有方法 `transfer:to:`：

```
- (void)transfer:(double)amount to:(Account*)otherAccount
{
    self.balance = self.balance - amount;
    otherAccount.balance = otherAccount.balance + amount;
}
```

多线程代码可能以许多方式出错。例如，若线程 A 读取了 `self.balance`，线程 B 可能在线程 A 继续之前修改它。关于所涉全部危险的精彩解释，见我们的[第二期](https://www.objc.io/issues/2-concurrency/)。

若改用不可变对象，事情就容易得多。我们无法修改它们，这迫使我们在完全不同的层面提供可变性，从而得到简单得多的代码。

### 缓存

不可变性还能帮助缓存值。例如，假设你已把一份 markdown 文档解析成树结构，各节点对应不同元素。若要从中生成 HTML，你可以缓存该值，因为你知道子节点永远不会改变。若是可变对象，你要么每次从头生成 HTML，要么构建优化并观察每一个对象。有了不可变性，你不必担心缓存失效。当然，这可能带来性能代价。但几乎在所有情况下，简洁性都会胜过轻微的性能下降。

### 其他语言中的不可变性

不可变对象是受 [Haskell](http://www.haskell.org/) 等函数式编程语言启发的概念之一。在 Haskell 中，值默认不可变。Haskell 程序通常有一个[纯函数式](http://en.wikipedia.org/wiki/Purely_functional)核心，其中没有可变对象、没有状态、也没有如 I/O 这样的副作用。

我们可以把这一点学到 Objective-C 编程中。尽可能使用不可变对象，程序会更容易测试。Gary Bernhardt 有一场精彩的[演讲](https://www.destroyallsoftware.com/talks/boundaries)，展示了不可变对象如何帮助我们写出更好的软件。演讲中他用的是 Ruby，但这些概念同样适用于 Objective-C。

**进一步阅读：**

- [Cocoa Encyclopedia: Object Mutability](https://developer.apple.com/library/mac/documentation/General/Conceptual/CocoaEncyclopedia/ObjectMutability/ObjectMutability.html#//apple_ref/doc/uid/TP40010810-CH5-SW1)
- [Mutability and Caching](http://garbagecollective.quora.com/Mutability-aliasing-and-the-caches-you-didnt-know-you-had)

---
