---
title: Time Machine error 35 in macOS Monterey
source: Jesse Squires
source_key: jessesquires
source_url: 'https://www.jessesquires.com/blog/2022/01/11/time-machine-error-35-monterey/'
original_language: en
published: 2022-01-11
status: active
license: © 2014–2026 Jesse Squires → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:349b7fa87bb192b9'
translated: false
---

> 原文：[Time Machine error 35 in macOS Monterey](https://www.jessesquires.com/blog/2022/01/11/time-machine-error-35-monterey/)　·　Jesse Squires

Well, it appears my saga of [obscure errors with Time Machine](https://www.jessesquires.com/blog/tags/time-machine/) continues. The first issue I had was in 2020 with [macOS Catalina and “error 45”](https://www.jessesquires.com/blog/2020/01/10/time-machine-failing-on-macos-catalina/). That error was [fixed (for me) in Big Sur](https://www.jessesquires.com/blog/2021/04/07/time-machine-error-45-big-sur/) in 2021. As of this week, the error is back, though this time on macOS Monterey.

I’ve been on macOS Monterey for quite a few months now. I haven’t had any _major_ issues with Monterey — only the thousands of paper cuts (like this error) representing the slow degradation of macOS that I’ve grown to expect in recent years.

The error message is basically the same as before, _“the backup disk image could not be accessed (error 35)”_ — however, now the error code is 35 instead of 45. Perhaps it is failing in a slightly different way, or perhaps the error code simply changed in Monterey. Like [I mentioned before](https://www.jessesquires.com/blog/2020/01/10/time-machine-failing-on-macos-catalina/), I use Time Machine with my NAS (“Leviathan.local”) and haven’t had any problems with my setup until these recent errors. Sadly, I still have no idea what causes the error nor how to fix it given the absolute dearth of useful information in the error message.

For now, rebooting my MacBook has “fixed” the issue and backups are working again — but this is likely only temporary. I expect to see the error again soon, and I supposed I’ll just have to reboot again. And again. And again.

![Time Machine backups failing on macOS Monterey](https://www.jessesquires.com/img/blog/time-machine-fail-again.jpg)

##### [Update](#updated-11-january-2022)  _11 January 2022_

Two readers have provided some tips on Twitter. [David Humphrey](https://twitter.com/humphd/status/1481049310888439814) mentioned a better possible workaround:

> I had something like this with Time Machine backups to my Synology, and it turned out to be macOS holding open simultaneous connections, which is why rebooting fixed it. When it happens now, I know that I can go and force a disconnect of the user on the NAS and that fixes.

[Rodrigo Escobar](https://twitter.com/RodAEscobar/status/1481040662027898885) shared [James Pond’s Time Machine troubleshooting docs](http://oldtoad.net/pondini.org/TM/Troubleshooting.html). Specifically, [item C17](http://oldtoad.net/pondini.org/TM/C17.html) (“sparse bundle could not be accessed”) seems to match! The options to resolve are consistent with David’s comments above.
