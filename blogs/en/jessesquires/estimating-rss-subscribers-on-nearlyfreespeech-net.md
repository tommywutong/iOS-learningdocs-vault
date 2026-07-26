---
title: Estimating RSS subscribers on NearlyFreeSpeech.net
source: Jesse Squires
source_key: jessesquires
source_url: 'https://www.jessesquires.com/blog/2023/04/26/estimating-rss-subscribers/'
original_language: en
published: 2023-04-26
status: active
license: © 2014–2026 Jesse Squires → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:51a2b922d818f96c'
translated: false
---

> 原文：[Estimating RSS subscribers on NearlyFreeSpeech.net](https://www.jessesquires.com/blog/2023/04/26/estimating-rss-subscribers/)　·　Jesse Squires

I recently asked on Mastodon for tips on estimating your total number of RSS subscribers. It turns out it is rather easy to do. While I do have (privacy-aware) [analytics for my site](https://www.jessesquires.com/blog/2020/05/08/simple-private-opensource-analytics-with-goatcounter/), this only tracks page views.

Some friends pointed me to [this blog post](https://darekkay.com/blog/rss-subscriber-count/) which describes how to do this by simply searching through your web server logs. If you use [NearlyFreeSpeech.net](https://www.nearlyfreespeech.net) for hosting, like me, there are some additional steps.

First, logs are _not_ enabled by default on NFSN. You need to navigate to your site settings to turn on logging. Logs are then stored in `/home/logs`. You can find all the information you need about log files on NFSN [in these FAQs](https://faq.nearlyfreespeech.net/section/logfiles/-).

You should wait at least a few days or a week after enabling logs before accessing them so that you can collect some data. Then you can `grep` the logs to see the requests for your feeds. I publish an RSS feed as well as a JSON feed.

```
cat access_log | grep feed.xml
cat access_log | grep feed.json
```

Unsurprisingly, the number of subscribers to the RSS feed is significantly higher than the JSON feed.

Some centralized services put the number of subscribers in the “user agent” string of their HTTP requests. You’ll see log entries like this:

```
"GET /feed.xml HTTP/1.1" 304 - "-" "Feedbin feed-id:1344882 - 122 subscribers"
"GET /feed.xml HTTP/1.1" 304 - "-" "Feedly/1.0 (+http://www.feedly.com/fetcher.html; 265 subscribers; like FeedFetcher-Google)"
```

I anticipated having at least a few thousand subscribers based on my site analytics, but it appears to be more on the order of a few hundred. It’s a shame that RSS readers are not more popular.

Obviously, decentralized RSS reader apps cannot provide subscriber data. But it was still neat to see what apps people are using. For example, it was nice to see [NetNewsWire](https://netnewswire.com) in the logs!

```
"GET /feed.json HTTP/1.1" 304 - "-" "NetNewsWire (RSS Reader; https://netnewswire.com/)"
```

If you are interested in seeing the _total_ number of requests for your feed, you can pipe the output to `wc`.

```
cat access_log | grep feed.* | wc -l
```

It is important to note that this number **does not** represent _unique_ users, but it was still interesting for me to see. In one week, my feeds were requested over 78,000 times. That was much higher than I expected.
