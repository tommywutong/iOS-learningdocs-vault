---
title: 美团外卖iOS App冷启动治理
source_url: 'https://tech.meituan.com/2018/12/06/waimai-ios-optimizing-startup.html'
source_domain: tech.meituan.com
source_group: single-site
original_language: zh
published: 2018-12-06
archived_at: 2026-07-27
content_hash: 'sha256:16c9169a16bf9278'
plan_ref: 第七周：编译、链接、Mach-O、dyld 与 App 启动 / Day 5｜把 Runtime 初始化放进 App 冷启动（对应 W6-08）
plan_week: 第七周：编译、链接、Mach-O、dyld 与 App 启动
plan_day: Day 5｜把 Runtime 初始化放进 App 冷启动（对应 W6-08）
container: //main
container_source: guess
---

> 原文：[美团外卖iOS App冷启动治理](https://tech.meituan.com/2018/12/06/waimai-ios-optimizing-startup.html)

![美团外卖iOS App冷启动治理](https://p0.meituan.net/meituantechblog/6082682d9f0e31d5f0a632118a922e3d362833.jpg)

# 美团外卖iOS App冷启动治理

郭赛 徐宏 2018-12-06

前端iOS移动端性能优化

## [一、背景](#一、背景)

冷启动时长是App性能的重要指标，作为用户体验的第一道“门”，直接决定着用户对App的第一印象。美团外卖iOS客户端从2013年11月开始，历经几十个版本的迭代开发，产品形态不断完善，业务功能日趋复杂；同时外卖App也已经由原来的独立业务App演进成为一个平台App，陆续接入了闪购、跑腿等其他新业务。因此，更多更复杂的工作需要在App冷启动的时候被完成，这给App的冷启动性能带来了挑战。对此，我们团队基于业务形态的变化和外卖App的特点，对冷启动进行了持续且有针对性的优化工作，目的就是为了呈现更加流畅的用户体验。

## [二、冷启动定义](#二、冷启动定义)

一般而言，大家把iOS冷启动的过程定义为：从用户点击App图标开始到appDelegate didFinishLaunching方法执行完成为止。这个过程主要分为两个阶段：

- T1：main()函数之前，即操作系统加载App可执行文件到内存，然后执行一系列的加载&链接等工作，最后执行至App的main()函数。
- T2：main()函数之后，即从main()开始，到appDelegate的didFinishLaunchingWithOptions方法执行完毕。

![](https://p0.meituan.net/travelcube/c0e0f70b538ae6527043421dc890459a34832.png)

然而，当didFinishLaunchingWithOptions执行完成时，用户还没有看到App的主界面，也不能开始使用App。例如在外卖App中，App还需要做一些初始化工作，然后经历定位、首页请求、首页渲染等过程后，用户才能真正看到数据内容并开始使用，我们认为这个时候冷启动才算完成。我们把这个过程定义为T3。

![](https://p0.meituan.net/travelcube/db061a267f6dc2b14ff7f9120020a5c261253.png)

综上，外卖App把冷启动过程定义为：**从用户点击App图标开始到用户能看到App主界面内容为止这个过程，即T1+T2+T3。**在App冷启动过程当中，这三个阶段中的每个阶段都存在很多可以被优化的点。

## [三、问题现状](#三、问题现状)

### [性能存量问题](#性能存量问题)

美团外卖iOS客户端经过几十个版本的迭代开发后，在冷启动过程中已经积累了若干性能问题，解决这些性能瓶颈是冷启动优化工作的首要目标，这些问题主要包括：

![](https://p0.meituan.net/travelcube/d2390f4cb9ee3ec996459a36c04553d4106767.png)

注：启动项的定义，在App启动过程中需要被完成的某项工作，我们称之为一个启动项。例如某个SDK的初始化、某个功能的预加载等。

### [性能增量问题](#性能增量问题)

一般情况下，在App早期阶段，冷启动不会有明显的性能问题。冷启动性能问题也不是在某个版本突然出现的，而是随着版本迭代，App功能越来越复杂，启动任务越来越多，冷启动时间也一点点延长。最后当我们注意到，并想要优化它的时候，这个问题已经变得很棘手了。外卖App的性能问题增量主要来自启动项的增加，随着版本迭代，启动项任务简单粗暴地堆积在启动流程中。如果每个版本冷启动时间增加0.1s，那么几个版本下来，冷启动时长就会明显增加很多。

## [四、治理思路](#四、治理思路)

冷启动性能问题的治理目标主要有三个：

1. 解决存量问题：优化当前性能瓶颈点，优化启动流程，缩短冷启动时间。
2. 管控增量问题：冷启动流程规范化，通过代码范式和文档指导后续冷启动过程代码的维护，控制时间增量。
3. 完善监控：完善冷启动性能指标监控，收集更详细的数据，及时发现性能问题。

![](https://p1.meituan.net/travelcube/11246e7f2fa16eb6281f0eb855a3ed4f183207.png)

## [五、规范启动流程](#五、规范启动流程)

截止至2017年底，美团外卖用户数已达2.5亿，而美团外卖App也已完成了从支撑单一业务的App到支持多业务的平台型App的演进[（美团外卖iOS多端复用的推动、支撑与思考）](https://tech.meituan.com/iOS_multiterminal_reuse.html)，公司的一些新兴业务也陆续集成到外卖App当中。下面是外卖App的架构图，外卖的架构主要分为三层，底层是基础组件层，中层是外卖平台层，平台层向下管理基础组件，向上为业务组件提供统一的适配接口，上层是基础组件层，包括外卖业务拆分的子业务组件（外卖App和美团App中的外卖频道可以复用子业务组件）和接入的其他非外卖业务。

![](https://p1.meituan.net/travelcube/21be5650c845c36193feb2c465b76e0a158992.png)

App的平台化为业务方提供了高效、标准的统一平台，但与此同时，平台化和业务的快速迭代也给冷启动带来了问题：

1. 现有的启动项堆积严重，拖慢启动速度。
2. 新的启动项缺乏添加范式，杂乱无章，修改风险大，难以阅读和维护。

面对这个问题，我们首先梳理了目前启动流程中所有的启动项，然后针对App平台化设计了新的启动项管理方式：**分阶段启动和启动项自注册**。

![](https://p1.meituan.net/travelcube/8ff8d109f0fc9ad3b0d800f2dce9ce21136469.png)

### [分阶段启动](#分阶段启动)

早期由于业务比较简单，所有启动项都是不加以区分，简单地堆积到didFinishLaunchingWithOptions方法中，但随着业务的增加，越来越多的启动项代码堆积在一起，性能较差，代码臃肿而混乱。

![](https://p0.meituan.net/travelcube/52635c087684765c9ee5b134c50226da136906.png)

通过对SDK的梳理和分析，我们发现启动项也需要根据所完成的任务被分类，有些启动项是需要刚启动就执行的操作，如Crash监控、统计上报等，否则会导致信息收集的缺失；有些启动项需要在较早的时间节点完成，例如一些提供用户信息的SDK、定位功能的初始化、网络初始化等；有些启动项则可以被延迟执行，如一些自定义配置，一些业务服务的调用、支付SDK、地图SDK等。我们所做的分阶段启动，首先就是把启动流程合理地划分为若干个启动阶段，然后依据每个启动项所做的事情的优先级把它们分配到相应的启动阶段，优先级高的放在靠前的阶段，优先级低的放在靠后的阶段。

![](https://p0.meituan.net/travelcube/e23cfa5397eb6f5015e372b4a3877b1c133714.png)

下面是我们对美团外卖App启动阶段进行的重新定义，对所有启动项进行的梳理和重新分类，把它们对应到合理的启动阶段。这样做一方面可以推迟执行那些不必过早执行的启动项，缩短启动时间；另一方面，把启动项进行归类，方便后续的阅读和维护。然后把这些规则落地为启动项的维护文档，指导后续启动项的新增和维护。

![](https://p1.meituan.net/travelcube/aa6f04b91154be74daa6620c84b2ff7695984.png)

通过上面的工作，我们梳理出了十几个可以推迟执行的启动项，占所有启动项的30%左右，有效地优化了启动项所占的这部分冷启动时间。

### [启动项自注册](#启动项自注册)

确定了启动项分阶段启动的方案后，我们面对的问题就是如何执行这些启动项。比较容易想到的方案是：在启动时创建一个启动管理器，然后读取所有启动项，然后当时间节点到来时由启动器触发启动项执行。这种方式存在两个问题：

1. 所有启动项都要预先写到一个文件中（在.m文件import，或用.plist文件组织），这种中心化的写法会导致臃肿的代码，难以阅读维护。
2. 启动项代码无法复用：启动项无法收敛到子业务库内部，在外卖App和美团App中要重复实现，和外卖App平台化的方向不符。

![](https://p1.meituan.net/travelcube/26af4e1cd782294cf9101f61191b594a165426.png)

而我们希望的方式是，启动项维护方式可插拔，启动项之间、业务模块之间不耦合，且一次实现可在两端复用。下图是我们采用的启动项管理方式，我们称之为启动项的自注册：一个启动项定义在子业务模块内部，被封装成一个方法，并且自声明启动阶段（例如一个启动项A，在独立App中可以声明为在willFinishLaunch阶段被执行，在美团App中则声明在resignActive阶段被执行）。这种方式下，启动项即实现了两端复用，不相关的启动项互相隔离，添加/删除启动项都更加方便。

![](https://p0.meituan.net/travelcube/62f3a7ab64c07d489617c72fca6f6831152162.png)

那么如何给一个启动项声明启动阶段？又如何在正确的时机触发启动项的执行呢？在代码上，一个启动项最终都会对应到一个函数的执行，所以在运行时只要能获取到函数的指针，就可以触发启动项。美团平台开发的组件启动治理基建Kylin正是这样做的：Kylin的核心思想就是在编译时把数据（如函数指针）写入到可执行文件的__DATA段中，运行时再从__DATA段取出数据进行相应的操作（调用函数）。

为什么要用借用__DATA段呢？原因就是为了能够覆盖所有的启动阶段，例如main()之前的阶段。

![](https://p0.meituan.net/travelcube/699afce3e08fcc76d03299e49bf3e41487690.png)

Kylin实现原理简述：Clang 提供了很多的编译器函数，它们可以完成不同的功能。其中一种就是 section() 函数，section()函数提供了二进制段的读写能力，它可以将一些编译期就可以确定的常量写入数据段。 在具体的实现中，主要分为编译期和运行时两个部分。在编译期，编译器会将标记了 **attribute**((section())) 的数据写到指定的数据段中，例如写一个{key(key代表不同的启动阶段), *pointer}对到数据段。到运行时，在合适的时间节点，在根据key读取出函数指针，完成函数的调用。

上述方式，可以封装成一个宏，来达到代码的简化，以调用宏 KLN_STRINGS_EXPORT("Key", "Value")为例，最终会被展开为：

```
__attribute__((used, section("__DATA" "," "__kylin__"))) static const KLN_DATA __kylin__0 = (KLN_DATA){(KLN_DATA_HEADER){"Key", KLN_STRING, KLN_IS_ARRAY}, "Value"};
```

使用示例，编译器把启动项函数注册到启动阶段A：

```
KLN_FUNCTIONS_EXPORT(STAGE_KEY_A)() { // 在a.m文件中，通过注册宏，把启动项A声明为在STAGE_KEY_A阶段执行
    // 启动项代码A
}
```

```
KLN_FUNCTIONS_EXPORT(STAGE_KEY_A)() { // 在b.m文件中，把启动项B声明为在STAGE_KEY_A阶段执行
    // 启动项代码B
}
```

在启动流程中，在启动阶段STAGE_KEY_A触发所有注册到STAGE_KEY_A时间节点的启动项，通过对这种方式，几乎没有任何额外的辅助代码，我们用一种很简洁的方式完成了启动项的自注册。

```
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    // 其他逻辑
    [[KLNKylin sharedInstance] executeArrayForKey:STAGE_KEY_A];  // 在此触发所有注册到STAGE_KEY_A时间节点的启动项
    // 其他逻辑
    return YES;
}
```

完成对现有的启动项的梳理和优化后，我们也输出了后续启动项的添加&维护规范，规范后续启动项的分类原则，优先级和启动阶段。目的是管控性能问题增量，保证优化成果。

## [六、优化main()之前](#六、优化main-之前)

在调用main()函数之前，基本所有的工作都是由操作系统完成的，开发者能够插手的地方不多，所以如果想要优化这段时间，就必须先了解一下，操作系统在main()之前做了什么。main()之前操作系统所做的工作就是把可执行文件（Mach-O格式）加载到内存空间，然后加载动态链接库dyld，再执行一系列动态链接操作和初始化操作的过程（加载、绑定、及初始化方法）。这方面的资料网上比较多，但重复性较高，此处附上一篇WWDC的Topic：[Optimizing App Startup Time](https://asciiwwdc.com/2016/sessions/406) 。

### [加载过程—从exec()到main()](#加载过程—从exec-到main)

真正的加载过程从exec()函数开始，exec()是一个系统调用。操作系统首先为进程分配一段内存空间，然后执行如下操作：

1. 把App对应的可执行文件加载到内存。
2. 把Dyld加载到内存。
3. Dyld进行动态链接。

![](https://p0.meituan.net/travelcube/db061a267f6dc2b14ff7f9120020a5c261253.png)

下面我们简要分析一下Dyld在各阶段所做的事情：

| 阶段 | 工作 |
|---|---|
| 加载动态库 | Dyld从主执行文件的header获取到需要加载的所依赖动态库列表，然后它需要找到每个 dylib，而应用所依赖的 dylib 文件可能会再依赖其他 dylib，所以所需要加载的是动态库列表一个递归依赖的集合 |
| Rebase和Bind | - Rebase在Image内部调整指针的指向。在过去，会把动态库加载到指定地址，所有指针和数据对于代码都是对的，而现在地址空间布局是随机化，所以需要在原来的地址根据随机的偏移量做一下修正 - Bind是把指针正确地指向Image外部的内容。这些指向外部的指针被符号(symbol)名称绑定，dyld需要去符号表里查找，找到symbol对应的实现 |
| Objc setup | - 注册Objc类 (class registration) - 把category的定义插入方法列表 (category registration) - 保证每一个selector唯一 (selector uniquing) |
| Initializers | - Objc的+load()函数 - C++的构造函数属性函数 - 非基本类型的C++静态全局变量的创建(通常是类或结构体) |

最后 dyld 会调用 main() 函数，main() 会调用 UIApplicationMain()，before main()的过程也就此完成。

了解完main()之前的加载过程后，我们可以分析出一些影响T1时间的因素：

1. 动态库加载越多，启动越慢。
2. ObjC类，方法越多，启动越慢。
3. ObjC的+load越多，启动越慢。
4. C的constructor函数越多，启动越慢。
5. C++静态对象越多，启动越慢。

针对以上几点，我们做了如下一些优化工作。

### [代码瘦身](#代码瘦身)

随着业务的迭代，不断有新的代码加入，同时也会废弃掉无用的代码和资源文件，但是工程中经常有无用的代码和文件被遗弃在角落里，没有及时被清理掉。这些无用的部分一方面增大了App的包体积，另一方便也拖慢了App的冷启动速度，所以及时清理掉这些无用的代码和资源十分有必要。

通过对Mach-O文件的了解，可以知道__TEXT:__objc_methname:中包含了代码中的所有方法，而__DATA__objc_selrefs中则包含了所有被使用的方法的引用，通过取两个集合的差集就可以得到所有未被使用的代码。核心方法如下，具体可以参考：[objc_cover](https://github.com/nst/objc_cover):

```
def referenced_selectors(path):
    re_sel = re.compile("__TEXT:__objc_methname:(.+)") //获取所有方法
    refs = set()
    lines = os.popen("/usr/bin/otool -v -s __DATA __objc_selrefs %s" % path).readlines() ## ios & mac //真正被使用的方法
    for line in lines:
        results = re_sel.findall(line)
        if results:
            refs.add(results[0])
    return refs
}
```

通过这种方法，我们排查了十几个无用类和250+无用的方法。

### [+load优化](#load优化)

目前iOS App中或多或少的都会写一些+load方法，用于在App启动执行一些操作，+load方法在Initializers阶段被执行，但过多+load方法则会拖慢启动速度，对于大中型的App更是如此。通过对App中+load的方法分析，发现很多代码虽然需要在App启动时较早的时机进行初始化，但并不需要在+load这样非常靠前的位置，完全是可以延迟到App冷启动后的某个时间节点，例如一些路由操作。其实+load也可以被当做一种启动项来处理，所以在替换+load方法的具体实现上，我们仍然采用了上面的Kylin方式。

使用示例：

```
// 用WMAPP_BUSINESS_INIT_AFTER_HOMELOADING声明替换+load声明即可，不需其他改动
WMAPP_BUSINESS_INIT_AFTER_HOMELOADING() { 
    // 原+load方法中的代码
}
```

```
// 在某个合适的时机触发注册到该阶段的所有方法，如冷启动结束后
[[KLNKylin sharedInstance] executeArrayForKey:@kWMAPP_BUSINESS_INITIALIZATION_AFTER_HOMELOADING_KEY] 
}
```

## [七、优化耗时操作](#七、优化耗时操作)

在main()之后主要工作是各种启动项的执行（上面已经叙述），主界面的构建，例如TabBarVC，HomeVC等等。资源的加载，如图片I/O、图片解码、archive文档等。这些操作中可能会隐含着一些耗时操作，靠单纯阅读非常难以发现，如何发现这些耗时点呢？找到合适的工具就会事半功倍。

### [Time Profiler](#time-profiler)

Time Profiler是Xcode自带的时间性能分析工具，它按照固定的时间间隔来跟踪每一个线程的堆栈信息，通过统计比较时间间隔之间的堆栈状态，来推算某个方法执行了多久，并获得一个近似值。Time Profiler的使用方法网上有很多使用教程，这里我们也不过多介绍，附上一篇使用文档：[Instruments Tutorial with Swift: Getting Started](https://www.raywenderlich.com/397-instruments-tutorial-with-swift-getting-started)。

### [火焰图](#火焰图)

除了Time Profiler，火焰图也是一个分析CPU耗时的利器，相比于Time Profiler，火焰图更加清晰。火焰图分析的产物是一张调用栈耗时图片，之所以称为火焰图，是因为整个图形看起来就像一团跳动的火焰，火焰尖部是调用栈的栈顶，底部是栈底，纵向表示调用栈的深度，横向表示消耗的时间。一个格子的宽度越大，越说明其可能是瓶颈。分析火焰图主要就是看那些比较宽大的火苗，特别留意那些类似“平顶山”的火苗。下面是美团平台开发的性能分析工具-Caesium的分析效果图：

![](https://p1.meituan.net/travelcube/1937c13dd8ef2301035197eb52eb10641650919.gif)

通过对火焰图的分析，我们发现了冷启动过程中存在着不少问题，并成功优化了0.3S+的时间。优化内容总结如下：

| 优化点 | 举例 |
|---|---|
| 发现隐晦的耗时操作 | 发现在冷启动过程中archive了一张图片，非常耗时 |
| 推迟&减少I/O操作 | 减少动画图片组的数量，替换大图资源等。因为相比于内存操作，硬盘I/O是非常耗时的操作 |
| 推迟执行的一些任务 | 如一些资源的I/O，一些布局逻辑，对象的创建时机等 |

## [八、优化串行操作](#八、优化串行操作)

在冷启动过程中，有很多操作是串行执行的，若干个任务串行执行，时间必然比较长。如果能变串行为并行，那么冷启动时间就能够大大缩短。

### [闪屏页的使用](#闪屏页的使用)

现在许多App在启动时并不直接进入首页，而是会向用户展示一个持续一小段时间的闪屏页，如果使用恰当，这个闪屏页就能帮我们节省一些启动时间。因为当一个App比较复杂的时候，启动时首次构建App的UI就是一个比较耗时的过程，假定这个时间是0.2秒，如果我们是先构建首页UI，然后再在Window上加上这个闪屏页，那么冷启动时，App就会实实在在地卡住0.2秒，但是如果我们是先把闪屏页作为App的RootViewController，那么这个构建过程就会很快。因为闪屏页只有一个简单的ImageView，而这个ImageView则会向用户展示一小段时间，这时我们就可以利用这一段时间来构建首页UI了，一举两得。

![](https://p0.meituan.net/travelcube/ca0f8fc0ba63235d9e4816cf178fd285118586.png)

### [缓存定位&首页预请求](#缓存定位-首页预请求)

美团外卖App冷启动过程中一个重要的串行流程就是：首页定位--\>首页请求--\>首页渲染过程，这三个操作占了整个首页加载时间的77%左右，所以想要缩短冷启动时间，就一定要从这三点出发进行优化。

之前串行操作流程如下：

![](https://p1.meituan.net/travelcube/22ae6296598300ddce12a14f987619c859034.png)

优化后的设计，在发起定位的同时，使用客户端缓存定位，进行首页数据的预请求，使定位和请求并行进行。然后当用户真实定位成功后，判断真实定位是否命中缓存定位，如果命中，则刚才的预请求数据有效，这样可以节省大概40%的时间首页加载时间，效果非常明显；如果未命中，则弃用预请求数据，重新请求。

![](https://p1.meituan.net/travelcube/2d17704cabd9db086b325377315e465890662.png)

## [九、数据监控](#九、数据监控)

Time Profiler和Caesium火焰图都只能在线下分析App在单台设备中的耗时操作，局限性比较大，无法在线上监控App在用户设备上的表现。外卖App使用公司内部自研的Metrics性能监控系统，长期监控App的性能指标，帮助我们掌握App在线上各种环境下的真实表现，并为技术优化项目提供可靠的数据支持。Metrics监控的核心指标之一，就是冷启动时间。

### [冷启动开始&结束时间节点](#冷启动开始-结束时间节点)

1. 结束时间点：结束时间比较好确定，我们可以将首页某些视图元素的展示作为首页加载完成的标志。
2. 开始时间点：一般情况下，我们都是在main()之后才开始接管App，但以main()函数作为冷启动起始点显然不合适，因为这样无法统计到T1时间段。那么，起始时间如何确定呢？目前业界常见的有两种方法，一是以可执行文件中任意一个类的+load方法的执行时间作为起始点；二是分析dylib的依赖关系，找到叶子节点的dylib，然后以其中某个类的+load方法的执行时间作为起始点。根据Dyld对dylib的加载顺序，后者的时机更早。但是这两种方法获取的起始点都只在Initializers阶段，而Initializers之前的时长都没有被计入。Metrics则另辟蹊径，以App的进程创建时间（即exec函数执行时间）作为冷启动的起始时间。因为系统允许我们通过sysctl函数获得进程的有关信息，其中就包括进程创建的时间戳。

```
#import <sys/sysctl.h>
#import <mach/mach.h>

+ (BOOL)processInfoForPID:(int)pid procInfo:(struct kinfo_proc*)procInfo
{
    int cmd[4] = {CTL_KERN, KERN_PROC, KERN_PROC_PID, pid};
    size_t size = sizeof(*procInfo);
    return sysctl(cmd, sizeof(cmd)/sizeof(*cmd), procInfo, &size, NULL, 0) == 0;
}

+ (NSTimeInterval)processStartTime
{
    struct kinfo_proc kProcInfo;
    if ([self processInfoForPID:[[NSProcessInfo processInfo] processIdentifier] procInfo:&kProcInfo]) {
        return kProcInfo.kp_proc.p_un.__p_starttime.tv_sec * 1000.0 + kProcInfo.kp_proc.p_un.__p_starttime.tv_usec / 1000.0;
    } else {
        NSAssert(NO, @"无法取得进程的信息");
        return 0;
    }
}
```

进程创建的时机非常早。经过实验，在一个新建的空白App中，进程创建时间比叶子节点dylib中的+load方法执行时间早12ms，比main函数的执行时间早13ms（实验设备：iPhone 7 Plus （iOS 12.0）、Xcode 10.0、Release 模式）。外卖App线上的数据则更加明显，同样的机型（iPhone 7 Plus）和系统版本（iOS 12.0），进程创建时间比叶子节点dylib中的+load方法执行时间早688ms。而在全部机型和系统版本中，这一数据则是878ms。

### [冷启动过程时间节点](#冷启动过程时间节点)

我们也在App冷启动过程中的所有关键节点打上一连串测速点，Metrics会记录下测速点的名称，及其距离进程创建时间的时长。我们没有采用自动打点的方式，是因为外卖App的冷启动过程十分复杂，而自动打点无法做到如此细致，并不实用。另外，Metrics记录的是时间轴上以进程创建时间为原点的一组顺序的时间点，而不是一组时间段，是因为顺序的时间点可以计算任意两个时间点之间的距离，即可以将时间点处理成时间段。但是，一组时间段可能无法还原为顺序的时间点，因为时间段之间可能并不是首尾相接的，特别是对于异步执行或者多线程的情况。

在测速完毕后，Metrics会统一将所有测速点上报到后台。下图是美团外卖App 6.10版本的部分过程节点监控数据截图：

![](https://p1.meituan.net/travelcube/43876b4100489ee09211347cbcb3e89e132435.png)

Metrics还会由后台对数据做聚合计算，得到冷启动总时长和各个测速点时长的50分位数、90分位数和95分位数的统计数据，这样我们就能从宏观上对冷启动时长分布情况有所了解。下图中横轴为时长，纵轴为上报的样本数。

![](https://p0.meituan.net/travelcube/c7459a320d3fdedb37bf3af3cbb9b36a84832.png)

## [十、总结](#十、总结)

对于快速迭代的App，随着业务复杂度的增加，冷启动时长会不可避免的增加。冷启动流程也是一个比较复杂的过程，当遇到冷启动性能瓶颈时，我们可以根据App自身的特点，配合工具的使用，从多方面、多角度进行优化。同时，优化冷启动存量问题只是冷启动治理的第一步，因为冷启动性能问题并不是一日造成的，也不能简单的通过一次优化工作就能解决，我们需要通过合理的设计、规范的约束，来有效地管控性能问题的增量，并通过持续的线上监控来及时发现并修正性能问题，这样才能够长期保证良好的App冷启动体验。

## [作者简介](#作者简介)

- 郭赛，美团点评资深工程师。2015年加入美团，目前作为外卖iOS团队主力开发，负责移动端业务开发，业务类基础设施的建设与维护。
- 徐宏，美团点评资深工程师。2016年加入美团，目前作为外卖iOS团队主力开发，负责移动端APM性能监控，高可用基础设施支撑相关推进工作。

## [招聘](#招聘)

美团外卖长期招聘Android、iOS、FE高级/资深工程师和技术专家，Base北京、上海、成都，欢迎有兴趣的同学投递简历到chenhang03@meituan.com。
