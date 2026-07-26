---
title: How I Learned to Stop Worrying and Love Cocoa Auto Layout
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2014/03/how-i-learned-to-stop-worrying-and-love-auto-layout/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:7451f8d4c6882866'
translated: false
---

> 原文：[How I Learned to Stop Worrying and Love Cocoa Auto Layout](https://oleb.net/blog/2014/03/how-i-learned-to-stop-worrying-and-love-auto-layout/)　·　Ole Begemann

# How I Learned to Stop Worrying and Love Cocoa Auto Layout

I made my peace with [Cocoa Auto Layout](https://developer.apple.com/library/ios/documentation/userexperience/conceptual/AutolayoutPG/Introduction/Introduction.html) when I realized how easy it is to mix with manual layout code.

Despite being almost three years old (on the Mac) and having vastly better tool support than in its early stages, Auto Layout remains [a complex topic](http://carpeaqua.com/2012/11/02/issues-with-achieving-auto-layout-zen/). Adopting it requires a totally [different mindset](https://oleb.net/blog/2013/03/things-you-need-to-know-about-cocoa-autolayout/) than the old approach of setting view frames directly. And while Auto Layout clearly is the future and I strongly encourage you to use it wherever practical, there are some cases where Auto Layout seems to create more problems than it solves:

- Animating views under Auto Layout

  requires you to animate the constraints directly, which can be a pain.
- Auto Layout does not play nicely with view transforms

  .
- Auto Layout can be too slow

  .

# Mix Auto Layout With Manual Layout Code

If you find yourself in a situation that is difficult to solve with Auto Layout, just don’t use it for that particular view. You can freely mix the constraint-based layout with manual layout code, even within the same view hierarchy.

Consider this example: one of your custom views contains several subviews, you are using Auto Layout to position all but one of them. This last subview has a scale and rotation transform applied that conflicts with the constraint-based layout, so you don’t apply any constraints to it. (This works best for views that are created in code since Xcode 5 tries to be smart for views in Auto Layout-enabled NIBs and adds missing constraints at build time. You should also set `translatesAutoresizingMaskIntoConstraints = NO` on the view since you will position and size it manually, anyway.)

## Just Another Step In layoutSubviews

You can think of Auto Layout as just an additional step that runs automatically in your view’s [`layoutSubviews`](https://developer.apple.com/library/ios/documentation/uikit/reference/uiview_class/UIView/UIView.html#//apple_ref/doc/uid/TP40006816-CH3-SW27) method. The Auto Layout algorithm performs some magic[1](#fn:1), at the end of which your subviews’ frames are set correctly according to the layout constraints. When that step is done, the Auto Layout engine halts until a relayout is required (for example, because the parent view size changes or a constraint gets added). What you do to your subviews’ frames after Auto Layout has done its job, doesn’t matter.

## Override layoutSubviews

All you now have to do is override `layoutSubviews` (or `viewDidLayoutSubviews` if you want to do this in a view controller), call `super` (which performs the Auto Layout step) and then perform any manual layout we want to add:

```
- (void)layoutSubviews
{
    // Important. This lets the Auto Layout engine do its job.
    [super layoutSubviews];

    // Now all subview frames are set according to their constraints.
    // We can freely reposition and/or resize any view here, even one
    // that has already been positioned with Auto Layout (that is not
    // recommended, though).

    // Here, we position and size a view we want to lay out manually.
    // Don't modify the frame directly because the view has a transform
    // applied.
    self.manualLayoutView.bounds = CGRectMake(...);
    self.manualLayoutView.center = CGPointMake(...);
}
```

This technique should be used sparingly, but I found that in some cases it can really simplify my code. It is also useful when transitioning an existing code base to Auto Layout in small steps.

---

**Update September 11, 2015:** The technique I discussed above works by overriding the layout system after it has done its job. It’s not very elegant. In WWDC 2015 session 219, [Mysteries of Auto Layout, Part 2](https://developer.apple.com/videos/wwdc/2015/?id=219), Apple engineers presented a different and cleaner solution.

Contrary to my advice above, you should make sure the view you want to position manually has its `translatesAutoresizingMaskIntoConstraints` property set to `YES` (the default for views created in code). This tells Auto Layout to generate constraints that enforce the frame you set on the view in the layout engine. Or, as the presenter put it in

> It makes views behave the way that they did under the legacy layout system but in an Auto Layout world.

That way, whenever you modify the view’s frame, the layout engine will update the constraints it added and your view will get repositioned. I haven’t tested whether this approach works in all situations I mentioned above (such as changing the view’s `transform`), but you should definitely use this approach if it works for you.

I highly recommend that WWDC session if you want to learn more about Auto Layout.

1. Actually, it solves a system of linear equations (the layout constraints), which is [very well documented](http://stacks.11craft.com/cassowary-cocoa-autolayout-and-enaml-constraints.html). But you can think of it as a black box that magically sets your subviews’ frames. [↩︎](#fnref:1)
