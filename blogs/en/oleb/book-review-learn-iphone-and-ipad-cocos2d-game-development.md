---
title: 'Book Review: Learn iPhone and iPad cocos2d Game Development'
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2011/06/book-review-learn-iphone-ipad-cocos2d-game-development/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:3e828bd6533086f3'
translated: false
---

> 原文：[Book Review: Learn iPhone and iPad cocos2d Game Development](https://oleb.net/blog/2011/06/book-review-learn-iphone-ipad-cocos2d-game-development/)　·　Ole Begemann

# Book Review: Learn iPhone and iPad cocos2d Game Development

[![Cover of Learn iPhone and iPad cocos2d Game Development](https://oleb.net/media/learn-iphone-ipad-cocos2d-game-development-cover-250px.png)](https://www.amazon.com/Learn-iPhone-iPad-cocos2d-Development/dp/1430233036/)

I recently found the time to learn a bit about game development on iOS, something I’ve been wanting to do for a long time. Most iOS games use OpenGL ES to get more performance and flexibility than what is possible with UIKit views and Core Animation layers. OpenGL is quite a different beast than those frameworks, though. For most iOS developers, the learning curve is very steep. And as soon as your game logic gets a little more complex, you make your life a lot easier by using an object-oriented game framework that builds on OpenGL ES.

# cocos2d

[cocos2d](http://www.cocos2d-iphone.org/) is the most popular game framework on the iOS platform. It started out as a Python project and was ported to the iOS platform by [Ricardo Quesada](https://twitter.com/ricardoquesada) as early as 2008. Now, three years later, it has become a very mature platform and is nearing its 1.0 release. As the project grew, the [documentation on the cocos2d website](http://www.cocos2d-iphone.org/wiki/doku.php/) has also improved. The quality of the online documentation is at a level that an experienced iOS developer does not necessarily need anything else to get started. Moreover, the project is open source and the code is relatively easy to read so the definitive reference is right there when you need it anyway.

# The Book

I still find it easier to learn a new technology with a book in hand and so I purchased [Learn iPhone and iPad cocos2d Game Development](https://www.amazon.com/Learn-iPhone-iPad-cocos2d-Development/dp/1430233036/) by [Steffen Itterheim](https://www.twitter.com/gaminghorror). If you’re in the market for a cocos2d book, Steffen’s is basically your only choice at the moment (Rod Strougo’s and Ray Wenderlich’s [Learning Cocos2D](https://www.amazon.com/Learning-Cocos2D-Hands--Building-Chipmunk/dp/0321735625/) will be the second one, coming out in July 2011). But even if there were dozens of other books on the topic, I would still highly recommend _Learn iPhone and iPad cocos2d Game Development_.

On fewer than 400 pages, Steffen manages to walk the reader through the entire framework. After introducing us to cocos2d’s design and core concepts, we get to build several nice sample games, each of them illustrating another feature of the framework:

- Sprites and how to animate them.
- Working with textures.
- Scrolling (including parallax scrolling).
- Collision detection.
- Particle effects.
- Map-based games (with both top-view and isometric maps).
- Working with the physics engines [Box2D](http://www.box2d.org/) and [Chipmunk](https://code.google.com/p/chipmunk-physics/). Both are not technically part of cocos2d but they ship with the source package and are easy to integrate with cocos2d.

# The Good

I still don’t know how Steffen managed to pack so much content into such a short book. And it’s not as if he doesn’t cover the topics in detail. After going through the book, I feel that I both have a pretty much complete overview over cocos2d and know quite a bit about its inner workings. Just about the only topic I missed was adding sound to a game (which Steffen mentions only briefly). But then, audio is not even a core part of cocos2d, though it ships with the [CocosDenshion](http://cocos2d-iphone.org/wiki/doku.php/cocosdenshion:faq) audio library.

Also, keep in mind the book was published in December 2010 and thus does not cover some of the most recent cocos2d changes. For example, Steffen does not cover how to prepare your game for the iPhone 4’s retina display. Those things are easy to pick up from the cocos2d website or with a bit of googling, though.

My favorite feature of the book is that it also introduces several third-party tools that help developers prepare their game’s content, such as the awesome [Zwoptex](http://zwoptexapp.com/) for generating sprite sheets and [Particle Designer](http://particledesigner.71squared.com/) for designing particle effects. These tools work hand in hand with cocos2d and conveniently produce files that the framework can read just like that. Finding these tools without the book would have involved a lot of googling.

# The Not Just as Good (But Not Bad)

One thing I did not like 100% is Steffen’s coding style. In his custom classes, he prefers to maintain weak references to cocos2d objects and relies a lot on the fact that objects in the cocos2d node hierarchy are retained by their parent nodes. Translated to UIKit programming, this is comparable to having your view controller not retain an outlet ivar (e.g., to a `UIButton`) because you can be sure that the view controller’s view will retain the button anyway. This frees you from releasing the button when the view gets unloaded. One can certainly do it that way, I just dislike it because it does not feel right to me: if an object needs to have another object around, it should retain it. It also does not follow Apple’s practice.

Another thing that did not affect me but I think could be improved is the book’s intro to Objective-C for newbies to the language. The introduction just a few pages long and as mentioned above, Steffen’s advice on memory management contradicts Apple’s in a few places, which can easily confuse beginners. In my opinion, the book should not claim to be suitable for newbies to the iOS platform. You will need at least another book.

# The Conclusion

All in all, highly recommended.
