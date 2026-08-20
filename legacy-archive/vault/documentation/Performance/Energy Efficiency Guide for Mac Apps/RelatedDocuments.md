---
title: Energy Efficiency Guide for Mac Apps
apple_id: TP40013929
resource_type: Guide
platform: macOS
topic: Performance
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/power_efficiency_guidelines_osx/RelatedDocuments.html
archived_at: '2026-07-18T01:50:22.600756Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Energy Efficiency Guide for Mac Apps](index.md)



## Related Documents

This chapter lists additional sources of information about the technologies and methods discussed in this document.

### Resources for Getting Your App to Idle

### Occlusion Notifications

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)[applicationDidChangeOcclusionState:](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428362-applicationdidchangeocclusionsta) in _[NSApplicationDelegate Protocol Reference](https://developer.apple.com/documentation/appkit/nsapplicationdelegate)_

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)[NSApplicationDidChangeOcclusionStateNotification](https://developer.apple.com/documentation/appkit/nsapplication/1428627-didchangeocclusionstatenotificat) in _[NSApplication Class Reference](https://developer.apple.com/documentation/appkit/nsapplication)_

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)[NSWindowDidChangeOcclusionStateNotification](https://developer.apple.com/documentation/appkit/nswindow/1419549-didchangeocclusionstatenotificat) in _[NSWindow Class Reference](https://developer.apple.com/documentation/appkit/nswindow)_

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)[occlusionState](https://developer.apple.com/documentation/appkit/nsapplication/1428656-occlusionstate) in _[NSApplication Class Reference](https://developer.apple.com/documentation/appkit/nsapplication)_

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)[occlusionState](https://developer.apple.com/documentation/appkit/nswindow/1419321-occlusionstate) in _[NSWindow Class Reference](https://developer.apple.com/documentation/appkit/nswindow)_

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)[windowDidChangeOcclusionState:](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419424-windowdidchangeocclusionstate) in _[NSWindowDelegate Protocol Reference](https://developer.apple.com/documentation/appkit/nswindowdelegate)_

### Active App Transitions

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)[applicationWillResignActive:](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428539-applicationwillresignactive) in _[NSApplicationDelegate Protocol Reference](https://developer.apple.com/documentation/appkit/nsapplicationdelegate)_

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)[applicationDidResignActive:](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428636-applicationdidresignactive) in _[NSApplicationDelegate Protocol Reference](https://developer.apple.com/documentation/appkit/nsapplicationdelegate)_

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)[applicationWillBecomeActive:](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428699-applicationwillbecomeactive) in _[NSApplicationDelegate Protocol Reference](https://developer.apple.com/documentation/appkit/nsapplicationdelegate)_

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)[applicationDidBecomeActive:](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428577-applicationdidbecomeactive) in _[NSApplicationDelegate Protocol Reference](https://developer.apple.com/documentation/appkit/nsapplicationdelegate)_

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)[NSApplicationWillResignActiveNotification](https://developer.apple.com/documentation/appkit/nsapplicationwillresignactivenotification) in _[NSApplication Class Reference](https://developer.apple.com/documentation/appkit/nsapplication)_

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)[NSApplicationDidResignActiveNotification](https://developer.apple.com/documentation/appkit/nsapplicationdidresignactivenotification) in _[NSApplication Class Reference](https://developer.apple.com/documentation/appkit/nsapplication)_

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)[NSApplicationWillBecomeActiveNotification](https://developer.apple.com/documentation/appkit/nsapplication/1428383-willbecomeactivenotification) in _[NSApplication Class Reference](https://developer.apple.com/documentation/appkit/nsapplication)_

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)[NSApplicationDidBecomeActiveNotification](https://developer.apple.com/documentation/appkit/nsapplicationdidbecomeactivenotification) in _[NSApplication Class Reference](https://developer.apple.com/documentation/appkit/nsapplication)_

### Resources for Prioritizing Work

### Quality of Service Classes (QoS)

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)_[Concurrency Programming Guide](../../General/Concurrency%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4daojr)_

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)_Grand Central Dispatch (GCD) Reference_

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)_[NSOperation Class Reference](https://developer.apple.com/documentation/foundation/nsoperation)_

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)_[NSOperationQueue Class Reference](https://developer.apple.com/documentation/foundation/nsoperationqueue)_

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)_[NSTask Class Reference](https://developer.apple.com/documentation/foundation/nstask)_

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)_[NSThread Class Reference](https://developer.apple.com/documentation/foundation/nsthread)_

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)powermetrics(1) Mac OS X Manual Page

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)spindump(8) Mac OS X Manual Page

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)_[Testing with Xcode](../../Developer%20Tools/Testing%20with%20Xcode/About%20Testing%20with%20Xcode.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2dcmzs)_

### Resources for Scheduling Work

### Grand Central Dispatch (GCD)

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)_[Concurrency Programming Guide](../../General/Concurrency%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4daojr)_

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)_Grand Central Dispatch (GCD) Reference_

### Scheduling Background Activity

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)[NSActivityBackground](https://developer.apple.com/documentation/foundation/nsactivityoptions/nsactivitybackground) in _[NSProcessInfo Class Reference](https://developer.apple.com/documentation/foundation/processinfo)_

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)[beginActivityWithOptions:reason:](https://developer.apple.com/documentation/foundation/nsprocessinfo/1415995-beginactivitywithoptions) in _[NSProcessInfo Class Reference](https://developer.apple.com/documentation/foundation/processinfo)_

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)[performActivityWithOptions:reason:usingBlock:](https://developer.apple.com/documentation/foundation/processinfo/1418048-performactivity) in _[NSProcessInfo Class Reference](https://developer.apple.com/documentation/foundation/processinfo)_

### Scheduling Background Networking

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)_[NSURLSessionDataDelegate Protocol Reference](https://developer.apple.com/documentation/foundation/nsurlsessiondatadelegate)_

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)_[NSURLSessionDelegate Protocol Reference](https://developer.apple.com/documentation/foundation/urlsessiondelegate)_

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)_[NSURLSessionDownloadDelegate Protocol Reference](https://developer.apple.com/documentation/foundation/urlsessiondownloaddelegate)_

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)_[NSURLSessionTaskDelegate Protocol Reference](https://developer.apple.com/documentation/foundation/nsurlsessiontaskdelegate)_

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)_[NSURL Class Reference](https://developer.apple.com/documentation/foundation/nsurl)_

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)_[NSURLRequest Class Reference](https://developer.apple.com/documentation/foundation/nsurlrequest)_

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)_[NSURLSession Class Reference](https://developer.apple.com/documentation/foundation/nsurlsession)_

### XPC Activity

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)_[activity.h Reference](https://developer.apple.com/documentation/xpc/activity.h)_ in _[XPC Services API Reference](https://developer.apple.com/documentation/xpc)_

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)_[Daemons and Services Programming Guide](../../Mac%20OSX/Daemons%20and%20Services%20Programming%20Guide/About%20Daemons%20and%20Services.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3te2i)_

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)_[XPC Services API Reference](https://developer.apple.com/documentation/xpc)_

### Resources for Reducing Overhead

### Minimizing I/O

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)fs_usage(1) Mac OS X Manual Page

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)_[Instruments User Guide](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/InstrumentsUserGuide/index.html#//apple_ref/doc/uid/TP40004652)_

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)_[Networking Overview](../../Networking%20Internet%20Web/Networking%20Overview/About%20Networking.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemrq)_

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)[Performance Tips](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/PerformanceTips/PerformanceTips.html#//apple_ref/doc/uid/TP40010672-CH7) in _[File System Programming Guide](../../File%20Management/File%20System%20Programming%20Guide/About%20Files%20and%20Directories.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydmnzs)_

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)_[Testing with Xcode](../../Developer%20Tools/Testing%20with%20Xcode/About%20Testing%20with%20Xcode.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2dcmzs)_

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)_[Xcode Overview](https://developer.apple.com/library/archive/documentation/ToolsLanguages/Conceptual/Xcode_Overview/index.html#//apple_ref/doc/uid/TP40010215)_

### Minimizing Timer Usage

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)_[CFRunLoop Reference](https://developer.apple.com/documentation/corefoundation/cfrunloop)_

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)_[Concurrency Programming Guide](../../General/Concurrency%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4daojr)_

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)[Creating XPC Services](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CreatingXPCServices.html#//apple_ref/doc/uid/10000172i-SW6) in _[Daemons and Services Programming Guide](../../Mac%20OSX/Daemons%20and%20Services%20Programming%20Guide/About%20Daemons%20and%20Services.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3te2i)_

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)_[Darwin Notification API Reference](https://developer.apple.com/documentation/darwinnotify/darwin_notification_api)_

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)[Determining Reachability and Getting Connected](https://developer.apple.com/library/archive/documentation/Networking/Conceptual/SystemConfigFrameworks/SC_ReachConnect/SC_ReachConnect.html#//apple_ref/doc/uid/TP40001065-CH204) in _[System Configuration Programming Guidelines](../../Networking/System%20Configuration%20Programming%20Guidelines/Introduction%20to%20System%20Configuration%20Programming%20Guidelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrv)_

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)_[Disk Arbitration Programming Guide](../../Disk%20Arbitration%20Programming%20Guide/About%20Disk%20Arbitration.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tgmjq)_

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)_[DNS Service Discovery Programming Guide](../../Networking/DNS%20Service%20Discovery%20Programming%20Guide/Introduction%20to%20DNS%20Service%20Discovery.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnru)_ and _[NSNetServices and CFNetServices Programming Guide](../../Networking/NSNetServices%20and%20CFNetServices%20Programming%20Guide/About%20NSNetServices%20and%20CFNetServices.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdomzw)_

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)_[File System Events Programming Guide](../../Darwin/File%20System%20Events%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2teobz)_

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)[Finding and Accessing Devices](https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/AccessingHardware/AH_Finding_Devices/AH_Finding_Devices.html#//apple_ref/doc/uid/TP30000379) in _[Accessing Hardware From Applications](../../Device%20Drivers/Accessing%20Hardware%20From%20Applications/Introduction%20to%20Accessing%20Hardware%20From%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgnzw)_

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)_Grand Central Dispatch (GCD) Reference_

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)_[Local and Remote Notification Programming Guide](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/index.html#//apple_ref/doc/uid/TP40008194)_

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)[Monitoring Events](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/EventOverview/MonitoringEvents/MonitoringEvents.html#//apple_ref/doc/uid/10000060i-CH15) in _[Cocoa Event Handling Guide](../../Cocoa/Cocoa%20Event%20Handling%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3da2i)_

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)_[NSDistributedNotificationCenter Class Reference](https://developer.apple.com/documentation/foundation/nsdistributednotificationcenter)_

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)_[NSTimer Class Reference](https://developer.apple.com/documentation/foundation/timer)_

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)`sleep(3) Mac OS X Developer Tools Manual Page`

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)[Synchronization](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/ThreadSafety/ThreadSafety.html#//apple_ref/doc/uid/10000057i-CH8) in _[Threading Programming Guide](../../Cocoa/Threading%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2to2i)_

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)timerfires(1) Mac OS X Manual Page

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)`usleep(3) Mac OS X Developer Tools Manual Page`

### Avoiding Extraneous Content Updates

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)_[Drawing Performance Guidelines](../Drawing%20Performance%20Guidelines/Introduction%20to%20Drawing%20Performance%20Guidelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge2tc2i)_

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)[getRectsBeingDrawn:count:](https://developer.apple.com/documentation/appkit/nsview/1483772-getrectsbeingdrawn) in _[NSView Class Reference](https://developer.apple.com/documentation/appkit/nsview)_

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)[needsToDrawRect:](https://developer.apple.com/documentation/appkit/nsview/1483570-needstodrawrect) in _[NSView Class Reference](https://developer.apple.com/documentation/appkit/nsview)_

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)[Optimizing View Drawing](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaViewsGuide/Optimizing/Optimizing.html#//apple_ref/doc/uid/TP40002978-CH11) in _[View Programming Guide](../../Cocoa/View%20Programming%20Guide/Introduction%20to%20View%20Programming%20Guide%20for%20Cocoa.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdsnzy)_

### Resources for Monitoring and Responding to Energy Use

### General Resources

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)Debug Your App in _[Xcode Overview](https://developer.apple.com/library/archive/documentation/ToolsLanguages/Conceptual/Xcode_Overview/index.html#//apple_ref/doc/uid/TP40010215)_

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)_[Instruments User Guide](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/InstrumentsUserGuide/index.html#//apple_ref/doc/uid/TP40004652)_

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)_[Testing with Xcode](../../Developer%20Tools/Testing%20with%20Xcode/About%20Testing%20with%20Xcode.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2dcmzs)_

### Monitoring Energy Usage

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)dtrace(1) Mac OS X Manual Page

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)fs_usage(1) Mac OS X Manual Page

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)pmset(1) Mac OS X Manual Page

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)powermetrics(1) Mac OS X Manual Page

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)sample(1) Mac OS X Manual Page

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)spindump(8) Mac OS X Manual Page

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)timerfires(1) Mac OS X Manual Page

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)top(1) Mac OS X Manual Page

### Performance Testing

![image: ../Art/document_icon_2x.png](attachments/Art/document_icon_2x.png)_[Performance Overview](../Performance%20Overview/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytimjq)_

[Best Practices](BestPractices.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztsmrzfvbuqmzyfvjvomi)

[WWDC Videos](WWDCVideos.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztsmrzfvbuqmrrfvjvomi)
