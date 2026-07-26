---
title: Aspects
source: dirtmelon
source_key: dirtmelon
source_url: 'https://dirtmelon.github.io/posts/Aspects/'
original_language: zh
published: 2020-03-07
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:622f2b8a2748cc3a'
translated: n/a
---

> 原文：[Aspects](https://dirtmelon.github.io/posts/Aspects/)　·　dirtmelon

## Aspects 好处都有啥

在 `Objective-C` 中可以使用 `method swizzling` 来进行 AOP 编程，可以替换掉原有方法的执行，或者在原有方法执行前后添加自己的代码。 举个最普遍的例子：我们需要统计 app 中每个 `ViewController` 出现的次数，需要在 `viewDidAppear:` 中添加统计方法，一般来说我们可能会考虑用继承，但是继承会带来以下两个问题：

1. 需要一个基类来实现这些代码，如果有多个类似的需求则会导致基类非常庞大；
2. 所有新建的 `ViewController` 都需要继承自这个基类，需要针对不同的 `Controller` 类型来编写不同的基类；

通过 `method swizzling` 我们可以在 `UIViewController` 的 `viewDidAppear:` 插入自己的替换代码，大多数无痕埋点都是使用这个解决方法。下面来看看不怎么优雅地实现一个 `method swizzling` 的代码：

```objectivec
@implementation UIViewController (MethodSwizzling)

+ (void)load {
    static dispatch_once_t onceToken;
    dispatch_once(&onceToken, ^{
        Class class = [self class];

        SEL originalSelector = @selector(viewWillAppear:);
        SEL swizzledSelector = @selector(melon_viewWillAppear:);
        Method originalMethod = class_getInstanceMethod(class, originalSelector);
        Method swizzledMethod = class_getInstanceMethod(class, swizzledSelector);

        BOOL didAddMethod =
            class_addMethod(class,
                originalSelector,
                method_getImplementation(swizzledMethod),
                method_getTypeEncoding(swizzledMethod));

        if (didAddMethod) {
            class_replaceMethod(class,
                swizzledSelector,
                method_getImplementation(originalMethod),
                method_getTypeEncoding(originalMethod));
        } else {
            method_exchangeImplementations(originalMethod, swizzledMethod);
        }
    });
}

- (void)melon_viewWillAppear:(BOOL)animated {
    [self melon_viewWillAppear:animated];
    NSLog(@“View Controller %@ view will appear”, self);
}
@end
```

可以看到如果通过 runtime 提供的方法来进行 `method swizzling` 的话，我们需要进行以下工作：

1. 新建分类，在分类中添加 `load` 方法，在 `load` 方法中进行 `method swizzling` ；
2. 在分类中添加需要替换的具有相同参数的方法； 如果有大量类的需要进行 `method swizzling` ，我们就需要编写大量分类和参数相同的方法。为了解决这个问题，`Aspects` 给我们提供了通过 `Block` 来进行 `method swizzling` 的途径，不需要分类，不需要编写参数相同的方法，一切都在 `Block` 中进行。下面来看下优雅地使用 `Aspects` 实现相同的功能：

```objectivec
[UIViewController aspect_hookSelector:@selector(viewWillAppear:)
                          withOptions:AspectPositionAfter
                           usingBlock:^(id<AspectInfo> aspectInfo, BOOL animated) {
        NSLog(@“View Controller %@ view will appear", aspectInfo.instance);
    }
                                error:NULL];
```

不算上自己实现的 `Block` 代码，`Aspects` 几乎算得上是只需要一行代码就可以实现 `method swizzling` 。

## 原理

> Aspects uses Objective-C message forwarding to hook into messages. This will create some overhead. Don’t add aspects to methods that are called a lot. Aspects is meant for view/controller code that is not called a 1000 times per second.
> 
> Adding aspects returns an opaque token which can be used to deregister again. All calls are thread safe.

上面是 `Aspects` 的说明，可以看到 `Aspects` 是通过 `Objective-C` 的消息转发来实现 hook 方法的。它会带来一些性能消耗。不要对那些会在一定时间内大量调用的方法使用。`Aspects` 也提供了一个用于还原 hook 的 token 。 `Objective-C` 是一门消息发送的语言，消息由接收对象，selector 和参数构成，消息派发系统会根据这三者来寻找对应的 IMP ，也就是具体的方法实现，如果给某个对象发送了一条无法找到对应 IMP 的 selector ，就会进入消息转发流程。

### resolveInstanceMethod

对象在接受到无法处理的 selector 时，首先会调用：

```objectivec
+ (BOOL)resolveInstanceMethod:(SEL)selector;
```

在返回结果前，可以动态地添加方法，然后返回 YES ：

```objectivec
+ (BOOL)resolveInstanceMethod:(SEL)selector {
	  if (selector 符合条件) {
        class_addMethod(self, selector, imp, @“v@:@");
        return YES;
    }
    return NO;
}
```

如果是类方法，则会调用 `resolveClassMethod:` 方法。

### forwardingTargetForSelector

如果 `resolveInstanceMethod:` 返回 NO ，那么就会调用 `forwardingTargetForSelector:` 方法，可以将方法转给其它对象来处理：

```objectivec
- (id)forwardingTargetForSelector:(SEL)selector;
```

返回的 id 为对应的执行方法的对象，通过 `forwardingTargetForSelector:` 可以实现类似多继承的特性。 如果当前的对象没有实现对应的方法，我们也可以在 `forwardingTargetForSelector:` 里动态生成一个新的类，然后给它添加对应的方法，再转发给新的类的对象，防止出现 `doesNotRecognizeSelector:` 的崩溃，当然我个人觉得越早崩溃越容易发现问题，不然有些逻辑上的错误找不出来。

### forwardInvocation

如果 `forwardingTargetForSelector:` 返回的 id 为 nil ，就会走到消息转发流程的最后一步，首先会调用 `methodSignatureForSelector:` 方法来生成 `NSMethodSignature` 对象，`NSMethodSignature` 包含 selector 的各种信息，参数类型，返回类型和调用对象类型等，它用于创建 `NSInvocation` 对象。当 `methodSignatureForSelector:` 返回了一个 `NSMethodSignature` 对象后，就会调用 `forwardInvocation:` 方法：

```objectivec
- (void)forwardInvocation:(NSInvocation *)invocation {
    [invocation setTarget:self.target];
    [invocation invoke];
}
```

通过 `NSInvocation` ，我们可以修改 selector 的接收对象，参数和返回值，等等。可以做的事情比较多。

### 消息转发整体流程

整体流程如下图所示， `resolveInstanceMethod:` 主要用于为类动态添加方法，`forwardingTargetForSelector:` 则用于将接收对象转换成其它类的对象， `forwardInvocation:` 可以做的事情较多，但是越往后成本越大，所以如果需要转换消息的接收对象，最好是在 `forwardingTargetForSelector:` 中执行，而不是在 `forwardInvocation:` 中转换。

![Artboard](https://raw.githubusercontent.com/dirtmelon/blog-images/main/Artboard.png)

`Aspects` 则是选择在 `forwardInvocations:` 上进行处理，对应需要 hook 的 selector ，`Aspects` 将其指向了 `_objc_msgForward` 方法，同时也对 `forwardInvocation:` 方法进行 hook 处理，使其指向自己的 `__ASPECTS_ARE_BEING_CALLED__` 方法，在 `__ASPECTS_ARE_BEING_CALLED__` 中插入自己需要进行调用的方法，然后会生成一个新的 `aliasSelector` 指向原有的方法 IMP ，通过 `aliasSelector` 来调用原有的方法。

![Artboard](https://raw.githubusercontent.com/dirtmelon/blog-images/main/Artboard-1.png)

## 先来看看头文件

`Aspects.h` 首先定义了 hook 的几种类型

```objectivec
typedef NS_OPTIONS(NSUInteger, AspectOptions) {
    AspectPositionAfter   = 0,            /// 在原方法之后执行
    AspectPositionInstead = 1,            /// 替代原方法
    AspectPositionBefore  = 2,            /// 在原方法之前执行
    AspectOptionAutomaticRemoval = 1 << 3 /// 只执行一次
};
```

`id<AspectToken>` 是 `Aspects` 在 hook 方法时返回的结果，使用 protocol 的方式对具体的类进行了抽象，调用者不需要关心具体的类是什么，只需要知道它是个遵循了 `AspectToken` protocol 的类。`id<AspectToken>` 相当于每个 hook 的 token ，通过这个 token ，我们可以调用 `remove` 方法来移除特定的 hook ：

```objectivec
/// Opaque Aspect Token that allows to deregister the hook.
@protocol AspectToken <NSObject>

/// Deregisters an aspect.
/// @return YES if deregistration is successful, otherwise NO.
- (BOOL)remove;
@end
```

`id<AspectInfo>` 协议，是我们使用的 `block` 返回的第一个参数，

```objectivec
/// The AspectInfo protocol is the first parameter of our block syntax.
@protocol AspectInfo <NSObject>

/// 当前被 hook 的实例。
- (id)instance;

/// 原始的 invocation 。
- (NSInvocation *)originalInvocation;

/// 方法参数，懒加载。
- (NSArray *)arguments;

@end
```

然后 `Aspects.h` 给 `NSObject` 添加了两个 hook 方法，一个是类方法，一个是实例方法，根据说明，`block` 的第一个参数是 `id<AspectInfo>` ，紧接着是被 hook 的方法的所有参数，这些都是可选的，你可以直接使用一个没有参数的 `block` ，也可以只传 `id<AspectInfo>` ，还可以输入跟原有方法参数一样的参数列表。

```objectivec
@interface NSObject (Aspects)
+ (id<AspectToken>)aspect_hookSelector:(SEL)selector
                           withOptions:(AspectOptions)options
                            usingBlock:(id)block
                                 error:(NSError **)error;

/// 针对特定对象进行 hook
- (id<AspectToken>)aspect_hookSelector:(SEL)selector
                           withOptions:(AspectOptions)options
                            usingBlock:(id)block
                                 error:(NSError **)error;

@end
```

## 走进 Aspect

`Aspect` 的入口只有 `NSObject` 的两个 hook 方法，以下是两个 hook 的方法的具体实现：

```objectivec
+ (id<AspectToken>)aspect_hookSelector:(SEL)selector
                      withOptions:(AspectOptions)options
                       usingBlock:(id)block
                            error:(NSError **)error {
    return aspect_add((id)self, selector, options, block, error);
}

/// @return A token which allows to later deregister the aspect.
- (id<AspectToken>)aspect_hookSelector:(SEL)selector
                      withOptions:(AspectOptions)options
                       usingBlock:(id)block
                            error:(NSError **)error {
    return aspect_add(self, selector, options, block, error);
}
```

可以看到不管是类还是实例方法的 hook ，都是统一调度 `aspect_add` 方法。只是类对象需要加多一层 `(id)self` 的转换。下面来看看作为统一入口的 `aspect_add` 方法的实现：

```objectivec
static id aspect_add(id self, SEL selector, AspectOptions options, id block, NSError **error) {
    NSCParameterAssert(self);
    NSCParameterAssert(selector);
    NSCParameterAssert(block);

    __block AspectIdentifier *identifier = nil;
	  // 给 hook 操作加锁
    aspect_performLocked(^{
 		  // 判断方法是否允许被 hook
        if (aspect_isSelectorAllowedAndTrack(self, selector, options, error)) {
            AspectsContainer *aspectContainer = aspect_getContainerForObject(self, selector);
            identifier = [AspectIdentifier identifierWithSelector:selector object:self options:options block:block error:error];
            if (identifier) {
                [aspectContainer addAspect:identifier withOptions:options];
				   // 进行 hook 的具体操作
                aspect_prepareClassAndHookSelector(self, selector, error);
            }
        }
    });
    return identifier;
}
```

`aspect_add` 作为内部实现的第一层方法，负责统筹调度各个内部方法，它自己并没有什么单独的代码逻辑。

## aspect_performLocked

为了方便加减锁，`Aspects` 提供了 `aspect_performLocked` 的方法，可以直接在 block 里进行线程安全的操作：

```objectivec
static void aspect_performLocked(dispatch_block_t block) {
    static OSSpinLock aspect_lock = OS_SPINLOCK_INIT;
    OSSpinLockLock(&aspect_lock);
    block();
    OSSpinLockUnlock(&aspect_lock);
}
```

使用的是 `OSSpinLock` ，但是 `OSSpinLock` 存在优先级反转的问题，具体可以看这里 [不再安全的 OSSpinLock

Garan no dou](https://blog.ibireme.com/2016/01/16/spinlock_is_unsafe_in_ios/) ，苹果推荐我们使用 `os_unfair_lock` 来替换掉，替换成 `os_unfair_lock` 后的代码如下：

```objectivec
static void aspect_performLocked(dispatch_block_t block) {
    static os_unfair_lock aspect_lock = OS_UNFAIR_LOCK_INIT;
    os_unfair_lock_lock(&aspect_lock);
    block();
    os_unfair_lock_unlock(&aspect_lock);
}
```

## aspect_isSelectorAllowedAndTrack

### AspectTracker

在开始说 `aspect_isSelectorAllowedAndTrack` 前先说说 `AspectTracker` ，` AspectTracker` 用于 hook 时判断子父类是否有重复 hook 。

```objectivec
@interface AspectTracker : NSObject
- (id)initWithTrackedClass:(Class)trackedClass;
// hook 的类
@property (nonatomic, strong) Class trackedClass;
// hook 的类名，在调用时会通过 NSStringFromClass 来生成
@property (nonatomic, readonly) NSString *trackedClassName;
// 被 hook 的方法名
@property (nonatomic, strong) NSMutableSet *selectorNames;
// 子类已经进行 hook 的方法名
@property (nonatomic, strong) NSMutableDictionary *selectorNamesToSubclassTrackers;
- (void)addSubclassTracker:(AspectTracker *)subclassTracker hookingSelectorName:(NSString *)selectorName;
- (void)removeSubclassTracker:(AspectTracker *)subclassTracker hookingSelectorName:(NSString *)selectorName;
- (BOOL)subclassHasHookedSelectorName:(NSString *)selectorName;
- (NSSet *)subclassTrackersHookingSelectorName:(NSString *)selectorName;
@end

@implementation AspectTracker

- (id)initWithTrackedClass:(Class)trackedClass {
    if (self = [super init]) {
        _trackedClass = trackedClass;
        _selectorNames = [NSMutableSet new];
        _selectorNamesToSubclassTrackers = [NSMutableDictionary new];
    }
    return self;
}

- (BOOL)subclassHasHookedSelectorName:(NSString *)selectorName {
    return self.selectorNamesToSubclassTrackers[selectorName] != nil;
}

- (void)addSubclassTracker:(AspectTracker *)subclassTracker hookingSelectorName:(NSString *)selectorName {
    NSMutableSet *trackerSet = self.selectorNamesToSubclassTrackers[selectorName];
    if (!trackerSet) {
        trackerSet = [NSMutableSet new];
        self.selectorNamesToSubclassTrackers[selectorName] = trackerSet;
    }
    [trackerSet addObject:subclassTracker];
}
- (void)removeSubclassTracker:(AspectTracker *)subclassTracker hookingSelectorName:(NSString *)selectorName {
    NSMutableSet *trackerSet = self.selectorNamesToSubclassTrackers[selectorName];
    [trackerSet removeObject:subclassTracker];
    if (trackerSet.count == 0) {
        [self.selectorNamesToSubclassTrackers removeObjectForKey:selectorName];
    }
}
- (NSSet *)subclassTrackersHookingSelectorName:(NSString *)selectorName {
    NSMutableSet *hookingSubclassTrackers = [NSMutableSet new];
    for (AspectTracker *tracker in self.selectorNamesToSubclassTrackers[selectorName]) {
        if ([tracker.selectorNames containsObject:selectorName]) {
            [hookingSubclassTrackers addObject:tracker];
        }
        [hookingSubclassTrackers unionSet:[tracker subclassTrackersHookingSelectorName:selectorName]];
    }
    return hookingSubclassTrackers;
}
- (NSString *)trackedClassName {
    return NSStringFromClass(self.trackedClass);
}

- (NSString *)description {
    return [NSString stringWithFormat:@“<%@: %@, trackedClass: %@, selectorNames:%@, subclass selector names: %@>”, self.class, self, NSStringFromClass(self.trackedClass), self.selectorNames, self.selectorNamesToSubclassTrackers.allKeys];
}

@end
```

`AspectTracker` 维护了一个字典 selectorNamesToSubclassTrackers ，以 selectorName 为 key ，value 为 `NSMutableSet` ，包含子类中对应 selectorName 的 tracker 。

`aspect_isSelectorAllowedAndTrack` 对 SEL 和类方法重复 hook 做了处理，下面分段来说下具体的处理逻辑。

`disallowedSelectorList` 包含了 `retain` ， `release` ， `autorelease` 和 `forwardInvocation` ，不允许对以上四个方法进行 hook：

```objectivec
static NSSet *disallowedSelectorList;
static dispatch_once_t pred;
dispatch_once(&pred, ^{
    disallowedSelectorList = [NSSet setWithObjects:@"retain”, @“release”, @“autorelease”, @“forwardInvocation:”, nil];
});

NSString *selectorName = NSStringFromSelector(selector);
if ([disallowedSelectorList containsObject:selectorName]) {
	  NSString *errorDescription = [NSString stringWithFormat:@"Selector %@ is blacklisted.", selectorName];
    AspectError(AspectErrorSelectorBlacklisted, errorDescription);
    return NO;
}
```

对于 `dealloc` 方法，只允许进行 `AspectPositionBefore` 的 hook ：

```objectivec
AspectOptions position = options&AspectPositionFilter;
if ([selectorName isEqualToString:@"dealloc"] && position != AspectPositionBefore) {
    NSString *errorDesc = @"AspectPositionBefore is the only valid position when hooking dealloc.”;
    AspectError(AspectErrorSelectorDeallocPosition, errorDesc);
    return NO;
}
```

检查是否有包含需要进行 hook 的方法：

```objectivec
if (![self respondsToSelector:selector] && ![self.class instancesRespondToSelector:selector]) {
     NSString *errorDesc = [NSString stringWithFormat:@"Unable to find selector -[%@ %@].", NSStringFromClass(self.class), selectorName];
     AspectError(AspectErrorDoesNotRespondToSelector, errorDesc);
     return NO;
}
```

最后就是针对类方法的重复 hook 。 判断是否为类对象，如果是类对象，则表示是在类这一层上进行 hook ，需要判断是否有重复 hook 相同的方法。这里判断是否为类对象时使用了 `object_getClass` ，跟 `class` 方法不同在于，如果 `self` 为类对象( `Class` )，则会返回 `meta class` ，如果是实例对象 ( `Instance` )，则返回类对象( `Class` )。而 `class` 只会返回类对象。如果是实例对象则不需要检测是否有重复 hook 相同的方法。

为什么需要判断是否有重复 hook 呢？因为 Aspect 是在消息转发流程的时候对原有的方法进行处理，所有消息都会经由它自己生成的 `__ASPECTS_ARE_BEING_CALLED__` 方法，如果子类和父类 hook 了同一个方法，子类的方法调用父类方法时，父类的方法走到 `__ASPECTS_ARE_BEING_CALLED__` 方法时就会丢失了是由父类进行调用这一信息，于是会重新调用子类的方法，造成死循环，所以这里要进行判断。

```objectivec
if (class_isMetaClass(object_getClass(self))) {
    // 防止重复 hook
} else {
    return YES;
}
```

`aspect_getSwizzledClassesDict()` 方法返回一个全局的 `NSMutableDictionary` ，用于记录已经进行过 hook 的类对应的 `AspectTracker`：

```objectivec
static NSMutableDictionary *aspect_getSwizzledClassesDict() {
    static NSMutableDictionary *swizzledClassesDict;
    static dispatch_once_t pred;
    dispatch_once(&pred, ^{
        swizzledClassesDict = [NSMutableDictionary new];
    });
    return swizzledClassesDict;
}
```

判断是否有进行过类是否有 hook 过相同的方法：

```objectivec
Class klass = [self class];
NSMutableDictionary *swizzledClassesDict = aspect_getSwizzledClassesDict();
Class currentClass = [self class];

AspectTracker *tracker = swizzledClassesDict[currentClass];
if ([tracker subclassHasHookedSelectorName:selectorName]) {
	  NSSet *subclassTracker = [tracker subclassTrackersHookingSelectorName:selectorName];
    NSSet *subclassNames = [subclassTracker valueForKey:@"trackedClassName"];
    NSString *errorDescription = [NSString stringWithFormat:@"Error: %@ already hooked subclasses: %@. A method can only be hooked once per class hierarchy.", selectorName, subclassNames];
    AspectError(AspectErrorSelectorAlreadyHookedInClassHierarchy, errorDescription);
    return NO;
}
```

首先获取对应的 `AspectTracker` ，然后通过 `subclassHasHookedSelectorName:` 方法判断子类是否有进行过 hook ，如果有，则返回 NO ，并输出对应的方法名和子类名，如果没有，则继续以下操作：

```objectivec
do {
    tracker = swizzledClassesDict[currentClass];
    if ([tracker.selectorNames containsObject:selectorName]) {
        if (klass == currentClass) {
            // Already modified and topmost!
            return YES;
        }
        NSString *errorDescription = [NSString stringWithFormat:@“Error: %@ already hooked in %@. A method can only be hooked once per class hierarchy.", selectorName, NSStringFromClass(currentClass)];
        AspectError(AspectErrorSelectorAlreadyHookedInClassHierarchy, errorDescription);
        return NO;
    }
} while ((currentClass = class_getSuperclass(currentClass)));
```

之前已经检查过子类是否有 hook 过对应的方法，这里进行的是父类的检查，不断向上获取 superclass ，如果父类有 hook 过对应的方法，就返回 NO 。

```objectivec
// Add the selector as being modified.
currentClass = klass;
AspectTracker *subclassTracker = nil;
do {
    tracker = swizzledClassesDict[currentClass];
    if (!tracker) {
        tracker = [[AspectTracker alloc] initWithTrackedClass:currentClass];
        swizzledClassesDict[(id<NSCopying>)currentClass] = tracker;
    }
    if (subclassTracker) {
        [tracker addSubclassTracker:subclassTracker hookingSelectorName:selectorName];
    } else {
        [tracker.selectorNames addObject:selectorName];
    }

    // All superclasses get marked as having a subclass that is modified.
    subclassTracker = tracker;
}while ((currentClass = class_getSuperclass(currentClass)));
// …
return YES;
```

如果子类和父类都没有 hook 过对应的方法，那么就可以进行记录，需要遍历所有父类对应的 tracker ，在循环过程中，将上一次获取子类的 tracker 添加到父类的 subclassTracker 中。

## aspect_getContainerForObject

在完成 hook 方法的合法性检测后，就需要获取到 `AspectsContainer` 。

### AspectIdentifier

由于 `AspectsContainer` 会包含 `AspectIdentifier` ，所以先来说下 `AspectIdentifier` :

```objectivec
// Tracks a single aspect.
@interface AspectIdentifier : NSObject
+ (instancetype)identifierWithSelector:(SEL)selector object:(id)object options:(AspectOptions)options block:(id)block error:(NSError **)error;
- (BOOL)invokeWithInfo:(id<AspectInfo>)info;
@property (nonatomic, assign) SEL selector;
@property (nonatomic, strong) id block;
@property (nonatomic, strong) NSMethodSignature *blockSignature;
@property (nonatomic, weak) id object;
@property (nonatomic, assign) AspectOptions options;
@end
```

`AspectIdentifier` 通过以下方法来初始化：

```objectivec
+ (instancetype)identifierWithSelector:(SEL)selector object:(id)object options:(AspectOptions)options block:(id)block error:(NSError **)error {
    NSCParameterAssert(block);
    NSCParameterAssert(selector);
    NSMethodSignature *blockSignature = aspect_blockMethodSignature(block, error); // TODO: check signature compatibility, etc.
    if (!aspect_isCompatibleBlockSignature(blockSignature, object, selector, error)) {
        return nil;
    }

    AspectIdentifier *identifier = nil;
    if (blockSignature) {
        identifier = [AspectIdentifier new];
        identifier.selector = selector;
        identifier.block = block;
        identifier.blockSignature = blockSignature;
        identifier.options = options;
        identifier.object = object; // weak
    }
    return identifier;
}
```

### aspect_blockMethodSignature

```objectivec
static NSMethodSignature *aspect_blockMethodSignature(id block, NSError **error) {
    AspectBlockRef layout = (__bridge void *)block;
	// 首先判断根据 flags 判断是否包含有方法签名，如果没有则报错
	if (!(layout->flags & AspectBlockFlagsHasSignature)) {
        NSString *description = [NSString stringWithFormat:@“The block %@ doesn’t contain a type signature.”, block];
        AspectError(AspectErrorMissingBlockSignature, description);
        return nil;
    }
	void *desc = layout->descriptor;
  // 根据 block 结构体做位置上的迁移
	desc += 2 * sizeof(unsigned long int);
	if (layout->flags & AspectBlockFlagsHasCopyDisposeHelpers) {
		desc += 2 * sizeof(void *);
    }
  // 判断是否有指向 signature
	if (!desc) {
        NSString *description = [NSString stringWithFormat:@"The block %@ doesn't has a type signature.", block];
        AspectError(AspectErrorMissingBlockSignature, description);
        return nil;
    }
	const char *signature = (*(const char **)desc);
	return [NSMethodSignature signatureWithObjCTypes:signature];
}
```

通过 `aspect_blockMethodSignature` 可以将 block 转换为 `NSMethodSignature` 。方法的第一行将 block 显示声明为 `AspectBlockRef` 结构体， `AspectBlockRef` 结构体的则是根据苹果公开的 block 结构来定义的， [compiler-rt/Block_private.h](https://github.com/llvm-mirror/compiler-rt/blob/master/lib/BlocksRuntime/Block_private.h) ，所以可以显式地将 `block` 转换为结构体 `AspectBlockRef` 。

```objc
// Block internals.
typedef NS_OPTIONS(int, AspectBlockFlags) {
	AspectBlockFlagsHasCopyDisposeHelpers = (1 << 25),
	AspectBlockFlagsHasSignature          = (1 << 30)
};
typedef struct _AspectBlock {
	__unused Class isa;
	AspectBlockFlags flags;
	__unused int reserved;
	void (__unused *invoke)(struct _AspectBlock *block, ...);
	struct {
		unsigned long int reserved;
		unsigned long int size;
		// requires AspectBlockFlagsHasCopyDisposeHelpers
		void (*copy)(void *dst, const void *src);
		void (*dispose)(const void *);
		// requires AspectBlockFlagsHasSignature
		const char *signature;
		const char *layout;
	} *descriptor;
	// imported variables
} *;AspectBlockRef
```

### aspect_isCompatibleBlockSignature

在获取到 block 的 `NSMethodSignature` 后，则需要判断是否合法，于是又调用了 `aspect_isCompatibleBlockSignature ` ：

```objectivec
static BOOL aspect_isCompatibleBlockSignature(NSMethodSignature *blockSignature, id object, SEL selector, NSError **error) {
    NSCParameterAssert(blockSignature);
    NSCParameterAssert(object);
    NSCParameterAssert(selector);

    BOOL signaturesMatch = YES;
	  // 先根据 selector 生成 NSMethodSignature
    NSMethodSignature *methodSignature = [[object class] instanceMethodSignatureForSelector:selector];
    // 在判断 blockSignature 的参数数量是否大于 methodSignature 的参数数量
    // 因为 Aspect 并没有限制 block 一定要有参数，因此 methodSignature 的参数数量是可以大于 blockSignature 的参数数量
    // 这给予了 Aspect 充分的灵活性
    if (blockSignature.numberOfArguments > methodSignature.numberOfArguments) {
        signaturesMatch = NO;
    }else {
        if (blockSignature.numberOfArguments > 1) {
            // blockSignature 参数必定包含 block ，如果 > 1 ，则第一个参数必须为 id<AspectInfo>
  	          // 对应的 typeCode 为 '@'
            const char *blockType = [blockSignature getArgumentTypeAtIndex:1];
            if (blockType[0] != '@') {
                signaturesMatch = NO;
            }
        }
        // 逐个比较参数的类型是否相同
        if (signaturesMatch) {
            for (NSUInteger idx = 2; idx < blockSignature.numberOfArguments; idx++) {
                const char *methodType = [methodSignature getArgumentTypeAtIndex:idx];
                const char *blockType = [blockSignature getArgumentTypeAtIndex:idx];
                // Only compare parameter, not the optional type data.
                if (!methodType || !blockType || methodType[0] != blockType[0]) {
                    signaturesMatch = NO; break;
                }
            }
        }
    }

    if (!signaturesMatch) {
        NSString *description = [NSString stringWithFormat:@"Block signature %@ doesn't match %@.", blockSignature, methodSignature];
        AspectError(AspectErrorIncompatibleBlockSignature, description);
        return NO;
    }
    return YES;
}
```

在进行完所有检测之后，就可以生成对应的 `AspectIdentifier` 。

### AspectsContainer

`AsepectsContainer` 包含一个对象或者类的所有 `AspectIdentifier` ，负责管理 `AspectIdentifier` 。

```objectivec
// Tracks all aspects for an object/class.
@interface AspectsContainer : NSObject
- (void)addAspect:(AspectIdentifier *)aspect withOptions:(AspectOptions)injectPosition;
- (BOOL)removeAspect:(id)aspect;
- (BOOL)hasAspects;
@property (atomic, copy) NSArray *beforeAspects;
@property (atomic, copy) NSArray *insteadAspects;
@property (atomic, copy) NSArray *afterAspects;
@end
```

每次生成 `AspectsContainer` 都是通过 `aspect_getContainerForObject` 方法来获取：

```objectivec
static AspectsContainer *aspect_getContainerForObject(NSObject *self, SEL selector) {
    NSCParameterAssert(self);
    // 生成一个带有 “aspects_” 前缀的 selector
    SEL aliasSelector = aspect_aliasForSelector(selector);
	  // 根据生成的 selector 获取对应的 container ，如果 container 为空，则生成一个新的，并设置到对应的对象中
    AspectsContainer *aspectContainer = objc_getAssociatedObject(self, aliasSelector);
    if (!aspectContainer) {
        aspectContainer = [AspectsContainer new];
        objc_setAssociatedObject(self, aliasSelector, aspectContainer, OBJC_ASSOCIATION_RETAIN);
    }
    return aspectContainer;
}
```

最后再将生成的 `AspectIdentifier` 添加到 `AspectsContainer` 中：

```objectivec
identifier = [AspectIdentifier identifierWithSelector:selector object:self options:options block:block error:error];
if (identifier) {
    [aspectContainer addAspect:identifier withOptions:options];

    // Modify the class to allow message interception.
    aspect_prepareClassAndHookSelector(self, selector, error);
}
```

## aspect_prepareClassAndHookSelector

接下来开始进行一些准备工作和 hook 操作：

```objectivec
static void aspect_prepareClassAndHookSelector(NSObject *self, SEL selector, NSError **error) {
    NSCParameterAssert(selector);
    Class klass = aspect_hookClass(self, error);
    Method targetMethod = class_getInstanceMethod(klass, selector);
    IMP targetMethodIMP = method_getImplementation(targetMethod);
    if (!aspect_isMsgForwardIMP(targetMethodIMP)) {
        // Make a method alias for the existing method implementation, it not already copied.
        const char *typeEncoding = method_getTypeEncoding(targetMethod);
        SEL aliasSelector = aspect_aliasForSelector(selector);
        if (![klass instancesRespondToSelector:aliasSelector]) {
            __unused BOOL addedAlias = class_addMethod(klass, aliasSelector, method_getImplementation(targetMethod), typeEncoding);
            NSCAssert(addedAlias, @"Original implementation for %@ is already copied to %@ on %@", NSStringFromSelector(selector), NSStringFromSelector(aliasSelector), klass);
        }

        // We use forwardInvocation to hook in.
        class_replaceMethod(klass, selector, aspect_getMsgForwardIMP(self, selector), typeEncoding);
        AspectLog(@"Aspects: Installed hook for -[%@ %@].", klass, NSStringFromSelector(selector));
    }
}
```

同样地， `aspect_prepareClassAndHookSelector` 方法也没有太多自己的实现逻辑，只是负责调用其它方法。

### aspect_hookClass

```objectivec
static Class aspect_hookClass(NSObject *self, NSError **error) {
    NSCParameterAssert(self);
  // statedClass 是类对象
  // baseClass 是类的 isa
	Class statedClass = self.class;
	Class baseClass = object_getClass(self);
  // 获取类 isa 的类名
	NSString *className = NSStringFromClass(baseClass);

  // 如果 className 包含 “_Aspects_" ，则表示它已经被 hook 处理过，直接返回即可
	if ([className hasSuffix:AspectsSubclassSuffix]) {
		return baseClass;
	}else if (class_isMetaClass(baseClass)) {
		  // 如果 baseClass 是isa，则表示是在 Class 层面进行 hook ，需要进行 aspect_swizzleClassInPlace
        return aspect_swizzleClassInPlace((Class)self);
    }else if (statedClass != baseClass) {
		  // 如果 statedClass 与 baseClass 不相等，则说明有可能是 KVO 过的对象，因为 KVO 对象会生成一个中间类
        // 也进行 aspect_swizzleClassInPlace
        return aspect_swizzleClassInPlace(baseClass);
    }

  // 这里往下是在实例对象层面进行 hook 方法操作，会参考 KVO 的实现原理，动态生成一个新的子类
  // 子类包含后缀 “_Aspects_”
	const char *subclassName = [className stringByAppendingString:AspectsSubclassSuffix].UTF8String;
	Class subclass = objc_getClass(subclassName);

	if (subclass == nil) {
		subclass = objc_allocateClassPair(baseClass, subclassName, 0);
		if (subclass == nil) {
            NSString *errrorDesc = [NSString stringWithFormat:@"objc_allocateClassPair failed to allocate class %s.", subclassName];
            AspectError(AspectErrorFailedToAllocateClassPair, errrorDesc);
            return nil;
        }
		// hook 转发方法
		aspect_swizzleForwardInvocation(subclass);
      // 将 class 方法指回给原来的类
		aspect_hookedGetClass(subclass, statedClass);
		aspect_hookedGetClass(object_getClass(subclass), statedClass);
      // 生成新的类
		objc_registerClassPair(subclass);
	}
  // 设置 self 为新生成的子类
	object_setClass(self, subclass);
	return subclass;
}
```

### aspect_swizzleClassInPlace

```objectivec
static Class aspect_swizzleClassInPlace(Class klass) {
    NSCParameterAssert(klass);
    NSString *className = NSStringFromClass(klass);

    _aspect_modifySwizzledClasses(^(NSMutableSet *swizzledClasses) {
        if (![swizzledClasses containsObject:className]) {
            aspect_swizzleForwardInvocation(klass);
            [swizzledClasses addObject:className];
        }
    });
    return klass;
}
```

`aspect_swizzleClassInPlace` 做重复性判断，防止重复 hook 相同的类。

### _aspect_modifySwizzledClasses

```objectivec
static void _aspect_modifySwizzledClasses(void (^block)(NSMutableSet *swizzledClasses)) {
    // 维护一个全局的 NSMutableSet ，用来记录进行过 swizzle 的 Class
    static NSMutableSet *swizzledClasses;
    static dispatch_once_t pred;
    // dispatch_once 保证只执行一次
    dispatch_once(&pred, ^{
        swizzledClasses = [NSMutableSet new];
    });
    // @synchronized 线程安全
    @synchronized(swizzledClasses) {
        block(swizzledClasses);
    }
}
```

### aspect_swizzleForwardInvocation

```objectivec
static NSString *const AspectsForwardInvocationSelectorName = @"__aspects_forwardInvocation:”;
static void aspect_swizzleForwardInvocation(Class klass) {
    NSCParameterAssert(klass);
    // If there is no method, replace will act like class_addMethod.
    IMP originalImplementation = class_replaceMethod(klass, @selector(forwardInvocation:), (IMP)__ASPECTS_ARE_BEING_CALLED__, “v@:@“);
    if (originalImplementation) {
        class_addMethod(klass, NSSelectorFromString(AspectsForwardInvocationSelectorName), originalImplementation, "v@:@");
    }
    AspectLog(@"Aspects: %@ is now aspect aware.", NSStringFromClass(klass));
}
```

对 Class 的 `forwardInvocation:` 方法进行 hook ，替换成自己的 `__ASPECTS_ARE_BEING_CALLED__` 方法。

### aspect_hookedGetClass

```objectivec
static void aspect_hookedGetClass(Class class, Class statedClass) {
    NSCParameterAssert(class);
    NSCParameterAssert(statedClass);
	Method method = class_getInstanceMethod(class, @selector(class));
	IMP newIMP = imp_implementationWithBlock(^(id self) {
		return statedClass;
	});
	class_replaceMethod(class, @selector(class), newIMP, method_getTypeEncoding(method));
}
```

因为在 hook 对象层面的方法时，我们动态生成了一个子类，所以需要将子类和子类 isa 的 `class` 方法指回给原来的类。

```objectivec
aspect_hookedGetClass(subclass, statedClass);
aspect_hookedGetClass(object_getClass(subclass), statedClass);
```

### aspect_prepareClassAndHookSelector

做完以上准备后回到 `aspect_prepareClassAndHookSelector` 接着走完剩下的流程

```objectivec
static void aspect_prepareClassAndHookSelector(NSObject *self, SEL selector, NSError **error) {
    NSCParameterAssert(selector);
    // kClass 是需要进行操作的类
    Class klass = aspect_hookClass(self, error);
    Method targetMethod = class_getInstanceMethod(klass, selector);
    IMP targetMethodIMP = method_getImplementation(targetMethod);
    if (!aspect_isMsgForwardIMP(targetMethodIMP)) {
        // Make a method alias for the existing method implementation, it not already copied.
        const char *typeEncoding = method_getTypeEncoding(targetMethod);
        // 生成带前缀 “aspects_” 的 selector
        SEL aliasSelector = aspect_aliasForSelector(selector);
        if (![klass instancesRespondToSelector:aliasSelector]) {
            // 添加 aliasSelector ，IMP 为原来的方法 IMP 。
            __unused BOOL addedAlias = class_addMethod(klass, aliasSelector, method_getImplementation(targetMethod), typeEncoding);
            NSCAssert(addedAlias, @"Original implementation for %@ is already copied to %@ on %@", NSStringFromSelector(selector), NSStringFromSelector(aliasSelector), klass);
        }

        // 将 selector 指向 aspect_getMsgForwardIMP 即 _objc_msgForward
        class_replaceMethod(klass, selector, aspect_getMsgForwardIMP(self, selector), typeEncoding);
        AspectLog(@"Aspects: Installed hook for -[%@ %@].", klass, NSStringFromSelector(selector));
    }
}
```

```objectivec
// 判断是否为消息转发的 IMP 。
static BOOL aspect_isMsgForwardIMP(IMP impl) {
    return impl == _objc_msgForward
#if !defined(__arm64__)
    || impl == (IMP)_objc_msgForward_stret
#endif
    ;
}
```

## **ASPECTS_ARE_BEING_CALLED**

`__ASPECTS_ARE_BEING_CALLED__` 是 `Aspect` hook 后提供的 `forwardInvocation:` 方法：

```objectivec
SEL originalSelector = invocation.selector;
SEL aliasSelector = aspect_aliasForSelector(invocation.selector);
invocation.selector = aliasSelector;
```

`invocation.selector` 为原有的 selector ，但是经过 hook 后已经指向了 `_objc_msgForward` ， `aliasSelector` 才是指向原有 IMP 的 selector 。

```objectivec
AspectsContainer *objectContainer = objc_getAssociatedObject(self, aliasSelector);
AspectsContainer *classContainer = aspect_getContainerForClass(object_getClass(self), aliasSelector);
AspectInfo *info = [[AspectInfo alloc] initWithInstance:self invocation:invocation];
NSArray *aspectsToRemove = nil;
```

获取对应的 container ，同时生成对应的 `AspectInfo` 。

```objectivec
// Before hooks.
aspect_invoke(classContainer.beforeAspects, info);
aspect_invoke(objectContainer.beforeAspects, info);
```

运行 hook 前的 `beforeAspects`

```objectivec
BOOL respondsToAlias = YES;
// 判断是否需要运行替代 hook ，检查 `insteadAspects` 是否为空
if (objectContainer.insteadAspects.count || classContainer.insteadAspects.count) {
    aspect_invoke(classContainer.insteadAspects, info);
    aspect_invoke(objectContainer.insteadAspects, info);
}else {
    Class klass = object_getClass(invocation.target);
    do {
        if ((respondsToAlias = [klass instancesRespondToSelector:aliasSelector])) {
            // invocation 的 selector 在前面已经被替换 aliasSelector ，对应的是原始方法的 IMP 。
            [invocation invoke];
            break;
        }
    }while (!respondsToAlias && (klass = class_getSuperclass(klass)));
}
```

```objectivec
aspect_invoke(classContainer.afterAspects, info);
aspect_invoke(objectContainer.afterAspects, info);
```

运行 hook 后的 `afterAspects`

```objectivec
if (!respondsToAlias) {
    invocation.selector = originalSelector;
    SEL originalForwardInvocationSEL = NSSelectorFromString(AspectsForwardInvocationSelectorName);
    if ([self respondsToSelector:originalForwardInvocationSEL]) {
        ((void( *)(id, SEL, NSInvocation *))objc_msgSend)(self, originalForwardInvocationSEL, invocation);
    }else {
        [self doesNotRecognizeSelector:invocation.selector];
    }
}
[aspectsToRemove makeObjectsPerformSelector:@selector(remove)];
```

没有成功 hook ，调用原有的 `forwardInvocation:` 对应的 IMP ，如果没有 `forwardInvocation:` 对应的 IMP ，则报 `doesNotRecognizeSelector` 的错。最后判断是否需要 `remove` 当前的 hook 。

```objectivec
#define aspect_invoke(aspects, info) \
for (AspectIdentifier *aspect in aspects) {\
    [aspect invokeWithInfo:info];\
    if (aspect.options & AspectOptionAutomaticRemoval) { \
        aspectsToRemove = [aspectsToRemove?:@[] arrayByAddingObject:aspect]; \
    } \
}
```

为了使调用栈更清晰，这里的 `aspect_invoke` 采用宏定义的方式。

### invokeWithInfo:

看看 `AspectIdentifier` 的 `invokeWithInfo` 具体实现。

```objectivec
NSInvocation *blockInvocation = [NSInvocation invocationWithMethodSignature:self.blockSignature];
NSInvocation *originalInvocation = info.originalInvocation;
```

首先根据 `AspectIdentifier` 的 `blockSignature` 方法来获取 block 对应的 `blockInvocation` 。

```objectivec
NSUInteger numberOfArguments = self.blockSignature.numberOfArguments;

// Be extra paranoid. We already check that on hook registration.
if (numberOfArguments > originalInvocation.methodSignature.numberOfArguments) {
    AspectLogError(@“Block has too many arguments. Not calling %@“, info);
    return NO;
}
```

上面已经说过为了保持 `Aspects` 的灵活性， `block` 的参数数量是可以小于原有方法的参数数量的，这里只需要确认 `block` 参数数量是否不大于原有方法的参数数量。其实这里注释说了这是一种强迫症行为，之前已经检测过参数数量了。

```objectivec
// The `self` of the block will be the AspectInfo. Optional.
if (numberOfArguments > 1) {
    [blockInvocation setArgument:&info atIndex:1];
}
```

如果 `block` 有参数，则第一个参数必须为 `AspectInfo` 。

```objectivec
void *argBuf = NULL;
for (NSUInteger idx = 2; idx < numberOfArguments; idx++) {
    const char *type = [originalInvocation.methodSignature getArgumentTypeAtIndex:idx];
    NSUInteger argSize;
    NSGetSizeAndAlignment(type, &argSize, NULL);

    if (!(argBuf = reallocf(argBuf, argSize))) {
        AspectLogError(@“Failed to allocate memory for block invocation.”);
        return NO;
    }

    [originalInvocation getArgument:argBuf atIndex:idx];
    [blockInvocation setArgument:argBuf atIndex:idx];
}

[blockInvocation invokeWithTarget:self.block];
```

从 `originalInvocation` 获取原有方法的参数，然后设置给 `blockInvocation` ，最后通过 `[blockInvocation invokeWithTarget:self.block]` 调用 block 。

```objectivec
if (argBuf != NULL) {
    free(argBuf);
}
return YES;
```

释放 `argBuf` ，返回 YES 。

## 移除 hook

`Aspects` 支持在 hook 后移除的操作：

```objectivec
[aspectsToRemove makeObjectsPerformSelector:@selector(remove)];
```

移除的入口为 `AspectIdentifier` 的 `remove` 方法：

```objectivec
- (BOOL)remove {
    return aspect_remove(self, NULL);
}
```

### aspect_remove

```objectivec
static BOOL aspect_remove(AspectIdentifier *aspect, NSError **error) {
    NSCAssert([aspect isKindOfClass:AspectIdentifier.class], @“Must have correct type.”);

    __block BOOL success = NO;
    aspect_performLocked(^{
        id self = aspect.object; // strongify
        if (self) {
            // 获取对应的 container
            AspectsContainer *aspectContainer = aspect_getContainerForObject(self, aspect.selector);
            success = [aspectContainer removeAspect:aspect];
            aspect_cleanupHookedClassAndSelector(self, aspect.selector);
            // destroy token
            aspect.object = nil;
            aspect.block = nil;
            aspect.selector = NULL;
        }else {
            NSString *errrorDesc = [NSString stringWithFormat:@"Unable to deregister hook. Object already deallocated: %@", aspect];
            AspectError(AspectErrorRemoveObjectAlreadyDeallocated, errrorDesc);
        }
    });
    return success;
}
```

调用 `container` 的 `removeAspect:` 方法来从 container 中移除对应的 `Aspect` ：

```objectivec
- (BOOL)removeAspect:(id)aspect {
    for (NSString *aspectArrayName in @[NSStringFromSelector(@selector(beforeAspects)),
                                        NSStringFromSelector(@selector(insteadAspects)),
                                        NSStringFromSelector(@selector(afterAspects))]) {
        NSArray *array = [self valueForKey:aspectArrayName];
        NSUInteger index = [array indexOfObjectIdenticalTo:aspect];
        if (array && index != NSNotFound) {
            NSMutableArray *newArray = [NSMutableArray arrayWithArray:array];
            [newArray removeObjectAtIndex:index];
            [self setValue:newArray forKey:aspectArrayName];
            return YES;
        }
    }
    return NO;
}
```

从 `beforeAspects` ， `insteadAspects` 和 `afterAspects` 中排查是否包含有对应的 `aspect` ，如果有则移除，返回 YES ，否则返回 NO 。

### aspect_cleanupHookedClassAndSelector

从 container 移除 `aspect` 后，接下来要复原对 runtime 的处理：

```objectivec
Class klass = object_getClass(self);
BOOL isMetaClass = class_isMetaClass(klass);
if (isMetaClass) {
    klass = (Class)self;
}
```

首先需要根据是否为 metaClass 做下处理。

```objectivec
Method targetMethod = class_getInstanceMethod(klass, selector);
IMP targetMethodIMP = method_getImplementation(targetMethod);
if (aspect_isMsgForwardIMP(targetMethodIMP)) {
    // Restore the original method implementation.
    const char *typeEncoding = method_getTypeEncoding(targetMethod);
    SEL aliasSelector = aspect_aliasForSelector(selector);
    Method originalMethod = class_getInstanceMethod(klass, aliasSelector);
    IMP originalIMP = method_getImplementation(originalMethod);
    NSCAssert(originalMethod, @"Original implementation for %@ not found %@ on %@", NSStringFromSelector(selector), NSStringFromSelector(aliasSelector), klass);

    class_replaceMethod(klass, selector, originalIMP, typeEncoding);
    AspectLog(@"Aspects: Removed hook for -[%@ %@].", klass, NSStringFromSelector(selector));
}
```

如果我们已经成功 hook ，则原有的 selector 指向的 IMP 为 `_objc_msgForward` 的 IMP ，再获取 `aliasSelector` ， `aliasSelector` 指向的 IMP 为原有方法的 IMP ，通过 `class_replaceMethod` 将原有的 selector 指向原有的 IMP 。

### aspect_deregisterTrackedSelector

```objectivec
static void aspect_deregisterTrackedSelector(id self, SEL selector) {
    if (!class_isMetaClass(object_getClass(self))) return;

    NSMutableDictionary *swizzledClassesDict = aspect_getSwizzledClassesDict();
    NSString *selectorName = NSStringFromSelector(selector);
    Class currentClass = [self class];
    AspectTracker *subclassTracker = nil;
    do {
        AspectTracker *tracker = swizzledClassesDict[currentClass];
        if (subclassTracker) {
            [tracker removeSubclassTracker:subclassTracker hookingSelectorName:selectorName];
        } else {
            [tracker.selectorNames removeObject:selectorName];
        }
        if (tracker.selectorNames.count == 0 && tracker.selectorNamesToSubclassTrackers) {
            [swizzledClassesDict removeObjectForKey:currentClass];
        }
        subclassTracker = tracker;
    }while ((currentClass = class_getSuperclass(currentClass)));
}
```

从全局的 trackers 记录中清除对应的 selectorName ，同时向上递归，从父类中也移除响应的 selectorName ，如果 selectorNames 为空，则从全局的 trackers 记录中清除对应的 tracker 。

### 清除对应的 container

```objectivec
AspectsContainer *container = aspect_getContainerForObject(self, selector);
```

首先根据 selector 获取对应的 container ，判断 container 是否还包含有 `AspectIdentifier` ，如果没有，就销毁 container ，复原 `forwardInvocation:` 方法的 hook ：

```objectivec
if (!container.hasAspects) {
	 ……
}
```

### aspect_destroyContainerForObject

```objectivec
static void aspect_destroyContainerForObject(id<NSObject> self, SEL selector) {
    NSCParameterAssert(self);
    SEL aliasSelector = aspect_aliasForSelector(selector);
    objc_setAssociatedObject(self, aliasSelector, nil, OBJC_ASSOCIATION_RETAIN);
}
```

`aspect_destroyContainerForObject` 的实现很简单，根据对应的 selector 调用 `objc_setAssociatedObject` 方法把 container 设为 nil 即可。

### 对 Class 做处理

```objectivec
NSString *className = NSStringFromClass(klass);
if ([className hasSuffix:AspectsSubclassSuffix]) {
    Class originalClass = NSClassFromString([className stringByReplacingOccurrencesOfString:AspectsSubclassSuffix withString:@“”]);
    NSCAssert(originalClass != nil, @"Original class must exist”);
    object_setClass(self, originalClass);
    AspectLog(@“Aspects: %@ has been restored.”, NSStringFromClass(originalClass));

    // 我们只有在能确定没有实例对象使用我们动态生成的子类时才可以调用 objc_disposeClassPair 来释放掉生成的子类
    // 但是我们没有进行全局的记录，所以无法确认，即使保持生成的子类也不会造成太大的性能影响。
    //objc_disposeClassPair(object.class);
}else {
    // Class is most likely swizzled in place. Undo that.
    if (isMetaClass) {
        aspect_undoSwizzleClassInPlace((Class)self);
    }else if (self.class != klass) {
        aspect_undoSwizzleClassInPlace(klass);
    }
}
```

首先判断 className 是否有后缀，如果有，则表示是 KVO 生成的子类，只需要将 self 设置回原有的 `originalClass` 即可。

### aspect_undoSwizzleClassInPlace

```objectivec
static void aspect_undoSwizzleClassInPlace(Class klass) {
    NSCParameterAssert(klass);
    NSString *className = NSStringFromClass(klass);

    _aspect_modifySwizzledClasses(^(NSMutableSet *swizzledClasses) {
        if ([swizzledClasses containsObject:className]) {
            aspect_undoSwizzleForwardInvocation(klass);
            [swizzledClasses removeObject:className];
        }
    });
}
```

同样地，我们需要对 `forwardInvocation:` 方法做还原处理， `aspect_undoSwizzleClassInPlace` 只是通过全局的 `swizzledClasses` 来判断是否要进行还原，真正的还原操作还是通过 `aspect_undoSwizzleForwardInvocation` 来处理。

### aspect_undoSwizzleForwardInvocation

```objectivec
static void aspect_undoSwizzleForwardInvocation(Class klass) {
    NSCParameterAssert(klass);
    Method originalMethod = class_getInstanceMethod(klass, NSSelectorFromString(AspectsForwardInvocationSelectorName));
    Method objectMethod = class_getInstanceMethod(NSObject.class, @selector(forwardInvocation:));
    // 这里做多一层防御，如果 originalMethod 为空，就使用 NSObject 的 forwardInvocation: 代替
    IMP originalImplementation = method_getImplementation(originalMethod ?: objectMethod);
    class_replaceMethod(klass, @selector(forwardInvocation:), originalImplementation, "v@:@");

    AspectLog(@"Aspects: %@ has been restored.", NSStringFromClass(klass));
}
```

由于前面已经 hook 了 `forwardInvocation:` ，所以这里通过 `NSSelectorFromString(AspectsForwardInvocationSelectorName)` 获取的 `SEL` 是原有的 `SEL` ，将 `forwardInvocation:` 指向 `originalImplementation` 即可还原。

## 总结

`Aspects` 作为一个提供 AOP 功能的库，全部代码不到一千行，且非常简单易用，就我看来，它有以下优点：

### 入口简单

`Aspects` 的入口只有两个方法：

```objectivec
@interface NSObject (Aspects)
+ (id<AspectToken>)aspect_hookSelector:(SEL)selector
                           withOptions:(AspectOptions)options
                            usingBlock:(id)block
                                 error:(NSError **)error;
- (id<AspectToken>)aspect_hookSelector:(SEL)selector
                           withOptions:(AspectOptions)options
                            usingBlock:(id)block
                                 error:(NSError **)error;

@end
```

对使用者来说，使用成本非常低，只需要根据自己的需求调用对应的方法即可，不再需要关心其它设置，拿来即用。

### 灵活

`Aspects` 不仅支持 metaClass 的 hook ，也支持实例对象的 hook ，且 hook 之后还可以进行移除 ，同时，对 block 进行了处理，使得 block 的参数数量可以小于方法的参数数量，更提高了灵活性，基本可满足一些常见的需求。

### 健壮性

由于 `Aspects` 是通过 runtime 进行操作，可能会影响整个 app ，对健壮性要求较高， `Aspects` 对各种情况都做了预防性编程，有些地方还做了些强迫症的检测，包括原有 selector 是否存在，block 结构是否正常等。

当然，除非是只能采取 hook 方案的需求，否则还是不要使用比较好，另外就是必须要假设 hook 失效的情况下，app 也可以正常运行，毕竟苹果爸爸说不定哪天就改了内部 block 的实现。

但是 `Aspects` 也有缺点，由于是通过消息转发流程来处理，性能上不如传统的 Method Swizzling 方式，同时由于对 `forwardInvocation:` 做了替换，如果其它一些库也对 `forwardInvocation:` 做了类似的操作，就有可能导致一些奇奇怪怪的问题。

## 参考

[NSInvocation - Foundation | Apple Developer Documentation](https://developer.apple.com/documentation/foundation/nsinvocation)

[NSMethodSignature - Foundation

Apple Developer Documentation](https://developer.apple.com/documentation/foundation/nsmethodsignature)

[面向切面编程之 Aspects 源码解析及应用

WeRead团队博客](https://wereadteam.github.io/2016/06/30/Aspects/)
