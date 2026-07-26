---
title: iOS-+load和+initialize方法调用时机
source_url: 'https://www.cnblogs.com/junhuawang/p/14304756.html'
source_domain: cnblogs.com
source_group: platform
original_language: zh
published: ''
archived_at: 2026-07-27
content_hash: 'sha256:d9092c07137b4f41'
plan_ref: 第三周：Runtime 行为与 Cocoa 对象通信 / Day 4｜用加载时机把 Category、load、initialize 串起来（对应 W5-07）
plan_week: 第三周：Runtime 行为与 Cocoa 对象通信
plan_day: Day 4｜用加载时机把 Category、load、initialize 串起来（对应 W5-07）
container: '//div[@id=''cnblogs_post_body'']'
container_source: map
---

> 原文：[iOS-+load和+initialize方法调用时机](https://www.cnblogs.com/junhuawang/p/14304756.html)

> Objective-C 有两个神奇的方法：+load 和 +initialize，这两个方法在类被使用时会自动调用。但是两个方法的不同点会导致应用层面上性能的显著差异。

### 一、+ initialize 方法和+load 调用时机

先来看一个表

| 方法 | +(void)load | +(void)initialize |
|---|---|---|
| 执行时机 | 在程序运行后立即执行 | 在类的方法第一次被调时执行 |
| 若自身未定义，是否沿用父类的方法？ | 否 (这是**由于+load方法是根据方法地址直接调用， 并不是经过objc_msgSend函数调用**。下面有解释) | 是 |
| 分类中的定义 | 全都执行，但后于类中的方法 覆盖类中的方法， | 只执行一个 |
| 执行次数（非主动调用的情况下） | 必然一次 | 0、1、多 次（调用者会不同） |

先看[官方解释](https://links.jianshu.com/go?to=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Fobjectivec%2Fnsobject%3Flanguage%3Dobjc)：

1. 首先说一下 + initialize 方法：苹果官方对这个方法有这样的一段描述：这个方法会在 **_第一次初始化这个类之前_** 被调用，我们用它来初始化静态变量。
2. load 方法会在加载类的时候就被调用，也就是 ios 应用启动的时候，就会加载所有的类，就会调用每个类的 + load 方法。
3. 之后我们结合代码来探究一下 + initialize 与 + load 两个方法的调用时机，首先是 **_+ load_**：

```
#pragram ---main函数中的代码---
#import <UIKit/UIKit.h>
#import "AppDelegate.h"
int main(int argc, char * argv[]) {
    NSLog(@"%s",__func__);
    @autoreleasepool {
        return UIApplicationMain(argc, argv, nil, NSStringFromClass([AppDelegate class]));
    }
}
#pragram ---基于NSObject的Person类---
#import "Person.h"
@implementation Person
 + (void)load{
    NSLog(@"%s",__func__);
}
 + (void)initialize{
    [super initialize];
    NSLog(@"%s %@",__func__,[self class]);
}
 - (instancetype)init{
    if (self = [super init]) {
        NSLog(@"%s",__func__);
    }
    return self;
}
@end
#pragram ---基于Person的Son类---
#import "Girl.h"
@implementation Girl
 + (void)load{
    NSLog(@"%s ",__func__);
}
 + (void)initialize{
    [super initialize];
    NSLog(@"%s ",__func__);
}
 - (instancetype)init{
    if (self = [super init]) {
        NSLog(@"%s",__func__);
    }
    return self;
}
@end
```

运行程序，我们看一下输出日志：

```css
2015-10-27 15:21:07.545 initialize[11637:334237] +[Person load]
2015-10-27 15:21:07.546 initialize[11637:334237] +[Girl load] 
2015-10-27 15:21:07.546 initialize[11637:334237] main
```

这说明在我并没有对类做任何操作的情况下，**+load 方法会被默认执行，并且是在 main 函数之前执行的**。

### 二、接下来我们来查看一下 **_+ initialize_** 方法，先在 ViewController 中创建 Person 和 Girl 对象：

```
#import "ViewController.h"
#import "Person.h"
#import "Son.h"
#import "Girl.h"
@interface ViewController ()
@end
@implementation ViewController
 - (void)viewDidLoad {
    [super viewDidLoad];
    Person * a = [Person new];
    Person * b = [Person new];
    Girl *c = [Girl new];
    Girl *d = [Girl new];
}
@end
```

下面我们来看一下输出日志：

```css
2015-10-27 15:33:56.195 initialize[11711:342410] +[Person load]
2015-10-27 15:33:56.196 initialize[11711:342410] +[Girl load] 
2015-10-27 15:33:56.197 initialize[11711:342410] main
2015-10-27 15:33:56.259 initialize[11711:342410] +[Person initialize] Person
2015-10-27 15:33:56.259 initialize[11711:342410] -[Person init]
2015-10-27 15:33:56.259 initialize[11711:342410] -[Person init]
2015-10-27 15:33:56.259 initialize[11711:342410] +[Girl initialize] 
2015-10-27 15:33:56.260 initialize[11711:342410] -[Girl init]
2015-10-27 15:33:56.260 initialize[11711:342410] -[Girl init]
```

通过这个实验我们可以确定两点：  
 - **+ initialize** 方法类似一个懒加载，如果没有使用这个类，那么系统默认不会去调用这个方法，且默认只加载一次；  
 - **+ initialize** 的调用发生在 +init 方法之前。

### 三、接下来再探究一下 **_+ initialize_** 在父类与子类之间的关系，创建一个继承自 Person 类的 Son类：

```
#pragram ---ViewController 中的代码---
#import "ViewController.h"
#import "Person.h"
#import "Son.h"
#import "Girl.h"
@interface ViewController ()
@end
@implementation ViewController
 - (void)viewDidLoad {
    [super viewDidLoad];
    Person * a = [Person new];
    Person * b = [Person new];
    Son*z = [Son new];
}
@end
```

看一下输出日志：

```css
2015-10-27 15:44:55.762 initialize[12024:351576] +[Person load]
2015-10-27 15:44:55.764 initialize[12024:351576] +[Son load]
2015-10-27 15:44:55.764 initialize[12024:351576] +[Girl load] 
2015-10-27 15:44:55.764 initialize[12024:351576] main
2015-10-27 15:44:55.825 initialize[12024:351576] +[Person initialize] Person
2015-10-27 15:44:55.825 initialize[12024:351576] -[Person init]
2015-10-27 15:44:55.825 initialize[12024:351576] -[Person init]
2015-10-27 15:44:55.826 initialize[12024:351576] +[Person initialize] Son
2015-10-27 15:44:55.826 initialize[12024:351576] -[Person init]
```

**我们会发现 Person 类的 _+ initialize_ 方法又被调用了，但是查看一下是子类 Son 调用的，也就是创建子类的时候，子类会去调用父类的 _+ initialize_ 方法。**

### 四、总结

- 如果你实现了 **_+ load_** 方法，那么当类被加载时它会自动被调用。这个调用非常早。  
  如果你实现了一个应用或框架的 **_+ load_**，并且你的应用链接到这个框架上了，那么 **_＋ load_** 会在 main() 函数之前被调用。  
  如果你在一个可加载的 bundle 中实现了 **_+ load_**，那么它会在 bundle 加载的过程中被调用。比如方法交换等
- **_+ initialize_** 方法的调用看起来会更合理，通常在它里面写代码比在 **_+ load_** 里写更好。  
  **_+ initialize_** 很有趣，因为它是懒调用的，也有可能完全不被调用。类第一次被加载时，

### 五、其他内部实现原理补充

### 一、+load 调用时机和顺序原理解析

load 方法在什么时候调用？  
 官方解释是：运行时，添加类或者分类的时候调用。实现此方法以在加载时执行特定于类的行为。

`+load`方法是一定会在runtime中被调用的，只要类被添加到runtime中了，就会调用`+load`方法，即**只要是在`Compile Sources`中出现的文件总是会被装载，与这个类是否被用到无关，因此`+load`方法总是在main函数之前调用**。所以我们可以自己实现`+laod`方法来在这个时候执行一些行为。

**换句话说，load是在app启动的时候加载并在**main函数之前调用****，从源码中找

```
_objc_init —>
_dyld_objc_notify_register(&map_images, load_images, unmap_image);
```

这里面的2个方法 map_images 和 load_images, map_images的作用就是加载所有的类/协议/分类，加载完成之后，就开始调用load_images，在这个方法里面看：

```
load_images(const char *path __unused, const struct mach_header *mh)
{
    ......
    {
        mutex_locker_t lock2(runtimeLock);
        prepare_load_methods((const headerType *)mh);    // 把所有需要load的类 加载一个list里面
    }
    call_load_methods();    // 调用load方法
}

void call_load_methods(void)
{
   ......
    do {
        while (loadable_classes_used > 0) {
            call_class_loads();                     // 先加载类的load 
        }
        more_categories = call_category_loads();    // 在加载category的load

    } while (loadable_classes_used > 0  ||  more_categories);   
   ......
}
```

另外有意思的一点是：

**`+load`方法不会覆盖**（因为**由于+load方法是根据方法地址直接调用，****并不是经过objc_msgSend函数调用**）。  
也就是说，如果子类实现了`+load`方法，那么会先调用父类的`+load`方法，然后又去执行子类的`+load`方法。  
但要注意的时+load方法只会调用一次。而且执行顺序是：类 -\>父类-\> 子类 -\>分类。而不同类之间的顺序不一定。

> 但是这里依然有一个疑问，官方解释没有说清楚，1、分类的加载顺序是怎样的？  
>  其实在源码中有可以看到：

```
void prepare_load_methods(const headerType *mhdr)
{
......
    classref_t *classlist = 
        _getObjc2NonlazyClassList(mhdr, &count);    // 1、按照编译顺序加载所有的类(不包括分类)
    for (i = 0; i < count; i++) {
        schedule_class_load(remapClass(classlist[i]));  // 2、在这里  按照先父类 在子类的方式加入列表
    }

    category_t **categorylist = _getObjc2NonlazyCategoryList(mhdr, &count);  // 分类也是类似的方式
    for (i = 0; i < count; i++) {
       ......
        add_category_to_loadable_list(cat);
    }
}

static void schedule_class_load(Class cls)
{
  .......
    schedule_class_load(cls->superclass);    //递归加载，先加载父类

    add_class_to_loadable_list(cls);
}
```

_由以上代码中 1、2备注，得出 ：_

_1、先加载类的load：类的加载是按照编译顺序，同时遵循先父类再子类的方式  
 2、再加载分类的load：分类直接按照编译顺序，和其绑定类的继承没有关系_

### 总结

1、先加载类的load  
 2、再加载分类的load  
 3、不同的类之间加载load顺序为：有继承关系的，先加载父类load、再加载子类的load，无继承关系的，按照编译顺序  
 ----比如顺序二 Student、OtherClass、Person，先加载Student的load，由于Person是Student的父类，所以Person的顺序比OtherClass早  
 4、分类的加载顺序是完全按照编译顺序，也就是谁在前面，谁先加载。和其绑定类的继承关系无关  
 ----比如顺序二中，Student继承Person，但是其分类的顺序是 Student+JE2、Student+JE1、Person+JE，顺序是什么样，加载load就是什么样。  
 5、即使有类的源文件，但是编译列表中没有，那么这个类就不会被编译，也就不会执行其load方法

### 2、+initialize

initialize方法在什么时候调用？  
 官方解释是：在类收到第一条消息之前初始化它。  
 换句话说，就是第一次用到它之前调用，比如初始化一个对象（其父类也会调用initialize）、调用类方法等。 从源码中找：

- 说明：没有发送消息的类不会调用initialize
- 如果主类有相应的分类（或多个分类），会调用分类中的initialize方法，具体调用的是哪个分类的方法，由编译顺序决定。
- 当子类没有重写initialize方法，这个时候回去执行父类的initialize方法

```
class_initialize -> initializeNonMetaClass()
void initializeNonMetaClass(Class cls)
{
    .......
    // Make sure super is done initializing BEFORE beginning to initialize cls.
    // See note about deadlock above.
    supercls = cls->superclass;
    if (supercls  &&  !supercls->isInitialized()) {
        initializeNonMetaClass(supercls);        // 递归加载父类的initialize
    }
    ........
}
```

`+initialize`方法是在**类或它的子类收到第一条消息之前被调用的**，这里所指的消息包括实例方法和类方法的调用，并且只会调用一次。  
`+initialize`方法实际上是一种惰性调用，也就是说如果一个类一直没被用到，那它的`+initialize`方法也不会被调用，这一点有利于节约资源。

与`+load`方法不同，却更符合我们预期的就是，`+initialize`方法会覆盖是因为调用的objc_msgSend。  
也就是说如果子类实现了`+initialize`方法，就不会执行父类的了，直接执行子类本身的。  
如果分类实现了`+initialize`方法，也不会再执行主类的。  
所以`+initialize`方法的执行覆盖顺序是：分类 -\> 子类 -\>类。且只会有一个`+initialize`方法被执行。

### 总结

1、initialize的执行顺序为先父类、在子类  
 2、分类的initialize方法会覆盖主类的方法（假覆盖，方法都在，只是没有执行）  
 3、只有在这个类有发送消息的时候才会执行initialize，比如初始化对象、调用类方法等。  
 4、多个分类的情况，只执行一次，具体执行哪个分类的initialize，有编译顺序决定（Build Phases -\> Compile Sources 中的顺序）  
 5、如果子类没有重写initialize，那么会调用其父类的initialize方法

### 3、两者的异同

#### 1、相同点

1).load和initialize会被自动调用，不能手动调用它们。  
 2).子类实现了load和initialize的话，会隐式调用父类的load和initialize方法。  
 3).load和initialize方法内部使用了锁，因此它们是线程安全的。

#### 2、不同点

1).调用顺序不同，

1. 以main函数为分界，`+load`方法在main函数之前执行，
2. `+initialize`在main函数之后执行。

2).若自身未定义，是否沿用父类的方法：

1. 子类中没有实现`+load`方法的话，不会调用父类的`+load`方法；（不会）
2. 而子类如果没有实现`+initialize`方法的话，也会自动调用父类的`+initialize`方法。（会）

3).调用时机：

1. `+load`方法是在类被装载进来的时候就会调用，
2. `+initialize`在第一次给某个类发送消息时调用（比如实例化一个对象），并且只会调用一次，是懒加载模式，如果这个类一直没有使用，就不回调用到`+initialize`方法。

4).调用方式：

1. _load是根据函数地址直接调用_
2. _initialize是通过objc_msgSend调用_

### 4、使用场景

1.`+load`一般是用来交换方法`Method Swizzle`，由于它是线程安全的，而且一定会调用且只会调用一次，通常在使用UrlRouter的时候注册类的时候也在`+load`方法中注册。  
 2.`+initialize`方法主要用来对一些不方便在编译期初始化的对象进行赋值，或者说对一些静态常量进行初始化操作。

### 5、为什么原本类的+load方法不会被分类的+load方法覆盖呢？

这是**由于+load方法是根据方法地址直接调用，并不是经过objc_msgSend函数调用**。

+load方法相关源码阅读顺序：

1. _objc_init
2. load_images
3. prepare_load_methods

    - schedule_class_load
    - add_class_to_loadable_list
    - add_category_to_loadable_list
4. calls

    - call_class_loads
    - call_category_loads
    - (*load_method)(cls, SEL_load)

### 3、+initialize方法调用的时机

+initialize方法会在类**第一次接收到消息时调用**。

调用顺序：先调用父类的+initialize，再调用子类的+initialize，每个类只会初始化1次

+initialize方法相关源码阅读顺序：

1. objc-msg-arm64.s

    - objc_msgSend
2. objc-runtime-new.mm

    - class_getInstanceMethod
    - lookUpImpOrNil
    - lookUpImpOrForward
    - _class_initialize
    - callInitialize
    - objc_msgSend(cls, SEL_initialize)

+initialize和+load的最大区别是，+initialize是通过objc_msgSend进行调用的，所以有以下特点：

- 如果子类没有实现+initialize，会调用父类的+initialize（所以父类的+initialize可能会被调用多次）
- 如果分类实现了+initialize，就覆盖类本身的+initialize调用
