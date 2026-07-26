---
title: Previously previously previously relocated items in macOS Catalina
source: Jesse Squires
source_key: jessesquires
source_url: 'https://www.jessesquires.com/blog/2020/04/11/previously-previously-previously-relocated-items-in-macos-catalina/'
original_language: en
published: 2020-04-11
status: active
license: © 2014–2026 Jesse Squires → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:bd6de043ebf8aef1'
translated: false
---

> 原文：[Previously previously previously relocated items in macOS Catalina](https://www.jessesquires.com/blog/2020/04/11/previously-previously-previously-relocated-items-in-macos-catalina/)　·　Jesse Squires

When I first upgraded to macOS Catalina, there was a “Relocated Items” folder on the desktop. Well, actually it was an alias to `/Users/Shared/Relocated Items/`. This was expected, given the new “[security features](https://mjtsai.com/blog/2019/07/23/annoying-catalina-security-features/)” in Catalina, which includes a new [read-only system volume](https://support.apple.com/en-us/HT210650). What I did not expect was to see this folder reappear with **every single update**.

![Previously relocated items](https://www.jessesquires.com/img/blog/previously-relocated-items.jpg)

<sub>Previously previously relocated items in macOS Catalina</sub>

Not only does “Relocated Items” reappear with each point release (10.15.1, 10.15.2, etc), it also returned with the latest [_supplemental update_](https://9to5mac.com/2020/04/08/apple-releases-macos-10-15-4-supplemental-update/). That is absurd to me. Who at Apple finds this acceptable?

#### * * *

After my initial upgrade to Catalina, I can’t remember all the files that were in “Relocated Items”, but now it’s the same apache config files every time single time. And every single time, I delete this folder and my system is fine. I have some custom apache configurations (in `/etc/apache2/..`) to test this website locally, but none of the relocated files are those configs.

#### * * *

As a software developer I understand what’s happening, but what about my parents or other folks who are not tech savvy? They have no idea what “Relocated Items” are and they don’t care. It only creates confusion, and leaks technical implementation details to users.

Is this a major problem? Of course not. But it is yet another incredibly [annoying](https://mjtsai.com/blog/2019/07/23/annoying-catalina-security-features/) “feature”. It is another cut to add to the [list of 1000 cuts](https://mjtsai.com/blog/2019/10/15/catalina-system-issues/) that came with macOS [~~Catalina~~ Vista](https://tyler.io/macos-10-15-vista/). I really hope the next major release of macOS addresses the shortcomings, bugs, and annoyances introduced in Catalina.
