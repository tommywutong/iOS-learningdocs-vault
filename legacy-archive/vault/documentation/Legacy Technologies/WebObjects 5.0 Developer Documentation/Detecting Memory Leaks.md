---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Topics/ProgrammingTopics.6.html
archived_at: '2026-07-15T08:14:54.648660Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Up](attachments/Topics/up.gif)](TopicsTOC.md) [![Previous](attachments/Topics/previous.gif)](ProgrammingTopics.5.md) [![Next](attachments/Topics/next.gif)](ProgrammingTopics.7.md)

#   Detecting Memory Leaks

##  Synopsis

Describes methods to detect and prevent memory leaks in an application.

##  Description

The best tool currently available to detect memory leaks is ObjectAlloc. This application is available on all platforms. ObjectAlloc uses the object allocation statistics built into the Foundation framework. When this facility is active, every object allocation, deallocation, copy, retain, release, and autorelease is recorded as it happens.

The ObjectAlloc application resides under
$NEXT_ROOT/Developer/Applications
on Windows NT machines with WebObjects 4 installed. The ObjectAlloc application resides under
/System/Developer/Applications
on Mac OS X Server machines with WebObjects 4 installed. General information about using ObjectAlloc is available through the Help menu.

You can use ObjectAlloc on a Mach/Windows machine to get the allocation information from a PDO process. To attach a PDO process to ObjectAlloc, make sure that the Executable field in the ObjectAlloc window is blank, and click the start button (the green arrow) on the ObjectAlloc panel. A panel will appear and ask, "Do you want ObjectAlloc to wait for a task to attach, and launch the task to be monitored yourself?" Click Yes to continue. The next panel appears with the environment variables that you'll need to set to monitor the task. Make sure
NSKeepAllocationStatistics
is set to
YES
.

Another memory leak detector, MallocDebug, is available on Mac OS X Server. Since this application uses Mach-specific messaging calls, it is not available under Windows NT. The online help provides detailed documentation on how to prepare an application for use with MallocDebug.For applications that use the Java-wrapped frameworks, WebObjects 4.0 provides methods to force garbage collection in the WOApplication class. The API is defined as follows:

```

public int garbageCollectionPeriod ();
public void setGarbageCollectionPeriod (int);
```


The default value for
WOGarbageCollectionPeriod
is 20, that is, garbage collection is forced every 20 requests.

##  See Also

- 

  [Detecting Freed Object Exceptions](Detecting%20Freed%20Object%20Exceptions.md#apple-gm2dsmru)

##  Questions

- 

  What tools can I use to detect memory leaks?
- 

  How do I force my WebObjects application to garbage collect?

##  Keywords

- 

  Memory
- 

  Leak
- 

  ObjectAlloc
- 

  MallocDebug
- 

  Garbage
- 

  Collection
- 

  Performance

##  Revision History

21 July, 1998. Mai Nguyen. First Draft.

26 October, 1998. Clif Liu. Second Draft.

```

```

---

© 1999 Apple Computer, Inc.

[![Up](attachments/Topics/up.gif)](TopicsTOC.md) [![Previous](attachments/Topics/previous.gif)](ProgrammingTopics.5.md) [![Next](attachments/Topics/next.gif)](ProgrammingTopics.7.md)[an error occurred while processing this directive]

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
