---
title: 键值观察编程指南
apple_id: 10000177i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/Articles/KVOBasics.html
archived_at: '2026-07-15T07:16:17.607841Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [键值观察编程指南](Introduction%20to%20Key-Value%20Observing%20Programming%20Guide.md)


[下一页](KVO%20Compliance.md)[上一页](Introduction%20to%20Key-Value%20Observing%20Programming%20Guide.md)

# 注册键值观察

要使对象能够接收某个符合 KVO 规范的属性的键值观察通知，必须执行以下步骤：

- 使用 [addObserver:forKeyPath:options:context:](https://developer.apple.com/documentation/objectivec/nsobject/1412787-addobserver) 方法将观察者注册到被观察对象上。
- 在观察者内部实现 [observeValueForKeyPath:ofObject:change:context:](https://developer.apple.com/documentation/objectivec/nsobject/1416553-observevalueforkeypath) 以接收更改通知消息。
- 当观察者不应再接收消息时，使用 [removeObserver:forKeyPath:](https://developer.apple.com/documentation/objectivec/nsobject/1408054-removeobserver) 方法注销观察者。至少应在观察者从内存中释放之前调用此方法。

观察对象首先向被观察对象发送一条 `addObserver:forKeyPath:options:context:` [消息](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Message.html#//apple_ref/doc/uid/TP40008195-CH59) 来注册自身，并将自己作为观察者、以及被观察属性的键路径一并传入。观察者还会额外指定一个 options 参数和一个 context 指针，用于管理通知的各个方面。

options 参数以选项常量的按位 `OR` 指定，它同时影响通知中提供的更改字典的内容，以及通知的生成方式。

指定选项 `NSKeyValueObservingOptionOld`，即可选择接收被观察属性更改前的值。使用选项 `NSKeyValueObservingOptionNew` 可请求属性的新值。将这两个选项按位 `OR` 即可同时接收新旧值。

使用选项 `NSKeyValueObservingOptionInitial`，可以指示被观察对象立即发送一条更改通知（在 `addObserver:forKeyPath:options:context:` 返回之前）。你可以利用这条额外的一次性通知，在观察者中建立属性的初始值。

加入选项 `NSKeyValueObservingOptionPrior`，可以指示被观察对象在属性更改之前（除了常规的更改后通知之外）再发送一条通知。更改字典通过包含值为包装了 `YES` 的 `NSNumber` 的键 `NSKeyValueChangeNotificationIsPriorKey` 来表示这是一条更改前通知，其他情况下该键不存在。当观察者自身的 KVO 合规性要求它为某个依赖于被观察属性的属性调用某个 -`willChange…` 方法时，你可以使用更改前通知——常规的更改后通知到来时，再调用 `willChange…` 就为时已晚。

`addObserver:forKeyPath:options:context:` 消息中的 context 指针包含任意数据，这些数据会在相应的更改通知中回传给观察者。你可以指定 `NULL`，完全依靠键路径字符串来确定更改通知的来源，但如果某个对象的超类也出于不同原因在观察同一键路径，这种做法可能会引发问题。

更安全、更具扩展性的做法是利用 context 来确保你收到的通知是发给你的观察者、而非某个超类的。

类中一个唯一命名的静态变量的地址是很好的 context。在超类或子类中以类似方式选择的 context 不太可能重叠。你可以为整个类选择单一的 context，并依靠通知消息中的键路径字符串来确定发生了什么变化。或者，你也可以为每个被观察的键路径创建一个独立的 context，这样就完全无需进行字符串比较，从而使通知解析更高效。清单 1 展示了以这种方式为 `balance` 和 `interestRate` 属性选择的示例 context。

__清单 1__　创建 context 指针

```objc
static void *PersonAccountBalanceContext = &PersonAccountBalanceContext;
static void *PersonAccountInterestRateContext = &PersonAccountInterestRateContext;
```

清单 2 中的示例演示了 Person 实例如何使用给定的 context 指针，将自己注册为某个 `Account` 实例的 `balance` 和 `interestRate` 属性的观察者。

__清单 2__　将检查器注册为 balance 和 interestRate 属性的观察者

```objc
- (void)registerAsObserverForAccount:(Account*)account {
    [account addObserver:self
              forKeyPath:@"balance"
                 options:(NSKeyValueObservingOptionNew |
                          NSKeyValueObservingOptionOld)
                 context:PersonAccountBalanceContext];

    [account addObserver:self
              forKeyPath:@"interestRate"
                 options:(NSKeyValueObservingOptionNew |
                          NSKeyValueObservingOptionOld)
                  context:PersonAccountInterestRateContext];
}
```


当对象的被观察属性的值发生变化时，观察者会收到一条 `observeValueForKeyPath:ofObject:change:context:` [消息](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Message.html#//apple_ref/doc/uid/TP40008195-CH59)。所有观察者都必须实现此方法。

观察对象会提供触发通知的键路径、作为相关对象的自身、包含更改详情的[字典](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Collection.html#//apple_ref/doc/uid/TP40008195-CH10)，以及注册该键路径观察时提供的 context 指针。

更改字典条目 `NSKeyValueChangeKindKey` 提供了有关所发生更改类型的信息。如果被观察对象的值发生了变化，`NSKeyValueChangeKindKey` 条目返回 `NSKeyValueChangeSetting`。根据注册观察者时指定的选项，更改字典中的 `NSKeyValueChangeOldKey` 和 `NSKeyValueChangeNewKey` 条目分别包含属性更改前和更改后的值。如果属性是对象，则直接提供该值。如果属性是标量或 C 结构体，该值会被包装在 [NSValue](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSValue/Description.html#//apple_ref/occ/cl/NSValue) 对象中（与[键值编码](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/KeyValueCoding.html#//apple_ref/doc/uid/TP40008195-CH25)中的做法相同）。

如果被观察的属性是对多关系，`NSKeyValueChangeKindKey` 条目还会通过分别返回 `NSKeyValueChangeInsertion`、`NSKeyValueChangeRemoval` 或 `NSKeyValueChangeReplacement`，指示关系中的对象是被插入、移除还是替换。

`NSKeyValueChangeIndexesKey` 对应的更改字典条目是一个 `NSIndexSet` 对象，指定关系中发生变化的索引。如果在注册观察者时指定了 `NSKeyValueObservingOptionNew` 或 `NSKeyValueObservingOptionOld` 选项，更改字典中的 `NSKeyValueChangeOldKey` 和 `NSKeyValueChangeNewKey` 条目就是数组，分别包含相关对象更改前和更改后的值。

清单 3 中的示例展示了 `Person` 观察者的 `observeValueForKeyPath:ofObject:change:context:` 实现，它会记录按[清单 2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi2telktk4za) 注册的 `balance` 和 `interestRate` 属性的新旧值。

__清单 3__　observeValueForKeyPath:ofObject:change:context: 的实现

```objc
- (void)observeValueForKeyPath:(NSString *)keyPath
                      ofObject:(id)object
                        change:(NSDictionary *)change
                       context:(void *)context {

    if (context == PersonAccountBalanceContext) {
        // Do something with the balance…

    } else if (context == PersonAccountInterestRateContext) {
        // Do something with the interest rate…

    } else {
        // Any unrecognized context must belong to super
        [super observeValueForKeyPath:keyPath
                             ofObject:object
                               change:change
                               context:context];
    }
}
```

如果你在注册观察者时指定了 `NULL` context，就需要将通知的键路径与你正在观察的键路径进行比较，以确定发生了什么变化。如果你为所有被观察的键路径使用了单一 context，则先将它与通知的 context 进行测试，若匹配，再使用键路径字符串比较来确定具体发生了什么变化。如果你像这里演示的那样为每个键路径提供了唯一的 context，那么只需一系列简单的指针比较，就能同时得知通知是否属于这个观察者，以及如果是，哪个键路径发生了变化。

无论哪种情况，当观察者无法识别 context（或在简单情况下，无法识别任何键路径）时，都应始终调用超类的 `observeValueForKeyPath:ofObject:change:context:` 实现，因为这意味着某个超类也注册了通知。

你可以通过向被观察对象发送 `removeObserver:forKeyPath:context:` 消息来移除键值观察者，并指定观察对象、键路径和 context。清单 4 中的示例展示了 `Person` 将自己从 `balance` 和 `interestRate` 的观察者中移除。

__清单 4__　将检查器从 balance 和 interestRate 的观察者中移除

```objc
- (void)unregisterAsObserverForAccount:(Account*)account {
    [account removeObserver:self
                 forKeyPath:@"balance"
                    context:PersonAccountBalanceContext];

    [account removeObserver:self
                 forKeyPath:@"interestRate"
                    context:PersonAccountInterestRateContext];
}
```

收到 `removeObserver:forKeyPath:context:` 消息后，观察对象将不再收到针对指定键路径和对象的任何 `observeValueForKeyPath:ofObject:change:context:` 消息。

移除观察者时，请牢记以下几点：

- 如果尚未注册为观察者就请求移除，会引发 `NSRangeException`。你要么针对相应的 `addObserver:forKeyPath:options:context:` 调用恰好调用一次 `removeObserver:forKeyPath:context:`，要么如果这在你的应用中不可行，就将 `removeObserver:forKeyPath:context:` 调用放在 try/catch 块中，以处理潜在的异常。
- 观察者在被释放时不会自动移除自身。被观察对象会继续发送通知，而不理会观察者的状态。然而，更改通知与任何其他消息一样，发送给已释放的对象会触发内存访问异常。因此，你必须确保观察者在从内存中消失之前移除自身。
- 该协议没有提供任何方法来询问某个对象是否为观察者或是否正在被观察。构造代码时应避免与释放相关的错误。一种典型的模式是：在观察者初始化期间（例如在 `init` 或 `viewDidLoad` 中）注册为观察者，在释放期间（通常在 `dealloc` 中）注销，从而确保 add 和 remove 消息正确配对且顺序恰当，并确保观察者在从内存中释放之前完成注销。

[下一页](KVO%20Compliance.md)[上一页](Introduction%20to%20Key-Value%20Observing%20Programming%20Guide.md)
