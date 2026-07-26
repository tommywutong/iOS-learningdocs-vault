---
title: 'Is a virtual machine for Cocoa programming inevitable? | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2010/07/is-virtual-machine-for-cocoa.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:d5a83bff503c8d9b'
translated: false
---

> 原文：[Is a virtual machine for Cocoa programming inevitable? | Cocoa with Love](https://www.cocoawithlove.com/2010/07/is-virtual-machine-for-cocoa.html)　·　Cocoa with Love (Matt Gallagher)

Recent articles by [John Siracusa](http://arstechnica.com/apple/news/2010/06/copland-2010-revisited.ars/) and [Jesper](http://waffle.wootest.net/2010/06/19/surpass/) have re-ignited some discussion about whether Apple might be working on another programming language to replace Objective-C. Neither of these articles closely examined a related but possibly more important question: is Apple planning to move application development to a virtual machine? In this article, I'll look at why I think moving to a virtual machine might happen along with a possible language transition.

> **Disclaimer**: this entire post is either a) speculation, b) aspiration or c) incrimination.

## Introduction: criticisms of Objective-C

Programmers, onlookers and pundits have criticised Objective-C for longer than Apple has been using it.

If the criticisms were valid and pressing, most could actually be addressed without replacing Objective-C/Cocoa.

Fixable complaints in the language and APIs include the lack of tuples, slices, maps or associations at a syntax level; the lack of template programming; the lack of namespaces; the lack of default parameters to methods; the lack of operator overrides/overloading; leaks and premature collection by the garbage collector (or lack of garbage collection on iOS platforms); the wordy, camel-coded naming conventions; the lack of package management; the lack of out-of-the-box support for "business" APIs like REST, SOAP, SQL, etc. Even the commonly mocked square bracket method invocation syntax could be changed (or supplemented) if the need existed.

None of these criticisms in isolation is a reason to replace Objective-C. All you could argue is that if Objective-C actually _needed_ to change all of these points, then perhaps you might as well replace the entire language.

But replacing the primary application programming language is a jarring task for a development community (especially one that has only just given up on Carbon) and Apple wouldn't do it to address aesthetic issues or minor features. The reasons for replacing a language would need to be more pragmatic and functional.

More relevant in the long term is the one feature that Objective-C can't remove or fix: complaints about C itself, in particular _C pointers_.

While code level compatibility with C is arguably Objective-C's best feature, it is also the source of Objective-C's most unpopular feature: the direct memory model.

## Direct access memory models are a shrinking market

You can't stop the shift away from direct access memory models like the one use in C language; they're simply losing popularity.

According to this list of [top 20 most popular programming languages](http://www.tiobe.com/index.php/content/paperinfo/tpci/index.html) (not exactly a scientific source but it will suffice) only 32% of people still use a language with a direct memory model (C, C++, Objective-C, Pascal and Delphi). In 10 years time, you probably won't see direct memory models used in new projects outside of kernels, drivers, computer games and low-level embedded software.

This means that whether or not Apple deprecate their direct memory model APIs (they probably won't), and whether or not they introduce a new language, Apple will introduce an official application environment with an abstracted memory model.

## The role of an application virtual machine in memory abstraction

Technically, Objective-C's current garbage collector is an abstracted memory model. But I'm excluding it from consideration because it's not a complete abstraction and it never will be while Objective-C contains C pointers.

Just because you don't need to release your memory, doesn't mean there aren't other memory problems. You still have pointers. These pointers can still point to anything. You still have C arrays that you can overrun. You can still have buffer overflows. You can still accidentally overwrite sections of memory. There are even situations where you can get the garbage collector to collect memory that you're still using.

That's a pretty leaky abstraction.

It is possible to create a memory model abstraction without using a genuine virtual machine (see [A Different Path](#adifferentpath), below) but a virtual machine allows you to lock down the abstraction so that there aren't any accidental loop holes. You no longer need pointers. You can't simply overwrite memory. You can't overrun arrays. You can't overflow buffers.

The virtual machine does this by removing instructions that offer direct access to memory. Instead, the instructions on the machine relate to objects, properties and values — you cannot access the wrong piece of memory and garbage collection can be precise rather than conservative because all memory references are known absolutely.

> **Clarification on what I mean by virtual machine**: A virtual machine is a description of a computer that is not directly tied to any specific computer implementation but instead can be mapped onto an actual machine. This mapping is normally either through runtime interpretation (like a scripting language), runtime simulation (like a computer emulator) or just-in-time compilation into native machine code (like Java's JVM). Regardless of how the virtual machine is run, the point is that the programmer only ever deals with this virtual scenario and the exact architecture and behaviors of the target machine are never directly accessed.

## Platform independence

A second argument for a virtual machine is actually unrelated to the language considerations: platform independence.

Apple have already switched CPU architectures twice in 17 years. It will almost certainly happen again. While the transition to Intel CPUs was unbelievably smooth (I remain stunned about how seamless it was) there was still a significant wait for Intel-native versions of many programs and significant cost to Apple and other developers to make the whole transition work.

With Apple's additional focus on iOS devices, it's also possible to imagine a range of different CPUs could be used across a single lineup and fat binaries (such as the existing armv6/armv7 iOS binaries) are only convenient for a small number of CPUs. If Apple wanted to use a dozen different CPUs, a single bytecode runtime would be the only way.

Wherever possible, good programming generally avoids coding to specific hardware components. Abstracting the CPU and the platform away from our programs is simply a logical step along the same lines.

> On the topic of running across different CPUs, an interesting point to consider is that Apple actually did recently introduce a new, platform independent language that runs in JIT compiled virtual machine: OpenCL. I don't foresee any push to re-implement Cocoa in OpenCL (it's way more cryptic than Objective-C) but the technology to do these things certainly exists.

## Virtual machine without a new language

An important point to note is that the introduction of a virtual machine could _preceed_ a new language.

If Apple decided that fear of manual memory management was keeping good programmers away but wasn't ready to actually transition to a new language in one leap, it would be possible to transition to the virtual machine _first_ (and gain many of the memory abstraction advantages) while keeping the code-level changes relatively minor.

While this might seem like a thoroughly strange thing to do, it does have a couple advantages.

The first is that an implementation of Objective-C adapted to run inside a virtual machine would be easier to bridge to native Objective-C outside the virtual machine. If you remember Apple's retired effort at bridging Java and Objective-C, the biggest technical difficulty was that Java's view of an object is less runtime dynamic than that of Objective-C and Java had difficulty keeping track of method and isa pointer changes on the Objective-C side. Bridging a virtual machine language to its non-virtual machine equivalent would be easier on this modelling level.

The second advantage of keeping Objective-C during the transition to a virtual machine is that Cocoa is currently written to match Objective-C's feature set. Cocoa might be able to remain substantially similar, making Apple's work upfront much easier.

> **Update:**[Jesper has responded to this point](http://waffle.wootest.net/2010/07/16/objective-dash/) and explained why virtualizing Objective-C while keeping some level of compatibility with non-virtualized Objective-C is probably not a good idea.  
>   
> In short: a virtualized version of Objective-C would (like C++.NET before it) need to have a number of language features removed (to the point where it is not source compatible enough to matter) or it would need to throw runtime exceptions all over the place if your code violated a long list of rules (which doesn't solve the memory abstraction problem it just hurts you if you get it wrong).

## A different path

Of course, just because the above advantages exist, doesn't mean that a virtual machine environment is a guaranteed next step in Mac programming evolution.

There do exist compiled, garbage collected, memory safe languages that don't require virtual machines but would satisfy the requirement of a totally abstracted memory model. [Google's Go language](http://golang.org/) is one example.

It is unlikely Apple would literally adopt Go. Aside from the fact that Go is still a work in progress, there is also the problem that Go (and most other languages) are not interoperable or bridgeable with Objective-C classes (again this is why bridging Java to Objective-C was problematic — the runtimes need to be significantly compatible). In fact, Go does not yet easily bridge to C or C++, yet.

Actually moving to a Go-like language would require a clean break with no backwards compatibility. While a clean break is not impossible (Carbon to Cocoa was a clean break), I think it more likely that Apple would choose to keep some amount of interoperability by either using a custom language — or a custom variation of an existing language — that uses a runtime closer to Objective-C. The reason why I suspect this is that Apple have already had the chance to replace Cocoa (with iOS) but chose to keep largely the same design — I suspect that they'd choose to keep Cocoa into the future on the Mac, even if the language or environment changes.

The greater possibilities of backwards compatibility, bridging and portability afforded by virtual machines, and the excellent performance of modern JIT implementations, lend me to think that a non-virtual machine option doesn't provide enough flexibility and advantages for the next isn't a compelling enough to warrant the pain of a language transition.

## Conclusion

Obviously, I like Objective-C and Cocoa; I'm sure that much is clear from the existence of this blog and my [posts](https://www.cocoawithlove.com/2009/10/objective-c-niche-why-it-survives-in.html) [defending](https://www.cocoawithlove.com/2008/08/in-defense-of-objective-c-20-properties.html) its [traits](https://www.cocoawithlove.com/2009/06/method-names-in-objective-c.html). I don't agree with most of the criticisms that I've listed in this article — for the most part, I think the criticisms are either trivialities or they're philosophically and technically misguided.

But Mac programmers can't fight against an overwhelming trend towards totally abstracted memory models that's largely happening outside the borders of Mac programming.

Furthermore, I don't think the eventual move towards an application virtual machine is a change that needs to be fought. Most of what currently defines Cocoa and Mac programming — the attention to detail, the way widgets, methods, classes and APIs all work well together won't change. In fact most of Cocoa might actually stay the same.

Eventually though, I'm sure Apple will switch to a new programming language; fashions change and a new language is always refreshing (if a little weird in the beginning).

There really isn't a rush to do this though. Certainly iOS devices don't need the performance hit right now. But even on the Mac I think there will be a few years warning before anything happens and no forced transition when it finally does.

When I say there isn't a rush: I mean it. I think its probable that you will still be able to release new, non-virtual-machine, Cocoa/Objective-C programs for the Mac OS du jour in 10 years time (in the same way that you can still write Carbon programs today if you choose). I just don't think it will be the most common choice.
