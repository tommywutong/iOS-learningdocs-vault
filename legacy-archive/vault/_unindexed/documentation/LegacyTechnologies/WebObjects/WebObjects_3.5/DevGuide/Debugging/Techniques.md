---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/Debugging/Techniques.html
archived_at: '2026-07-15T07:51:22.300877Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DebuggingTOC.md) [!Previous Section](LaunchForDebug.md)

# Debugging Techniques

To debug WebScript and Java code, you rely primarily on log messages and trace statements that write to standard output. This section describes the statements you can include in your code to help you debug.

## Writing Debug Messages

The method __logWithFormat:__ (in Java, __logString__) writes a formatted string to standard error (__stderr__).
In WebScript and Objective-C, __logWithFormat:__ works like the __printf()__ function in C. This method takes a format string and a variable number of additional arguments. For example, the following code excerpt prints the string "The value of myString is Elvis":

```
    myString = @"Elvis";
    [self logWithFormat:@"The value of myString is %@", myString];
```


When this code is parsed, the value of __myString__ is substituted for the conversion specification __%@__. The conversion character @ indicates that the data type of the variable being substituted is an object (that is, of the __id__ data type).
Because in WebScript all variables are objects, the conversion specification you use must always be __%@__. Unlike __printf()__, you can't supply conversion specifications for primitive C data types such as __%d__, __%s__, __%f__, and so on. (If you do, you might see the address of the variable rather than its value.)
In Java, the equivalent of __logWithFormat:__ is __logString__, and you can send it only to WebApplication objects. Instead of using __printf__ specifications, it uses concatenation. Here's how you'd write the same lines of code in Java:

```
    myString = "Elvis";
    application().logString("The value of myString is " + myString);
```


Perhaps the most effective debugging technique is to use __logWithFormat:__ to print the contents of __self__. This prints the values of all of your component variables. For example, this statement at the end of the __sayHello__ method in HelloWorld's __Main.wos__:

```
    [self logWithFormat:@"The contents of self in sayHello are %@", self];
```


produces output that resembles the following:

```
    The contents of self in sayHello are
    <<WOScriptedClass(/WebObjects/Examples/WebScript/HelloWorld.woa/Main.wo/Main): 0x8cb08 name=Main subcomponents=0x0> visitorName=frank>
```


Here's how you'd write the same line of code in Java:

```
    application().logString("The contents of this in sayHello are "
        + this.toString());
```


## Using Trace Methods

WOApplication (in Java, WebApplication) provides trace methods that log different kinds of information about your running application. These methods are useful if you want to see all or part of the call stack. The following table describes the trace methods:

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
    - init {
        [super init];
        [self.application traceAssignments:YES];
        [self.application traceScriptedMessages:YES];
        return self;
    }
```


## Isolating Portions of a Page

If a component is producing unexpected HTML output, you can try to isolate the problem by printing small portions of the page at a time. Use HTML comments (__<!--__) to comment out all but the suspect portion of the page and reload the component. Verify that this portion works as you intend it to. Reduce the size of the commented out portion of the page until more and more of the page is visible in the browser. Continue until you have found the offending area.

[!Table of Contents](DebuggingTOC.md) [!Next Section](Pitfalls.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
