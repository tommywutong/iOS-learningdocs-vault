---
title: 'Submitting functionality for a future version of iOS | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2011/01/submitting-functionality-for-future.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:0a04fb409e11dfff'
translated: false
---

> 原文：[Submitting functionality for a future version of iOS | Cocoa with Love](https://www.cocoawithlove.com/2011/01/submitting-functionality-for-future.html)　·　Cocoa with Love (Matt Gallagher)

A number of websites are reporting that my application, [StreamToMe 3.5](http://itunes.apple.com/au/app/streamtome/id325327899?mt=8) was approved with mention of a piece of future iOS functionality. While this was actually the case, it does not mean that Apple have started accepting apps for this new version of iOS.

## What happened? What is this article about?

![](https://www.cocoawithlove.com/assets/objc-era/streamtome_ios_icon.png)

A few different websites ([Mac Rumors](http://www.macrumors.com/2011/01/25/apple-now-approving-ios-4-3-compatible-airplay-apps/), [Engadget](http://www.google.com.au/url?sa=t&source=web&cd=2&ved=0CBwQFjAB&url=http%3A%2F%2Fwww.engadget.com%2F2011%2F01%2F25%2Fios-4-3-ready-apps-begin-turning-up-in-the-app-store%2F&ei=O9M_TZ2kJo2mugOR6_zMAw&usg=AFQjCNFAV-KO-6xclSl2ebB-L8nAS1Scmg&sig2=jIUR97OJiQY75vc_99ptRg) and [dozens of others according to Google](http://www.google.com.au/search?q=streamtome+ios+4.3)) have picked up on an unfortunate point: the "What's new in version 3.5" text for [StreamToMe](http://itunes.apple.com/au/app/streamtome/id325327899?mt=8) discussed a feature that will be enabled once a future version of iOS is released.

From these articles, it appears people are assuming that Apple have started accepting submissions for applications built with iOS 4.3. At the time of this post, the current SDK is _iOS 4.2_ so approval of an iOS 4.3 linked application would be newsworthy.

While I love the attention, it pains me to point out the fact that it might not be as newsworthy as people hope.

While the feature line was not a lie, this version of StreamToMe has _**not**_ been linked against iOS 4.3 — it is an iOS 4.2 application — and Apple are not ready for people to mention future functionality in their programs.

## Can I submit my app linked against iOS 4.3?

Apple won't let you submit an application to the iOS app store if it is linked against a future or beta version of the iOS SDK. At the moment, the current version of the iOS SDK is iOS 4.2. Do not submit an application linked against a beta SDK — it will be rejected.

If you are an Apple developer, Apple will probably email you when iOS 4.3 submissions are being accepted. They have traditionally done this about 2 weeks before the release of the iOS version to consumers and there's no reason to expect this to change in future.

Apple have not notified developers that they can submit using iOS 4.3. Therefore you should only use iOS 4.2 for current submissions.

## So what's up with StreamToMe claiming iOS 4.3 behavior then?

First: it was a bit of clumsy copy writing on my part. I shouldn't have mentioned it when I submitted and have removed the mention from the application description.

Sometimes there are elements of a future version of iOS that you can defensively code to support. In this case, I wanted to invoke a single method to support functionality, should it become available in a future version.

How does StreamToMe use this magic method without linking against it?

The answer is: dynamically. StreamToMe looks at runtime to see if the magic method is there. The code looks like this:

```objc
if ([someCurrentObject respondsToSelector:@selector(magicMethodToEnableFutureFunctionality:)])
{
    IMP imp = [someCurrentObject methodForSelector:@selector(magicMethodToEnableFutureFunctionality:)];
    if (imp)
    {
        ((void(*)(id, SEL, BOOL))imp)(someCurrentObject, @selector(magicMethodToEnableFutureFunctionality:), YES);
    }
}
```

I've used the name `magicMethodToEnableFutureFunctionality:` here instead of the real method name, to protect the guilty party involved.

Getting the `IMP` followed by the ugly looking typecast function invocation is just to make sure the parameter is passed to `magicMethodToEnableFutureFunctionality:` correctly (since the compiler has no method declaration to use, we typecast to ensure correctness). You can achieve the same result by declaring the method in a category of the `someCurrentObject`'s class but I preferred this approach here purely to keep my only-temporary-until-the-future-version-is-official code in one place. In either case the `respondsToSelector:` call is required as it is the step that ensures the method exists.

By doing everything both dynamically and defensively, the limitations associated with linkage and current iOS funtionality are avoided.

## That's great, I can make all my future changes like this!

Be careful!

This type of action is a calculated risk. The risk is that the final release of the iOS version you're hoping to support in future might change the name of the method to something else, in which case, this code have any effect. The future version of iOS could change the _type_ of the parameter — which could cause your program to _crash_ until you change your code. There's also the risk that the future functionality could be removed from iOS entirely before release for whatever reason.

While you're coding defensively to support changes, you're still creating risk.

The reasons I decided to take this risk with StreamToMe 3.5 were:

- The functionality was very simple (one simple method was all that was required)
- StreamToMe 3.5's feature set was complete and it was due for a release _now_, while the future iOS release is an indeterminate time into the future
- I didn't think anyone would really notice until after iOS 4.3 (**oops: I spot a flaw in my plan**)

Even if you do include changes like this: don't mention them in your text. Clearly, such mentions may slip through accidentally but it is against your developer agreement to mention future functionality.

## Conclusion

[StreamToMe 3.5](http://itunes.apple.com/au/app/streamtome/id325327899?mt=8) is mega-hyper-super wünderfantastic. You should buy 12 copies just for yourself and dozens more for your friends.

But sorry, it's not an iOS 4.3 application. It was built using the current, plain vanilla Xcode 3.2.5 and plain chocolate (without sprinkles) iOS 4.2 SDK. What it may or may not support in the future remains something to be seen when it happens. The world continues to turn at the normal, sub-ludicrous speed.

Please, don't link your own applications against future iOS versions and submit then until Apple give the green light to do so. You'll just get told to resubmit using the current SDK.

If you're prepared to be a cavalier cowboy coder like I have been, and take crazy risks that promise future functionality without any real guarantee, well you can clearly do that but at least know you're taking a risk so that when you get burned you'll understand why.
