---
title: 键值编码与键值观察
source: objc.io
source_key: objcio
source_url: 'https://www.objc.io/issues/7-foundation/key-value-coding-and-observing'
original_language: en
published: ''
status: frozen
license: 未声明（页面无版权声明，文章版权归各作者）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:427a1bb4846150e9'
translated: true
---

> 原文：[Key-Value Coding and Observing](https://www.objc.io/issues/7-foundation/key-value-coding-and-observing)　·　objc.io

键值编码和键值观察是两种形式化机制，借助 Objective-C 语言的动态性和自省能力，它们能帮助我们简化代码。本文将通过一些示例看看如何使用它们。

## 观察模型对象的变化

在 Cocoa 的 Model-View-Controller 模式中，控制器负责让视图和模型保持同步。这包含两方面：模型对象发生变化时，必须更新视图以反映这一变化；用户与控件交互时，则必须相应地更新模型。

_键值观察_（Key-Value Observing）帮助我们让视图反映模型对象的变化。控制器可以观察视图所依赖的那些属性值。

来看一个示例：我们的模型类 `LabColor` 表示 [Lab 色彩空间](https://en.wikipedia.org/wiki/Lab_color_space)中的一种颜色，其分量是 _L_、_a_ 和 _b_（而不是红、绿、蓝）。我们希望用滑块改变这些值，并用一个大矩形显示颜色。

模型类为这三个分量分别设有属性：

```
@property (nonatomic) double lComponent;
@property (nonatomic) double aComponent;
@property (nonatomic) double bComponent;
```

### 依赖属性

我们需要据此创建一个 `UIColor` 来显示颜色。为此将添加红、绿、蓝分量的三个额外属性，以及一个 `UIColor` 属性：

```
@property (nonatomic, readonly) double redComponent;
@property (nonatomic, readonly) double greenComponent;
@property (nonatomic, readonly) double blueComponent;

@property (nonatomic, strong, readonly) UIColor *color;
```

至此，我们已经具备该类接口所需的一切：

```
@interface LabColor : NSObject

@property (nonatomic) double lComponent;
@property (nonatomic) double aComponent;
@property (nonatomic) double bComponent;

@property (nonatomic, readonly) double redComponent;
@property (nonatomic, readonly) double greenComponent;
@property (nonatomic, readonly) double blueComponent;

@property (nonatomic, strong, readonly) UIColor *color;

@end
```

计算红、绿、蓝分量的数学方法见 [Wikipedia](https://en.wikipedia.org/wiki/Lab_color_space#CIELAB-CIEXYZ_conversions)。代码大致如下：

```
- (double)greenComponent;
{
    return D65TristimulusValues[1] * inverseF(1./116. * (self.lComponent + 16) + 1./500. * self.aComponent);
}

[...]

- (UIColor *)color
{
    return [UIColor colorWithRed:self.redComponent * 0.01 green:self.greenComponent * 0.01 blue:self.blueComponent * 0.01 alpha:1.];
}
```

这里没有特别令人兴奋的部分。对我们而言有趣的是，`greenComponent` 属性依赖于 `lComponent` 和 `aComponent` 属性。这对键值观察很重要：每当我们设置 `lComponent` 属性时，都希望任何关注红绿蓝分量或 `color` 属性的人收到通知。

Foundation 框架提供的依赖表达机制是：

```
+ (NSSet *)keyPathsForValuesAffectingValueForKey:(NSString *)key
```

更具体地说，是：

```
+ (NSSet *)keyPathsForValuesAffecting<Key>
```

在这个具体示例中，代码如下：

```
+ (NSSet *)keyPathsForValuesAffectingRedComponent
{
    return [NSSet setWithObject:@"lComponent"];
}

+ (NSSet *)keyPathsForValuesAffectingGreenComponent
{
    return [NSSet setWithObjects:@"lComponent", @"aComponent", nil];
}

+ (NSSet *)keyPathsForValuesAffectingBlueComponent
{
    return [NSSet setWithObjects:@"lComponent", @"bComponent", nil];
}

+ (NSSet *)keyPathsForValuesAffectingColor
{
    return [NSSet setWithObjects:@"redComponent", @"greenComponent", @"blueComponent", nil];
}
```

现在，我们已经完整表达了这些依赖关系。请注意，这些依赖可以链式传递。例如，这让我们可以安全地创建子类并重写 `redComponent` 方法，依赖关系仍能继续生效。

### 观察变化

接下来看看视图控制器。这个 `NSViewController` 子类以属性形式持有模型对象 `LabColor`：

```
@interface ViewController ()

@property (nonatomic, strong) LabColor *labColor;

@end
```

我们希望注册视图控制器来接收键值观察通知。`NSObject` 上用于此目的的方法是：

```
- (void)addObserver:(NSObject *)anObserver
         forKeyPath:(NSString *)keyPath
            options:(NSKeyValueObservingOptions)options
            context:(void *)context
```

每当 `keyPath` 的值变化，这会使 `anObserver` 收到：

```
- (void)observeValueForKeyPath:(NSString *)keyPath
                      ofObject:(id)object
                        change:(NSDictionary *)change
                       context:(void *)context
```

的调用。这个 API 看上去有些令人生畏。更糟的是，我们还必须记得调用：

```
- (void)removeObserver:(NSObject *)anObserver
            forKeyPath:(NSString *)keyPath
```

来移除观察者，否则应用会以奇怪的方式崩溃。

在大多数情况下，使用一个辅助类即可用更简单、更优雅的方式实现 _键值观察_。我们向视图控制器添加一个所谓的 _观察令牌_ 属性：

```
@property (nonatomic, strong) id colorObserveToken;
```

然后在视图控制器设置 `labColor` 时，只需重写 `labColor` 的 setter 并观察其 `color` 的变化，如下所示：

```
- (void)setLabColor:(LabColor *)labColor
{
    _labColor = labColor;
    self.colorObserveToken = [KeyValueObserver observeObject:labColor
                                                     keyPath:@"color"
                                                      target:self
                                                    selector:@selector(colorDidChange:)
                                                     options:NSKeyValueObservingOptionInitial];
}

- (void)colorDidChange:(NSDictionary *)change;
{
    self.colorView.backgroundColor = self.labColor.color;
}
```

[`KeyValueObserver` 辅助类](https://github.com/objcio/issue-7-lab-color-space-explorer/blob/master/Lab%20Color%20Space%20Explorer/KeyValueObserver.m)仅仅封装了对 `-addObserver:forKeyPath:options:context:`、`-observeValueForKeyPath:ofObject:change:context:` 和 `-removeObserverForKeyPath:` 的调用，使视图控制器代码免受杂乱细节的干扰。

### 串联起来

最后，视图控制器需要响应 _L_、_a_ 和 _b_ 滑块的变化：

```
- (IBAction)updateLComponent:(UISlider *)sender;
{
    self.labColor.lComponent = sender.value;
}

- (IBAction)updateAComponent:(UISlider *)sender;
{
    self.labColor.aComponent = sender.value;
}

- (IBAction)updateBComponent:(UISlider *)sender;
{
    self.labColor.bComponent = sender.value;
}
```

完整代码可在我们的 GitHub 仓库中作为[示例项目](https://github.com/objcio/issue-7-lab-color-space-explorer)获取。

## 手动通知与自动通知

上面的做法似乎有点像魔法，但实际情况是：在 `LabColor` 实例上调用 `-setLComponent:` 等方法，会自动在 `-setLComponent:` 方法中的代码运行之前或之后调用：

```
- (void)willChangeValueForKey:(NSString *)key
```

以及：

```
- (void)didChangeValueForKey:(NSString *)key
```

无论我们实现 `-setLComponent:`，还是（如本例）选择为 `lComponent` 自动合成访问器，都会发生这一行为。

有些情况下，我们希望或必须重写 `-setLComponent:`，并控制是否发出变更通知，例如：

```
+ (BOOL)automaticallyNotifiesObserversForLComponent;
{
    return NO;
}

- (void)setLComponent:(double)lComponent;
{
    if (_lComponent == lComponent) {
        return;
    }
    [self willChangeValueForKey:@"lComponent"];
    _lComponent = lComponent;
    [self didChangeValueForKey:@"lComponent"];
}
```

我们禁用了对 `-willChangeValueForKey:` 和 `-didChangeValueForKey:` 的自动调用，随后自行调用它们。只有在禁用了自动调用时，才应该在 setter 内调用 `-willChangeValueForKey:` 和 `-didChangeValueForKey:`。而且在大多数情况下，这项优化并不会带来太多收益。

如果在访问器之外修改实例变量（例如 `_lComponent`），也需要注意以 `-willChangeValueForKey:` 和 `-didChangeValueForKey:` 同样包裹这些改动。但在绝大多数情况下，确保始终使用访问器会让代码更简单。

## 键值观察与上下文

有时我们可能不想使用 `KeyValueObserver` 辅助类。创建一个额外对象有轻微的开销。如果观察大量键，这可能会变得可察觉，尽管这种情况不大可能发生。

如果实现的类通过以下方法注册自身为观察者：

```
- (void)addObserver:(NSObject *)anObserver
         forKeyPath:(NSString *)keyPath
            options:(NSKeyValueObservingOptions)options
            context:(void *)context
```

那么传入一个对该类唯一的 `context` _至关重要_。建议在类的 `.m` 文件顶部放置：

```
static int const PrivateKVOContext;
```

然后向 API 传入指向此 `PrivateKVOContext` 的指针作为上下文，如下：

```
[otherObject addObserver:self forKeyPath:@"someKey" options:someOptions context:&PrivateKVOContext];
```

接着按下面方式实现 `-observeValueForKeyPath:...` 方法：

```
- (void)observeValueForKeyPath:(NSString *)keyPath
                      ofObject:(id)object
                        change:(NSDictionary *)change
                       context:(void *)context
{
    if (context == &PrivateKVOContext) {
        // Observe values here
    } else {
        [super observeValueForKeyPath:keyPath ofObject:object change:change context:context];
    }
}
```

这可以确保子类化正常工作。使用这一模式，父类和子类都能安全地观察同一对象上的相同键而不会冲突。否则，最终会遇到非常难以调试的异常行为。

## 高级键值观察

我们常常希望值变化时更新某些 UI，但还需要在初始时运行一次更新 UI 的代码。指定 `NSKeyValueObservingOptionInitial` 后，可以用 KVO 同时做到这两件事。它会使 KVO 通知在调用 `-addObserver:forKeyPath:...` 时触发。

### 变化前后

注册 KVO 时也可以指定 `NSKeyValueObservingOptionPrior`，这样能在值被修改前收到通知。这恰好对应于调用 `-willChangeValueForKey:` 的时刻。

如果使用 `NSKeyValueObservingOptionPrior` 注册，会收到两次通知：一次在变化前，一次在变化后。第一次的 `change` 字典中会多出一个键，我们可以据此判断这是变化前的通知还是变化后的通知：

```
if ([change[NSKeyValueChangeNotificationIsPriorKey] boolValue]) {
    // Before the change
} else {
    // After the change
}
```

### 值

如果需要该键的旧值或新值（或两者），可指定 `NSKeyValueObservingOptionNew` 和/或 `NSKeyValueObservingOptionOld`，要求 KVO 将它们作为通知的一部分传递。

这通常比使用 `NSKeyValueObservingOptionPrior` 更简单、更好。可以这样提取旧值和新值：

```
id oldValue = change[NSKeyValueChangeOldKey];
id newValue = change[NSKeyValueChangeNewKey];
```

KVO 基本上会分别在调用 `-willChangeValueForKey:` 和 `-didChangeValueForKey:` 的时刻，存储对应键的值。

### 索引

KVO 还对集合变化通知提供了非常强大的支持。这些通知针对由下列方法返回的集合代理对象：

```
-mutableArrayValueForKey:
-mutableSetValueForKey:
-mutableOrderedSetValueForKey:
```

稍后会进一步说明它们的工作方式。如果使用这些对象，变更字典将包含变更种类（插入、移除或替换）的信息；对于有序关系，变更字典还会包含受影响索引的信息。

集合代理对象与这些详细变更通知相结合，可在展示大型集合时高效更新 UI，不过需要相当多的工作。

## 键值观察与线程

重要的是，KVO 同步发生在实际变化所在的同一线程。这里没有队列或运行循环的魔法。对 `-didChange...` 的手动或自动调用会触发 KVO 通知的发送。

因此，除非能确保观察该键的所有对象都能以线程安全的方式处理变更通知，否则务必不要从其他线程修改属性。一般而言，我们不建议混用 KVO 和多线程。若使用多个队列或线程，就不应在线程或队列之间使用 KVO。

KVO 同步发生这一事实非常强大。只要运行在单一线程上（例如主队列），KVO 就能保证两件重要的事。

首先，如果调用 KVO 兼容的 setter，例如：

```
self.exchangeRate = 2.345;
```

那么在该 setter 返回时，可以保证 `exchangeRate` 的所有观察者都已经收到通知。

其次，如果以 `NSKeyValueObservingOptionPrior` 观察键路径，在调用 `-observe...` 方法前，某个访问 `exchangeRate` 属性的人看到的值会保持不变。

## 键值编码

最简单形式的键值编码允许我们通过：

```
@property (nonatomic, copy) NSString *name;
```

这样的属性，使用：

```
NSString *n = [object valueForKey:@"name"]
```

以及：

```
[object setValue:@"Daniel" forKey:@"name"]
```

进行访问。请注意，这既适用于对象类型的属性，也适用于标量类型（例如 `int` 和 `CGFloat`）及结构体（例如 `CGRect`）。Foundation 会自动为我们进行封装和拆封。例如，若属性为：

```
@property (nonatomic) CGFloat height;
```

可以这样设置：

```
[object setValue:@(20) forKey:@"height"]
```

键值编码允许我们使用字符串来标识并访问属性，这些字符串称为 _键_（keys）。在特定情形下，这能带来很大的灵活性，从而简化代码。下一节“_简化表单式用户界面_”会给出示例。

但键值编码并不止于此。集合（`NSArray`、`NSSet` 等）具备强大的集合运算符，可配合键值编码使用。最后，对象还能通过代理对象等方式，为并非普通属性的键提供键值编码支持。

### 简化表单式用户界面

假设有如下对象：

```
@interface Contact : NSObject

@property (nonatomic, copy) NSString *name;
@property (nonatomic, copy) NSString *nickname;
@property (nonatomic, copy) NSString *email;
@property (nonatomic, copy) NSString *city;

@end
```

以及一个详情视图控制器，其中有四个对应的 `UITextField` 属性：

```
@interface DetailViewController ()

@property (weak, nonatomic) IBOutlet UITextField *nameField;
@property (weak, nonatomic) IBOutlet UITextField *nicknameField;
@property (weak, nonatomic) IBOutlet UITextField *emailField;
@property (weak, nonatomic) IBOutlet UITextField *cityField;

@end
```

现在可以简化更新逻辑。首先，需要两个方法：一个返回所有感兴趣的模型键，另一个将这些键分别映射到其对应文本字段的键：

```
- (NSArray *)contactStringKeys;
{
    return @[@"name", @"nickname", @"email", @"city"];
}

- (UITextField *)textFieldForModelKey:(NSString *)key;
{
    return [self valueForKey:[key stringByAppendingString:@"Field"]];
}
```

借此可以用模型更新文本字段：

```
- (void)updateTextFields;
{
    for (NSString *key in self.contactStringKeys) {
        [self textFieldForModelKey:key].text = [self.contact valueForKey:key];
    }
}
```

也可以让所有四个文本字段共用一个 action 方法来更新模型：

```
- (IBAction)fieldEditingDidEnd:(UITextField *)sender
{
    for (NSString *key in self.contactStringKeys) {
        UITextField *field = [self textFieldForModelKey:key];
        if (field == sender) {
            [self.contact setValue:sender.text forKey:key];
            break;
        }
    }
}
```

注意：如[_键值验证_](#key-value-validation)一节所述，稍后会添加验证。

最后，需要确保在必要时更新文本字段：

```
- (void)viewWillAppear:(BOOL)animated;
{
    [super viewWillAppear:animated];
    [self updateTextFields];
}

- (void)setContact:(Contact *)contact
{
    _contact = contact;
    [self updateTextFields];
}
```

至此，[详情视图控制器](https://github.com/objcio/issue-7-contact-editor/blob/master/Contact%20Editor/DetailViewController.m)就可以工作了。

可在我们的 [GitHub 仓库](https://github.com/objcio/issue-7-contact-editor)查看完整项目。它也使用了下文讨论的[_键值验证_](#key-value-validation)。

### 键路径

键值编码还允许穿过关系进行访问。例如，若 `person` 是一个具有 `address` 属性的对象，且 `address` 又有 `city` 属性，就可以通过以下方式取得它：

```
[person valueForKeyPath:@"address.city"]
```

请注意，这里调用的是 `-valueForKeyPath:` 而非 `-valueForKey:`。

### 不使用 `@property` 的键值编码

不使用 `@property` 和 `@synthesize` / 自动合成，也能实现符合键值编码要求的属性。最直接的示例是简单实现 `-<key>` 和 `-set<Key>:` 方法。例如，若想支持设置 `name`，可以实现：

```
- (NSString *)name;
- (void)setName:(NSString *)name;
```

这很直接，与 `@property` 的工作方式完全相同。

不过，有一点需要注意：标量值和结构体值如何处理 `nil`。假设想通过实现以下方法，为 `height` 提供键值编码支持：

```
- (CGFloat)height;
- (void)setHeight:(CGFloat)height;
```

调用：

```
[object setValue:nil forKey:@"height"]
```

时会抛出异常。为了处理 `nil` 值，需要确保重写 `-setNilValueForKey:`，例如：

```
- (void)setNilValueForKey:(NSString *)key
{
    if ([key isEqualToString:@"height"]) {
        [self setValue:@0 forKey:key];
    } else
        [super setNilValueForKey:key];
}
```

可以通过重写下列方法，让一个类支持键值编码：

```
- (id)valueForUndefinedKey:(NSString *)key;
- (void)setValue:(id)value forUndefinedKey:(NSString *)key;
```

这可能看起来很奇怪，但它允许一个类动态支持特定的键。不过，使用这两个方法会带来性能损失。

顺带一提，Foundation 支持直接访问实例变量。应谨慎使用这一功能。请查阅 `+accessInstanceVariablesDirectly` 的文档。它的默认值为 `YES`，这会使 Foundation 依次查找名为 `_<key>`、`_is<Key>`、`<key>` 或 `is<Key>` 的实例变量。

### 集合运算符

键值编码一项常被忽视的功能是对集合运算符的支持。例如，可以通过以下方式取得数组中的最大值：

```
NSArray *a = @[@4, @84, @2];
NSLog(@"max = %@", [a valueForKeyPath:@"@max.self"]);
```

或者，如果有一个 `Transaction` 对象数组，且对象带有 `amount` 属性，也可以取得最大的 `amount`：

```
NSArray *a = @[transaction1, transaction2, transaction3];
NSLog(@"max = %@", [a valueForKeyPath:@"@max.amount"]);
```

当调用 `[a valueForKeyPath:@"@max.amount"]` 时，系统会对数组 `a` 的每个元素调用 `-valueForKey:@"amount"`，然后返回其中的最大值。

Apple 的键值编码文档有一节名为 [Collection Operators](https://developer.apple.com/library/ios/documentation/cocoa/conceptual/KeyValueCoding/Articles/CollectionOperators.html)，其中对此有详细说明。

### 通过集合代理对象进行键值编码

可以像公开普通对象那样公开集合（`NSArray`、`NSSet` 等）。不过，键值编码也允许通过代理对象实现符合键值编码要求的集合。这是一种高级技巧，很少会用到，但它是工具箱中很强大的一项技巧。

在对象上调用 `-valueForKey:` 时，该对象可以为 `NSArray`、`NSSet` 或 `NSOrderedSet` 返回集合代理对象。该类并不实现普通的 `-<Key>` 方法，而是实现代理会使用的一系列方法。

如果希望该类能够通过 `contacts` 键的代理对象返回 `NSArray`，可以实现：

```
- (NSUInteger)countOfContacts;
- (id)objectInContactsAtIndex:(NSUInteger)idx;
```

这样，在调用 `[object valueForKey:@"contacts”]` 时，会返回一个 `NSArray`，将所有调用代理给这两个方法。但该数组支持 `NSArray` 的_所有_方法。调用者无法察觉代理的存在。换言之，调用者不知道返回的是普通 `NSArray` 还是代理对象。

对 `NSSet` 和 `NSOrderedSet` 也可以做同样的事。必须实现的方法如下：

| NSArray | NSSet | NSOrderedSet |
|---|---|---|
| `-countOf<Key>` | `-countOf<Key>` | `-countOf<Key>` |
|  | `-enumeratorOf<Key>` | `-indexIn<Key>OfObject:` |
| One of | `-memberOf<Key>:` |  |
| `-objectIn<Key>AtIndex:` |  | One of |
| `-<key>AtIndexes:` |  | `-objectIn<Key>AtIndex:` |
|  |  | `-<key>AtIndexes:` |
| Optional (performance) |  |  |
| `-get<Key>:range:` |  | Optional (performance) |
|  |  | `-get<Key>:range:` |

这些_可选_方法可以提升代理对象的性能。

仅在特殊情况下才适合使用这些代理对象，但在那些情况下它们会很有帮助。想象一下，现有的数据结构非常大，而调用者不需要（一次）访问所有元素。

举个（或许有些牵强的）例子，可以编写一个含有巨大素数列表的类，如下：

```
@interface Primes : NSObject

@property (readonly, nonatomic, strong) NSArray *primes;

@end

@implementation Primes

static int32_t const primes[] = {
    2, 101, 233, 383, 3, 103, 239, 389, 5, 107, 241, 397, 7, 109,
    251, 401, 11, 113, 257, 409, 13, 127, 263, 419, 17, 131, 269,
    421, 19, 137, 271, 431, 23, 139, 277, 433, 29, 149, 281, 439,
    31, 151, 283, 443, 37, 157, 293, 449, 41, 163, 307, 457, 43,
    167, 311, 461, 47, 173, 313, 463, 53, 179, 317, 467, 59, 181,
    331, 479, 61, 191, 337, 487, 67, 193, 347, 491, 71, 197, 349,
    499, 73, 199, 353, 503, 79, 211, 359, 509, 83, 223, 367, 521,
    89, 227, 373, 523, 97, 229, 379, 541, 547, 701, 877, 1049,
    557, 709, 881, 1051, 563, 719, 883, 1061, 569, 727, 887,
    1063, 571, 733, 907, 1069, 577, 739, 911, 1087, 587, 743,
    919, 1091, 593, 751, 929, 1093, 599, 757, 937, 1097, 601,
    761, 941, 1103, 607, 769, 947, 1109, 613, 773, 953, 1117,
    617, 787, 967, 1123, 619, 797, 971, 1129, 631, 809, 977,
    1151, 641, 811, 983, 1153, 643, 821, 991, 1163, 647, 823,
    997, 1171, 653, 827, 1009, 1181, 659, 829, 1013, 1187, 661,
    839, 1019, 1193, 673, 853, 1021, 1201, 677, 857, 1031,
    1213, 683, 859, 1033, 1217, 691, 863, 1039, 1223, 1229,
};

- (NSArray *)primes;
{
    return [self valueForKey:@"backingPrimes"];
}

- (NSUInteger)countOfBackingPrimes;
{
    return (sizeof(primes) / sizeof(*primes));
}

- (id)objectInBackingPrimesAtIndex:(NSUInteger)idx;
{
    NSParameterAssert(idx < sizeof(primes) / sizeof(*primes));
    return @(primes[idx]);
}

@end
```

现在可以运行：

```
Primes *primes = [[Primes alloc] init];
NSLog(@"The last prime is %@", [primes.primes lastObject]);
```

这会调用一次 `-countOfPrimes`，然后以 `idx` 等于最后一个索引调用一次 `-objectInPrimesAtIndex:`。它_不会_先将所有整数包装为 `NSNumber`，再将它们全都包装为 `NSArray`，最后只为取出最后一个对象。

[_Contacts Editor_ 示例应用](https://github.com/objcio/issue-7-contact-editor)在一个人为构造的示例中，使用同一方法包装了 C++ `std::vector`。不过，它说明了如何使用这种方法。

#### 可变集合

甚至可以将集合代理用于可变集合，即 `NSMutableArray`、`NSMutableSet` 和 `NSMutableOrderedSet`。

访问这类可变集合的方式略有不同。调用者现在必须调用以下方法之一：

```
- (NSMutableArray *)mutableArrayValueForKey:(NSString *)key;
- (NSMutableSet *)mutableSetValueForKey:(NSString *)key;
- (NSMutableOrderedSet *)mutableOrderedSetValueForKey:(NSString *)key;
```

作为一种技巧，可以让类通过以下方法返回可变集合代理：

```
- (NSMutableArray *)mutableContacts;
{
    return [self mutableArrayValueForKey:@"wrappedContacts"];
}
```

随后为键 `wrappedContacts` 实现正确的方法。

除了为不可变集合列出的上述方法，还必须实现以下方法：

| NSMutableArray / NSMutableOrderedSet | NSMutableSet |
|---|---|
| 至少一个插入方法和一个移除方法 | 至少一个添加方法和一个移除方法 |
| `-insertObject:in<Key>AtIndex:` | `-add<Key>Object:` |
| `-removeObjectFrom<Key>AtIndex:` | `-remove<Key>Object:` |
| `-insert<Key>:atIndexes:` | `-add<Key>:` |
| `-remove<Key>AtIndexes:` | `-remove<Key>:` |
|  |  |
| Optional (performance) one of | Optional (performance) |
| `-replaceObjectIn<Key>AtIndex:withObject:` | `-intersect<Key>:` |
| `-replace<Key>AtIndexes:with<Key>:` | `-set<Key>:` |

如前所述，这些可变集合代理对象与键值观察结合时也非常强大。当这些集合发生变更时，KVO 机制会将详细的变更信息放入 `change` 字典。

这里既有批量变更方法（接收多个对象），也有只接收单个对象的方法。建议选择在给定任务中最容易实现的方案，略微偏向批量更新的方法。

如果实现这些方法，需要注意自动和手动 KVO 合规性。Foundation 默认假定使用自动通知，并会发送细粒度变更通知。若选择通过以下方法自行实现细粒度通知：

```
-willChange:valuesAtIndexes:forKey:
-didChange:valuesAtIndexes:forKey:
```

或：

```
-willChangeValueForKey:withSetMutation:usingObjects:
-didChangeValueForKey:withSetMutation:usingObjects:
```

就必须关闭自动通知，否则 KVO 会为每一次变更发送两次通知。

### 常见的键值观察错误

首先也是最重要的一点，KVO 合规性是 API 的一部分。若某个类的所有者没有承诺属性符合 KVO 要求，我们就不能假定 KVO 会起作用。Apple 会说明哪些属性符合 KVO 要求。例如，`NSProgress` 类列出了其大多数 KVO 合规属性。

有时人们会在一次变化_已经_发生之后，放置中间不做任何事的一对 `-willChange` 和 `-didChange` 调用来触发 KVO。这会发布 KVO 通知，却会破坏依赖 `NSKeyValueObservingOld` 选项的观察者。特别是，这会影响 KVO 自身对观察键路径的支持。KVO 依赖 `NSKeyValueObservingOld` 属性来支持键路径观察。

还要指出，集合本身不可观察。KVO 观察的是_关系_而不是集合。不能观察一个 `NSArray`；只能观察对象上的一个属性，而这个属性可以是 `NSArray`。例如，若有一个 `ContactList` 对象，可以观察其 `contacts` 属性，但不能将 `NSArray` 作为被观察对象传给 `-addObserver:forKeyPath:...`。

同样，观察 `self` 并不总是可行，而且这大概也不是一个好的设计模式。

### 调试键值观察

在 `lldb` 中，可以像这样转储被观察对象的观察信息：

```
(lldb) po [observedObject observationInfo]
```

这会打印大量关于谁在观察什么的信息。

该格式是私有的，绝不能依赖它的任何内容，Apple 随时都可以修改它。但它是一个非常强大的调试工具。

## 键值验证

最后，键值验证也是键值编码 API 的一部分。它是一套用于验证属性值的一致 API，但自身几乎不提供任何逻辑或功能。

不过，若正在编写能够验证值的模型类，应该以键值验证规定的方式实现 API，以确保一致性。键值验证是在模型类中验证值的 Cocoa 约定。

再强调一次：键值编码不会执行任何验证，也不会调用键值验证方法。控制器必须自行完成这一工作。不过，按键值验证实现验证方法可确保它们保持一致。

一个简单示例如下：

```
- (IBAction)nameFieldEditingDidEnd:(UITextField *)sender;
{
    NSString *name = [sender text];
    NSError *error = nil;
    if ([self.contact validateName:&name error:&error]) {
        self.contact.name = name;
    } else {
        // Present the error to the user
    }
    sender.text = self.contact.name;
}
```

强大之处在于，我们要求模型类（本例中的 `Contact`）验证 `name`，同时也给予模型类清理该名称的机会。

如果希望确保名称没有前导空白，这类逻辑就应放在模型对象内部。`Contact` 类可为 `name` 属性实现如下键值验证方法：

```
- (BOOL)validateName:(NSString **)nameP error:(NSError * __autoreleasing *)error
{
    if (*nameP == nil) {
        *nameP = @"";
        return YES;
    } else {
        *nameP = [*nameP stringByTrimmingCharactersInSet:[NSCharacterSet whitespaceAndNewlineCharacterSet]];
        return YES;
    }
}
```

[_Contact Editor_ 示例](https://github.com/objcio/issue-7-contact-editor)在 `DetailViewController` 和 `Contact` 类中演示了这一点。

---
