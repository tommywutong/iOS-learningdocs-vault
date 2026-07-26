---
title: 'Porting a Mac program to Windows using The Cocotron | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2010/04/porting-mac-program-to-windows-using.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:0e9c969f71c34409'
translated: false
---

> 原文：[Porting a Mac program to Windows using The Cocotron | Cocoa with Love](https://www.cocoawithlove.com/2010/04/porting-mac-program-to-windows-using.html)　·　Cocoa with Love (Matt Gallagher)

In this last of three posts about porting a Mac application to Windows, I look at the steps involved in setting up [The Cocotron](http://cocotron.org) with a remote debugging session between Xcode and the application running on Windows. I'll also talk about the code that didn't "just work" and some of the approaches I used to fix the program and get it working.

## Introduction

If you want some background on what The Cocotron is and alternative ways of porting applications from the Mac to Windows, please read the [first](https://www.cocoawithlove.com/2010/04/options-for-porting-objective-ccocoa.html) and [second](https://www.cocoawithlove.com/2010/04/design-of-multi-platform-app-using.html) part in this series.

## Setting up The Cocotron for remote debugging

Installing The Cocotron is a three step process:

1. Download the InstallCDT zip file

  , decompress it and run the InstallCDT script it contains. I think CDT stands for Cocotron Developer Tools. This installs a copy of gcc and related tools that you will required for cross-compilation. It will also install required MinGW libraries and W32API libraries for linking Windows projects.
2. Check out a copy of The Cocotron code

  . The repository has recently moved to Mercurial, so you'll need to have a copy of

  Mercurial

  or check out the

  Subversion mirror

  . Open the Cocoa.xcodeproj and build the project.
3. Download a copy of xcxdb-Installation.zip

  and run the install-xcxdb,sh script it contains. XCXDB probably stands for Xcode Cocotron (X)cross DeBugger.

The third point is not strictly required for using The Cocotron but is required for remote debugging as it installs a version of gdb that will allow remote debugging between Xcode and Windows. The XCXDB install has the added advantage that it adds a Template to the Project Templates that will create a Windows debuggable project without needing to mess around with specific project settings.

You can add The Cocotron and XCXDB settings to an existing project but it takes a bit more effort: apply the [Build settings for CDT](http://www.cocotron.org/Tools/Build_Settings) and then, from an XCXDB project created from the template, copy the manifest, icon, Remote-Target.txt and win-icon.rc files, then copy the run script build phase that includes gdbserver.exe in your debug builds, set the GDB connection to "pipe" and probably a few other things I'm forgetting.

Setting up the project manually is easy to get wrong, so you'll want to get a project running from the "Cocotron" User Template before trying to modify an existing project.

## Coordinating on the Windows side

I run Windows XP Home in VirtualBox on the same Mac as Xcode. You could also use VMWare, Parallels or a separate, dedicated Windows machine. VirtualBox is cheaper than these options (it's free) but is also the slowest so you'll want a faster machine.

Running a virtual machine and Xcode on the same computer also uses lots of RAM. You could probably manage in 4GB of RAM but I have 6GB of RAM and have contemplated getting more to accomodate VirtualBox, Xcode and my other regular applications.

To make a virtual machine work, the best approach is to make the virtual machine use a "bridged" network adapter. This gives it its own IP address on the local network. Incidentally, I had to switch from VirtualBox's default AMD network driver to the Intel driver — since the AMD driver would crash periodically while debugging, causing the whole virtual machine to lose network connectivity until I restarted it.

Once the Windows virtual machine has its own IP address, edit the IP address in the "Remote-Target.txt" file from the Xcode project to match this address. Make sure the Firewall on the Windows machine allows access to 999 (the default port that XCXDB uses for debugging). You can use another port if needed, just use a different port in Remote-Target.txt and below when you start gdbserver on the remote machine.

You also need to ensure that the build location for your Xcode project is a shared volume that both the Mac and Windows machines can access. I chose to use VirtualBox's "Shared Folders" to make the build location on my Mac's drive a network volume under Windows.

## Running the sample XCXDB project

In Xcode, create a project from the Cocotron User Template. I named mine "XCXDB-Sample".

Select the XCXDB-Sample-Windows target from the targets menu.

From Windows as I configured it, the path to the XCXDB-Sample directory is Z:\\Projects\\XCXDB-Sample. I chose to use an MSYS terminal client to navigate to the /z/Projects/XCXDB-Sample/build/Debug-cocotron-win32/XCXDB-Sample.app directory (download MSYS and its dependencies from [mingw.org](http://mingw.org)).

The reason why I used MSYS instead of a DOS command prompt like cmd.exe, is that MSYS allows the standard out and standard error of any running application (this includes `NSLog()` messages from Cocoa) to work for applications (otherwise these facilities are only visible to dedicated command-line programs in Windows). MSYS also offers a more familiar (if slightly quirky) bash shell environment.

Once you're in the XCXDB-Sample.app directory, run:

```objc
./gdbserver --multi localhost:999
```

Normally in XCXDB, this command is run from the debug.bat file. However, ".bat" files don't run under MSYS. You can create a shell script if you prefer.

The Windows command shell will now display: "Listening on port 999".

From Xcode, select "Build and Debug" from the "Build" menu. If all has gone well, the status bar at the bottom of the project menu will build and then display "GDB: Stopped". You need to tell GDB to try to connect. With the one of the Xcode project windows selected, type Command-Option-P (Debugger continue).

If the communication between Mac and Windows isn't working you may see an error in the Debugger Console.

```objc
mix_cmd_pid_info: the program being debugged is not running.
mix_cmd_exec_interrupt: Inferior not executing.
```

This indicates that either:

- The working directory of the Executable in Xcode is not set to the "Project Directory".
- Remote-Target.txt was not found in the Project Directory.
- The relative path to the "remote exec-file" did not match a file on the Windows machine.

```objc
mix_cmd_pid_info: the program being debugged is not running.
```

If you get this line without the "Inferior not executing" message shown above, then the RemoteTarget.txt did not contain the correct IP address or the gdbserver.exe isn't running.

## A few tips for remotely debugging with The Cocotron and XCXDB

You will encounter unimplemented functions and methods in The Cocotron. You may even encounter bugs.

To help you fix these issues, you'll probably want to build The Cocotron's Cocoa.xcodeproj project in Debug and keep the AppKit.xcodeproj and Foundation.xcodeproj projects open. This will build debug information into the AppKit and Foundation DLLs and will let you debug problems in these frameworks.

Since the debugger is configured to communicate via PIPE instead of the interactive terminal, you can't enter GDB commands into the Command Console in Xcode. You _can_ add extra commands to the Remote-Target.txt file though.

Every time I started listening on a socket, GDB reported a SIGSEGV signal. The program didn't crash (I'm not sure it was a real SIGSEGV) but it paused the debugger. If this happens for you and it gets too annoying, you can add the line "handle SIGSEGV nostop noprint pass" to the start of the Remote-Target.txt file.

I had issues setting breakpoints at times. Often, I could only set breakpoints before the program started or when the program was already stopped at another breakpoint. If anyone finds away around this nuisance, I'd like to know.

## Code which won't "just work" in The Cocotron

Here begins a story of the issues I encountered porting [ServeToMe](http://zqueue.com/servetome/index.html) to Windows using The Cocotron.

Once I'd gone through the arduous task of adding required settings and files to my existing projects, came the task of getting the program compiling.

I'm not going to discuss the difficulties of compiling and linking third-party dependencies on another platform. Don't misunderstand me: it is very difficult; but since it has little to do with The Cocotron, I won't discuss that work here.

### Almost everything involving sockets

ServeToMe includes an HTTP server and does a lot with BSD socket communication. None of this worked initially.

The Cocotron itself doesn't implement sockets — instead that falls directly through to WinSock's implementation. Most socket code just required the Windows headers to be included:

```objc
#if __WIN32__
    #undef WINVER
    #define WINVER 0x501
    #import &lt;winsock2.h&gt;
    #import &lt;ws2tcpip.h&gt;
#else
    #import &lt;sys/socket.h&gt;
    #import &lt;netinet/in.h&gt;
    #include &lt;arpa/inet.h&gt;
#endif
```

and the respective libraries (libwsock32.a, libws2_32.a and libmswsock.a) included from the /Developer/Cocotron/1.0/PlatformInterfaces/i386-mingw32msvc/lib directory.

There are a few common socket-related functions in `<arpa/inet.h>` and other headers on the Mac that WinSock doesn't include. Examples include `inet_ntop` and `inet_pton`. You will need to reimplement these yourself. If you Google for them, you'll find implementations around.

### Quirks and omissions in the MinGW libraries

The MinGW libraries implement a lot of POSIX functions but certainly not all.

One of the more annoying omissions for me was `mkdtemp()` (which creates temporary directories in a safe manner). In the end I had to find an open source implementation of this function in FreeBSD and included that in my project.

A few other functions like `random()` were missing (using `rand()` instead was sufficient) and some functions like `mkdir()` took a different number of arguments (again a simple `#define` to change the arguments was sufficient).

### Objective-C Runtime Differences

The Cocotron's Objective-C runtime does not support `+load` methods at this time. This meant that I had to move all the code that I previously invoked in `+load` methods into another location. Not really a big difficulty — I registered service handlers for my HTTP server in a different location.

### Unimplemented behaviors

The CoreFoundation functions for generating UUIDs — `CFUUIDCreate` and `CFUUIDCreateString` — were not implemented. With functions like this, you need to choose: do you add the functionality to Cocotron and submit the changes back to the trunk, or do you just use the Win32 equivalent inline in your code.

With other functions I used that weren't implemented, like `SecKeychainFindGenericPassword`, I implemented the changes properly in The Cocotron and [committed back to the trunk](http://code.google.com/p/cocotron/source/browse/Security/SecBase.m) (I feel bad, looking at my additions, that don't match the indentation of the other code).

With UUIDs though, I couldn't be bothered working out if a platform independent or multi-platform solution was easy or possible, so I just slapped the Win32 version into my code:

```objc
#ifdef __WIN32__
    UUID uuid;
    UuidCreate(&uuid);
    unsigned char *cString;
    UuidToString(&uuid, &cString);
    uuidString = [[NSString alloc] initWithUTF8String:cString];
    RpcStringFree(&cString);
#else
    CFUUIDRef uuid = CFUUIDCreate(NULL);
    uuidString = (NSString *)CFUUIDCreateString(NULL, uuid);
    CFRelease(uuid);
#endif
```

I also use an `NSStatusBar` menu for ServeToMe (a menu item at the right of the menubar).

```objc
statusItem = [[[NSStatusBar systemStatusBar]
    statusItemWithLength:NSSquareStatusItemLength] retain];

[statusItem setMenu:statusMenu];
[statusItem setHighlightMode:YES];
[statusItem setToolTip:@"ServeToMe"];
[statusItem setImage:[NSImage imageNamed:@"StatusBarIcon"]];
```

This wasn't implemented in The Cocotron either.

As with UUIDs, I didn't have the time to integrate a solution properly into a Cocotron implementation of `NSStatusBar`, implementing this was not nearly as elegant.

```objc
NSString *const NSContentArrayBinding = @"contentArray";
NSString *iconPath =
   [[NSBundle mainBundle] pathForResource:@"ServeToMeSmall" ofType:@"ico"];

ZeroMemory(&niData,sizeof(NOTIFYICONDATA));
niData.cbSize = sizeof(NOTIFYICONDATA); // don't bother using features from DLL V5 or later
niData.uID = TrayIconID;
niData.uFlags = NIF_ICON | NIF_MESSAGE | NIF_TIP;
niData.hIcon = (HICON)LoadImage(
    NULL,
    [iconPath UTF8String],
    IMAGE_ICON,
    GetSystemMetrics(SM_CXSMICON),
    GetSystemMetrics(SM_CYSMICON),
    LR_LOADFROMFILE | LR_DEFAULTCOLOR);
niData.hWnd = (HWND)[(Win32Window *)[[self window] platformWindow] windowHandle];
niData.uCallbackMessage = TrayIconMessage;

// tooltip message
strncpy(niData.szTip, "ServeToMe",
    sizeof(niData.szTip));

BOOL result = Shell_NotifyIcon(NIM_ADD,&niData);
if (!result)
{
    NSLog(@"Shell_NotifyIcon failed: %d", GetLastError());
}

// free icon handle
if(niData.hIcon && DestroyIcon(niData.hIcon))
    niData.hIcon = NULL;
```

And all of that is just to show the icon! Responding to clicks in the icon and showing a menu, then minimizing the window into that icon to show that the program is still running took a lot more.

It's very strange to include all this Win32 code in the middle of a Cocoa application.

### Windows does not support that

My code previously used `-[NSFileHandle waitForDataInBackgroundAndNotify]`. The Cocotron does not implement this method.

At first I thought it was just a missing implementation that I could add.

Then I learned that Windows _can't_ wait for a notification on an unnamed pipe. The `select` function or the `WaitForMultipleObjects` in Win32 won't accept a file handle from an unnamed pipe.

This actually required refactoring my code to use `readInBackgroundAndNotify` instead. This isn't a huge change but it is a situation where Windows was actually incapable of replicating the exact behavior and changing the program to work in a slightly different way turned out to be the easiest approach.

Obviously, it is possible to implement an abstraction around the whole concept of pipe and file handles to replicate the same functionality but that's a lot of work, and is antithetical to how the rest of The Cocotron works (it aims to be a thin implementation of Cocoa on top of Win32 without heavy abstraction layers).

### Windows filesystem

Obviously, hardcoded paths need to change when you move to Windows.

Unfortunately, there are a couple other quirks to handle.

ServeToMe uses `lstat` and `readdir` to traverse directories instead of any higher level function (for performance reasons [discussed in an earlier post](https://www.cocoawithlove.com/2009/09/optimizing-loading-of-very-large-table.html)). MinGW provides a `stat` implmentation for file information but does not provide `lstat`, so handling Windows Shortcuts would be tricky — I didn't try.

Unfortunately, `stat` doesn't handle UNC paths. These are Windows network paths for volumes that aren't mounted as drive letters. For this reason, I decided to move to a higher level API.

The correct way to do this under Win32 is probably `GetFileAttributesExW`. However, it turns out that it was easier to simply revert to the higher level `NSFileManager` API for getting file system information. This API is fully implemented by The Cocotron, supports UNC paths and worked fairly efficiently in testing.

> the function name
> 
> is amusing evidence of the age of Win32 and its efforts to maintain backwards compatibility. The original function,
> 
> is still there but is just about useless — it was deprecated in 1999 — and Win32 never fully committed to Unicode so the function has to point out: Warning! "Wide" chars!

That's right: in some cases, the Windows version of ServeToMe is _more_ Cocoa than the Mac version. But only in some cases.

## Time taken

Porting ServeToMe to Windows took me just over 2 weeks. This time breaks down as:

- Setting up my Windows virtual machine and The Cocotron and getting remote debugging working: 2 days
- Commenting out code which doesn't work up-front and getting the program to launch: 2 hours
- Re-adding functionality that was missing or didn't immediately work: 1.5 days
- Fixing quirks associated with sockets and port mappings: 1.5 days
- Building or reimplementing 3rd party libraries for Windows: 4 days
- Sorting out minor bugs and issues: a day or two (so far)

This two weeks is similar to the amount of time it took me to write the first version of ServeToMe from scratch (admittedly, it was a lot less sophisticated).

Does this mean a full-time Windows developer could have reimplemented the whole program in a native Windows language and environment (e.g. C# .Net) in the same time-period? Yes, a really good C# programmer with existing libraries of code to rely on and access to my original implementation could probably have reimplemented rather than ported within the same time period.

The big advantage of using The Cocotron instead is not the up-front time saving of this approach (which would reduce if I gained practice porting projects in this manner) but the fact that all changes I make to the codebase will now appear in both versions Mac and Windows with no extra effort — they are completely in sync. Also, The Cocotron allowed me to stay in a code environment where I'm an expert (Cocoa/Objective-C), rather than dabbling outside my area of expertise where I'm more likely to make serious mistakes.

## Conclusion

When I started as a professional developer, I worked as an MFC and Win32 developer at a large company. It's very weird going back to Win32 after 7 years away from it.

Of course, I'm Cocoa programmer now and very comfortable in Xcode. Being able to develop a Windows application without leaving that comfortable environment was a great relief.

It was not without its difficulties though. Setting up a remote debugging environment is frustrating. There are lots of issues that can crop up until you're familiar with the setup.

I certainly encountered missing functionality in The Cocotron but it was all very simple to implement as needed. I even encountered a couple of bugs in The Cocotron but likewise, they were simple to address (no harder than most bugs in my own code).

The final result was not necessarily the fastest path to functionality on Windows but one which achieved maximum shared functionality between the two codebases (both now and moving forward) and only small amounts of work outside of my normal Cocoa skillset.
