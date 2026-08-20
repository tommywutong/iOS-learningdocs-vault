---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/Debug9.html
archived_at: '2026-07-15T08:05:16.529208Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](Debugging%20a%20WebObjects%20Application.md) [!Previous Section](Debug8.md)

## Using Trace Methods

WOApplication provides trace methods that log different kinds of information about your running application. These methods are useful if you want to see all or part of the call stack. The following table describes the trace methods:

|  __Method__ |  Description |
|  - trace: |  Enables all tracing. |
|  - traceAssignments: |  Logs information about all assignment statements. |
|  - traceStatements: |  Logs information about all statements. |
|  - traceScriptedMessages: |  Logs information when an application enters and exits a scripted method. |
|  - traceObjectiveCMessages: |  Logs information about all Objective-C methods invocations. |

```
```


The output from the trace methods appears in Project Builder's launch panel.
You use the trace methods wherever you want to turn on tracing. Usually, you do this in the __init__ method (or constructor) of a component or the application:

```
// Objective-C
- init {
    [super init];
    [[self application] traceAssignments:YES];
    [[self application] traceScriptedMessages:YES];
    return self;
}

// Java
public Main() {
    super();
    this.application.traceAssignments(true);
    this.application.traceScriptedMessages(true);
    .
    .
    .
}
```

[!Table of Contents](Debugging%20a%20WebObjects%20Application.md) [!Next Section](Debug10.md)
