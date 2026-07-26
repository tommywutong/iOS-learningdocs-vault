---
title: 'Co-experiences: Hanging out in the digital living room'
source: Meta Engineering — iOS
source_key: fbeng
source_url: 'https://engineering.fb.com/2020/12/16/android/co-experiences/'
original_language: en
published: 2020-12-16
status: active
license: © Meta → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:5f640b505e8b9fc4'
translated: false
---

> 原文：[Co-experiences: Hanging out in the digital living room](https://engineering.fb.com/2020/12/16/android/co-experiences/)　·　Meta Engineering — iOS

In the spring of 2019 — a full year before the COVID-19 pandemic caused the entire world to turn our living rooms into offices, schools, and gathering places — Mark Zuckerberg shared a plan to create [the digital equivalent of the living room](https://www.facebook.com/notes/mark-zuckerberg/a-privacy-focused-vision-for-social-networking/10156700570096634/), where people could connect and hang out together. That work was already underway early this year, when countries began to implement stay-at-home measures. As people began moving online [at a volume the internet could barely support](https://www.facebook.com/atscaleevents/videos/1054336998415512), we realized that plan needed to become a reality as quickly as possible. We shifted plans to accelerate work on co-experiences, a suite of digital shared experiences people can enjoy together.

What do we mean by co-experiences? Think about those moments in your own living room when you feel closer to friends and family. Those probably include sitting down for a long chat, but also experiences like watching sports or an emotional season finale on TV, sharing music by a new band you’re into, or sharing old photos and the stories behind them. People bond over shared experiences, and we want to make video chat on Messenger and Instagram a space where people can share these same types of experiences in their virtual living rooms. To that end, we’ve already rolled out [Messenger Rooms](https://about.fb.com/news/2020/04/introducing-messenger-rooms/), [cross-app communication](https://about.fb.com/news/2020/09/new-messaging-features-for-instagram/) between Messenger and Instagram, as well as screen sharing, 360 backgrounds, and AR lighting. Our latest addition is [Watch Together](https://messengernews.fb.com/2020/09/14/feel-together-messenger-introduces-watch-together/), which allows people to watch shows and videos together on their devices.

To accomplish this, we needed to operate like a startup. Even though Messenger is an established product, we were building a new experience from scratch and had to make sure we were building something that people wanted and would actually use. It needed to be valuable and actually make video chatting more fun. This meant optimizing for learning, listening, and adapting. We challenged our assumptions early and often, and moved quickly. We also had to look at video calling as a whole in order to truly make this a hangout experience. We had to completely redesign the video call experience to create a natural, comfortable space for people to hang out by making the interface simple and intuitive enough that anyone could jump in quickly and find the options they need.

Along the way, we built new platforms and solved the hard technical problems that come with building synchronous experiences, so that everyone can see the same thing at the same time no matter which device or network they’re on. This presented additional technical challenges when done at Facebook scale. For Watch Together, we needed to build a brand-new state synchronization platform over our video calling stack, fine-tune audio to optimize mixing and reduce echo, and build personalized video recommendation models, to name just a few.

## **Product engineering challenges**

We wanted to think of Watch Together as its own product and have a strong product/market fit — a product that people would not only use but also want to share with others and use when hanging out. We knew that we probably wouldn’t get things right on the first attempt, so we were prepared for trial and error and to learn quickly.

To optimize the features we were building and make sure it was the experience people wanted, we drew on both quantitative signals from our instrumentation and qualitative signals in the form of research feedback from real people using Watch Together: We ran numerous research studies and maintained a product influencer community with a diverse set of users. Thanks to feedback from these users, we completely redesigned the video calling experience to create an intuitive space for the things people do together. We designed a new swipe-up drawer; simplified the flows for selecting videos; and tweaked and iterated on ranking, the categories, and groupings and content available. We also tested multiple different call layouts to optimize the viewing experience so that on a person’s device, they see a comfortable balance between the video being watched and their view of the other participants. We also heard the importance of audio balance, echo canceling, and independent volume control for the video, each of which we brought into the final experience.

![](https://engineering.fb.com/wp-content/uploads/2020/12/Watch-Together-Experience.jpg)

We were able to draw on strong quantitative signals provided by instrumentation to understand what is happening and how the product is being used, and to validate what matches expectations and what doesn’t. We leveraged tools like funnel analysis and drop rates, ranking performance, UX interactions, participation, and retention J-curves to inform where Watch Together needed improvement. We ran hundreds of individual experiments to get to the experience that exists today. All these UX patterns were built in a generic way so that we can leverage them in new experiences in the future.

## **Building a synchronous experience**

One of the biggest challenges with co-experiences was enabling real-time, high-precision synchronization across various apps and devices to ensure that everyone is watching the same thing at the same time. In addition, we needed to build in control reliability to ensure that playback controls such as play, pause, rewind, or fast-forward occur simultaneously across devices. We also needed the audio stream from videos and real-time calls to be well synchronized so that people aren’t dealing with lags and overlaps.

To address this, we built our own state synchronization platform (state sync), which utilizes our multiway infrastructure (the servers we use to host individual and group calls) for real-time resolution of client-side state for all devices in a call. This is a significant improvement over previous technology. Prior to state sync, engineers jumped through many hoops to synchronize state between calls. The most common method was to use data messages, sending information to all clients for client-side resolution on each respective device. This led to individual Android, iOS, and web implementations of how to calculate the final state. But this strategy often led to inconsistencies between clients, and it was not always as reliable as we’d like. With state sync, we can support web, Android, and iOS across both Messenger and Instagram, leveraging our own calling infrastructure.

We defined [Thrift](https://github.com/facebook/fbthrift) structures for both the input (the messages to be received on the server) and the output (the expected resolved output structure from the server). From there, state sync can be broken down into three main parts: subscription, input, and resolution.

1. To begin sending and receiving state, the client must first subscribe to the state sync topic it wishes to interface with. This ensures we don’t send Watch Together data to a client that doesn’t support it.
2. In the input stage, we use the predefined Thrift structures to send formatted messages for resolution. We use a snapshot-based model, such that the latest input from a client is the one used by the resolver, in case multiple inputs are sent in quick succession.
3. All clients in a call hit the same server-side resolver, centralizing all inputs through the same resolver logic, eliminating the need for multiple message processing units on each client. This is another big benefit of state sync: We save processing power on the clients and maintain consistency.

State sync was built as a new, generic platform designed so that we can leverage it for future experiences. Today, it powers not only Watch Together but also other scenarios, such as screen-sharing moderation in Messenger Rooms, and [Rooms to Live](https://about.fb.com/news/2020/07/go-live-on-facebook-from-messenger-rooms/). The platform is also built with [cross-app communication](https://about.fb.com/news/2020/09/privacy-matters-cross-app-communication/) in mind, enabling friends and family to connect via Watch Together or any of the new [Messenger experiences on Instagram](https://about.fb.com/news/2020/11/new-messaging-features-on-instagram-and-messenger/).

## **The future of co-experiences**

Thanks to the work we’ve done to understand hangouts, build generic UX components that can be reused, and develop our state sync platform, we have a solid foundation in place on top of which we can continue to grow experiences like Watch Together, as well as build new co-experiences.

These tools will allow us to scale over time to support more experiences and to support them across all of our apps and services. In the future, we’d love to see a world where people could use Messenger and Instagram as a virtual living room, to talk, share, watch, and much more. We are just getting started and are excited for the journey ahead.
