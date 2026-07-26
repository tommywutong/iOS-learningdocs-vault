---
title: Replacing Google Search with DuckDuckGo
source: Jesse Squires
source_key: jessesquires
source_url: 'https://www.jessesquires.com/blog/2018/02/25/replacing-google-with-duckduckgo/'
original_language: en
published: 2018-02-25
status: active
license: © 2014–2026 Jesse Squires → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:013a53e21555fad9'
translated: false
---

> 原文：[Replacing Google Search with DuckDuckGo](https://www.jessesquires.com/blog/2018/02/25/replacing-google-with-duckduckgo/)　·　Jesse Squires

I’m not interested in being an advertising product for Google to exploit. I’m also not interested in the company’s [unsavory practices](https://daringfireball.net/linked/2017/09/01/hill-google-forbes), in general. I’ve been using [DuckDuckGo](https://duckduckgo.com) for over a year now, and I’m incredibly happy with it as a replacement for Google Search — not only for personal usage, but also for implementing a [custom search component](https://www.jessesquires.com/search/) for this site.

![DuckDuckGo](https://www.jessesquires.com/img/blog/duckduckgo.png)

<sub>DuckDuckGo / [Source](https://duckduckgo.com)</sub>

### Why not Google Search?

Google no longer provides you with a simple list of ranked results. To become a major player in the [attention economy](https://en.wikipedia.org/wiki/Attention_economy), Google Search must track you across the web and mine your personal information to provide you with “personalized results” and to sell your information to advertisers. Google can now even [track your _offline_ purchases](https://www.washingtonpost.com/news/the-switch/wp/2017/05/23/google-now-knows-when-you-are-at-a-cash-register-and-how-much-you-are-spending/?utm_term=.0554ea667e32) — that is, at physical stores in the real world. Pretty creepy. The company strongly emphasizes how they’ve done this securely, to protect users — but that’s beside the point for me. _I do not want this intrusion into my daily, **offline** life._

Google’s enormity gives it [undue](https://daringfireball.net/linked/2017/09/01/hill-google-forbes) [influence](https://80x24.net/post/the-problem-with-amp/) on content providers and publishers. In particular, [Google AMP](https://www.ampproject.org) results, which are diplayed prominently in search, [threaten](https://danielmiessler.com/blog/google-amp-not-good-thing/) [the web](https://www.theregister.co.uk/2017/05/19/open_source_insider_google_amp_bad_bad_bad/) at a fundamental level.

The [lack of ethics](https://www.theguardian.com/technology/2016/dec/04/google-democracy-truth-internet-search-facebook) codified into Google search are disappointing and irresponsible. Google has positioned itself as the digital arbiter of truth. However, this is undermined by its pursuit to grab a slice of the attention economy, which requires curating unique search results for each user. This combined with an absence of fact-checking produces outcomes that range from [unfortunate](https://gizmodo.com/googles-algorithm-is-lying-to-you-about-onions-and-blam-1793057789) to [alarming](https://searchengineland.com/googles-one-true-answer-problem-featured-snippets-270549) to [horrifying](https://www.npr.org/sections/thetwo-way/2017/01/10/508363607/what-happened-when-dylann-roof-asked-google-for-information-about-race). Google’s curated results have the power to shape and distort people’s views. That’s an ethical problem.

I’ll give them credit though. Google has worked to address some of the problems in the articles that I’ve linked to above. However, the company’s financial incentives remain the same as far as I can tell. As long as they are beholden to satisfying advertisers and scrounging for users’ attention, I’m not hopeful that the trolls won’t find new ways to turn the search engine into an alt-right propaganda machine again.

##### [Update](#updated-17-march-2021)  _17 March 2021_

In completely unsurprising news, Google’s search results [have gotten worse](https://daringfireball.net/linked/2021/03/04/fowler-google-search) over time. And while I’m here — updating this post 3 years later — I have to say, DuckDuckGo has been great. I have no complaints.

### Benefits of DuckDuckGo

Similar to many Apple products and services, DuckDuckGo was established with [privacy as a fundamental feature](https://duckduckgo.com/about), not to mention [a company value](https://spreadprivacy.com). While their revenue model is still based on advertising, the service does not mine your data to do so. DuckDuckGo also sometimes adds an affiliate code to some eCommerce sites, but this is done without using any personally identifiable information. All the details are clearly explained [in their privacy policy](https://duckduckgo.com/privacy), which you can compare with the [Google privacy policy](https://www.google.com/policies/privacy/). Google [collects](https://www.google.com/policies/privacy/#infocollect) and [shares](https://www.google.com/policies/privacy/#nosharing) a staggering amount of your data that is personally identifiable. They obscure how they use it behind vague phrases like “improving your user experience”, and even after deleting your information from their services they reserve the right to retain a copy for “legitimate business or legal purposes”. DuckDuckGo provides a strikingly different policy, which puts privacy first and even includes an [“Information Not Collected”](https://duckduckgo.com/privacy#s3) section.

> You can usually find out a lot about a person from their search history.
> 
> — Gabriel Weinberg, [DuckDuckGo Privacy](https://duckduckgo.com/privacy#s2)

Gabriel Weinberg has a rather [comprehensive list](https://www.quora.com/Why-should-I-use-DuckDuckGo-instead-of-Google) of reasons to use DuckDuckGo. I won’t bother reiterating each of them, but I will highlight one of my favorite features — [!bangs](https://duckduckgo.com/bang), which let you search other sites directly. For example, you can type `!giphy oh yeah` into DuckDuckGo and land directly on [Giphy’s search results](https://giphy.com/search/oh-yeah) for “oh yeah”.

### Quality of search

After over a year of using DuckDuckGo, I think search quality is excellent. At times it could be better, but that’s a trade-off that I’m willing to make for privacy and a more ethical product. Overall, I’m incredibly happy using DuckDuckGo. If you aren’t satisfied with DuckDuckGo’s results, you can always `!google` to search again. I use this occasionally, though it’s increasingly rare.

### Implementing a custom search box

Google allows you to create a free [custom search component](https://cse.google.com/cse/) and embed it into your site, which I used here before switching to DuckDuckGo. You enter your site url, configure some settings, and then grab the code snippet to embed it. It sounds simple, but it is actually a heavy-handed and cumbersome script-based approach. It’s an exercise in pain to customize the appearance, and it won’t appear when using most ad-blockers.

Creating a [custom DuckDuckGo search](https://duckduckgo.com/search_box) is much simpler. They provide an [`<iframe>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe) snippet, which is not ideal. Luckily, you can create and style your own search box with basic html forms — something Google doesn’t offer.

```
<form name="search" action="//duckduckgo.com/">
    <div class="form-group">
        <div class="input-group">
            <input type="search" class="form-control" placeholder="DuckDuckGo" name="q">
            <input type="hidden" value="jessesquires.com" name="sites">
            <input type="hidden" value="1" name="kh">
            <input type="hidden" value="1" name="kn">
            <input type="hidden" value="1" name="kac">
            <input type="hidden" value="1" name="kc">
            <span class="input-group-btn">
                <button class="btn btn-default" type="submit">Search</button>
            </span>
        </div>
    </div>
</form>
```

This adds a basic form with a few [custom URL parameters](https://duckduckgo.com/params) and custom styling using [bootstrap](https://getbootstrap.com). You can add this to your own site by replacing `jessesquires.com` on line 5 with your own domain. You can see and use my custom search [here](https://www.jessesquires.com/search/).

You can find [the diff on GitHub](https://github.com/jessesquires/jessesquires.com/commit/d2126bacca43e5f9fb77f980c67fe178d6933673#diff-c9db0e13a328be0eaa311c5b24ad331c) for deleting Google custom search and replacing it with DuckDuckGo. It’s much more elegant, lightweight, and just looks better.

Thanks to [Stuard Colville](https://muffinresearch.co.uk/adding-a-duckduckgo-search-box-to-your-blog/) for his helpful post on doing this without using iframes.

### Making the switch

If you value privacy and the open web, it’s time to switch. By supporting DuckDuckGo, you will only help improve their service. Contrary to what most giant tech companies would have you believe, _it is possible_ to build a great service without exploiting users’ privacy and personal information.

##### [Update](#updated-09-june-2021)  _09 June 2021_

Bing was [caught blocking results](https://mashable.com/article/microsoft-bing-tank-man/) for Tiananmen Square protests in Hong Kong. Per [Gabriel Weinberg](https://mobile.twitter.com/yegg/status/1401216879293874185): _“China banned DuckDuckGo in 2014 and we have no plans to change that.”_

It is rare to see a tech company **not** cooperate with authoritarian governments.

##### [Update](#updated-23-october-2021)  _23 October 2021_

[A new report by Thomas Brewster at Forbes](https://forbes.com/sites/thomasbrewster/2021/10/04/google-keyword-warrants-give-us-government-data-on-search-users/): _“The U.S. government is secretly ordering Google to provide data on anyone typing in certain search terms, an accidentally unsealed court document shows. There are fears such ‘keyword warrants’ threaten to implicate innocent Web users in serious crimes and are more common than previously thought.”_

[@DuckDuckGo](https://twitter.com/DuckDuckGo/status/1447559362906447874): _“Google complies with invasive ‘keyword warrants’ that identify anyone who searched for a term. DuckDuckGo doesn’t have any search histories by design and, bc of that, has had 0 search warrants (of any kind) since our founding in 2008.”_

Good to know.
