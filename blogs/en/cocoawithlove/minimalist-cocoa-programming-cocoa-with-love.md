---
title: 'Minimalist Cocoa programming | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2010/09/minimalist-cocoa-programming.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:dbe055561b2fb8e2'
translated: false
---

> 原文：[Minimalist Cocoa programming | Cocoa with Love](https://www.cocoawithlove.com/2010/09/minimalist-cocoa-programming.html)　·　Cocoa with Love (Matt Gallagher)

In this post, I build and run a Cocoa Mac application on the command-line. This might not sound like a very difficult goal but I'll attempt to follow an additional constraint: use as few tools, components, classes and even lines of code as possible; truly minimalist Cocoa programming. The goal is to create an application that qualifies as a proper Mac application (including a menubar and a window) but without using Xcode, without an Info.plist file, without NIB files, without Interface Builder and without even using a text editor other than the Terminal itself.

## Introduction

For this post, I was inspired (in a somewhat tangential way) by Amit Singh's [Crafting a Tiny Mach-O Executable](http://www.osxbook.com/blog/2009/03/15/crafting-a-tiny-mach-o-executable/). In his article, Amit Singh crafts a 248 byte Mach-O executable in an effort to make the smallest executable possible on Mac OS X (he also presents a 165 byte version but this no longer runs in Snow Leopard).

A Cocoa application would never really get this small since "Cocoa" implies a large amount of linkage and runtime overhead in the executable (and I don't really want to start coding any of that by hand in assembly). But it inspired me to consider how you might reduce scale and complexity for a Cocoa App; what would be a minimalist Cocoa Mac application?

Of course, the answer in this case is entirely dependent on what criteria you require for a program to be considered a "Cocoa Mac application". I decided that a Cocoa Mac application must:

- to run the main event loop
- Display a menubar with an application menu and a quit item which must correctly terminate the application
- -based window
- Bring the main window to the front on startup like a normal application
- Code and program should raise no warnings or errors (preferrably no poor coding practices either but that's subjective)

Ordinarily, these aren't difficult objectives — they are part of the standard Xcode Cocoa application template — but there's actually a huge amount of content described in the default template. Just because you didn't add the different pieces yourself doesn't make it minimalist.

## Starting small

If you're extreme enough to believe that you could program directly in hex, then you might consider the following to be the baseline for minimalist Mac OS X programming:

```bash
echo "CEFAEDFE07000000030000000200000002000000CC00000000000000010000007C0000005F5F5445585400000000000000000000001000000010000000000000F8000000070000000500000001000000000000005F5F74657874000000000000000000005F5F5445585400000000000000000000E810000010000000E80000000200000000000000000000000000000000000000000000000500000050000000010000001000000000000000000000000000000000000000000000000000000000000000000000000000000000000000E8100000000000000000000000000000000000000000000031C040682A00000081EC04000000CD80" | xxd -r -p - tiny; chmod a+x tiny; ./tiny; echo $?
```

That's Amit Singh's 248-byte program in raw hex, saved to a file by "xxd", marked as executable using "chmod", run and the result displayed (it returns the exit condition 42).

Realistically though, all I can read are the first 5 bytes "CEFAEDFE07" which are the magic value for a Mach-O executable plus the CPU type for X86 CPUs. While historically, people certainly have programmed in hex, I would never write a Mac OS X program like this and I doubt anyone else would either. So piping Amit's actual assembly directly through nasm is probably a more realistic baseline for minimalist Mac OS X programming.

I'm not going to fight through this in assembly though (it's an Objective-C blog, after all), so I'm going to need a compiler to progress from here.

Creating, building and running the smallest possible C program looks something like this:

```bash
echo "main(){}" | gcc -x c - ; ./a.out; echo $?
```

The options used with gcc might look a bit odd but they are: "-x c" (build as C code) and "-" (take input on standard in). The default output file name of "a.out" is acceptable for now.

While technically this builds a valid program and looks simpler than the block of hex up above, it actually does less than the previous program did — it doesn't even deliberately return a specific value (instead I get 252 which is probably just junk from the stack since `main` implicitly returns an `int` that we aren't returning).

It's a little better to actually return a value. While it's not much, you can at least claim that the program "does something".

```bash
echo "int main(){return 0;}" | gcc -x c -; ./a.out ; echo $?
```

Great, we've returned the default success value.

## Tiny Cocoa

The smallest Objective-C program is the same as the smallest C program, just change the command-line so gcc builds Objective-C:

```bash
echo "int main(){return 0;}" | gcc -x objective-c -; ./a.out ; echo $?
```

but the gcc output is literally the same. I'll need to use at least one class to truly claim this is Objective-C:

```bash
echo "#import &lt;objc/Object.h&gt;
int main(){return [Object class]==nil;}" | gcc -x objective-c -lobjc -; ./a.out ; echo $?
```

Making a Foundation program is no harder, we just link against the Foundation framework instead of libobjc. I could use literally the same program but here's one with a proper `NSAutoreleasePool`, logging and process information:

```bash
echo '#import &lt;Foundation/Foundation.h&gt;
int main(){
    id pool=[NSAutoreleasePool new];
    NSLog(@"%@", [[NSProcessInfo processInfo] arguments]);
    [pool drain];
    return 0;
}' | gcc -framework Foundation -x objective-c - ; ./a.out ; echo $?
```

Notice that `NSProcessInfo` has no problems getting the command-line arguments without `main` needing to handle them.

With an AppKit application, the `main` function looks a little simpler because `-[NSApplication run]` creates its own autorelease pool (although I'll need to bring it back again later to work outside `-[NSApplication run]`):

```bash
echo '#import &lt;Cocoa/Cocoa.h&gt;
int main(){
    [[NSApplication sharedApplication] run];
    return 0;
}' | gcc -framework Cocoa -x objective-c - ; ./a.out ; echo $?
```

Unfortunately, while this AppKit program runs, it doesn't present a user-interface and doesn't quit unless we kill it. Not very satisfying.

## Satisfying the requirements

In Snow Leopard, programs without application bundles and Info.plist files don't get a menubar and can't be brought to the front unless the presentation option is changed:

```objc
[NSApp setActivationPolicy:NSApplicationActivationPolicyRegular];
```

Next, we need to create the menu bar. You don't need to give the first item in the menubar a name (it will get the application's name automatically):

```objc
id menubar = [[NSMenu new] autorelease];
id appMenuItem = [[NSMenuItem new] autorelease];
[menubar addItem:appMenuItem];
[NSApp setMainMenu:menubar];
```

Then we add the quit item to the menu. Fortunately the action is simple since `terminate:` is already implemented in `NSApplication` and the `NSApplication` is always in the responder chain.

```objc
id appMenu = [[NSMenu new] autorelease];
id appName = [[NSProcessInfo processInfo] processName];
id quitTitle = [@"Quit " stringByAppendingString:appName];
id quitMenuItem = [[[NSMenuItem alloc] initWithTitle:quitTitle
    action:@selector(terminate:) keyEquivalent:@"q"] autorelease];
[appMenu addItem:quitMenuItem];
[appMenuItem setSubmenu:appMenu];
```

Finally, all we need to do is create a window and activate the application:

```objc
id window = [[[NSWindow alloc] initWithContentRect:NSMakeRect(0, 0, 200, 200)
    styleMask:NSTitledWindowMask backing:NSBackingStoreBuffered defer:NO]
        autorelease];
[window cascadeTopLeftFromPoint:NSMakePoint(20,20)];
[window setTitle:appName];
[window makeKeyAndOrderFront:nil];
[NSApp activateIgnoringOtherApps:YES];
```

In keeping with the pattern of the rest of the post, here's the entire program as a single, command-line executable statement:

```bash
echo '#import &lt;Cocoa/Cocoa.h&gt;
int main ()
{
    [NSAutoreleasePool new];
    [NSApplication sharedApplication];
    [NSApp setActivationPolicy:NSApplicationActivationPolicyRegular];
    id menubar = [[NSMenu new] autorelease];
    id appMenuItem = [[NSMenuItem new] autorelease];
    [menubar addItem:appMenuItem];
    [NSApp setMainMenu:menubar];
    id appMenu = [[NSMenu new] autorelease];
    id appName = [[NSProcessInfo processInfo] processName];
    id quitTitle = [@"Quit " stringByAppendingString:appName];
    id quitMenuItem = [[[NSMenuItem alloc] initWithTitle:quitTitle
        action:@selector(terminate:) keyEquivalent:@"q"] autorelease];
    [appMenu addItem:quitMenuItem];
    [appMenuItem setSubmenu:appMenu];
    id window = [[[NSWindow alloc] initWithContentRect:NSMakeRect(0, 0, 200, 200)
        styleMask:NSTitledWindowMask backing:NSBackingStoreBuffered defer:NO]
            autorelease];
    [window cascadeTopLeftFromPoint:NSMakePoint(20,20)];
    [window setTitle:appName];
    [window makeKeyAndOrderFront:nil];
    [NSApp activateIgnoringOtherApps:YES];
    [NSApp run];
    return 0;
}' | gcc -framework Cocoa -x objective-c -o MinimalistCocoaApp - ; ./MinimalistCocoaApp
```

That's an entire Cocoa Mac application that you can copy onto the clipboard, paste directly at the prompt in Terminal, hit return and it'll run.

## Conclusion

At 9352 bytes when compiled (exact size may change from computer to computer), my simple Cocoa program is nowhere near as small as the assembly written Mac OS X baseline of 248 bytes. At 27 lines long, it might not immediately seem "minimalist", either. However, it does satisfy the requirements I set for being a proper Cocoa Mac application.

The reality is that the things done under-the-hood by the default application templates, by the Xcode build system, by Interface Builder and by `NSApplication` itself in conjunction with the Info.plist file are significant. To replicate the required subset of their functionality requires at least some work. Compared to the standard Xcode Cocoa application template's 85782 bytes for the entire compiled bundle, my app's goal of Cocoa minimalism seems far more successful.

Reducing the size of the executable wasn't my primary goal, though. I was aiming to reduce the number of tools, components, files and classes required for a genuine Cocoa Mac application. Relative to the standard suite of tools and collection of files involved in building a Cocoa Mac app, 27 lines of code processed using echo, gcc and a bash terminal represents a significant simplification.

I welcome further suggestions about how to satisfy the same requirements with less.
