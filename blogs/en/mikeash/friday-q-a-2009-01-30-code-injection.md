---
title: 'Friday Q&A 2009-01-30: Code Injection'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2009-01-30-code-injection.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:4fdf6968dd930d74'
translated: false
---

> 原文：[Friday Q&A 2009-01-30: Code Injection](https://www.mikeash.com/pyblog/friday-qa-2009-01-30-code-injection.html)　·　mikeash.com Friday Q&A

Posted at 2009-01-30 18:34 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2009-02-06: Profiling With Shark](https://www.mikeash.com/pyblog/friday-qa-2009-02-06-profiling-with-shark.html)  
Previous article: [Friday Q&A 2009-01-23](https://www.mikeash.com/pyblog/friday-qa-2009-01-23.html)  
Tags: [codeinjection](https://www.mikeash.com/pyblog/?tag=codeinjection) [evil](https://www.mikeash.com/pyblog/?tag=evil) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [hack](https://www.mikeash.com/pyblog/?tag=hack)

Friday Q&A 2009-01-30: Code Injection

by [Mike Ash](https://www.mikeash.com/)

**What It Is**  
 Let's start with a real easy example:

```
    Fear:~/shell mikeash$ cat injectlib.c
    #include <stdio.h>
    void inject_init(void) __attribute__((constructor));
    void inject_init(void)
    {
        fprintf(stderr, "Here's your injected code!\n");
    }
    Fear:~/shell mikeash$ gcc -bundle -o injectlib injectlib.c
    Fear:~/shell mikeash$ gdb attach `ps x|grep Safari|grep -v grep|awk '{print $1}'`
    GNU gdb 6.3.50-20050815 (Apple version gdb-962) (Sat Jul 26 08:14:40 UTC 2008)
    [snip]
    0x93e631c6 in mach_msg_trap ()
    (gdb) p (void *)dlopen("/Users/mikeash/shell/injectlib", 2)
    $1 = (void *) 0x28f3b5b0
    (gdb) 
```

And if we look in our Console (where Safari's stderr goes), we see:

```
    [0x0-0x17f97f8].com.apple.Safari[23558]: Here's your injected code!
```

And that's code injection in a nutshell. You bang into another process, load some of your own code, and get it to run. What you do there is up to you!

**How to Do It**  
 Of course, using `gdb` to inject code isn't exactly what one might call practical. For one thing, `gdb` is unlikely to be present on your users' systems, as it's a developer tool.

However there are better alternatives, some as part of Mac OS X and some as third-party tools.

**Input Managers**  
 [Input Managers](http://www.cocoadev.com/index.pl?InputManager) are intended to provide keyboard input mechanisms for allowing custom ways to translate keystrokes into text on the screen, for example a custom Chinese input method.

They aren't very useful for their stated purpose on Mac OS X because they only work in Cocoa apps, not Carbon apps. But because they work by loading the input manager directly into every Cocoa application, they're great for code injection. All you need to do is build a bundle [with the right layout](http://developer.apple.com/documentation/Cocoa/Conceptual/InputManager/Tasks/InputServerDeployment.html#//apple_ref/doc/uid/20001039), put it in the right place, and suddenly you're loaded into every Cocoa app.

Of course Apple isn't too keen on code injection and they've threatened that they might take our toys away at some point. Input Managers still work on Leopard, although they've been restricted and now require root access to install them. They may or may not still be around on Snow Leopard, it's hard to say yet.

Input Managers are a bit troublesome. First, on Leopard, they have to be installed with some fairly precise permissions and that's annoying. Second, they load into every Cocoa app even if you only want to fiddle with one of them. The third-party [SIMBL](http://www.culater.net/software/SIMBL/SIMBL.php) helps with both of these problems. It will load standard bundles placed in standard locations (although SIMBL itself still needs the special magic installation to function), and it allows plugins to provide a list of applications they want to load into.

**Mach ports**  
 [In a previous edition](https://www.mikeash.com/pyblog/friday-qa-2009-01-16.html), I briefly mentioned that mach ports allowed injecting code into other processes. This works because mach ports can allow essentially full control over other processes. If you can get your hands on the right port (and see the `task_for_pid` function for how to do that) you can do things like map new memory into the process with custom contents and create a new thread in the target process that executes that memory. Set things up right and you have code injection.

This is pretty hard to pull off, as it ends up being a pretty complex bootstrapping process. Fortunately, the third-party [mach_inject](http://extendamac.svn.sourceforge.net/viewvc/extendamac/trunk/code/) does all the hard work for you.

There are, of course, some downsides. One is that you need to run as root (or as part of the `procmod` group) to be able to get the necessary task port, even if you're injecting code into another process owned by the same user. Another is that the time of injection is non-deterministic. Input Managers load at a fairly well defined point in the application startup process, but mach_inject loads whenever your process can make the call, which could be much later, and potentially earlier, before things are really set up properly yet.

**APE**  
 [Application Enhancer](http://www.unsanity.com/haxies/ape/sdk) is a third-party injection mechanism. It's kind of like a better SIMBL which can load code into any application, not just Cocoa apps, and which loads it a little earlier than SIMBL does (which is an advantage for certain kinds of code).

Once again, there are downsides. Probably the biggest downside is that APE is by far the largest offender in the code injection war. A lot of people out there know APE by name, think that APE is evil, and refuse to use it.

Another big downside is that the company which makes APE is no longer maintaining it in a timely fashion. The first non-beta release of APE that supported Leopard was made in August 2008, a year after that OS version shipped. It's currently unknown whether they even plan to support Snow Leopard at all, let alone how long it will take them to release Snow Leopard support if they do. At this point, APE is good for experimentation but I can't recommend basing an actual product on it.

Lastly, APE is non-free and requires a license fee for commercial/shareware products, although that fee is quite reasonable.

**Miscellaneous**  
 Those are the main mechanisms, but the system provides a few more, of varying utility:

1. **Contextual menu plugins.** These are Finder plugins intended to extend the contextual menu in the Finder. Of course once they're loaded, they can do whatever they want. The downside is that, as I understand it, they're loaded lazily on Leopard so you don't get your shot until and unless the user actually brings up the plugins section of the contextual menu. And of course it only gets you into the Finder.
2. **Scripting Additions.** These are meant to be used to extend the capabilities of AppleScript on the system, but they actually work by loading into an application which is responding to the appropriate Apple Event. For example, run this command in your shell: `osascript -e 'tell app "Finder" to display dialog "I just injected some code into Finder!"'` Replace that standard scripting additions command with your own and off you go.
3. **WebKit plugins.** These are rarely useful unless you really are implementing a browser plugin, but it's a way to potentially get code into Safari and other WebKit-using applications.
4. **Kernel extensions.** Not really an injection mechanism, but once you're in the kernel you rule the system and can do whatever you want to anything.
5. **Buffer overflows.** Don't laugh too hard, people have done this! One of the older iPhone jailbreaking mechanisms used a buffer overflow in Safari to get in and do its dirty work. Of course these are absolutely not something to rely on, as vendors have this weird idea that they ought to fix them once they're discovered.

**What's It Good For?**  
 Code injection is a powerful tool for extending applications you don't control. For example, my own LiveDictionary uses the Input Manager mechanism to load into Safari so that it can monitor the user's keyboard and mouse inputs in that app, and read the text under the mouse cursor at the appropriate times. (This is something that could be done using the Accessibility API today, but at the time LiveDictionary was written it wasn't yet functional enough.)

For more examples, just take a look at [Unsanity](http://www.unsanity.com/). They have a whole line of products based around APE and code injection, doing things ranging from GUI themes to mouse cursor customization to custom menus.

Basically, any time you need control over objects inside another application, and that application doesn't expose a mechanism to get at them from the outside (such as AppleScript or a plugin interface), code injection is how you do it.

How do you accomplish your task once you're inside? Well that all depends on exactly what you want to do. It's much like writing code in your own application, except you have much less control about how things work and much less information about how things are structured. It's the kind of thing where if you don't know how to write the injected code, it's probably something you shouldn't be doing in the first place. Since you're running code in a foreign process, you're in an unforgiving environment where mistakes are much more dire than usual.

**What's Bad About It?**  
 Code injection is dangerous and nasty and very special care needs to be taken when doing it.

There are two fundamental reasons for this. First, when you're in another process, you have much less control over the environment than usual. It's also easy for that process to make certain assumptions about how things work. For example, you might pop up a window, while the application assumes that all windows are ones that it created. Crash, boom, game over.

The second reason is more of a political one. It's extremely rude to crash another process. Users hate it when you crash their other programs. Developers hate it when they get crash reports and support requests caused by your code. While crashing is never a good thing, crashing somebody else's program is an order of magnitude worse than crashing your own standalone program.

**Practical Advice**  
 Given the dangers, how should you proceed? Here are some very general guidelines:

1. Avoid code injection if at all possible. Take another look at your options. Can you use Accessibility to do what you want? AppleScript? Is there an official plugin interface? Sometimes you really have no choice, but exhaust all other options first.
2. Load into as few programs as possible. If you're using a mechanism like Input Managers that loads into a lot of applications but you only want to hit a few, be sure to restrict your module to just the ones you want. This reduces the chances of affecting an application you didn't even need to be in. For Input Managers, you can use SIMBL to accomplish this.
3. Do as little in the injected code as possible. If you do a lot of complicated work in your code, move that into a background process and talk to it using Distributed Objects or another IPC mechanism. That way, if something in the background process crashes, it won't take other applications down with it. (LiveDictionary is a good example of this, the Input Manager itself basically just grabs input and text out of the target application, and all of the dictionary parsing, lookup, and display is done in an LSUIElement application.)
4. Modify your environment as little as possible. Got a handy Cocoa programming trick that involves posing as a common AppKit class? Don't do it. Need to install some category methods with common names on NSObject? Forget about it. Want to load some enormous framework that you don't _really_ need? Best to avoid it if you can. Any large application is going to have hidden assumptions about the environment it runs it, often completely inadvertently. Try to modify as little as possible to avoid make it crash when you step over one of those invisible lines.
5. Program defensively. I mean _really_ defensively. Check every potential failure spot thoroughly, and fail as gracefully as possible. Remember, it's much better for your injected code to stop working or disable itself but leave the application running than it is to crash the application.

**Wrapping Up**  
 That's it for this week's Friday Q&A.; Come back next week for another show. Bring a friend and get 50% off the price of admission!

Did I overlook something important? Forget to mention your favorite technology? Do you passionately hate code injection in every form? Post your comments below.

And as always, Friday Q&A; is powered by your suggestions. If you have a topic you'd like to see discussed here, post it below or [e-mail me](mailto:mike@mikeash.com). (Your name will be used unless you ask me not to.)

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2009-01-30-code-injection.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
