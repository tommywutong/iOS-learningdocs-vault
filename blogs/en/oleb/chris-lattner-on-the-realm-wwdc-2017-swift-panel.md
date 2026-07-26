---
title: Chris Lattner on the Realm WWDC 2017 Swift panel
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2017/06/chris-lattner-wwdc-swift-panel/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:1dc3ea21982b3890'
translated: false
---

> 原文：[Chris Lattner on the Realm WWDC 2017 Swift panel](https://oleb.net/blog/2017/06/chris-lattner-wwdc-swift-panel/)　·　Ole Begemann

# Chris Lattner on the Realm WWDC 2017 Swift panel

[Chris Lattner](http://www.nondot.org/sabre/) was a guest [on a Swift panel](https://news.realm.io/news/wwdc-2017-swift-panel/) during WWDC a few weeks ago. Here are some quotes I found interesting, edited for brevity and clarity. (I’m focusing on Chris Lattner here, but the other panelists — [Kamilah Taylor](http://www.kamilahtaylor.com), [Lily Ballard](https://twitter.com/LilyInTech), and [Jesse Squires](http://www.jessesquires.com) — also had interesting things to say. You should really watch the whole thing if you can.)

# On the debate whether the open [Swift evolution](https://github.com/apple/swift-evolution) process is a good thing

_(Starting at 36:56)_

> **Lattner:** My take on it is that it’s good and bad. I think the way it is happening is the best it can be because the Swift team really does get a lot of value from people’s feedback. … Even though it’s very frustrating sometimes, it really helps to get people arguing back and forth and back and forth to really understand what the tradeoffs are.
> 
> > So much of language design is about tradeoffs. And you can’t see those tradeoffs unless you have a community of people that really represent those different points.
> 
> Because so much of language design is about tradeoffs and balancing. There is no one perfect answer in a multidimensional design space. You have to pick a point that’s good in some ways but bad in other ways. It’s just all tradeoffs. And you can’t see those tradeoffs unless you have people that really represent those different points. And I think that’s really great.
> 
> To me, the frustration sets in when the [Core Team](https://swift.org/community/#community-structure) comes out and says, [“we’re not going to talk about changing keywords”](https://forums.swift.org/t/rejected-se-0159-fix-private-access-levels/5576), and then the debate rages on about changing keywords. That’s not super productive, but that’s at least easy to ignore.

# Comparing the Swift 4 release to the Swift 3 release

_(40:38)_

> **Lattner:** Swift 3 started out with [a long list of goals](https://github.com/apple/swift-evolution/blob/30889943910a4a4e46a800f03d17a91e11ca475f/README.md#development-major-version--swift-30) and then the goals got whittled down as time rolled on. That list of goals was largely my fault. Managing software is hard, planning is hard, and then open source and thousands of people descending on the project like it happened was kind of unplanned. Awesome, but unplanned.
> 
> Swift 3 pivoted about halfway through: the main goal [changed from ABI stability](https://forums.swift.org/t/winding-down-the-swift-3-release/2631) to source stability. And I think that was totally the right thing to do. … What we realized halfway through the Swift 3 development cycle was, as the community is growing and as more and more people are writing more and more code, _not_ breaking that code became really important. … One of the reasons we started out by saying that Swift is not source-stable is that we knew that before the open-source release we didn’t have the benefit of lots of people debating, discussing, arguing, and [bikeshedding](https://en.wikipedia.org/wiki/Law_of_triviality). And you really need that to make something great.
> 
> …

# On leaving Apple

_(54:03)_

> **Lattner:** Deciding to move on from being an active committer to Swift was a big and hard decision for me. I obviously still love Swift and it’s super important to me, which is why I’m here and why I stay involved in the Core Team meetings and Evolution. It’s not because I love bikeshedding, believe it or not.
> 
> But the thing to think about is that the Swift team is really amazing. How shall I say this without it sounding weird? Losing me was not a big loss because you have people like [Doug Gregor](https://twitter.com/dgregor79) and [Joe Groff](https://twitter.com/jckarter) and [John McCall](https://twitter.com/pathofshrines) and countless other people. And the thing about [Ted](https://twitter.com/tkremenek) that many people don’t recognize is that he has been running things for a long time. And so in many ways it’s about making official what was already happening. And Ted is the mastermind in many, many ways. So the Swift team at Apple is super, super amazing. And I’m sure you guys have seen that. So they just didn’t need me in that sense.
> 
> Now that said, it’s super hard because it’s an amazing team and so many great people, beyond their abilities, but it was time to move on.

# On Swift as a server language

_(1:02:16)_

> **Lattner:** … From a technical perspective Swift has a lot to offer. If you compare it to Go, Node.js, Ruby, PHP, any of those … there’s the beancounter aspect too: Swift code runs faster. If you’re building cloud apps, then you’re paying for the CPU utilization, you’re often paying for the memory utilization as well. And Swift just runs faster, performs better, and uses less memory. And so that turns into dollars. …
> 
> Java is an interesting one because Java runs fast. It’s a super mature ecosystem, the VMs are really good. It’s not about the CPU utilization with Java, it’s more about the fact that a comparable Swift app will usually use about three or four times less memory. And that can be a big deal.

# On metaprogramming and dynamic features in Swift

_(1:04:27)_

> **Lattner:** My take on that is that it’s a question of prioritization, not a “will it ever happen?” question. For sure, most people, including the Swift team, want reflective capabilities. But a lot of people want code to compile faster too.
> 
> When setting out on the goals for Swift 4 and the goals for Swift 5, which is now Ted’s challenge, you have to be careful how you define the scope. Because if you overreach, stuff doesn’t happen or you get a bunch of stuff that’s half done and that’s not good either.
> 
> [The `Codable` stuff in Swift 4](https://github.com/apple/swift-evolution/blob/master/proposals/0166-swift-archival-serialization.md) is one example [how we try to balance this]. … There is a generally useful language feature to implement this. In that case it’s static reflection, in other words macros. [Hygienic macros](https://en.wikipedia.org/wiki/Hygienic_macro) are really great for solving certain classes of problems. But that’s a big feature that’s open-ended and requires a huge design process.
> 
> But when and if this finally has time to be designed, then it would subsume the current synthesization of `Codable`, `Hashable`, `Equatable`, and that kind of mechanical stuff. And when that happens, the current implementation will get sucked out of the compiler and put in the standard library and that will be a beautiful day. But that doesn’t mean we should prevent building that feature now, which is solving real problems and making the language more usable in really important ways.
> 
> When we talk more about general reflective capabilities, and I don’t know specifically which ones you’re thinking about, there is progress in Swift 4 with the [key path work](https://github.com/apple/swift-evolution/blob/master/proposals/0161-key-paths.md). It doesn’t solve all of those problems, but a large class of problems in a really nice, type-safe and expressive way. And bricks are being placed so that when there is time there is a nice house to build reflective technology on top of. Actually, in Swift 3, a lot of the work went in to lay out runtime metadata for objects, which powers the Xcode heap debugger. What we’re missing is an API to wrap that so that you can actually reflect on something and then, say, walk all the instance variables, or even reflect on a closure and walk all the state that it closes over. So the runtime has all that stuff, it just hasn’t been designed and built out. And I don’t know when, but I do expect that to become a priority.
> 
> > I hope that something like async/await will be at the top of the list of goals for Swift 5.
> 
> You brought up concurrency as well. I think concurrency is a super high priority going beyond Swift 4. I don’t know what the formal goal for Swift 5 will be, but I really hope that something like [async/await](https://en.wikipedia.org/wiki/Await) will be at the top of the list. … We’ll see. A lot of it depends on how Swift 4 finishes up.

# On the origins of Swift

_(1:10:56)_

> **Lattner:** Swift started in 2010. That’s when I started hacking on it. No small part of that was because we just finished [Clang](https://en.wikipedia.org/wiki/Clang) C++ support. And I wouldn’t say writing C++ compilers is fully soul-destroying _[audience laughs]_, but it is challenging, and it is hard to escape that process without wondering, having done this and proven it’s possible, what would a good language look like?
> 
> For me personally [at that point] it was just, “let’s start hacking, let’s start building something, let’s see where it goes pulling on the string”. It wasn’t a formal, official process or project or anything like that. It was just, “let’s do something fun and then see what happens”, with no expectation of world domination.
> 
> As Swift eventually became more well-known within Apple there were a lot of discussions, and one of the big questions that was raised frequently was, “[instead of] doing a new language why not make Objective-C better?”. And so if you recall, between 2010 and 2014 Objective-C became a lot better. [ARC](https://clang.llvm.org/docs/AutomaticReferenceCounting.html) came out. ARC was one of the first major steps that was driven by Swift that is general goodness, made Objective-C better, and had to be done as a prerequisite to make Swift happen because you can’t make something memory-safe if it’s not automated. Other things like [modules](https://clang.llvm.org/docs/Modules.html), even small things like [Objective-C literals](https://clang.llvm.org/docs/ObjectiveCLiterals.html) were all about pushing Objective-C closer and closer to Swift so that when it came out it felt more obvious.
> 
> > Why do a new language instead of making Objective-C better? The answer basically came down to C.
> 
> In the internal discussion the real question came down to, “why would we do a new language instead of making Objective-C better?”. And the answer basically came down to C. Objective-C is built on top of C and C has things like pointers. If you take pointers out of Objective-C, you get a different language anyways because so much of what you do in Objective-C revolves around pointers. And getting rid of @ signs is not a big enough improvement. Square brackets vs. parentheses, reasonable people can disagree, it’s not worth making a massive change. So if you’re going to massively break source, you might as well start over from scratch and do something that’s really great, that you can build on as a new platform. And then make sure that it works really well together with all the existing code.

# In which fields would you like to see Swift in the future?

_(1:15:32)_

> **Lattner:** My goal for Swift has always been and still is total world domination. It’s a modest goal. _[Applause]_ But this is not Swift 5 we’re talking about. This is a 10- or 15- or 20-year goal. So how are we going to achieve that? It’s the same process as writing a big app: you take the goal and decompose it into subproblems and then solve the individual problems. And the way you get to world domination with a language is you have to have a killer app first. You have to have a reason for a community to learn that programming language. There are so many languages that exist out there that nobody uses. And with Swift, that was clearly iOS programming.
> 
> > My goal for Swift has always been and still is total world domination. It’s a modest goal.
> 
> And once you have that, then you have this amazing thing. You get programmers that are smart and push the boundaries and want more. And they also work on other things [beside iOS apps]. Look at Javascript or any of these other languages out there. They started with a simple premise (“I want to do simple scripting in a web browser”) and now people are writing freaking server apps in it. What happened there? Is there a logical leap that was missed? How is this a good idea? _[Audience laughs]_ Sorry, I love Javascript too. I’d just love to kill it even more.
> 
> What happens is that communities evolve. They grow and they push the boundaries and that’s totally awesome. I think that one of the key things to the design of Swift very early on was designing for generality. It wasn’t designed as the minimal increment on top of Objective-C to get rid of semicolons. If that were the case, it would look a lot more like Objective-C, and the type system wouldn’t have nearly the features that it does. It also may have been completely dependent on Objective-C, which would have made Swift on the server and Swift on Linux not really possible. One of the cool things about Swift on Linux is that you can use Swift completely standalone, without having Objective-C dependencies in it.
> 
> When I look at Swift as a world domination goal, the way to solve this problem is to build something general that can solve a really important class of problems, you get an amazing community, and then you start solving problems that prevent it from being used in other spaces.
> 
> The current battle going on right now is on the front of server development. And that’s not an accident. It’s the next natural extension out from the app development world. You get a lot of people that want to solve the same problems on the client and the server, and share data structures and things like that. You also need very similar kinds of features from a language level. I think the number one thing that will be transformative in the server development space is when the concurrency features start to come in. That’s the thing that is really missing, that really hurts when you’re building server apps. And it’s really just a matter of time before that happens. With patience, that will unblock the next level of adoption and get more people going. With that I think Swift has a pretty credible shot to be a Java-class language, which can be used by a lot of application-level things. And as, for example, regular expression literals come in, that will be a beautiful day someday which makes Swift even more awesome for scripting. And now you have something that can span applications, server, scripting. And there’s obviously work to be done on libraries and other pieces like that.
> 
> > Killing C++ is really the unsolved problem, and it totally has to happen.
> 
> But to me, the real killer feature, which is probably three or four years out, is systems development. Killing C++ is really the unsolved problem, and it totally has to happen. Because C++, while practical, and it’s really the only practical answer for some tasks, has its own class of problems because it’s built on the unsafety of C. Which means that all the applications that are built from that world are suffering. If and when we get Swift to the point where it can solve that class of system programming things, that’s where it gets opened up to an entire community of people, for example game developers that are writing console games, that really care about that last ounce of performance. And they need to be saved from C++.
> 
> There’s always a time delay between making it possible and then seeing it happen. And so Swift on the server today is possible, but it’s still pretty early days. The year after that, hopefully with concurrency features, it will become really appealing. But still, I don’t expect people to rewrite all of their backend stuff over night. You look 5, 10, 15 years down the line and that’s where, assuming things go well, it could be a very different world. And that’s a very exciting world to be in the early days of.

# On Swift’s similarities with Kotlin

_(1:24:26)_

> **Lattner:** Swift and [Kotlin](https://en.wikipedia.org/wiki/Kotlin_%28programming_language%29) evolved at about the same point in time with the same contemporary languages around them. And so the surface-level syntax does look very similar. … But if you go one level down below the syntax, the semantics are quite different. Kotlin is very reference semantics, it’s a thin layer on top of Java, and so it perpetuates through a lot of the Javaisms in its model.
> 
> If we had done an analog to that for Objective-C it would be like, everything is an `NSObject` and it’s [`objc_msgSend`](https://developer.apple.com/documentation/objectivec/1456712-objc_msgsend) everywhere, just with parentheses instead of square brackets. And a lot of people would have been happy with that for sure, but that wouldn’t have gotten us the functional features, that wouldn’t have gotten us value semantics, that wouldn’t have gotten us a lot of the safety things that are happening [in Swift].
> 
> I think that Kotlin is a great language. I really mean that. Kotlin is a great language, and they’re doing great things. They’re just under a different set of constraints.

# How do you decide which features to add to Swift (case in point: abstract classes)?

_(1:31:54)_

> **Lattner:** Swift is unapologetic about stealing good ideas from wherever they can come from. There’s even some [Dart](https://en.wikipedia.org/wiki/Dart_%28programming_language%29) features in Swift, like the way it handles string escapes. So it’s not really where it comes from, and Swift isn’t trying to ape some other language in any way. It’s about taking the best ideas.
> 
> > Swift is unapologetic about stealing good ideas from wherever they can come from.
> 
> Now, what is a good idea? Are abstract classes a good idea? That’s a harder thing. Abstract classes actually have been debated on evolution and it’s gone back and forth. I personally am in the “abstract classes would be a good thing in principle” camp. But then it’s also a prioritization question. There’s a lot of other things that people want to have, namespaces for example.
> 
> > A lot of people that say subclassing is bad are reacting to the overclassification of Objective-C.
> 
> What irritates me is when people say classes are bad. Or subclassing is bad. That’s totally false. Classes are super important. Reference semantics are super important. If anything, the thing that’s wrong is to say, one thing is bad and the other thing is good. These are all different tools in our toolbox, and they’re used to solve different kinds of problems. And the bad thing is to say, classes are awesome and should be used to solve all problems, or structs are awesome and should be used to solve all problems. I think a lot of people that say subclassing is bad are reacting to the “overclassification” of Objective-C.

# Didn’t Apple promote the idea that classes are bad with the protocol-oriented programming session at WWDC?

_(1:35:05)_

> **Lattner:** The [protocol-oriented programming talk](https://developer.apple.com/videos/play/wwdc2015/408/) was two years ago. It was the unveiling [of protocol extensions]. That was to expose the community to a new way of thinking about things. In fact, if you watch the talk [Dave Abrahams](https://twitter.com/daveabrahams) said, classes are good for this and this and this reason. The point of that talk was to challenge the way people thought about things and explain the new feature of protocol-oriented programming, which is quite different from the way that most people approach extending their types.

# On making Swift a great language for teaching

_(1:37:32)_

> **Lattner:** I don’t know if I should say this or not, but one of the original ideas for playgrounds was to get on the iPad. So it was designed to get to the iPad, though that was not the practical place to start.
> 
> > One of the original ideas for playgrounds was to get on the iPad.
> 
> Making Swift teachable was a really important goal. The concept of [progressive disclosure](http://bitsplitting.org/2017/01/18/progressive-disclosure-in-swift/) in Swift, where you can start with something very simple and then learn complexity as you go, was totally driven by making it teachable. I personally spent a lot of time trying to make sure that the introduction to Swift could just be `print("Hello World")`. No semicolons, no `\n`s, none of that `public static void main` stuff. Making it simple and approachable was a strong goal, and not in a weird way where in a teaching environment there is this “Swift Prime” language that’s similar but different.
> 
> To me that was about designing it for generality, and designing it not just to be teachable to people that are completely new to programming, but also to “normal” programmers who know the common parts of the language they use on a day-by-day basis, but then come up against a more advanced feature. And Swift is not a simple language. It’s actually a large language that is complicated in the corners and in the edges, but that’s okay so long as you don’t run up against that every single day. If you’re a math geek you can think about it as kind of [Huffman encoding](https://en.wikipedia.org/wiki/Huffman_coding), so the common case is really familiar and the uncommon case uses a longer encoding and you have to look it up when you don’t know it. That was really intentional and part of the design.

# And finally…

[That settles it then.](https://twitter.com/olebegemann/status/878267880495865858) “Obviously”.
