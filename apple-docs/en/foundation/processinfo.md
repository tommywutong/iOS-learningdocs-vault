---
title: ProcessInfo
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/processinfo
source_url: 'https://developer.apple.com/documentation/foundation/processinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/processinfo.json'
content_hash: 'sha256:96d29e6cf60464fa'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# ProcessInfo

<sub>Class</sub>

A collection of information about the current process.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class ProcessInfo
```

## Overview

Each process has a single, shared [ProcessInfo](processinfo.md) object known as a _process information agent_ that can return information such as arguments, environment variables, host name, and process name. The [processInfo](processinfo/processinfo.md) class method returns the shared agent for the current process. For example, the following line returns the [ProcessInfo](processinfo.md) object, which then provides the name of the current process:

**Swift**

```swift
let processName = ProcessInfo.processInfo.processName
```

**Objective-C**

```objc
NSString *processName = [[NSProcessInfo processInfo] processName];
```

> [!note] Note
> [ProcessInfo](processinfo.md) is thread-safe in macOS 10.7 and later.

The [ProcessInfo](processinfo.md) class also includes the [operatingSystemVersion](processinfo/operatingsystemversion.md) property, which returns an [OperatingSystemVersion](operatingsystemversion.md) structure identifying the operating system version on which the process is executing.

[ProcessInfo](processinfo.md) objects attempt to interpret environment variables and command-line arguments in the user’s default C string encoding if they can’t convert to Unicode as UTF-8 strings. If neither the Unicode nor C string conversion works, the [ProcessInfo](processinfo.md) object ignores these values.

### Manage Activities

The system has heuristics to improve battery life, performance, and responsiveness of applications for the benefit of the user. You can use the following methods to manage _activities_ that give hints to the system that your application has special requirements:

- [- beginActivityWithOptions:reason:](<processinfo/beginactivity(options_reason_).md>)
- [- endActivity:](<processinfo/endactivity(__).md>)
- [- performActivityWithOptions:reason:usingBlock:](<processinfo/performactivity(options_reason_using_).md>)

In response to creating an activity, the system disables some or all of the heuristics so your application can finish quickly while still providing responsive behavior if the user needs it.

You use activities when your application performs a long-running operation. If the activity can take different amounts of time (for example, calculating the next move in a chess game), it should use this API to ensure correct behavior when the amount of data or the capabilities of the user’s computer varies. Activities fall into two major categories:

- _User-initiated_ activities are explicitly started by the user. Examples include exporting or downloading a user-specified file.
- _Background_ activities perform the normal operations of your application and aren’t explicitly started by the user. Examples include autosaving, indexing, and automatic downloading of files.

In addition, if your application requires high priority input/output (I/O), you can include the [NSActivityLatencyCritical](processinfo/activityoptions/latencycritical.md) flag (using a bitwise `OR`). You should only use this flag for activities like audio or video recording that require high priority I/O.

If your activity takes place synchronously inside an event callback on the main thread, you don’t need to use this API.

Be aware that failing to end these activities for an extended period of time can have significant negative impacts on the performance of your user’s computer, so be sure to use only the minimum amount of time required. User preferences may override your application’s request.

You can also use this API to control automatic termination or sudden termination (see [Support Sudden Termination](processinfo.md#Support-Sudden-Termination)). For example, the following code brackets the work to protect it from sudden termination:

**Swift**

```swift
let activity = ProcessInfo.processInfo.beginActivity(
    options: .automaticTerminationDisabled, 
    reason: "Good Reason")
// Perform some work.
ProcessInfo.processInfo.endActivity(activity)
```

**Objective-C**

```objc
id activity = [[NSProcessInfo processInfo] beginActivityWithOptions:NSActivityAutomaticTerminationDisabled reason:@"Good Reason"];
// Perform some work.
[[NSProcessInfo processInfo] endActivity:activity];
```

The above example is equivalent to the following code, which uses the [- disableAutomaticTermination:](<processinfo/disableautomatictermination(__).md>) method:

**Swift**

```swift
ProcessInfo.processInfo.disableAutomaticTermination("Good Reason")
// Perform some work.
ProcessInfo.processInfo.enableAutomaticTermination("Good Reason")
```

**Objective-C**

```objc
[[NSProcessInfo processInfo] disableAutomaticTermination:@"Good Reason"];
// Perform some work.
[[NSProcessInfo processInfo] enableAutomaticTermination:@"Good Reason"];
```

Because this API returns an object, it may be easier to pair begins and ends than when using the automatic termination API. If your app deallocates the object before the [- endActivity:](<processinfo/endactivity(__).md>) call, the activity ends automatically.

This API also provides a mechanism to disable system-wide idle sleep and display idle sleep. These can have a large impact on the user experience, so be careful to end activities that disable sleep (including [NSActivityUserInitiated](processinfo/activityoptions/userinitiated.md)).

### Support Sudden Termination

macOS 10.6 and later includes a mechanism that allows the system to log out or shut down more quickly by, whenever possible, killing applications instead of requesting that they quit themselves.

Your application can enable this capability on a global basis and then manually override its availability during actions that could cause data corruption or a poor user experience by allowing sudden termination.

Alternatively, your application can manually enable and disable this functionality. Creating a process assigns a counter that indicates if the process is safe to terminate. You decrement and increment the counter using the methods [- enableSuddenTermination](<processinfo/enablesuddentermination().md>) and [- disableSuddenTermination](<processinfo/disablesuddentermination().md>). A value of `0` enables the system to terminate the process without first sending a notification or event.

Your application can support sudden termination upon launch by adding a key to the application’s `Info.plist` file. If the [NSSupportsSuddenTermination](../bundleresources/information-property-list/nssupportssuddentermination.md) key exists in the `Info.plist` file and has a value of [true](../swift/true.md), it’s the equivalent of calling [- enableSuddenTermination](<processinfo/enablesuddentermination().md>) during your application launch. This allows the system to terminate the process immediately. You can still override this behavior by invoking [- disableSuddenTermination](<processinfo/disablesuddentermination().md>).

Typically, you disable sudden termination whenever your app defers work that the app must complete before it terminates. If, for example, your app defers writing data to disk and enables sudden termination, you should bracket the sensitive operations with a call to [- disableSuddenTermination](<processinfo/disablesuddentermination().md>), perform the necessary operations, and then send a balancing [- enableSuddenTermination](<processinfo/enablesuddentermination().md>) message.

In agents or daemon executables that don’t depend on AppKit, you can manually invoke [- enableSuddenTermination](<processinfo/enablesuddentermination().md>) right away. You can then use the enable and disable methods whenever the process has work it must do before it terminates.

Some AppKit functionality automatically disables sudden termination on a temporary basis to ensure data integrity.

- [UserDefaults](userdefaults.md) temporarily disables sudden termination to prevent the process from terminating between the time at which it sets the default and the time at which it writes the preferences file — including that default — to disk.
- [NSDocument](../appkit/nsdocument.md) temporarily disables sudden termination to prevent the process from terminating between the time at which the user has made a change to a document and the time at which [NSDocument](../appkit/nsdocument.md) writes the user’s change to disk.

> [!tip] Tip
> You can determine the value of the sudden termination using the following LLDB command.
>
> ```objc
> print (long)[[NSClassFromString(@"NSProcessInfo") processInfo] _suddenTerminationDisablingCount]
> ```
>
> Don’t attempt to invoke or override `suddenTerminationDisablingCount` (a private method) in your application. It’s there for this debugging purpose and may disappear at any time.

### Monitor Thermal State to Adjust App Performance

_Thermal state_ indicates the level of heat generated by logic components as they run apps. As the thermal state increases, the system decreases heat by reducing the speed of the processors. Optimize your app’s performance by monitoring the thermal state and reducing system usage as the thermal state increases. Query the current state with [thermalState](processinfo/thermalstate-swift.property.md) to determine if your app needs to reduce system usage. You can register the [NSProcessInfoThermalStateDidChangeNotification](processinfo/thermalstatedidchangenotification.md) for notifications of a change in thermal state. For recommended actions, see [ThermalState](processinfo/thermalstate-swift.enum.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting the process-information agent

- [processInfo](processinfo/processinfo.md) — Returns the process information agent for the process.

### Accessing process information

- [arguments](processinfo/arguments.md) — Array of strings with the command-line arguments for the process.
- [environment](processinfo/environment.md) — The variable names (keys) and their values in the environment from which the process was launched.
- [globallyUniqueString](processinfo/globallyuniquestring.md) — Global unique identifier for the process.
- [macCatalystApp](processinfo/ismaccatalystapp.md) — A Boolean value that indicates whether the process originated as an iOS app and runs on macOS.
- [iOSAppOnMac](processinfo/isiosapponmac.md) — A Boolean value that indicates whether the process is an iPhone or iPad app running on a Mac.
- [iOSAppOnVision](processinfo/isiosapponvision.md) — A Boolean value that indicates whether the process is an iPhone or iPad app running on visionOS.
- [processIdentifier](processinfo/processidentifier.md) — The identifier of the process (often called process ID).
- [processName](processinfo/processname.md) — The name of the process.

### Accessing user information

- [userName](processinfo/username.md) — Returns the account name of the current user.
- [fullUserName](processinfo/fullusername.md) — Returns the full name of the current user.

### Working with sudden application termination

- [- disableSuddenTermination](<processinfo/disablesuddentermination().md>) — Disables the application for quickly killing using sudden termination.
- [- enableSuddenTermination](<processinfo/enablesuddentermination().md>) — Enables the application for quick killing using sudden termination.

### Controlling automatic termination

- [- disableAutomaticTermination:](<processinfo/disableautomatictermination(__).md>) — Disables automatic termination for the application.
- [- enableAutomaticTermination:](<processinfo/enableautomatictermination(__).md>) — Enables automatic termination for the application.
- [automaticTerminationSupportEnabled](processinfo/automaticterminationsupportenabled.md) — A Boolean value indicating whether the app supports automatic termination.

### Getting host information

- [hostName](processinfo/hostname.md) — The name of the host computer on which the process is executing.
- [operatingSystemVersionString](processinfo/operatingsystemversionstring.md) — A string containing the version of the operating system on which the process is executing.
- [operatingSystemVersion](processinfo/operatingsystemversion.md) — The version of the operating system on which the process is executing.
- [- isOperatingSystemAtLeastVersion:](<processinfo/isoperatingsystematleast(__).md>) — Returns a Boolean value indicating whether the version of the operating system on which the process is executing is the same or later than the given version.
- [OperatingSystemVersion](operatingsystemversion.md) — A structure that contains version information about the currently executing operating system, including major, minor, and patch version numbers.
- [- operatingSystem](<processinfo/operatingsystem().md>) — Returns a constant to indicate the operating system on which the process is executing. _(deprecated)_
- [Anonymous](1552984-anonymous.md) — The following constants are provided by the `NSProcessInfo` class as return values for [- operatingSystem](<processinfo/operatingsystem().md>).
- [- operatingSystemName](<processinfo/operatingsystemname().md>) — Returns a string containing the name of the operating system on which the process is executing. _(deprecated)_

### Getting computer information

- [processorCount](processinfo/processorcount.md) — The number of processing cores available on the computer.
- [activeProcessorCount](processinfo/activeprocessorcount.md) — The number of active processing cores available on the computer.
- [physicalMemory](processinfo/physicalmemory.md) — The amount of physical memory on the computer in bytes.
- [- isDeviceCertifiedFor:](<processinfo/isdevicecertified(for_).md>) — Indicates whether the device supports the requested performance tier.
- [- hasPerformanceProfile:](<processinfo/hasperformanceprofile(__).md>) — Indicates whether an app is running under a known performance profile.
- [systemUptime](processinfo/systemuptime.md) — The amount of time the system has been awake since the last time it was restarted.

### Managing activities

- [- beginActivityWithOptions:reason:](<processinfo/beginactivity(options_reason_).md>) — Begin an activity using the given options and reason.
- [- endActivity:](<processinfo/endactivity(__).md>) — Ends the given activity.
- [- performActivityWithOptions:reason:usingBlock:](<processinfo/performactivity(options_reason_using_).md>) — Synchronously perform an activity defined by a given block using the given options.
- [- performExpiringActivityWithReason:usingBlock:](<processinfo/performexpiringactivity(withreason_using_).md>) — Performs the specified block asynchronously and notifies you if the process is about to be suspended.
- [ActivityOptions](processinfo/activityoptions.md) — Option flags used with [- beginActivityWithOptions:reason:](<processinfo/beginactivity(options_reason_).md>) and [- performActivityWithOptions:reason:usingBlock:](<processinfo/performactivity(options_reason_using_).md>).

### Getting the thermal state

- [thermalState](processinfo/thermalstate-swift.property.md) — The current thermal state of the system.
- [ThermalState](processinfo/thermalstate-swift.enum.md) — Values used to indicate the system’s thermal state.

### Determining whether low power mode is enabled

- [lowPowerModeEnabled](processinfo/islowpowermodeenabled.md) — A Boolean value that indicates the current state of Low Power Mode.

### Working with notifications

- [NSProcessInfoThermalStateDidChangeNotification](processinfo/thermalstatedidchangenotification.md) — Posts when the thermal state of the system changes.
- [NSProcessInfoPowerStateDidChangeNotification](nsnotification/name-swift.struct/nsprocessinfopowerstatedidchange.md) — Posts when the power state of a device changes.

### Working with notification messsages

- [PowerStateDidChangeMessage](processinfo/powerstatedidchangemessage.md) — A message the system sends when the device’s power state changes.
- [ThermalStateDidChangeMessage](processinfo/thermalstatedidchangemessage.md) — A message the system sends when the device’s thermal state changes.
