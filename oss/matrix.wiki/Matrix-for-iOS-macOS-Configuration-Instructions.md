# Configuration Instructions of Matrix for iOS/macOS

## WCCrashBlockMonitorPlugin

`WCCrashBlockMonitorPlugin` is based on the [KSCrash] (https://github.com/kstenerud/KSCrash) framework and features crash capture and lag monitoring. The ability to capture crashes is consistent with the `KSCrash` framework. The principles of lag monitoring can be found in [iOS微信卡顿监控](https://github.com/Tencent/matrix/wiki/ios-wechat-blockmonitor-cn). The monitor return data format can be found in: [Matrix for iOS/macOS Data Format Description](https://github.com/Tencent/matrix/wiki/data-format-info-en).

`WCCrashBlockMonitorPlugin` can be customized with `WCCrashBlockMonitorConfig`. Sucn as:

```
WCCrashBlockMonitorConfig *crashBlockConfig = MyConfig;
WCCrashBlockMonitorPlugin *crashBlockPlugin = [[WCCrashBlockMonitorPlugin alloc] init];
crashBlockPlugin.pluginConfig = crashBlockConfig;
.....
[crashBlockPlugin start];
```

##### WCCrashBlockMointorConfig

Description of each configuration field of `WCCrashBlockMointorConfig`:

* **appVersion & appShortVersion**

	The custom version number in the retured monitor data. If not filled, the version number in the return data is automatically obtained from the bundle.

* **enableCrash**

	Whether to enable crash capture, the default value is **YES**; when set to **NO**, the plugin will not have crash capture capability.

* **enableBlockMonitor**
	
	Whether to enable lag monitoring, the default value is **YES**; when set to **NO**, the plugin will not have the lag monitoring capability.

* **blockMonitorDelegate**

	By implementing `blockMonitorDelegate`, you can get the events returned during the lag monitoring process, which gives you more precise control over the lag monitoring.

* **onHandleSignalCallBack**

	After getting the crash log, notify that a crash has occurred. **Use with caution: Do not have any memory operations in the running code in the callback, or it will easily cause another crash.**

* **onAppendAdditionalInfoCallBack**

	In the process of generating the crash log and the lag log, a callback is provided to write the custom data. Such as:

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

	The default is `EWCCrashBlockReportStrategy_All`.
	
	Set to `EWCCrashBlockReportStrategy_Auto`, the crash log will pass through the `onReportIssue:` callback after the next restart of the application; the lag log generated **on the same day** will pass through the `onReportIssue:` callback each time the application enters the foreground.
	
	Set to `EWCCrashBlockReportStrategy_All`, the crash log will pass through the `onReportIssue:` callback after the next restart of the application; **all** the lag log will pass through the `onReportIssue:` callback each time the application enters the foreground.
	
	Set to `EWCCrashBlockReportStrategy_Manual`, the `onReportIssue:` callback needs to be triggered manually, the interface is defined in `WCCrashBlockMonitorPlugin+Upload.h`.

```
typedef NS_ENUM(NSUInteger, EWCCrashBlockReportStrategy) {
    EWCCrashBlockReportStrategy_Default = 0, 
    EWCCrashBlockReportStrategy_All = 1,
    EWCCrashBlockReportStrategy_Manual = 2,
};
```

* **blockMonitorConfiguration**

	The configuration of the lag monitor, `WCBlockMonitorConfiguration` detailed configuration is shown in the next section.

#### WCBlockMonitorConfiguration

Description of each configuration field of `WCBlockMonitorConfiguration`:

* **runloopTimeOut**

	The unit is microseconds, the default value is **2000000**, which is 2 seconds;
	Defining the duration of the lag time, the Runloop blocking time exceeds runloopTimeOut and is considered a lag.

* **checkPeriodTime**

	The unit is microseconds, the default value is **1000000**, which is 1 second;
	Defines the period in which the child thread checks the state of the main thread Runloop.

* **bMainThreadHandle**

	The default value is **NO**; It's the time-consuming stack extraction function switch, set to YES to start the time-consuming stack extraction, the lag monitor will periodically get the main thread stack, the acquisition frequency and the number of saves are determined by the two parameters perStackInterval and mainThreadCount.

* **perStackInterval**

	The unit is microseconds, the default value is **50000**, which is 50 milliseconds;
	Defines the interval at which the main thread stack is obtained.

* **mainThreadCount**

	The default is **10**;
	Defines the number of saves to the most recent main thread stack.

* **limitCPUPercent**

	The default value is **80**;
	If the single core CPU takes up more than `limitCPUPercent`, it is considered that the CPU is too high.Set to 80, then on a dual-core machine, when the CPU occupies more than 160%, the lag monitor considers the current CPU too high and then generates a snapshot of the thread.

#### Lag Type

In the JSON log generated by lag monitor, there is a `dump_type` field indicating the type of the lag to which the current log belongs. The lag type has:

* **EDumpType_MainThreadBlock 2001**

	The main thread is stuck when the application is in the foreground.

* **EDumpType_BackgroundMainThreadBlock 2002**

	The main thread is stuck when the application is in the background.

* **EDumpType_CPUBlock 2003**

	It is detected that the current application consumes too much CPU.

* **EDumpType_LaunchBlock 2007**

	**Within 5 seconds** of the application launching, the main thread stuck.

* **EDumpType_CPUIntervalHigh 2008**

	It was detected that the application was more than **80% CPU** in the foreground for **one minute**.
	*EDumpType_CPUIntervalHigh is deprecated after Matrix adding the power-consuming monitor.*
	
* **EDumpType_BlockThreadTooMuch 2009**

	The type of lag that is subdivided frome the `EDumpType_MainThreadBlock` and `EDumpType_BackgroundMainThreadBlock`, with more than **64** threads when the lag monitor detected the lag.

* **EDumpType_BlockAndBeKilled 2010**

	When the application restarts, it is detected that the last application shutdown is because the main thread is stuck causing the application to be forcibly closed, and the lag monitor marks the lag before the application is closed as `EDumpType_BlockAndBeKilled`.

* **EDumpType_PowerConsume 2011**

	The calltree that generated by the power-consuming monitor. It consist of the stacks that consume CPU in one minitue.
	
## WCMemoryStatPlugin

`WCMemoryStatPlugin` is a performance-optimized out-of-memory monitoring tool. The principles of out-of-memory monitoring can be found in [iOS微信内存监控](https://mp.weixin.qq.com/s/CiqMlEIp1Ir2EJSDGgMooQ). The monitor return data format can be found in: [Matrix for iOS/macOS Data Format Description](https://github.com/Tencent/matrix/wiki/data-format-info-en).

#### Important

> `WCMemoryStatPlugin` uses private API during monitoring to monitor the use of virtual memory outside of the `malloc` memory pool.
> 
> In Release mode, the use of the private API is blocked, avoiding the risk of audit of App Store.
> 
> If you want out-of-memory monitor to fully monitor the memory stack usage, compile with Debug mode or manually define the macro `USE_PRIVATE_API` in the code.

#### Performance

`WCMemoryStatPlugin` has a CPU usage of about 13% when running in the iPhone 6 Plus. This is related to the amount of data generated by the application. The amount of data generated is large, which may result in a slightly higher CPU usage.

`WCMemoryStatPlugin` uses `mmap` to maps files to memory, with a around 20MB memory occupation.

#### Configuration
 
The filtering policy for `WCMemoryStatPlugin` monitoring objects and stacks can be configured via `WCMemoryStatConfig`. Such as:

```
WCMemoryStatPlugin *memStatConfig = MyConfig;
WCMemoryStatPlugin *memStatPlugin = [[WCMemoryStatPlugin alloc] init];
memStatPlugin.pluginConfig = memStatConfig;
......
[memStatPlugin start];
```

Description of each configuration field of `WCMemoryStatConfig`:

* **skipMinMallocSize**

	The default value is **PAGE_SIZE**;
	If the object allocates memory size greater than or equal to `skipMinMallocSize`, the allocation event of the object will be tracked.
	
* **skipMaxStackDepth**
	
	The default value is **8**; 
	If the allocated memory size is less than `skipMinMallocSize`, and in the front `skipMaxStackDepth` addresses of the obtained stack, there is a currently application symbol, then this allocation event will be tracked.
	
## Get the program log of Matrix

Set `MatrixAdaptor` delegate and implement the delegate; the logs generated in `Matrix` are called back via the `MatrixAdapterDelegate`.

```
// Set delegate
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