---
title: GenericToolbar and IB3
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2007/12/GenericToolbar-and-IB3/'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:a0da3dca008c84ab'
translated: false
---

> 原文：[GenericToolbar and IB3](https://belkadan.com/blog/2007/12/GenericToolbar-and-IB3/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Performance Optimization: Why We Can't Use valueForKeyPath:](https://belkadan.com/blog/2007/10/Performance-Optimization-Why-We-Cannot-Use-valueForKeyPath/)

[NSNumber, CFNumber, and CFBoolean](https://belkadan.com/blog/2008/01/NSNumber-CFNumber-and-CFBoolean/) »

« [GenericToolbar Icon](https://belkadan.com/blog/2007/06/GenericToolbar-Icon/?tag=generictoolbar)

## [GenericToolbar and IB3](#)

About a month and a half ago I got an e-mail from a GenericToolbar user telling me that GenericToolbar didn’t work with Leopard, or more specifically with IB3. The nib file reported a missing plugin and then wouldn’t load because the GenericToolbar class couldn’t be found.

Interface Builder 3 does not use IB2 palettes.

At this time I actually did not have Leopard myself, developer preview or otherwise. As such I wasn’t able to do anything at the time. When I actually did get Leopard, however, I set to work on the problem immediately (after making sure my most mainstream app, Webmailer, still worked).

Initial triage showed that my original plan would not work; I had intended to make GenericToolbar into a sort of compatibility patch for IB2 to read IB3 toolbars, but the entire nib file format changed. So that was out.

What _did_ have to happen, though, was a way for all those people who had used GenericToolbar in the past to open their nib files, even if it was _just to delete the toolbar_. (Of course, that’s not what I was aiming for.) Sure, I could say “reinstall Xcode 2”, but what kind of developer would respect that?

So as of two days ago, the GenericToolbar Converter for IB3 has been released, and GenericToolbar has effectively been retired. The converter is an IB3 plugin that essentially loads IB2 GenericToolbar nibs as if they were using IB3 toolbars. GenericToolbar had slightly more capabilities than IB3 toolbars, so a few things are lost, and there are a few options the user can choose from for _how_ the import actually works.

When I say GenericToolbar has been “retired”, I mean that while it is still supported (both the converter and the IB2 palette), I don’t plan to add any more features, nor add full support for GenericToolbar in IB3. Apple did a nice enough job as it is, and there’s still IB2 around if you need it.

Of course…IB3 toolbars still aren’t supported on older versions of OS X. So there may still be a GenericToolbar revived for IB3…if there’s enough interest.

---

As for the rest of the Belkadan product family, I’m in reasonably good shape. Webmailer is good to go, and works just as well as it did in Tiger. (It’s a pretty simple app, so I’m not surprised.) The elusive PHP/CC project is on hold for now; it’s having some problems loading into Xcode 3. I’m going to try to keep that compatible with Xcode 2 as well.

And Dockyard, supposedly the flagship product of Belkadan Software is—still not ready for Leopard. Third-party menu extras were broken once again on Leopard; I can only hope that the Unsanity folks can get MEE up and running soon. But Dockyard Manager still works. Rather, it still runs. But it doesn’t play nicely with Spaces, not at _all_…since the Spaces preferences are stored with the rest of the Dock preferences. (It would have been nice if Apple had separated them like it did with the Dashboard prefs. Dashboard, by the way, is also run by the Dock, along with Cmd-Tab, Exposé, and good old minimized windows.) Some people consider this a feature (I actually got an e-mail saying as much), but when your old Spaces app-binding preferences don’t quite return when you switch back, it’s more of a bug than anything else.

So, I’m investigating alternate ways to change the items in the Dock, as well as giving the Dockyard interface a complete overhaul. For that reason a new version of Dockyard won’t be coming in the imminent future. But the near future, sure.

This entry was posted on [December](https://belkadan.com/blog/2007/12) 13, [2007](https://belkadan.com/blog/2007) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [GenericToolbar](https://belkadan.com/blog/tags/generictoolbar)
