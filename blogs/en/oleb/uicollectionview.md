---
title: UICollectionView
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2012/09/uicollectionview/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:3213fa876eb5ec0c'
translated: false
---

> 原文：[UICollectionView](https://oleb.net/blog/2012/09/uicollectionview/)　·　Ole Begemann

# UICollectionView

If you are an iOS developer, chances are that at some point in your career you have thought about writing (or you have in fact written) your own custom grid view.

# Let’s Design a Grid View

Let’s imagine we want to write such a class. We might put a great deal of thought into the public API of our grid view, because [great API design is both really important and very hard](http://mattgemmell.com/2012/05/24/api-design/). We might decide on a great name for our class; calling it a `CollectionView` instead of the more obvious `GridView` is more generic and may better convey its purpose. We might choose a datasource-and-delegate-driven design, not only because it follows the [MVC pattern](http://developer.apple.com/library/ios/#documentation/general/Conceptual/CocoaEncyclopedia/Model-View-Controller/Model-View-Controller.html) but because mimicking the interface of a well-known related class from the platform owner (`UITableView`, in this case) makes our API so much easier to understand for fellow developers.

Taking even more cues from `UITableview`, we might consider making our collection view really fast by reusing cells as the content is scrolled. By using `NSIndexPath` objects to model cell positions and adapting the table view’s datasource and delegate methods to deal with a two-dimensional layout, we would end up with a pretty capable class. And I bet most of us would stop here.

If we had lots of time available, we might attempt to make the view extremely flexible by adding support for sections, supplementary and decoration views as well as tons of other customizable attributes, though this makes the code a good deal more complicated. While we’re at it, we could give the users of our class the choice between horizontal and vertical scrolling. We would be close to having the perfect grid view now.

But let’s not stop there. If we were really great developers, we might be able to give users a way to create truly flexible layouts. It wouldn’t matter whether a developer would want to arrange images in a plain grid, stack several cells on top of each other in a slightly disarranged way, display locations on a map or show events in a calendar’s week view. Our class could do it all.

Now, to top it off, add custom animations to the feature set. Whenever a cell is inserted into or deleted from the collection view, the developer should be able to specify the appropriate animation: animatable attributes should not just include the cell’s position but arbitrary attributes like alpha, scale and rotation. Specifying these animations should be so deceptively simple that a user of the class can’t believe how easy it is.

If we did all this, the result would be `UICollectionView`.

# The Awesomest UI Class I’ve Ever Seen

[`UICollectionView`](https://developer.apple.com/library/ios/#documentation/UIKit/Reference/UICollectionView_class/Reference/Reference.html) is spectacular. The combination of a clear interface and incredible flexibility make it an absolute masterpiece of API design. The UIKit engineers who designed it have truly outdone themselves. It is by far my favorite feature of the iOS 6 SDK. Make sure to watch [WWDC sessions 205 and 219](https://developer.apple.com/videos/wwdc/2012/) if you haven’t yet seen them.

The more I think about it, the ingenuity of Apple’s engineers is not only visible in the architecture of `UICollectionView` itself, with its support for flexible [`UICollectionViewLayout`s](https://developer.apple.com/reference/uikit/uicollectionviewlayout), which in turn support custom [`UICollectionViewLayoutAttributes`](https://developer.apple.com/reference/uikit/uicollectionviewlayoutattributes) that allow layout developers to customize every imaginable part of a cell.

To me, the same genius can be seen in [`UICollectionViewFlowLayout`](https://developer.apple.com/reference/uikit/uicollectionviewflowlayout), the standard layout implementation that comes with iOS 6. Far from just supporting plain grids, `UICollectionViewFlowLayout` is so flexible that it can be used as a basis for almost any cell layout I can imagine. It requires some real thinking outside the box by the author of the class to realize that the simple grid is just a special case of something so wonderfully flexible.

I tweeted this the other day:

> In a few months, GitHub will be full of UICollectionViewLayout subclasses.
> 
> [@olebegemann](https://twitter.com/olebegemann)
> 
> Ole Begemann
> 
> [September 19, 2012](https://twitter.com/olebegemann/status/248380531690045440)

Maybe, UICollectionView_Flow_Layout subclasses would have been more accurate.

# PSTCollectionView for iOS 5

PS: If you still need to support iOS 5, check out Peter Steinberger’s [`PSTCollectionView`](https://github.com/steipete/PSTCollectionView), an API-compatible re-implementation of Apple’s class for the older OSes. Awesome job by Peter. I can’t even imagine how much work this was.
