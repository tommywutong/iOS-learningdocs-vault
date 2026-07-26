# Matrix for iOS/macOS 数据格式说明

## MatrixIssue

实现 `MatrixPluginListenerDelegate`，通过 `- (void)onReportIssue:(MatrixIssue *)issue` 获得监控插件返回的数据。

回调出来的 MatrixIssuse 里封装了监控数据，以下是 MatrixIssue 各个字段的说明：

* **issueTag**
	
	表明当前 issue 对象属于哪个 plugin；每个 plugin 的 tag 可以通过 `+[MatrixPlugin getTag]` 获得。
	
* **issueID**
	
	当前 issue 的唯一标识。
		
* **dataType & filePath & issueData**
	
	dataType 指明当前 issue 返回数据的数据类型，定义在 `EMatrixIssueDataType`。
	如果 dataType 为 `EMatrixIssueDataType_Data`，数据在 issueData 中；
	如果 dataType 为 `EMatrixIssueDataType_FilePath`，数据在 filePath 对应的文件中。
	
* **reportType**
	
	reportType 是由每个 plugin 自行定义的。
	
	在 WCCrashBlockMonitorPlugin 中：
	
	* reportType 为 `EMCrashBlockReportType_Crash` 时，说明当前 issue 中携带的数据为崩溃日志；
	* reportType 为 `EMCrashBlockReportType_Lag` 时，说明当前 issue 中携带的数据为卡顿日志。
	
* **customInfo**
	
	某些 issue 可能会携带一些附加信息。
	
**重要**

>处理完 MatrixIssue 之后，调用 `-[Matrix reportIssueComplete:success:]` 可以将 issue 对应的数据从本地进行删除。 

>如果没有调用 `-[Matrix reportIssueComplete:success:]`，那么日志将会在应用本地中存在着。

## WCCrashBlockMonitorPlugin 的数据

插件会通过 `- (void)onReportIssue:(MatrixIssue *)issue` 回调崩溃日志和卡顿日志。

#### 崩溃日志

当 MatrixIssue 对象的 issueTag 为 `+[WCCrashBlockMonitorPlugin getTag]`，reportType 为 `EMCrashBlockReportType_Crash`时，MatrixIssue 携带的数据为崩溃日志。

崩溃日志数据格式为 JSON：[示例](recource/crash-sample.txt)。

#### 卡顿日志

当 MatrixIssue 对象的 issueTag 为 `+[WCCrashBlockMonitorPlugin getTag]`，reportType 为 `EMCrashBlockReportType_Lag` 时，MatrixIssue 携带的数据为卡顿日志（除了 dumpType 为 2011时）。

卡顿日志数据格式为 JSON：[示例](recource/block-killed-lag-sample.txt)。

卡顿日志对应的 MatrixIssue 中，customInfo 带有说明信息：
	
* **`g_crash_block_monitor_custom_dump_type` "dumptype"**
	
	说明 MatrixIssue 中的卡顿数据所属的卡顿类型，一个 MatrixIssue 中的数据只属于一个卡顿类型，卡顿类型定义在 EDumpType；

* **`g_crash_block_monitor_custom_file_count` "filecount"**
	
	说明 MatrixIssue 中的 JSON 数据是由多少份卡顿日志组成的；

* **`g_crash_block_monitor_custom_report_id` "reportID"**
	
	当前 MatrixIssue 数据中包含的所有卡顿日志的 reportID，便于管理存储在本地的卡顿日志。

可以使用 **matrix/matrix-iOS/Script/ks2apple.py** 对 JSON 文件进行解析。

#### 耗电堆栈

当 MatrixIssue 对象的 issueTag 为 `+[WCCrashBlockMonitorPlugin getTag]`，reportType 为 `EMCrashBlockReportType_Lag` ，MatrixIssue 中的 customInfo 的 `dumptype` 为 `EDumpType_PowerConsume 2011` 时，MatrixIssue 携带的数据为耗电堆栈。

耗电堆栈数据格式为 JSON: [示例](recource/power-comsuming-stack.txt)。

可以使用 **matrix/matrix-iOS/Script/battery2apple.py** 对 JSON 文件进行解析。

## WCMemoryStatPlugin 的数据

插件会通过 `- (void)onReportIssue:(MatrixIssue *)issue` 回调爆内存时的内存分配和堆栈调用情况。

当 MatrixIssue 对象的 issueTag 为 `+[WCMemoryStatPlugin getTag]`时， MatrixIssue 携带的数据为爆内存数据。

爆内存数据格式为 JSON 格式：[示例](recource/oom-info-sample.txt)。

**重要**
>数据中 uuid 指地址对应的二进制的 uuid，offset 为在二进制符号的地址偏移。

```
 {
	"head": {
        "protocol_ver": 1,				# protocol version, current(version 1), required
		"phone": "oppo",				# string，device type, required
		"os_ver": "android-17",			# Android(api level), iPhone(iOS version), required
 		"launch_time": timestamp,		# launch time, unix timestamp, required
		"report_time": timestamp,		# report time, unix timestamp, required
		"app_uuid": uuid				# app uuid, required
 		// custom field
 		"uin": uin						# uin, optional
	},
	"items": [{
		"tag": "iOS_MemStat",
        "info": "",
		"scene": "WCTimeLine",			# FOOM Scene
		"name": "NSObject",				# class name
		"size": 123456,					# allocated memory size
		"count": 123,					# object count
		"stacks": [{
			"caller": "uuid@offset",	# caller who allocated the memory
			"size": 21313,				# total size
			"count": 123,				# object count
			"frames": [{
				"uuid": "uuid",
				"offset": 123456
			}]
		}]
	}]
 }
```

