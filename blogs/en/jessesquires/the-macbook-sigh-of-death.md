---
title: The MacBook sigh of death
source: Jesse Squires
source_key: jessesquires
source_url: 'https://www.jessesquires.com/blog/2022/02/15/mac-sigh-of-death/'
original_language: en
published: 2022-02-15
status: active
license: © 2014–2026 Jesse Squires → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:9ef5f9b22389c37b'
translated: false
---

> 原文：[The MacBook sigh of death](https://www.jessesquires.com/blog/2022/02/15/mac-sigh-of-death/)　·　Jesse Squires

I have been experiencing bizarre kernel panics with my Mac lately. I have a 2020 Intel MacBook Pro, the last Intel model before the M1 debuted. It has generally been working fine. Despite poor software quality and numerous bugs lurking around in macOS, I rarely see kernel panics anymore. In fact, I can’t remember the last time I had a kernel panic before this issue. There have been no major changes on my machine and I’m on the latest version of Monterey.

Here’s what happens. Suddenly the MacBook display turns off, the fans turn on full blast for a couple seconds (they are louder than compiling the largest Xcode project you can think of), and then the machine shuts down completely. I’m calling it the “sigh of death” because it’s as if the machine is simply giving up and exhaling in an exasperated, dramatic sigh of defeat — like an exaggerated cartoon character would do. It has happened to me 3-4 times within the past few weeks.

![macOS screen of death](https://www.jessesquires.com/img/blog/mac-sigh-of-death-1.jpg)

<sub>macOS screen of death</sub>

If you have been using a Mac for any amount of time, you have likely seen the “screen of death” at least once. If not, consider yourself lucky. Usually when this happens, it is preceded by some notable event — your machine freezes, your cursor starts beach-balling, everything becomes completely unresponsive, and then you’ll see the screen of death. It’s also usually silent, or at least, there’s no notable change with the fans.

That’s why this is so peculiar. It seems to be random and unprovoked in terms of software — there are not any specific apps, scripts, tasks, etc. that seem to trigger it. Prior to the kernel panic, the machine is fully responsive and functioning like normal. In some cases, I am actively using it. However, there is one commonality across all incidents so far. Each time it has happened, it is _after_ I unplug the machine from power. I typically work at a desk with the MacBook plugged in, and occasionally I’ll move to the kitchen table or couch and work off battery power for a bit. Each time the sigh of death has occurred, it is shortly after being unplugged. It makes me wonder if there’s some hardware issue?

Upon rebooting, the “Problem Report for macOS” window appears as expected. Usually, the details section will contain a stack trace from which you can derive _some_ kind of useful information about what happened — but not with the sigh of death. All it says is “Intel CrashLog recorded due to unexpected reset” — whatever that means.

![macOS report a problem](https://www.jessesquires.com/img/blog/mac-sigh-of-death-2.jpg)

Finally, I vaguely remember reading another blog post from someone about this exact issue. It was awhile back, perhaps during a macOS beta, and they also called it the “sigh of death”. Unfortunately, I could not find the article anywhere on the web. If anyone recalls this post or can find it, please send me the link and I’ll update this post to link to it.

And if you are experiencing this issue, or have any idea about what’s happening, please let me know.

##### [Update](#updated-16-february-2022)  _16 February 2022_

Thank you [Michael Tsai](https://twitter.com/mjtsai/status/1493986603156525056) for finding the post I was referring to above, [The Big Sur Sneeze](https://mjtsai.com/blog/2020/12/23/the-big-sur-sneeze/). My memory of that post was not entirely accurate. The details are slightly different than what I describe in this post, but it seems likely that the underlying issue is the same.

Also, a few folks on Twitter commented that they have experienced this issue.

[@MrThon](https://twitter.com/MrThon/status/1494004392122585093):

> I have the same problem after I unplug the dock with external screen, then later plug it back, external screen does not come back and then sigh and reboot

[Grant Butler](https://twitter.com/grantjbutler/status/1494008856506101761):

> Yeah, that’s where I’ve been experiencing it. Plug in a USB-C/DisplayPort monitor, and then after a few seconds, the get the sigh and reboot.
