---
title: iOS 卡顿监测方案总结
source_url: 'https://cloud.tencent.com/developer/article/1895911'
source_domain: cloud.tencent.com
source_group: platform
original_language: zh
published: ''
archived_at: 2026-07-27
content_hash: 'sha256:51f21d616985bbb2'
plan_ref: 第五周：RunLoop、AutoreleasePool、响应者链与生命周期 / Day 2｜先会 RunLoop，再理解常驻线程与卡顿监测（对应 W4-03）
plan_week: 第五周：RunLoop、AutoreleasePool、响应者链与生命周期
plan_day: Day 2｜先会 RunLoop，再理解常驻线程与卡顿监测（对应 W4-03）
container: '//div[contains(@class,''rno-markdown'')]'
container_source: map
---

> 原文：[iOS 卡顿监测方案总结](https://cloud.tencent.com/developer/article/1895911)

**前言**

最近在写 `APM` 相关的东西，所以整理了一下 iOS 中卡顿监测的那些方案，不了解卡顿的原理的可以看这篇文章**iOS 保持界面流畅的技巧[1]**，写的很好。

### **FPS**

**FPS (Frames Per Second)** 是图像领域中的定义，表示每秒渲染帧数，通常用于衡量画面的流畅度，每秒帧数越多，则表示画面越流畅，`60fps` 最佳，一般我们的 APP 的 FPS 只要保持在 `50-60` 之间，用户体验都是比较流畅的。

监测FPS也有好几种，这里只说最常用的方案，我最早是在 **YYFPSLabel[2]** 中看到的。实现原理实现原理是向主线程的 `RunLoop` 的添加一个 `commonModes` 的 `CADisplayLink`，每次屏幕刷新的时候都要执行 `CADisplayLink` 的方法，所以可以统计 1s 内屏幕刷新的次数，也就是 FPS 了，下面贴上我用 Swift 实现的代码。

代码语言：javascript

复制

```javascript
class WeakProxy: NSObject {
    
    weak var target: NSObjectProtocol?
    
    init(target: NSObjectProtocol) {
        self.target = target
        super.init()
    }
    
    override func responds(to aSelector: Selector!) -> Bool {
        return (target?.responds(to: aSelector) ?? false) || super.responds(to: aSelector)
    }

    override func forwardingTarget(for aSelector: Selector!) -> Any? {
        return target
    }
}

class FPSLabel: UILabel {
    var link:CADisplayLink!
    //记录方法执行次数
    var count: Int = 0
    //记录上次方法执行的时间，通过link.timestamp - _lastTime计算时间间隔
    var lastTime: TimeInterval = 0
    var _font: UIFont!
    var _subFont: UIFont!
    
    fileprivate let defaultSize = CGSize(width: 55,height: 20)
    
    override init(frame: CGRect) {
        super.init(frame: frame)
        if frame.size.width == 0 && frame.size.height == 0 {
            self.frame.size = defaultSize
        }
        self.layer.cornerRadius = 5
        self.clipsToBounds = true
        self.textAlignment = NSTextAlignment.center
        self.isUserInteractionEnabled = false
        self.backgroundColor = UIColor.white.withAlphaComponent(0.7)
        
        _font = UIFont(name: "Menlo", size: 14)
        if _font != nil {
            _subFont = UIFont(name: "Menlo", size: 4)
        }else{
            _font = UIFont(name: "Courier", size: 14)
            _subFont = UIFont(name: "Courier", size: 4)
        }
        
        link = CADisplayLink(target: WeakProxy.init(target: self), selector: #selector(FPSLabel.tick(link:)))
        link.add(to: RunLoop.main, forMode: .commonModes)
    }
    
    //CADisplayLink 刷新执行的方法
    @objc func tick(link: CADisplayLink) {
        
        guard lastTime != 0 else {
            lastTime = link.timestamp
            return
        }
        
        count += 1
        let timePassed = link.timestamp - lastTime
        
        //时间大于等于1秒计算一次，也就是FPSLabel刷新的间隔，不希望太频繁刷新
        guard timePassed >= 1 else {
            return
        }
        lastTime = link.timestamp
        let fps = Double(count) / timePassed
        count = 0
        
        let progress = fps / 60.0
        let color = UIColor(hue: CGFloat(0.27 * (progress - 0.2)), saturation: 1, brightness: 0.9, alpha: 1)
        
        let text = NSMutableAttributedString(string: "\(Int(round(fps))) FPS")
        text.addAttribute(NSAttributedStringKey.foregroundColor, value: color, range: NSRange(location: 0, length: text.length - 3))
        text.addAttribute(NSAttributedStringKey.foregroundColor, value: UIColor.white, range: NSRange(location: text.length - 3, length: 3))
        text.addAttribute(NSAttributedStringKey.font, value: _font, range: NSRange(location: 0, length: text.length))
        text.addAttribute(NSAttributedStringKey.font, value: _subFont, range: NSRange(location: text.length - 4, length: 1))
        self.attributedText = text
    }
    
    // 把displaylin从Runloop modes中移除
    deinit {
        link.invalidate()
    }
    
    required init?(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
}
```

### **RunLoop**

其实 `FPS` 中 `CADisplayLink` 的使用也是基于 `RunLoop`，都依赖 `main RunLoop`。我们来看看

先来看看简版的 `RunLoop` 的代码

代码语言：javascript

复制

```javascript
// 1.进入loop
__CFRunLoopRun(runloop, currentMode, seconds, returnAfterSourceHandled)

// 2.RunLoop 即将触发 Timer 回调。
__CFRunLoopDoObservers(runloop, currentMode, kCFRunLoopBeforeTimers);
// 3.RunLoop 即将触发 Source0 (非port) 回调。
__CFRunLoopDoObservers(runloop, currentMode, kCFRunLoopBeforeSources);
// 4.RunLoop 触发 Source0 (非port) 回调。
sourceHandledThisLoop = __CFRunLoopDoSources0(runloop, currentMode, stopAfterHandle)
// 5.执行被加入的block
__CFRunLoopDoBlocks(runloop, currentMode);

// 6.RunLoop 的线程即将进入休眠(sleep)。
__CFRunLoopDoObservers(runloop, currentMode, kCFRunLoopBeforeWaiting);

// 7.调用 mach_msg 等待接受 mach_port 的消息。线程将进入休眠, 直到被下面某一个事件唤醒。
__CFRunLoopServiceMachPort(waitSet, &msg, sizeof(msg_buffer), &livePort)

// 进入休眠
// 8.RunLoop 的线程刚刚被唤醒了。
__CFRunLoopDoObservers(runloop, currentMode, kCFRunLoopAfterWaiting

// 9.如果一个 Timer 到时间了，触发这个Timer的回调
__CFRunLoopDoTimers(runloop, currentMode, mach_absolute_time())

// 10.如果有dispatch到main_queue的block，执行bloc
 __CFRUNLOOP_IS_SERVICING_THE_MAIN_DISPATCH_QUEUE__(msg);
 
 // 11.如果一个 Source1 (基于port) 发出事件了，处理这个事件
__CFRunLoopDoSource1(runloop, currentMode, source1, msg);

// 12.RunLoop 即将退出
__CFRunLoopDoObservers(rl, currentMode, kCFRunLoopExit);
```

我们可以看到 `RunLoop` 调用方法主要集中在 `kCFRunLoopBeforeSources` 和 `kCFRunLoopAfterWaiting`之间，有人可能会问 `kCFRunLoopAfterWaiting` 之后也有一些方法调用，为什么不监测呢？

我的理解，大部分导致卡顿的的方法是在 `kCFRunLoopBeforeSources` 和 `kCFRunLoopAfterWaiting` 之间，比如 `source0` 主要是处理 App 内部事件，App 自己负责管理(出发),如 `UIEvent(Touch` 事件等，GS 发起到 RunLoop 运行再到事件回调到 UI)、`CFSocketRef`。

开辟一个子线程，然后实时计算 `kCFRunLoopBeforeSources` 和 `kCFRunLoopAfterWaiting` 两个状态区域之间的耗时是否超过某个阀值，来断定主线程的卡顿情况。

这里做法又有点不同，**iOS 实时卡顿监控[3]**是设置连续 5 次超时 `50ms` 认为卡顿，戴铭在 **GCDFetchFeed[4]**中设置的是连续 3 次超时 `80ms` 认为卡顿的代码。以下是 **iOS 实时卡顿监控[5]**中提供的代码：

代码语言：javascript

复制

```javascript
- (void)start
{
    if (observer)
        return;
    
    // 信号
    semaphore = dispatch_semaphore_create(0);
    
    // 注册RunLoop状态观察
    CFRunLoopObserverContext context = {0,(__bridge void*)self,NULL,NULL};
    observer = CFRunLoopObserverCreate(kCFAllocatorDefault,
                                       kCFRunLoopAllActivities,
                                       YES,
                                       0,
                                       &runLoopObserverCallBack,
                                       &context);
    CFRunLoopAddObserver(CFRunLoopGetMain(), observer, kCFRunLoopCommonModes);
    
    // 在子线程监控时长
    dispatch_async(dispatch_get_global_queue(0, 0), ^{
        while (YES)
        {
            long st = dispatch_semaphore_wait(semaphore, dispatch_time(DISPATCH_TIME_NOW, 50*NSEC_PER_MSEC));
            if (st != 0)
            {
                if (!observer)
                {
                    timeoutCount = 0;
                    semaphore = 0;
                    activity = 0;
                    return;
                }
                
                if (activity==kCFRunLoopBeforeSources || activity==kCFRunLoopAfterWaiting)
                {
                    if (++timeoutCount < 5)
                        continue;
                    
                    PLCrashReporterConfig *config = [[PLCrashReporterConfig alloc] initWithSignalHandlerType:PLCrashReporterSignalHandlerTypeBSD
                                                                                       symbolicationStrategy:PLCrashReporterSymbolicationStrategyAll];
                    PLCrashReporter *crashReporter = [[PLCrashReporter alloc] initWithConfiguration:config];
                    
                    NSData *data = [crashReporter generateLiveReport];
                    PLCrashReport *reporter = [[PLCrashReport alloc] initWithData:data error:NULL];
                    NSString *report = [PLCrashReportTextFormatter stringValueForCrashReport:reporter
                                                                              withTextFormat:PLCrashReportTextFormatiOS];
                    
                    NSLog(@"------------\n%@\n------------", report);
                }
            }
            timeoutCount = 0;
        }
    });
}
```

### **子线程 Ping**

但是由于主线程的 RunLoop 在闲置时基本处于 `Before Waiting` 状态，这就导致了即便没有发生任何卡顿，这种检测方式也总能认定主线程处在卡顿状态。

这套卡顿监控方案大致思路为：创建一个子线程通过信号量去 ping 主线程，因为 ping 的时候主线程肯定是在 `kCFRunLoopBeforeSources` 和 `kCFRunLoopAfterWaiting` 之间。每次检测时设置标记位为 YES，然后派发任务到主线程中将标记位设置为 NO。接着子线程沉睡超时阙值时长，判断标志位是否成功设置成 NO，如果没有说明主线程发生了卡顿。**ANREye[6]** 中就是使用子线程 Ping 的方式监测卡顿的。

代码语言：javascript

复制

```javascript
@interface PingThread : NSThread
......
@end

@implementation PingThread

- (void)main {
    [self pingMainThread];
}

- (void)pingMainThread {
    while (!self.cancelled) {
        @autoreleasepool {
            dispatch_async(dispatch_get_main_queue(), ^{
                [_lock unlock];
            });
            
            CFAbsoluteTime pingTime = CFAbsoluteTimeGetCurrent();
            NSArray *callSymbols = [StackBacktrace backtraceMainThread];
            [_lock lock];
            if (CFAbsoluteTimeGetCurrent() - pingTime >= _threshold) {
                ......
            }
            [NSThread sleepForTimeInterval: _interval];
        }
    }
}
@end
```

以下是我用 Swift 实现的：

代码语言：javascript

复制

```javascript
public class CatonMonitor {
    
    enum Constants {
        static let timeOutInterval: TimeInterval = 0.05
        static let queueTitle = "com.roy.PerformanceMonitor.CatonMonitor"
    }
    
    private var queue: DispatchQueue = DispatchQueue(label: Constants.queueTitle)
    private var isMonitoring = false
    private var semaphore: DispatchSemaphore = DispatchSemaphore(value: 0)
    
    public init() {}
    
    public func start() {
        guard !isMonitoring else { return }
        
        isMonitoring = true
        queue.async {
            while self.isMonitoring {
                
                var timeout = true
                
                DispatchQueue.main.async {
                    timeout = false
                    self.semaphore.signal()
                }
                
                Thread.sleep(forTimeInterval: Constants.timeOutInterval)
                
                if timeout {
                    let symbols = RCBacktrace.callstack(.main)
                    for symbol in symbols {
                        print(symbol.description)
                    }
                }
                self.semaphore.wait()
            }
        }
    }
    
    public func stop() {
        guard isMonitoring else { return }
        
        isMonitoring = false
    }
}
```

### **CPU 超过了 80%**

这个是 **Matrix-iOS 卡顿监控[7]**提到的：

> 我们也认为 CPU 过高也可能导致应用出现卡顿，所以在子线程检查主线程状态的同时，如果检测到 CPU 占用过高，会捕获当前的线程快照保存到文件中。目前微信应用中认为，单核 CPU 的占用超过了 80%，此时的 CPU 占用就过高了。

这种方式一般不能单独拿来作为卡顿监测，但可以像微信 Matrix 一样配合其他方式一起工作。

戴铭在 **GCDFetchFeed** 中如果 CPU 的占用超过了 80% 也捕获函数调用栈，以下是代码：

代码语言：javascript

复制

```javascript
#define CPUMONITORRATE 80

+ (void)updateCPU {
    thread_act_array_t threads;
    mach_msg_type_number_t threadCount = 0;
    const task_t thisTask = mach_task_self();
    kern_return_t kr = task_threads(thisTask, &threads, &threadCount);
    if (kr != KERN_SUCCESS) {
        return;
    }
    for (int i = 0; i < threadCount; i++) {
        thread_info_data_t threadInfo;
        thread_basic_info_t threadBaseInfo;
        mach_msg_type_number_t threadInfoCount = THREAD_INFO_MAX;
        if (thread_info((thread_act_t)threads[i], THREAD_BASIC_INFO, (thread_info_t)threadInfo, &threadInfoCount) == KERN_SUCCESS) {
            threadBaseInfo = (thread_basic_info_t)threadInfo;
            if (!(threadBaseInfo->flags & TH_FLAGS_IDLE)) {
                integer_t cpuUsage = threadBaseInfo->cpu_usage / 10;
                if (cpuUsage > CPUMONITORRATE) {
                    //cup 消耗大于设置值时打印和记录堆栈
                    NSString *reStr = smStackOfThread(threads[i]);
                    SMCallStackModel *model = [[SMCallStackModel alloc] init];
                    model.stackStr = reStr;
                    //记录数据库中
                    [[[SMLagDB shareInstance] increaseWithStackModel:model] subscribeNext:^(id x) {}];
//                    NSLog(@"CPU useage overload thread stack：\n%@",reStr);
                }
            }
        }
    }
}
```

### **卡顿方法的栈信息**

当我们得到卡顿的时间点，就要立即拿到卡顿的堆栈，有两种方式一种是遍历栈帧，实现原理我在**iOS获取任意线程调用栈[8]**写的挺详细的，同时开源了代码 **RCBacktrace[9]**，另一种方式是通过Signal获取任意线程调用栈，实现原理我在**通过 Signal handling(信号处理)获取任意线程调用栈[10]**写了，代码在 **backtrace-swift[11]**，但这种方式在调试时比较麻烦，建议用第一种方式。

#### **参考资料**

[1]

iOS 保持界面流畅的技巧: _https://blog.ibireme.com/2015/11/12/smooth_user_interfaces_for_ios/_

[2]

YYFPSLabel: _https://github.com/ibireme/YYText/blob/master/Demo/YYTextDemo/YYFPSLabel.m_

[3]

iOS 实时卡顿监控: _https://simcast.com/?d=tanhao.me&s=bone&sw=17&tr=17122618650&oip=20.187.154.207&eol&adult=true_

[4]

GCDFetchFeed: _https://github.com/ming1016/GCDFetchFeed_

[5]

iOS 实时卡顿监控: _https://simcast.com/?d=tanhao.me&s=bone&sw=17&tr=17122627591&oip=20.187.154.207&eol&adult=true_

[6]

ANREye: _https://github.com/zixun/ANREye_

[7]

Matrix-iOS 卡顿监控: _https://cloud.tencent.com/developer/article/1427933_

[8]

iOS获取任意线程调用栈: _https://juejin.cn/post/6844903944842395656_

[9]

RCBacktrace: _https://github.com/woshiccm/RCBacktrace_

[10]

通过 Signal handling(信号处理)获取任意线程调用栈: _https://juejin.cn/post/6844903919617835021_

[11]

backtrace-swift: _https://github.com/woshiccm/backtrace-swift_

**-End-**
