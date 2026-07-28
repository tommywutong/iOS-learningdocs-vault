---
title: 在 iOS 上实现主线程看门狗
source: Jesse Squires
source_key: jessesquires
source_url: 'https://www.jessesquires.com/blog/2022/08/11/implementing-a-main-thread-watchdog-on-ios/'
original_language: en
published: 2022-08-11
status: active
license: © 2014–2026 Jesse Squires → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:262832ba902e21c2'
translated: true
---

> 原文：[Implementing a main thread watchdog on iOS](https://www.jessesquires.com/blog/2022/08/11/implementing-a-main-thread-watchdog-on-ios/)　·　Jesse Squires

在 iOS 上，操作系统会采用看门狗（watchdog）机制来监控并终止无响应的 App。如果你的 App 阻塞主线程（main thread）的时间过长，系统就会将其杀死。在崩溃报告中，你可以通过终止原因代码 `0x8badf00d`（“ate bad food”）来识别[看门狗终止](https://developer.apple.com/documentation/xcode/addressing-watchdog-terminations)。

这对于判断终止发生的_原因_很有帮助——即你的 App 长时间阻塞了主线程。然而，它并不总能回答（在你的代码中）_什么_实际导致了终止。来自 Apple 的[应对看门狗终止指南](https://developer.apple.com/documentation/xcode/addressing-watchdog-terminations)指出：

> 不过，主线程的回溯（backtrace）并不总能包含问题的根源。例如，假设你的 App 恰好需要 4 秒来完成一个任务，而总的挂钟时间为 5 秒。当看门狗在 5 秒后终止 App 时，耗时 4 秒的代码不会出现在回溯中，因为它已经完成，尽管它耗尽了几乎全部时间配额。崩溃报告反而记录了看门狗终止 App 时正在执行的回溯帧，即使这些记录的回溯帧并非问题的根源。

为了克服这类场景固有的局限性，我们可以编写自己的主线程看门狗，并在 App 中添加自定义日志记录，以帮助诊断 `0x8badf00d` 终止的根本原因。实际上，Core Foundation 中的 API 让这件事变得相对简单。我们可以使用 [`CFRunLoopObserver`](https://developer.apple.com/documentation/corefoundation/cfrunloopobserver-ri3)。下面的代码实现了一个简单的运行循环观察者（run loop observer），主要基于 [Justin Spahr-Summers](https://github.com/jspahrsummers) 编写的[这个 gist](https://gist.github.com/jspahrsummers/419266f5231832602bec)。

```
// WatchdogRunLoopObserver.h

@protocol WatchdogRunLoopObserverDelegate <NSObject>

- (void)runLoopDidStallWithDuration:(NSTimeInterval)duration;

@end

@interface WatchdogRunLoopObserver : NSObject

@property (nonatomic, weak, nullable) id<WatchdogRunLoopObserverDelegate> delegate;

- (instancetype)init;

- (instancetype)initWithRunLoop:(CFRunLoopRef)runLoop stallingThreshold:(NSTimeInterval)threshold;

- (void)start;

- (void)stop;
@end
```

```
// WatchdogRunLoopObserver.m

#import "WatchdogRunLoopObserver.h"
#include <mach/mach_time.h>

static const NSTimeInterval DefaultStallingThreshold = 4;

@interface WatchdogRunLoopObserver ()

@property (nonatomic, assign, readonly) CFRunLoopRef runLoop;
@property (nonatomic, assign, readonly) CFRunLoopObserverRef observer;
@property (nonatomic, assign, readonly) NSTimeInterval threshold;
@property (nonatomic, assign) uint64_t startTime;

@end

@implementation WatchdogRunLoopObserver

- (instancetype)init {
    return [self initWithRunLoop:CFRunLoopGetMain()
               stallingThreshold:DefaultStallingThreshold];
}

- (instancetype)initWithRunLoop:(CFRunLoopRef)runLoop
              stallingThreshold:(NSTimeInterval)threshold {
    NSParameterAssert(runLoop != NULL);
    NSParameterAssert(threshold > 0);

    self = [super init];
    if (self == nil) {
        return nil;
    }

    _runLoop = (CFRunLoopRef)CFRetain(runLoop);
    _threshold = threshold;

    // 预先计算时间基准信息。
    mach_timebase_info_data_t timebase;
    mach_timebase_info(&timebase);

    NSTimeInterval secondsPerMachTime = timebase.numer / timebase.denom / 1e9;

    __weak typeof(self) weakSelf = self;

    // 以极低的顺序观察，以便即使在高优先级操作（如 UI 重绘或动画）中
    // 也能捕获停滞。
    _observer = CFRunLoopObserverCreateWithHandler(NULL, kCFRunLoopAllActivities, YES, INT_MIN,
                                                   ^(CFRunLoopObserverRef observer, CFRunLoopActivity activity) {
        typeof(self) strongSelf = weakSelf;
        if (!strongSelf) {
            return;
        }

        switch (activity) {
                // 我们认为的一次“迭代”可能从这几个事件中的任何一个开始。
            case kCFRunLoopEntry:
            case kCFRunLoopBeforeTimers:
            case kCFRunLoopAfterWaiting:
            case kCFRunLoopBeforeSources:
                if (strongSelf.startTime == 0) {
                    strongSelf.startTime = mach_absolute_time();
                }
                break;

            case kCFRunLoopBeforeWaiting:
            case kCFRunLoopExit: {
                uint64_t endTime = mach_absolute_time();
                if (strongSelf.startTime <= 0) {
                    break;
                }

                uint64_t elapsed = endTime - strongSelf.startTime;

                NSTimeInterval duration = elapsed * secondsPerMachTime;
                if (duration > strongSelf.threshold) {
                    [strongSelf iterationStalledWithDuration:duration];
                }

                strongSelf.startTime = 0;
                break;
            }

            default:
                NSAssert(NO, @"WatchdogRunLoopObserver should not have been triggered for activity %i", (int)activity);
        }
    });

    if (_observer == NULL) {
        return nil;
    }

    return self;
}

- (void)dealloc {
    if (_observer != NULL) {
        CFRunLoopObserverInvalidate(_observer);

        CFRelease(_observer);
        _observer = NULL;
    }

    if (_runLoop != NULL) {
        CFRelease(_runLoop);
        _runLoop = NULL;
    }
}

- (void)start {
    CFRunLoopAddObserver(self.runLoop, self.observer, kCFRunLoopCommonModes);
}

- (void)stop {
    CFRunLoopRemoveObserver(self.runLoop, self.observer, kCFRunLoopCommonModes);
}

- (void)iterationStalledWithDuration:(NSTimeInterval)duration {
    [self.delegate runLoopDidStallWithDuration:duration];
}

@end
```

这个类 `WatchdogRunLoopObserver` 本质上是将 `CFRunLoopObserver` 包装成一个更友好、更易用的 API。它会计算每次运行循环迭代所花费的时间，并在超过你指定的阈值时通知其 `delegate`（委托）。它默认使用 4 秒的阈值。

我们可以将其包装成一个更友好的 Swift API。

```
final public class Watchdog: NSObject, WatchdogRunLoopObserverDelegate {
    @objc
    public static let shared = Watchdog()

    private let observer = WatchdogRunLoopObserver()

    private var isStarted = false

    override private init() {
        super.init()
        self.observer.delegate = self
    }

    deinit {
        stop()
    }

    public func start() {
        if isStarted {
            return
        }

        print("[Watchdog] started")
        observer.start()
        isStarted = true
    }

    public func stop() {
        print("[Watchdog] stopped")
        observer.stop()
    }

    // MARK: WatchdogRunLoopObserverDelegate

    public func runLoopDidStall(withDuration duration: TimeInterval) {
        // TODO: 在这里实现你的自定义日志记录
        //    - 当前正在运行什么任务？
        //    - 哪个视图控制器（view controller）位于屏幕最前？
        print("🚫 ⚠️ [Watchdog] main thread blocked for \(duration) seconds")
    }
}
```

然后，在 App 启动时或在任何你需要开始跟踪潜在主线程阻塞的地方，你可以启动和停止共享的看门狗。

```
Watchdog.shared.start()

Watchdog.shared.stop()
```

在 `runLoopDidStall(withDuration:)` 委托回调中，你可以实现自定义日志记录——当前 App 中正在发生什么、哪个视图控制器位于屏幕最前等。你应该包含任何相关的上下文信息，以帮助你诊断可能是什么阻塞了主线程。我已将所有这些代码以及一个简单的示例 App 放在 [GitHub](https://github.com/jessesquires/ios-watchdog) 上。

这是一种相对轻量级的跟踪这些问题的方法。有关包含报告完整堆栈跟踪的、更复杂的实现，请参阅[这篇 Facebook 工程博客文章](https://engineering.fb.com/2015/06/25/ios/delivering-high-scroll-performance/)及其随附的 [gist](https://gist.github.com/clementgenzmer/4ff6c51224089cc65e9b)。
