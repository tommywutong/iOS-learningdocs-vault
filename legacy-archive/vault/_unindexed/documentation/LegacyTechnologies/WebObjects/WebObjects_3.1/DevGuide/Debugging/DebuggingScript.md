---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/Debugging/DebuggingScript.html
archived_at: '2026-07-15T07:46:41.186616Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DevTasks.book.md) [!Previous Section](DevTasks.book.md)

# Debugging WebScript

WebScript provides methods that are useful for debugging: __logWithFormat:__ and several trace methods. Using these methods in conjunction with launching your application from a command shell provides you with a fairly complete picture of your running application.

## Launching From the Command Line

To debug your application, you should launch it from the command line so that you have better control over the executable and so that you'll be able to see messages written to standard output or standard error.
To start a WebObjects application from the command line:

- Locate the application executable.

If you don't have compiled code and haven't built a custom executable, use the __WODefaultApp__ executable located in _NeXT_Root___/NextLibrary/Executables__.

- Change directories to the directory in which the application executable is located.
- Start the application by invoking the executable as follows:

```
    ApplicationExecutable -d DocumentRoot RelativeApplicationDirectory
```


You must provide a minimum of two arguments to the executable: the HTTP server's document root and the application directory relative to <DocumentRoot>__/WebObjects__. For example, the resources for HelloWorld are located in <DocumentRoot>__/WebObjects/Examples/HelloWorld.woa__, so HelloWorld's relative application directory is __Examples/HelloWorld__. (You must leave off the __.woa__ extension.) You'd use the following command to start HelloWorld:

```
    WODefaultApp.exe -d c:/netscape/ns-home/docs Examples/HelloWorld
```


To start a compiled application, you'd use the command:

```
    AppName.exe -d DocumentRoot RelativeApplicationDirectory
```


For example, if you wanted to run an application named Registration.woa, you would change directories to the Registration.woa directory and then type:

```
    Registration.exe -d c:/netscape/ns-home/docs
        MyApplications/Registration
```


assuming you've placed Registration in a directory called __MyApplications__.

__Note:__ If you're using Windows NT, be sure to use forward slashes in the arguments to the application executable, even if you're running the application from the DOS Command Prompt.

- In your browser, open the URL you'd normally use to launch your application:

```
    http://localhost/cgi-bin/WebObjects/MyApplications/Registration
```


As your application runs, the output from __logWithFormat:__ and other information about your application is displayed in the command shell window.

## logWithFormat:

The WebScript method __logWithFormat:__ writes a formatted string to __stderr__. Like the __printf()__ function in C, this method takes a format string and optionally, a variable number of additional arguments. For example, the following code excerpt prints the string: "The value of myString is Elvis":

```
myString = @"Elvis";
[self logWithFormat:@"The value of myString is %@", myString];
```


When this code is parsed, the value of __myString__ is substituted for the conversion specification __%@__. The conversion character @ indicates that the data type of the variable being substituted is an object (that is, of the __id__ data type).
Because WebScript only supports the data type __id__, the conversion specification you use must always be __%@__. Unlike __printf()__, you can't supply conversion specifications for primitive C data types such as %d, %s, %f, and so on.
Perhaps the most effective debugging technique you can use in WebScript is to use __logWithFormat:__ to print the contents of __self__. This causes WebScript to output the values of all of your variables. For example, putting the statement:

```
[self logWithFormat:@"The contents of self in register are %@", self];
```


at the end of the __register__ method in the Registration application's __Main.wos__ script produces output that resembles the following:

```
The contents of self in register are <WOComponent 0xafe04
     message = You have been successfully registered.
     newPerson = {
   address = "Graceland\015\nNashville, TN";
   email = "elvis@graceland.com";
   name = Elvis;
}>
```


__Note:__  If you're writing Java code, the __logWithFormat:__ method is named __logString__ and you can send it only to WebApplication objects. Instead of using __printf()__ conversion specifications, it uses concatenation. Here's how you'd write the same line of code in Java:

```
this.application().logString("The contents of this in register are "
        + this.toString());
```


## Trace Methods

WOApplication provides trace methods that log different kinds of information about your running application. These methods are useful if you want to see the call stack. The trace methods are described in the following table:

| __ Method__ | __ Description__ |
|  - trace |  Enables all tracing. |
|  - traceAssignments |  Logs information about all assignment statements. |
|  - traceStatements |  Logs information about all statements. |
|  - traceScriptedMessages |  Logs information when an application enters and exits a scripted method. |
|  - traceObjectiveCMessages |  Logs information about all Objective-C method invocations. |

```
```


To use any of the trace methods, you must run your application from a command shell.
You use the trace methods wherever you want to turn on tracing. Usually, this is in the __init__ method of a component or the application:

```
- init {
    [super init];
    [self.application traceAssignments:YES];
    [self.application traceScriptedMessages:YES];
    return self;
}
```


__Note:__  The trace methods are not available in the Java interface.

[!Table of Contents](DevTasks.book.md) [!Next Section](DebuggingCompiled.md)
