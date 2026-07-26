---
title: Dashboard Rant
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/dashboard-rant.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:f57515f479bf492b'
translated: false
---

> 原文：[Dashboard Rant](https://www.mikeash.com/pyblog/dashboard-rant.html)　·　mikeash.com Friday Q&A

Posted at 2005-04-29 00:00 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Using FileMerge with subversion](https://www.mikeash.com/pyblog/using-filemerge-with-subversion.html)  
Previous article: [Name/comment conflict](https://www.mikeash.com/pyblog/namecomment-conflict.html)  
Tags: [dashboard](https://www.mikeash.com/pyblog/?tag=dashboard) [rant](https://www.mikeash.com/pyblog/?tag=rant)

Dashboard Rant

by [Mike Ash](https://www.mikeash.com/)

The first problem is that doing the entire widget in HTML throws out all of the good GUI builder stuff that we've come to expect from Interface Builder on OS X. Using Interface Builder and Cocoa Bindings, you can do a lot of things without writing any code.  
  
 Want to create a slider, a text box, and have both of them link to a preference and update each other when the user changes one? This is a two-minute task in IB which involves writing no code. Want to do the _exact same thing_ in a Dashboard widget? You'll have to write code (even if it is just HTML) to create the controls, you'll have to position them by typing pixel values into your favorite text editor, and finally you'll have to write a bunch of glue code, in JavaScript, to hook it all together. This doesn't even take into account the fact that there is no slider control in standard HTML, so you'll probably have to build your own. I don't really understand how this is supposed to make things easier for the non-coder, and it certainly makes life hard for programmers.  
  
 Another problem is that Dashboard has no decent debugging facilities whatsoever. Because it's all done with WebKit, once you run out of the possibilities of straight HTML then you have to start writing JavaScript.  
  
 I have nothing against JavaScript in particular, but Dashboard makes it almost impossible to debug them. As any good programmer knows, programming mostly consists of debugging, so this makes life difficult.  
  
 A Dashboard widget can simply be a normal web page, using normal HTML, CSS, and JavaScript, in which case normal JavaScript debugging techniques may be used. I'm told that JavaScript debuggers exist, and I'm sure they would be handy for this kind of thing. The problem is that normal web pages can't do things like access other pieces of the user's system (for good reason!), flip their Dashboard widget to the back to let the user set preferences, etc.  
  
 Because of this, if your widget does any of the things that make widgets unique and interesting, you can't really test or debug your widget outside of Dashboard itself, because only Dashboard has the necessary JavaScript APIs to do these extra things. To a certain extent, you can bypass this by stubbing out your Dashboard-specific code, but you can only go so far.  
  
 In the widget I worked on, I ended up having a severe problem with a Dashboard-specific API, namely the widget.system() function. I couldn't test in Safari, I couldn't use any kind of debugger, and it was a nightmare to work out. I finally abandone d the widget.system() interface altogether and wrote a widget plugin to do the work instead.  
  
 And this brings us to our first Dashboard hint! Avoid widget.system() at all costs when working with any significant amount of data. It's highly prone to lockups, intermittent failures, deadlocks, etc., whether in synchronous or asynchronous mode. I would have requests that worked fine and then failed the second time they were requested, locking up my widget and making it unusable, with no indications as to why. I tried every possible workaround I could think of, but the problems never went away until I ditched the widget.system() call and switched to using a widget plugin. I suggest you short-circuit the problem and simply make a widget plugin to begin with; they're ridiculously easy to create.  
  
 Another problem with widgets is that they all look and act totally differently from everything else. This is a problem both for users and for developers. It's a problem for users because, in addition to the already confusing array of Aqua, Metal, Wood, Milk, etc., there's now also a zillion different Dashboard interfaces.  
  
 It's a problem for developers because they have to actually, _create_ these unique interfaces if they want to fit in with Dashboard. (Apple explicitly discourages using standard Aqua widgets; you're not even supposed to use a standard HMTL submit button, but rather create your own graphical submit button.) So every time you want a button, a scroll bar, a slider, a radio button, a checkbox... you have to make your own graphics and write a bunch of support code behind it.  
  
 The Dashboard environment is simply a gigantic step backwards in almost every way. A perfect example of this is the localization system. If you want to localize your widget, you basically have to construct the whole localization system from scratch yourself by building a dictionary in JavaScript and writing a function to retrieve values from it. Of course you can just copy/paste the code from Apple's examples, but that's beside the point; Apple doesn't provide any of this for you in an API, and it doesn't use the standard .strings format that's used in all Cocoa and Carbon applications for localization. Goodbye to working with AppleGlot, PowerGlot, or any other localization apps.  
  
 In short, the entire Dashboard environment is, for the programmer, like a nostalgia trip back to the 1980s, when you had to do everything yourself. This isn't entirely fair; JavaScript has nice string APIs, regular expressions support, etc. However, when it comes to creating a GUI, all of the progress which Mac OS X has brought us gets thrown out the window, and it's back to the coding equivalent of banging rocks together to make fire.

**19 comments:**

what a crybaby…but I do agree. :)

**eddienull** - 29 April '05 - 11:18

Dashboard is mostly for ‘web designers’ who are used to working in crappy environments.

**john** - 29 April '05 - 12:39

I think it’s a step in the right direction. Opportunities for full Cocoa/Carbon programmers to create tiny little useful programs has been here for a long time. Dock drop-ins, Menu extras, Contextual plug-ins and small programs – you name it.  
  
 Dashboard adds not much new in this respect – just a nice Expose effect and an universal F12 system-wide activation. That’s it. So the real BIG feature, in my oppinion, is that is raises the number of potential developer by one or two orders of magnitude.  
  
 Exactly this is why I think Dashboard will be huge. (And yes – I do agree, from program-design perspective, it’s a huge step backwards. It’s just that Dashboard widget creation is not programming – it’s scripting.)

**zzen** - 15 May '05 - 17:54

I don’t get it – if you’re a Mac developer experienced in Interface Builder, why not just write an actual Cocoa app instead of a Dashboard widget? You sound like Lance Armstrong with a set of training wheels, complaining that they don’t let you corner as tightly as you’d like.

**Michal Migurski** ([email](mailto:mike-mikeash@teczno.com)) ([link](http://mike.teczno.com)) - 16 May '05 - 19:42

Lots of bona-fide Mac developers will be migrating little long-running tools to Dashboard, rather than have them cluttering up the Dock or fighting with NSUIElement complexity (removing an app from the Dock means losing its menubar). I’ve got one myself.

**Nat Irons** ([link](http://bumppo.net)) - 16 May '05 - 21:17

I wrote a widget in about 4 hours to download weather radar images, resize and display them. The difficulty was to make it only request updates when someone is looking.  
  
 There is a most helpful debug() subroutine at the end of Apple’s world clock which allows you to print debug messages to the screen.  
  
 At least the standard widgets are readable source, and you’ll need to if you want to see how much code it takes to do the flip effect.

**Scott Schram** ([link](http://schram.net)) - 16 May '05 - 21:28

I’m not writing an actual Cocoa app because actual Cocoa apps cannot be displayed in the Dashboard. If I want something to be in the Dashboard, the I have to write a completely separate thing. This is one of my big complaints; Apple simultaneously created a new user interface area, and a new API, but has tied the two together strongly. I can’t use Cocoa to make Dashboard widgets, and somebody who actually likes the Dashboard programming environment can’t use what he knows anywhere else.

**Michael Ash** ([email](mailto:mike@mikeash.com)) ([link](http://www.mikeash.com)) - 17 May '05 - 08:01

Shades of Hypercard… “simple” development environments always involve trade-offs. In my first official job as a developer I was tasked with porting an existing Mac application to NeXT, using the NextStep environment which was very similar to Cocoa. I learned early on about the trade-offs of using a system where someone else makes decisions on your behalf in order to save you the trouble of making them yourself… depending on what you’re writing, sometimes it’s just easier to be a developer than a scripter.

**Waldron Faulkner** ([email](mailto:wit_happens@yahoo.com)) - 17 May '05 - 17:22

Dude, if you want IB, build a Cocoa app!!! Dashboard is **not** for you! It’s for the rest of us!

**pb** ([email](mailto:pb@pb.com)) - 19 May '05 - 15:50

I’ve had some trouble with widget.system() much as you describe…with larger amounts of data. My next plan of attack was precisely what you describe – a plugin which uses NSTask to provide the same functionality – but I wanted to check around online to be sure I wasn’t missing some silly fix. Anyway, I acknowledge that the above wouldn’t be difficult, but even due to that fact, would you consider simply making your plugin generally availible for myself (who could make it, but I’m lazy) and others (who might not know any Cocoa at all) to make use of?

**Eben Eliason** ([email](mailto:eben@interdimensionmedia.com)) ([link](http://www.interdimensionmedia.com)) - 20 May '05 - 12:51

To pb: The Dashboard is a totally different area in the GUI. Why shouldn’t I be able to access it from a normal application? Also, why don’t the rest of you want to use your awesome Dashboard skills to build apps that don’t require pulling up the Dashboard?  
  
 To Eben: my use of widget.system() was only to avoid writing a plugin; I didn’t actually need to call through to the shell. As such, my plugin doesn’t do anything with NSTask or anything like that. If you want an example plugin, there’s a good one in /Developer/Examples/Dashboard called Fortune.

**Michael Ash** ([email](mailto:mike@mikeash.com)) ([link](http://www.mikeash.com)) - 22 May '05 - 09:57

As for the UI stuff, widget UIs need to be unique, more so than a normal Aqua app. They need to be (practically) instantly recognizable. Using color in this way gets you a widget that people will remember to look for when they show Dashboard. “I need xyzI need to look for the (purple/green/blue/etc.) widget.”

**Chad** - 29 May '05 - 17:18

Yeah, widget.system has some flaws… Here’s some info I wrote up on my trials and workaround with widget.system:  
  
[http://4haks.blogspot.com/2005/06/overco..](http://4haks.blogspot.com/2005/06/overcoming-4096-byte-limit-of.html)

**Stacey Abshire** ([link](http://4haks.blogspot.com)) - 04 July '05 - 13:32

The big problem with widget.system() is that the input it reads can only be 4095 characters long. It looks like that xmlHTTP code is the way to go—I’m pleased google found this page!

**Brenda** ([email](mailto:brenda@aol.com)) - 09 July '05 - 19:08

The 4k limit for widget.system() is probably because of the size of the kernel’s pipes. A naive way to implement a subprocess is like this:  
  
 spawn subprocess  
 wait for process to terminate  
 read contents of pipe  
  
 But if the pipe fills up, then the process will get stuck waiting for you to empty it, while you’re waiting for it to die. It’s a common bug, but it’s shocking that Apple managed to get it wrong for this. You’d think they would have tested it with output larger than 4k; what were they doing during those 18 months of Tiger development?  
  
 Anyway, Brenda, I’m happy to see that this article was helpful to someone, even if it was indirectly.

**Michael Ash** ([email](mailto:mike@mikeash.com)) ([link](http://mikeash.com)) - 12 July '05 - 10:20

Mike, yeah I agree, there are a lot of problems, initially. Things sometimes seems so convoluted when working with widgets. Even XMLHttpRequest, although good, fails to work well with anything other than text or xml. Also, try opening a file dialogue from a widget, or doing an modal alert box.  
  
 On the plus side though, if you’ve got good reuse skills they will take you a long way past these problems.  
  
 For example I managed to easily reuse the scroller, fader and stretcher examples from apple, and yeah they were buggy, but quite easy to fix.  
 If you are having trouble debugging, turn development mode on in Safari and Dashboard, and get Mozilla which has a great debugger, Venkman.  
 Another plus is that Javascript is way more portable than Cocoa. Some of the widgets you see today on your dashboard will likely end up on mobile devices next year.  
  
 Debugging scripts can also be faster than debugging compiled code, since you don’t have to wait for compiles to finish, although fix and continue helps for that.  
  
 In terms of time taken to code an app, well, in my case, I managed to write my first widget (currency tracker) in 3 days with 0 (zero) javascript experience, and only limited html and css, but then I have lots of coding experience. My next one (a2b) took about a week. Both got into Apple’s top 50. That compares with 3 months for my first cocoa app, although that was a lot bigger.  
  
 I put it down to javascript’s simplicity, the fact that regexes are part of the javascript language (a big plus), and the sheer amount of learning you have to do to get into Cocoa, and at the end of the day, if you need Cocoa you can always write a Cocoa plugin for a widget.  
  
 I was betting my business on writing cocoa apps, now I’m going for widgets, in the short term at least.  
  
 Mike Amy

**Mike Amy** ([link](http://www.cocoade.com)) - 12 July '05 - 10:34

That scripting language comment is a total red herring. You can write Cocoa apps in at least half a dozen scripting (by which I mean that there is no compile-link-run cycle) languages, including Perl, Python, Lisp, Ruby, Lua, and F-Script, if that’s all you want.  
  
 Being able to reuse code is another red herring. Wonderful that you can reuse code to get something like a scroll bar or window resizing; meanwhile, I’m busy getting real work done in Cocoa, because I get those features for free.  
  
 An environment’s worth is not measured in how easy it is to do easy things, but how easy it is to do difficult things. Easy things will be easy regardless, but a poor environment can make difficult tasks nearly impossible. Likewise, it’s not measured in how easy it is for newbies, but how easy it is for people who have taken some time to learn it. You’re only a newbie for a little while, but you have years to be an expert. In both of these respects, Dashboard falls down hard.  
  
 Dashboard is great for putting together cute demos, but it’s horrible for making anything truly interesting, and not terribly user-friendly to boot.

**Michael Ash** ([email](mailto:mike@mikeash.com)) ([link](http://mikeash.com)) - 12 July '05 - 16:29

It seems that all debugging complaints have now been invalidated by the following page:  
  
[http://developer.apple.com/technotes/tn2..](http://developer.apple.com/technotes/tn2005/tn2139.html)

**eobet** ([link](http://www.eobet.com/)) - 16 June '06 - 04:05

That technote is almost a year old and brings nothing new to the table. All it describes is some very basic debug-via-printf which is really pretty horrible, and was of course possible (and I was doing it) when I wrote the rant. Apple’s unreleased Dashcode looks like it will be the answer to many of my complaints (although the complaints about having to do everything in HTML/CSS/JS and being forced to do a lot of custom controls etc. still stand) once it finally comes out.

**Mike Ash** - 16 June '06 - 13:23

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

No comments have been posted.

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.
