---
title: Xcode Plugins
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/xcode-plugins/'
original_language: en
published: 2014-04-14
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:1c750e056a1daadc'
translated: false
---

> 原文：[Xcode Plugins](https://nshipster.com/xcode-plugins/)　·　NSHipster (Mattt)

# [Xcode Plugins](https://nshipster.com/xcode-plugins/)

Written by  [Mattt](https://nshipster.com/authors/mattt/)  March 25^th, 2019 ([revised](https://github.com/nshipster/articles/commits/master/2014-04-14-xcode-plugins.md))

Apple is nothing if not consistent. From [Pentalobular screws](https://en.wikipedia.org/wiki/Pentalobe_screw) to [Sandboxing](https://developer.apple.com/app-sandboxing/), customers are simply expected to relinquish a fair amount of control when they choose to buy a Mac or iPhone. Whether these design decisions are made to ensure a good user experience, or this control is exercised as an end in itself is debatable, but the reality is that in both hardware and software, Apple prefers an ivory tower to a bazaar.

No better example of this can be found with Xcode: the very software that software developers use to build software for the walled ecosystems of iOS & OS X software, _is itself a closed ecosystem_.

Indeed, significant progress has been made in recent years to break open the developer workflow, from alternative IDEs like [AppCode](http://www.jetbrains.com/objc/?utm_source=nshipster) to build tools like [CocoaPods](http://cocoapods.org), [xctool](https://nshipster.com/xctool/) and [nomad](http://nomad-cli.com). However, the notion that Xcode itself could be customized and extended by mere mortals is extremely recent, and just now starting to pick up steam.

Xcode has had a plugin architecture going back to when Interface Builder was its own separate app. However, this system was relatively obscure, undocumented, and not widely used by third parties. Despite this, developers like [Delisa Mason](https://twitter.com/kattrali) and [Marin Usalj](https://twitter.com/_supermarin) have done incredible work creating a stable and vibrant ecosystem of third-party Xcode extensions.

**Simply install [Alcatraz](http://alcatraz.io), and pull down all of the plugins (and color schemes and templates) that you desire.**

This week on NSHipster: a roundup of some of the most useful and exciting plugins for Xcode—ready for you to try out yourself today!

> And since these question come up every time there’s an article with pictures:
> 
> 1. The color scheme is [Tomorrow Night](https://github.com/ChrisKempson/Tomorrow-Theme)
> 2. The app used to make animated GIFs is [LICEcap](http://www.cockos.com/licecap/)

---

## Making Xcode More Like `X`

Just as New York became a melting pot of cultures from immigrants arriving at [Ellis Island](https://en.wikipedia.org/wiki/Ellis_Island), Xcode has welcomed the tired, poor, huddled masses of developers from every platform and language imaginable. Like those first wave Americans, who settled into their respective ethnic neighborhoods to re-establish their traditions in a new land, so too have new iOS developers brought over their preferred workflows and keybindings.

Perhaps you would appreciate a taste of home in the land of Cupertino.

### Vim

Finding it _too easy_ to quit Xcode? Try [XVim](https://github.com/JugglerShu/XVim), an experimental plugin that adds all of your favorite Vim keybindings.

### SublimeText

![SCXcodeMiniMap](https://nshipster.com/assets/scxcodeminimap-49147de0dfe87923deb13e3acafd2ab749cddb3aa323dceb59f1fd3cc81379e7d25d6b1140cc1d297a15691de79c934027c153f21d498dfd7c5624fb5fef6f92.png)

Do you miss having a code minimap along the right gutter of your editor to put things into perspective? Install [SCXcodeMiniMap](https://github.com/stefanceriu/SCXcodeMiniMap) and never again miss the tree nodes for the forest.

### Atom

![Show in GitHub](https://nshipster.com/assets/showingithub-182f71a469f1de22928c67986622756719bb35c09837319e448f6f3d5ba08a2f3df0d623182c33ee7e534207af373f188069b7defb153a9817a4990e0a683732.png)

Looking to be more in tune with GitHub? Add the [Show in GitHub / BitBucket](https://github.com/larsxschneider/ShowInGitHub) plugin to open to the selected lines of a file online.

## Fixing Xcode

Rather than waiting with crossed fingers and clenched teeth each June, as Apple engineers unveil the next version of Xcode, developers now have the ability to tailor the de facto editor to their particular needs (and most importantly, fix what’s broken).

### Add Line Breaks to Issue Navigator

![BBUFullIssueNavigator](https://nshipster.com/assets/bbufullissuenavigator-0495b0aba8e5c285ef716c8576d8d68a8ae73d6782b781321410bef2c6f20966100a2e57e5d3d08d3a74770482769cb61e1fb990fb84a47d1da8c0889d18c06b.png)

An annoyance going back to Xcode 4 has been the truncation of items in the Issues Navigator. Never again be frustrated by surprise ellipses when compiler warnings were just starting to get interesting, with [BBUFullIssueNavigator](https://github.com/neonichu/BBUFullIssueNavigator).

### Dismiss Debugging Console When Typing

![BBUDebuggerTuckAway](https://nshipster.com/assets/bbudebuggertuckaway-2d850345e1771741c4c93c0738c47e683246a7baf18717b02504e110f6de550ba315cf8c9220e19aeba9d166c8fd6462216887ff1e3c9934778960c39ca88945.gif)

Another annoyance going back to Xcode 4 is how the debugging console seems to always get in the way. No more, with [BBUDebuggerTuckAway](https://github.com/neonichu/BBUDebuggerTuckAway). As soon as you start typing in the editor, the debugging window will get out of your way.

### Add ANSI Color Support to Debugging Console

![XcodeColors](https://nshipster.com/assets/xcodecolors-551297eb3e288dd4b4e31ac8660938bd45781bd7d69d400d149512731bf169f9cae2ddb01cca28067783ea3bf4b6049c287e54c0113f3c97d640b90698b78189.png)

`ncurses` enthusiasts will no doubt be excited by the [XcodeColors](https://github.com/robbiehanson/XcodeColors) plugin, which adds support for ANSI colors to appear in the debugging console.

### Hide `@property` Methods in Source Navigator

Finding that `@property` synthesizers are creating a low signal-to-noise ratio in the Source Navigator? Let [Xprop](https://github.com/shpakovski/Xprop) excise the cruft, and let the functions and methods shine through.

### Blow Away DerivedData Folder

[Xcode texting you again?](http://www.textfromxcode.com) `rm -rf`-ing the heck out of “Library/Developer/Xcode/DerivedData” does the trick every time, 90% of the time. Add a convenient button to your Xcode window to do this for you, with the [DerivedData Exterminator](https://github.com/kattrali/deriveddata-exterminator).

## Turbocharging Xcode

Not being the most verbose language in existence, Objective-C can use all the help it can get when it comes to autocompletion. Xcode does a lot of heavy lifting when it comes to class and method completion, but these plugins extend it even further:

### Autocomplete `switch` Statements

![SCXcodeSwitchExpander](https://nshipster.com/assets/scxcodeswitchexpander-29c024a656503ebda519bdf87e6e5315c461ce9aa66d87b06749ce623f3284f7e9552448e25e344100bc93a067d07698f0bfa31a2699b8488a79772aa4117460.gif)

Fact: `switch` statements and [`NS_ENUM`](https://nshipster.com/ns_enum-ns_options/) go together like [mango and sweet sticky rice](http://www.thaitable.com/thai/recipe/mango-on-sticky-rice). The only way it could be improved would be with [SCXcodeSwitchExpander](https://github.com/stefanceriu/SCXcodeSwitchExpander) with automagically fills out a `case` statement for each value in the enumeration.

### Autocomplete Documentation

![VVDocumenter](https://nshipster.com/assets/vvdocumenter-937068617dc5891217afe6cb643decd9ed7c2797b2ccfbee32383e3110b953a1c764210beb4a9cb85298bd413d641234f886da2d9544553496608737b4844417.gif)

[Documentation](https://nshipster.com/documentation/) adds a great deal of value to a code base, but it’s a tough habit to cultivate. The [VVDocumenter-Xcode](https://github.com/onevcat/VVDocumenter-Xcode) plugin does a great deal to reduce the amount of work necessary to add [appledoc](http://gentlebytes.com/appledoc/)-compatible header documentation. Install it and wrap your code in a loving lexical embrace.

## Formatting Xcode

[“Code organization is a matter of hygiene”](https://nshipster.com/pragma/), so you owe it to yourself and your team to keep whitespace consistent in your code base. Make it easier on yourself by automating the process with these plugins.

### Code Formatting with ClangFormat

[ClangFormat-Xcode](https://github.com/travisjeffery/ClangFormat-Xcode) is a convenient wrapper around the [ClangFormat](http://clang.llvm.org/docs/ClangFormat.html) tool, which automatically formats whitespace according to a specified set of style guidelines. Eliminate begrudging formatting commits forever with this plugin.

### Statement Alignment

![XAlign](https://nshipster.com/assets/xalign-42614b0113c7b43acb51f69353b68a4f6e8dbeed0e7d752fcbf4442a89204c1ecea1a9f37ded0f6e178b2ce9dd7869a8a7a3230cedd591b66048074c062e45d4.gif)

Fancy yourself a code designer, automated formatters be damned? [XAlign](https://github.com/qfish/XAlign) automatically aligns assignments _just so_, to appease your most egregious OCD tendencies.

## Extending Xcode

In a similar vein to what [Bret Victor writes about Learnable Programming](http://worrydream.com/LearnableProgramming/), these plugins push the boundaries of what we should expect from our editors, adding context and understanding to code without obscuring the meaning.

### Inspect `NSColor` / `UIColor` Instances

![ColorSense](https://nshipster.com/assets/colorsense-ab72ab6b7a29aa8467d0becdd73d5760bd8ade562c86c65f768b90dff0beb9587aceecf47af33e9a958c96f0ab26b152b889962d8e001ad7b8fc5802417b0150.png)

Telling what a color is from its RGB values alone is a hard-won skill, so faced with an `NSColor` or `UIColor` value, we have little recourse to know what it’ll look like until the code is built and run. Enter [ColorSense for Xcode](https://github.com/omz/ColorSense-for-Xcode)

Quoth the README:

> When you put the caret on one of your colors, it automatically shows the actual color as an overlay, and you can even adjust it on-the-fly with the standard OS X color picker.

### Autocomplete Images from Project Bundle

![KSImageNamed](https://nshipster.com/assets/ksimagenamed-1518215ca0bac470ab70a7498cab74f268541d3c5ab983560e580305e267fa90c58261f2e2d33086d78619616ea504285279febc2291a0e043bdcab9decf05cf.gif)

Similar to the ColorSense plugin, [KSImageNamed](https://github.com/ksuther/KSImageNamed-Xcode) will preview and autocomplete images in `[UIImage imageNamed:]` declarations.

### Semantics Highlighting

![Polychromatic](https://nshipster.com/assets/polychromatic-2a32a0bdade8fb6c8286b94f99b5def6101c4eed9bef76de7e61068782a613816c6029bedee8044d148e6a36fa5e88b1c9d67cedbfb59baddb1a0a0d7200f14d.png)

Any editor worth its salt is expected to have some form of syntax highlighting. But [this recent post by Evan Brooks](https://medium.com/p/3a6db2743a1e) presents the idea of _semantic_ highlighting in editors. The idea is that each variable within a scope would be assigned a particular color, which would be consistent across references. This way, one could easily tell the difference between two instance variables in the same method.

[Polychromatic](https://github.com/kolinkrewinkel/Polychromatic) is a fascinating initial implementation of this for Xcode, and worth a look. The one downside is that this plugin requires the use of special desaturated color schemes—something that may be addressed in a future release, should this idea of semantic highlighting start to pick up mind share.

### Localization

![Lin](https://nshipster.com/assets/lin-1-e94e6d23a6b083a9b2b5ace9731e17aa660d7dd41b8d1dcb6de3f880486ea06756294f70d9e912a2f704ba1e5c10a079a6a2a10f6f2e80640355ae3f34ee4fe3.png)

![Lin](https://nshipster.com/assets/lin-2-17c1b4494eece8767c1c7d51d6fe34a0322f51456bece51fc7d484ae0c8f8c2fdf2f1654864c9d8de4e2610eb8b6a52d475e82593b96764b0b61388ec9218931.png)

It’s no secret that NSHipster has [a soft spot for localization](https://nshipster.com/nslocalizedstring/). For this reason, this publication is emphatic in its recommendation of [Lin](https://github.com/questbeat/Lin-Xcode5), a clever Xcode plugin that brings the localization editor to your code.

---

Xcode’s plugin architecture is based on a number of private frameworks specific to Xcode, including DVTKit & IDEKit. A [complete list](https://github.com/luisobo/Xcode5-RuntimeHeaders) can be derived by running [`class-dump`](http://stevenygard.com/projects/class-dump/) on the Xcode app bundle.

> Using private frameworks would be, of course, verboten on the AppStore, but since plugins aren’t distributed through these channels, developers are welcome to use whatever they want, however they want to.

To get started on your own plugin, download the [Xcode5 Plugin Template](https://github.com/kattrali/Xcode5-Plugin-Template), using the other available plugins and class-dump’d headers as a guide for what can be done, and how to do it.
