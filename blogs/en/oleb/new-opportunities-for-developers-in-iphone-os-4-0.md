---
title: New Opportunities for Developers in iPhone OS 4.0
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2010/04/new-opportunities-for-developers-in-iphone-os-4-0/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:582e915c321e0511'
translated: false
---

> 原文：[New Opportunities for Developers in iPhone OS 4.0](https://oleb.net/blog/2010/04/new-opportunities-for-developers-in-iphone-os-4-0/)　·　Ole Begemann

# New Opportunities for Developers in iPhone OS 4.0

It’s always a good idea to build apps that make use of new features when they come out. Competition is likely to be less fierce in the beginning, and since Apple is likely to introduce those features that have been requested most by users or have been deemed most interesting by Apple’s own market research, you can count on the fact that there will be considerable user demand for the new functionality. So let’s have a look at the public information that we got from yesterday’s [iPhone OS 4.0 introduction event](http://events.apple.com.edgesuite.net/1004fk8d5gt/event/) and what new app ideas could come out of it. Rather than talking about the things that Steve Jobs already highlighted in the presentation, I want to focus on some of the other new APIs that Apple showed us on this slide:

![Slide: New APIs in iPhone OS 4.0](https://oleb.net/media/iphone-os-4-0-slide-new-apis.png)

<sub>Some of the new APIs in iPhone OS 4.0.</sub>

# All things photos

At the moment, third-party apps have no direct programmatic access to the user’s photo library. The only thing they can do is present an image picker to the user who can then pick one (and only one at a time) photo that gets forwarded to the app. If “Photo Library access” means what I think it means, namely full programmatic access to the photo library, it could enable us to build full-fledged photo organizing apps similar to iPhoto or even Aperture and Lightroom and thereby solve [The Photography Question](http://speirs.org/blog/2010/4/3/everything-changes.html) (Fraser Speirs, see the bottom of that article). I hope the access to the Photo Library includes access to the images’ EXIF metadata (which currently does not get through the image picker) and the ability to modify, create and delete photo albums.

We know that the iPad already supports photos in RAW format so with this addition I predict that an iPhoto-like app on the iPad will be a huge hit. The fact that Apple also mentions support for ICC profiles on the slide suggests that they really mean to provide everything that’s necessary to write a professional RAW converter for iPhone OS.

And though [Core Image](https://en.wikipedia.org/wiki/Core_Image) isn’t mentioned and presumably not part of OS 4.0, the hardware-accelerated math library “Accelerate” that Steve Jobs mentioned could make it quite easy to write advanced photo filters with decent performance without having to resort to full OpenGL rendering (what I had to do in [Picture Effects](http://pictureeffectsapp.com) to get realtime updating). I see a Photoshop clone for the iPad on the horizon.

# Full access to still and video camera data

Direct access to the camera’s video feed can be used for:

- New forms of Augmented Reality apps (based on image recognition instead of sensor data).
- I would count on it

  ).
- Realtime manipulation of the live video. I will certainly look into this for Picture Effects. Hopefully it can become more like Photo Booth with effects being applied in realtime to the live video from the camera.
- API.
- Google Goggles

  .

# Calendar access and Local notifications

Access to the device’s calendar has to be one of the most-requested features since day one of the iPhone SDK. Now that it is coming, it will make a lot of existing organizer apps even more useful. Assuming developers can not only read existing calendar entries but also have write access, that is. I see a lot of apps integrating web data (like events from [upcoming](http://upcoming.yahoo.com/), the match schedule of your favorite football team or the date of the next solar eclipse) with the calendar.

Many developers presumably asked Apple for a calendar API in order to schedule alarms at a certain time that worked even if their app was not running. Until now, you would have to use push notifications for this, with all the additional overhead that requires: you would have to maintain a server and your app would have to communicate with it. With iPhone OS 4.0, this is no longer necessary and you don’t even have to add your alarms to the calendar where they might confuse the user. Apple added local notifications that, from the user’s perspective, seem to work just like push notifications but don’t travel through the cloud. Presumably, your app just tells the notification service to alert the user at a specified date and that’s it. For example, a to-do app can use local notifications to tell you about a task that is due. A travel companion app could alert you when your train is about to arrive.

# Location-based alerts

If I remember correctly, one of Android’s signature apps when it came out was a shopping list app that could remind you to buy groceries whenever your location was near the supermarket. Until now, apps like that weren’t possible on the iPhone, but with OS 4.0, you can use the low-power cell-tower-based background location service that Scott Forstall mentioned in the presentation. Same with a travel companion app that should alert you when you are on a train and your destination station comes up.

# What are your ideas?

That’s it for my ideas of what new things we can do on iPhone OS 4.0. What are yours? ~~Please share some in the comments.~~ [Ideas are worthless](http://37signals.com/svn/posts/1122-i-had-that-idea-years-ago), after all. It’s the execution that counts.
