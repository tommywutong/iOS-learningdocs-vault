---
title: 关联对象
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/associated-objects/'
original_language: en
published: 2014-02-10
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:038a0783667a83c7'
translated: true
---

> 原文：[Associated Objects](https://nshipster.com/associated-objects/)　·　NSHipster (Mattt)

# [关联对象](https://nshipster.com/associated-objects/)

作者：[Mattt](https://nshipster.com/authors/mattt/)　2014 年 2 月 10 日

```
#import <objc/runtime.h>
```

Objective-C 开发者都被训练得对紧随这句不祥召唤咒语之后的一切保持警惕。这当然有充分的理由：篡改 Objective-C 运行时，会改变其上运行的所有代码的现实结构。

在正确的人手中，`<objc/runtime.h>` 的函数有能力以其他方式无法做到的方式，为 App 或框架添加强大的新行为。在错误的人手中，它会耗尽代码（以及与之交互的一切）那众所周知的[理智计量器](https://en.wikipedia.org/wiki/Eternal_Darkness:_Sanity's_Requiem#Sanity_effects)，并带来[可怕副作用](https://www.youtube.com/watch?v=RSXcajQnasc#t=0m30s)。

因此，带着极大的惶恐，我们审视这笔[浮士德式交易](https://en.wikipedia.org/wiki/Deal_with_the_Devil)，并来看一看 NSHipster 读者最常要求的主题之一：关联对象。

---

关联对象（Associated Objects）——或最初所称的关联引用（Associative References）——是 Objective-C 2.0 运行时的一项特性，在 OS X Snow Leopard 中引入（在 iOS 4 中可用）。该术语指的是 `<objc/runtime.h>` 中声明的以下三个 C 函数，它们允许对象在运行时为键关联任意值：

- `objc_setAssociatedObject`
- `objc_getAssociatedObject`
- `objc_removeAssociatedObjects`

这为什么有用？它允许开发者**在分类（category）中向现有类添加自定义属性（property）**，而[这原本是 Objective-C 的一个显著短板](https://developer.apple.com/library/ios/documentation/cocoa/conceptual/ProgrammingWithObjectiveC/CustomizingExistingClasses/CustomizingExistingClasses.html)。

```
@interface NSObject (AssociatedObject)
@property (nonatomic, strong) id associatedObject;
@end

@implementation NSObject (AssociatedObject)
@dynamic associatedObject;

- (void)setAssociatedObject:(id)object {
     objc_setAssociatedObject(self, @selector(associatedObject), object, OBJC_ASSOCIATION_RETAIN_NONATOMIC);
}

- (id)associatedObject {
    return objc_getAssociatedObject(self, @selector(associatedObject));
}
```

通常建议将键设为 `static char`——或者更好的是，指向它的指针。基本上，是一个保证为常量、唯一且作用域限定在 getter 和 setter 内的任意值：

```
static char kAssociatedObjectKey;

objc_getAssociatedObject(self, &kAssociatedObjectKey);
```

然而，存在一个更简单的解决方案：直接使用选择器（selector）。

> 由于 `SEL` 保证唯一且恒定，你可以将 `_cmd` 用作 `objc_setAssociatedObject()` 的键。[#objective](https://twitter.com/search?q=%23objective&src=hash)-c [#snowleopard](https://twitter.com/search?q=%23snowleopard&src=hash)
> 
> — Bill Bumgarner (@bbum) [2009 年 8 月 28 日](https://twitter.com/bbum/statuses/3609098005)

## 关联对象的行为

值可以根据枚举类型 `objc_AssociationPolicy` 定义的行为关联到对象上：

| 行为 | `@property` 等价写法 | 描述 |
|---|---|---|
| `OBJC_ASSOCIATION_ASSIGN` | `@property (assign)` 或 `@property (unsafe_unretained)` | 指定对关联对象的弱引用。 |
| `OBJC_ASSOCIATION_RETAIN_NONATOMIC` | `@property (nonatomic, strong)` | 指定对关联对象的强引用，并且关联不是原子操作。 |
| `OBJC_ASSOCIATION_COPY_NONATOMIC` | `@property (nonatomic, copy)` | 指定关联对象被拷贝，并且关联不是原子操作。 |
| `OBJC_ASSOCIATION_RETAIN` | `@property (atomic, strong)` | 指定对关联对象的强引用，并且关联是原子操作。 |
| `OBJC_ASSOCIATION_COPY` | `@property (atomic, copy)` | 指定关联对象被拷贝，并且关联是原子操作。 |

用 `OBJC_ASSOCIATION_ASSIGN` 对对象进行的弱关联，并不像 `weak` 引用那样在对象释放时自动置为 nil，而是遵循与 `unsafe_unretained` 类似的行为，这意味着在实现内访问弱关联对象时应谨慎。

## 移除值

在探索关联对象的过程中，人们可能会忍不住在某个时候调用 `objc_removeAssociatedObjects()`。然而，[如文档所述](https://developer.apple.com/library/mac/documentation/Cocoa/Reference/ObjCRuntimeRef/Reference/reference.html#//apple_ref/c/func/objc_removeAssociatedObjects)，你不太可能有理由亲自调用它：

> 此函数的主要目的是使将对象恢复到“原始状态”变得容易。你不应该使用此函数来一般性地移除对象的关联，因为它也会移除其他客户端可能已添加到该对象的关联。通常，你应该使用带有 nil 值的 `objc_setAssociatedObject` 来清除关联。

## 模式

### 添加私有变量以辅助实现细节

在扩展内置类的行为时，可能需要跟踪额外的状态。这是关联对象的**教科书式**用例。

### 添加公共属性以配置分类行为

有时，使用属性（property）来使分类行为更灵活，比使用方法参数更合理。在这些情况下，面向外部的属性是使用关联对象的可接受情形。

### 为 KVO 创建关联观察者

在分类实现中使用 [KVO](https://nshipster.com/key-value-observing/) 时，建议使用自定义关联对象作为观察者（observer），而不是让对象自身观察自己。

## 反面模式

### 存储不需要的关联对象

视图的一个常见模式是创建一种便捷方法，根据模型对象或复合值来填充字段和特性（attribute）。如果稍后不再需要该值，那么不关联该对象是可接受的，甚至更可取。

### 存储可推断值的关联对象

例如，人们可能会忍不住在 `tableView:accessoryButtonTappedForRowWithIndexPath:` 中存储对自定义配件视图的父级 `UITableViewCell` 的引用，而实际上这可以通过调用 `cellForRowAtIndexPath:` 来获取。

### 使用关联对象代替 _X_

……其中 X 是以下任何一种：

- [子类化（Subclassing）](https://developer.apple.com/library/ios/documentation/cocoa/conceptual/ProgrammingWithObjectiveC/CustomizingExistingClasses/CustomizingExistingClasses.html) —— 当继承比组合更合适时。
- [目标-动作（Target-Action）](https://developer.apple.com/library/ios/documentation/general/conceptual/Devpedia-CocoaApp/TargetAction.html) —— 用于向响应者添加交互事件。
- [手势识别器（Gesture Recognizers）](https://developer.apple.com/library/ios/documentation/EventHandling/Conceptual/EventHandlingiPhoneOS/GestureRecognizer_basics/GestureRecognizer_basics.html) —— 在目标-动作不满足的任何情况下。
- [委托（Delegation）](https://developer.apple.com/library/ios/documentation/general/conceptual/DevPedia-CocoaCore/Delegation.html) —— 当行为可以委托给另一个对象时。
- [NSNotification 与 NSNotificationCenter](https://nshipster.com/nsnotification-and-nsnotificationcenter/) —— 用于以松耦合方式在系统中通信事件。

---

关联对象应被视为最后手段，而不是一种寻找问题的解决方案（而且事实上，分类本身从一开始就不应该位于工具链的顶端）。

就像任何巧妙的把戏、hack、或变通方法一样，人们会自然地倾向于主动寻找使用它的机会——尤其是在刚学会它之后。尽最大努力理解和判断何时它是正确的解决方案，并避免自己难堪地被人轻蔑地问“你究竟为何”决定使用*那种*方案。
