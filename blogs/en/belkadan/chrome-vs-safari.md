---
title: Chrome vs. Safari
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2011/06/Chrome-vs-Safari/'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:6f9afc822b6e5d64'
translated: false
---

> 原文：[Chrome vs. Safari](https://belkadan.com/blog/2011/06/Chrome-vs-Safari/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [User-Side Troubleshooting](https://belkadan.com/blog/2011/05/User-Side-Troubleshooting/)

[gdba](https://belkadan.com/blog/2011/06/Gdba/) »

« [User-Side Troubleshooting](https://belkadan.com/blog/2011/05/User-Side-Troubleshooting/?tag=mac-os-x)

[Priorities](https://belkadan.com/blog/2011/07/Priorities/?tag=mac-os-x) »

[Header Anchors: A Safari Extension](https://belkadan.com/blog/freebies/Header-Anchors/?tag=safari) »

## [Chrome vs. Safari](#)

_This was originally posted on my personal blog in December 2010. It’s still pretty much how I feel about Chrome._

Last week Google ran a program called [Chrome for a Cause](http://chrome.blogspot.com/search/label/chrome%20for%20a%20cause), in which Google donated money to charities based on how many tabs people opened in Chrome. The system was easily game-able, since it didn’t test whether you actually _used_ the tabs, but it was limited to million anyway, so Google was pretty much guaranteed to hit it.

The point of one of these things is, of course, to get more people to try using Chrome; knowing full well that that was the case, I decided to use Chrome for a week, and see how it stacks up to my regular browser, Safari.

First, a note on why I use Safari. Safari is the browser made by Apple, and the default browser on Mac OS X. I like it because it has very strong support for HTML5 and various experimental-y features of the web, and because it has a pretty solid and well-thought-out user interface. And it _feels_ like a Mac app, and integrates quite well with the rest of the system. (This last is precisely the reason why Safari on Windows sucks, or at least used to suck: it still feels like a Mac app, which is the wrong thing to do on a Windows system.)

The one thing Safari didn’t have until recently is extensions, and Safari’s extensions are still rather limited (both in capability and quantity) compared to Chrome’s or Firefox’s. The “feels like a real Mac app” kept me from switching to Firefox, though—the various attempts at faking Mac behavior made Firefox feel like a crippled application, despite any web browsing capabilities.

Chrome, on the other hand, is the newest major contender to the browser market (just over two years old), and I’d only tried it for a little bit a year ago. Like Safari, it’s based on the WebKit rendering engine, so it handles cutting-edge HTML5ed-up websites well. (Firefox’s Gecko engine is also pretty good, though.) In the last year, Chrome’s market share has surpassed Safari’s.

This comparison comes after using Chrome for a week, then switching back and using Safari for, well, most of a week.

#### Safari beats Chrome

- Tabs in the title bar. It’s ironic that the browser is called “Chrome” when one of the original stated goals is to _remove_ the “chrome” (browser interface elements) from your web browsing experience. It makes sense, actually, to have the tabs above the address bar, but while it does look cleaner with more browsing room, it’s just harder to drag the window around. And I’ve found I really like being able to double-click an empty part of the tab bar to make a new tab, but double-clicking a window’s title bar minimizes it, and Chrome is no exception. I’m torn, but ultimately I think I like the classic way better, even if it does take up more space.
- Preferences window. Chrome’s _actual_ preferences may be more customizable than Safari, but you’d have to dig into the low-level settings interface to see that. But more than that, Chrome’s preferences window just feels wrong. Labels are bolded, the last section has a scroll bar for just plain-old interface items, and buttons that bring up more info open a new window instead of a sheet. (This could be considered a feature, but it’s not Mac-like.)

#### Chrome beats Safari

- Memory usage. Safari is a memory hog, although part of that is running it in 64-bit mode and Chrome in 32-bit mode. But leaving Safari open for hours results in it ballooning to a few hundred megabytes of RAM, while Chrome reclaims things better when tabs are closed. Chrome handles Flash better, too.
- Closing tabs. Rather than try to explain this, I’m just going to refer you to [an article that explains the intelligent behavior of tabs in Chrome](http://www.theinvisibl.com/news/2009/12/08/a-piece-with-a-lot-of-screenshots-about-the-close-tab-behaviour-in-google-chrome/). And not having the close button on the left, as is standard on Mac OS X, didn’t bother me as much as I thought it would.
- Favicons in tabs. This is not unique to Chrome; if anything Safari is the weird case here. (I think even IE puts favicons in tabs now.) I suppose it would interfere with the nice clean look of Safari, but it is useful to know at a glance what’s in each tab.

#### Tossups

- The status bar. This is that little bar at the bottom of the window that shows where a link’s going to lead; occasionally a few sites will put messages down there using JavaScript as well. (This suggests a dastardly way to hide a link’s true destination.) On Safari it’s hidden by default, but I always turn it on. On Chrome…there isn’t one. Instead, mousing over a link gives you an overlay on top of the main page content. This is another one of those “minimizing the chrome” changes, but I can’t decide which I like better. Definitely something I noticed, though.
- The location field. On Safari, the location field will also give you results from your history, matching both URLs and page titles. With [Keystone](http://belkadan.com/keystone), you can also get “keyword search”, like “wiki Chrome” to look up Chrome on Wikipedia. Keystone is a hack, though, adding a feature to Safari by injecting code into the app. (And by the way, I wrote it.) Chrome includes the same history search, _plus_ keyword search (if you set it up right), _plus_ the top Google results for your query. Like the new “Google Instant” feature, the Chrome completions come up on-the-fly as you type. The downside is the results are not as clearly delimited, and the prediction seems to be worse than Safari’s (possibly since there are more options?). I could get used to the Chrome interface, though; I just didn’t take the time to set it up nicely to match my Keystone setup.
- Click-through. Both Safari and Chrome get this wrong: if the window’s in the background and you click on a tab, it’ll bring the window forwards _and_ switch to the tab. Convenient, you might think? More often annoying. Worse, if you click on a close button, it’ll bring the window forward _and close the tab!_ This is destructive behavior and should _not_ be the default in either browser. (…IMHO, of course.)
- Tab re-opening. This is not something that’s very important, but Safari considers re-opening an accidentally-closed tab to be an Undo operation, so you use Cmd-Z to do it. In Chrome, it’s distinct from the per-tab undo stacks, so you use the separate Cmd-Shift-T to do it. Both of these are reasonable things to do; I just kept using Cmd-Z in Chrome when I meant Cmd-Shift-T.

#### Final Thoughts

Chrome’s actually pretty good. Coming from a UI stickler like me, that’s quite a compliment. It runs smoothly, isn’t missing crucial features, and feels Mac-like enough to fit in. Contrast this with Firefox, which I basically can’t use for a whole day without feeling restricted. I would never switch my primary Mac browser to Firefox, but I actually could switch to Chrome. Google did a pretty good job.

I’m still sticking with Safari, partly because it still is a little more Mac-like, and I don’t really use extensions.^[1](#fn:ext) But I wish I could use Chrome as my alternate browser. Unfortunately, my usual reason for an alternate browser is to check out how a site looks with another rendering engine, or because a site doesn’t work in Safari. Chrome’s WebKit engine is too close to Safari’s WebKit engine for it to be useful for this. Looks like Firefox is going to hang on a bit longer.

1. At least, not at the time. Today I have a couple, despite the security risk, the main one being Marc Hoyois’ [ClickToPlugin](http://hoyois.github.com/safariextensions/clicktoplugin/). Sort of a power version of ClickToFlash, and as a proper extension rather than an injected bundle. [↩︎](#fnref:ext)

This entry was posted on [June](https://belkadan.com/blog/2011/06) 03, [2011](https://belkadan.com/blog/2011) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Mac OS X](https://belkadan.com/blog/tags/mac-os-x), [Safari](https://belkadan.com/blog/tags/safari), [Chrome](https://belkadan.com/blog/tags/chrome)
