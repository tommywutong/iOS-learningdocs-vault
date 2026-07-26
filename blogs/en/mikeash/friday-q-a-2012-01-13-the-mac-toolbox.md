---
title: 'Friday Q&A 2012-01-13: The Mac Toolbox'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2012-01-13-the-mac-toolbox.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:2698bdf82ac74764'
translated: false
---

> 原文：[Friday Q&A 2012-01-13: The Mac Toolbox](https://www.mikeash.com/pyblog/friday-qa-2012-01-13-the-mac-toolbox.html)　·　mikeash.com Friday Q&A

Posted at 2012-01-13 19:28 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Plausible Labs is Hiring](https://www.mikeash.com/pyblog/plausible-labs-is-hiring.html)  
Previous article: [Buy Videos of My VTM Presentations](https://www.mikeash.com/pyblog/buy-videos-of-my-vtm-presentations.html)  
Tags: [classic](https://www.mikeash.com/pyblog/?tag=classic) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [guest](https://www.mikeash.com/pyblog/?tag=guest) [nostalgia](https://www.mikeash.com/pyblog/?tag=nostalgia) [oldschool](https://www.mikeash.com/pyblog/?tag=oldschool) [toolbox](https://www.mikeash.com/pyblog/?tag=toolbox)

Friday Q&A 2012-01-13: The Mac Toolbox

by [Gwynne Raskind](http://blog.darkrainfall.org/)

---

**Back In My Day, We Tracked Mouse Drags 512 Pixels Through One-Bit Color!**  
When the very first Macintosh computers were released, they didn't have much of anything we take for granted in modern times. For example:

- Virtual memory
- Color
- Networking
- Hard drives
- Large software libraries

What you had was an 8 Mhz Motorola 68000 CPU, 128KB of RAM (that's _kilo_bytes, as in half the size of the raw rendered HTML for this article!) a 512x384 black & white screen, one 400K 3.5" floppy disk drive, a keyboard with no arrow keys connected with a RJ11 (telephone) plug, a one-button mouse plugged into a DB-9 connector, and if you had paid the extra money or had one left over from your Apple ][, a rather noisy dot-matrix printer with a proprietary DE-9 connector. The machine was not upgradable in any meaningful fashion.

While many of these limitations, ridiculous to the point of absurdity by modern standards, were eventually lifted, its legacy carried forward in one very visible way right up until the introduction of the Carbon API with the development Mac OS X: The Mac Toolbox, the original API for programming with the Macintosh computer.

**What Is This Toolbox?**  
The Mac Toolbox was a comprehensive set of APIs for interacting with the Macintosh hardware and operating system to read input, process data, and output results (the fundamental nature of any program). It was originally written in a mix of MC68000 assembly language and Lisa Pascal. To those used to today's Objective-C programming in Cocoa, it can look like quite a lot of gibberish.

In particular, even in its most modern incarnation before Carbon, the Toolbox did not do things that many Cocoa programmers have never even considered handling manually. To create an application which has a single window, containing a simple text field with a scroll bar, and functional File and Edit commands is the work of almost zero code in modern Cocoa. The equivelant program using the Mac Toolbox is a bit more complicated.

We start with the resource file for the program. A resource file is a document containing an organized database of resources, various formatted bits of data in a known format that the OS can load on command. Nib files are partially an evolution of resource files, but resources contained considerably more than UI elements, and were considerably harder to manage than nibs. Far and away, the most popular program for editing resources was Apple's free ResEdit tool. To save time and space, I won't walk through the fairly simple process of setting up the resources the program will use; here's the completed resources file:

![The resource file](https://www.mikeash.com/pyblog/friday-qna-2012-01-13-resources.png)

That's three `MENU` resources for the Apple, File, and Edit menus, an `MBAR` resource listing the three menus and their resource IDs, and a `WIND` resource with the basic template for the window. There's also an `ALRT`/`DITL` pair for the about box.

**Put The Tools In The Box And Rattle Them Around**  
Now for some code. Please be aware that to keep things from getitng wildly out of hand with complications, **I've ignored error checking**. This is a Bad Idea at the best of times; with the Toolbox it could often be all but suicidal. It's "okay" for sample code, but you'd never try it in reality.

No, I mean it. In Cocoa you can often get away with ignoring errors, though you shouldn't. Back in Toolbox days, you couldn't get away with it. Period.

```
    #include <Dialogs.h>
    #include <Fonts.h>
    #include <MacWindows.h>
    #include <Menus.h>
    #include <QuickDraw.h>
    #include <TextEdit.h>
    #include <Controls.h>

    enum
    {
        kMenuBarID = 128,

        kAppleMenu = 128,
        kFileMenu = 129,
        kEditMenu = 130,

        kWindowID = 128
    };

    static AEEventHandlerUPP        oappUPP, odocUPP, pdocUPP, quitUPP;
    static Boolean                  gDone = false;

    static void DoNewCommand(void)
    {
    }

    static void DoOpenDocument(FSSpec file)
    {
    }

    static void DoAboutCommand(void)
    {
        Alert(128, NULL);
    }

    static void DoOpenCommand(void)
    {
        StandardFileReply stdReply;
        SFTypeList theTypeList;

        StandardGetFile(NULL, -1, theTypeList, &stdReply);
        if (stdReply.sfGood)
            DoOpenDocument(stdReply.sfFile);
    }

    static void DoSaveCommand(void)
    {
    }

    static void DoSaveAsCommand(void)
    {
    }

    static void DoCloseCommand(void)
    {
    }

    static void DoCut(void)
    {
    }

    static void DoCopy(void)
    {
    }

    static void DoPaste(void)
    {
    }

    static void DoClear(void)
    {
    }

    static void DoSelectAll(void)
    {
    }

    static void DoWindowClick(WindowPtr window, EventRecord *event)
    {
    }

    static pascal OSErr     AEOpenApplication(const AppleEvent *theAE, AppleEvent *reply, UInt32 refCon)
    {
        DoNewCommand();
        return noErr;
    }

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

    static pascal OSErr     AEPrintDocuments(const AppleEvent *theAE, AppleEvent *reply, UInt32 refCon)
    {
        return errAEEventNotHandled;    // Don't support printing
    }

    static pascal OSErr     AEQuitApplication(const AppleEvent *theAE, AppleEvent *reply, UInt32 refCon)
    {
        gDone = true;
        return noErr;
    }

    static void Initialize(void)
    {
        MaxApplZone();
        MoreMasters();
        MoreMasters();

        InitGraf(&qd.thePort);
        InitFonts();
        InitWindows();
        InitMenus();
        TEInit();
        InitDialogs(NULL);
        InitCursor();

        FlushEvents(everyEvent, 0);

        oappUPP = NewAEEventHandlerUPP(AEOpenApplication);
        AEInstallEventHandler(kCoreEventClass, kAEOpenApplication, oappUPP, 0L, false);
        odocUPP = NewAEEventHandlerUPP(AEOpenDocuments);
        AEInstallEventHandler(kCoreEventClass, kAEOpenDocuments, odocUPP, 0L, false);
        pdocUPP = NewAEEventHandlerUPP(AEPrintDocuments);
        AEInstallEventHandler(kCoreEventClass, kAEPrintDocuments, pdocUPP, 0L, false);
        quitUPP = NewAEEventHandlerUPP(AEQuitApplication);
        AEInstallEventHandler(kCoreEventClass, kAEQuitApplication, quitUPP, 0L, false);

        SetMenuBar(GetNewMBar(kMenuBarID));
        AppendResMenu(GetMenuHandle(kAppleMenu), 'DRVR' );
        DrawMenuBar();
    }

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

    static void HandleMouseDown(EventRecord *event)
    {
        WindowPartCode      part;
        WindowPtr           window;

        part = FindWindow(event->where, &window);
        switch (part)
        {
            case inMenuBar:
                HandleMenuSelection(MenuSelect(event->where));
                break;
            case inSysWindow:
                SystemClick(event, window);
                break;
            case inContent:
                DoWindowClick(window, event);
                break;
            case inDrag:
                DragWindow(window, event->where, &qd.screenBits.bounds);
                break;
            case inGoAway:
                if (TrackGoAway(window, event->where))
                    DoCloseCommand();
        }
    }

    static void HandleKeyPress(EventRecord *event)
    {
        if ((event->modifiers & cmdKey))
            HandleMenuSelection(MenuEvent(event));
    }

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
            case autoKey:
            {
                HandleKeyPress(event);
                break;
            }
            case updateEvt:
                BeginUpdate((WindowPtr)event->message);
                EndUpdate((WindowPtr)event->message);
                break;
            case diskEvt:
                if ((event->message & 0xFFFF0000) != noErr)
                {
                    Point       pt = { 100, 100 };

                    DILoad();
                    DIBadMount(pt, event->message);
                    DIUnload();
                }
                break;
            case activateEvt:
                break;
            case osEvt:
                break;
            case kHighLevelEvent:
                AEProcessAppleEvent(event);
                break;
            case nullEvent:
                if (FrontWindow())
                    IdleControls(FrontWindow());
                break;
        }
    }

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

    void        main(void)
    {
        Initialize();
        RunEventLoop();
    }
```

As you can see, I've left a lot of the "meat", the routines that actually do anything, unimplemented. There's two reasons for that: First, it shows just how much raw boilerplate code one had to write in Toolbox-land; a lot of this was unnecessary even with Carbon. In Cocoa only a few lines of it translate to anything other than empty space.

The other reason is I just don't remember enough Toolbox anymore to show the implementation of those routines! There are at least three "major" flavors of Classic code: The old System 6 routines, the newer System 7 routines, and the "appearance-aware" routines that came with OS 8.5. Keeping track of which functions belong to which era is problematic enough without realizing that with the amount of manual lifting that has to be done, the 5-line Cocoa app becomes a 2000-line Classic program.

**Conclusion**  
All in all, I feel I have to apologize for the terseness of this article. I'd hoped to explore the Toolbox in more depth, but I don't have the time to invest in re-learning a system that, in all likelihood, I will never use again. The Toolbox was a brilliant API for its time, and its worst fault was that it suffered from what all good things do: Age.

The Toolbox is gone, but not forgotten. Classic Mac OS, I salute you. Thanks for reading, everyone; I'll be making a followup post in the next few days looking at the code in detail, and I'll be back in two weeks with another Friday Q&A. Stay tuned for Mike's article next week!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2012-01-13-the-mac-toolbox.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
