---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/Topics/DetectMemLeak.html
archived_at: '2026-07-15T08:01:07.085910Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Programming Topics](WebObjects%20Programming%20Topics.md)

# Detecting Memory Leaks

##  Synopsis

Describes methods to detect and prevent memory leaks in an application.

##  Description

The best tool currently available to detect memory leaks is ObjectAlloc. This application is available on all platforms. ObjectAlloc uses the object allocation statistics built into the Foundation framework. When this facility is active, every object allocation, deallocation, copy, retain, release, and autorelease is recorded as it happens.

The ObjectAlloc application resides under $NEXT_ROOT/Developer/Applications on WebObjects4.0/Windows NT machines. The ObjectAlloc application resides under /System/Developer/Applications on WebObjects 4.0/ Mac OS X Server machines. General information about using ObjectAlloc is available by selecting the help menu.

You can use ObjectAlloc on a Mach/Windows machine to get the allocation information from a PDO process. To attach a PDO process to ObjectAlloc, make sure that the "Executable" field in the ObjectAlloc window is blank, and press the Start button (the green arrow) on the ObjectAlloc panel. A panel will appear and ask, "Do you want ObjectAlloc to wait for a task to attach, and launch the task to be monitored yourself?" Press "Yes" to continue. The next panel appears with the environment variables that you'll need to set to monitor the task. Make sure _NSKeepAllocationStatistics_
is set to YES.

Another memory leak detector, MallocDebug, is available on Mac OS X Server. Since this application uses Mach-specific messaging calls, it is not available under Windows NT. The on line help provides detailed documentation on how to prepare an application for use with MallocDebug.

For applications that use the Java-wrapped frameworks, WebObjects 4.0 provides methods to force garbage collection in the WOApplication class. The API is defined as follows:

#####  Figure 1. Java Code

```
public int garbageCollectionPeriod ();
```



```
public void setGarbageCollectionPeriod (int);
```


The WOGarbageCollectionPeriod defaults to 20, i.e., garbage collection will be forced every 20 requests.

##  See Also

· Debugging

· Detecting Freed Object Exceptions

##  Questions

· What tools can I use to detect memory leaks?

· How do I force my WebObjects application to garbage collect?

##  Keywords

· Memory Leaks

· ObjectAlloc

· MallocDebug

· Garbage Collection

· Performance

##  Revision History

21 July, 1998. Mai Nguyen. First Draft.

26 October, 1998. Clif Liu. Second Draft.

```

```


Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
