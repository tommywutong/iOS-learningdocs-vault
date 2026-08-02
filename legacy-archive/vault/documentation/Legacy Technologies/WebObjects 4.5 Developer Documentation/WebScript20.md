---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/WebScript20.html
archived_at: '2026-07-15T08:06:32.211099Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](The%20WebScript%20Language.md) [!Previous Section](WebScript19.md)

### Handling an Exception

Where and how an exception is handled depends on the context where the exception was raised. In general, a raise message is sent to an NSException object within the domain of an exception handler. An exception handler is contained within a control structure created by the keywords NS_DURING, NS_HANDLER, and NS_ENDHANDLER, as shown here:

```
.
.
NS_DURING
    [some code];
    [some more code];
NS_HANDLER
    [exception handler code];
    [more exception handler code];
NS_ENDHANDLER
.
.
```


The section of code between NS_DURING and NS_HANDLER is the _exception handling domain_; the section between NS_HANDLER and NS_ENDHANDLER is the _local exception handler_. The normal flow of program execution is marked by the gray arrow; the code within the local exception handler is executed only if an exception is raised. Sending a __raise__ message to an exception object causes program control to jump to the first executable line following NS_HANDLER.
Although an exception can be raised directly within the exception handling domain, exceptions more often arise indirectly from a method invoked from the domain. No matter how deep in a call sequence the exception is raised, execution jumps to the local exception handler (assuming there are no intervening exception handlers, as discussed in the next section). In this way, exceptions raised at a low level can be caught at a high level.
You may leave the exception handling domain (the section of code between NS_DURING and NS_HANDLER) by:

- Raising an exception.
- Calling NS_VALUERETURN(), which returns a value from the DURING block.
- Calling NS_VOIDRETURN, which returns void from the DURING block.
- "Falling off the end."

"Falling off the end" is simply the normal path of execution-after all statements in the exception handling domain are executed, execution continues on the line following NS_ENDHANDLER.
__Note:__  You can't use return to exit an exception handling domain-errors will result.

[!Table of Contents](The%20WebScript%20Language.md) [!Next Section](WebScript21.md)
