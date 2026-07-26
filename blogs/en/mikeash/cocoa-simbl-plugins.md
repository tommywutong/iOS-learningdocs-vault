---
title: Cocoa SIMBL Plugins
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/cocoa-simbl-plugins.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:4d597ea926bb229c'
translated: false
---

> 原文：[Cocoa SIMBL Plugins](https://www.mikeash.com/pyblog/cocoa-simbl-plugins.html)　·　mikeash.com Friday Q&A

Posted at 2006-03-25 00:00 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Custom NSCells Done Right](https://www.mikeash.com/pyblog/custom-nscells-done-right.html)  
Previous article: [Fluid Simulation for Dummies](https://www.mikeash.com/pyblog/fluid-simulation-for-dummies.html)  
Tags: [cocoa](https://www.mikeash.com/pyblog/?tag=cocoa) [injection](https://www.mikeash.com/pyblog/?tag=injection) [plugin](https://www.mikeash.com/pyblog/?tag=plugin) [simbl](https://www.mikeash.com/pyblog/?tag=simbl)

Cocoa SIMBL Plugins

by [Joshua Pokotilow](http://tuneteller.com/)

One such option is [SIMBL](http://www.culater.net/software/SIMBL/SIMBL.php) (pronounced "cymbal"), which is a Cocoa plugin loader for OS X. Once a user has SIMBL installed, you can create XCode projects of type "Cocoa Bundle", compile them and drop the output in either "~/Library/Application Support/SIMBL/Plugins" or "/Library/Application Support/SIMBL/Plugins" on the user's machine. "What's the point?", you may ask. By doing this, any code you write inside your plugin project will have access to any objects that belong to the application you want your plugin to load for. In other words, you can use SIMBL plugins to enhance Cocoa applications! I'll pause for a moment as the full ramifications of this idea wrap their tendrils around your consciousness.  
  
*pauses*  
  
Alright. So once I understood everything I described above, the concept I had the hardest time grasping was how to know what objects resided in applications I didn't write. Well, as it turns out, you don't need to know much about proprietary objects that reside in specific applications, because you can already do a whole lot with generic ApplicationKit objects that exist in nearly every Cocoa application, such as the menu bar, the main window, etc. For the sake of clarification, here's an example: say you're in a strange mood and you decide you really want to inject a new menu item into the Safari main menu that tells you the time in India. Assuming you already have a working subclass of NSMenuItem defined called InternationalClock, the following code snippet makes sense:  
  
 // Create our clock.  
 NSMenuItem *indiaClock = [InternationalClock clockForCountry: @"India"];  
  
 // Inject it.  
 NSMenu* safariMenuBar = [[NSApplication sharedApplication] mainMenu];  
 [safariMenuBar addItem: indiaClock];  
  
If you want to get more specific and modify proprietary Safari objects, things get a little hairier -- you'll need to know what custom classes are defined in Safari, perhaps what instance variables exist in these classes [(1)](#1), and certainly what methods you may invoke. For this, I would recommend a great CLI utility called [class-dump](http://www.codethecode.com/Projects/class-dump/), which is also mentioned on the wonderful wiki at [http://www.culater.net/wiki/moin.cgi/CocoaReverseEngineering](http://www.culater.net/wiki/moin.cgi/CocoaReverseEngineering). class-dump lists custom classes, along with their corresponding method names and instance variables for any Cocoa application you pass it, and I'm willing to bet that it could suffice as the only utility that most developers need to accomplish their plugin-writing goals.  
  
(1) -[NSObject valueForKey:] is a very handy method for retrieving object attributes, such as private instance variables, from inside your custom bundle.

**No comments:**

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.
