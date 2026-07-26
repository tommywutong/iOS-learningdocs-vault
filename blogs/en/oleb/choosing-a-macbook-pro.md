---
title: Choosing a MacBook Pro
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2013/10/choosing-a-macbook-pro/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:8532d9fe4210385b'
translated: false
---

> 原文：[Choosing a MacBook Pro](https://oleb.net/blog/2013/10/choosing-a-macbook-pro/)　·　Ole Begemann

# Choosing a MacBook Pro

I am in the market for a new Retina MacBook Pro, but which one of the [new Haswell-based models Apple introduced this week](http://www.theverge.com/2013/10/22/4866808/apple-refreshes-macbook-pro-lineup) should I buy?

# 13-inch or 15-inch?

This decision was relatively easy for me. While I obviously like the lower weight and better portability of the 13-inch model, I usually do not carry my laptop around every day. It stays in one place for most of the week so portability is not my largest concern. On the other hand, I do work from time to time at places where I have no external display available so I value the additional pixels and screen area of the 15-inch model.

I also like the prospect of getting a quad-core CPU, if only to minimize compile times and the overall responsiveness of Xcode. While my current mid-2010 MacBook Pro has worked very well for me for more than three years[1](#fn:1), I lately found it to be uncomfortably slow when working with large projects in Xcode, despite upgrades to 8 GB RAM and a fast SSD.

So it’s gonna be a 15-inch MacBook Pro for me. Which leads me to the next question.

# Integrated Graphics or Discrete GPU?

For the first time, Apple gives buyers of the 15-inch MacBook Pro the choice between Intel’s integrated graphics and an additional dedicated GPU. Interestingly, the price premium for the discrete GPU is effectively zero: while it is only offered on the higher-end model, you will arrive at exactly the same price if you configure the lower-end model with the other model’s CPU, RAM and SSD choices – which is something I had planned to do in any event.

## Discrete GPU Comes For Free

It sounds like getting the dedicated GPU should be a no-brainer then. Unfortunately, it’s not that simple. The discrete GPU uses more power and can lead to considerably worse battery life. In a [review of last year’s Retina MacBook Pro](http://www.anandtech.com/show/6023/the-nextgen-macbook-pro-with-retina-display-review/16), AnandTech found that having the discrete GPU enabled would reduce web browsing battery life by as much as 25%.

And while there are software tools like [gfxCardStatus](http://gfx.io) that let the user manually disable the external GPU, this does not work very well in practice as many apps prevent the system from switching off the discrete graphics chip. As I understand it, as soon as an app uses certain Core Animation APIs the system will require to run it on the dedicated GPU even if the integrated graphics would be perfectly capable of doing so.

The same is true when you connect an external display: although the integrated GPU can drive up to three displays (including the internal one), the system will force-activate the discrete GPU.

![gfxCardStatus listing apps that prevent switching to the integrated GPU](https://oleb.net/media/gfxcardstatus-screenshot.png)

<sub>gfxCardStatus prevents switching to the integrated GPU on a 2012 Retina MacBook Pro.</sub>

In fact, Intel’s new Iris Pro 5200 GPU in the quad-core Haswell CPUs has become powerful enough to almost rival the discrete GPU in many applications. I highly recommend you read the [AnandTech Iris Pro 5200 review](http://www.anandtech.com/show/6993/intel-iris-pro-5200-graphics-review-core-i74950hq-tested), which gives a great overview of Haswell’s graphics capabilities.

## 4K Display Support

The most important graphics feature for me is support for external high-resolution displays, whether they come from Apple in the form of Retina Cinema Display or 4K monitors from other manufacturers. In the [MacBook Pro Tech Specs](http://www.apple.com/macbook-pro/specs-retina/), Apple lists a maximum resolution of 2560 × 1600 px over DisplayPort while 4K resolutions are officially supported over HDMI.[2](#fn:2)

On the other hand, Intel [actively advertises](http://software.intel.com/en-us/articles/quick-reference-guide-to-intel-processor-graphics) the [4K support](http://www.hardwareluxx.com/index.php/reviews/hardware/cpu/26405-haswell-test-intel-core-i7-4770k-and-i5-4670k.html?start=2) of the Haswell GPUs so I hope that Apple just doesn’t tell us the entire truth here because their own 4K Cinema Displays are not ready yet.

At any rate, it seems that regarding 4K display support the integrated GPU is just as future-proof as the dedicated GPU.

# Conclusion

Since I am not a gamer, I believe I am better off with the slightly lower performance and superior power efficiency of the integrated GPU, despite the lack of a price premium for the dedicated GPU.

That’s why I ordered the low-end 15-inch model, configured with 16 GB RAM, a faster CPU and a larger SSD. I expect this laptop to last me a number of years and since it is practically not user-upgradeable, I figured I should max it out as far as I can. I can’t wait for it to be delivered.

1. Except for a [hardware failure last year](https://oleb.net/blog/2012/05/15-inch-mbp-mid-2010-crashing-to-black-screen/) that Apple fixed under warranty. [↩︎](#fnref:1)
2. The restriction to refresh rates of 24 or 30 Hz at 4K seems to be an explicit [limitation of the HDMI 1.4 standard](https://en.wikipedia.org/wiki/HDMI) and not of the graphics hardware. The new HDMI 2.0 standard with support for 4K at 60 Hz has just been released in September 2013. [↩︎](#fnref:2)
