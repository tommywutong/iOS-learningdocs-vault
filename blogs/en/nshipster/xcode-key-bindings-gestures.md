---
title: 'Xcode Key Bindings & Gestures'
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/xcode-key-bindings-and-gestures/'
original_language: en
published: 2013-09-30
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:67a11166caaad7f2'
translated: false
---

> 原文：[Xcode Key Bindings & Gestures](https://nshipster.com/xcode-key-bindings-and-gestures/)　·　NSHipster (Mattt)

# [Xcode Key Bindings & Gestures](https://nshipster.com/xcode-key-bindings-and-gestures/)

Written by  [Mattt](https://nshipster.com/authors/mattt/)  September 30^th, 2013

The extent to which programming-as-craft is compared to manual disciplines like woodworking is tiresome. It’s absolutely the case that one should know and maintain their tools as well as a carpenter or metalsmith, but… I mean, c’mon. One would think that an industry demanding the skills of ninjas and rockstars would mix it up a little: “keep your shurikens polished, sharp, and hidden” or “tune your guitar and condition your hair twice daily”.

Here at NSHipster, the advice is simple and only slightly allegorical: “Xcode is your mustache, so keep it trimmed, waxed to a sharp point, and free of bugs.”

Anyway, a few weeks ago, we looked at how [Xcode Snippets](https://nshipster.com/xcode-snippets/) can make you more productive by reducing the amount of boilerplate code you have to type out. This week, we’re going to pick up on that thread and cover the essential key bindings and gestures.

Xcode key bindings and gestures not only shave off seconds of precious work, but make you look more confident, competent, and cromulent in the process. Learn the following tricks of the trade and join the elite set of Xcode power users.

---

> For your reference, here is a legend of the common modifier key symbols (as well as a symbol for click [shamelessly borrowed from the International Phonetic Alphabet](https://en.wikipedia.org/wiki/Click_consonant)):

| Command | Control | Option | Shift | Click |
|---|---|---|---|---|
| `⌘` | `⌃` | `⌥` | `⇧` | `ʘ` |

## Open Quickly (`⇧⌘O`)

![Open Quickly](https://nshipster.com/assets/xcode-shortcuts-quick-open-31210595d03fa40bb28184d5487850d7be3ab2429e7ca08326fe1ac10e6c554306f61e67547ba9256d48ffde2264bb512ea28b67e62db5e19530f2ed50021e29.png)

Learn to rely less on the Project Navigator by learning to love Open Quickly. There’s a lot to love, too—with support for partial case- and position-insensitive matches, Xcode does a great job of finding what you want with just a minimal amount of input on your part.

---

## Quick Documentation (`⌥ʘ` on Symbol / Three-Finger Tap)   
 Open Documentation (`⌥ʘʘ` on Symbol)

![Quick Documentation](https://nshipster.com/assets/xcode-shortcuts-quick-documentation-1f574c95af3fd7ea5946173b934331705eeddcfc9a860e594ea4b1655a84534f03b69b33c02414e7bfae301b70f4b8be140756756d1397051aedb5cf49edc7a2.gif)

Quick Documentation is probably the first Xcode shortcut developers should learn. Just alt-click (or three-finger tap) any class, variable, or constant value, and Xcode will give you a quick rundown of what you’re looking at. Alt-double-click to bring up the documentation window, opened to the relevant entry.

## Jump to Definition (`⌘ʘ` on Symbol)

Also well-know to an expert Xcoder’s workflow is Jump to Definition, which opens the editor window to the relevant `@interface` definition or constant declaration in a `.h` file. This is especially useful for getting a raw look at system frameworks like Foundation, to get an idea of what’s _really_ going on behind-the-scenes.

## Jump to Next Counterpart (`^⌘↑` / `^⌘↓` / Three-Finger Vertical Swipe)

![Jump to Next Counterpart](https://nshipster.com/assets/xcode-shortcuts-counterpart-0dad81b700200c8ec69ea351f2ffa8ba921f6eff195ae4b22f2eba8e9866dd291a0a87d7f5bcae7376e4f5d02de2028e5b702be2d5b4fb075c6df6a315474dc6.gif)

Last, but certainly not least, there’s Jump to Next Counterpart, which is very likely the shortcut used the most on any given day. Quickly switch between a `.h` header and it’s corresponding `.m` implementation with a simple three-finger swipe up or down (or `^⌘↑` / `^⌘↓` if you feel so inclined).

---

## Comment Selection / Current Line (`⌘/`)

![Comment Selection](https://nshipster.com/assets/xcode-shortcuts-comment-d9ecad7d9d8848452f9cdd1ed52f614af9bdd1d1a9206057e6d0f08e5ce8c2cb4bbd361d8645273c049a95d192cff8f86f2ce2e92e5ca7f71b3e1fbef6d08541.gif)

Sure, you _could_ be debugging the “right way” by setting breakpoints and being clever with your code paths, but there’s quite so refreshingly simple and powerful as phasing code in and out of computational existence with a comment. Add or remove `//` comments to the current line or selection.

## Show Standard Editor (`⌘↵`)   
 Show Assistant Editor (`⌥⌘↵`)   
 Show Version Editor (`⌥⇧⌘↵`)

![Editors](https://nshipster.com/assets/xcode-shortcuts-editors-f9659d7f89d2896f59ddea52fccf32775fdf1cb7a01fedd86376dd8e277188b25af6b044dbc5222712b573244d039531cf5f8204cbb175d7694e99f4ee6b908e.gif)

For how useful the Assistant Editor can be, surprisingly few developers can actually remember the key combo to turn it on and off. But now with `⌘↵` and `⌥⌘↵` fresh in your mind, you’ll be helping Xcode help yourself more often.

![Assistant Editor Position](https://nshipster.com/assets/xcode-shortcuts-assistant-editor-position-0b008203b279eb2a88341f2cb34525b5f80a7447b6d7bf372b5cb04f0335877af94ee2c749f0b15484195eb764abf83df3e3bfa8f995aaf791e38b6d90c117c4.png)

As an aside, if you’re not big on how editors are stacking, a different horizontal or vertical arrangement can be chosen in View \> Assistant Editor.

---

![Panels](https://nshipster.com/assets/xcode-shortcuts-panels-db94a508cfd1267361a72af9dcab1d61abe457794c79e37830ad2df62c6b5034d9d84bae46183300b5a48726ffb707045afed3eac99bb5c06d1b6e0433bddbfd.gif)

Sandwiching the editors on the left and right flanks, the Navigator and Utilities panels encircle your code in their loving embrace. Learning how to get them to show what’s useful and GTFO when needed are critical for inner peace and maximum productivity.

## Show/Hide Navigator Panel (`⌘0`)

## Select Navigator (`⌘1, ..., ⌘8`)

1. Project Navigator
2. Symbol Navigator
3. Find Navigator
4. Issue Navigator
5. Test Navigator
6. Debug Navigator
7. Breakpoint Navigator
8. Log Navigator

## Show/Hide Utilities Panel (`⌥⌘0`)

## Select Utilities Panel (`⌥⌘1, ⌥⌘2, ...`)

### Source File

1. File Inspector
2. Quick Help

### Interface Builder

1. File Inspector
2. Quick Help
3. Identity Inspector
4. Attributes Inspector
5. Size Inspector
6. Connections Inspector

## Show / Hide Debug Area (`⇧⌘Y`)   
 Activate Console (`⇧⌘C`)

![Show / Hide Debug Area](https://nshipster.com/assets/xcode-shortcuts-debug-area-cadeaf82c3ec3758dac8805cb63f9ae8b8c5f427dd7c80bb75be60c9a4b413a487783d05bed1c44d438ac33341645abfb88655c4035d59b6da7e177bb9966c38.gif)

Anyone miss the option in Xcode 3 to have a detached debugger window? Yeah, me too.

Knowing how to toggle the debug area and activate the console in a single keystroke may be a shallow consolation, but it does help take the edge off of the pain or loss.

---

## Find (`⌘F`) /  
 Find & Replace (`⌥⌘F`) /  
 Find in Project (`⇧⌘F`) /  
 Find & Replace in Project (`⌥⇧⌘F`)

![Find](https://nshipster.com/assets/xcode-shortcuts-find-60a32c81ec23f7b78f1197272dd0ba115adad1b85204291beed8454665a560ebd039953b1fbc80163142a0edeb004b4a6550ccc6e5ce961a39f0b68f84162c29.gif)

For when Xcode’s refactoring capabilities come up short… which is to say: often. On the plus side, Xcode allows reference, definition, and regular expression search in addition to literal text.

## Spelling & Grammar (`⌘:`)

![Spelling & Grammar](https://nshipster.com/assets/xcode-shortcuts-spelling-and-grammar-2fded17d993f497b5316622ff38882fff487e7ab3057ebd0e119a6c25b5ad57c4157f0d923808230d689ac5178c569c5afb4051180cd3575da5b7d766394ff92.png)

All-powerful as Clang is, it still can’t help your nightmarish grammar and punctuation in your comments. Especially for anyone releasing code into the open-source wilds, do yourself a favor and give it a once-over with a built-in OS X spelling and grammar check.

---

![Xcode Shortcut Preferences](https://nshipster.com/assets/xcode-shortcuts-preferences-2ed9620ee3b592ddf8d5fe5b94c2951b6d76b4f34dc1443a354810cc2abe7eac8885e9f143d54ac6db3af47bfe3e5e1c23600a576ac963692dd02ee335e41a07.png)

But, of course, the fun doesn’t stop there! Like any respectable editor, Xcode allows you to customize the key bindings for every menu item and action across the app.

Here are a few non-standard key bindings that you might find useful:

- `^w`: Close Document (replaces Delete to Mark)
- `^⌘/`: Show / Hide Toolbar
- `^⌘F`: _None_ (removes Full Screen (at least until Mavericks))

Got any useful or clever bindings to share? Tweet them to [@NSHipster](https://twitter.com/NSHipster)!
