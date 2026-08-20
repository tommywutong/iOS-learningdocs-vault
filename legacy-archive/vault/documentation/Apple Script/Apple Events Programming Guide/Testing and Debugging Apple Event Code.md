---
title: Apple Events Programming Guide
apple_id: TP40001449
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-10-31'
source_url: https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleEvents/debugging_aepg/debugging_aepg.html
archived_at: '2026-07-15T05:19:29.245370Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Apple Events Programming Guide](Introduction%20to%20Apple%20Events%20Programming%20Guide.md)


[Next](Selected%20Apple%20Event%20Manager%20Functions.md)[Previous](Writing%20and%20Installing%20Coercion%20Handlers.md)

# Testing and Debugging Apple Event Code

To test and debug your Apple event code you can generally use the same techniques and tools you use with any code. For example, Xcode contains a full-featured source-level debugger that lets you set breakpoints and step through your code line by line. For C, C++, and Objective-C code, Xcode uses GDB, the debugger from the [GNU Project](http://www.gnu.org/). You can use Xcode’s graphical interface to GDB or you can enter commands directly into the GDB console. For more information, see “Debugging” in Xcode Help and [Debugging With GDB](https://developer.apple.com/documentation/DeveloperTools/gdb/gdb/gdb_toc.html).

The remainder of this chapter provides tips that are specific to debugging code that works with Apple events.

The easiest way to determine if your application is receiving a particular event is to set a breakpoint in the event handler for that event, then send an event of that type to your application. There are several ways to send Apple events to your application:

- You can create and send events that target your application from within the application itself or from a test application. For more information, see [Creating and Sending Apple Events](Creating%20and%20Sending%20Apple%20Events.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrqhewueqkcirauur2c). This approach can be useful if you’re setting up a test suite and want to thoroughly test how your application responds to a variety of events.
- You can use Script Editor to send Apple events to your application.

  For example, you can execute this one-line script to send your application a `quit` event:

  __Listing 8-1__  A simple script to quit an application

```
    tell app "MyApplication" to quit
```

  If your application is scriptable, you may prefer to set up a test suite of scripts to thoroughly exercise the events you support, rather than perform the same task in a test application.

  For additional information on sending Apple events with Script Editor, see [Script Editor is an Apple Event Test Tool](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrrgawugscejfbuqqsb).
- You can use the Mac OS to send Apple events to your application.

  For example, you can select an application document in the Finder and double-click it to send an `open documents` event to the application. See [Handling Apple Events Sent by the Mac OS](Responding%20to%20Apple%20Events.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrqgywuerkkijcekr2j) for a list of the events the Mac OS sends to applications.

What if you’re sending events to your application, but the debugger never reaches the breakpoints you set in your Apple event code? One simple approach is to install a single Apple event handler with the event type and event class set to `typeWildCard`. Any Apple event your application receives will be dispatched to this handler, so a breakpoint in the handler should allow you to verify whether the application is actually receiving events.

Once you know your application is receiving events, you can take a closer look at the events using the information provided in [Examining Apple Events](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrrgawugsceijaucrkf). That information is also useful if you never hit the breakpoint in your wildcard handler. For example, you can examine the test events you are sending to see if they correctly target your application.

The Script Editor application, located in `/Applications/AppleScript`, is a useful tool for working with Apple events. If your application is scriptable, you can use Script Editor to write and execute scripts that target your application, resulting in Apple events being sent to the application.

Even if your application is not fully scriptable, you can use Script Editor to send it events such as the `open application` and `quit` events that your application usually receives from the Mac OS. Listing 8-1 shows an example of this.

In addition, you can use Script Editor to construct and send Apple events using raw format, in which you enclose actual four-character codes in special characters to specify an event. For example, Listing 8-2 shows how to use the raw format to send an `open location` command to the Safari application and open the specified web page.

__Listing 8-2__  Sending a raw event to open an URL

```
tell application "Safari"
    «event GURLGURL» "http://www.apple.com/"
end tell
```

When you compile this script, Script Editor examines Safari’s scripting dictionary and converts the second line to this:

```
    open location "http://www.apple.com/"
```

However, for an application that doesn’t have a scripting dictionary, the raw code is not replaced by an equivalent term, but the Apple event can still be sent and understood (if the application supports it).

You enter the special characters that surround the raw code (called double angle brackets or guillemets) by typing Option-\ and Option-Shift-\. For additional information, see [Double Angle Brackets in Results and Scripts](https://developer.apple.com/documentation/AppleScript/Conceptual/AppleScriptLangGuide/AppleScript.5f.html) in [AppleScript Language Guide](https://developer.apple.com/documentation/AppleScript/Conceptual/AppleScriptLangGuide/index.html).

[Turning on Apple Event Logging](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrrgawugsceirfecqsf) shows how you can examine the Apple events Script Editor sends and receives.

There are several available mechanisms for examining the contents of Apple events that your application sends and receives.

You can set environment variables in a Terminal window so that any Apple events sent or received by an application launched in that window are logged to the window in a human-readable format. Listing 8-4 shows how you would do this if you’re working with the C shell.

__Listing 8-3__  Turning on logging for sent and received Apple events in the C shell

```
%setenv AEDebugSends 1; setenv AEDebugReceives 1
```

If you are using the `bash` shell you, you can use the form shown in Listing 8-4.

__Listing 8-4__  Turning on Apple event logging in the Bash shell

```
%export AEDebugSends=1; export AEDebugReceives=1
```

To see which Apple events an application sends and receives, you set these environment variables, then launch the application in a Terminal window. For example, to see what events the Script Editor application sends, you can execute the line in Listing 8-5. Once the Script Editor launches, you can compile and execute scripts and examine, in the Terminal window, the Apple events that are generated.

__Listing 8-5__  Launching Script Editor in Terminal

```
% /Applications/AppleScript/Script\ Editor.app/Contents/MacOS/Script\ Editor
```

Listing 8-6 shows how to perform the same task with the Finder, a scriptable application that may send Apple events to your application.

__Listing 8-6__  Launching Finder in Terminal

```
% /System/Library/CoreServices/Finder.app/Contents/MacOS/Finder
```

This technique for examining Apple events works for both Carbon and Cocoa applications. For example, Listing 8-7 shows the output for a `reopen` Apple event sent to a Carbon application when you click on its icon in the Dock.

__Listing 8-7__  Output of a reopen Apple event in Terminal

```
AE2000 (968): Received an event:
------oo start of event oo------
{ 1 } 'aevt':  aevt/rapp (ppc ){
          return id: 22609967 (0x159002f)
     transaction id: 0 (0x0)
  interaction level: 112 (0x70)
     reply required: 0 (0x0)
             remote: 0 (0x0)
  target:
    { 1 } 'psn ':  8 bytes {
      { 0x0, 0x60001 } (Dock)
    }
  optional attributes:
    { 1 } 'reco':  - 1 items {
      key 'optk' -
        { 1 } 'list':  - 1 elements {
          { 1 } 'keyw':  4 bytes {
            'frnt'
          }
        }
    }

  event data:
    { 1 } 'aevt':  - 1 items {
      key 'frnt' -
        { 1 } 'bool':  1 bytes {
          false
        }
    }
}
------oo  end of event  oo------
```

From the formatted output in Listing 8-7, you can identify various information in the Apple event. For example, `aevt/rapp` is the event class/event ID pair for the event. You can look up these values in the Apple Event Manager headers and see that `'rapp'` is the value of the constant `kAEReopenApplication`, defined in `AERegistry.h`. For this event, no reply is required (`reply required: 0`), but if a reply were required, the target would be the Dock (`target: { 1 } 'psn ': 8 bytes { { 0x0, 0x60001 } (Dock) }`), which sent the Apple event.

Although Apple event log information can be somewhat cryptic, you can see that the event contains an optional attribute containing boolean data with the value false and the key `'frnt'`. This indicates that the application was not frontmost at the time the `reopen` event was sent (when you clicked the application icon in the Dock). If the application is in front, the event data will contain the value `false`.

You can open multiple Terminal windows, turn on debugging output in each, and debug your own application and other applications that it sends Apple events to or receives Apple events from at the same time.

The GDB debugger provides a `call` command that you can use to call routines such as Apple Event Manager functions. The section [“Using AEPrint\* with GDB”](https://developer.apple.com/technotes/tn/tn2045.html#dssyntaxcprgdb) in Technical Note TN2106, [AEBuild\*, AEPrint\*, and Friends](https://developer.apple.com/technotes/tn/tn2045.html), shows how you can set breakpoints in GDB and print out the contents of Apple events in a readable format. While this approach is a little more complex, it provides a good example of setting breakpoints on Apple Event Manager routines and examining Apple events.

There are a number of third-party tools, some of them quite powerful, for monitoring and debugging Apple events and scriptable applications. You can find some of them listed at [AppleScript Resources](http://www.apple.com/applescript/resources.html).

[Next](Selected%20Apple%20Event%20Manager%20Functions.md)[Previous](Writing%20and%20Installing%20Coercion%20Handlers.md)

