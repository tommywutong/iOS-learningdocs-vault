---
title: 6种iOS开发中常用的设计模式
source_url: 'https://blog.csdn.net/weixin_38633659/article/details/149066468'
source_domain: blog.csdn.net
source_group: platform
original_language: zh
published: ''
archived_at: 2026-07-27
content_hash: 'sha256:315c6520b751eec6'
plan_ref: 第三周：Runtime 行为与 Cocoa 对象通信 / Day 6｜最后才比较对象通信模式（对应 W3-01、W6-07）
plan_week: 第三周：Runtime 行为与 Cocoa 对象通信
plan_day: Day 6｜最后才比较对象通信模式（对应 W3-01、W6-07）
container: '//div[@id=''content_views'']'
container_source: map
---

> 原文：[6种iOS开发中常用的设计模式](https://blog.csdn.net/weixin_38633659/article/details/149066468)

我们讨论的六种设计模式都是iOS开发中常用的模式。下面我将分别解释每种模式的概念、使用场景以及在Objective-C中的实现方式。

#### 1. 单例模式（Singleton Pattern）

**意图**：确保一个类只有一个实例，并提供一个全局访问点。  
 **使用场景**：需要频繁使用且资源消耗大的对象，或者需要全局唯一状态的场景（如配置管理、日志记录、网络管理器等）。  
 **Objective-C实现**：

```objectivec
// .h文件
@interface MySingleton : NSObject
+ (instancetype)sharedInstance;
@end
// .m文件
@implementation MySingleton
+ (instancetype)sharedInstance {
    static MySingleton *instance = nil;
    static dispatch_once_t onceToken;
    dispatch_once(&onceToken, ^{
        instance = [[MySingleton alloc] init];
    });
    return instance;
}
@end
```

**注意**：使用`dispatch_once`保证线程安全，且防止多次创建。

#### 2. 委托模式（Delegate Pattern）

**意图**：允许一个对象（委托方）将某些任务交给另一个对象（委托对象）处理。这是一种对象间通信的模式。  
 **使用场景**：常见于UIKit框架（如UITableViewDelegate，UITextFieldDelegate），用于事件回调或数据请求。  
 **实现步骤**：

1. 定义委托协议（Protocol）。
2. 在委托方中声明一个弱引用（weak）的delegate属性。
3. 在需要时向delegate发送消息。
4. 委托对象实现协议方法。  
  **示例**：

```objectivec
// 定义协议
@protocol TaskDelegate <NSObject>
- (void)taskDidComplete;
@end
// 委托方
@interface TaskHandler : NSObject
@property (nonatomic, weak) id<TaskDelegate> delegate;
- (void)startTask;
@end
@implementation TaskHandler
- (void)startTask {
    // 任务完成后回调
    [self.delegate taskDidComplete];
}
@end
// 委托对象
@interface ViewController : UIViewController <TaskDelegate>
@end
@implementation ViewController
- (void)viewDidLoad {
    [super viewDidLoad];
    TaskHandler *handler = [[TaskHandler alloc] init];
    handler.delegate = self;
}
- (void)taskDidComplete {
    NSLog(@"Task completed!");
}
@end
```

#### 3. 观察者模式（Observer Pattern）

**意图**：定义对象间的一种一对多的依赖关系，当一个对象状态改变时，所有依赖它的对象都得到通知并自动更新。  
 **使用场景**：数据模型与视图之间的同步，跨模块状态通知。  
 **Objective-C实现方式**：

- **KVO (Key-Value Observing)**: 内建于NSObject，用于监听属性变化。
- **NSNotificationCenter**: 广播机制，任意对象可以发送通知，多个观察者可以监听。  
  **KVO示例**：

```objectivec
// 被观察对象
@interface ObservedObject : NSObject
@property (nonatomic, strong) NSString *name;
@end
// 观察者
[self.observedObject addObserver:self 
                      forKeyPath:@"name" 
                         options:NSKeyValueObservingOptionNew 
                         context:nil];
// 实现回调
- (void)observeValueForKeyPath:(NSString *)keyPath 
                      ofObject:(id)object 
                        change:(NSDictionary<NSKeyValueChangeKey,id> *)change 
                       context:(void *)context {
    if ([keyPath isEqualToString:@"name"]) {
        NSLog(@"Name changed to: %@", change[NSKeyValueChangeNewKey]);
    }
}
// 移除观察者（在dealloc中）
- (void)dealloc {
    [self.observedObject removeObserver:self forKeyPath:@"name"];
}
```

**NSNotificationCenter示例**：

```objectivec
// 发送通知
[[NSNotificationCenter defaultCenter] postNotificationName:@"DataUpdated" object:nil];
// 监听通知
[[NSNotificationCenter defaultCenter] addObserver:self 
                                        selector:@selector(handleDataUpdated:) 
                                            name:@"DataUpdated" 
                                          object:nil];
// 处理通知
- (void)handleDataUpdated:(NSNotification *)notification {
    // 更新UI或数据
}
// 移除监听（在dealloc中）
- (void)dealloc {
    [[NSNotificationCenter defaultCenter] removeObserver:self];
}
```

#### 4. 工厂方法模式（Factory Method Pattern）

**意图**：定义一个创建对象的接口，但让子类决定实例化哪一个类。工厂方法使得一个类的实例化延迟到其子类。  
 **使用场景**：需要创建一系列相关或依赖对象，但不想指定具体类时。  
 **Objective-C实现**：

```objectivec
// 抽象产品
@interface Product : NSObject
@end
// 具体产品A
@interface ProductA : Product
@end
// 具体产品B
@interface ProductB : Product
@end
// 工厂基类
@interface Factory : NSObject
+ (Product *)createProduct;
@end
@implementation Factory
+ (Product *)createProduct {
    // 默认实现，或者抛出异常（因为子类必须重写）
    [NSException raise:@"Abstract Method" format:@"Subclasses must override"];
    return nil;
}
@end
// 具体工厂A
@interface FactoryA : Factory
@end
@implementation FactoryA
+ (Product *)createProduct {
    return [[ProductA alloc] init];
}
@end
// 具体工厂B
@interface FactoryB : Factory
@end
@implementation FactoryB
+ (Product *)createProduct {
    return [[ProductB alloc] init];
}
@end
// 使用
Product *productA = [FactoryA createProduct];
Product *productB = [FactoryB createProduct];
```

#### 5. 策略模式（Strategy Pattern）

**意图**：定义一系列算法，将每个算法封装起来，并使它们可以互相替换。策略模式让算法独立于使用它的客户端而变化。  
 **使用场景**：需要动态切换算法或行为（如排序算法、支付方式）。  
 **Objective-C实现**：

```objectivec
// 策略接口
@protocol PaymentStrategy <NSObject>
- (void)payAmount:(NSInteger)amount;
@end
// 具体策略：信用卡支付
@interface CreditCardPayment : NSObject <PaymentStrategy>
@end
@implementation CreditCardPayment
- (void)payAmount:(NSInteger)amount {
    NSLog(@"Paid %ld via Credit Card", amount);
}
@end
// 具体策略：支付宝支付
@interface AlipayPayment : NSObject <PaymentStrategy>
@end
@implementation AlipayPayment
- (void)payAmount:(NSInteger)amount {
    NSLog(@"Paid %ld via Alipay", amount);
}
@end
// 上下文（使用策略）
@interface PaymentContext : NSObject
@property (nonatomic, strong) id<PaymentStrategy> strategy;
- (void)executePayment:(NSInteger)amount;
@end
@implementation PaymentContext
- (void)executePayment:(NSInteger)amount {
    [self.strategy payAmount:amount];
}
@end
// 使用
PaymentContext *context = [[PaymentContext alloc] init];
context.strategy = [[CreditCardPayment alloc] init];
[context executePayment:100]; // 使用信用卡支付
context.strategy = [[AlipayPayment alloc] init];
[context executePayment:200]; // 使用支付宝支付
```

#### 6. 组合模式（Composite Pattern）

**意图**：将对象组合成树形结构以表示“部分-整体”的层次结构。组合模式使得用户对单个对象和组合对象的使用具有一致性。  
 **使用场景**：表示树形结构（如UIView层次、菜单树）。  
 **Objective-C实现**：

```objectivec
// 组件接口
@protocol Component <NSObject>
- (void)operation;
@end
// 叶子节点（无子节点）
@interface Leaf : NSObject <Component>
@end
@implementation Leaf
- (void)operation {
    NSLog(@"Leaf operation");
}
@end
// 复合节点（可包含子节点）
@interface Composite : NSObject <Component>
@property (nonatomic, strong) NSMutableArray<id<Component>> *children;
- (void)addComponent:(id<Component>)component;
- (void)removeComponent:(id<Component>)component;
@end
@implementation Composite
- (instancetype)init {
    if (self = [super init]) {
        _children = [NSMutableArray array];
    }
    return self;
}
- (void)addComponent:(id<Component>)component {
    [self.children addObject:component];
}
- (void)removeComponent:(id<Component>)component {
    [self.children removeObject:component];
}
- (void)operation {
    // 先执行自身操作
    NSLog(@"Composite operation");
    // 再执行所有子节点的操作
    for (id<Component> child in self.children) {
        [child operation];
    }
}
@end
// 使用
Composite *root = [[Composite alloc] init];
Composite *branch1 = [[Composite alloc] init];
Leaf *leaf1 = [[Leaf alloc] init];
Leaf *leaf2 = [[Leaf alloc] init];
[root addComponent:branch1];
[root addComponent:leaf1];
[branch1 addComponent:leaf2];
[root operation]; // 递归调用所有节点的operation方法
```

#### 总结

- **单例模式**：全局唯一实例。
- **委托模式**：对象间通信（一对一）。
- **观察者模式**：一对多的状态通知（KVO/Notification）。
- **工厂方法模式**：由子类决定创建的对象。
- **策略模式**：动态切换算法。
- **组合模式**：树形结构的部分-整体处理。  
   在iOS开发中，这些模式被广泛应用，理解它们有助于构建可维护、可扩展的代码结构。
