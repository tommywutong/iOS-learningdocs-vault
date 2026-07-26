---
title: One Mobile Site to Serve Thousands of Phones
source: Meta Engineering — iOS
source_key: fbeng
source_url: 'https://engineering.fb.com/2011/03/31/android/one-mobile-site-to-serve-thousands-of-phones/'
original_language: en
published: 2011-03-31
status: active
license: © Meta → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:9e5c0c3cae4e8657'
translated: false
---

> 原文：[One Mobile Site to Serve Thousands of Phones](https://engineering.fb.com/2011/03/31/android/one-mobile-site-to-serve-thousands-of-phones/)　·　Meta Engineering — iOS

![](https://engineering.fb.com/wp-content/uploads/2011/03/FoL_DAB3tVKeYtoBACGRth1uPQkAAAE.jpg)Building for the mobile Web is a big challenge. You have to plan for thousands of different devices with varying capabilities, screen sizes, keyboards, CSS and JavaScript support, underlying technologies, and browser bugs.

Today we’re excited to start rolling out a major upgrade to m.facebook.com that delivers the best possible mobile Web experience no matter what device you’re using.

Previously, we solved this problem by building multiple versions of mobile Facebook: m.facebook.com for less feature-rich mobile devices and touch.facebook.com for touch devices.

There are two major problems with this approach:

1. We were limited by the lowest common denominator for each site. We couldn’t use JavaScript and had device specific file size limitations on m.facebook.com. Supporting a wide array of touch phones of varying quality on touch.facebook.com limited our ability to use modern CSS and JavaScript APIs.
2. Every time we launched a new feature, we had to build it multiple times across different code bases: once for facebook.com, then again for m.facebook.com, touch.facebook.com, and in native applications as well. Honestly, we weren’t very good at doing this, so certain features were missing on different devices.

With the new m.facebook.com, users with high-end touch devices will see a rich touch-friendly interface; for users with feature phones, the site will look and work great.

Every device uses the same framework. This way we can move even faster and build new features just once for every mobile device. It also means that everyone can access the same features, whether writing messages or checking into Places. There will no longer be a difference between m.facebook.com and touch.facebook.com, we’ll automatically serve you the best version of the site for your device.

## What’s Under the Hood

Our new site is powered by a UI framework based on XHP, Javelin, and WURFL, a detailed database mapping user agents to device capabilities. This enables us to very precisely target experiences and features to thousands of different devices.

For example, on the latest WebKit based devices, like iPhone and Android, we use CSS3 and vendor-specific rules for display and animation as well as some of the new JavaScript APIs included in HTML5 for local caching and history management. For example, to animate out a deleted comment, all it takes is:

`.deletable.deleting {</p><p>-webkit-transition: translateX(-200%);</p><p>}`

For other devices we can target specific issues. For example, some devices don’t have keyboards, or have limited means of navigating a page, tiny screens, or crippling browser bugs. We can customize our site in each case to deal with these issues and provide the best possible experience to everyone.

This mobile UI framework allows engineers to focus on building their product and not on supporting device edge cases. Rather than directly writing HTML, CSS, and JavaScript, our product engineers write XHP and use these mobile components to build new features. Take for example a button component, rendered on a device that lacks CSS support, a device with very basic CSS support, and on a high resolution touch device:

![](https://engineering.fb.com/wp-content/uploads/2011/03/Fn3_DABgkAFFAv8EAM2ikXxuPQkAAAE.jpg)

To render this button, all an engineer needs to write is \<m:button label=”Share” /\> and XHP takes care of the rest, rendering it correctly based on the device.

We think it’s important to provide an excellent mobile Web experience. Now, whenever we launch new features on the mobile site, they’ll be available on any mobile browser, presented in the best possible experience. We’re excited to roll out the new m.facebook.com site to everyone over the next few weeks.

**Update: Some of you asked about 0.facebook.com. That site also uses the same codebase as m.facebook.com.**

_Lee Byron, a product designer, is looking forward to deleting tens of thousands of lines of old mobile site code._
