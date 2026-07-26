---
title: Building Facebook Messenger
source: Meta Engineering — iOS
source_key: fbeng
source_url: 'https://engineering.fb.com/2011/08/12/android/building-facebook-messenger/'
original_language: en
published: 2011-08-12
status: active
license: © Meta → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:f0f795e695a4174e'
translated: false
---

> 原文：[Building Facebook Messenger](https://engineering.fb.com/2011/08/12/android/building-facebook-messenger/)　·　Meta Engineering — iOS

![](https://engineering.fb.com/wp-content/uploads/2011/08/Fnn_DAAe9rVpk9ABAEVn_T1uPQkAAAE.jpg)

On Tuesday we introduced Facebook Messenger, a new stand-alone messaging app that enables people to send messages 1-on-1 or to groups of friends. I joined Facebook five months ago with my two other co-founders, Ben Davenport and Jon Perlow, who worked with me to build a group messaging application called Beluga. Our new app, Facebook Messenger, represents the best of both worlds — it combines the ease and simplicity of Beluga with the scale and integration of Facebook Messages.

I had a couple of life experiences that led me to create Beluga. For instance, a group of us were meeting up for a movie at the Tribeca Film Festival in New York City but the hour leading up the movie was a total communication failure. I had a friend texting to tell me another friend was running late. We were saving a ticket for another friend, but he decided not to come and no one knew. It wasn’t until hours later when I returned home that I saw an IM from the friend who was late and an email from the friend who had bailed. We think Facebook Messenger’s ability to integrate chat, text messages and email helps solve this exact problem.

We started building Beluga as a tool for group coordination but we discovered that enabling lightweight, private, instant communication can change the way a group of people connect with each other much more broadly. Instead of emailing out the vacation photos weeks after a trip, people start to share more in the moment. The instant nature of the messages enables group conversations to start up spontaneously and bridges the gap between people connecting from their computers and those on mobile devices. Messenger’s integration with Facebook Chat now makes that scenario a reality.

## Diving into New Waters

When we joined Facebook and started to build Messenger, our first technical challenge was learning the entire infrastructure stack for Facebook Messages. It was great to be building on a scalable platform that had already launched to hundreds of millions of users, but the system contained certain assumptions and design decisions that didn’t always quite mesh with the product we wanted to build. Luckily, our new colleagues were also excited about the vision for Messenger and joined the effort to make sure the system could do what we needed.

One of the problems we experienced was long latency when sending a message. The method we were using to send was reliable but slow, and there were limitations on how much we could improve it. With just a few weeks until launch, we ended up building a new mechanism that maintains a persistent connection to our servers. To do this without killing battery life, we used a protocol called MQTT that we had experimented with in Beluga. MQTT is specifically designed for applications like sending telemetry data to and from space probes, so it is designed to use bandwidth and batteries sparingly. By maintaining an MQTT connection and routing messages through our chat pipeline, we were able to often achieve phone-to-phone delivery in the hundreds of milliseconds, rather than multiple seconds.

Other than performance and the system-integration issues, the biggest challenges were really product decisions around how to seamlessly integrate different channels of communication with differing user expectations. People communicate differently on chat than they do on the phone — for instance, you might start a chat conversation with “Hey, you there?” but you probably wouldn’t send that as a text, because of course the person’s there! You can try to make the system smart and do the “right” thing in lots of different cases, but if you make the rules too complex, it may feel too “magical” and not like a reliable communication channel.

To ensure that Messenger felt right, we constantly tested different designs with our colleagues. As we rolled out the builds to more and more people within Facebook, we got even more feedback and learned where our assumptions were differing from reality. We’re so excited to finally launch Facebook Messenger to the public — and we look forward to getting feedback from millions more people.

We hope you enjoy using Facebook Messenger as much as we enjoyed building it!

_Lucy Zhang, a software engineer, looks forward to never having a hard time coordinating movie night again._
