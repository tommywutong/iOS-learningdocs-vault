---
title: Scripting Bridge
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2009/07/Scripting-Bridge/'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:fc24312897b7c7f6'
translated: false
---

> 原文：[Scripting Bridge](https://belkadan.com/blog/2009/07/Scripting-Bridge/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [What Happened to Dockyard?](https://belkadan.com/blog/2009/07/What-Happened-to-Dockyard/)

[Auspicious Continuation](https://belkadan.com/blog/2011/05/Auspicious-Continuation/) »

« [Safer Plugin Categories](https://belkadan.com/blog/2009/04/Safer-Plugin-Categories/?tag=cocoa)

[Automatic Reference Counting](https://belkadan.com/blog/2011/06/Automatic-Reference-Counting/?tag=cocoa) »

## [Scripting Bridge](#)

Recently I had occasion to deal with the Finder, beyond what NSFileManager or NSWorkspace could handle. Now, the easy way to do this is through AppleScript, and Cocoa does provide a way to run AppleScripts (NSAppleScript). The trouble is, (a) NSAppleScript is slow and only runs on the main thread, and (b) you can’t pass input easily.

AppleScript is built on Apple events, a mid-to-high-level form of interprocess communication that’s been around since System 7. Apple events can be constructed and sent off using either pure C code (what’s now part of the CoreServices framework) or the Objective-C wrapper, NSAppleEventDescriptor, in the Foundation framework. But constructing a proper Apple event is a little onerous, and again, customizing the message being sent has to be done interspersed with the building of the event. Even with the convenient AEBuildAppleEvent() function, which takes a stringified version of the event, it’s just not transparent and simple.

Enter Scripting Bridge. It was announced and trumpeted (at moderate volume) way back before Leopard was released—it is, of course, a 10.5-only feature. And somehow it slipped beneath my radar, though of course most of my apps were/are backwards compatible to 10.4 or even 10.3. The ADC site had a rather trivial example that actually shows the most important part of the bridge: it looks like Objective-C and uses regular Foundation classes whenever possible.

> For example, using the Bridge, you could get the name of the current iTunes track with the following line of code:
> 
> ```
> NSString *currentTrackName = [[iTunes currentTrack] name];
> ```
> 
> The Scripting Bridge uses native Cocoa data types, such as NSString and NSArray, requires far less code than using an NSAppleEventDescriptor, and runs more than twice as fast as a precompiled NSAppleScript.

The fallout benefit was that all the languages bridged with the Cocoa runtime, like Ruby, Python, and F-script, also get this functionality. It’s in that context that I’ve heard Scripting Bridge mentioned since the Leopard launch. But let’s take a look at what it would do to a bit of Dockyard code:

```
result = AEBuildAppleEvent(kAECoreSuite, kAESetData, typeApplicationBundleID, systemEventsIDChars, systemEventsIDLength,
  kAutoGenerateReturnID, kAnyTransactionID, &event, NULL,
  (([OrientationLeft isEqual:[defaultsDict objectForKey:OrientationKey]]) ?
    "data:left,'----':'obj '{form:prop,want:prop,seld:dplo,from:'obj '{form:prop,want:prop,seld:dpas,from:()}}" :
    [OrientationRight isEqual:[defaultsDict objectForKey:OrientationKey]] ?
      "data:righ,'----':'obj '{form:prop,want:prop,seld:dplo,from:'obj '{form:prop,want:prop,seld:dpas,from:()}}" :        
      "data:bott,'----':'obj '{form:prop,want:prop,seld:dplo,from:'obj '{form:prop,want:prop,seld:dpas,from:()}}"));
if (result == aeBuildSyntaxNoErr)
{
  result = AESendMessage(&event, NULL, kAENoReply, 0);
  AEDisposeDesc(&event);
}
```

Bleah. It works. It’s a lot more efficient than calling out to an AppleScript. But it’s certainly not clear what’s going on. Compare that to this (though untested):

```
id orientation = [defaultsDict objectForKey:OrientationKey];
SystemEventsApplication *sysEvents = [SBApplication applicationWithBundleIdentifier:@"com.apple.systemevents"];
if ([OrientationLeft isEqual:orientation]) {
  sysEvents.dockPreferences.location = SystemEventsDplsLeft;

} else if ([OrientationRight isEqual:orientation]) {
  sysEvents.dockPreferences.location = SystemEventsDplsRight;

} else {
  sysEvents.dockPreferences.location = SystemEventsDplsBottom;
}
```

Which one’s easier to read?

So, there is a downside. Scripting Bridge is very simple when it works, but downright impossible to debug when it doesn’t. With several layers of indirection and insulation from the Apple event architecture, you can’t really do things “manually” with Scripting Bridge. (There is a `-propertyWithClass:code:` method that lets you override some default behavior, particularly when SB isn’t able to determine the right class for you.) The one error-recovery method isn’t actually very useful for error-recovery, and it’s the one place where the framework unexpectedly drops you down to the C level. I would expect them to at least wrap the event in an NSAppleEventDescriptor, but no…

In the end, I was able to do almost everything I needed to while staying above the bridge. Debugging is hard, but there generally _is_ a way to do everything. (Hint: use URLs to refer to filesystem items, not paths.) But there is another high-level alternative: [appscript][\\1]. Appscript is a very similar framework optimized for Python, Ruby, and then Objective-C. The project states that it isn’t yet feature-complete for Objective-C, but it’s both stable, being around since Panther, and still under active development. …But I haven’t used it myself.

Now, _implementing_ scriptability is still unfortunately annoying if your app doesn’t fit a nice model. Fortunately we’ve been insulated from raw AppleEvents on that end for a while now. I’ll try to document my efforts in that field next time it comes around.

This entry was posted on [July](https://belkadan.com/blog/2009/07) 21, [2009](https://belkadan.com/blog/2009) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Cocoa](https://belkadan.com/blog/tags/cocoa)
