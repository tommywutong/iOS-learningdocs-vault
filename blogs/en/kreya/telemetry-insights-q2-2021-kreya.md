---
title: 'Telemetry insights Q2 2021 | Kreya'
source: Kreya Blog
source_key: kreya
source_url: 'https://kreya.app/blog/telemetry-insights-q2-2021/'
original_language: en
published: 2021-07-06
status: active
license: Copyright © riok GmbH（页脚）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:75eee8ad7db2fc76'
translated: false
---

> 原文：[Telemetry insights Q2 2021 | Kreya](https://kreya.app/blog/telemetry-insights-q2-2021/)　·　Kreya Blog

How many users use Kreya? How many requests are sent each day? Why do we collect this information? These and more questions we want to answer in the following blogpost and give you a detailed insight in our telemetry data.

## Why do we collect this information?

First of all, we don't track any personal data. Kreya collects telemetry data from each installation with a random UUID which cannot be traced back to you.

We mainly collect this telemetry data to understand how our users are using Kreya. Before we implemented telemetry, we had no idea how many active users we had or if Kreya was used at all. The telemetry data helps us to improve Kreya and prioritize features as well as bugs. Secondary it enables us to create fancy charts - _who does not love fancy charts?_ 📈 - and give you an overview of how Kreya is used. For a list of all tracked events and how to disable it, see the [telemetry documentation](https://kreya.app/docs/telemetry/).

## How many users use Kreya?

Now that the formalities have been clarified 😉, let's get started.

### Overview

We implemented the telemetry with Kreya [version 1.4](https://kreya.app/docs/release-notes/), which went live on 30 April. This means that we now have data for the last two months.

| Measurement | Amount |
|---|---|
| Unique users (AppStarted) | 1,208 |
| Weekly active users | max. 304 |
| Invoked operations | 58,526 |

### Unique users (AppStarted)

In the line chart below, the new installations of Kreya on Tuesdays, Thursdays and Sundays are shown. You can see very well that at the weekend the numbers drop to about 5 users. In May, an average of 18 new users a day installed Kreya and started it at least once. In June, the numbers have increased slightly to about 20 users per day. On 15 June, a new record was set, 43 users installed Kreya.

In the following bar chart the different operating systems are listed. As you can see Kreya is used fairly evenly on the three main operating systems with a slight lead of Linux.

### Weekly active users

The number of weekly active users has always increased over time, only in the second half of May there was a small drop. This is probably related to the holidays during this period, as less work was done. This chart gives a better overview of the active users, since the weak numbers at the weekend are combined with the work days. The maximum number of weekly active users (304) was reached on 26 June for the period of 20 June - 26 June.

It's a bit strange to see this numbers compared to the metric of snapcraft. It's the app store for Linux, where various snaps are published. On their chart we reached over 600 weekly active users at the end of June. We don't know why this huge difference appears. Although we are happy that Kreya is a featured snap on [Snapcraft](https://snapcraft.io/) since April 2021.

### Invoked operations

For every invoked operation an event (OperationInvoked) is triggered. A total of 58,526 requests were sent in the last two months. The line chart below, shows how many operations were invoked in a week. There were around 3,000 at the start of May and almost 10,000 at the end of June.

There is a huge difference between the different gRPC modes. Both, grpcWeb and grpcWebText, are used rather rarely. By far the most used mode is the default gRPC mode.

The low numbers for the send mode 'one By One' are a little surprising. Only 12 operations were invoked with this kind of send mode. With this send mode each request can be sent one by one if there are multiple requests in an operation. This indicates that rather few operations with client streaming or duplex streaming are invoked.

## Other interesting numbers

On our [website](https://kreya.app) we are using [Plausible](https://plausible.io/), the privacy-friendly alternative to Google Analytics. This tool gives us some other interesting numbers which we want to share with you. The most visitors of our website coming from the United States (20%) followed by India (11%), Russia (7%), Germany (6%), UK (5%), Japan (3%) and China (3%).

In total, we had 2,400 unique visitors in the last two months. Most of them come via direct link to our site (46%). Other top sources are [Google](https://www.google.com/) (18%), [GitHub](https://github.com/) (15%), [Hacker News](https://news.ycombinator.com/) (6%), [Snapcraft](https://snapcraft.io/) (3%) and [Reddit](https://www.reddit.com/) (2%).

The download button was clicked 659 times, which is almost half of the measured unique users inside the kreya application. This is probably due to the many ad blockers that are used to access the website.

## Conclusion

We are very proud to see our product is used by a bunch of people. The steadily rising numbers make us confident for the coming months. For feedback or suggestions on which charts you would like to see in the future, write to us at [[email protected]](https://kreya.app/cdn-cgi/l/email-protection#335b565f5f5c735841564a521d524343).

For now that's it for the fancy charts. Help us spread the word and tell your friends and work colleagues about Kreya. 🚀
