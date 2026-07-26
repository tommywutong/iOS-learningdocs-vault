---
title: The iPhone Development Story
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/the-iphone-development-story.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:e8ac3392fb2e00e8'
translated: false
---

> 原文：[The iPhone Development Story](https://www.mikeash.com/pyblog/the-iphone-development-story.html)　·　mikeash.com Friday Q&A

Posted at 2008-09-18 00:30 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [It's a Poor Carpenter Who Blames His Tools or: Xcode Sucks Again](https://www.mikeash.com/pyblog/its-a-poor-carpenter-who-blames-his-tools-or-xcode-sucks-again.html)  
Previous article: [NetAwake](https://www.mikeash.com/pyblog/netawake.html)  
Tags: [iphone](https://www.mikeash.com/pyblog/?tag=iphone) [rant](https://www.mikeash.com/pyblog/?tag=rant)

The iPhone Development Story

by [Mike Ash](https://www.mikeash.com/)

But even a perfectly normal experience with the iPhone developer program is intensely weird. Compared to the simplicity of developing and distributing a Mac app, Apple's iPhone program is extremely convoluted and strange. Here's the story, step by step.

**1. Sign up with the iPhone Dev Center**  
 The [iPhone Dev Center](http://developer.apple.com/iphone/) is Apple's portal page for iPhone development. Here, you can download the SDK and find tutorial videos and documentation. For reasons unknown to me, merely having an account with the [Apple Developer Connection](http://connect.apple.com/) does not suffice. I have to sign up again for the iPhone site. This is pretty straightforward, however: just click through some scary legal forms and off you go. Now I can download the SDK and get started.

**2. Enroll in the iPhone Developer Program**  
 I'm not done signing up with stuff yet! You see, although I signed up and clicked through the scary legal stuff and downloaded the SDK, I can't actually install any software on my iPhone. I can read documentation, write code, compile it, and even run it in the iPhone simulator, but I can't get it onto my actual iPhone.

(And don't think that the simulator makes for an adequate development platform. There's a reason it's called a "simulator" and not an "emulator". Running on the real hardware ends up being pretty different.)

For this privilege, Apple makes me sign up for the developer program. I get to fill out some more forms, click through some more scary legal stuff, and send off my request.

Request? That's right, I don't get an answer immediately. Instead I get to....

**3. Wait**  
 This step is going to come up again. I believe that this time the answer came the next business day.

**4. Pay**  
 Did I mention that the program is not free? And remember, this isn't to distribute apps, it's just to start realistically working on them. $99 to put apps on my own iPhone. (Or as it happens, on my own iPod Touch.) But I pay my money and shortly afterwards I receive an activation code.

Now I'm ready to put software on my iPhone! Well, not quite.

**5. Provision**  
 A stock iPhone won't take _any_ software that hasn't been signed by Apple. This puts us third-party guys in a bind, because we can't get Apple to sign every single build we make. So what Apple does is allow you to create a provisioning profile. This is a cryptographic blob which essentially tells your iPhone to accept apps signed by you and not just Apple. To create it, we have to get the iPhone's unique identifier (accessible through Xcode) and then paste it into Apple's web form, then download the result from Apple. Very oddly, although I am enrolled as an individual developer, I still have to make a request and then manually approve my own request before the provisioning profile can be generated.

I download the profile, install it using Xcode, and now I'm ready to put software on my iPhone!

And if you believe that, you haven't been paying attention.

**6. Certificate**  
 I said that the provisioning profile tells the iPhone to accept software signed by you. Well, you also need a certificate to sign with. And of course this can't be any old certificate, but a special one made by Apple. The process here is fairly involved. You get to open Keychain Access, go to a little-used corner, generate a certificate _request_, open the result in a text editor, copy/paste the blob of random characters into Apple's web form, and then submit it. Then you get to download and install the result (after placing a request, and then approving that same request) as well as an intermediate certificate provided by Apple. And if you're like me, you also get to scratch your head over a bunch of really bizarre errors until you have a sudden flash of inspiration and run Keychain First Aid to fix corruption.

But now it's all done! My iPhone (iPod Touch) is provisioned, I have my certificate, I have the intermediate certificate, and I am now _finally_ ready to put software on it.

Come on, you know better than that by now.

**7. Screw about in Xcode**  
 Of course none of this goes quite right. There are a bunch of settings in Xcode that have to perfectly match the stuff that you gave to Apple, and they don't start out matching. The errors are essentially worthless. I believe I only ever saw Xcode generate _one_ error, over and over and over again, as it encountered a whole bunch of different problems.

But by careful log reading, insight, pure random luck, and internet searches, I finally arrive at a working system. I build in Xcode, and the application appears on my iPhone (iPod Touch). Yes, really. I'm not kidding this time. It actually worked, at last.

**8. Develop!**  
 This is what I'm here for, after all. Now that all the pieces are _finally_ in place, I can get down to writing code. (Yes, I could write code before. But I couldn't run it on the hardware that it was targeting, which made it somewhat less useful that it otherwise could be.)

As everybody knows, developing for the iPhone is a lot like developing for the Mac. Instead of Cocoa, you have Cocoa touch, which is very similar. There are significant differences as well, though, so it takes some getting used to.

In addition to the perfectly natural difficulties encountered from working on a new platform, there's also a big artificial difficulty. As any experienced developer knows, a great deal of help can be had from simply talking to other developers working on the same system. But Apple doesn't let us do that! If you'll recall, I mentioned a bunch of scary legal stuff that you had to click through to sign up with the program. Among all the other stuff, it included the [&*%#ing NDA](http://www.fuckingnda.com/) (WARNING: link contains extremely large curse words) which says that we can't talk about this stuff, with anyone, ever.

And it's not just boilerplate. If you read between the lines a bit on [Apple's cocoa-dev info page](http://lists.apple.com/mailman/listinfo/cocoa-dev), they pretty much come right out and threaten to sue anyone who violates their NDA on the mailing list.

It's not just code that takes the hit. Xcode took a lot of magic incantations to work as well. It would have been a lot easier if I had been able to (legally) talk with my fellow developers about it.

**9. Ship**  
 At last, the product is complete, and it's ready to be given to the customers. Well, not quite. This being the iPhone, Apple has a lot more hoops for me to jump through first! I had thought that all the craziness with certificates was behind me. I should have known better.

**10. Certificate**  
 For reasons entirely unknown to me, a build that is intended for distribution through the iTunes App Store needs to be built with a special distribution certificate. I don't understand why Apple can't just sign the build with their own special certificate. But apparently that's not good enough. So I go through the whole process all over again. Keychain Access, request, approve my own request, download, install.

Now I'm ready to ship.

I realize you're probably getting tired of this game, so I'll stop. Next time I say that I'm ready to ship, I'll mean it. Because of course, I'm not ready yet!

**11. Provision**  
 I forgot to mention that you need a special distribution provisioning profile too. I don't really understand why. You can't even install the built-for-distribution app on the iPhone. But there you have it.

**12. Screw about in Xcode**  
 You may recognize this from step 7. It's the same basic thing, but with a new twist. There are literally pages of instructions (admittedly, largely due to having a bunch of screenshots) detailing how to reconfigure the Xcode project to use this special magic distribution certificate instead of the development certificate I had before. The first time I went through these pages of instructions, I apparently missed something because when I built I got The Error instead of having things work. When I went back and redid the instructions from the top, suddenly it worked!

**13. Submit**  
 This involves filling out a pretty standard web form. First they ask a bunch of basic information about the app, such as its name, its version number, a description, and whether it includes cryptography. (Apps which include cryptography need a special license to be sold outside the United States. As if the US had some sort of monopoly on cryptography! And yes, this foolishness is due to Uncle Sam, not Apple.)

Next I get to a screen where I can upload the application, a large size icon, and screenshots. I click and upload the application. Then I do the icon. For some reason, Apple does not accept PNG files for either the icon or the screenshots, even though that's what their screenshot tools generate (on both platforms) and Mac OS X has had support for it since day one. They do support TIFF and JPEG. Alas, I don't notice this prohibition at first, and I upload a PNG version of my large icon. Somewhere in this process, something chokes, and I'm shown a cryptic error screen.

I press the back button, and I'm informed that my session has timed out. I go back to the main page, log in again, and go to the applications area. Nothing is listed. All of my previous work has been lost, and I have to re-enter everything a second time.

Fantastic.

I go through it all a second time, this time noticing and respecting the TIFF/JPEG requirements, and I make it through successfully. I set a price for the program, and now, at last, finally, it is ready to be purchased.

Just kidding! I'm sorry. I know I said I wouldn't do this anymore. But I couldn't resist.

**14. Wait**  
 The app sits in the list with this nice yellow gumdrop and a tag reading "In Review". There is no indication of progress, no ETA, no indication that anything is being done. I assume that something _is_, but I have to take this completely on faith.

This is when I started writing this post. While researching it, I went back and went through some of the motions that I had to do earlier on, so I could remember what they looked like. While I was doing this, I managed to hit all the right buttons to sign up with the iPhone Developer Program. Not one to let sanity stand in their way, Apple happily accepted my submission a second time. And so my account was thrown back in time, from being enrolled to once again waiting for acceptance.

I quickly sent off an e-mail to Apple requesting help, and then sat down for some low level panic. Fortunately, my status was changed back to being accepted within a couple of hours. Apple finally replied to my frantic request for help last week, about three weeks after I sent it. You'd think that with the NDA in place preventing us from helping each other, the least Apple could do would be to answer their e-mails in a timely fashion.

**15. Get Rejected**  
 About a week later, I get an e-mail from Apple. Wouldn't you know it, Apple can't make the thing work, so they reject the application. This e-mail is actually pretty decent, with the majority of it obviously written by an actual human about my particular case. When I write back to ask if they had run through NetAwake's troubleshooting guide, they reply within just a few hours to say that they had and it didn't help. Good on them for being so responsive!

Of course this puts my partner and me in a tough situation. The program works fine on our networks, but not on Apple's. And while Apple was nice about responding to my query, it's obvious that I can't get them to bust out a network sniffer and tell me about their router configuration.

After a great deal of thought we come up with a couple of things that might help it work on Apple's network, apply the fixes, and are ready to try them out on Apple.

**16. Screw about in Xcode**  
 This time it doesn't take nearly as long, but Xcode still has to put up some token resistance. There are two code-signing files that are supposed to be embedded in the application, and only one shows up in my initial build. After some clean building and a great deal of cussing, suddenly both of them show up, and I'm good to go.

**17. Resubmit**  
 Fortunately Apple provides a streamlined process for submitting a new build of a rejected application. A special link appears in the application's information on the submission site, and uploading the new application is just a couple of clicks away.

**18. Wait**  
 Of course once you're rejected you go to the back of the line, and I get to wait another week to see if the fixes did the trick or not.

**19. Get Rejected Again**  
 A week after resubmitting (nearly three weeks after the original submission), another e-mail from Apple arrives. This time they've found a legitimate bug in the application, and have rejected it because of that. This is perfectly understandable, and is actually a very good service they provide. But it is extremely annoying to have to wait a week to discover that they've found a bug, and then wait another week to see if the fix works for them.

(Note, I'm not saying that the first rejection wasn't a bug. Maybe it was, maybe it wasn't. I don't really have enough information to say one way or the other. This one definitely was, though.)

**20. Re-Resubmit**  
 My partner makes the fix, I submit again, and the waiting game begins. This is somewhat nail-biting by now, because not only is it possible that our bug fix didn't quite work and we've just wasted another week (although unlikely), but because of this bug we _still_ don't know whether our fix for the original rejection worked.

**21. Wait Again**  
 Of course it takes Apple another week to check our new submission. As explained, much nail biting ensues.

**22. Accepted!**  
 Finally, nearly a month after the original submission, the application is accepted by Apple and appears in the store. It spent longer going through Apple's approval process than it did in development! And while Apple did find a legitimate bug, spending a month in limbo for a single bug is a very poor tradeoff.

**Conclusion**  
 Development for iPhone is an incredibly difficult process, much more difficult than it needs to be. The arduous process of shipping an application for the Mac suddenly appears to be absolutely straightforward after going through this mess. I really don't envy those companies who have staked their success to the iPhone platform. The amount of arbitrary hassle, uncertainty, and delay in the process can only feel vastly worse when your livelihood depends on it.

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.
