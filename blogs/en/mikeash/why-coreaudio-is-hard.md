---
title: Why CoreAudio is Hard
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/why-coreaudio-is-hard.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:697a7fc60de5f303'
translated: false
---

> 原文：[Why CoreAudio is Hard](https://www.mikeash.com/pyblog/why-coreaudio-is-hard.html)　·　mikeash.com Friday Q&A

Posted at 2006-10-19 00:00 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [More Fun With Autorelease](https://www.mikeash.com/pyblog/more-fun-with-autorelease.html)  
Previous article: [Hacking C++ From C](https://www.mikeash.com/pyblog/hacking-c-from-c.html)  
Tags: [audio](https://www.mikeash.com/pyblog/?tag=audio) [coreaudio](https://www.mikeash.com/pyblog/?tag=coreaudio) [rant](https://www.mikeash.com/pyblog/?tag=rant)

Why CoreAudio is Hard

by [Mike Ash](https://www.mikeash.com/)

Playing fullscreen video used to be a really big deal but it just isn't very impressive anymore. The actual video data for 1080p video at 30fps is only about 240MB/sec. With current memory bandwidths being measured in GB/sec, this is still close enough to the ceiling to be interesting, but not enough to be a really hard problem. The main challenge in playing 1080p video is not getting the pixels onto the screen, but decoding the pixels from the incredibly sophisticated and complex compression format.  
   
 If you look at video, you generally have a very long time in which to generate a frame. 24fps is cinema quality, which gives you over 40ms per frame to draw it. It's generally accepted that higher framerates are better up to a point, but even 60fps (the normal limit for LCDs) still gives you about 17ms per frame.  
   
 CD quality audio, in effect, has frames which are only four bytes long (16-bit samples, two channels) but which play back at 44.1kHz. This only gives you 22 microseconds per frame! Of course, the frames are miniscule, but if you miss even one, odds are that the user will hear it. If you did something terrible like take a disk interrupt that took five milliseconds to process, you will hear an ear-rending glitch in the output audio. By contrast, you can drop an entire 17ms frame in 60fps video and it's usually pretty hard to notice.  
   
 So, modern OSes don't like very small tasks that have to happen extremely often. The obvious fix is buffering. Instead of generating one frame every 22 microseconds, generate a thousand of them every 22 milliseconds. Now we're back in the realm of video, except that we've added 22 milliseconds of latency to our audio output. This is a lot better, but the consequences of a possible delay are still much worse.  
   
 It comes down to a tradeoff between reliability and latency. You can avoid all glitches by using a 10-second buffer, but this will add a great deal of hilarity to iChat voice conferences and games. You can avoid basically all of the latency by using a 22-microsecond buffer, but then you get constant glitches as the OS services interrupts. The right balance is obviously somewhere in the middle.  
   
 Avoiding glitches is generally more important than avoiding latency, so most audio systems have fairly high latency. CoreAudio is architected around having as little latency as possible. This influences a lot of other decisions, and results in CA's often-confusing pull model for audio, as well as the fact that CA render callbacks run in realtime threads and are therefore subject to a bunch of annoying restrictions on what they're allowed to do.  
   
 These restrictions, by the way, make it very hard to have a good ObjC wrapper around CoreAudio. ObjC message dispatch is generally unsuited for realtime tasks. It's usually fast, but there are certain slow paths that can be taken if caches have been invalidated or you hit a class/selector combo that hasn't been seen before. Hit one of those in your render callback, or worse hit one of those and then smash into a spinlock that's held by a non-realtime thread, and life gets unpleasant very fast.  
   
 Overall this architecture is a good thing, as it gives us a high-performance and powerful audio layer. The problem is that there isn't a decent abstract layer above it for applications which just want to play back some music and don't care if it takes half a second to get to the speakers, and there's no abstract layer for the non-realtime components like effects and decoding. You can use QuickTime and NSSound and so forth for a lot of it, but they don't cover it all.  
   
 So in conclusion, yes, CoreAudio is hard, but this is at least partially justified. If you're really serious about doing audio on OS X, the time you spend tearing your hair out over it will not be misspent. If your needs are basic, see if you can use QuickTime or even OpenAL. If you want to do something like change the default system output device and you don't already know CoreAudio, curse the gods and resign yourself to slogging through it. Oh, and look for sample code, Apple has a fair amount for CA.

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.
