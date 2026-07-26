---
title: How to reboot the Touch Bar without rebooting your MacBook
source: Jesse Squires
source_key: jessesquires
source_url: 'https://www.jessesquires.com/blog/2021/03/02/how-to-reboot-touch-bar-without-rebooting-macbook/'
original_language: en
published: 2021-03-02
status: active
license: © 2014–2026 Jesse Squires → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:408eb6645bedea05'
translated: false
---

> 原文：[How to reboot the Touch Bar without rebooting your MacBook](https://www.jessesquires.com/blog/2021/03/02/how-to-reboot-touch-bar-without-rebooting-macbook/)　·　Jesse Squires

The Touch Bar on my MacBook started freezing and experiencing UI glitches recently. It was completely unresponsive. At the time, the only way I knew to fix it was to reboot my entire machine, which felt ridiculous. Luckily, there is a better way.

Rather than thoroughly interrupt what you are doing, instead you can run `sudo killall TouchBarServer`. You should see the Touch Bar flash off and then turn back on immediately, now functioning properly.

So you do not forget this later, you can add a custom shell command to your `.zprofile` or `.bash_profile` for when this inevitably happens again.

```
function touchbar-reboot() {
    sudo killall TouchBarServer
}
```

Thanks to [Shai Mishali](https://mobile.twitter.com/freak4pc/status/1366418389862875136) (and [David Smith](https://mobile.twitter.com/Catfish_Man)) for the tip!

#### * * *

The first thing I tried was logging out and logging in again, but of course that did not work. I assume that was because the Touch Bar is [powered by bridgeOS](https://www.jessesquires.com/blog/2020/12/22/obscure-bridgeos-crash/), thus logging out of macOS had no effect.

I cannot wait until there is an option to get a MacBook Pro [without a Touch Bar](https://www.jessesquires.com/blog/2020/07/08/best-touch-bar-configuration-for-people-who-hate-the-touch-bar/).

#### * * *

**UPDATE:** [Alex Persian mentioned](https://mobile.twitter.com/alex_persian/status/1367119114775498755) on Twitter that you can also use `sudo killall ControlStrip` and `sudo pkill "Touch Bar agent"`. However, it is not clear how these relate to `TouchBarServer`. Are they child processes of `TouchBarServer`? Who knows. In my brief testing, `sudo killall ControlStrip` appears to have the same effect as `sudo killall TouchBarServer`, while `sudo pkill "Touch Bar agent"` does not seem to do anything.

My plan (and recommendation) is to use only `sudo killall TouchBarServer` for now, and if that does not always fix the Touch Bar freezing, then try these other options.
