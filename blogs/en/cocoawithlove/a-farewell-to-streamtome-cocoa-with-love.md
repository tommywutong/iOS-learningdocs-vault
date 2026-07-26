---
title: 'A Farewell to StreamToMe | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/blog/a-farewell-to-streamtome.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:e7afc7c6e190c7d6'
translated: false
---

> 原文：[A Farewell to StreamToMe | Cocoa with Love](https://www.cocoawithlove.com/blog/a-farewell-to-streamtome.html)　·　Cocoa with Love (Matt Gallagher)

Last night, I removed my app StreamToMe from the iOS and Mac App Stores, after 9 years on sale. It’s a deeply sad experience for me – like I’ve lost a faithful pet – so I wanted to write a quick retrospective.

This will be a discussion about what it’s like to have an app on the App Store that is financially successful but eternally problematic from a support and maintenance perspective. I’ll talk about why I lost interest in StreamToMe and, at times, deliberately neglected my own product. Finally, I’ll talk about why I’ve decided to simply pull it from the store – not open source it or sell it – even though it still works for many people.

> **Predicting the future is hard**: It’s been 8 months since my previous article when I said I would release CwlViews “in a few weeks”. I’ve been busy with other things and have barely touched CwlViews in that time. Oops. In more-organized news, the book I was writing with Chris Eidhof and Florian Kugler, [App Architecture in Swift](https://www.objc.io/books/app-architecture/), launched in May and you can [get the finished book from objc.io](https://www.objc.io/books/app-architecture/).

---

## StreamToMe

StreamToMe was a streaming music, video and photos app for iOS and macOS that I wrote and distributed via the respective App Stores.

![Some StreamToMe promotional screenshots from the iOS 6 era. ‘member Aperture?](https://www.cocoawithlove.com/assets/blog/streamtome_promo.jpg)

<sub>Some StreamToMe promotional screenshots from the iOS 6 era. 'member Aperture?</sub>

StreamToMe relied on a lightweight streaming server, named ServeToMe, to stream media from the user’s computer to the device in Apple’s HTTP Live Streaming format over the local network or internet. The ServeToMe server performed live transcoding (conversion to the required format) or live remuxing (moving to the streaming container without transcoding) as needed, including bitrate changes to support variable network conditions.

StreamToMe + ServeToMe competed with AirVideo, Plex, AirMediaCenter and numerous others that also implement Apple’s HTTP Live Streaming for personal media streaming. StreamToMe had low overheads, low latency, highly robust seeking and support for weird formats and was better at music and photo handling than the more video-focussed players.

## From prototype to iPad

I wrote the first version of StreamToMe in June 2009, shortly after Apple announced HTTP Live Streaming at WWDC. It took a week to write a prototype and about a month to prepare for release. The first version had no thumbnails, no playlists, no ability to seek within a file. Despite the lack of features, it sold a few copies – indicating a desire for something in its space – so I added the most obviously missing features in the next couple months and it sold more copies.

Then Apple announced the iPad. I didn’t own an iPad – nor did I have any intention of getting one – but I hastily updated StreamToMe to handle the iPad in the simulator, called it version 2.0 and [defiantly announced day 1 availability on my blog](https://www.cocoawithlove.com/2010/04/streamtome-is-available-for-ipad.html). A few websites picked up my announcement and sales suddenly took off.

The result was a blessing and a disaster.

Bugs in my Bonjour handling for the iPad release meant that anyone on an IPv6 capable network couldn’t discover their server. A handful of other issues in my hasty release led to 2000 support emails in single day. I did nothing but fight fires for the next couple months.

Despite the bugs though, StreamToMe continued to sell.

## Trying to please people makes things worse

I fixed the bugs but now I had a different problem: customers, lots of them, all wanting features. If they all wanted the _same_ features, there might not be a problem but I quickly learned that media is a deeply personal experience and everyone wants to experience it a different way.

Ever wondered why all the major media player are a weird kitchen-sink of features bolted onto each other? Media players are a product-space where everyone uses a tiny slice of the features but no two users use the same slice of features and the entire space is really, really broad.

One user plays only TV shows. Another plays only movies. Another plays only lossless audio in continuous albums. Another plays only individual songs. Another plays only audiobooks. Another plays only content they’ve ripped for themselves. One of them stores all their files in a single folder. One of them stores every file in their own folder. One stores all the files in different folders but aliases in a single folder. One stores them over a number of NAS drives. One of them zips all media into archives and expects the media player to perform unzipping on-the-fly. One of them plays content from ISO format disc images. One of them uses an old media encoder that sets the wrong H.264 profile. One of them uses external subtitle files for each movie. One of them uses external thumbnail files for each song. One of them uses separate album artwork files in each folder. Most have a few files in formats you haven’t heard about in years. One of them uses AIFF files. One of them uses Real Media files. One of them uses WTV files.

There is no “common” user. Analytics and data gathering look like random noise. You could probably spend an eternity adding features to a media player and a significant percentage of users would still feel left out because you’ve omitted _their_ favorite feature.

Like an idiot, I scrambled to add as many features as I could. Unfortunately, I ended up with a huge swath of features that _I_ didn’t really use and the app stopped feeling like it properly catered to me. For something that started as a personal passion project, I was starting to feel like an dispassionate observer, rather than a passionate participant.

And as the feature set grew, so did a different class of maintenance problems and these were not simple bugs that could be fixed.

## Never write a multi-faceted integration project

You can fix bugs. You can write unit tests, regression tests and integration tests that run on your own equipment. But if your product is heavily reliant on integration with the _user’s_ environment then you’re in trouble.

Streaming media players are usually a fairly thin I/O, routing and scheduling layer between the following systems:

1. user’s media collection, including formats, encodings and folder hierarchies
2. user’s storage systems (NAS devices, external drives, internal storage)
3. a media transcoder (ServeToMe used a custom build of ffmpeg and Apple’s AVFoundation)
4. server OS network services (HTTP server and network advertising)
5. server network (including WiFi/internet router, UPnP-IGD, network topology)
6. client network services (network provider, reachability, network discovery)
7. client media player services (HLS, background audio, picture-in-picture)
8. client network (possibly home WiFi, possibly cellular provider, possibly third-party WiFi)
9. client ancillary services (Apple TVs, Chromecasts, smart TVs)

The streaming media player usually bundles the media transcoder (3) but has no control over the rest; they’re black boxes and when they don’t do what you expect, they often fail silently: no logs, no feedback; nothing. They all update regularly, are replaced by new devices regularly, are all subject to misconfiguration, are sometimes actively hostile towards personal media streaming, regularly have APIs that are complex enough to be impossible to fully support, and will all result in the user blaming the streaming media player if anything goes wrong.

Everything about home networking is a mess. There’s a vast set of reasons why two devices on the same home network cannot see each other (IP subnets, NAT, firewalls, VPN, blocked multicasts) and spending your days explaining this via email to purchasers of a $3 app is not rewarding at all.

Then there’s everything about Windows. For a longtime Mac user like me, everything about Windows feels like torture. Ever tried opening a socket connection on a Windows computer? Anti-virus software will intercept any socket connection that starts with “GET” and silently discard the traffic if they’re not happy. Have you ever tried to write a Windows installer for a Windows service? Writing the installer can literally double the development work for the overall project. Even once you get it working on a normal computer, you’ll get a handful of failed installs a week due to corrupted registries, broken .NET installations or mysterious security settings.

And the problem with larger integration projects is that every day, there are new components be added or removed from the environment of your users. Services you rely upon are updated and break your program. People acquire new kinds of devices and expect them to integrate. Maintaining integration with a perpetually changing set of environments across the iOS app, the macOS app, the macOS server and the Window server sapped the energy out of me. I _wanted_ StreamToMe to fade away so the support effort would fade.

### Special mention: interfering network providers

Since October last year, T-Mobile have intercepted every attempted StreamToMe audio stream and blocked the connection. Why? I suspect they’re trying to apply bitrate shaping to reduce the bitrate of traffic but they are making incorrect assumptions about the nature of StreamToMe leading to total packet loss. The effect is that I get a constant stream of customers complaining that StreamToMe doesn’t work and I need to unravel the fact that the underlying complaint is “won’t stream over T-Mobile’s network”. T-Mobile claimed that StreamToMe doesn’t support IPv6 which is a puzzling expectation for connections that are nearly always IPv4 and I wasted a couple weeks with some of my customers trialling different IPv6 improvements to the app and server without success. In any case, it’s infuriating that a network on the opposite side of the world to me expects me to alter my app to support their specific approach to interfering with customer network traffic.

I would route all traffic over HTTPS to prevent network interference but that’s just a different game that is rigged against home servers like ServeToMe. Apple’s HTTP live streaming won’t accept peer certificates (home servers can’t use typical certificate validation) and running a client side proxy to tunnel over TLS causes a huge number of problems on iOS for background apps since all your network listen sockets break during backgrounding.

## Fading away

At StreamToMe’s peak, it sold nearly 10,000 units per month. It was never free or priced on the bottom couple tiers so it was making good money for a single-developer app with low overheads.

The following graph shows StreamToMe’s lifetime unit sales. Most of the peaks coincide with the sales of new iOS devices. The three most dramatic upticks are the release of the original iPad, the Apple TV 2 and the iPad 2 but you can also see Apple’s yearly iOS update cycle in the tail.

![StreamToMe units sold per month, over its lifetime](https://www.cocoawithlove.com/assets/blog/streamtome_units.png)

<sub>StreamToMe units sold per month, over its lifetime</sub>

The good sales I had between 2010 and 2013 were significantly helped by a flurry of new devices. These spikes of additional sales are dependent on being ready when new product categories appear. There would certainly have been another bump in 2015 had I actually released a tvOS version of StreamToMe for the Apple TV 4 but I was busy making excuses for why I couldn’t do that.

## Denial

For years, I’ve been telling myself that I would put out a new version that added long-promised features. That I would finally put out a tvOS version. That I would finally overhaul the clunky interface. That I would update to Swift.

I told myself that the sales would recover and StreamToMe would feel like a new app again.

I told myself that these updates were waiting until I had the free time.

But then I had the time available and I worked on anything else except StreamToMe. Given free time, I wanted to work on personal projects that excited me. StreamToMe was difficult and grueling, not just because it was a nightmare of support and integration but also because it had ceased to be a personal project.

## Media landscape changes

In 2009, my media consumption flow went like this:

1. Buy DVDs and CDs
2. Extract them to my computer
3. Stream them to myself using StreamToMe

I used StreamToMe in this way every day. Recently though, I haven’t used it in months.

I haven’t bought a physical CD or DVD in years. Netflix, Hulu, Amazon Prime, Twitch, YouTube and Apple Music have changed where media is stored but almost as big is the fact that the surge in content creation and distribution has completely changed the breadth of available media. With the scarcity equation shifted, I don’t find myself returning to previous purchases that I thought I would enjoy forever.

I don’t watch my own DVDs and BluRays. In a couple years, I might not even own a physical media player. I listen to my music less. I’ve stopped watching TV and stopped listening to the radio.

While many consumers haven’t changed as dramatically as I have, even if StreamToMe was updated and feature-rich, I don’t think the market for StreamToMe is anywhere near what it was 10 years ago.

## Taking it down

100-200 units sold per month over the last year was enough to justify working on it one day per month but StreamToMe invariably took 2 or 3 days of my time each month. It wasn’t exactly a loss-making in raw terms but as an opportunity cost, I could do better things with my time.

A deciding factor ended up being problems with the ServeToMe server on Windows. ServeToMe depended upon iTunes on Windows for a number of services and iTunes’ recent move to the Window Store broke these dependencies and hence broke StreamToMe for roughly a third of my customers.

Dependencies are replaceable and I could spend a week or two replacing them but I don’t want to devote the time. I could official withdraw support for Windows from the app but I know from experience that it would be replaced by continual questions about whether there was a Windows server available. And even if I did all that, it still wouldn’t address the hundreds of other minor unfixed issues, as well as major ones like cellular carrier interference. And beyond the bugs, the app still looks dated, still contains code written during the iPhone OS 2 era and still has never been updated to ARC, much less autolayout or a thousand other iOS improvements. The server is much newer after a major rewrite in 2013 but is written in C++11 – a language I haven’t used for any new projects in the last 5 years – so it’s just another project that feels like I’m no longer personally involved.

According to App Store analytics, there are over 30,000 active users of StreamToMe for whom these issues are not deal-breakers (that represents roughly 10% of the customers who have ever bought the app). The app itself will continue to work for these people, even though I’ve taken it off the App Store – with luck, it will continue to work for years to come.

30,000 is a non-trivial base of active users but I don’t think it would be easy for anyone to adopt StreamToMe and grow that base. The code, the features and everything else about the app is just a mess.

## Conclusion

I’ve spent a lot of this article complaining about StreamToMe but the truth is that I’m really sad to take it off of the App Store. I continued to maintain it this long because I’m emotionally attached to it. StreamToMe remains the only successful product that I’ve launched entirely on my own. For around 4 years, it was my primary source of income.

StreamToMe would certainly be more successful right now if I had maintained it passionately but it took me a long time to realize that I lost interest in it. Regardless of my stewardship, I think the market has changed and I think the overall downward trend would be the same in any case. People are no longer buying their first iPad and looking to buy hundreds of apps for it in a flurry of excitement. Media consumption habits have changed. My habits have changed.

> **StreamToMe users**: Even though it’s removed from sale, previous purchasers of StreamToMe can still redownload the latest StreamToMe 3.18 from the Purchases screen in the App Store app. [ServeToMe is still available](https://zqueue.com/servetome/) from its webpage. The StreamToMe app is tested and fully functional on iOS 12.
