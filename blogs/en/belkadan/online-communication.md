---
title: Online Communication
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2024/01/Online-Communication/'
original_language: en
published: 2024-01-20
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:cb2774a595f3ae43'
translated: false
---

> 原文：[Online Communication](https://belkadan.com/blog/2024/01/Online-Communication/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [The Biggest Smallest PNG](https://belkadan.com/blog/2024/01/The-Biggest-Smallest-PNG/)

[Run-time Polymorphism in Swift](https://belkadan.com/blog/2024/04/Run-time-Polymorphism-in-Swift/) »

« [Soft Orders of Magnitude](https://belkadan.com/blog/2023/10/Soft-Orders-of-Magnitude/?tag=user-experience)

## [Online Communication](#)

I’ve been thinking about different sorts of internet communities, and how they can feel pretty different based on their primary medium. By “community” I mean a group you specifically choose to be part of, a group where you can recognize other “regulars”…a group that feels like a “place” that feels comfortable. Sometimes this is going to be a closed group of friends; other times it’s friends-of-friends that come and go; still others it’s people oriented around a common interest. But as far as text-based online media go, I think they fit into five main categories: **Messaging**, **Chat Rooms**, **Livestream Chat**, **Comment Threads**, and **Forums**.

|  | Examples | Sync or Async? | Send with | Grouped into… |
|---|---|---|---|---|
| ![](https://belkadan.com/blog/2024/01/Online-Communication/1-messaging.svg) **Messaging** | IM, DMs, SMS, Signal | Sync preferred | Enter | “Groups” (or individual contacts) |
| ![](https://belkadan.com/blog/2024/01/Online-Communication/2-chat-room.svg) **Chat Rooms** | IRC, Discord, Slack | Sync preferred | Enter | “Channels” in a “Server” |
| ![](https://belkadan.com/blog/2024/01/Online-Communication/3-livestream-chat.svg) **Livestream Chat** | Twitch, YouTube | Sync only | Enter | “Videos” in a “Channel” |
| ![](https://belkadan.com/blog/2024/01/Online-Communication/4-comment-threads.svg) **Comment Threads** | Reddit, Facebook, Instagram, AO3, even Twitter and Mastodon, plus some websites | Async | Explicit action | Posts or topics within “Categories” or “Accounts” |
| ![](https://belkadan.com/blog/2024/01/Online-Communication/5-forums.svg) **Forums** | Email, Discourse, “classic” 00s forums, newsgroups | Async | Explicit action | Threads in “Categories” or “Groups” |

**Messaging** we’re all pretty familiar with, but it doesn’t necessarily scale to “communities”, especially when using the “fun” chat bubble rendering that can take up a fair bit of extra space. Not having categories is the biggest thing for me, though—you end up having several interleaved conversations in a single group, or making several topic-based groups with the same people.

**Chat rooms** are my current favorite of these five, being in both small, medium, and fairly large Discord servers and feeling the most connection there. (My organizationally-minded brain likes being able to have multiple channels, too.) While they can be a bit chaotic, they provide flexibility in choosing which topics to participate in, while still having that live back-and-forth that allows conversations to build on the ideas of everyone involved. I’m not saying this _can’t_ happen in another medium, but it’s rarer.

**Livestream chat** is an interesting category. I originally had it as a kind of chat room, but I think it’s sufficiently different because there’s _always_ a non-textual component: the host of the stream, who’s more likely to respond to messages out loud than to take the time to type them like everyone else. But people do think of these as communities, and get to know each other as regulars. They’re unique in that messages are always going to be attached via timestamp to the video, and anyone who wants to read them later has to go through the video to do so.

**Comment threads** _usually_ have a tree structure, or at least a single level of indentation, to distinguish replies from “top-level posts”. But the main thing that distinguishes a comment thread is that there’s a _thing being commented on,_ whether that’s a thing on the website itself or a link out to somewhere else. Twitter-likes are special here in that the thing being commented on looks basically the same as a comment (and they often ecshew the hierarchical presentation), but I’m convinced they still fit in this category. The livestream chats, on the other hand, don’t inherently have any structure (even if they sometimes have reply indicators) and require live participation, while comment threads are expected to be asynchronous.

**Forums** actually feel the most heavyweight to me out of the five. Posts usually have a visual indication to set them apart from one another, and reply hierarchy isn’t given primary rendering. I’m throwing email in this bucket because “Conversation View” email renderers, including the ones in Apple Mail and the default Gmail client, effectively organize threads the same way forums do, even if the top level is a bit different.

---

I’m sure I’m not the first to try to categorize online media like this, but I do want to highlight the separation between the “primarily synchronous” and the “primarily asynchronous” sections. It’s important to me that you _can_ do messaging and chat rooms asynchronously, but the best moments I’ve had in them are the ones where you and one or several other people are all talking together. That doesn’t happen the same way in a forum, and it’s a bit of a stretch even in Twitter-likes where it’s considered normal.

…But on the flip side, in forums the discussion _sticks around,_ and sometimes is relevant years later, whereas reading the transcript of a chat room conversation, or trying to find something that happened years ago in a chat room, is a lot more difficult. And the fast-paced nature of live conversations can be offputting for people who like being more careful and composed with their words.

Anyway, I appreciate the community that comes with all five of these, but they’re also _different._ So when someone complains about the enshittification of Discord (valid) and responds by starting a forum, well…that’s great, and they do overlap. But a forum isn’t a chat room, and I’d miss that synchrony.

P.S. Obviously I haven’t tried to fit non-textual media into this, but if someone wanted to take a stab at it: group video calls, group audio calls, multiplayer games with voice chat, whatever that weird Twitter roundtable call thing was.

P.P.S. Speaking of multiplayer games, [MUDs](https://en.wikipedia.org/wiki/Multi-user_dungeon) also don’t fit my categories, even though they’re definitely text-based. A secret sixth thing, also synchronous.

This entry was posted on [January](https://belkadan.com/blog/2024/01) 20, [2024](https://belkadan.com/blog/2024) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [User experience](https://belkadan.com/blog/tags/user-experience)
