Matrix ResourceCanary
======

+ [背景](#背景)
+ [设计目标](#设计目标)
+ [预研与大致实现](#预研与大致实现)
+ [细节与改进](#细节与改进)
+ [使用效果与开销](#使用效果与开销)
+ [未来的计划](#未来的计划)

<a name="背景"></a>
背景
------

随着微信Android客户端的代码规模越来越庞大，依赖人工Review来确保代码没有泄漏或冗余问题虽然还是最保险的办法，但代码增长的速度总是大于Review的速度，完全靠人力介入变得越来越吃力，且依赖线上反馈进行事后排查也非常被动。为此我们从最为常见的Activity泄漏和Bitmap对象冗余入手提出了研发ResourceCanary模块的计划。

作为Matrix的一个子模块，ResourceCanary将把原本难以发现的Activity泄漏和重复创建的冗余Bitmap暴露出来，并提供引用链等信息帮助排查这些问题的根源，以提高微信客户端的代码质量。

<a name="设计目标"></a>
设计目标
------

在引入任何自动分析工具之前，对于Activity泄漏，一般都是在自动化测试阶段监控内存占用，一旦超过预期，则发起一次GC后进行Dump Hprof操作。分析人员将Hprof文件导入MAT中查看各个Activity的引用链，找出被静态成员或Application对象等长生命周期对象持有的Activity，再进行修复。对于冗余的Bitmap，也是将Hprof导入Android Monitor后通过Android Monitor自带的工具找出冗余的Bitmap对象。

可见上面的流程人工参与程度较大，与Matrix对质量监控的日常化、流程化的目标不符。我们希望在引入ResourceCanary后能实现下面的目标：

- 自动且较为准确地监测Activity泄漏，发现泄漏之后再触发Dump Hprof而不是根据预先设定的内存占用阈值盲目触发
- 自动获取泄漏的Activity和冗余Bitmap对象的引用链
- 能灵活地扩展Hprof的分析逻辑，必要时允许提取Hprof文件人工分析

<a name="预研与大致实现"></a>

预研与大致实现
------

根据设计目标，首先我们需要解决监测阶段和分析阶段的自动化问题。期间我们参考了LeakCanary和Android Monitor中的部分代码，并根据需要作了一些修改。

### 监测阶段

首先回顾一下Activity泄漏的大致定义：

> Activity对象被生命周期更长的对象通过强引用持有，使Activity生命周期结束后仍无法被GC机制回收，导致其占用的内存空间无法得到释放。

不难发现要监测Activity泄漏，我们要解决两个问题：

+ 如何在一个恰当的时机得知一个Activity已经结束了生命周期
+ 如何判断一个Activity无法被GC机制回收

对于第一个问题，最直观的想法就是找一个Activity被销毁时的必经调用点记录下当前Activity的信息，显然`Activity.onDestroy()`方法是一个不错的选择。实现上也有下面两种做法：

+ 让所有Activity继承一个BaseActivity，然后在`BaseActivity.onDestroy()`方法中进行记录。
+ 通过某种机制得知`Activity.onDestroy()`方法被调用，然后进行记录
	+ 4.0以前可以通过反射替换`ActivityThread.mInstrumentation`对象为自己的代理，然后在代理中的`callActivityOnDestroy()`方法中记录。
	+ 4.0以后可以通过`Application.registerActivityLifecycleCallbacks()`方法注册一个回调对象，在回调对象的`onActivityDestroyed()`方法中记录。

考虑到Matrix将被设计成一个通用框架，在ResourceCanary里让所有Activity继承一个BaseActivity的做法入侵性太强，基本不在考虑范围内。再加上目前Android 4.0版本以前的机器占比并不高，放弃4.0版本以前的机器后第二种做法就不再需要反射系统隐藏字段了，因此最终我们选择了第二种做法得知Activity已经结束了生命周期。

对于第二个问题，乍一看Dalvik或ART虚拟机的GC机制我们是没法直接干预的，而且Android Framework也没有提供任何API让我们直接得知一个对象已被GC，但熟悉Java的同学大概很快就想到了WeakReference也许可以曲线救国。根据Java API文档中的描述：

> **Weak reference objects, which do not prevent their referents from being made finalizable, finalized, and then reclaimed.**
> 
> ……
> 
> **Suppose that the garbage collector determines at a certain point in time that an object is weakly reachable. At that time it will atomically clear all weak references to that object** and all weak references to any other weakly-reachable objects from which that object is reachable through a chain of strong and soft references. At the same time it will declare all of the formerly weakly-reachable objects to be finalizable. **At the same time or at some later time it will enqueue those newly-cleared weak references that are registered with reference queues.**

我们可以通过创建一个持有已销毁的Activity的WeakReference，然后主动触发一次GC，如果这个Activity能被回收，则持有它的WeakReference会被置空，且这个被回收的Activity一段时间后会被加入事先注册到WeakReference的一个队列里。这样我们就能间接知道某个被销毁的Activity能否被回收了。

另外，由于我们暂时还没发现即时得知一个Bitmap是否冗余的方法，因此监测阶段我们并不特别为冗余Bitmap设计监测逻辑，留待分析阶段来获取所有冗余的Bitmap对象的信息。

### 分析阶段

通过监测阶段确定了某个Activity已经泄漏并触发了Dump Hprof之后，接下来就可以进行下面两项分析了：

+ 从Hprof文件中获取泄漏的Activity到GC Root的强引用链
+ 从Hprof文件中获取所有冗余的Bitmap对象以及它们的强引用链（即图像数据完全相同的Bitmap对象）

**GC Root**
im
GC Root是指这样一类对象，他们本身并不被其他生命周期更长的对象持有，但JVM的特性导致了这些对象无法被GC机制回收，因此从他们出发，经过一系列强引用可到达的对象都是无法被回收的。他们包括下列对象：

+ 类；（被JVM加载的类是无法卸载的，因此无法被回收，导致被类持有（即通过静态成员持有）的对象也无法被回收）
+ 活动的Thread实例；
+ 局部变量或方法参数变量持有的对象；
+ JNILocalReference持有的对象；
+ JNIGlobalReference持有的对象；
+ synchronized关键字用到的对象；

如果某个Activity被泄漏，则必然存在从它到某个GC Root的强引用链。只要我们将这条强引用链找出来，开发者就能根据引用链上的对象找到合适的修改点快速解决问题。

**获取泄漏的Activity到GC Root的强引用链**

Hprof文件中包含了Dump时刻内存中的所有对象的信息，包括类的描述，实例的数据和引用关系，线程的栈信息等。具体可参考[这份文档](http://hg.openjdk.java.net/jdk8/jdk8/jdk/raw-file/43cb25339b55/src/share/demo/jvmti/hprof/manual.html)中的Binary Dump Format一节。按照文档描述的格式将Hprof中的实例信息解析成描述引用关系的图结构后，套用经典的图搜索算法即可找到泄漏的Activity到GC Root的强引用链了。

大多数时候这样的强引用链不止一条，全部找出来会让一次分析操作的耗时大大增加，延长了整个测试流程的周期，而且对解决问题并没有更多帮助。实际上我们只需要找到最短的那条就可以了。如下图：
![ref-graph](https://github.com/Tencent/matrix/blob/dev/assets/img/wiki/resource-canary/ref-graph.png)

这种情况下只要切断蓝色箭头即可使泄漏的Activity与GC Root脱离联系。如果持有泄漏的Activity的GC Root不止一个，或者从GC Root出发的引用不止一条，在Matrix框架成为流程化工具的背景下我们可以通过多次检测来解决，这样至少保证了每次执行ResourceCanary模块的耗时稳定在一个可预计的范围内，不至于在极端情况下耽误其他流程。

本来我们打算自行实现这个算法，幸运的是在阅读LeakCanary的代码时我们发现了一个叫haha的库已经把Hprof文件按照文档描述的格式解析成了结构化的引用关系图，而且LeakCanary也按照与上面的描述类似的思路实现了引用链的提取逻辑，于是我们就不再重复造轮子，直接使用了LeakCanary的这部分代码了。

**从Hprof文件中获取所有冗余的Bitmap对象**

这个功能Android Monitor已经有完整实现了，原理简单粗暴——把所有未被回收的Bitmap的数据buffer取出来，然后先对比所有长度为1的buffer，找出相同的，记录所属的Bitmap对象；再对比所有长度为2的、长度为3的buffer……直到把所有buffer都比对完，这样就记录下了所有冗余的Bitmap对象了，接着再套用LeakCanary获取引用链的逻辑把这些Bitmap对象到GC Root的最短强引用链找出来即可。

### 让ResourceCanary更为灵活

目前为止设计目标中的自动化要求已确定了解决方案，还有最后一个问题：上面提到的监测和分析两步是都在App侧做，还是把分析步骤拆到Matrix服务端做呢？由于监测步骤监测的是Activity泄漏这个Android系统特有的概念，因此不得不依赖系统环境；但分析步骤只是一个处理Hprof文件的过程，完全不需要依赖Android系统，理论上将这两部拆开是完全可行的。而且拆开之后我们至少能获得下面的好处：

+ 更新分析逻辑不再需要重新发客户端版本
+ Hprof文件留在了服务端，为人工分析提供了机会
+ 如果跳过触发Dump Hprof，甚至可以把监测步骤在现网环境启用，以发现测试阶段难以触发的Activity泄漏

于是ResourceCanary最终决定将监测步骤和分析步骤拆成两个独立的工具，以满足设计目标。

<a name="细节与改进"></a>
细节与改进
------

### 减少误报

LeakCanary的监测部分的工作流程如下图所示：
![leakcanary-watcher-route](https://github.com/Tencent/matrix/blob/dev/assets/img/wiki/resource-canary/leakcanary-watcher-route.png)

可见其对Activity是否泄漏的判断依赖VM会将可回收的对象加入WeakReference关联的ReferenceQueue这一特性，在Demo的测试过程中我们发现这中做法在个别系统上可能存在误报，原因大致如下：

+ VM并没有提供强制触发GC的API，通过`System.gc()`或`Runtime.getRuntime().gc()`只能“建议”系统进行GC，如果系统忽略了我们的GC请求，可回收的对象就不会被加入ReferenceQueue
+ 将可回收对象加入ReferenceQueue需要等待一段时间，LeakCanary采用延时100ms的做法加以规避，但似乎并不绝对管用
+ 监测逻辑是异步的，如果判断Activity是否可回收时某个Activity正好还被某个方法的局部变量持有，就会引起误判
+ 若反复进入泄漏的Activity，LeakCanary会重复提示该Activity已泄漏

对此我们做了以下改进：

+ 增加一个一定能被回收的“哨兵”对象，用来确认系统确实进行了GC
+ 直接通过`WeakReference.get()`来判断对象是否已被回收，避免因延迟导致误判
+ 若发现某个Activity无法被回收，再重复判断3次，且要求从该Activity被记录起有2个以上的Activity被创建才认为是泄漏，以防在判断时该Activity被局部变量持有导致误判
+ 对已判断为泄漏的Activity，记录其类名，避免重复提示该Activity已泄漏

### 裁剪Hprof

Hprof文件的大小一般约为Dump时的内存占用大小，就微信而言Dump出来的Hprof大小通常为150MB～200MB之间，如果不做任何处理直接将此Hprof文件上传到服务端，一方面会消耗大量带宽资源，另一方面服务端将Hprof文件长期存档时也会占用服务器的存储空间。

通过分析Hprof文件格式可知，Hprof文件中buffer区存放了所有对象的数据，包括字符串数据、所有的数组等，而我们的分析过程却只需要用到部分字符串数据和Bitmap的buffer数组，其余的buffer数据都可以直接剔除，这样处理之后的Hprof文件通常能比原始文件小1/10以上。

### 提高Hprof分析效率

LeakCanary中的引用链查找算法都是针对单个目标设计的，ResourceCanary中查找冗余Bitmap时可能找到多个结果，如果分别对每个结果中的Bitmap对象调用该算法，在访问引用关系图中的节点时会遇到非常多的重复访问的节点，降低了查找效率。为此我们修改了LeakCanary的引用链查找算法，使其在一次调用中能同时查找多个目标到GC Root的最短引用链。

<a name="使用效果与开销"></a>

## 使用效果与开销

### 使用效果

以其中一份检测结果为例，ResourceCanary会输出如下的引用关系：

> Format：TypeName FieldName / array ElemType\[\] \[index\] 
>
> android.app.ActivityThread mOnPauseListeners
>
> android.util.ArrayMap mArray
>
> array java.lang.Object\[\] \[0\]
>
> com.tencent.mm.plugin.account.ui.SimpleLoginUI instance

分析之后可知，此处SimpleLoginUI的一个实例被ActivityThread中类型为ArrayMap的mOnPauseListeners字段持有，导致了泄漏。

### 性能开销

监测部分，在周期性轮询阶段由于是在后台线程执行的，目前设定的轮询间隔为1min。以通讯录界面和朋友圈界面的帧率作为参考，在接入ResourceCanary后2min内的平均帧率降低了10帧左右（未接入时同样时段内的平均帧率为120帧/秒），开销并不明显。

Dump Hprof阶段的开销则较大。Dump时整个App会卡死约5～15s，但考虑到ResourceCanary模块不会在线上环境启用，因此尚可接受。个人猜想Dump Hprof操作的耗时通过某些hack应该还有优化的空间；对Hprof的预处理阶段耗时约3～20s（取决于机器性能和Hprof的大小），内存开销约为1.5倍Hprof的大小，但由于是在另一个进程中完成的，而且只有在触发了Dump Hprof之后才会执行，因此对App正常运行的干扰也较小。不过改进算法使耗时和内存占用都尽可能少，还是要继续探究的。

分析部分由于是服务器上的工具，因此设计时并未太关注性能问题，实际使用时分析一个200M左右的Hprof平均需要15s左右的时间。此部分主要消耗在引用链分析上。由于引用链分析需要广度优先遍历完Hprof中记录的全部对象，因此在想到合适的剪枝条件之前时间消耗应该不会有显著降低。

未来的计划
------

目前ResourceCanary支持了Activity泄漏监测和冗余Bitmap监测，但由于检测机制本身和ROM的碎片化等问题，目前仍有少量误报的情况，未来我们将持续跟进误报案例，提高ResourceCanary的可靠性。