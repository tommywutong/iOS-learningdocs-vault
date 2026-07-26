---
title: KVC实现原理
source_url: 'https://www.neroxie.com/2019/07/12/KVC%E5%AE%9E%E7%8E%B0%E5%8E%9F%E7%90%86/'
source_domain: neroxie.com
source_group: single-site
original_language: zh
published: 2019-07-12
archived_at: 2026-07-27
content_hash: 'sha256:26e97d6079e93927'
plan_ref: 第三周：Runtime 行为与 Cocoa 对象通信 / Day 5｜KVC 提供间接访问，KVO 在它的约定上插入通知（对应 W3-09）
plan_week: 第三周：Runtime 行为与 Cocoa 对象通信
plan_day: Day 5｜KVC 提供间接访问，KVO 在它的约定上插入通知（对应 W3-09）
container: '//*[contains(@class,''post-body'')]'
container_source: guess
---

> 原文：[KVC实现原理](https://www.neroxie.com/2019/07/12/KVC%E5%AE%9E%E7%8E%B0%E5%8E%9F%E7%90%86/)

`KVC`全称是`Key Value Coding`，定义在`NSKeyValueCoding.h`文件中。`KVC`提供了一种间接访问其属性方法或成员变量的机制，可以通过字符串来访问对应的属性方法或成员变量。关于KVC的实现主要依赖于其搜索规则。

## 搜索规则

在赋值过程中，我们会使用`- (void)setValue:(id)value forKey:(NSString *)key`或者`(void)setValue:(id)value forKeyPath:(NSString *)keyPath;`进行KVC的赋值操作。在取值过程中，我们会使用`- (id)valueForKey:(NSString *)key;`或者`- (id)valueForKeyPath:(NSString *)keyPath;`。

KVC在通过`key`或者`keyPath`进行操作的时候，可以查找属性方法、成员变量等，查找的时候可以兼容多种命名。具体的查找规则在[KVC官方文档](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/SearchImplementation.html#//apple_ref/doc/uid/20000955-CJBBBFFA)中可以找到。

KVC的实现主要依赖于`setter`和`getter`方法，所以关于命名需要符合苹果的规范。另外在搜索过程中`accessInstanceVariablesDirectly`这个只读属性也起着重要的作用。这个属性表示是否允许读取实例变量的值，如果为YES则在KVC查找的过程中，从内存中读取属性实例变量的值，默认为YES。

### 赋值原理

以`setValue:forKey:`为例，其内部实现主要有以下步骤：

1. 以`set<Key>:`、`_set<Key>`的顺序查找对应命名的`setter`方法，如果找到的话，调用这个方法并将值传进去(根据需要进行对象转换)；
2. 如果没有发现`setter`方法，但是`accessInstanceVariablesDirectly`类属性返回YES，则按`_<key>`、`_is<Key>`、`<key>`、`is<Key>`的顺序查找一个对应的实例变量。如果发现则将value赋值给实例变量；
3. 如果没有发现`setter`方法或实例变量，则调用`setValue:forUndefinedKey:`方法，默认抛出一个异常，但是一个NSObject的子类可以提出合适的行为。

接着我们用代码进行相关的测试：

**实验1：验证setter方法**

```plain
// model1
@interface KVCTestModel1 : NSObject

@end

@implementation KVCTestModel1

- (void)setName:(NSString *)name {
    NSLog(@"%s", __func__);
}

- (void)_setName:(NSString *)name {
    NSLog(@"%s", __func__);
}

@end

// model2
@interface KVCTestModel2 : NSObject

@end

@implementation KVCTestModel2

- (void)_setName:(NSString *)name {
    NSLog(@"%s", __func__);
}

@end

// model3
@interface KVCTestModel3 : NSObject

@end

@implementation KVCTestModel3

@end

// 调用
- (void)_testKVC {
    KVCTestModel1 *model1 = [[KVCTestModel1 alloc] init];
    [model1 setValue:@"Nero" forKey:@"name"];

    KVCTestModel2 *model2 = [[KVCTestModel2 alloc] init];
    [model2 setValue:@"Nero" forKey:@"name"];

    KVCTestModel3 *model3 = [[KVCTestModel3 alloc] init];
    [model3 setValue:@"Nero" forKey:@"name"];
}
```

执行结果如下：  
![kvc_setter1](https://neroblog.oss-cn-hangzhou.aliyuncs.com/kvc_setter1.jpg)

**实验2：验证实例变量**

```plain
// model1
@interface KVCTestModel1 : NSObject {
    NSString *_name;
    NSString *_isName;
    NSString *name;
    NSString *isName;
}

@end

// model2
@interface KVCTestModel2 : NSObject {
    NSString *_isName;
    NSString *name;
    NSString *isName;
}

@end

// model3
@interface KVCTestModel3 : NSObject {
    NSString *name;
    NSString *isName;
}

@end

// model4
@interface KVCTestModel4 : NSObject {
    NSString *isName;
}

@end

// 调用
- (void)_testKVC {
    self.kvcTestModel1 = [[KVCTestModel1 alloc] init];
    [self.kvcTestModel1 setValue:@"Nero" forKey:@"name"];

    self.kvcTestModel2 = [[KVCTestModel2 alloc] init];
    [self.kvcTestModel2 setValue:@"Nero" forKey:@"name"];

    self.kvcTestModel3 = [[KVCTestModel3 alloc] init];
    [self.kvcTestModel3 setValue:@"Nero" forKey:@"name"];

    self.kvcTestModel4 = [[KVCTestModel4 alloc] init];
    [self.kvcTestModel4 setValue:@"Nero" forKey:@"name"];
}
```

执行结果如下：  
![kvc_setter2](https://neroblog.oss-cn-hangzhou.aliyuncs.com/kvc_setter2.jpg)

另外如果设置`accessInstanceVariablesDirectly`返回为NO，即使有符合命名规范的实例变量名，KVC也无法赋值成功；`setValue:forUndefinedKey:`默认会抛出一个异常，你可以用重写这个方法用来拦截。

赋值原理流程图如下：  
![kvc_setter_process.jpg](https://neroblog.oss-cn-hangzhou.aliyuncs.com/kvc_setter_process.jpg)

### 取值原理

以`valueForKey:`为例，其内部实现主要有以下几步：

1. 通过`getter`方法搜索实例，以`get<Key>`, `<key>`, `is<Key>`, `_<key>`的顺序搜索符合规则的方法，如果有，就调用对应的方法；
2. 如果没有发现简单`getter方法`，并且在类方法`accessInstanceVariablesDirectly`是返回YES的的情况下搜索一个名为`_<key>`、`_is<Key>`、`<key>`、`is<Key>`的实例；
3. 如果返回值是一个对象指针，则直接返回这个结果；如果返回值是一个基础数据类型，但是这个基础数据类型是被`NSNumber`支持的，则存储为`NSNumber`并返回；如果返回值是一个不支持`NSNumber`的基础数据类型，则通过`NSValue`进行存储并返回；
4. 在上述情况都失败的情况下调用`valueForUndefinedKey:`方法，默认抛出异常，但是子类可以重写此方法。

由于和前面的赋值原理实验相似，这里就不添加相关的验证代码了。另外`valueForKey:`返回的结果还可能是数组或者其他集合类型，所以在上面第1步和第2步之间还有一些其他的规则，这些规则用来判断是否是数组或者其他集合类型的规则，但是我觉得忽略这些规则跟整体流程理解冲突不大，所以就忽略掉了（具体的在官在[KVC官方文档](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/SearchImplementation.html#//apple_ref/doc/uid/20000955-CJBBBFFA)中可以找到。）。

## 补充：

**面试题分析: KVC能否能够触发KVO**

答案是肯定的。

测试代码如下：

```plain
@interface KVCTestModel1 : NSObject {
    @public
    NSString *_name;
}

@end

@implementation KVCTestModel1

@end

// 测试代码
KVCTestModel1 *model1 = [[KVCTestModel1 alloc] init];
[model1 addObserver:self forKeyPath:@"name" options:NSKeyValueObservingOptionNew context:nil];

// 直接修改成员变量
model1 -> _name = @"Nero1";
NSLog(@"%@", [model1 valueForKey:@"name"]);

// 手动触发KVO
[model1 willChangeValueForKey:@"name"];
model1 -> _name = @"Nero2";
[model1 didChangeValueForKey:@"name"];
NSLog(@"%@", [model1 valueForKey:@"name"]);

// KVC赋值
[model1 setValue:@"Nero3" forKeyPath:@"name"];
NSLog(@"%@", [model1 valueForKey:@"name"]);

[model1 removeObserver:self forKeyPath:@"name"];
```

打印结果：  
![](https://neroblog.oss-cn-hangzhou.aliyuncs.com/KVC%26KVO.jpg)

通过上面的代码我们可以认为，在以KVC的方式对变量进行赋值的时候，会判断该对象是否使用了KVO，如果是，则会触发KVO。
