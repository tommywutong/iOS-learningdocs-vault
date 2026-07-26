---
title: 'Making News Feed nearly 50% faster on iOS'
source: Meta Engineering — iOS
source_key: fbeng
source_url: 'https://engineering.fb.com/2014/10/31/ios/making-news-feed-nearly-50-faster-on-ios/'
original_language: en
published: 2014-10-31
status: active
license: © Meta → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:322fbbdc1ca59d0f'
translated: false
---

> 原文：[Making News Feed nearly 50% faster on iOS](https://engineering.fb.com/2014/10/31/ios/making-news-feed-nearly-50-faster-on-ios/)　·　Meta Engineering — iOS

Our engineering team spends a lot of time and effort making News Feed reliable, simple, and fast. Almost two years ago, we switched the Facebook iOS app [from HTML5 to native iOS code](https://engineering.fb.com/posts/347875255344145/under-the-hood-rebuilding-facebook-for-ios/) to optimize performance.

Our work didn’t stop with News Feed. We wanted to bring the same speed to other parts of the app, so in later updates we also introduced native rewrites for Timeline, Groups, Pages, Search, and more. But we began to notice something curious – News Feed was getting slower with each release. With each update it would take a tiny bit longer for News Feed to load, and it began to add up.

What was going on? To figure it out, we added instrumentation to each step in the process of loading News Feed — network, parsing, data processing, layout calculations, and view creation. What we found surprised us — the problem was in our data model layer. With each passing release, the time it took to create and query model objects was longer and longer. Only turning to a brand new model layer would solve the slowdown.

## Data models on iOS

First, let’s talk about how News Feed was designed to work on iOS. The Facebook APIs we use serve as a JSON representation of the stories in your News Feed. Because we didn’t want UIViews to consume JSON directly — there are no type safety or hints about what fields you can expect to get from the server — we create intermediate data models from JSON and used those to power the user interface. Like most iOS apps, we chose to use the system default framework for managing data models: Core Data. Already built into iOS and very well documented, it allowed us to get the native rewrite out the door without reinventing the wheel.

Returning to our performance problems, though, we found that Core Data had a quirk. As we ported more features, our Core Data database slowed down. We started with only a few dozen entities in Core Data, but this had ballooned to hundreds. Some of those entities had a lot of fields — Pages, for example, had more than 100!

Under the hood, Apple’s Core Data framework uses SQLite to store data. As we added more entities and more fields, the number of tables, columns, and indexes grew. Core Data stores data in a fully normalized format, so each time we encountered a Pages object in JSON, we would have to perform a fetch-or-create in Core Data and then update the page. Saving would touch dozens of indexes in SQLite, thanks to an enormous number of relationships (i.e., how many things reference people or Pages objects on Facebook).

We realized that while Core Data had served us well in the beginning, we needed to go without some of its features to accommodate our scale. We set about replacing it with our own solution, resulting in News Feed performing nearly 50% faster on iOS.

## A new model layer

Core Data is at heart an object-relational mapper (ORM). It provides features like full normalization and synchronous consistency across multiple isolated contexts.

But since the Facebook app is essentially a cache for data that lives on the server, a completely normalized representation of data wasn’t needed. All of those fetch-or-creates while parsing JSON objects were resource-intensive and unnecessary. When data is downloaded from a Facebook server, it’s already as up-to-date as it can be.

We sought a system that was consistent — if someone likes a post on one screen, other screens should update accordingly — yet we balanced that by settling for asynchronous eventual consistency, rather than the synchronous consistency guaranteed by Core Data. In Objective-C parlance, we wanted the ability to “dispatch_async” the consistency operations on our object graph.

We developed our own bare-bones form of model objects guided by three principles:

1. Immutability. In this new data layer, models are completely immutable after creation. To modify even a single field, a developer must create an entirely new model object. This might seem crazy at first, but since you can’t modify the object, there’s no need for locks; thread safety becomes trivial. This also allows us to write code in a dataflow (or “functional reactive”) pattern, which we’ve found reduces programmer error and makes code clearer.
2. Denormalized Storage. To serialize these models to disk, we chose to use NSCoding. With each part of the app assigned its own cache, there is no longer contention for the single Core Data store shared by the entire app. It also ensures that products that don’t want to cache to disk don’t have to.
3. Asynchronous, Opt-In Consistency. By default, there are no consistency guarantees. By making consistency opt-in instead of opt-out, we were able to ensure that database indexes are not used in situations where consistency is unnecessary. To opt-in, a developer passes a model to a consistency controller; when it detects that a consistent field has changed inside the model, it hands the developer a new model with those updates. Behind the scenes, this consistency controller uses a GCD background queue to compute these updates, ensuring we never block the main thread.

Taking a cue from “POJOs” in Java, we refer to these objects as “PONSOs,” or plain ol’ NSObjects.

## Porting feed

After creating our own model objects, one major roadblock remained. News Feed had been written with the assumption that it would be rendered using a Core Data model, but now we might have only had an equivalent PONSO. However, we didn’t want to rewrite all of News Feed to use only PONSOs since we wanted to A/B test the rollout of these new model objects.

The solution was a clever use of protocols. For each type of object, we used a script to code-gen a protocol that represented a model-agnostic interface. Both the Core Data object and the PONSOs adopted this protocol, and we migrated News Feed code bit-by-bit to use these new protocols instead of hard-coded references to Core Data classes. When the last hard-coded Core Data reference was migrated, we were ready to launch.

## The launch

We used our [Airlock system](https://engineering.fb.com/posts/520580318041111/airlock-facebook-s-mobile-a-b-testing-framework/) to gradually introduce this new version of News Feed to the public. This framework helped us verify that iOS News Feed was nearly twice as fast under the new framework. Our work won’t stop there, of course—we’ve got more improvements coming, so look forward to an even snappier News Feed soon!

_Adam Ernst, a software engineer at Facebook New York, will be speaking at the New York Mobile Forum on Thursday, October 30th, along with engineers from Etsy, Pixable, Tumblr, Vine, and more. To learn more and apply for the Forum, visit http://newyorkmobileforum.splashthat.com/._
