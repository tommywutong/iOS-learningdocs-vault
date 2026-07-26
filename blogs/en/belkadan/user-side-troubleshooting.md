---
title: User-Side Troubleshooting
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2011/05/User-Side-Troubleshooting/'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:7f29c0cf95bf0cee'
translated: false
---

> 原文：[User-Side Troubleshooting](https://belkadan.com/blog/2011/05/User-Side-Troubleshooting/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Auspicious Continuation](https://belkadan.com/blog/2011/05/Auspicious-Continuation/)

[Chrome vs. Safari](https://belkadan.com/blog/2011/06/Chrome-vs-Safari/) »

« [Garbage Collectors and Stack Drawers](https://belkadan.com/blog/2009/06/Garbage-Collectors-and-Stack-Drawers/?tag=mac-os-x)

[Chrome vs. Safari](https://belkadan.com/blog/2011/06/Chrome-vs-Safari/?tag=mac-os-x) »

## [User-Side Troubleshooting](#)

The other day one of my friends called me with a puzzling problem: her MacBook would start up, she could log in, and…that was about it. Running any programs resulted in a quick quit, including the Finder. The repair person she was talking to said that if it was a hardware problem, it’d be covered and they could do it for free…but software she’d have to pay. And they said it was software. She decided that it’d be easier to just do an Archive & Install and start fresh than pay them, which was a good decision IMO. (She’s not particularly tech-savvy, but she could certainly do a reinstall and get things working.) But she asked me to look at it first.

She logged in, and I saw what she meant. Finder would start up and show its menus across the top, but as soon as I opened a window it would crash. System Preferences showed its usual array of preference panes, but trying to open one caused a crash.more

iCal, inexplicably, seemed to work, or at least open cleanly. But that wasn’t much help.

Thinking cleverly, I used Spotlight to open up Terminal, quickly looked up how to start file sharing from the command line (`sudo AppleFileServer`), and then tried to connect from my own laptop. Thankfully, the AirPort menu still worked and we were able to get on the same network, though I guess we could have used straight Ethernet if necessary. I was relieved when it all worked and I opened up her home folder in _my_ Finder.

At this point we could have backed up anything to my external, but with a couple dozen gigabytes of data on her computer I was still trying to find the cause of her problems. So I opened up the crash logs for the apps I had tried to open in the last few minutes: Finder and System Preferences.

(begin programmer jargon here)

Every crash was in `CFRelease`, i.e. something was being overfreed, or some non-object was being freed. My mind jumped the wrong way at first: “the only way `CFRelease` can break is if there’s a new plug-in or something loaded into every process!”

Nope. Looking at the list of loaded libraries at the bottom of the crash log showed nothing suspicious. The few non-Apple libraries were mostly ones I’d used myself like Dropbox. (Yes, Dropbox puts itself in _every_ process to give you that nice menu in the Finder. Here’s a case for SIMBL?[1](#fn:simbl)) So that was a red herring. Going back to the logs, I noticed something more important: every single crash came from a call to `SetDefaultLocaleString`, with a common call stack for about two or three frames past that.

Localization settings are stored in the global preferences domain (terminology from `NSUserDefaults`, etc), which most people don’t even know how to edit. Maybe there’s a clue there.

(end programmer jargon here)

Okay, so it’s a problem with her localization settings? Maybe. I happen to know that localization settings are stored in a hidden file called `.GlobalPreferences.plist`, buried in a user’s Preferences folder. But no, the locale was `en_US`, i.e. US English. What could be the problem, then?

Okay, well. Searching online for `SetDefaultLocaleString` didn’t give me anything useful, so I had to backtrack a little. _Was_ this a user settings problem? To find out, we tried logging in to another user account.[2](#fn:acct)

It worked. !

Okay, so that narrowed things down a fair amount. It’s now definitely a user-specific issue, and because of that we need to find out what the differences between the two users are. I start a brute-force comparison of _all_ preference files using FileMerge, an old and mildly kludgy tool that comes (came?) with Xcode, with the intent to move the comparison to entire Library folders if necessary. Keeping in mind that we’re doing this on _my_ computer, over WiFi…it’s going to take a while.

I can’t forget those crash logs, though…there has to be something to do with locales.

Eventually the comparison finishes and I open up the list of preferences. Most of them I can ignore – almost anything that’s application-specific can’t be causing this. I come back to the `.GlobalPreferences.plist` files, which are of course different, and open them up.

Curses – property list files aren’t stored in text format anymore! Okay, a manual comparison it is. Let’s fire up Property List Editor…

Well. As I saw before, the current locale, `AppleLocale`, was fine. But my friend’s list of preferred languages, what you edit in the “Language & Text” preference pane, was empty. The `AppleLanguages` key was still there, but it had no items in it. So I tried copying _my_ language preferences into her preferences file. Couldn’t hurt, right?

And it worked. Perfectly. (I think we logged out and back in first.) She was very happy.

I haven’t filed a bug report with Apple because I can’t reproduce it on my own computer, possibly because of the default setting in the computer-wide preferences (`/Library/Preferences`). (Not sure if hers was intact or not.) But moreover, I can’t think of how this would happen. Presumably some ill-behaved installer was trying to snoop or mess with her language settings, and managed to screw up the file in the process. I’m guessing I never come across this again.

---

What’s interesting here isn’t so much the very strange bug as the steps I took to troubleshoot it. Sure, there was some [xkcd tech support](http://xkcd.com/627/) here, but there was also two things that the average person wouldn’t be able to do:

- read a crash log
- means and where the associated preferences would be stored

In this case, being not just a programmer but a Mac developer helped me solve the problem; this knowledge is not quite Googleable. It’s worth noting that this is usually _not_ the case when I “fix someone’s computer” – programming skills and computer science theory have little to do with troubleshooting and actually using computers.[3](#fn:brian) But this is a case that I would be able to solve and other “tech-savvy” people, including my fellow CS students, might not, simply because they don’t have the Mac domain knowledge.

Still, my friend could have just created a new user account and that would have solved the problem. Add “try another account” to the toolbox of “standard troubleshooting techniques for non-tech-savvy users”.

For me, though, this kind of thing is fun. It’s a puzzle, which I have to solve. And I was glad to help, glad to be of service.

1. [SIMBL](http://www.culater.net/software/SIMBL/SIMBL.php) is a little hidden which loads bundles into targeted applications at run-time, and it’s also what lets [Keystone](http://belkadan.com/keystone) work at all. This is of course a _huge_ security risk, and you should never install random SIMBL bundles, but it’s also very handy for adding functionality to an existing program without affecting every other program on the system. [↩︎](#fnref:simbl)
2. I’m glad there _was_ another user account, because I’d guess that adding a new OS X user from the command line is a bit harder than starting file sharing or configuring the network. [↩︎](#fnref:acct)
3. One of my CS professor’s catchphrases was “I hate computers”. [↩︎](#fnref:brian)

This entry was posted on [May](https://belkadan.com/blog/2011/05) 31, [2011](https://belkadan.com/blog/2011) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Mac OS X](https://belkadan.com/blog/tags/mac-os-x)
