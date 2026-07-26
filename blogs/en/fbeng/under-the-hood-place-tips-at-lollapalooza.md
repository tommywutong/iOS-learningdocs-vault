---
title: 'Under the hood: Place Tips at Lollapalooza'
source: Meta Engineering — iOS
source_key: fbeng
source_url: 'https://engineering.fb.com/2015/08/18/ios/under-the-hood-place-tips-at-lollapalooza/'
original_language: en
published: 2015-08-18
status: active
license: © Meta → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:f27798e389c0ee36'
translated: false
---

> 原文：[Under the hood: Place Tips at Lollapalooza](https://engineering.fb.com/2015/08/18/ios/under-the-hood-place-tips-at-lollapalooza/)　·　Meta Engineering — iOS

If you were lucky enough to be in Chicago last month, or if you’re simply a concert enthusiast, you might have noticed a unique experience at Lollapalooza 2015 — enabled by our New York City-based Place Tips team.

[Place Tips](http://newsroom.fb.com/news/2015/01/introducing-place-tips-in-news-feed/) connect your Facebook experience with the physical world around you. They surface social content like posts, photos, and reviews from your friends about the places you visit. Place Tips also contain information about businesses — for example, contact info, menu items, and upcoming events. After an initial rollout in January with select partners in New York City, Place Tips are now rolling out across the United States.

![](https://engineering.fb.com/wp-content/uploads/2015/08/GGYHrgBSqpmCDZ8BAN8jQEUAAAAAbj0JAAAB.jpg)

<sub>Facebook Bluetooth® beacons make sure customers see the right Place Tips for their location.</sub>

We partnered with Lollapalooza to build specialized Place Tips that enriched the experience for people at the festival in Chicago and also brought it to life for those following from home via Facebook. At Lollapalooza, one could enter Place Tips from atop News Feed. We surfaced information like popular public photos, stage lineups, and area maps. We also curated posts by organizers, bands, celebrities, and friends at the festival. All U.S. users — whether they were at the festival or not — could access the experience by searching for “Lollapalooza” in the Facebook app.

![](https://engineering.fb.com/wp-content/uploads/2015/08/GHsXrgDkE3tVfqkCAKB1R3cAAAAAbj0JAAAB.jpg)

The Lollapalooza implementation of Place Tips started during a designer’s hackamonth (Facebook’s work exchange program in which employees can try out a new project for a month) and moved quickly from design to implementation. The infrastructure that powers Place Tips — a Facebook-built rendering framework, designed and implemented out of our New York City office — made the quick turnaround possible.

The team that built this framework was challenged with how to display an unlimited feed of varied information via cards across our mobile applications. The product was somewhat similar to News Feed in concept, but these cards needed to display arbitrary aggregations of data — for example, friends’ photos at a place or previous posts with a particular friend. Uniquely, the cards needed both flexible and consistent rendering across all our apps and app versions. This led to a system where the server has a very high level of control of the client rendering.

This platform currently powers several Facebook products, including Place Tips, across our apps and mobile site. At a high level, it is a framework that allows a server to control native client rendering using pre-existing templates on the clients. The interesting part is mapping card data to the rendering when the templates could vary drastically — in availability and in behavior — depending on client and version.

To handle this, the platform has template identifiers called styles. Each style is an unbreakable contract between the client and the server that specifies the rendering, interaction behavior, and expected data for a template. Style templates are built into the client apps; to support a new design, we simply need to build a new style template into the next client build of our app. With each request, the client informs the server of which styles it is capable of handling; the server will respond with cards that use only supported styles. This eliminates any guesswork or special-cased app version logic and thus allows the server to cleanly and predictably control native client rendering for all apps and versions.

Let’s look at an example. Suppose we wanted Place Tips for Lollapalooza to show Upcoming Events:

![](https://engineering.fb.com/wp-content/uploads/2015/08/GEg8mwBSaB48BsgFADAq5joAAAAAbj0JAAAB.jpg)

This card is configured using a template style that arranges three sub-templates: a header (the icon and message at the top), attachments (the three events), and a footer action (the See All button).

Since these sub-templates are abstractly composed, we can mix and match anything into these positions. For example, it would be trivial to replace the footer with an action to open a URL, the attachments with a grid of photos, or the header with a map.

This is roughly what the data response from the server to the client for this card looks like:

```javascript
{
    style_type: “STORY”,
    header: {
      style_type: “ICON_MESSAGE”,
      icon: …,
      message: “Upcoming Events”,
    },
    attachments: {
      style_type: “PROFILE_BLOCKS”,
      nodes: [
        {profile: …},
        {profile: …},
        {profile: …},
      ],
    },
    footer_actions: [
      {
        style_type: “SEE_ALL_PROFILES”,
        message: “See All”,
      }
    ],
  }
```

To turn this response into the card, the client simply needs to support existing template implementations for each style type. For example, “STORY,” “ICON_MESSAGE,” “PROFILE_BLOCKS,” and “SEE_ALL_PROFILES” have their own independent implementation, each of which handles specific data payload. There is very little product-specific logic at the card level, which makes the client layer very thin. Thus, the platform lets us quickly build and iterate most of our logic on the server and immediately turn that into consistent natively rendered UI across all clients.

The Lollapalooza project in particular benefited from this platform in a few ways:

1. Many of the renderings we wanted to use for our custom cards were already implemented on the clients as generic styles. For example, our custom Now Playing unit also uses the aforementioned PROFILE_BLOCKS attachment style to render each band. This meant that building that unit required almost zero client work.
2. Because of our mobile release cycle, the last client release to go public before Lollapalooza was cut at the end of June. This means we were limited to building on the server for the entire month leading up to Lollapalooza. Luckily, this is the workflow at which this platform excels.
3. All the new styles we built for Lollapalooza cards are usable by any new client. This will enable us to reuse our work to ship even more custom Place Tips experiences, faster!

We’re excited about the opportunity for Place Tips to grow and support more advanced experiences and place types. Rapid development frameworks and awesome new technologies like Facebook Bluetooth® beacons make it possible for our team to quickly execute on strategies to make Place Tips more engaging and useful in more places.

_Huge thanks go to Jonathan Hull for helping us drive this partnership, and to Henry Zhang for helping us write about the platform powering Place Tips!_
