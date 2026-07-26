---
title: What Happened to Dockyard?
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2009/07/What-Happened-to-Dockyard/'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:e0a06e2ec0495379'
translated: false
---

> 原文：[What Happened to Dockyard?](https://belkadan.com/blog/2009/07/What-Happened-to-Dockyard/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Garbage Collectors and Stack Drawers](https://belkadan.com/blog/2009/06/Garbage-Collectors-and-Stack-Drawers/)

[Scripting Bridge](https://belkadan.com/blog/2009/07/Scripting-Bridge/) »

## [What Happened to Dockyard?](#)

As any programmer knows, feature creep is dangerous, deadlines tend to slip, and work expands not just to fill the time allotted, but far past.

As a Dockyard fan would know (though I doubt there are any), Dockyard 2.0 is now almost _two years late_. Yes, there was supposed to be a release shortly after Leopard, after I could work out the kinks. What happened?

Well, first I didn’t get my hands on Leopard for quite a while. Then I noticed one of its big new features—Spaces—had turned out to be a big new problem for Dockyard. (Basically, the Dock controls Spaces, and Dockyard forces the Dock to reload by quitting it. The result would be windows getting “trapped” in another Space and suddenly popping back…or not.) _How to fix this…_ I wondered. And the current Dockyard alphas do have an imperfect workaround in place now.

But that’s just an excuse. The real reasons for Dockyard’s inordinate delays are threefold…

**Time**. As a college student, webmaster for multiple sites, developer supporting a few existing projects, singer and arranger for various groups, etc., I underestimated the amount of time that I could put towards new development of long-term personal projects. The “[ten-hour Tetris](http://belkadan.com/blog/2009/03/JavaScript-Tetris/)” a few months back was a sort of self-dare, about what could be accomplished in a short time. But Dockyard isn’t a short-term project, it’s a large project, which I have high standards for.

A surprising factor was **Conflict of Interest**. I haven’t mentioned it on this site before, but last summer I was fortunate enough to have an internship at Apple, Inc. Yes, _the_ Apple. This summer I’m back there again (though in a different group), and have the same problem: working on independent Cocoa apps (maybe even web apps) can _definitely_ be a conflict of interest. Particularly apps like Dockyard and the Safari plugin I [hinted at](http://belkadan.com/blog/2009/04/Hacking-Safari-4-for-Great-Convenience/) a few weeks ago, which are full of what’s been called “undocumented goodness” but what could easily be construed as “inside information”. To keep things clear, I’m not touching Cocoa development during the summer.

(By the way, if you want to tell me about something you want fixed, don’t. [File a bug](https://bugreport.apple.com) (and [here too](http://openradar.appspot.com/)) — we do read them, though a few months before a new OS is released is probably not the best time for a response.)

The biggest problem, though, is what I said before: Dockyard is now a **Large Product**. When did that happen?

Let’s look at Dockyard itself. Dockyard v1.0 was a simple menu listing of docks. You couldn’t even change the name of a dock after it had been created, and you couldn’t launch items from the menu. The feature that was so valuable to me, after the core functionality, was the implementation as a menu extra, a first-class status item like the clock, battery, or even the Scripts Menu. One of several undocumented strategies in a app (actually a plugin) written during my first year of Objective-C.

Dockyard 1.5 added renaming (hooray) and that obvious-but-great feature of opening items in another dock by choosing them from a submenu. Other dock switchers already did this, but it worked well in Dockyard. No problems yet.

Dockyard 1.6…menu extra, plus widget, _plus_ manager application. Uh-oh! The old Dockyard format was stretching, and a lot of code went into keeping these three in sync if you had them all open. Plus, killing the Dock also means killing the Dashboard. I turned that into a feature by allowing you to switch Dashboard configurations along with your dock. But the current system was untenable.

And now we came to the feature requests and expectations: integration with VirtueDesktops or another pre-Spaces desktop manager, integration with Spaces itself, global hotkeys, switching via screen corners or sides (I had liked this feature in another dock switcher), and of course, not disrupting Spaces to the point of unusability. All of these gave me delusions of grandeur, making me envision a grand plug-in model for switch triggers and switch actions, and an implementation based on distributed objects, instead of keeping separate Dockyard “clients” in sync.

Alas, such visions were much too far-reaching. The one bug that’s a show-stopper is the Spaces-disruption, and everything else merely drained my time and made the project spin out of control. I don’t want to abandon the project, but I look around at [Dock Spaces](http://www.nscoding.co.uk/) and [Docks](http://www.thoughtfultree.com/app/docks) and see two products with nice UIs that implement the core functionality _as well as I do, or better_. (Actually, Dock Spaces used to have better UI than it does now. Oh well.)

Both of those still use the “kill-the-dock-to-reload” strategy, though, so both are subject to Leopard’s occasional Spaces-related window-loss. And neither has a true menu extra, though both have the Apple-supported “status item” available. (The difference to the user is mainly that menu extras can be reordered, instead of just adding on to the left end of the status bar. The difference to the developer is that menu extras run inside a single app called SystemUIServer, and can have a few extra features beyond having a plain menu.) It’s just like that situation four, five years ago: there are apps that do it, but not the way I’d do it. Only now I have three large roadblocks keeping me from doing it my way.

So, a plan. First, assume Dockyard is not coming back. GenericToolbar has already been retired, and [PHP/CC](http://belkadan.com/blog/2007/09/Short-Xcode-Tip-on-Plugins/) was never updated for Xcode 3. (By the way, Xcode is not easy to reverse-engineer, basic support for other languages got a little better anyway, and I’m not working on PHP-based projects these days. Don’t expect an update.) That leaves Webmailer as the lone released project for Belkadan Software right now, and while it deserves a quick look-over, I think it’s actually doing pretty well. The Safari keyword plugin will join it hopefully in early autumn.

As for Dockyard, I still want that functionality. Here’s a short list of must-have features:

- Must not break Spaces (unless the user tells it to use old-style switching)
- Menu extra, with submenus for the contents, i.e. “at least what v1.5 had”
- Scripting support, so it can be controlled from outside
- Distributed notifications, so other things can react to it
- Switch docks, picking up user modifications along the way

And here’s some nice-to-have features:

- Manager interface. Hopefully a better one than the 1.6/1.0 release.
- Global hot-keys
- Screen corners and edges

Maybe some day in the future I’ll get to all of these. But meanwhile, I’m going to have to retire Dockyard as well. It’s had to suffer the embarrassing “10.3 - 10.4” on the front page of Belkadan Software long enough. Come the next site redesign (hopefully before the end of summer, but maybe not until the Safari plugin’s release), Dockyard (and GenericToolbar) will be leaving their place of prominence and relegated to a “past products” section.

Apologies to anyone who was desperately waiting for Dockyard 2.0. I’m disappointed, too, but it’s far past time to be realistic about the future of this project.

---

For those of you who were really hoping to get the solution to the Downloads stack drawer problem, it goes something like this. Attach a folder action to your Downloads stack that moves the drawer item out of the drawer and then back in when an item is added. Why don’t I have an implementation to give you? Simply, because it doesn’t always work. Safari’s trick of putting a package down for temporary downloads, then moving the downloaded file out of the package when it’s done, seems to confuse the folder action system. Or maybe it’s just throttling it, or something. Or it’s infinite-looping (firing the action on the drawer icon item coming back). Whatever it is, I sometimes see the drawer pop to the front and sometimes don’t. YMMV.

If you really care about this, file a bug with Apple to allow custom stack icons, or badging, or _something_ to avoid the “stack of folders” syndrome seen in the last post.

This entry was posted on [July](https://belkadan.com/blog/2009/07) 08, [2009](https://belkadan.com/blog/2009) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Dockyard](https://belkadan.com/blog/tags/dockyard)
