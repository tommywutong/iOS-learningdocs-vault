---
title: IOLog and Interrupt Context
apple_id: DTS10001648
resource_type: QA
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2011-07-22'
source_url: https://developer.apple.com/library/archive/qa/qa1100/_index.html
archived_at: '2026-07-18T02:29:55.801819Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1100

# IOLog and Interrupt Context

## Q:  The documentation for IOLog says "IOLog should not be called from interrupt context." How do I know if I'm running in interrupt context?

A: "Interrupt context" is another name for primary interrupt or hardware interrupt time, as opposed to secondary interrupt or software interrupt time.

There are only two places in I/O Kit you need to worry about running at primary interrupt time. The first is in the `Filter` function you pass in to `IOFilterInterruptEventSource::filterInterruptEventSource`. The other, far less common case is in the `IOInterruptAction` function passed to `IOService::registerInterrupt`. At these times very little of the system is available so you cannot call `IOLog`.

The `Action` function you pass when creating a `IOFilterInterruptEventSource` will run on the work loop that the event source is attached to, so you can call `IOLog` in the `Action` function. Remember, the `Action` function will only be called if your `Filter` function returns `true` or calls `IOFilterInterruptEventSource::signalInterrupt`.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2011-07-22 | Reformatted content and made minor editorial changes. Expanded explanation of when the Action function is called. |
| 2002-02-13 | New document that describes when I/O Kit runs at primary (hardware) interrupt context. |

