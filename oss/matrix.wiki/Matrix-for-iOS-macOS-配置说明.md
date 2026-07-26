# Matrix for iOS/macOS 配置说明

## WCCrashBlockMonitorPlugin

WCCrashBlockMonitorPlugin 基于 [KSCrash](https://github.com/kstenerud/KSCrash) 框架开发，具有崩溃捕捉和卡顿监控能力。崩溃捕捉的能力和 KSCrash 框架一致，卡顿监控的原理可以参见：[iOS微信卡顿监控](https://github.com/Tencent/matrix/wiki/Matrix-for-iOS-macOS-%E5%8D%A1%E9%A1%BF%E7%9B%91%E6%8E%A7%E5%8E%9F%E7%90%86)。 监控返回数据格式可以参见：[Matrix for iOS/macOS 数据格式说明](https://github.com/Tencent/matrix/wiki/Matrix-for-iOS-macOS-%E6%95%B0%E6%8D%AE%E6%A0%BC%E5%BC%8F%E8%AF%B4%E6%98%8E)。


可以通过 WCCrashBlockMonitorConfig 对 WCCrashBlockMonitorPlugin 的监控能力进行定制。 如：

```
WCCrashBlockMonitorConfig *crashBlockConfig = MyConfig;
WCCrashBlockMonitorPlugin *crashBlockPlugin = [[WCCrashBlockMonitorPlugin alloc] init];
crashBlockPlugin.pluginConfig = crashBlockConfig;
.....
[crashBlockPlugin start];
```

##### WCCrashBlockMointorConfig

WCCrashBlockMointorConfig 各个配置字段的说明：

* **appVersion & appShortVersion**

	定制监控返回数据中的版本号，如果不填，返回数据中的版本号会自动从 bundle 中获取。

* **enableCrash**

	是否开启崩溃监控，默认值为 YES ；设置为 NO，plugin 将不会具有崩溃捕捉能力。

* **enableBlockMonitor**
	
	是否开启卡顿监控，默认值为 YES ；设置为 NO，plugin 将不会具有卡顿监控能力。

* **blockMonitorDelegate**

	实现 blockMonitorDelegate，可以获得卡顿监控过程中返回的事件，从而对卡顿监控有更精确的掌控。

* **onHandleSignalCallBack**

	获得崩溃日志之后，通知有崩溃产生。**慎用：回调中的运行代码中不要有任何内存操作，不然容易引起再次崩溃。**

* **onAppendAdditionalInfoCallBack**

	在生成崩溃日志和卡顿日志的过程中，提供回调写入自定义数据。 如：

```
void kscrash_crashCallback(const KSCrashReportWriter *writer)
{
	    writer->beginObject(writer, "WeChat");
	    
	    writer->addUIntegerElement(writer, "uin", 1000);
	    writer->addStringElement(writer, "commit_id", "2019-1-1");
	    writer->addBooleanElement(writer, "bool", NO);
	    
	    writer->beginArray(writer, "log");
	    for (int i = 1; i < 10; i++) {
	    	writer->addStringElement(writer, nil, "123");
	    }
	    writer->endContainer(writer);
	    
	    writer->endContainer(writer);
}
```

* **reportStrategy**

	默认是 EWCCrashBlockReportStrategy_All.
	
	设置为 EWCCrashBlockReportStrategy_Auto，崩溃日志在应用下次重启之后会通过 `onReportIssue:` 回调；卡顿日志在应用每次进前台时，将当天一种卡顿类型的日志通过 `onReportIssue:` 回调。
	
	设置为 EWCCrashBlockReportStrategy_All，崩溃日志在应用下次重启之后会通过 `onReportIssue:` 回调；卡顿日志在应用每次进前台时，将全部卡顿日志通过 `onReportIssue:` 回调。
	
	设置为 EWCCrashBlockReportStrategy_Manual，`onReportIssue:`的回调需要主动进行触发，触发回调接口定义在 `WCCrashBlockMonitorPlugin+Upload.h`。

```
typedef NS_ENUM(NSUInteger, EWCCrashBlockReportStrategy) {
    EWCCrashBlockReportStrategy_Default = 0, 
    EWCCrashBlockReportStrategy_All = 1,
    EWCCrashBlockReportStrategy_Manual = 2,
};
```

* **blockMonitorConfiguration**

	卡顿监控的参数配置，WCBlockMonitorConfiguration 详细配置见下节。

#### WCBlockMonitorConfiguration

WCBlockMonitorConfiguration 的各个配置字段说明：

* **runloopTimeOut**

	单位是微秒，默认值是 2000000，即 2 秒；
	定义卡顿时长，Runloop 阻塞时间超过 runloopTimeOut 即认为是卡顿。

* **checkPeriodTime**

	单位是微秒，默认值是 1000000，即 1 秒；
	定义子线程检查主线程 Runloop 状态的周期。

* **bMainThreadHandle**

	默认值是 NO；耗时堆栈提取功能的开关，设置为 YES 即开启耗时堆栈提取，卡顿监控会定时获取主线程堆栈，获取频率以及保存个数由 perStackInterval 和 mainThreadCount 这两个参数决定。

* **perStackInterval**

	单位是微秒，默认值是 50000，即 50 毫秒；
	定义获取主线程堆栈的间隔。

* **mainThreadCount**

	默认值是 10 个；
	定义保存最近主线程堆栈的个数。

* **limitCPUPercent**

	默认值是 80；
	定义认为单核CPU占用超过多少即认为是CPU过高。设置为 80，那么在双核机器上，当 CPU 占用超过 160% 的时候，卡顿监控就会认为当前CPU过高，然后生成 CPU 过高的线程快照。

#### 卡顿类型

在卡顿监控生成的 JSON 日志中，有 dump_type 字段表明当前日志所属的卡顿类型。卡顿类型有：

* **EDumpType_MainThreadBlock 2001**

	前台主线程卡顿；应用在前台时主线程 Runloop 处理事件超时了。

* **EDumpType_BackgroundMainThreadBlock 2002**

	后台主线程卡顿；应用在后台时主线程 Runloop 处理事件超时了。

* **EDumpType_CPUBlock 2003**

	CPU过高堆栈；检测到当前应用占用CPU过高。

* **EDumpType_LaunchBlock 2007**

	启动卡顿；在应用启动 5 秒内，发生的主线程卡顿，归为启动卡顿。

* **EDumpType_CPUIntervalHigh 2008**

	CPU时间段内过高堆栈；检测到应用在前台连续一分钟 CPU 超过80%。
	
	*EDumpType_CPUIntervalHigh 在 Matrix 加入耗电监控后已经弃用。*

* **EDumpType_BlockThreadTooMuch 2009**

	线程过多卡顿；从前台和后台主线程卡顿中细分出来的卡顿类型，将卡顿时线程数超过64的卡顿归为线程过多卡顿。

* **EDumpType_BlockAndBeKilled 2010**

	卡死卡顿；当应用重启时，检测到上次应用关闭是因为主线程卡顿导致应用被强制关闭，卡顿监控会把应用关闭前的卡顿标记为卡死卡顿。

* **EDumpType_PowerConsume 2011**

	耗电堆栈；检测到应用连续一分钟 CPU 占用超过80%，将一分钟内的耗 CPU 堆栈组合起来成为耗电堆栈。

## WCMemoryStatPlugin

WCMemoryStatPlugin 是一款性能优化到极致的内存监控工具。关于内存监控的原理，可参见：[iOS微信内存监控](https://mp.weixin.qq.com/s/CiqMlEIp1Ir2EJSDGgMooQ)。监控返回的数据格式，可参见：[Matrix for iOS/macOS 数据格式说明](https://github.com/Tencent/matrix/wiki/Matrix-for-iOS-macOS-%E6%95%B0%E6%8D%AE%E6%A0%BC%E5%BC%8F%E8%AF%B4%E6%98%8E)。

#### 重要

> WCMemoryStatPlugin 在监控过程中会使用到私有 API，用来监控 malloc 内存池以外的虚拟内存的使用。
> 
> 在 Release 模式下，会将私有 API 的使用屏蔽，避免 App Store 审核风险。
> 
> 如果要让内存监控完整监控内存堆栈使用，请使用 Debug 模式进行编译，或者手动打开 `USE_PRIVATE_API` 的宏定义。

#### 性能

内存监控工具在 iPhone 6 Plus 运行时 CPU 占用率为 13% 左右，这跟应用产生的数据量相关，产生的数据量大，可能会导致 CPU 占用率稍微偏高。

内存监控的数据用 mmap 方式把文件映射到内存，内存占用量在 20MB 左右。

#### 配置
 
可以通过 WCMemoryStatConfig 对 WCMemoryStatPlugin 监控堆栈和对象时的过滤策略进行配置。如：

```
WCMemoryStatPlugin *memStatConfig = MyConfig;
WCMemoryStatPlugin *memStatPlugin = [[WCMemoryStatPlugin alloc] init];
memStatPlugin.pluginConfig = memStatConfig;
......
[memStatPlugin start];
```

WCMemoryStatConfig 各个配置字段的说明：

* **skipMinMallocSize**

	默认值是 PAGE_SIZE；
	对象分配内存大小大于等于 skipMinMallocSize 将会记录跟踪。
	
* **skipMaxStackDepth**
	
	默认值是 8；
	如果分配内存大小小于 skipMinMallocSize，并且获取的堆栈在前 skipMaxStackDepth 个地址里，存在当前应用的符号，那么这次分配事件会被记录跟踪。

## 获得 Matrix 组件输出的日志

设置 MatrixAdaptor 对象的 delegate，并将其实现；Matrix 中的日志会通过 MatrixAdapterDelegate 回调。

```
// 设置 delegate 
#import <Matrix/MatrixAdapter.h>

[MatrixAdapter sharedInstance].delegate = self;

....

// MatrixAdapterDelegate

- (BOOL)matrixShouldLog:(MXLogLevel)level
{
    return [MyApp shouldLog:level];
}

- (void)matrixLog:(MXLogLevel)logLevel
           module:(const char *)module
             file:(const char *)file
             line:(int)line
         funcName:(const char *)funcName
          message:(NSString *)message
{
    [MyApp logWithLevel:level module:module errorCode:0
						  file:file line:line func:funcName message:message];
}

```

