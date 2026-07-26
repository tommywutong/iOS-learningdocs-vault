---
title: 'A new era for Cocoa with Love | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/blog/2016/01/25/a-new-era-for-cocoa-with-love.html'
original_language: en
published: 2016-01-25
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:5bcbc16dd576ce24'
translated: false
---

> 原文：[A new era for Cocoa with Love | Cocoa with Love](https://www.cocoawithlove.com/blog/2016/01/25/a-new-era-for-cocoa-with-love.html)　·　Cocoa with Love (Matt Gallagher)

I haven’t written a Cocoa with Love article in 4 and a half years. What’s been happening? Is there anything new in Cocoa?

“Everything”, you say? Excellent! I should have plenty of new code to share.

But not in this article.

## Previously on Cocoa with Love…

Cocoa with Love started as a place for me to write down some fun hacks I used for doing mischievous things in Cocoa – mostly abusing the Objective-C runtime. It’s fun to do things generally considered undocumented or impossible and Objective-C’s highly introspectible runtime let the devious programmer do much by hijacking other people’s code and subverting it. Of course, these sorts of actions are little more than cute tricks with few real use cases (they’re too risky, too high maintenance and there’s usually a non-devious way to achieve the same effect). I branched out in a number of different directions and even tried writing some articles about designing better apps, I primarily demonstrated a “business as usual” approach to app development and I’m not really happy with the overall result.

I’ve looked back through most of my old articles and many contain code that no longer compiles or code that’s completely superseded by newer APIs. Still more contain out-of-date information or worse: offer advice and opinions I no longer endorse.

I’m not planning to take the old articles down – people do still read them – but I’m not going to update or maintain them either. I’ve put a prominent “Reader beware” disclaimer on all of them to highlight that they should be viewed with appropriate caution. They’re doomed to become less relevant as Cocoa development continues to move towards Swift and away from Objective-C and that’s fine by me. I’d rather take the opportunity afforded by Swift and start fresh.

## A new theme

Switching from Objective-C to Swift will be an obvious change as I return to Cocoa with Love but it’s not the only change. I’ve wanted to return to Cocoa with Love since before Swift’s announcement (it’s a long delayed 2014 New Year’s Resolution of mine) to try writing articles that loosely fit into a broad, overarching theme: writing maintainable Cocoa apps.

I realize that as a topic, “writing maintainable Cocoa apps” sounds like a good choice for boring people into a coma. Despite the banal connotations, maintenance is truly the hardest problem in app development and minimizing maintenance costs is a good way to make everything else in programming feel better.

The hardest problem in app development is not "how do I implement this" or "how can I make this run faster". These are problems that programmers will necessarily have to address but they're not persistent; we solve them and move on. Maintainability is a pervasive and persistent problem; there's no single solution and it doesn't simply go away.

The importance of maintenance is due to the fact that an app is never “done”. In most modern desktop and mobile spaces, update cycles for operating systems, devices – even device categories – are annual or faster. There is always a change that requires a corresponding update. At the same time, your app has its own update cycle because you want to advance its feature set. Sadly, the fundamental architecture of modern user-applications does not gracefully endure multiple refreshes. A typical codebase will grow progressively harder to maintain until after 2 to 3 years, you’re barely maintaining existing features, let alone adding new ones. If you can afford to double your developer resources, you’ll need to completely rewrite or thoroughly refactor otherwise the only option is app abandonment.

This situation is horrible: we invest months or years into projects and throw that work away on a regular basis.

A significant portion of this problem is due to the same code maintenance issues that affect all programming. Any programming project – not just user-applications – can suffer loss of momentum over successive releases due to haphazard implementation, poor original designs, difficulties refactoring code and other forms of “code rot”.

But the manifestation of maintenance difficulties affecting user-apps is particularly acute. Even fair implementations of adequately designed apps can rapidly grow unreasonably difficult to add features or update for new technologies and OS versions. User-applications, as a programming domain, have a high concentration of traits that most programming tries to avoid for the exact reason that they are difficult to maintain. Most prominent of these traits are:

- apps are inherently stateful
- controllers naturally subsume other components increasing coupling and fragility
- efforts to combat coupling lead to excessive layers of abstraction rather than cleaner code
- apps include many timing dependent behaviors including callbacks, asynchrony, animation and user events
- apps are heavily reliant on OS provided APIs, taking many things out of your direct control
- apps are difficult to test automatically

The cumulative result is that app programming, while not a technically difficult field, tends to create fragile webs of code that are highly interdependent along a number of different axes leading to programs that are easy enough to design initially but surprisingly time-consuming and expensive to maintain and update.

We need to write code that is resilient against regular code maintenance issues and at the same time, address the problems that undermine app maintenance in particular. Unless we do, every program we write is just another soon-to-be-abandoned app.

## How do we improve “maintainability”?

If you’re savvy enough to reading this blog, then you’re doubtless aware that there are plenty of ideas around – technologies, frameworks, design patterns and programming techniques – that aim to limit the various negative traits that I listed as contributing to maintenance problems for user-applications.

- Some are applications of basic programming theory
- Some are lessons to avoid misusing development tools
- Some are as simple as better coding practices
- Some try to limit problems through evolved design patterns
- Some try to detect problems sooner through better testing approaches
- Some involve changing conventional thinking about errors, data, time or state
- Some involve pure functional, dataflow, declarative or other programming paradigms
- Some are frameworks that encapsulate a difficult trait throughout your program
- Some are frameworks that entirely replace the native application frameworks with alternatives

However, it’s interesting to consider though, that despite the number of techniques claiming to limit maintenance problems, none are universally considered essential for app development. Swift language notwithstanding, mainstream Cocoa app development is not dramatically different to NeXTSTEP development 20 years ago. Which leaves open the question: how many of these techniques – if any – actually succeed at their goals?

## Conclusion

My aim with the “Swift era” of Cocoa with Love will be to look at different approaches to make app programming suck less. If we program with fewer runtime errors and our new features are easier to add, we’ll have more fun – even if “maintainability” sounds like a dull word.
