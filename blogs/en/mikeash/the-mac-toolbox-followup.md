---
title: 'The Mac Toolbox: Followup'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/the-mac-toolbox-followup.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:869b79e9f6a189ad'
translated: false
---

> 原文：[The Mac Toolbox: Followup](https://www.mikeash.com/pyblog/the-mac-toolbox-followup.html)　·　mikeash.com Friday Q&A

Posted at 2012-01-20 16:14 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2012-02-03: Ring Buffers and Mirrored Memory: Part I](https://www.mikeash.com/pyblog/friday-qa-2012-02-03-ring-buffers-and-mirrored-memory-part-i.html)  
Previous article: [Friday Q&A 2012-01-20: Fork Safety](https://www.mikeash.com/pyblog/friday-qa-2012-01-20-fork-safety.html)  
Tags: [classic](https://www.mikeash.com/pyblog/?tag=classic) [followup](https://www.mikeash.com/pyblog/?tag=followup) [guest](https://www.mikeash.com/pyblog/?tag=guest) [nostalgia](https://www.mikeash.com/pyblog/?tag=nostalgia) [oldschool](https://www.mikeash.com/pyblog/?tag=oldschool) [toolbox](https://www.mikeash.com/pyblog/?tag=toolbox)

The Mac Toolbox: Followup

by [Gwynne Raskind](http://blog.darkrainfall.org/)

---

**Includes and constants and globals, oh my**  
In the Toolbox days, there were no all-encompassing headers where you do one `#import` and you have everything you need. Right up until Carbon, this simple truth remained as a holdover from the times when compilers took a major speed penalty for every single header they had to read. Nor did `#import` exist. Just `#include`, with all the slings and arrows that flesh was heir to. At least the names were usually straightforward.

```
    #include <Dialogs.h>        // Dialog Manager (for InitDialogs())
    #include <Fonts.h>          // Font Manager (for InitFonts())
    #include <MacWindows.h>     // Window Manager
    #include <Menus.h>          // Menu Manager
    #include <QuickDraw.h>      // QuickDraw
    #include <TextEdit.h>       // TextEdit (for TEInit())
    #include <Controls.h>       // Control Manager
```

There also weren't nice string names and outlet connections from nibs to give you access to your resources, so you were best off defining a constant for every resource in your application to make your code even remotely readable. Resource IDs for applications started from 128, and you had better believe following that rule was important. Because resource files were opened as overlays atop each other, the system's resources sat right underneath yours, and if you overrode a system resource by defining another with the same type and ID, chaos could and generally did ensue.

```
    enum
    {
        kMenuBarID = 128,

        kAppleMenu = 128,
        kFileMenu = 129,
        kEditMenu = 130,

        kWindowID = 128
    };
```

Then you had global variables. Generally frowned upon in any modern program of today, they were all but a requirement for Toolbox development when not using C++ or some other object-oriented language. There was just no other efficient way to get data where it was going. Certainly the global variable for exiting the event loop was a lot better than returning `Boolean` from every single event handling function in your code on the off chance an action might lead to a `Quit`. Not to mention your `aevt/quit` Apple Event handler (more on that below).

```
    static AEEventHandlerUPP        oappUPP, odocUPP, pdocUPP, quitUPP;
    static Boolean                  gDone = false;
```

**Alerts and StandardFile**  
Check out the fancy function for handling an about box! Later versions of OS 8 and 9 brought a better API for presenting simple alerts, but before that you just defined an `ALRT` (ALeRT) and `DITL` (Dialog ITem List) pair which described your about box and displayed them. I already violated my own rule about defining a constant for the resource ID, something that would tend to happen a lot when you needed just one more resource for this one little bit of code. `Alert()` and its cousins such as `StopAlert()` were used quite a bit for such things as error messages as well.

```
    static void DoAboutCommand(void)
    {
        Alert(128, NULL);
    }
```

The API for asking the user to select a file from the hard drive went through quite a few evolutions, along with the data type for storing the location of a file. My knowledge only goes back so far as the System 6 APIs, of which `SFGetFile()` was the relevant member. This returned an `SFReply`, containing a volume reference number, directory ID, and a 63-character MacRoman-encoded file name string. This was superseded in System 7 with `StandardGetFile()`, whose `StandardFileReply` instead contained an `FSSpec`, which was really just the same three values packaged up as a fancy structure for easier passing around.

In OS 8.1 (or 8.5, I've forgotten which), Navigation Services and the modern File Manager were introduced, which provided a considerably more featured API, an interface whose merits versus the old StandardFile dialogs were debated, and the `FSRef` datatype which survived right into some Cocoa code until URLs became the norm for referring to files on disk. A particular quirk of `FSRef` was that it could not refer to files which did not exist, prompting many coders to come up with their own solutions for holding either a parent directory `FSRef` and file name (an `HFSUniStr255`, a brutally contrived data type if ever there was one) or falling back on `FSSpec`. The latter was common for its simplicity, making `FSRef` a bit of a mess.

I did not use Navigation Services here, as I was trying to stick to System 7 APIs. Instead, I call into StandardFile, telling it to let me pick only files with the type `TEXT`, and checking for whether or not the user clicked OK before opening the file (or more exactly, calling the stub function which should have opened it). _Note: This is different from the version in the original article, which didn't limit the file type._

Even many Cocoa programmers are still familiar with the `OSType` concept. In OS 9 and earlier, files typically did not have extensions, and even where they did, only the most modern versions of OS 9 made significant decisions based on them. UTIs did not exist at all. Instead, files had (and indeed, still have, though they're much rarer now) "creator code"s and "type"s. These were ostensibly four-letter codes uniquely identifying the owner and type of a file, of which all-lowercase codes were reserved by Apple. In truth, they were just 32-bit integers (_not_ strings) whose uniqueness was guaranteed by convention at best, and by nothing most of the time. Collisions in creator codes happened all the time, and there was no standardization of file types either. It was little different than problems with three-letter file extensions, just with a little extra space to work in. UTIs were created specifically to address these problems. I leave it to the reader to decide whether that's met with any success.

_Note: The practiced C programmer will wonder how you can have a four-character character literal, as these are not supported by the language specification. The spec technically allows for these literals, but to my knowledge they were only ever widely used in Toolbox and Carbon programming, and have no place in Cocoa. Modern compilers will warn when they're used unless explicitly told not to._

```
    static void DoOpenCommand(void)
    {
        StandardFileReply stdReply;
        SFTypeList theTypeList = { 'TEXT', 0, 0, 0 };

        StandardGetFile(NULL, 1, theTypeList, &stdReply);
        if (stdReply.sfGood)
            DoOpenDocument(stdReply.sfFile);
    }
```

**Apple Events**  
Apple Events were, and still remain to this day, the mechanism by which AppleScript functions. They were also the first real form of direct interprocess communication, an area severely lacking in the Toolbox before their introduction for the primary reason that before MultiFinder and System 7, only one application ever ran at a time. Ever! Desk accessories notwithstanding. Many applications were written with this in mind, and the cooperative multitasking environment provided by System 7 necessitated a lot of fundamental re-engineering for programs which had gotten too aggressive about owning the whole machine.

Apple Events had a "class" and "event code", which were both another use of those 32-bit character literals. They evolved much later into Carbon Events, becoming the primary mechanism by which the OS communicated with applications, but in the early days existed as the only "asynchronous" way for the OS to tell a program much of anything. Though, as they were dispatched via the event loop like everything else, this was little more than a convenient metaphor.

Four "core" events were "required" for every application. I put "required" in quotes because, in practice, applications could get away without even knowing they existed. A more accurate description would be that they were required for any application which claimed to be "high-level event aware" in its `'SIZE'` resource (more on that later).

The first required Apple Event was the "open application" event, corresponding more or less to Cocoa's `-applicationDidFinishLaunching:` application delegate method. Since this event was _not_ sent if the user had opened the application by double-clicking one of its documents (or later, dragging and dropping a document icon onto the application icon), it was a good place for doing your "default" thing. In this case, I have it do a "new document".

What's this `pascal` keyword, you might wonder? This was a requirement for just about any callback the Toolbox might call, and told the compiler, "emit code to make this function comply with Pascal's calling conventions instead of C's." Because the Toolbox itself was written in Pascal (or in conforming assembly language), anything it called had to accept parameters and return values as specified by Pascal, or havoc would ensue. Every Toolbox routine was declared `pascal` in the C headers, when it wasn't just a bit of inline 68K machine code.

```
    static pascal OSErr     AEOpenApplication(const AppleEvent *theAE, AppleEvent *reply, UInt32 refCon)
    {
        DoNewCommand();
        return noErr;
    }
```

For the "open documents" Apple Event, corresponding to Cocoa's `-application:openFiles:` method, I get the "direct object" parameter as a list from the event, count the items in that list, then loop over the list getting each item as a FSSpec pointer and opening the resulting spec. Then I dispose of the list.

In all of this, I ignore quite a few error checks which would make the code all but unreadable. This is almost entirely pure boilerplate code.

Perhaps you can see how all of this was intended to produce a type-agnostic flexible event system, but in practice all it produced was a complicated batch of APIs which were fiendishly difficult to use correctly in all cases. Maybe the OS sent me an FSRef instead of an FSSpec, and this was an OS version which didn't include a working coercion handler to turn one into the other. Maybe there was no direct object, or the direct object was just a single file. Most of the assumptions this code makes were only safe for System 7.5 and earlier, and check out how many parameters I have to declare junk variables for because `NULL` was not a safe thing to pass.

```
    static pascal OSErr     AEOpenDocuments(const AppleEvent *theAE, AppleEvent *reply, UInt32 refCon)
    {
        FSSpec          file;
        AEDescList      docList;
        SInt32          items, i;
        Size            siz;
        AEKeyword       kwd;
        DescType        typ;

        AEGetParamDesc(theAE, keyDirectObject, typeAEList, &docList);
        AECountItems(&docList, &items);
        for (i=1; i<=items; i++)
        {
            AEGetNthPtr(&docList, i, typeFSS, &kwd, &typ, (void *)(&file), sizeof(FSSpec), &siz);
            DoOpenDocument(file);
        }
        (void) AEDisposeDesc(&docList);
        return noErr;
    }
```

I didn't even think about supporting printing (a truly monstrous task in Toolbox days), so I just return an error from the "print documents" handler. If I'd chosen to allow it, I could have used the same boilerplate from the open documents event to get the list of files. Yes, the exact same code, save that I'd call `DoPrintDocument(file)` instead.

```
    static pascal OSErr     AEPrintDocuments(const AppleEvent *theAE, AppleEvent *reply, UInt32 refCon)
    {
        return errAEEventNotHandled;    // Don't support printing
    }
```

Finally, the "quit application" event. This is _not_ equivalent to `-applicationWillTerminate:`, because if this event handler doesn't do anything, the application won't quit! I exit the event loop from here, of course.

Mind you, I wouldn't get this event if I chose "Quit" from the "File" menu (_not_ the application menu, there was no such thing), unless I dispatched it to myself manually.

```
    static pascal OSErr     AEQuitApplication(const AppleEvent *theAE, AppleEvent *reply, UInt32 refCon)
    {
        gDone = true;
        return noErr;
    }
```

**Initialization**  
Surely, you must be wondering, at least the system initializes itself on startup. Maybe there's just one function that needs calling, as with `NSApplicationMain()` or `RunApplicationEventLoop()`!

Sorry, no. In the Toolbox days, you did everything yourself. Let's take a look at the breakdown:

```
    static void Initialize(void)
    {
```

First off, maximize my application's zone (this does not mean what you think it does) and ask for more master pointers.

Maximizing my zone means that I'm asking for my heap to be as large as it can be before doing anything else. This saves the Memory Manager from having to grow it later as my allocations increase, a potentially time-consuming task. Why isn't this the default? Old design decisions from the days of tiny memory space.

Master pointers were used to implement handles. A handle is a double-pointer which allows a block of memory to be relocated at need without having to update every reference to that block. This theoretically prevented memory fragmentation, but it could get ugly with the need to lock handles before accessing their contents. There was no reference or depth count on locking, making passing handles around a very fussy business.

```
        MaxApplZone();
        MoreMasters();
        MoreMasters();
```

Now, initialize all the basic Toolbox managers. Start with QuickDraw, and give it the address of the `GrafPort` passed by the OS. That's the very ancient equivalent of an `NSGraphicsContext`, for you Cocoa devs. You'd think if it were passed by the OS, you wouldn't need to give it back to the OS, but the nature of global variables in the Toolbox world made this the easier way. In theory, you could have passed a different port, but I've never seen nor heard of such a thing, and I can't imagine what the use would have been. By the time Carbon rolled around, this entire initialization had been completely done away with.

```
        InitGraf(&qd.thePort);
```

Initialize the Font Manager, the Window Manager, the Menu Manager, and TextEdit. These all do what they say.

```
        InitFonts();
        InitWindows();
        InitMenus();
        TEInit();
```

Initialize the Dialog Manager. Pass `NULL` so there's no resume procedure. A resume procedure was, pre-System 7, a function that could be called by the OS when the infamous bomb dialog popped up and the user clicked "Resume". Generally, the function would do a jump to `main()`, restarting the application. This was the only safe thing to do, though in olden times programs would sometimes actually attempt recovery. This is the equivalent of trying to restore normal operations from a `SIGSEGV` handler in Cocoa code. Good luck with that. From System 7 on, it was unsupported to pass anything other than `NULL` for this, and I believe that doing otherwise had no effect anyway.

```
        InitDialogs(NULL);
```

Finally, set the cursor to the standard arrow and show it.

```
        InitCursor();
```

Now make sure there's no leftover cruft in the event queue from anything the user might have done between launch time and initialization. Computers were slow enough back then to make this worth doing.

```
        FlushEvents(everyEvent, 0);
```

Install handlers for the four "required" Apple Events. What is a UPP, you might ask? A UPP is a "Universal Procedure Pointer", a convoluted bit of trickery and hacking that the Mixed Mode Manager used to make sure the Toolbox could talk to 68K and PowerPC programs equally regardless of which architecture the program itself or the particular Toolbox routines involved was using. Apple sidestepped the whole problem during the PowerPC to Intel transition by just recompiling everything as a fat binary, a much more viable option in the Panther and Tiger days than in times when hard drive sizes were still measured in the tens of megabytes.

```
        oappUPP = NewAEEventHandlerUPP(AEOpenApplication);
        AEInstallEventHandler(kCoreEventClass, kAEOpenApplication, oappUPP, 0L, false);
        odocUPP = NewAEEventHandlerUPP(AEOpenDocuments);
        AEInstallEventHandler(kCoreEventClass, kAEOpenDocuments, odocUPP, 0L, false);
        pdocUPP = NewAEEventHandlerUPP(AEPrintDocuments);
        AEInstallEventHandler(kCoreEventClass, kAEPrintDocuments, pdocUPP, 0L, false);
        quitUPP = NewAEEventHandlerUPP(AEQuitApplication);
        AEInstallEventHandler(kCoreEventClass, kAEQuitApplication, quitUPP, 0L, false);
```

Finally, load up our `'MBAR'` resource and set the menu bar hold the menus it lists. Add the installed desk accessories to the Apple menu, and draw the menu bar.

`AppendResMenu()` is a bit interesting. The original implementation of this Toolbox call did exactly what it said: Appended the names of every resource of the given type to the given menu. With '`DRVR`', this meant each installed desk accessory, as those were stored as `DRVR` resources. However, in System 7, it became possible to put other things in the Apple menu. So, `AppendResMenu()` had its meaning overloaded so that when drivers were added to an Apple menu, it would instead add all the items that belonged in an Apple menu.

```
        SetMenuBar(GetNewMBar(kMenuBarID));
        AppendResMenu(GetMenuHandle(kAppleMenu), 'DRVR' );
        DrawMenuBar();
    }
```

**Menu commands**  
Menu commands are passed around in their raw form as 32-bit integers encoding the menu's resource ID in the high 16 bits and the item number in the low 16 bits. To figure out what to do, one extracts these two words and branches based on them. Yes, this means your code is intimately and directly tied to the exact layout of items in your menu resources. You remembered to make a constant for every menu ID and item number, right? No? Wow, are you in for a fun time.

You may notice that for all items in the Apple menu that I didn't define, I call the `OpenDeskAcc()` function with the name of the item. This is the second half of the overloaded `AppendResMenu()` call from earlier; it was overloaded similarly to open the appropriate Apple menu item rather than just desk accessories.

At the end, regardless of what happened, I call `HiliteMenu(0)`. Yes, that's right, the Toolbox doesn't un-hilite the menu title for you. You have to do it yourself.

```
    static void HandleMenuSelection(long response)
    {
        short       menu = (short)((response & 0xFFFF0000) >> 16),
                    item = (short)(response & 0x0000FFFF);
        Str255      name;

        switch (menu)
        {
            case kAppleMenu:
                if (item == 1)
                    DoAboutCommand();
                else
                {
                    GetMenuItemText(GetMenuHandle(menu), item, name);
                    (void) OpenDeskAcc(name);
                }
                break;
            case kFileMenu:
                if (item == 1)
                    DoNewCommand();
                else if (item == 2)
                    DoOpenCommand();
                else if (item == 4)
                    DoSaveCommand();
                else if (item == 5)
                    DoSaveAsCommand();
                else if (item == 7)
                    DoCloseCommand();
                else if (item == 9)
                    gDone = true;
                break;
            case kEditMenu:
                if (item == 1)
                    ;
                else if (item == 3)
                    DoCut();
                else if (item == 4)
                    DoCopy();
                else if (item == 5)
                    DoPaste();
                else if (item == 6)
                    DoClear();
                else if (item == 8)
                    DoSelectAll();
                break;
        }
        HiliteMenu(0);
    }
```

**Event handling**  
There are lots of different kinds of events the OS can tell you about! In Carbon, there were literally hundreds of potential Carbon Events you might be sent. But even in the Toolbox, there were plenty of things that might happen...

```
    static void HandleMouseDown(EventRecord *event)
    {
        WindowPartCode      part;
        WindowPtr           window;
```

The mouse was clicked? Well, let's figure out which window it was clicked in and what part of that window.

```
        part = FindWindow(event->where, &window);
        switch (part)
        {
```

It was in the menu bar! Call a Toolbox function to synchronously track the menu drag and return the 32-bit response, and pass that off to our menu command handler.

```
            case inMenuBar:
                HandleMenuSelection(MenuSelect(event->where));
                break;
```

It was in a window the application doesn't own? Well, let the system handle it, then...

```
            case inSysWindow:
                SystemClick(event, window);
                break;
```

It was in a window the application _does_ own! Pass it off to our own window click handler.

```
            case inContent:
                DoWindowClick(window, event);
                break;
```

In the title bar? Better track that window drag, and make sure to tell the Toolbox what the boundaries of the drag have to be.

```
            case inDrag:
                DragWindow(window, event->where, &qd.screenBits.bounds);
                break;
```

Oh, the window's close box? Track that drag, and if the mouse is released therein, call the close handler.

```
            case inGoAway:
                if (TrackGoAway(window, event->where))
                    DoCloseCommand();
```

Were there other places it could land? Plenty, but we don't have to worry about them in a really simple program. Handling the zoom box, or the expand/collapse box, or in later versions of the OS, the proxy or toolbar icons, was more trouble than it was worth!

```
        }
    }
```

Hey, a key was pressed! If the command key was down, treat it as a menu equivalent and handle that.

```
    static void HandleKeyPress(EventRecord *event)
    {
        if ((event->modifiers & cmdKey))
            HandleMenuSelection(MenuEvent(event));
    }
```

Okay, now for the more general cases of events:

```
    static void HandleEvent(EventRecord *event)
    {
        switch (event->what)
        {
            case mouseDown:
            {
                HandleMouseDown(event);
                break;
            }
            case keyDown:
```

`autoKey`? Oh, that's just if a key was held down.

```
            case autoKey:
            {
                HandleKeyPress(event);
                break;
            }
```

Update event! That's the result of `[view setNeedsDisplay:YES]` on an entire-window scale. If you don't call `BeginUpdate()` and `EndUpdate()`, even if there's nothing to actually do, you'll just keep getting update events ad infinitum.

```
            case updateEvt:
                BeginUpdate((WindowPtr)event->message);
                EndUpdate((WindowPtr)event->message);
                break;
```

Hey, the user put a disk in the floppy drive! If something went wrong, you'd better make sure they get the message, and be sure to pick some arbitrary point on the screen to show the error dialog at. Be sure to load up the Disk Initialization package first, and to unload it when you're done. Can't have it taking up memory you're not using.

The Disk Initialization package could be used for manually initializing floppies, verifying the formatting, and wiping them with zeroes. There were also a couple of extended routines in System 7.5+ for formatting disks with different filesystems.

```
            case diskEvt:
                if ((event->message & 0xFFFF0000) != noErr)
                {
                    Point       pt = { 100, 100 };

                    DILoad();
                    DIBadMount(pt, event->message);
                    DIUnload();
                }
                break;
```

Activate events just mean your window was brought forward or moved backward, usually by your own code.

```
            case activateEvt:
                break;
```

OS events had two subtypes: suspend (you're no longer the frontmost application) and resume (you're the frontmost again). There was also a "convert clipboard" flag in System 7+ which told the application to make sure the contents of the clipboard made sense, as they might have changed.

```
            case osEvt:
                break;
```

`kHighLevelEvent` is the generic dispatch point for Apple Events. `AEProcessAppleEvent()` calls through to any registered Apple Event handlers.

```
            case kHighLevelEvent:
                AEProcessAppleEvent(event);
                break;
```

A null event just means nothing's happening! Since nothing happens on its own in Toolbox-land, we check whether there's a frontmost window, and if there is, make sure any controls it contains get their share of idle time. This, for example, makes insertion points in text fields blink and indeterminate progress bars do their barbershop animation.

```
            case nullEvent:
                if (FrontWindow())
                    IdleControls(FrontWindow());
                break;
        }
    }
```

And finally, the event loop itself. Herein we find the infamous `WaitNextEvent()` function, System 7's answer to the inadequacies of the older, not-multitasking-aware `GetNextEvent()`. WNE fetched the next event from the event queue which matched the requested set of events, allowed the specified amount of time to background processes, and returned whether or not there was any event to handle.

If there was no event to handle, we do the same thing as we do for a `nullEvent`. I don't actually remember what circumstances would distinguish the false return from `WaitNextEvent()` from receiving a valid `nullEvent`, I'm afraid. In either case, loop until something says it's time to quit.

```
    static void RunEventLoop(void)
    {
        EventRecord         event;

        while (!gDone)
        {
            if (WaitNextEvent(everyEvent, &event, 30L, nil))
                HandleEvent(&event);
            else
            {
                if (FrontWindow())
                    IdleControls(FrontWindow());
            }
        }
    }
```

**`main`**  
And finally, the ever-important entry point of the application, `main()` itself!

Oh. All it has to do is call the initialization and the event loop. Even in System 7 days, there wasn't usually much for `main()` to clean up once the event loop was done.

`main()` didn't take any parameters in the Toolbox universe. There was no command line and no concept of environment variables, so there was really nothing to pass. What little information the OS passed directly to the program was in that `qd` global.

```
    void        main(void)
    {
        Initialize();
        RunEventLoop();
    }
```

**Conclusion**  
All I can say is, it really took a lot to get simple things done in the old days. But, it also felt a lot closer to the machine itself, with control possible over just about everything if you wanted it. Cocoa's really gotten away from that concept, as has programming in general. I don't miss the extra work, but I sometimes get nostalgic for the feeling of speaking the OS' own language.

That's all from me this week, I'll be back next week with a Friday Q&A. Meanwhile, enjoy Mike's article for this week, and as always, thanks for reading!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
