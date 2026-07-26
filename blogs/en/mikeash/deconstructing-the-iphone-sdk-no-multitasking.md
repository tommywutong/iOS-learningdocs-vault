---
title: 'Deconstructing the iPhone SDK: No Multitasking'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/deconstructing-the-iphone-sdk-no-multitasking.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:050ed2b14b368fe6'
translated: false
---

> 原文：[Deconstructing the iPhone SDK: No Multitasking](https://www.mikeash.com/pyblog/deconstructing-the-iphone-sdk-no-multitasking.html)　·　mikeash.com Friday Q&A

Posted at 2008-03-15 01:02 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Use strnstr](https://www.mikeash.com/pyblog/use-strnstr.html)  
Previous article: [Code Signing and You](https://www.mikeash.com/pyblog/code-signing-and-you.html)  
Tags: [iphone](https://www.mikeash.com/pyblog/?tag=iphone) [rant](https://www.mikeash.com/pyblog/?tag=rant)

Deconstructing the iPhone SDK: No Multitasking

by [Mike Ash](https://www.mikeash.com/)

To those of you who are late to the party, the iPhone SDK [has many limitations](http://www.rogueamoeba.com/utm/2008/03/11/iphone-sdk-bug-filing/) on what your apps can do. Among these limitations is a requirements that applications not run in the background. In other words, when the user switches away from an application, it must quit.

Sadly, Apple does not explain their restrictions. [A lot of rationalizations](http://daringfireball.net/2008/03/one_app_at_a_time) have appeared, but overall I believe that they make little sense.

**Insufficient Hardware**

The most common rationalization is that the iPhone is not powerful enough to support full multitasking. This is a curious argument, and it's hard to see how anyone who's been using a computer for more than a few years could make it. For example, here are the specifications of the first computer I used that could multitask, a [Macintosh LC](http://docs.info.apple.com/article.html?artnum=112178):

- 16MHz Motorola 68020
- 2MB
- 40MB

(Later I loaded a hack on my [Apple IIGS](http://en.wikipedia.org/wiki/Apple_IIGS), worse in many ways, which also let it multitask. But this was very much a hack, unstable and slow, so it doesn't really count.)

But, you say, this was poorly done cooperative multitasking. The iPhone runs UNIX! Well, here are the specifications of the first computer I ran a [UNIX-alike](http://www.mklinux.org/) on, a [PowerCenter Pro 180](http://www.everymac.com/systems/powercc/powercenter_pro/powercenter_pro180.html):

- 180MHz PowerPC 604e
- I forgot, but probably 32MB
- 2GB

And of course you can [run UNIX](http://netbsd.org) on [vastly](http://netbsd.org/ports/#suggested-arm) [less](http://netbsd.org/ports/#suggested-m68k).

Now, compare these specs with the [iPhone](http://en.wikipedia.org/wiki/IPhone):

- 620MHz ARM
- 128MB
- At least 4GB, up to 16GB, usually 8GB

(Here is [the original source for the CPU](http://www.engadget.com/2007/07/01/iphone-processor-found-620mhz-arm/) and [the source for the RAM](http://www.semiconductor.com/resources/reports_database/view_device.asp?sinumber=18016).)

**CPU**

It should be pretty clear that the CPU can handle running more than one program at once. You can't just compare the clock speeds, because the ARM architecture is vastly different, but a 620MHz ARM is plenty speedy. It's going to compare very favorably to the PowerCenter Pro and it's going to utterly crush the LC.

CPU speed isn't even very critical for multitasking. I've done realtime high-performance preemptive multithreading on an embedded CPU running at a couple of MHz powered by 6 AA batteries all literally sitting inside [an oversized Lego brick](http://en.wikipedia.org/wiki/Lego_mindstorms).

Multitasking only increases CPU requirements by the amount of extra _activity_ present. You can have a hundred apps all running on the slowest possible CPU if only one of them is actually doing something. On the other hand, you can run two applications on a really powerful CPU and they will fail if they both need the whole thing to run at the required speed.

Most iPhone apps will play nicely. Most people want to run in the background to watch for incoming messages or alert about events, hardly demanding tasks. Those which don't play nicely will not be very popular.

**RAM**

This is an even bigger one, according to most of the people I've seen. The device has only 128MB of RAM. Of course 128MB of RAM is luxury compared to many systems running full GUIs. To put this in perspective, 128MB of RAM was the minimum system requirement for Mac OS X 10.3, and it handled multitasking just fine.

Of course the limited RAM is greatly compounded by...

**No Swap**

The iPhone has no swap! Panther could get away with 128MB of RAM but it would swap like crazy. Without swap, the naysayers claim, there's no reasonable way to allow arbitrary multitasking.

This is true but misses the point entirely. The question is not whether the iPhone can support multitasking without swap. The proper question is this: _why doesn't it have swap?_

- Swap would be too slow, some say. But swap is essentially random access, thus the single most important factor in swap speed is the seek time of the storage device. The iPhone uses flash memory, and flash has basically no seek time It's 100-1000 times faster than a hard drive. Swapping to flash will in most cases be much faster than swapping to rotating magnetic platters.
- Flash has limited write cycles! The typical flash drive can only be written to between 100,000 and a million times per cell before it wears out and stops working. People tend to interpret this as meaning that flash drives are delicate and need to be manhandled as little as possible to survive. But this is simply not true; the limit is

  . Modern wear-leveling algorithms spread out the writes across the entire drive. A modern flash drive will

  last for decades

  before failing even when it's being written to at maximum speed all day every day. The flash drive will be the last component of your iPhone to die.

The device is clearly technically capable, so why doesn't it do it? I speculate that it may simply be a holdover from when the iPhone only ran Apple software and therefore didn't need it.

**Battery**

At last, one which makes some sense. Runaway background apps will kill your battery, making for an unpleasant phone experience.

However, if you don't want runaway background apps killing your battery, don't run them. This is particularly true if Apple is going to play nanny to us all and only let us use approved software. Part of the approval process could be making sure they behave nicely in the background, rather than the current state of making sure they don't run in the background at all.

Better yet, the OS could be made a bit smarter and heavily deprioritize background applications, such that they would not be allowed to use a large proportion of the CPU even if nothing else wants it. This would ensure that battery usage is kept to a minimum while still allowing apps to keep a watchful eye over whatever they need to monitor.

**Conclusion**

The situation with the iPhone SDK is frustrating for many reasons, not the least of which is the fact that Apple refuses to explain any of its actions. This leaves the rest of us guessing. A lot of people have guessed that this particular limit is due to technological restrictions, believing that the iPhone is simply too limited to handle true multitasking. I hope I have made a convincing case that this is not true. Apple's motivations may be based on user experience or limited engineering time, but the hardware itself is more than capable.

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.
