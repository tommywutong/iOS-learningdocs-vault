---
title: Cocoa Scripting Guide
apple_id: TP40002164
resource_type: Guide
platform: macOS
topic: Interapplication Communication
technology: null
published: '2008-03-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_debugging/SAppsDebugging.html
archived_at: '2026-07-15T07:18:50.772661Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Cocoa Scripting Guide](Introduction%20to%20Cocoa%20Scripting%20Guide.md)


[Next](Cocoa%20Scripting%20Classes%20and%20Categories.md)[Previous](Script%20Commands.md)

# Testing, Debugging, and Performance

This chapter lists tactics you can use to test and debug your scriptable Cocoa application. It also provides a brief list of possible performance issues, including links to performance information elsewhere in this document.

As noted in [Designing for Scriptability](Designing%20for%20Scriptability.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsnzyfvbeeq2cineuuri), planning for testing should be an integral part of your application design and implementation. Your test plan should include regular milestones to confirm each step of scriptability. These can include:

1. Validating your terminology (verifying that your sdef is semantically correct).
2. Verifying that the application is receiving Apple events.
3. Verifying that your script commands get instantiated and executed when the corresponding Apple events are received.
4. Verifying that the expected methods are called to get and set scriptable values.
5. Verifying that support for more complex script statements you support, such as `every` and `whose` statements, is working. (For examples of these types of statements, see the object specifiers for the filter (`whose`) and `every` reference forms in [Table 6-1](Object%20Specifiers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnrufvbuqmznknlte).)

Your test plan should also include performance testing. For more information, see [Performance Issues for Scriptability](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobrfvjvomi).

As you implement your application, you should build up a suite of test scripts to exercise its scriptability. And the more features you make scriptable, the more your script testing can serve as a testbed for your entire application.

From Script Editor, you can cut and paste the Event Log output from your test scripts and save it for later regression testing. As you make changes to your application, whether in script-specific code or not, you can compare the current output to the saved version to help you find possible side-effects.

Make your test scripts as complete as possible by following these guidelines:

- Exercise the entire hierarchy of your AppleScript object model: for example, have your scripts get and set every accessible property of every accessible object, using `repeat` loops and `every` statements.

  After getting and setting values, use a `log` statement to log the `properties` property of the objects to record the changes.
- Test access by every applicable reference form: for example, iterate over scriptable collections by name, by ID, by index, and by any other form that applies. (See [Table 6-1](Object%20Specifiers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnrufvbuqmznknlte) for a list of reference forms.)
- Test creating new objects by using the `make` command and specifying properties.

  For example, this script tests Sketch by creating a new graphic object in an existing document:

  __Listing 8-1__  Simple test script

```
tell application "Sketch"
    tell document "Test Doc.sketch"
        make new circle at end with properties {x position:50, y position:30, width:60, height:60}
    end tell
end tell
```
- Test using `whose` clauses: they're a powerful scripting feature that is important to users.

  A `whose` clause can provide a good stress test for your scriptability, and may turn up performance issues.
- Run scripts that make changes then reverse them, then check whether the end result matches the starting point.
- Run your test scripts regularly, even after code changes that you don't expect to affect your application's scriptability.

For additional information on using test scripts, including examples, see [Implementing a Verb-First Command—Align](Script%20Commands.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2delktk43q) and [Implementing an Object-First Command—Rotate](Script%20Commands.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2delktk4za).

Turning on Cocoa’s debugging output for scripting will help you debug your scriptable application. Debugging output shows information such as

- loaded scriptability information (from an sdef file or from script suite and script terminology files)
- executed script commands
- the arguments to executed commands

To turn on this support, you set a debugging value in the user defaults system provided by OS X. Default values in the global domain are accessible to any application. For example, during development, an application can set a user default value that a debugger checks to determine whether to display certain debug information. That’s the approach that Cocoa takes to log debug information for scripting.

To turn on Cocoa’s debugging output for scripting, you do the following:

1. Open a Terminal window. Terminal is available in `/Applications/Utilities`.
2. Enter the following line and press Return to execute it:

```
defaults write NSGlobalDomain NSScriptingDebugLogLevel 1
```

   You can turn off debugging output with a line like this:

```
defaults write NSGlobalDomain NSScriptingDebugLogLevel 0
```

   You can display all the current values in the global domain with a line like this:

```
defaults read NSGlobalDomain
```
3. If your application is already running, quit the application.
4. If you launch your application from the Finder, look for debug information in the Console application (available in `/Applications/Utilities`). If you launch your application in Xcode, look for debug information in the Debug Console pane or in the Run pane.

You will not see any debugging information until the application receives an Apple event that causes it to execute a script command (and in turn, to load the application’s scriptability information). You can view debugging information for either a development or a deployment build of your application.

If you only want to turn on script debugging for a particular application, you can use the application domain. The application domain is identified by the bundle identifier of the application, typically a string in the form of a Java-style package name (think of it as a reverse URL). For example, you could turn on script debug logging for the Sketch sample application (available from Apple) by executing the following line:

```
defaults write com.apple.CocoaExamples.Sketch NSScriptingDebugLogLevel 1
```

To read this value or to reset it to zero, use one of the following two lines:

```
defaults read com.apple.CocoaExamples.Sketch NSScriptingDebugLogLevel
defaults write com.apple.CocoaExamples.Sketch NSScriptingDebugLogLevel 0
```


The following listing shows a script that changes the height of a circle in a Sketch application window.

```
tell application "Sketch"
    tell the first document
        set height of first circle to 100
    end tell
end tell
```

Listing 8-2 shows the debug output from running the script shown above on a version of Sketch that supplies its scriptability information with an sdef file. The output shows the command listed as `Command: Intrinsics.set`, because Cocoa scripting automatically supplies information for various "intrinsic" AppleScript terminology.

The debug information includes the direct parameter (the property to set, `height`), the receivers for the command (a specifier for `circles 1 of orderedDocuments 1`), and the arguments for the command (the value to set, `100`). You can also see that Sketch returns a result of `null`, because no return value is needed for a `set` command.

__Listing 8-2__  Debug scripting output for sdef-based Sketch

```
2006-02-24 13:51:29.951 Sketch[8245] Command: Intrinsics.set
    Direct Parameter: <NSPropertySpecifier: height>
    Receivers: <NSIndexSpecifier: circles 1 of orderedDocuments 1>
    Arguments: {Value = <NSAppleEventDescriptor: 100
2006-02-24 13:51:29.953 Sketch[8245] Result: (null)
```

Listing 8-2 shows output from running the same script on a version of the Sketch application that supplies its scriptability information in the script suite format. There are two main differences from the previous listing:

- First, the output shows the Standard suite (formerly called the Core suite), Text suite, and Sketch suites—you will see this information the first time the application loads those suites in response to receiving an Apple event.
- Second, the command is listed as `Command: NSCoreSuite.Set`, reflecting the suite format for providing intrinsic scriptability information.

__Listing 8-3__  Debug scripting output for script suite-based Sketch

```
2005-05-20 13:38:39.736 Sketch[2005-05-20 13:40:55.215 Sketch[516] Suite NSCoreSuite, apple event code 0x3f3f3f3f
2005-05-20 13:40:55.223 Sketch[516] Suite NSTextSuite, apple event code 0x3f3f3f3f
2005-05-20 13:40:55.253 Sketch[516] Suite Sketch, apple event code 0x736b7463
2005-05-20 13:40:55.259 Sketch[516] Command: NSCoreSuite.Set
    Direct Parameter: <NSPropertySpecifier: height>
    Receivers: <NSIndexSpecifier: circles 1 of orderedDocuments 1>
    Arguments: {Value = 100; }
    Key Specifier: <NSPropertySpecifier: height>
2005-05-20 13:40:55.261 Sketch[516] Result: (null)
```


To view an sdef file in a dictionary viewer, double-click it in the Finder. Double-clicking an sdef file in an Xcode project similarly opens it in a dictionary viewer window. To view or edit the XML for the file, open the sdef file with any plain text editor; in Xcode, select the sdef file and choose File > Open As > Plain Text File.

As you add information to an sdef file, you can verify that the file is still valid (semantically correct) by opening it with Script Editor or Xcode. If those applications cannot parse the file, you will see “Nothing to see here; move along.” displayed in the dictionary viewer. You can then open the Console log to see specific parsing errors.

You can also validate your sdef with the `xmllint` tool, using a command line like the following:

```
xmllint --noout --postvalid --xinclude YourApp.sdef
```

See the xmllint man page for more details.

The `description` methods of various Cocoa scripting classes can provide useful information. You can view this information during a debugging session with the `print object` command in the GDB debugger. (This command can be abbreviated as `po`.) For example, you can examine the information Cocoa scripting has extracted from your sdef file or script suite and script terminology files. To do so, follow these steps:

1. Debug the application in Xcode.
2. Break anywhere in the application.
3. Open the Debugger Console Log and enter this command:

```
print object [NSClassFromString(@"NSScriptSuiteRegistry") sharedScriptSuiteRegistry]
```

As a result of these steps, you will get a detailed listing of the scriptability information `NSScriptSuiteRegistry` has loaded for the application. Listing 8-4 shows just the `get` and `set` command information from that output.

__Listing 8-4__  Partial output of NSScriptSuiteRegistry information

```
 Command: get ('core'/'getd')
        Implementation class: NSGetCommand
        Name: "get", description: "Returns the value of the specified object(s)."
        Unnamed argument ('----'), type: specifier ('obj '), optional: no
            (No user-readable name or description needed for unnamed arguments)
        Result type: any ('****')
            Description: <none>
    Command: set ('core'/'setd')
        Implementation class: NSSetCommand
        Name: "set", description: "Sets the value of the specified object(s)."
        Unnamed argument ('----'), type: specifier ('obj '), optional: no
            (No user-readable name or description needed for unnamed arguments)
        Argument: Value ('data'), type: any ('****'), optional: no
            Name: "to", description: "The new value."
        Result type: <none> ('null')
            Description: <none>
```

Similarly, you can get descriptions of instances of the `NSScriptCommand` and `NSAppleEventDescriptor` classes. For example, you can use the following command at a break point during script command execution:

```
print object [NSClassFromString(@"NSScriptCommand") currentCommand]
```

If you need to know more about specific Apple events received by your application, you can examine the information for the Apple event that triggered the current scripting command with a statement like the following:

```
print object [[NSClassFromString(@"NSScriptCommand") currentCommand] appleEvent]
```

You can get similar information by using `NSLog` statements in your application, allowing you to track execution through your code as you implement scriptability support. For example, the Sketch application contains the file `my.h`. That file provides definitions to turn logging on or off based on the value of `myMasterSwitch`, shown in Listing 8-5. Set it to `1`, recompile, and any `NSLog` statements in your application will be executed:

__Listing 8-5__  Turning on log statements

```
#define    myMasterSwitch    ( 0 )

#if        myMasterSwitch
#define    myLog1(x)    NSLog(x)
#define    myLog2(x,y)    NSLog(x,y)
#else
#define    myLog1(x)
#define    myLog2(x,y)
#endif
```

To dump information for a command object in Sketch, you could place this `NSLog` statement in the `performDefaultImplementation` method of the `SKTAlignCommand` class:

```
myLog2(@"SKTAlignCommand performDefaultImplementation command = %@", self);
```

Here's the result, from Xcode's Console window (after setting `myMasterSwitch` to `1` in `my.h` and recompiling):

__Listing 8-6__  NSLog output for SKTAlignCommand

```
2006-02-01 13:15:31.622 Sketch[1662] ME SKTAlignCommand performDefaultImplementation command = Sketch Suite.align
    Direct Parameter: <CFArray 0x3d3780 [0xa073a150]>{type = mutable-small, count = 2, values = (
    0 : <NSIndexSpecifier: graphics 1 of orderedDocuments named "SketchDoc">
    1 : <NSIndexSpecifier: graphics 2 of orderedDocuments named "SketchDoc">
)}
    Receivers: (null)
    Arguments: {
        "" = (
            <NSIndexSpecifier: graphics 1 of orderedDocuments named "SketchDoc">,
            <NSIndexSpecifier: graphics 2 of orderedDocuments named "SketchDoc">
        );
        toEdge = 1986359907;
    }
```

In this output, you can see that the direct parameter uses index specifiers to specify two graphics. The direct parameter (with the same two specifiers) is also displayed in the arguments array, identified by the empty string `(""`) key. The edge to align the graphics to is also provided as an argument, with the key `"toEdge"`.

There are a number of Apple event debugging tips that work well both for applications that use the Apple Event Manager directly and those that use frameworks such as Cocoa. For example, the chapter [Testing and Debugging Apple Event Code](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleEvents/debugging_aepg/debugging_aepg.html#//apple_ref/doc/uid/TP40001449-CH210) in _[Apple Events Programming Guide](../../Apple%20Script/Apple%20Events%20Programming%20Guide/Introduction%20to%20Apple%20Events%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbz)_ describes how you can:

- Determine if your application is receiving Apple events (and log the information in those events).
- Use Script Editor as a test tool to send events to your application.
- Observe Apple events for multiple applications.
- Find third-party resources for monitoring and debugging Apple events and scriptable applications.

Performance considerations should be an integral part of your test plan, so that as you implement your application, you always know when its performance increases or decreases. You may have a pretty good idea of which code paths are most likely to cause trouble, but acquiring regular timing information will help avoid surprises.

In general, you won't have to worry about performance in receiving Apple events and translating them into command objects, as applications don't commonly receive great numbers of Apple events, and Cocoa can decode them quite rapidly. However, your application should not rely on Apple events to communicate information that is more suitable to a lighter weight form of communication, such as notifications. See [Kernel and Device Drivers Layer](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/OSX_Technology_Overview/SystemTechnology/SystemTechnology.html#//apple_ref/doc/uid/TP40001067-CH207) in _[Mac Technology Overview](../../Mac%20OSX/Mac%20Technology%20Overview/About%20Developing%20for%20Mac.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrx)_ for more information on the interprocess communications options available in OS X.

If an Apple event initiates a script command that requires your application to perform an asynchronous (and perhaps lengthy) operation, you can suspend the command and resume it when the operation is complete, as described in [Suspending and Resuming Apple Events and Script Commands](How%20Cocoa%20Applications%20Handle%20Apple%20Events.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgiztsljrgeztinzxha). Depending on the operation, you may want to provide progress information while the command is suspended. However, suspending a command (or an Apple event) does not prevent the originating script from timing out if your application takes too long to respond to an event.

Performance can also be an issue in determining how to implement a particular application script command. For example, it may be easier to implement an object-first command, where the command calls a method for each object on which it operates. However, using an object-first approach may have performance consequences in cases where significant overhead is incurred for each object, especially when dealing with large numbers of objects. As an alternative, using the verb-first approach may allow you to minimize overhead and optimize operations on multiple objects. These approaches are described in [Object-first Versus Verb-first Script Commands](Script%20Commands.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2delktk4yq).

For most applications, performance of Cocoa scripting's default handling of `whose` clauses should be sufficient. However, if you find the need to speed it up, you can use the mechanism described in [Implementing A Method for Evaluating Object Specifiers](Object%20Specifiers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnrufvbuqmznknltm).

Cocoa scripting relies on key-value coding (KVC) to get and set values and find objects in your application. Performance of KVC can vary depending on the methods you implement to support it. This is especially true for operations on arrays. For tips on handling these issues, see [Performance Considerations With KVC](Getting%20and%20Setting%20Properties%20and%20Elements.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnrufvbuqmjyfvjvony).

For a general introduction to performance issues, see _[Performance Starting Point for OS X](https://developer.apple.com/library/archive/referencelibrary/GettingStarted/GS_Performance/index.html#//apple_ref/doc/uid/TP30001082)_.

[Next](Cocoa%20Scripting%20Classes%20and%20Categories.md)[Previous](Script%20Commands.md)

