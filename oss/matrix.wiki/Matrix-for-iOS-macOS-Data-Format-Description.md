# Matrix for iOS/macOS Data Format Description

## MatrixIssue

Implement `MatrixPluginListenerDelegate` and get the data returned by the monitoring plugin via `- (void)onReportIssue:(MatrixIssue *)issue`.

The monitoring data is encapsulated in the `MatrixIssuse`. The following is a description of each of the `MatrixIssue` fields:

* **issueTag**
	
	Indicates which plugin the current issue object belongs to; the tag for each plugin can get by `+[MatrixPlugin getTag]`.
	
* **issueID**
	
	The unique identifier of the current issue.
		
* **dataType & filePath & issueData**
	
	`dataType` indicates the data type of the current issue's data, defined in `EMatrixIssueDataType`.
	If the `dataType` is `EMatrixIssueDataType_Data`, the data is in `issueData`;
	If the `dataType` is `EMatrixIssueDataType_FilePath`, the data is in the file corresponding to `filePath`.
	
* **reportType**
	
	The `reportType` is defined by each plugin.
	
	In `WCCrashBlockMonitorPlugin`:
	
	* If the `reportType` is `EMCrashBlockReportType_Crash`, the data carried in the current issue is the crash log;
	* If the `reportType` is `EMCrashBlockReportType_Lag`, the data carried in the current issue is the lag log.
	
* **customInfo**
	
	Some issues may carry some additional information.
	
**Important**

>After processing `MatrixIssue`, call `-[Matrix reportIssueComplete:success:]` to delete the data corresponding to the issue locally.

>If `-[Matrix reportIssueComplete:success:]` is not called, the log will still exist in the application local.

## Data of WCCrashBlockMonitorPlugin

The plugin will call back the crash log and the lag log via `- (void)onReportIssue:(MatrixIssue *)issue`.

#### Crash Log

When the `issueTag` of the `MatrixIssue` object is `+[WCCrashBlockMonitorPlugin getTag]` and the `reportType` is `EMCrashBlockReportType_Crash`, the data carried by `MatrixIssue` is the crash log.

The crash log data format is **JSON**: [sample](recource/crash-sample.txt).

#### Lag Log

When the `issueTag` of the `MatrixIssue` object is `+[WCCrashBlockMonitorPlugin getTag]` and the `reportType` is `EMCrashBlockReportType_Lag`, the data carried by `MatrixIssue` is the lag log (except `dumptype` is 2011)

The lag log data format is **JSON**: [sample](recource/block-killed-lag-sample.txt).

In the `MatrixIssue` corresponding to the lag log, `customInfo` has additional info:
	
* **`g_crash_block_monitor_custom_dump_type` "dumptype"**
	
	Indicate the type of the lag data in the `MatrixIssue` belongs to. The data in a `MatrixIssue` belongs to only one type of lag, and the type of the lag is defined in `EDumpType`;

* **`g_crash_block_monitor_custom_file_count` "filecount"**
	
	Indicate how many files of the JSON data in the `MatrixIssue` are composed of;

* **`g_crash_block_monitor_custom_report_id` "reportID"**
	
	The `reportID` of all the lag logs contained in the current `MatrixIssue` data, `reportID` makes it easy to manage the lag logs.

Use **matrix/matrix-iOS/Script/ks2apple.py** to parse the JSON to a plain text.

#### Power-Consuming Stack

When the `issueTag` of the `MatrixIssue` object is `+[WCCrashBlockMonitorPlugin getTag]` and the `reportType` is `EMCrashBlockReportType_Lag`, and the `dumpType` of the `customInfo` in `MatrixIssue` is `EDumpType_PowerConsume 2011`, the data carried by `MatrixIssue` is the power-consuming stack.

The Power-Consuming Stack format is **JSON**: [sample](recource/power-comsuming-stack.txt).

Use **matrix/matrix-iOS/Script/battery2apple.py** to parse the JSON to a plain text.

## Data of WCMemoryStatPlugin

The plugin will call back memory allocation and callstack related to a out-of-memory event with `- (void)onReportIssue:(MatrixIssue *)issue`.

When the `issueTag` of the `MatrixIssue` object is `+[WCMemoryStatPlugin getTag]`, the data carried by `MatrixIssue` is out-of-memory data.

The out-of-memory report data format is **JSON**: [sample](recource/oom-info-sample.txt). 

**Important**
>In the data, `uuid` refers to the binary uuid corresponding to the address, and `offset` is the address offset of the symbol in the binary.

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

