---
title: NSHipster on UICollectionView
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2012/09/nshipster-on-uicollectionview/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:72ce50d0eb9b0047'
translated: false
---

> 原文：[NSHipster on UICollectionView](https://oleb.net/blog/2012/09/nshipster-on-uicollectionview/)　·　Ole Begemann

# NSHipster on UICollectionView

In [last week’s post on `UICollectionView`](https://oleb.net/blog/2012/09/uicollectionview/), I did not go into detail how to actually use it. Matt Thompson wrote an [NSHipster post that does just that](https://nshipster.com/uicollectionview/). Comparing the `UICollectionView` API to `UITableView`, Matt nicely outlines the design similarities between the two components. He also explains how collection views implement their dynamic layouts, making them so much more flexible than tables.

`UICollectionView` is a central component for Apple to enable better app design for multiple screen sizes, especially for bigger screens where table views just don’t cut it:

> Since the introduction of the iPad, there has been a subtle, yet lingering tension between the original UI paradigms of the iPhone, and the demands of this newer, larger form factor. With the iPhone 5 here, and a rumored “iPad mini” on the way, this tension could have threatened to fracture the entire platform, had it not been for UICollectionView (as well as Auto-Layout).

Matt shares my enthusiasm for the design of the class:

> There are a million ways Apple could (or could not) have provided this kind of functionality, but they really knocked it out of the park with how they designed everything.
> 
> The clean, logical separation between data source and layout; the clear division between cell, supplementary, and decoration views; the extensive set of layout attributes that are automatically animated… a lot of care and wisdom has been put together with these APIs.
> 
> As a result, the entire landscape of iOS apps will be forever changed. With collection views, the aesthetic shift that was kicked off with the iPad will explode into an entire re-definition of how we expect apps to look and behave.
