---
title: 'Please Don''t Use URL Shorteners on Twitter'
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2012/08/please-dont-use-url-shorteners-on-twitter/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:bf8bff358ad5be25'
translated: false
---

> 原文：[Please Don't Use URL Shorteners on Twitter](https://oleb.net/blog/2012/08/please-dont-use-url-shorteners-on-twitter/)　·　Ole Begemann

# Please Don't Use URL Shorteners on Twitter

In this article, I am going to ignore this otherwise excellent piece of advice:

> Following someone on Twitter and complaining about what they tweet about is like phoning someone to tell them you don't want to talk to them
> 
> [@rickygervais](https://twitter.com/rickygervais)
> 
> Ricky Gervais
> 
> [August 18, 2012](https://twitter.com/rickygervais/status/236814912951836672)

Dear readers, I have a request for you: **if you are still using URL shorteners for posting on Twitter, please stop.**^[1](#fn:1) Here are my reasons:

# URLs have meaning

Tweets with obscure shortlinks are less scannable. They make it harder for the reader to evaluate whether clicking a link is worthwhile or not. I might have already seen the Techcrunch story you are linking to. Or I know that I’ve subscribed with RSS to the blog you’re referring to so I won’t miss the article even if I don’t open it right now. Or I just don’t like certain publications.

If your link points to bit.ly, I either need one more click to make the correct determination or I won’t consider clicking it at all because the “risk” of not getting what I anticipated is too high. I also suspect tweets with shortened links don’t get retweeted as often as tweets containing “real” URLs. Users who want to provide their followers the best value might choose to rephrase your tweet and include the original URL rather than retweet you.

140 characters is very little. You should try to make every single one count, including the URLs. They are part of the content of your tweet.

# Short URLs don’t save characters anymore

[For almost a year now](https://dev.twitter.com/discussions/2806), Twitter has been wrapping every URL in a [t.co](http://t.co) link. All URLs cost the same amount of characters^[2](#fn:2), regardless of their original length. The one reason why link shorteners got so popular (indispensable, in fact) on Twitter is no longer valid.

Thankfully, Twitter was smart enough to preserve the original URLs in the metadata that is included with each tweet. Using the information in these so-called [Tweet Entities](https://dev.twitter.com/docs/tweet-entities), Twitter clients (including the Twitter website) can replace the t.co link with the original URL in their user interface.^[3](#fn:3) Links shortened with other URL shorteners do not have this advantage.

# Your links may stop working

URLs are the fabric of the web. We should do all we can to keep them working. Unfortunately, if the company behind your URL shortener of choice decides to (or is forced to) shut the service down, all the links you have posted will stop working. This may not seem like a big problem, especially considering the apathy Twitter itself is showing towards keeping a permanent searchable archive of old tweets. But if (not when; I don’t have any trust in Twitter in that regard) they manage to do that someday, it would be a pity.

It’s bad enough that we are forced to use t.co on Twitter. At least we can assume that the t.co service will stay alive as long as Twitter lives. I just hope that the Library of Congress [archives not just all tweets](http://blogs.loc.gov/loc/2010/04/how-tweet-it-is-library-acquires-entire-twitter-archive/) but also their metadata.

# Analytics Should Not Interfere With Usability

Perhaps the biggest motivation for still using URL shorteners is the analytics data many shortening services provide. It can be very addictive to see how many people click the links you post. This is understandable but in my opinion, getting analytics should not interfere with the interests of your readers. My hunch is you’ll be more influential by caring less about analytics and doing what’s right from the reader’s perspective. Moreover, there are other ways to track the success of your tweets: the number of retweets and favorites you receive probably correlates strongly with the number of clicks. If you link to your own site, classic web analytics also help.

When Twitter introduced t.co, they promised to offer special APIs that would give developers access to their analytics data [a]fter the full t.co rollout is complete and our analytics has crystallized. So far, this promise remains unfulfilled. Perhaps this will change in the [upcoming 1.1 release](https://dev.twitter.com/blog/changes-coming-to-twitter-api) of the API (I’m not holding my breath, however). Given the fact that analytics apps don’t fall in the [top-right quadrant](http://marketingland.com/star-trek-twitter-quadrants-19105), we should expect Twitter to strengthen their offering in this area.

**Update August 24, 2012:** I fixed the permalink of the tweet I quoted above and improved the wording in a few places. I did not make substantial changes to the text.

1. When I speak of URL shorteners in this post, I mean generic shortening services like bit.ly and goo.gl where the contents of the URL give no indication of the original URL. Site-specific shortlinks like flic.kr or youtu.be are just as or almost as easy to parse as the original so I don’t have any problems with those. In addition, URL shorteners do have their place for rickrolling and other pranks. [↩︎](#fnref:1)
2. The length of t.co URLs is currently 20 characters for http and 21 for https links. This length could increase in the future if Twitter runs out of permutations for the current character counts. Developers can use the [GET help/configuration](https://dev.twitter.com/docs/api/1/get/help/configuration) API call to calculate accurate tweet lengths before posting. [↩︎](#fnref:2)
3. Clicking on the URL will still open the t.co URL, which then redirects you to the original page. Twitter’s [Display Guidelines](https://dev.twitter.com/terms/display-guidelines) strictly forbid client developers to bypass the detour through t.co because that would negate the whole point of this enforced routing: accurate click statistics. Regrettably, the Display Guidelines also prescribe the concrete format for the display of the original URL (very long URLs are shown in a truncated form); I’d like to have the option to see the full URLs. [↩︎](#fnref:3)
