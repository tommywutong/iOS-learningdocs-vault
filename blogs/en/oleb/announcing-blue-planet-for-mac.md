---
title: Announcing Blue Planet for Mac
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2011/02/announcing-blue-planet-for-mac/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:4b3cc5df0e5c72eb'
translated: false
---

> 原文：[Announcing Blue Planet for Mac](https://oleb.net/blog/2011/02/announcing-blue-planet-for-mac/)　·　Ole Begemann

# Announcing Blue Planet for Mac

My new Mac App [Blue Planet](http://blueplanetapp.com) is now available [on the Mac App Store for just $0.99](http://itunes.apple.com/de/app/blue-planet/id418903397?mt=12). Blue Planet is a small utility that replaces your desktop picture with a beautiful dynamic map of the Earth. As the day progresses and the sun illuminates different portions of the Earth, the map changes in real-time so you always see where it is day and where night.

[![Screenshot of Blue Planet on Mac OS X](https://oleb.net/media/blue-planet-screenshot-1.png)](https://oleb.net/media/blue-planet-screenshot-1.png)

You can choose from four gorgeous day images of the Earth, and the night view is even more beautiful in my opinion. The map can be centered on your current location or set to follow the sun. Visit the [Blue Planet website](http://blueplanetapp.com) for more screenshots and a comprehensive list of features.

If you decide to buy Blue Planet, I’d be very interested in your feedback.

# How does it work under the hood?

Internally, the map consists of three `CALayer` objects. The daylight image is the bottommost layer. Above it lies the image of the Earth at night. The area that is currently illuminated by the sun is stored in a `CGPathRef`. I then create a `CAShapeLayer` with this path and use the shape layer to mask the night image layer, thereby revealing the day image layer underneath. A Core Image blur filter provides the soft transition from between day and night.

I arrange two of these layer stacks side by side so that I can move from any point on the equator to anywhere else with a smooth animation.

The path that represents the sun-illuminated area of the Earth is recalculated roughly every minute or so. This means that the CPU utilization of Blue Planet is effectively zero.

# Almost 3 weeks in review

I submitted Blue Planet for review on February 7 and it was approved on February 27. So it took Apple almost three weeks to approve it, and not because of any problems with the app that I am aware of. It simply sat in “Waiting for Review” for 18 days and then was reviewed and approved over the weekend. From what I’ve seen other people say on Twitter, review times on the Mac App Store seem to be generally quite long at the moment. If you plan to submit an app, you should probably expect to wait at least two weeks (updates seem to go through quicker).

## First update in the works

The good thing about the long time in review is that the first update for Blue Planet is already around the corner. Expect an interactive time-lapse UI where you can play with the time of day and time of year to see how the sun illuminates different parts of the Earth as the seasons come and go.
