---
title: 'Interprocess communication: snooping, intercepting and subverting | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2009/02/interprocess-communication-snooping.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:80498927a5a45fff'
translated: false
---

> 原文：[Interprocess communication: snooping, intercepting and subverting | Cocoa with Love](https://www.cocoawithlove.com/2009/02/interprocess-communication-snooping.html)　·　Cocoa with Love (Matt Gallagher)

When Xcode is running, Interface Builder seems to magically know which classes, methods and variables are available. Where does Interface Builder get this information? How can you recreate this effect when editing source files in an external editor without Xcode running? This is the story of how I investigated the communication between Xcode and Interface Builder, so that I could recreate it for myself.

## Xcode and Interface Builder, sitting in a tree...

Prior to Mac OS X 10.5 (Snowless Leopard), if you made a change to your classes, `IBActions` or `IBOutlets`, you needed to manually instruct Interface Builder to re-read the relevant header files before these changes were visible in Interface Builder.

With Xcode 3 and Interface Builder this has changed. If you add a new class to a project in Xcode, it is immediately available in class lists when you switch to Interface Builder. Similarly, change an `IBAction` or `IBOutlet` in Xcode, save the header file and switch to Interface Builder: your changes are immediately visible.

And yet, if you quit Xcode and edit the same files in an external editor, Interface Builder doesn't automatically detect the changes. Clearly, Interface Builder is using something other than basic file monitoring to detect the changes.

## NSDistributedNotificationCenter

The simplest way for applications in Mac OS X to communicate is through the distributed notification center, `NSDistributedNotificationCenter` in Foundation or `CFNotificationCenterRef` (initialized with `CFNotificationCenterGetDistributedCenter`) in CoreFoundation. This allows applications to broadcast dictionaries of objects to any application interested in listening.

To see if Xcode is communicating to Interface Builder using a `NSDistributedNotificationCenter`, I needed to configure the process "distnoted" (the daemon which manages the `NSDistributedNotificationCenter`) to log notifications so I could see if anything relevant is broadcast.

Apple's [Technical Note TN2124: Mac OS X Debugging Magic](http://developer.apple.com/technotes/tn2004/tn2124.html) explains _some_ of what's needed. On the command line:

```objc
sudo touch /var/log/do_dnserver_log
```

Apple's documentation leaves out the next (required) steps:

```objc
sudo touch /var/log/dnserver.log
sudo chown daemon /var/log/dnserver.log
```

and then restart.

Sadly for my investigation, this isn't how Xcode communicates to Interface Builder. Looking at the log when Xcode and Interface Builder are started, reveals nothing relevant from either program.

## NSPortNameServer

I observed the next clue to how Xcode and Interface Builder communicate by starting two copies of each. In this setup, a new class created in the first instance of Xcode will be visible in both instances of Interface Builder but a new class created in the second instance of Xcode will not be detected by either copy of Interface Builder.

This type of behavior is typical of named port connections.

A quick Mac OS X lesson: almost all inter-process communication on the Mac is built on Mach Ports underneath. Mach Ports are a way to pass messages (blocks of data) between processes.

The easiest way to for a process advertise a Mach Port so that other processes may connect to it, is to give it a name. Network names are registered using `NSNetService` (Bonjour) but on a single host (as is far more likely in this case) network names are registered through `NSPortNameServer`.

`NSPortNameServer` is, in turn, handled by "launchd" (the daemon that Apple created to replace init, cron, inetd and others). So to see if the `NSPortNameServer` supposition was correct, I needed to get "launchd" to output log information about Port Names.

Again, I followed [Technical Note TN2124: Mac OS X Debugging Magic](http://developer.apple.com/technotes/tn2004/tn2124.html) to learn how to do this:

```objc
sudo launchctl log level debug
```

And once again, the information contained in the Tech Note turned out to be insufficient. Apple really need to update this Tech Note.

I wrote a program to send thousands of port name lookups on random names but no logging was output. However, I could see that the "syslog" process (the process that records logging information) was very busy but it wasn't recording any information anywhere.

This is a typical "syslog.conf" problem: you must direct "syslog" information for the relevant "facility" and "level" to a destination. Unfortunately, the "facility" name that Apple gives for "launchd" in Tech Note TN2124 is wrong. Instead, I appended a "`*.debug`" line to my "syslog.conf" file and sent the output to /var/log/debug.log instead.

This finally worked: "launchd" information (and debug information from other processes) found its way to the debug log file.

Finding the correct piece of information in this haystack looked like an impossible task until I started Interface Builder without Xcode running:

```objc
Mach service lookup failed: PBXProjectWatcherServerConnection-3.1.2
```

It doesn't follow Apple's own naming policy for Port Names (which would be something more like "com.apple.Xcode.projectwatcherserverconnection.3.1.2") but at least it is clear about its function.

## NSConnection

At this point, the data sent over the Mach Port could be anything. How do you work out the format? I hoped that Apple used an `NSConnection` since the Cocoa libraries will handle this automatically for me.

Fortunately, running the following line of Cocoa Objective-C:

```objc
id rootObject =
    [NSConnection rootProxyForConnectionWithRegisteredName:
        @"PBXProjectWatcherServerConnection-3.1.2" host:nil];
```

cleanly returned an object of type `PBXProjectWatcherManager`, revealing that yes, this is a regular `NSConnection` served over the Mach Port.

## Recreating PBXProjectWatcherManager

The final step in replacing Xcode's role in keeping Interface Builder up-to-date with changes was to recreate `PBXProjectWatcherManager`. The easiest way to get this working, is to use [class-dump](http://iphone.freecoder.org/classdump_en.html) to tell us what methods `PBXProjectWatcherManager` implements.

Running class-dump directly on Xcode.app was no real help (Xcode.app doesn't directly contain most of Xcode's functionality — it's in shared libraries). Using Activity Monitor (or lsof on the command-line) to inspect the Open Files of Xcode reveals all the shared libraries that Xcode uses. Most of these libraries live in /Developer/Library/PrivateFrameworks, so I ran the following script in that directory:

```objc
foreach f (*.framework)
  class-dump $f > ~/Desktop/`basename $f .framework`.h
end
```

to generate header file descriptions of each framework on the desktop. "DevToolsInterface.h" turned out to contain the description of the `PBXProjectWatcherManager` class.

Then it was a matter of working out which methods of `PBXProjectWatcherManager` are invoked and what they needed to return. So I created two projects: one to advertise its own `PBXProjectWatcherManager` under the name "PBXProjectWatcherServerConnection-3.1.2" and listen as Interface Builder connected and one to connect to Xcode's version of the same and work out the correct responses.

## Final solution

The result is that Interface Builder invokes the following:

| Method invoked | Required response |
|---|---|
| `openProjectsContainingFile:` | An `NSString` containing a URI to any Projects that contain a file with the specified path. |
| `pathOfProject:` | An `NSString` containing the file path for the specified Project URI. |
| `nameOfProject:` | An `NSString` containing the project name for the specified Project URI. |
| `targetsInProject:` | An `NSArray` of `NSString` containing the UUIDs for all targets in the specified Project URI. |
| `nameOfTarget:inProject:` | An `NSString` containing the target name for the specified target UUID. |
| `filesOfTypes:inTarget:ofProject:` | Types is normally `nil` so the response is an `NSArray` of `NSString` containing file paths to all files contained in the target. |

Apparently, Interface Builder gets all the header file paths for all targets that use a given XIB file and monitors these files itself for changes. Experimental testing indicates that all that is required to replace Xcode's role in this case is to return these Project, Target and File values and Interface Builder will handle the rest (parsing the header files for information it requires).

Interface Builder re-requests these values every time it is brought to the front, so it polls the "PBXProjectWatcherServerConnection-3.1.2" server, rather than implementing any automated form of observation (despite observation methods on `PBXProjectWatcherManager`). My guess is that this is more robust if either end of the `NSConnection` crashes.

## Conclusion

I hope I've been informative about interprocess communication on the Mac and techniques for monitoring and intercepting these communications.

These techniques presented in this post are only useful for intercepting standard Cocoa communication techniques.

Obviously, implementing your own "PBXProjectWatcherServerConnection-3.1.2" server would require care. It isn't sending complicated information but you would need to update it every time Xcode is updated and there are dozens of other methods in the `PBXProjectWatcherManager` that may play a role I didn't uncover in this brief investigation.
