---
title: 'What''s in a Button?'
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2025/11/Whats-in-a-Button/'
original_language: en
published: 2025-11-27
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:39df1790ddf7ff0f'
translated: false
---

> 原文：[What's in a Button?](https://belkadan.com/blog/2025/11/Whats-in-a-Button/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [SICPelago](https://belkadan.com/blog/2025/04/SICPelago/)

[YAML is (not) my preferred configuration format](https://belkadan.com/blog/2026/03/YAML-Is-Not-My-Preferred-Configuration-Format/) »

« [The Shell is a Program](https://belkadan.com/blog/2024/12/The-Shell-is-a-Program/?tag=user-experience)

« [Misleading Metrics and UX Tradeoffs](https://belkadan.com/blog/2018/04/Misleading-Metrics/?tag=rant)

## [What's in a Button?](#)

A while back I posted this spicily-phrased take:

> I appreciate that someone else understands that being a GUI has some basic requirements and “draws to the screen” is not the interesting one. The bar is about 20cm off the floor but everyone forgets to jump.

Despite mostly not working on GUIs in my career, I have strong opinions about consistency and about affordances for beginners and power users alike. So today, let’s take a simple case study: a button.more No one _really_ agrees these days on what a button should look like, but we can figure that out later. For now, we can take an icon and draw a border around it and that probably counts:

![](https://belkadan.com/blog/../logo)

A disclaimer: we’ll be working in HTML and CSS, and you can view the page source to see how I did each of the examples, but I’m not trying to make the best HTML or CSS here. Instead, I’m trying to demonstrate how someone might try to build a UI element from scratch, in or out of a browser. (It’s up to you to judge how successful I am.)

Buttons are specifically UI elements that do things, so let’s add an action when you click it:

![](https://belkadan.com/blog/../logo)

Perfect! We’re basically done, right?

(Note to voice control users: for this article I have specifically hidden the first several examples from readers/tools (that's what aria-hidden="true" is for) so you don’t have to wade through iterations of the same boring thing. It’s just bringing up a dialog. Unfortunately, when we get to the point of talking about focused elements you’ll start hearing some incomplete descriptions.)

### There are lots of ways to submit an action

I implemented this using an event called “mouse down”. What if you’re on a phone? In that case we care about touch events instead, right?

![](https://belkadan.com/blog/../logo)

Oops! Phone browsers try to adapt for desktop-only sites—they’ll actually translate a tap to “mouse down”. On iOS Safari, this new version actually shows _two_ dialogs. This wasn’t intentional: it’s a consequence of me testing the “mouse _up”_ event, which _doesn’t_ (usually?) get translated the same way, but then using “mouse down” in the final version of the blog post and not re-testing before I published. (Thanks to @guenther@chaos.social for pointing this out.)

But really “mouse down” is the wrong event to begin with. Users sometimes misclick, and so OSs back to [System 1.0 for the Mac](https://infinitemac.org/1984/System%201.0) (possibly even earlier) have a feature called _drag cancellation_ or _pointer cancellation,_ where if you drag away from the button before letting go of the click/tap, it doesn’t fire. This behavior can’t be provided with only one of “mouse down on my UI element” and “mouse up on my UI element”; you need both, or some higher-level operation.[1](#fn:cancellation)

To be fair I had to go a little out of my way to do this section, for demonstration purposes. Modern web browsers pack up everything we’ve been talking about in a single “click” event that handles both clicks and taps as well as drag-cancellation. But if you’re trying to make a button from scratch _outside_ of a web browser, you might have made this mistake.

![](https://belkadan.com/blog/../logo)

### Keyboard navigation

Some people don’t use a mouse—whether to keep their hands efficiently on the keyboard, or because they don’t have the manual dexterity to use pointing devices, or both, or some other reason. To facilitate this, desktop OSs let you tab between all the interactable items in a window—not just form fields, but _everything_ you might need to interact with. (These days it’s often tucked away in a setting called “Full keyboard access” or something, but sometimes even without hunting for that you might be able to get it to work with Option-Tab or Ctrl-Tab. Adding Shift goes backwards.) Our button should support this.

![In Safari, this is described as "Press Tab to highlight each item on a web page", option Option-Tab as the fallback when not enabled.](https://belkadan.com/blog/2025/11/Whats-in-a-Button/safari-full-keyboard-access.png)

![](https://belkadan.com/blog/../logo)

We also didn’t say anywhere to draw a ring when _focused_ (in fact, maybe your web browser doesn’t, but mine does). Let’s fix that by adding some explicit style information:

![](https://belkadan.com/blog/../logo)

Even here we’re still relying on the web browser to track this “focused” state for us; ultimately _someone_ has to know what UI element is focused, and which the “next” and “previous” elements should be.

While we’re here, let’s fix one more display issue from the previous section: buttons should show some feedback when you start to press them, to go with the drag-cancellation feature and also so you can tell that the click happened at all. We’re again going to lean on the web browser for this _active_ or _highlighted_ state, but it really does make the experience much better.

![](https://belkadan.com/blog/../logo)

### Voice control

Some people don’t use a mouse _or_ keyboard to control their computers. Instead, they use voice recognition programs that can translate commands into UI actions. For yet another time, the web browser assists us here: if you can manage to select one of the “focusable” button above, you can activate it.

However, voice control is often paired with screen reading: a navigation for people who can’t use a display (usually because of visual impairment, but I have on a handful of occasions used it to work with a computer I had no monitor for). There are a number of ways interactable UI elements show up there, but in this case let’s just see what happens when the user focuses the button (using keyboard navigation, or a scroll wheel, or something):

Oh dear. We used an icon with no [alt text](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#authoring_meaningful_alternate_descriptions), so the user has no idea what this button does. This is more about _images_ than about _buttons_ specifically, but even with a text button you may still want your screen-reader label / “accessibility label” to be different from the displayed text, since the user may not have the same contextual information when they navigate to it.

![Surprise Button (8 of 11)](https://belkadan.com/blog/../logo)

Okay, fixed. Ish. Again, web browsers are helping out a lot here; every OS has a different accessibility interface, and every GUI toolkit has to plug into it. Or not, and frustrate users.

### Key Equivalents

We’re finally approaching something that behaves like a button from 1990. It’s still not very pretty, but most of the changes we’ve been making have been to things other than appearance. Here’s one more: did you know many buttons on your system have keyboard shortcuts, just like menu items? On Windows these are usually Alt-something; on a Mac they’re Cmd-something like menu items. (Most of the time this only matters for dialog boxes; the rest of the time most buttons have equivalent menu items anyway.)

This is less common in web pages in general. It’s not even that common in general, beyond standard shortcuts of Return for default actions, Escape for Cancel, and maybe Cmd-Delete for “confirm remove”. But we’ll add it here anyway: if you’re a power user, this button can now be pressed with Ctrl-B, or perhaps Ctrl-Option-B, or maybe Alt-Shift-B, or… ([It depends on your browser and OS](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/accesskey), and the chart doesn’t even seem to be up to date.)

![Surprise Button (9 of 11)](https://belkadan.com/blog/../logo)

### Consistency

Even with all this, we _still_ don’t have something that behaves like a normal button. It doesn’t “highlight” when pressing Space, because I didn’t explicitly write code for it. VoiceOver, the macOS screenreader, calls it a “group” or “image” rather than a button. It doesn’t support a “disabled” state.

It turns out this has been the wrong approach from the start, at least for an application or web page. We don’t need to do any of this. We can start with a system-provided button:

ignoring the accesskey this time so it's not duplicated

And then customize it to do our own drawing.

ignoring the accesskey this time so it's not duplicated

It’s still a chunk of the work we had before, but _now_ we and the web browser agree that it’s a button, and we get most of what we discussed for free. As well as anything else I forgot in making this blog post.

### Conclusion

All that for a button. Lists, sliders, and tables are more complicated, and text editing is so complicated that even a number of apps that otherwise roll their own UI (usually games) still use the system text input.

The general moral here is that we, as an industry, have had _40 years_ to establish what desktop GUIs are like, over 30 to establish what web pages are like, and nearly 20 to establish what mobile GUIs are like. Not every tradition is good, but if you’re a sighted mouse-user, you might not even know what you’re omitting when you diverge from conventions. Which translates to people being frustrated with your app or web page, or in the worst case not being able to use it at all.

If you’re an app developer, the lesson is simple: if you want to customize a UI element, start with a standard one and change how it draws, rather than building one up from scratch and trying to match the system in every little way. If you are a GUI library author, things might be trickier. You’re _trying_ to rebuild things, and there’s a good chance you _do_ know more than me about GUIs. But please at least consider if it’s going to work with a screenreader.

P.S. Let this not discourage _exploration,_ taking apart existing UI elements and building new ones to see how they work. I just want people to stop thinking “works for me” is good enough.

1. Is this useful? Video game controllers don’t have an equivalent; actions happen when you press the button down. But video games don’t usually have you select things from the entirety of a screen; instead, you’re either choosing from a list or table with directional inputs, or the choice of button _is_ the decision. And even then there’s often a confirmation step, more than there is with non-game computer programs—though that could also be due to desktop and mobile apps usually having an “undo” feature as well. [↩︎](#fnref:cancellation)

This entry was posted on [November](https://belkadan.com/blog/2025/11) 27, [2025](https://belkadan.com/blog/2025) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [User experience](https://belkadan.com/blog/tags/user-experience), [Rant](https://belkadan.com/blog/tags/rant)
