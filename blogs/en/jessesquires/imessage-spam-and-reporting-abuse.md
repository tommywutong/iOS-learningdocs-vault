---
title: iMessage spam and reporting abuse
source: Jesse Squires
source_key: jessesquires
source_url: 'https://www.jessesquires.com/blog/2022/01/13/imessage-spam-and-reporting-abuse/'
original_language: en
published: 2022-01-13
status: active
license: © 2014–2026 Jesse Squires → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:410bb72b0902c436'
translated: false
---

> 原文：[iMessage spam and reporting abuse](https://www.jessesquires.com/blog/2022/01/13/imessage-spam-and-reporting-abuse/)　·　Jesse Squires

iMessage is [in the news again](https://mjtsai.com/blog/2022/01/11/blue-bubble-envy-is-real/) recently with a [revival of years-old stories](https://pxlnv.com/linklog/wsj-green-bubbles/) about “green bubbles” versus “blue bubbles” — and the social dynamics among teens who prefer blue bubbles while ostracizing their peers with green bubbles. There’s a lot to like and dislike about iMessage, but one thing that amazes me is that there is still no way to easily report abuse and the process for blocking spam is needlessly difficult.

At this point, I get regular iMessage spam and junk on a weekly or monthly basis. It is nearly as bad as email, although all modern email clients have sophisticated blocking and filtering tools — so I rarely get bothered by email spam or phishing. Aside from the absence of tools to automate blocking and report abuse, iMessage is significantly worse than email ever was because I always _receive a notification in real time_. Since iMessage is my primary messaging app, I cannot turn off notifications.

![iMessage spam screenshot](https://www.jessesquires.com/img/blog/imessage-spam-1.jpg)

<sub>An iMessage spam message that I received this morning</sub>

When you receive iMessage spam, you might think there’s a quick action available in the swipe menu to block or report. Sadly, no. You can only delete, silence notifications, or pin it — none of which prevent future junk from this spammer. Also, why would anyone want to pin this thread? Shouldn’t iMessage be smart enough to offer an option to report abuse here instead?

![iMessage swipe actions](https://www.jessesquires.com/img/blog/imessage-spam-2.jpg)

<sub>iMessage swipe actions</sub>

Or, perhaps you could long-press to bring up the context menu options? Still, nothing.

![iMessage context menu options](https://www.jessesquires.com/img/blog/imessage-spam-3.jpg)

<sub>iMessage context menu options</sub>

How can it be that in 2022 iMessage provides no way to report abuse like every other social media platform? (And yes, we should consider iMessage a [social media platform](https://daringfireball.net/2016/10/imessage_stickiness). It has [hundreds of millions of users](https://techcrunch.com/2012/06/11/imessage-has-more-than-140m-users-and-has-150b-messages-over-1b-a-day/) that send [billions of messages](https://appleinsider.com/articles/13/01/23/apple-sees-2b-imessages-sent-every-day-from-half-a-billion-ios-devices) daily.) According to [this Apple support document](https://support.apple.com/en-us/HT201229), you should see a “Report Junk” button when viewing messages from unknown senders. However, I **have never seen** that button. (See screenshots below.) That button never appears for unknown contacts that send me junk. Is this a bug or is that support document outdated?

iMessage does offer a setting to “Filter Unknown Senders” but the only benefit is that it will silence notifications for unknown contacts, and it introduces additional drawbacks. In addition to making the UI _even more clunky_ and difficult to navigate, it implements wholesale filtering of _all_ unknown numbers. This is _not_ what most people want or need. In today’s world there are dozens of notification and reservation systems that send texts — restaurant reservations, package delivery notifications, haircut appointment reminders, SMS-based 2-factor authentication systems, and so on. If you “Filter Unknown Senders”, then you don’t get notifications from any of these systems, most of which are very time-sensitive! This setting is too naive to be useful in any way.

![iMessage Support Doc](https://www.jessesquires.com/img/blog/imessage-spam-5.jpg)

<sub>Apple Support claims there is a "Report Junk" option / [Source](https://support.apple.com/en-us/HT201229)</sub>

The only recourse I have is to block bad actors manually every single time I receive junk. Thankfully Apple provides that functionality. The only problem is that the option to block a message is buried so deep in the UI, I bet most users never find it. How many taps does it take to block a contact on iMessage? **Five!** Also known as way too fucking many.

![Steps to block an iMessage sender](https://www.jessesquires.com/img/blog/imessage-spam-4.jpg)

<sub>Steps to block an iMessage sender</sub>

1. Tap to view the message, even though you already know it is spam from the contact info and preview text. **Note:** there is _no_ “Report Junk” button in the screenshot above.
2. Tap the sender’s contact photo/info in the nav bar.
3. Tap “Info” on the sender’s contact card.
4. Tap “Block this Caller”.
5. Tap “Block Contact”.

In fact, claiming there are only 5 steps is actually quite generous. After you block a contact, you then have to unwind from all these views to _get back_ to your iMessage inbox, which requires 3 more taps. **And then** you have to _manually_ delete the message, which requires another 2 taps. In total, that’s 10 fucking taps to block a spammer and delete their message. Absolute madness is an understatement. Who designed this?!

iMessage should offer a quick and easy way to block (and optionally report) bad actors. Rather than give me an option to pin a thread for an unknown (and obvious spammer) contact, it should offer the option to block the sender and report abuse to Apple. Apple could then maintain a list of known bad actors to help curb abuse of its platform.

##### [Update](#updated-08-november-2022)  _08 November 2022_

Good news! Beginning in iOS 16, some of these issues have been addressed. Now when you delete a message thread from any unknown sender, there is a new option to “Delete and Report Junk” and the “Report Junk” button always appears in threads from unknown senders. (See the screenshot below.) This is great.

Unfortunately, blocking a contact still requires the litany of steps listed above.

![iMessage on iOS 16](https://www.jessesquires.com/img/blog/imessage-spam-6.jpg)

<sub>iMessage on iOS 16, Delete and Report Junk</sub>
