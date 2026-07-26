---
title: 'Meet a Facebook Engineer: Ben Gertzfield'
source: Meta Engineering — iOS
source_key: fbeng
source_url: 'https://engineering.fb.com/2012/02/04/ios/meet-a-facebook-engineer-ben-gertzfield/'
original_language: en
published: 2012-02-04
status: active
license: © Meta → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:4b75cc7d80ba3829'
translated: false
---

> 原文：[Meet a Facebook Engineer: Ben Gertzfield](https://engineering.fb.com/2012/02/04/ios/meet-a-facebook-engineer-ben-gertzfield/)　·　Meta Engineering — iOS

_At Facebook, our engineers collaborate to create an open environment where ideas win and are executed quickly. Each week, our engineers will give you a look into what it’s like to iterate and build at Facebook in our new “Meet a Facebook Engineer” Q&A series. Check back weekly to hear from different engineers about what problems they’re passionate about solving right now, what they’re up to at Facebook and what advice they have for you._

![](https://engineering.fb.com/wp-content/uploads/2012/02/Fnn_DABkA4_wPDACANMbimJuPQkAAAE.jpg)

## Q: How do you decide what problems you want to work on?

**A:** At Facebook, you can jump in and fix any problem you want, whether it’s a pet peeve you have or some little feature that’s been missing. We’re not afraid to try things here, and there’s no bureaucracy or procedure in place to say, “No, you can’t touch that.” Whatever crazy idea you might have, we can hack it up at a Hackathon and see if it sticks. Most of them don’t, but there’s no penalty or shame in failing at Facebook. Everybody’s into trying lots of new things and seeing what works.

## Q: What does code review look like at Facebook?

**A:** It’s a lot like a peer review system for scientific journals. When programmers want to make a fix or add a new feature, they write it, test it, and post it for review. Anyone who’s subscribed to updates in that area will be able to see what has changed and give feedback. Nothing is secret at Facebook; if you’re interested in a particular thing like translation or mobile or tabs, you can just subscribe to updates in that area.

## Q: What’s your passion project here?

**A:**I’m really passionate about making Facebook work in other languages besides English. Something I’m really proud of doing here is making it so that we allow non-English characters in fan page URLs. It used to be that when you visited a fan page of a public figure who listed their name in a language other than English, we would remove any non-English characters from the URL in the browser bar. So, when I’d go to the fan page for my favorite Japanese animator [宮崎駿](https://www.facebook.com/pages/%E5%AE%AE%E5%B4%8E%E9%A7%BF/103160003103710)[(Hayao Miyazaki)](https://www.facebook.com/pages/Hayao-Miyazaki/112164162133344), the URL would turn into garbage. I fixed it so that other languages would show up right in the bar. That fix ended up having a bunch of cool side effects, like objects with these new URLs ranking higher in search. Now, if I search for my favorite Japanese animator, his page will show up higher in results because the name’s actually inside the link.

I actually came to Facebook in part because it had the first successful crowd-sourced translation on the internet. Before I came to Facebook, I had been trying and trying to get my software translated into non-English languages. Usually you have to hire a lot of experts in every language, which costs a lot of money and takes a long time. But I soon saw that on Facebook, the users were translating the site themselves. I thought, “How did they get them to do that?” After thinking about it I figured out that when the users translate Facebook into their own language, it makes the site better for them because more of their friends can use it. So we have this virtuous cycle of people translating the site into their language to make sure their friends can use it, which in turn makes the experience better for them. That would never happen on a lot of other sites.

## Q: What problems do you care most about solving now?

**A:**Like in any kind of science, the biggest problem in computers is trying not to reinvent the wheel. We’re going to get better only if we build upon the foundations that others have built before us. In CS, we’re blessed that we can make a hundred copies of a computer program and it doesn’t cost us anything. It’s not like using a tool or a chisel. I’m really passionate about writing reusable sets of tools that we can use to make lots of different products. It always makes me really happy to get people sharing and not rewriting things from scratch.

I most recently worked on [Facebook Messenger](https://www.facebook.com/mobile/messenger), and we wanted to create a lot of the same features in Messenger that we had in the main iPhone app. So I spent a lot of time evaluating what they had in common and how we could reuse and separate out the common functionalities. It doesn’t sound very sexy and exciting, but figuring out how to share and reuse code between lots of products is one of the hardest problems in this field.

## Q: How did your work on Messenger scale into other parts of the site?

**A:** Believe it or not, we wrote the system for Facebook Messenger based on something they use for space probes. It’s a system called [MQTT](http://mqtt.org/faq), and we put it into Facebook Messenger for iPhone so we could send real-time chat messages back and forth really efficiently and cheaply, to save the battery on your cell phone. It was secure, it was fast, and it did everything we needed.

Then we took a look at the Facebook for iPhone app, which had always had some Chat problems. At the time, there were actually three different Chat systems being used simultaneously, none of which worked. We ripped them all out and replaced them with the guts of Facebook Messenger. Nobody even noticed, and that was my goal. I just wanted it to be better, and I was really proud it worked out that way.

## Q: What advice you have for engineers?

**A:**Fail early and often. We spend so much of our time worrying about whether what we’re doing is going to work—I say just try it. You’ll probably fail, but you’ll learn in the process, right? If you figure out why it failed you won’t make that mistake again, and eventually you’ll just run out of mistakes to make.
