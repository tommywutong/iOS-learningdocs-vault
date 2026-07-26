---
title: 'John Siracusa: A Dark Age of Objective-C'
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2011/04/john-siracusa-a-dark-age-of-objective-c/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:6ce18c46d4ff6ff7'
translated: false
---

> 原文：[John Siracusa: A Dark Age of Objective-C](https://oleb.net/blog/2011/04/john-siracusa-a-dark-age-of-objective-c/)　·　Ole Begemann

# John Siracusa: A Dark Age of Objective-C

In [last week’s episode of the Hypercritical podcast](http://5by5.tv/hypercritical/14), John Siracusa revisited a topic (beginning at minute 21:09) he already blogged about in 2005. At that time, in a series of blog posts titled [Avoiding Copland 2011](http://arstechnica.com/staff/fatbits/2005/09/1372.ars) ([Part 2](http://arstechnica.com/staff/fatbits/2005/09/1393.ars), [Part 3](http://arstechnica.com/staff/fatbits/2005/10/1412.ars)), John wondered whether there was a fundamental crisis looming in Apple’s future, of a similar impact as the badly-managed switch to a modern OS with memory protection and preemptive multitasking, exemplified in the failure of the Copland project. In the 1990s, this crisis almost killed Apple.

# Apple’s lack of a memory-managed language and API

In 2005, John identified Objective-C and Cocoa as a serious potential pitfall in Apple’s future. Specifically, the fact that Objective-C required manual memory management (and still does on iOS) and forced developers to mess around with pointers might make it more flexible and faster than more abstract platforms like Java and C#, but eventually, the world would inevitably move towards higher levels of abstraction and give Apple’s competitors an advantage:

> All other things being equal, when faced with two technologies, one less abstracted but higher performance, and one more abstracted but slower, the more abstracted, slower technology will always win in the long run. While hardware performance increases over time, the human capacity to deal with complexity does not[.]

To make matters worse, it wouldn’t be enough for Apple to just invent or adopt a new programming language: the entire API that is Cocoa is written and optimized for Objective-C, and a language that diverts significantly from Objective-C would also require a new set of APIs that builds on its strengths.

I think John makes a very good argument how far ahead Microsoft was (and still is) on the transition to a higher level of abstraction and a corresponding API and what a feat it was to pull this off (.NET was introduced in early 2002, almost a decade ago). That’s not to say that Apple is a decade behind, of course, since Cocoa is arguably a much better API than Win32 was.

# iOS to the rescue: it’s like traveling back in time

Originally, John envisioned the 2010–2015 timeframe when Apple would run into problems with Objective-C. When he [revisited his predictions for the first time in 2010](http://arstechnica.com/apple/news/2010/06/copland-2010-revisited.ars), none of it had really happened. John identifies the rise of the iPhone as one reason for that. When developers faced the constraints of the iOS devices (slow CPUs, very little memory, no swap space), the low-level nature of Objective-C turned into an advantage again and it might at least partly be responsible for the generally better performance of iOS compared to its competitors.

> This new hardware reality has effectively set the clock back on higher-level programming languages and frameworks in the minds of Apple developers, and Objective-C's nature as a superset of C has renewed its status as a perceived advantage. It's hard to get worked up about still dealing with low-level, per-byte-precise entities like pointers and C structs when your application is constantly receiving low-memory warnings from the OS.

But let’s look a few years ahead again: iOS devices have already made great progress in terms of performance, and even today, with significantly more memory than the original iPhone and dual core CPUs beginning to appear, features like garbage collection start to make sense on the iOS platform. This trend will surely continue at a fast pace over the next few years. And Apple’s competitors in the mobile space, be they Google or Microsoft or HP, have all settled on managed languages for their platforms.

All that doesn’t seem to bother app developers at the moment, with thousands of newcomers to Objective-C and Cocoa still being lured by both the prospect of App Store success _and_ the quality of Apple’s APIs (I don’t know much about Android but from what I hear, many consider developing for iOS to be a more pleasant experience). That surely attests to the high quality of both the language and the frameworks.

> Oh, I know what you're thinking. You there, you Cocoa developer—you think I'm off my rocker. Cocoa and Objective-C are Apple's biggest strength, you say, not a ticking technology time bomb! Furthermore, despite its C heritage, it's unfair to characterize Apple's implementation of Objective-C as "low-level" when it offers dynamic capabilities and language features that even the mighty Java still lacks.
> 
> […]
> 
> Despite the lack of a 2010 crisis, Apple will _eventually_ need to address this issue. The reason I was thinking about it five years ago is the same reason I'm even more concerned about it now: development platforms are hard to change. First there are the technical issues of selecting or developing a new language and creating a new API for it. Great APIs take years to develop and mature. Just look at Cocoa for a good example.

# Did Apple miss a chance with the iOS introduction?

That raises an interesting question: did Apple miss the perfect chance to switch to a new platform with iOS? Given enough time to plan all this, they could have left Objective-C and Cocoa behind on Mac OS X and created an all-new OS with its own programming language and API for their new and shiny mobile platform. If, rather than proudly proclaiming that the iPhone ran OS X under the hood, Steve Jobs had said that there was no way to port OS X to this tiny, feeble device, nobody would have doubted him, I suppose.

Just as it is now, the iOS SDK would be Apple’s new star; and instead of porting features invented for the iPhone (such as Core Animation) directly to Cocoa on the Mac, Apple would have let Foundation and AppKit die a slow and painful death and used Snow Leopard and Lion to slowly introduce the new iOS SDK to the Mac as another way to write Mac apps. The introduction of the Mac App Store could have served as the final breakthrough of the platform if Apple only accepted apps written in “UIKit” to the store.

It’s a nice thought experiment but it obviously misses the fact that such a move would have involved a lot more resources on Apple’s part and could have easily delayed the introduction of the iPhone by a couple of years. It takes time to develop a mature platform and it is doubtful if iOS would be as full-featured and stable as it is now. Moreover, we had just established that the problems of Objective-C have actually turned into an advantage again on mobile devices. Had the iPhone been just as successful if it had launched on a new software platform but with the same performance problems OS X had in the beginning? I think not. The You had me at scrolling effect was too important.

# Something has to happen someday

So where does that leave us? As John says, Objective-C will certainly be obsolete _someday_, even if we don’t know when. And there is more to it than just automatic memory management. In my opinion, the long-term weakness of Objective-C is its strict C heritage. As long as we developers continually have to convert between `NSInteger` and `NSNumber *` just to store a simple value in a collection or pass it to some API, something is wrong and should be fixed.

Like John, I do hope that some team at Apple has another transition in the works. As to the question what the solution for Apple could be: I have no idea. Perhaps the huge effort Apple continues to put into the [LLVM project](http://llvm.org/) is an indication that LLVM has something to do with it.

I highly recommend listening to the podcast or reading the four articles. Good stuff.

**Update April 24, 2011:** I first wrote a paragraph about this topic in my [iOS development highlights: July 2010](https://oleb.net/blog/2010/07/ios-development-highlights-july-2010/) article. The first bullet point has a few good links to other people’s posts. I encourage you to check them out.
