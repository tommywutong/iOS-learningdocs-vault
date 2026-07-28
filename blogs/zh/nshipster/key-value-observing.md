---
title: 键值观察
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/key-value-observing/'
original_language: en
published: 2013-10-07
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:d818c8a28fa02c2b'
translated: true
---

> 原文：[Key-Value Observing](https://nshipster.com/key-value-observing/)　·　NSHipster (Mattt)

# [键值观察](https://nshipster.com/key-value-observing/)

作者：[Mattt](https://nshipster.com/authors/mattt/)　　2013 年 10 月 7 日

随便问一个对 NSBlock 有所了解的人：键值观察（Key-Value Observing）拥有整个 Cocoa 中**最糟糕**的 API。它笨拙、冗长、令人困惑。而最糟糕的是，这个糟糕的 API 掩盖了框架中最引人注目的特性之一。

在处理复杂的、有状态系统时，勤勉的簿记工作对于保持清醒至关重要。以免左手不知道右手在做什么，对象需要某种方式来发布和订阅随时间变化的状态变更。

在 Objective-C 和 Cocoa 中，有几种方式来传递这些事件，每种方式都有不同程度的形式化和耦合度：

- **`NSNotification`** 和 **`NSNotificationCenter`** 提供了一个中心化的枢纽，App 的任何部分都可以通过它来通知其他部分或被其他部分通知状态变更。唯一的要求是知道要查找什么，具体来说是通知的名称。例如，`UIApplicationDidReceiveMemoryWarningNotification` 信号表示 App 处于低内存环境。
- **键值观察（Key-Value Observing）** 允许在特定对象实例之间进行即席的、事件驱动的自省，通过监听特定键路径（key path）上的变化来实现。例如，一个 `UIProgressView` 可以观察网络请求的 `numberOfBytesRead` 来推导并更新其自身的 `progress` 属性。
- **委托（Delegate）** 是一种流行的模式，用于通过一组固定的方法向指定的处理程序发送事件信号。例如，`UIScrollView` 每次其滚动偏移量改变时，都会向它的委托发送 `scrollViewDidScroll:`。
- 各种**回调（Callback）**，例如像 `NSOperation -completionBlock` 这样的 block 属性（在 `isFinished == YES` 后触发），或者作为钩子传入函数的 C 函数指针，比如 `SCNetworkReachabilitySetCallback(3)`。

在这些方法中，键值观察可以说是最不被理解的一个。所以本周，NSHipster 将致力于为此情况提供一些急需的澄清和最佳实践概念。对于普通观察者来说，这似乎是在做无用功，但本刊的订阅者知道得更多。

---

`<NSKeyValueObserving>`，即 KVO，是一个非正式协议，它定义了用于观察和通知对象之间状态变更的通用机制。作为一个非正式协议，你不会看到类炫耀它们对它的遵守（它被隐式地假定为所有 `NSObject` 子类都遵守）。

KVO 的主要价值主张相当引人注目：任何对象都可以订阅以被通知任何其他对象中的状态变更。其中大部分是内置的、自动的和透明的。

> 作为参考，这种观察者模式的类似表现是现代大多数 JavaScript 框架的秘密武器，例如 [Backbone.js](http://backbonejs.org) 和 [Ember.js](http://emberjs.com)。

## 订阅

可以为对象在特定键路径（key path）上添加观察者，如 [KVC 操作符文章](https://nshipster.com/kvc-collection-operators/) 所述，这些键路径是指定一系列属性的点分隔键。大多数情况下使用 KVO，这些只是对象的顶层属性。

用于添加观察者的方法是 `–addObserver:forKeyPath:options:context:`：

```
- (void)addObserver:(NSObject *)observer
         forKeyPath:(NSString *)keyPath
            options:(NSKeyValueObservingOptions)options
            context:(void *)context
```

> - `observer`：要注册以接收 KVO 通知的对象。观察者必须实现键值观察方法 `observeValueForKeyPath:ofObject:change:context:`。
> - `keyPath`：相对于接收者的、要观察的属性的键路径。此值不能为 `nil`。
> - `options`：`NSKeyValueObservingOptions` 值的组合，指定观察通知中包含的内容。可能的值请参见“NSKeyValueObservingOptions”。
> - `context`：传递给 `observeValueForKeyPath:ofObject:change:context:` 中 `observer` 的任意数据。

真糟糕。这个 API 之所以如此难看，是因为最后两个参数几乎总是分别为 `0` 和 `NULL`。

`options` 指的是 `NSKeyValueObservingOptions` 的位掩码。特别要注意 `NSKeyValueObservingOptionNew` 和 `NSKeyValueObservingOptionOld`，因为如果有的话，它们是你最可能使用的选项。可以随意略过 `NSKeyValueObservingOptionInitial` 和 `NSKeyValueObservingOptionPrior`：

### NSKeyValueObservingOptions

> - `NSKeyValueObservingOptionNew`：指示变更字典应提供新的属性值（如果适用）。
> - `NSKeyValueObservingOptionOld`：指示变更字典应包含旧的属性值（如果适用）。
> - `NSKeyValueObservingOptionInitial`：如果指定，则在观察者注册方法返回之前，应立即向观察者发送通知。如果同时也指定了 `NSKeyValueObservingOptionNew`，则通知中的变更字典将始终包含 `NSKeyValueChangeNewKey` 条目，但永远不会包含 `NSKeyValueChangeOldKey` 条目。（在初始通知中，被观察属性的当前值可能已陈旧，但对观察者来说是新的。）你可以使用此选项来替代显式调用观察者的 `observeValueForKeyPath:ofObject:change:context:` 方法中同时调用的代码。当此选项与 `addObserver:forKeyPath:options:context:` 一起使用时，将为每个被添加观察者的索引对象发送一个通知。
> - `NSKeyValueObservingOptionPrior`：是否应在每次变更之前和之后分别向观察者发送通知，而不是在变更之后发送单个通知。在变更之前发送的通知的变更字典始终包含一个值为 `@YES` 的 `NSKeyValueChangeNotificationIsPriorKey` 条目，但永远不会包含 `NSKeyValueChangeNewKey` 条目。当指定此选项时，变更之后发送的通知中的变更字典包含的条目与未指定此选项时相同。当观察者自身的键值观察合规性要求它为自身的某个属性调用 `-willChange...` 方法，并且该属性的值依赖于被观察对象的属性的值时，你可以使用此选项。（在这种情况下，在变更之后收到 `observeValueForKeyPath:ofObject:change:context:` 消息时，再要正确地调用 `-willChange...` 已经太晚了。）

这些选项允许对象获取变更前后的值。在实践中，这通常不是必需的，因为新值通常可以从属性的当前值获得。

也就是说，`NSKeyValueObservingOptionInitial` 有助于减少响应 KVO 事件时的代码路径。例如，如果你有一个方法，它根据某个字段的 `text` 值动态启用按钮，那么传递 `NSKeyValueObservingOptionInitial` 会在添加观察者后立即以初始状态触发事件。

至于 `context`，这个参数是一个值，以后可用于区分对不同对象上相同键路径的观察。这有点复杂，稍后将讨论。

## 响应

KVO 的另一个导致其丑陋的方面是，没有办法像人们在控制（control）使用的目标-动作模式中习惯的那样，指定自定义选择器来处理观察。

相反，观察者的所有变更都通过一个单一方法——`-observeValueForKeyPath:ofObject:change:context:` 来汇集：

```
- (void)observeValueForKeyPath:(NSString *)keyPath
                      ofObject:(id)object
                        change:(NSDictionary *)change
                       context:(void *)context
```

这些参数与在 `–addObserver:forKeyPath:options:context:` 中指定的相同，但 `change` 除外，它根据所使用的 `NSKeyValueObservingOptions` `options` 而被填充。

该方法的典型实现看起来像这样：

```
- (void)observeValueForKeyPath:(NSString *)keyPath
                      ofObject:(id)object
                        change:(NSDictionary *)change
                       context:(void *)context
{
  if ([keyPath isEqualToString:@"state"]) {
    …
  }
}
```

根据单个类正在观察的对象种类数量，此方法也可能引入 `-isKindOfObject:` 或 `-respondsToSelector:` 来明确标识正在传递的事件类型。然而，最安全的方法是使用 `context` 进行相等性检查——尤其是在处理父类也观察相同键路径的子类时。

### 正确的 Context 声明

什么是一个好的 `context` 值？这里有一个建议：

```
static void * XXContext = &XXContext;
```

就这么简单：一个存储自身指针的静态值。它本身没有任何意义，这使得它非常适合 `<NSKeyValueObserving>`：

```
- (void)observeValueForKeyPath:(NSString *)keyPath
                      ofObject:(id)object
                        change:(NSDictionary *)change
                       context:(void *)context
{
  if (context == XXContext) {
      if ([keyPath isEqualToString:NSStringFromSelector(@selector(isFinished))]) {

      }
  }
}
```

### 更好的键路径

将字符串作为键路径传递严格来说不如直接使用属性，因为任何拼写错误都不会被编译器捕获，并且会导致事情无法工作。

对此有一个巧妙的解决方法，即使用 `NSStringFromSelector` 和 `@selector` 字面量：

```
NSStringFromSelector(@selector(isFinished))
```

由于 `@selector` 会扫描目标中所有可用的选择器，这不能防止所有错误，但可以捕获大多数错误——包括 Xcode 自动重构带来的破坏性更改。

```
- (void)observeValueForKeyPath:(NSString *)keyPath
                      ofObject:(id)object
                        change:(NSDictionary *)change
                       context:(void *)context
{
    if ([object isKindOfClass:[NSOperation class]]) {
        if ([keyPath isEqualToString:NSStringFromSelector(@selector(isFinished))]) {

        }
    } else if (...) {
        …
    }
}
```

## 取消订阅

当观察者完成对某个对象的监听后，它应调用 `–removeObserver:forKeyPath:context:`。这通常会在 `-observeValueForKeyPath:ofObject:change:context:` 或 `-dealloc`（或类似的销毁方法）中调用。

### 使用 `@try` / `@catch` 安全取消订阅

KVO 可能最明显的麻烦在于它在收尾时如何困扰你。如果你在对象**未**注册为观察者时（无论是由于已经取消注册还是最初就没有注册）调用 `–removeObserver:forKeyPath:context:`，则会抛出一个异常。关键在于，_甚至没有内置的方法来检查一个对象是否已注册！_

这导致人们依赖于一种相当不幸的粗暴方法：使用 `@try` 而不处理 `@catch`：

```
- (void)observeValueForKeyPath:(NSString *)keyPath
                      ofObject:(id)object
                        change:(NSDictionary *)change
                       context:(void *)context
{
    if ([keyPath isEqualToString:NSStringFromSelector(@selector(isFinished))]) {
        if ([object isFinished]) {
          @try {
              [object removeObserver:self forKeyPath:NSStringFromSelector(@selector(isFinished))];
          }
          @catch (NSException * __unused exception) {}
        }
    }
}
```

诚然，_不_处理捕获到的异常，如本例所示，是挥舞着投降的`[UIColor whiteColor]`旗帜。因此，只有当面临间歇性崩溃，且无法通过正常的簿记工作（无论是由于竞态条件还是超类的未记录行为）加以补救时，才应真正使用此技术。

## 自动属性通知

KVO 之所以有用，在于它几乎得到了普遍采用。正因为如此，使所有内容正确连接所需的大部分工作都由编译器和运行时自动处理了。

> 类可以通过重写 `+automaticallyNotifiesObserversForKey:` 并返回 `NO` 来选择退出自动 KVO。

但是复合或派生值呢？假设你有一个对象，它具有 `@dynamic`、`readonly` 的 `address` 属性，该属性读取并格式化其 `streetAddress`、`locality`、`region` 和 `postalCode`？

那么，你可以实现方法 `keyPathsForValuesAffectingAddress`（或其不那么神奇的通用方法 `+keyPathsForValuesAffectingValueForKey:`）：

```
+ (NSSet *)keyPathsForValuesAffectingAddress {
    return [NSSet setWithObjects:NSStringFromSelector(@selector(streetAddress)), NSStringFromSelector(@selector(locality)), NSStringFromSelector(@selector(region)), NSStringFromSelector(@selector(postalCode)), nil];
}
```

---

好了，这就是关于 KVO 的一些常规观察和最佳实践。对于一个有进取心的 NSHipster 来说，KVO 可以成为一个强大的基础，在其上可以构建巧妙而强大的抽象。明智地使用它，理解这些规则和约定，以便在你的 App 中充分利用它。
