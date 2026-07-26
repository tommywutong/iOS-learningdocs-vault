---
title: Time Machine error 45
source: Jesse Squires
source_key: jessesquires
source_url: 'https://www.jessesquires.com/blog/2020/07/17/time-machine-error-45/'
original_language: en
published: 2020-07-17
status: active
license: © 2014–2026 Jesse Squires → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:1ad3229484814b1b'
translated: false
---

> 原文：[Time Machine error 45](https://www.jessesquires.com/blog/2020/07/17/time-machine-error-45/)　·　Jesse Squires

This is a brief follow-up to [the post I wrote about Time Machine failing](https://www.jessesquires.com/blog/2020/01/10/time-machine-failing-on-macos-catalina/) on macOS Catalina.

![Time Machine backups failing](https://www.jessesquires.com/img/blog/time-machine-fail.png)

I recently [upgraded my 6-year-old MacBook Pro](https://www.jessesquires.com/blog/2020/07/08/best-touch-bar-configuration-for-people-who-hate-the-touch-bar/), and one of the things I was most excited about was to see how many odd, random bugs and quirks would magically fix themselves by having the latest hardware, a clean install of macOS, and a clean install of all of my apps. I did not migrate or restore from Time Machine to specifically have a fresh start.

As expected, a lot of random issues have disappeared — Bluetooth flakiness, random UI glitches, etc. This new machine has been running smoothly. And yes, even Time Machine has been automatically backing up without issues. No more “error 45”.

Until now. After a few weeks with zero issues, Time Machine automatic backups are failing again with “error 45” like before. I still have no clue what is causing this issue, but now I know it is a bug in Catalina **for sure**. Previously, I thought it might have been a problem with my old machine and upgrading from Mojave.

#### * * *

The only good news is that I _sort of_ have a workaround, but not actually. I disabled automatic backups in System Preferences. This removes the annoying, incessant failure notifications. Unfortunately, it means that I must backup manually. However, every time that I initiate a manual backup it succeeds. So… who knows. `¯\_(ツ)_/¯`

To be honest, hourly backups are a bit excessive for me anyway. Everything that is important to me is backed up elsewhere — code is on GitHub, photos in iCloud, etc. So this is not a terrible setup for me. I keep the Time Machine icon in my menu bar, which allows me to easily initiate a manual backup every day or every few days.

#### * * *

Now that I think of it, “error 45” is an apt description of 2020 (and the past 4 years).
