---
title: 'Friday Q&A 2013-04-05: Windows and Window Controllers'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2013-04-05-windows-and-window-controllers.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:e963d3d8c0b662e0'
translated: false
---

> 原文：[Friday Q&A 2013-04-05: Windows and Window Controllers](https://www.mikeash.com/pyblog/friday-qa-2013-04-05-windows-and-window-controllers.html)　·　mikeash.com Friday Q&A

Posted at 2013-04-05 13:36 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A Is On Vacation](https://www.mikeash.com/pyblog/friday-qa-is-on-vacation.html)  
Previous article: [Objective-C Literals in Serbo-Croatian](https://www.mikeash.com/pyblog/objective-c-literals-in-serbo-croatian.html)  
Tags: [cocoa](https://www.mikeash.com/pyblog/?tag=cocoa) [design](https://www.mikeash.com/pyblog/?tag=design) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [window](https://www.mikeash.com/pyblog/?tag=window)

Friday Q&A 2013-04-05: Windows and Window Controllers

by [Mike Ash](https://www.mikeash.com/)

**Variants**  
It's common to see different ways of instantiating and managing windows. Xcode's templates, for example, put an `NSWindow` instance in `MainMenu.xib`, and treat the application delegate as the window's controller. It's common to pack multiple related windows into a single nib. People sometimes instantiate windows in code wherever they need them. Some will subclass NSWindow and put the controlling code in the subclass.

The central thesis of this article is that all of the approaches listed above are wrong. Yes, even the Xcode template, the first thing people see when they check out this whole Cocoa thing, is wrong. This is the fundamental correct design:

```
    one window = one nib + one NSWindowController subclass
```

**Why**  
Fundamental separation of concerns makes this the best approach, and it ultimately costs no more time or effort than lesser approaches.

Most windows need a lot of controller functionality. Even extremely basic windows can eventually grow to take on a lot of tasks. As the largest unit of Cocoa UI, each kind of window needs and deserves its own controller class. It's possible to cram the logic for multiple windows into a single controller, but this ultimately makes no more sense than cramming the logic for a string and an array into the same class, just because you happen to be using them at the same time.

Most windows also function as independent units. It's rare to have a window that _always_ appears with another window. Even if it does now, it may not later as you evolve your UI. Because of this, each window should be in its own nib file, separate from any others. The only objects in a nib, other than `MainMenu.xib`, should be File's Owner, which is an instance of your `NSWindowController` subclass, the window itself, and any non-window objects related to the window, such as auxiliary views and controller objects. `MainMenu.xib` is a special case: it should contain File's Owner, which is the `NSApplication` instance, the menu bar, the application delegate, any other objects related to these, but _no `NSWindow` instances_.

**How**  
Start off by creating an `NSWindowController` subclass. Give it a name like `MAImportantThingWindowController` to make it obvious what it is.

Next, create the nib. Give this one a name like `MAImportantThingWindow.xib`. The Xcode template for a nib with a window it in will set things up well, so you can use that. If you prefer to build it yourself, create a new empty nib file, then add a new window to it from the library.

Set up the nib with the `NSWindowController` subclass. Set the class of File's owner to the controller class. Once that's done, connect the controller's `window` outlet to the window, and connect the window's `delegate` outlet to the controller.

That's it for nib setup, beyond whatever specific UI you want to build yourself. It's time to make the controller aware of the nib.

Xcode will pre-populate some methods in the subclass for you, but these aren't important. The `windowDidLoad` implementation it provides is useful, but doesn't contain anything interesting. The `initWithWindow:` method it provides is pointless and can be deleted.

`NSWindowController` provides a `initWithWindowNibName:` method. However, your subclass is built to work with only a single nib, so it's pointless to make clients specify that nib name. Instead, we'll provide a plain `init` method that does the right thing internally. Simply override it to call `super` and provide the nib name:

```
    - (id)init
    {
        return [super initWithWindowNibName: @"MAImportantThingWindow"];
    }
```

If your window controller needs parameters to set itself up, for example a model object that it's going to display and edit, then those parameters can be added to this `init` method.

Optionally, depending on your level of paranoia, you _may_ override initWithWindowNibName: to guard against accidentally calling it from elsewhere:

```
    - (id)initWithWindowNibName: (NSString *)name
    {
        NSLog(@"External clients are not allowed to call -[%@ initWithWindowNibName:] directly!", [self class]);
        [self doesNotRecognizeSelector: _cmd];
    }
```

I don't personally bother with this sort of guard most of the time, but it can be comforting or potentially useful to have depending on your habits and those of the people you work with.

If you have instance-specific initialization to perform, that can be done in the `init` method just like any other class. Note, however, that outlets are _not_ connected at this point, so you can't do anything that involves those. UI initialization comes later.

After the nib loads, `NSWindowController` calls `windowDidLoad`, which is the perfect override point for UI initialization:

```
    - (void)windowDidLoad
    {
        [_myView setColor: ...];
        [_myButton setImage: ...];
    }
```

The implementation in `NSWindowController` is documented to do nothing, so it's not necessary to call `super`.

`NSWindowController` loads its nib lazily. When initialized, it just remembers which nib it's supposed to use. Only when you ask for its window does it actually proceed to load the nib. Because of this, you need to be careful when accessing outlets in code that may run before the nib loads. For example, this method will silently fail if it's called before the window is loaded:

```
    - (void)setName: (NSString *)name
    {
        [_nameField setStringValue: name];
    }
```

There are two ways to work around this. One is to simply force the window to load before using an outlet:

```
    - (void)setName: (NSString *)name
    {
        [self window];
        [_nameField setStringValue: name];
    }
```

This has some unnecessary overhead if the window wouldn't otherwise be loaded at this point, but works well enough. Most of the time, a window controller is being used because it's going to display the window.

The other way is to keep an instance variable for the data as well as setting it in the UI. The setter will both set the instance variable and manipulate the outlet:

```
    - (void)setName: (NSString *)name
    {
        _name = name;
        [_nameField setStringValue: _name];
    }
```

This also needs a line of code in `windowDidLoad` to sync up the UI when it does finally load:

```
    - (void)windowDidLoad
    {
        if(_name)
            [_nameField setStringValue: _name];
        // more setup code here
    }
```

Everything else in the nib and the window controller is up to you. It all depends on what you want the window to do. At this point you can create outlets and views and controls as you normally would.

**Using the Controller**  
With this stuff in place, using the controller is simple. First, allocate and initialize it:

```
    MAImportantThingWindowController *controller = [[MAImportantThingWindowController alloc] init];
```

Perform any necessary setup:

```
    [controller setName: _name];
```

Then show the window:

```
    [controller showWindow: nil];
```

If there are multiple windows of this kind floating around, you usually want to add this controller to an array that holds all of the controllers of this type:

```
    [_importantThingControllers addObject: controller];
```

If there's only one, then you'll probably want an instance variable to hold it:

```
    _importantThingController = controller;
```

That's it! As you use it, you may find that you need to pass more data through from whatever is instantiating and manipulating the controller. To do this, just add setters to the controller class that manipulate the UI as needed, and call those setters as appropriate.

**Conclusion**  
There are a lot of ways to manage windows in Cocoa, but most of those ways are wrong. Sadly, there are a lot of different, incorrect techniques floating around out there, up to and including Apple's own Xcode templates. Now you know the proper way to do it. Just remember the principle:

```
    one window = one nib + one NSWindowController subclass
```

That's it for today. Check back next time for more wacky shenanigans. Friday Q&A is driven by reader ideas, so if you have a topic you'd like to see here, please [send it to me](mailto:mike@mikeash.com).

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
