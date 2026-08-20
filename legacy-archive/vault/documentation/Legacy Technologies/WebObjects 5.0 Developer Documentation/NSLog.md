---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/FoundationRef/Java/Classes/NSLog.html
archived_at: '2026-07-15T08:13:56.169706Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md) 

# NSLog

> **__Inherits from:__**
> : Object

> **__Package:__**
> : com.webobjects.foundation

---

## Class Description

---

NSLog is a static class that you use to access the WebObjects Foundation logging system. It allows you to log debugging messages, and provides functionality for controlling the level and focus of debugging output. Logging with NSLog offers greater flexibility and integration with the WebObjects runtime and debugging system than does logging with System.out, System.err, or java.rmi.server.LogStream.

By specifying debug groups and the debug level using NSLog's methods, you can control the scope and granularity of debugging output. Perhaps you are only interested in seeing debugging output that relates to the Enterprise Objects Framework, or more specifically, debugging output that relates to database fetches. NSLog is designed to allow you to specify the output you want to see, based on predefined debug groups and levels. See the section on ["Creating Custom Debug Groups" (page 128)](#apple-ijbeiskiifeuu) to understand how NSLog uses a bit mask to specify sets of debug groups.

Although NSLog provides functionality for advanced debugging, it is also as simple to use as outputting to System.out.\*: `NSLog.out.appendln("WebObjects");`

The above code outputs "WebObjects" in the console by default, but output can be directed to custom NSLog.Loggers.

The logging system is made up of three classes: NSLog, NSLog.Logger, and NSLog.PrintStreamLogger. NSLog provides methods for controlling the level (amount of information sent to the logger) and focus (scope of the information sent to the logger) of debugging output. NSLog.Logger is an abstract class that provides the basic functionality for NSLog. NSLog.PrintStreamLogger is a subclass of NSLog.Logger and appends information to the debug logger which is directed to a java.io.PrintStream pointing to System.out, System.err, or to a custom java.io.PrintStream.

The NSLog class cannot be instantiated.

## Redirecting the Output of NSLog

The Foundation logging system offers the ability to create custom logging implementations, and to redirect their output to custom java.io.PrintStreams, such as local files. This example illustrates these features of the logging system, and directs output to a custom java.io.PrintStream, the local file "/Local/Users/log.txt":

> ```
> // Output defaults to System.out.
> NSLog.PrintStreamLogger aLogger = new NSLog.PrintStreamLogger();
>
> // New print stream based on path.
> PrintStream aStream = NSLog.printStreamForPath ("/Local/Users/log.txt");
>
> // Direct output to the custom PrintStream.
> aLogger.setPrintStream (aStream);
>
> // Assign the custom PrintStreamLogger to the declared instances of NSLogger in NSLog.
> NSLog.setOut(aLogger);
> NSLog.setErr(aLogger);
> NSLog.setDebug(aLogger);
>
> // Enable verbose logging.
> aLogger.setIsVerbose (true);
> String str = "WebObjects";
>
> // Outputs "[2000-10-18 09:01:00 GMT] <main> WebObjects"
> aLogger.appendln (str);
>
> // Disables logging.
> aLogger.setIsEnabled (false);
>
> // Outputs nothing, since logging is disabled.
> daLogger.appendln (str);
> ```

By subclassing NSLog.Logger instead of NSLog.PrintStreamLogger, you can provide custom logging implementations that are not based on java.io.PrintStreams, such as outputting to email, Swing windows, etc. See the documentation for ["NSLog.Logger" (page 139)](NSLog.Logger.md#apple-ijbesqsei5eec) for more details.

## Debug Groups

To control the scope of the debug information that is sent to the logger, NSLog declares a number of debug groups, which are listed in the ["Constants" (page 129)](#apple-inauurkiijfeu) section. By default, logging is enabled for all the debug groups declared by NSLog. All the WebObjects frameworks, including Foundation and EOF, use NSLog for debugging, and rely on debug groups to control the scope of their debug logging.

As an example, this code uses debug groups to disable logging for debug information related to the Enterprise Objects Framework:

> ```
> NSLog.refuseDebugLoggingForGroups(NSLog.DebugGroupEnterpriseObjects)
> ```

Before sending debug information to the logger, all classes that log EOF-related debug information check to see if debug logging is allowed for EOF-related issues using one of the __debugLoggingAllowedFor...__ methods. Since the above code removed the DebugGroupEnterpriseObjects bit from the bit mask, EOF-related issues won't be sent to the logger.

## Debug Levels

To control the granularity of debug information that is sent to the logger, NSLog declares a number of debug levels, which are listed in the ["Constants" (page 129)](#apple-inauurkiijfeu) section. A debug level specifies the importance of the information displayed in a message. These messages may be the result of exceptions or errors, but may also just be informational, such as printing variable values.

When an exception is encountered, debug information should only be sent to the logger if the debug level is [DebugLevelCritical](#apple-ineemrkgjfdes) or greater. If the debug level is set to [DebugLevelOff](#apple-ineemssdincui), any error message in the catch block should not be sent to the logger. A simple example:

> ```
> } catch (SomeException e) {
>     if (NSLog.debugLoggingAllowedForLevel(DebugLevelCritical) {
>         NSLog.debug.appendln("Exception encountered: " + e.getMessage());
>         NSLog.debug.appendln(e);
>     }
> }
> ```

When you want to see the value of a variable at particular points in your application, you use [DebugLevelInformational](#apple-ineemssjjbbeg) to control logging. Logging the values of variables can be expensive, so it is prudent to wrap this kind of logging in a debug level conditional. For instance, you should conditionalize the logging of values in an array like this:

> ```
> // Assuming declaration of int[] anArray = new int[10];
> if debugLoggingAllowedForLevel(DebugLevelInformational) {
>     for (i = 0, i < 9, i++) {
>         NSLog.out.appendln(anArray[i]);
>     }
> }
> ```

[DebugLevelDetailed](#apple-ineemskgineuq) should be used to conditionalize logging for computationally intensive tasks, such as JDBC function calls.

Note that if you specify the allowed debug level using the [setAllowedDebugLevel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgtdpm4xxgzluifwgy33xmvseizlcovtuyzlwmvwa) method, messsages of that level and lower will be logged. That is, [DebugLevelDetailed](#apple-ineemskgineuq) will also log messages of level [DebugLevelInformational](#apple-ineemssjjbbeg) and messages of level [DebugLevelCritical](#apple-ineemrkgjfdes). Likewise, [DebugLevelInformational](#apple-ineemssjjbbeg) will also log messages of level [DebugLevelCritical](#apple-ineemrkgjfdes), but not messages of level [DebugLevelDetailed](#apple-ineemskgineuq).

## Creating Custom Debug Groups

NSLog uses a bit mask to specify a set of debug groups, which means that you can easily create a custom debug groups mask for more flexible logging. For instance, if you are interested in logging debugging output only for EOF-related issues and EOModel-related issues, you can simply bitwise inclusive OR the groups together using the "|" operator in Java. That creates a debug groups mask which you can use to more flexibly monitor and log errors relating to those two issues. To do this:

> ```
> // First, remove all debug groups from the mask, since they are all enabled by default.
> NSLog.refuseDebugLoggingForGroupsMask(~0);
> // Create a custom debug groups mask.
> NSLog.allowDebugLoggingForGroupsMask     (DebugGroupEnterpriseObjects | DebugGroupModel);
> ```

In addition to the debug groups provied for you by WebObject, you can add your own debug groups. The high 32 bits (i.e. bits 32 - 63) are available to developers. The low bits are reserved by WebObjects. An example of declaring a new debug group:

> ```
> public static final long DebugGroupCustomGroup = 1 << 32;
> ```

## NSLog From the Command Line

You can enable debug groups and levels from the command line. For example:

> ```
> % cd MyJavaWOApp.woa
> % ./MyJavaWOApp -DNSDebugLevel=2 -DNSDebugGroups=32
> ```

The above code enables [DebugLevelInformational](#apple-ineemssjjbbeg) and [DebugGroupResources](#apple-ineemqsjjfdue). The argument for debug level is passed in as an int; for debug groups, the argument is passed in as a long. Therefore, you must calculate the long value for each debug group you pass on the command line (in order to get the bit position for each group).

To do this, calculate 2 ^ (value for the debug group as listed in the ["Constants" (page 129)](#apple-inauurkiijfeu) section). For example, to enable [DebugGroupWebObjects](#apple-ineemrsfjfauc), calculate 2 ^ 2, and pass the result as the argument on the command line.

You can enable multiple debug groups by summing the long values of each group. For example:

> ```
> % ./MyJavaWOApp -DNSDebugLevel=2 -DNSDebugGroups=16 + 32 + 1024
> ```

The above code enables [DebugGroupMultithreading](#apple-ineemskbizeug). [DebugGroupResources](#apple-ineemqsjjfdue), and [DebugGroupFormatting](#apple-ineemsshjbbeq).

## Constants

---

NSLog defines the following constants:

|  |  |  |  |
| --- | --- | --- | --- |
| __Constant__ | __Type__ | __Value__ | __Description__ |
| DebugGroupApplicationGeneration | `long` | 3 | The debug group for logging of general application generation issues. |
| DebugGroupArchiving | `long` | 6 | The debug group for logging of encoding and decoding issues. |
| DebugGroupAssociations | `long` | 19 | The debug group for logging of association exceptions and problems. |
| DebugGroupComponentBindings | `long` | 9 | The debug group for logging of binding exceptions and problems. |
| DebugGroupControllers | `long` | 20 | The debug group for logging of controller exceptions and problems. |
| DebugGroupComponents | long | 26 | Description forthcoming. |
| DebugGroupDatabaseAccess | `long` | 16 | The debug group for logging of database access exceptions and problems. |
| DebugGroupDeployment | `long` | 22 | The debug group for logging of Monitor, wotaskd, and deployment related issues. |
| DebugGroupEnterpriseObjects | `long` | 1 | The debug group for enabling logging of general EOF issues. |
| DebugGroupFormatting | `long` | 10 | The debug group for logging of formatting exceptions and problems. |
| DebugGroupIO | `long` | 13 | The debug group for logging of I/O exceptions and problems. |
| DebugGroupKeyValueCoding | `long` | 8 | The debug group for logging of key value coding exceptions and problems |
| DebugGroupModel | `long` | 15 | The debug group for logging of EOModel exceptions, problems, and inconsistencies. |
| DebugGroupMultithreading | `long` | 4 | The debug group for logging of threading issues. |
| DebugGroupParsing | `long` | 23 | The debug group for logging of HTML parsing issues and other HTML-related issues. |
| DebugGroupQualifiers | `long` | 11 | The debug group for logging of qualifier issues.The debug group for logging of formatting exceptions and problems. |
| DebugGroupReflection | `long` | 24 | The debug group for logging of class introspection issues. |
| DebugGroupRequestHandling | long | 25 | The debug group for logging of issues related to the request-response loop. |
| DebugGroupResources | `long` | 5 | The debug group for logging of resource loading/lookup exceptions and problems. |
| DebugGroupRules | `long` | 21 | The debug group for logging of dynamic rule system issues and logging issues. |
| DebugGroupSQLGeneration | `long` | 17 | The debug group for logging of SQL generation issues and logging. |
| DebugGroupTiming | `long` | 14 | The debug group for logging of dynamic rule system issues. |
| DebugGroupUserInterface | `long` | 18 | The debug mask for logging of widget set and view exceptions and problems. |
| DebugGroupValidation | `long` | 7 | The debug group for logging of validation exceptions and problems. |
| DebugGroupWebObjects | `long` | 2 | The debug group for enabling logging of general WebObjects framework issues. |
| DebugLevelOff | `int` | 0 | Logs no messages. The default. |
| DebugLevelCritical | `int` | 1 | Logs debug messages that should not be sent in non-debug mode, such as stack traces. Logging with this debug level is not likely to affect the performance of your application. |
| DebugLevelInformational | `int` | 2 | Logs debug messages that don't qualify as computationally intensive. Logging with this debug level will slow your application only moderately. |
| DebugLevelDetailed | `int` | 3 | Logs debug messages that qualify as computationally intensive, such as JDBC function calls. Logging with this debug level will slow your application considerably. |

## Method Types

---

> **Setting the debug groups mask**
>
> : [setAllowedDebugGroups](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgtdpm4xxgzluifwgy33xmvseizlcovtuo4tpovyhg)
>
> **Setting and retrieving the debug level**
>
> : [setAllowedDebugLevel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgtdpm4xxgzluifwgy33xmvseizlcovtuyzlwmvwa): [allowedDebugLevel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgtdpm4xwc3dmn53wkzcemvrhkz2mmv3gk3a)
>
> **Adding and removing debug groups to the mask**
>
> : [allowDebugLoggingForGroups](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgtdpm4xwc3dmn53uizlcovtuy33hm5uw4z2gn5zeo4tpovyhg): [refuseDebugLoggingForGroups](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgtdpm4xxezlgovzwkrdfmj2wotdpm5tws3thizxxer3sn52xa4y)
>
> **Determining if debug logging is enabled for a particular debug group or groups mask**
>
> : [debugLoggingAllowedForLevel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgtdpm4xwizlcovtuy33hm5uw4z2bnrwg653fmrdg64smmv3gk3a): [debugLoggingAllowedForGroups](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgtdpm4xwizlcovtuy33hm5uw4z2bnrwg653fmrdg64shojxxk4dt): [debugLoggingAllowedForLevelAndGroups](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgtdpm4xwizlcovtuy33hm5uw4z2bnrwg653fmrdg64smmv3gk3cbnzseo4tpovyhg)
>
> **Redirecting output to custom PrintStreams**
>
> : [setDebug](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgtdpm4xxgzluirswe5lh): [setErr](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgtdpm4xxgzluivzhe): [setOut](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgtdpm4xxgzluj52xi)
>
> **Convenience methods**
>
> : [printStreamForPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgtdpm4xxa4tjnz2fg5dsmvqw2rtpojigc5di): [throwableAsString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgtdpm4xxi2dsn53wcytmmvaxgu3uojuw4zy)

## Static Methods

---

### allowDebugLoggingForGroups

`public static synchronized void allowDebugLoggingForGroups( long debugGroups)`

Enables logging for the debug group or the debug groups mask specified by _debugGroups_ by adding it (via bitwise inclusive OR) to the debug groups mask. For instance, to allow debug logging for EOF-related issues, add the EOF debug group, [DebugGroupEnterpriseObjects](#apple-ijbeirkbizbeu) to the mask:
> ```
> NSLog.allowDebugLoggingForGroups(DebugGroupEnterpriseObjects);
> ```

This differs from [setAllowedDebugGroups](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgtdpm4xxgzluifwgy33xmvseizlcovtuo4tpovyhg) in that [allowDebugLoggingForGroups](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgtdpm4xwc3dmn53uizlcovtuy33hm5uw4z2gn5zeo4tpovyhg) _adds_ debug groups and debug groups masks to the bit mask in NSLog. [setAllowedDebugGroups](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgtdpm4xxgzluifwgy33xmvseizlcovtuo4tpovyhg), however, _replaces_ the bit mask in NSLog with the debug group or debug groups mask it is passed. For example,

> ```
> // This will add the EOF debug group to the mask:
> NSLog.allowDebugLoggingForGroups(DebugGroupEnterpriseObjects);
>
> // This will replace all debug groups and masks in the bit mask with the EOF debug group
> NSLog.setAllowedDebugGroups(DebugGroupEnterpriseObjects);
> ```

Use the [refuseDebugLoggingForGroups](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgtdpm4xxezlgovzwkrdfmj2wotdpm5tws3thizxxer3sn52xa4y) method to disallow specific debug groups.

By default, logging is allowed for all debug groups. If you set the debug level to be low (for example, DEBUG_LEVEL-DETAILED), the debugging output may be overwhelming.

See ["Creating Custom Debug Groups" (page 128)](#apple-ijbeiskiifeuu) for more information.

---

### __allowedDebugLevel__

`public static int allowedDebugLevel()`

Returns the allowed debug level.

---

### debugLoggingAllowedForLevel

`public static boolean debugLoggingAllowedForLevel(int aDebugLevel)`

Returns `true` if debug logging is allowed for _aDebugLevel_. Debug logging is allowed if _aDebuglevel_ is less than or equal to the debug level set by [setAllowedDebugLevel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgtdpm4xxgzluifwgy33xmvseizlcovtuyzlwmvwa). This is because the highest debug level, [DebugLevelDetailed](#apple-ineemskgineuq), implies [DebugLevelInformational](#apple-ineemssjjbbeg) which implies [DebugLevelCritical](#apple-ineemrkgjfdes). See the ["Debug Levels" (page 127)](#apple-ijbeirciijbum) for more information.

---

### debugLoggingAllowedForGroups

`public static boolean debugLoggingAllowedForGroups(long debugGroups)`

Returns `true` if the debug groups specified by _debugGroups_ are enabled (that is, the debug groups are part of the debug groups bit mask). See the ["Creating Custom Debug Groups" (page 128)](#apple-ijbeiskiifeuu) for code examples.

---

### debugLoggingAllowedForLevelAndGroups

`public static boolean debugLoggingAllowedForLevelAndGroups( int aDebugLevel, long debugGroups)`

Returns `true` if the debug groups specified by _debugGroups_ are enabled, and if the debug level is less than or equal to the debug level set by [setAllowedDebugLevel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgtdpm4xxgzluifwgy33xmvseizlcovtuyzlwmvwa).

---

### printStreamForPath

`public static java.io.PrintStream printStreamForPath(String aPath)`

Returns a java.io.PrintStream to a file at the specified path. Returns null if there is any problem with the path (i.e. it doesn't exist), or with the file at that path (i.e. it's a path to a directory, so a PrintStream can't be created for it).

---

### refuseDebugLoggingForGroups

`public static synchronized void refuseDebugLoggingForGroups( long debugGroups)`

Disables debug logging for the debug groups mask specified by _debugGroups_.

By default, logging is allowed for all debug groups. If you set the debug level to be low (for example, DEBUG_LEVEL-DETAILED), the debugging output may be overwhelming.

See [allowDebugLoggingForGroups](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgtdpm4xwc3dmn53uizlcovtuy33hm5uw4z2gn5zeo4tpovyhg) for more information.

---

### setAllowedDebugGroups

`public static void setAllowedDebugGroups( long debugGroups)`

Determines the set (the bit mask) of allowed debug groups. Typically, this method is invoked at the beginning of the application execution, since it affects logging behavior in the entire application, and completely overrides the global debug groups mask. If you want to turn logging on for a smaller scope and for a shorter period of execution, you should use [allowDebugLoggingForGroups](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgtdpm4xwc3dmn53uizlcovtuy33hm5uw4z2gn5zeo4tpovyhg) and [refuseDebugLoggingForGroups](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgtdpm4xxezlgovzwkrdfmj2wotdpm5tws3thizxxer3sn52xa4y).

|  |
| --- |
| __Note:__ This method completely overrides the global debug groups mask, and affects logging behavior in the entire application. It is suggested that you only use it once at the beginning of application execution. |

By default, logging is allowed for all debug groups. If you set the debug level to be low (for example, DEBUG_LEVEL-DETAILED), the debugging output may be overwhelming.

See [allowDebugLoggingForGroups](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgtdpm4xwc3dmn53uizlcovtuy33hm5uw4z2gn5zeo4tpovyhg) for an explanation of when to use that method or [setAllowedDebugGroups](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgtdpm4xxgzluifwgy33xmvseizlcovtuo4tpovyhg).

---

### setAllowedDebugLevel

`public static void setAllowedDebugLevel(int aDebugLevel)`

Sets the debug level to _aDebugLevel_. Throws an IllegalArgumentException if _aDebugLevel_ is invalid. Typically, this method is invoked at the beginning of the application execution, since it affects logging behavior in the entire application.

By default, logging is allowed for all debug groups. If you set the debug level to be low (for example, DEBUG_LEVEL-DETAILED), the debugging output may be overwhelming.

See the ["Constants"](#apple-inauurkiijfeu) section in this document for a list of predefined debug levels.

---

### setDebug

`public static void setDebug(NSLog.Logger aLogger)`

Sets the debugging logger NSLog.debug to _aLogger_. By default, NSLog.debug is a NSLog.PrintStreamLogger that sends its output to System.err. NSLog.debug is used for status and error messages that will conditionally be shown.

---

### setErr

`public static void setErr(NSLog.Logger aLogger)`

Sets the logger NSLog.err to _aLogger_. By default, NSLog.err is a NSLog.PrintStreamLogger that sends its output to System.err. NSLog.err is used for error messages that will always be shown.

---

### setOut

`public static void setOut(NSLog.Logger aLogger)`

Sets the logger NSLog.out to _aLogger_. By default, NSLog.out is a NSLog.PrintStreamLogger that sends its output to System.out. NSLog.out is used for status messages that will always be shown.

---

### throwableAsString

`public static String throwableAsString(Throwable aThrowable)`

Returns the stack trace of _aThrowable_ as a string.

---

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
