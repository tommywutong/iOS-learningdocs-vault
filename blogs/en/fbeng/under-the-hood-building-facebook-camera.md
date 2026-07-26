---
title: 'Under the Hood: Building Facebook Camera'
source: Meta Engineering — iOS
source_key: fbeng
source_url: 'https://engineering.fb.com/2012/08/28/ios/under-the-hood-building-facebook-camera/'
original_language: en
published: 2012-08-28
status: active
license: © Meta → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:21d45ad6556be95e'
translated: false
---

> 原文：[Under the Hood: Building Facebook Camera](https://engineering.fb.com/2012/08/28/ios/under-the-hood-building-facebook-camera/)　·　Meta Engineering — iOS

Today we released Facebook Camera for iPhone 1.1. With this update, we’ve added our most commonly-requested feature, the ability to add photos to albums. You can also see all the likes and comments for your photos in one place and get your photo-related Facebook notifications within the app. Now that Camera has been out in the wild and we’re adding new features, I’d like to share a peek into the development process.

Facebook has been working on making photos better across the board. First, the photos team worked on improving performance and the viewing experience by increasing photo resolution and creating the option to view photos full size. On timeline, we added space for a cover photo so you can make your favorite photos front and center. By the time I joined the company through the acquisition of my startup Gowalla, the photos team was heavily focused on improving its mobile experience.

At Gowalla, we made a mobile app that was all about sharing experiences with friends. So when I joined Facebook, I knew I wanted to continue that thread and work on a unique app to help people share. While I was in Bootcamp (the six-week intensive onboarding process for all new engineers), I met with Jorn van Dijk, the designer on the Camera project. He had also joined the company via acquisition, and we connected over the vision for Camera. I started working on some small projects for the app, and decided to join the team. On the same day that I finished Bootcamp, the Camera team moved into our war room, a Facebook tradition for product teams that are focused on shipping a new product. As a result, for my first six months at the company, I never sat at my own desk.

In the beginning, most of the development effort had been focused on taking photos, filtering, and sharing. The app launched into camera mode, and we didn’t have feed, comments, or likes yet. So we started concentrating heavily on the consumption side of the app. We created the “bubble” UI for comments and likes, and we did lots of iteration on the feed design–figuring how to display multi-photo posts, captions, tags, etc. It started to feel nice.

![](https://engineering.fb.com/wp-content/uploads/2012/08/Fnv_DAAvzu4KHSgCAFKrhyVuPQkAAAE.jpg)

All of this work brought us to a surprisingly difficult decision: should the app start in camera mode, or feed? On one hand, we want to make capturing and sharing easy and obvious; on the other hand, the feed makes the app more engaging. We tested variations on both approaches, and the team was evenly divided over which worked best. Then another wrinkle emerged: an update to iOS added a camera button to the iPhone’s lock screen. It’s a small change that ends up having a big impact on how people use their phone to capture photos. We knew that people would use the lock screen camera for taking photos more than ever, meaning that Facebook Camera could primarily focus on making it easy to share existing photos beautifully. But we still weren’t sure how to structure the UI to enable it.

One weekend, I decided to block out all distractions and hack together a new approach to the navigation, merging the production and consumption parts of the app into one space. The result was a prototype that puts a mini camera roll at the top of the feed. When the feed is scrolled down, it provides easy access to the camera button, as well as some thumbnails of the most recent photos in your camera roll. People are more likely to share recent photos that were taken recently, so showing the last few photos in the same context as the feed creates a compelling “prompt” to share. Most importantly, it works really well for people who use the lock-screen camera.

While the team was working hard to get the infrastructure up to speed, Jorn, Dirk Stoop, and I decided to hack on this prototype to see if we could turn the it into a workable solution. For a few days, we worked in Dirk’s backyard until we were happy with the design, without distracting the rest of the team. At that point, we all came together to merge the new structure into the project, and focused on shipping the final product.

For me, the process we went through on this app demonstrates some remarkable things about Facebook’s culture: first, Facebook engineers are truly encouraged to join the project that they are most excited about, and where they can have the greatest impact. And despite being an established company with hundreds of millions of users, even new employees are given the opportunity to have a major impact on the direction of new products.

To check out our new version of Camera, take a look at the full release notes and download the app [here](http://itunes.apple.com/us/app/facebook-camera/id525898024?mt=8).
