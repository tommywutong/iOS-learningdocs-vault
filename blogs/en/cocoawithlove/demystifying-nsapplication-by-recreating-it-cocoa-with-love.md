---
title: 'Demystifying NSApplication by recreating it | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2009/01/demystifying-nsapplication-by.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:1716e0e9cbe5de58'
translated: false
---

> 原文：[Demystifying NSApplication by recreating it | Cocoa with Love](https://www.cocoawithlove.com/2009/01/demystifying-nsapplication-by.html)　·　Cocoa with Love (Matt Gallagher)

In this post I will recreate code that is normally concealed between the `NSApplicationMain` call (invoked in a Cocoa application's `main` function) and the `sendEvent:` method (which distributes the events to windows and views from the main run loop). By recreating this code for you, I hope to explain the steps that occur between program startup and the dispatch of events to your code — so you can gain greater understanding of what `NSApplication` does on your behalf.

## Introduction

The default Cocoa Application template provided by Xcode contains just one line of code, in one function:

```objc
int main(int argc, char *argv[])
{
    return NSApplicationMain(argc,  (const char **) argv);
}
```

Somehow, this one line of code is enough to create a menubar, put a window onscreen and then handle user events (mouse clicks and menu selections) until the user quits the program, at which point the application gracefully exits.

## What we know

Scattered throughout the Cocoa documentation are hints about what must happen in `NSApplicationMain`:

-   - The name of the "MainMenu" NIB file to load automatically on startup
    - The name of the application's principal class (the class of the application object)
- Construct the application object
- Load the "MainMenu" NIB file
- Begin the "Run Loop" (which handles the rest of the program)

I will recreate all of these steps by implementing my own version of `NSApplicationMain` — named `MyApplicationMain` — and by creating my own `NSApplication` subclass that implements the `run` method for itself.

## MyApplicationMain

### Create the application object

The first step in the `MyApplicationMain` function is to read the name of the "Principal class" and construct the application object from this class.

```objc
NSDictionary *infoDictionary = [[NSBundle mainBundle] infoDictionary];
Class principalClass =
    NSClassFromString([infoDictionary objectForKey:@"NSPrincipalClass"]);
NSAssert([principalClass respondsToSelector:@selector(sharedApplication)],
    @"Principal class must implement sharedApplication.");
NSApplication *applicationObject = [principalClass sharedApplication];
```

The `infoDictionary` method returns the "Info.plist" for a bundle (in this case, our application's bundle) converted into an `NSDictionary` for easy access. All we need to do is get the "NSPrincipalClass" string and fetch the class identified by that string.

Since the application is a singleton, we construct it by calling the `sharedApplication` method on the class. If we try to construct the object using standard `alloc` and `init` calls, the `NSApp` singleton instance won't be set correctly and an exception will be thrown at a later point when a second application is created.

> my earlier post about singletons
> 
> or visit Apple's page on
> 
> Creating a Singleton Instance
> 
> .

### Load the contents of the MainMenu NIB file

Loading the "MainMenu" NIB file is a similar task: get the name from the `infoDictionary` and then load it.

```objc
NSString *mainNibName = [infoDictionary objectForKey:@"NSMainNibFile"];
NSNib *mainNib =
    [[NSNib alloc] initWithNibNamed:mainNibName bundle:[NSBundle mainBundle]];
[mainNib instantiateNibWithOwner:applicationObject topLevelObjects:nil];
```

I briefly considered implementing the `NSNib` code too, to show how that works for loading objects in a NIB file, but since the format of a NIB file is not publicly declared, it wasn't possible. Suffice it to say that the `instantiateNibWithOwner:topLevelObjects` method performs the following steps:

-   - (used for

      objects)
    - (used for most other objects in the Interface Builder library)
    - (used for all other objects)
- pointers on objects as specified in the NIB file and establishes all bindings
- on all objects that implement this method

### Start the run loop

It is extremely important that the application's main loop runs on the main thread. For this reason, we don't directly invoke `run` but instead make sure it is performed on the main thread.

```objc
if ([applicationObject respondsToSelector:@selector(run)])
{
    [applicationObject
        performSelectorOnMainThread:@selector(run)
        withObject:nil
        waitUntilDone:YES];
}
```

I also check that the `applicationObject` will respond to the method before trying to invoke it, just in case the "Principal Class" from the Info.plist file is not a valid `NSApplication` or `NSApplication`-like object.

## Implementing our own run loop

The remaining task required so that you can trace the application's execution from startup to dispatch of events to your code is the implementation of the run loop.

Despite Apple's comment in the `NSApplication` documentation that `run` is one of the "Methods to Override", my brief search failed to uncover anyone who had actually done it. My suspicion is this: it is _not_ a method to override and that document is woefully out-of-date. The only reason to implement your own _run_ method now is curiosity, not functionality.

In that spirit, here's a reimplementation of `run` and a corresponding `terminate` method:

```objc
- (void)run
{
    NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];

    [self finishLaunching];

    shouldKeepRunning = YES;
    do
    {
        [pool release];
        pool = [[NSAutoreleasePool alloc] init];

        NSEvent *event =
            [self
                nextEventMatchingMask:NSAnyEventMask
                untilDate:[NSDate distantFuture]
                inMode:NSDefaultRunLoopMode
                dequeue:YES];

        [self sendEvent:event];
        [self updateWindows];
    } while (shouldKeepRunning);

    [pool release];
}

- (void)terminate:(id)sender
{
    shouldKeepRunning = NO;
}
```

It's as simple as you might expect: take the next event out of the queue for your application and route it appropriately using `sendEvent:` which handles the task of determining which window wants the event and invokes `sendEvent:` on the window to further route the event to a specific view.

For those interested: I discovered all the methods that need to be invoked in the `run` method in the most naive way: by searching the `NSApplication` documentation for "loop" to find all methods that claimed they were invoked in the main run loop.

The specific function of `finishLaunching` method is a bit of a mystery. All I know is that menus, menu updates and a host of other features won't work if it isn't invoked. It is possible that it sets up the responder chain for some actions. It is possible it adds observers to the run loop. I don't really know.

`nextEventMatchingMask:untilDate:inMode:dequeue:` is the biggest reason why I chose, when "reimplementing" `NSApplication` for this post, to make my implementation a subclass of `NSApplication` instead of a completely separate class. This method (or something it contains) converts notifications from the operating system and hardware drivers into `NSEvent` objects. A principal class is not required to be a subclass of `NSApplication` but I wouldn't know where to begin reimplementing this method, so I had to use `NSApplication` to do it.

## Conclusion

> RecreatingNSApplication.zip
> 
> (60kB)

This recreation of `NSApplicationMain` and `NSApplication`'s `run` does not do everything that the real implementations do (I've deliberately kept it simple for clarity) but I think it shows that the key steps involved are straightforward and easy to understand.

There are a few steps that I haven't reimplemented: loading NIB files, retrieving events and routing events. Unfortunately, these remain black boxes to me, so I can't shed further light on them. You can find out some things by setting breakpoints (in your constructors for objects created in NIBs or in your event methods) and reading the names of Apple functions invoked to bring these commands to you.

Beyond this, you can also read how [GNUStep implements the same methods](http://www.koders.com/objectivec/fidC548A9896F2887D86D7074E7C563CC920B1698EC.aspx). Apple doesn't necessarily do the same thing but GNUStep at least represents an observable solution to the same problems.
