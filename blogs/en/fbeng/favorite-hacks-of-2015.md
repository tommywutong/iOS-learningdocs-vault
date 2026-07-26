---
title: Favorite hacks of 2015
source: Meta Engineering — iOS
source_key: fbeng
source_url: 'https://engineering.fb.com/2015/12/30/android/favorite-hacks-of-2015/'
original_language: en
published: 2015-12-30
status: active
license: © Meta → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:f45e4e1d6faf0466'
translated: false
---

> 原文：[Favorite hacks of 2015](https://engineering.fb.com/2015/12/30/android/favorite-hacks-of-2015/)　·　Meta Engineering — iOS

Every year, we host a number of hackathons across the globe, where teams come together for a few days to brainstorm, build for fun, or craft innovative solutions to sticky problems. The passion people have for the ideas generated in this space outside of their daily work results in everything from new products to open source tools for the developer community. Here are a few of our favorite features that have hackathon roots and that debuted in 2015.

## React + Oculus: Real-time coding for VR

![](https://engineering.fb.com/wp-content/uploads/2015/12/GN04vgDbur6P9OsDAJeoRgwAAAAAbj0JAAAD.png)

In an infra hack this fall, two engineers built a prototype for Oculus and VR that allows developers to modify the code in real time. Instead of switching between the headset and the monitor to modify code, developers can now write code with the headset on. Using the standard [React](https://facebook.github.io/react/) library, the engineers replaced the DOM renderer with a custom one that renders to three.js. A dot appears in the middle of the developer’s vision and a window pops up with components — a box or a sphere, for example — that will render into VR. The selector can be used to edit objects in real time, such as changing the box color. This hack extends React’s mantra “learn once, write everywhere” to VR.

## On-board optics

Front panel congestion from optics plugged in at the top-of-rack switch restricts airflow and makes cooling difficult. One hackathon team moved the optics to the middle of the board, which not only resolves congestion but also improves signal integrity and reduces power consumption, as the optics are closer to the switch chip. With this configuration, the team was able to run a 300 Gb/s link over multi-mode fiber.

## Celebrate Pride

![](https://engineering.fb.com/wp-content/uploads/2015/12/GN84vgChXUAXKk8FAIHZgDMAAAAAbj0JAAAB.jpg)

Originally the vision of two interns, the popular rainbow filter for profile pictures in support of the LGBTQ community went from [hack to product](https://engineering.fb.com/posts/778505998932780/72-hours-to-launch-celebrate-pride/) in just 72 hours. In the tool, a preview of the new profile picture — using a rainbow overlay that leveraged existing Facebook code — loads quickly by using CSS layering and deferring image processing until the person clicks the “Use as Profile Picture” button. It also has a text field for a caption, which the team designed to show up inline in the “changed profile picture” story, making it easier for people to share the page with their friends. In the weekend following the launch, more than 26 million people updated their profile pictures to celebrate Pride.

## Stetho

[Stetho](http://facebook.github.io/stetho/) is a debugging platform for Android that gives developers access to the web-based Chrome Developer Tools, which allows them to inspect network traffic and view hierarchy, query SQLite databases, and manage an app’s SharedPreferences. Developers can also enable the dumpapp tool, a command-line interface to application components with both default and customizable plugins. Like many hacks, Stetho was built by an engineer who was dissatisfied with existing tools. After gaining traction internally, Stetho became our first Android open source project this year.

## Boomerang

![](https://engineering.fb.com/wp-content/uploads/2015/12/GNc4vgCv5-SNZycGANWS_zYAAAAAbj0JAAAD.png)

Boomerang is a hack turned product from Instagram that’s as engaging as a video but as easy to capture as a single photo. Press one button, and Boomerang takes a series of photos in less than a second and then stitches them together into a video, which is sped up and played forward and backward on loop and automatically saved to your camera roll. Boomerang for iOS uses the same image-stabilization technology as Hyperlapse, which gives the videos a cinematic feel. Boomerang was the first app that Instagram globally launched on [Android](https://play.google.com/store/apps/details?id=com.instagram.boomerang) and [iOS](https://itunes.apple.com/us/app/boomerang-from-instagram/id1041596399) simultaneously. Boom.

## Warp Speed Data Transfer

While working on distributed, replicated databases within Facebook, a software engineer realized that the snapshot transfer part of the system was slow and inefficient. So he got together with another engineer during an infra hack and wrote the first version of [Warp Speed Data Transfer](https://github.com/facebook/wdt), an embeddable library and command line tool for transferring data between two systems as fast as possible. To do this, input is cut into blocks and sent in parallel over multiple TCP paths with different source and destination ports. They push into the socket without waiting for good transfers, and if one block transfer fails, they’ll retry it on any available connection. We open-sourced WDT this year with new features and improvements coming regularly, like encryption in the latest release. At Facebook, WDT now does transfers at more than 500 GB/s.

## Securing email communications from Facebook

![](https://engineering.fb.com/wp-content/uploads/2015/12/GN84vgAtR1GBeokCANHq7m8AAAAAbj0JAAAD.png)

We want people to have secure connections to the Facebook site. It’s why we implemented HTTPS with HTTP strict transport security (HSTS) across our site and provide a Tor .onion site for those who want an extra layer of security. At a hackathon, our team began envisioning a new feature to enable people to add their OpenPGP public key to their profiles, and by June of this year, we [rolled out](https://fb.facebook.com/notes/protect-the-graph/securing-email-communications-from-facebook/1611941762379302) a dedicated profile field for including an OpenPGP public key with a corresponding privacy option. We also included the option for people to receive encrypted notifications from Facebook. Our outbound messages are signed using our own key, allowing end-to-end encrypted notification emails sent from Facebook to your preferred email accounts.

All of these features and tools exist thanks to the dedication and passion our teams have for what they build. But this is only a snapshot of what we’ve done. With a new slate of hackathons coming up, we can’t wait to see the innovations that 2016 will bring. Happy hacking!
