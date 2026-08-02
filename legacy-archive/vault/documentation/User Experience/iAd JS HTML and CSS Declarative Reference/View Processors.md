---
title: iAd JS HTML and CSS Declarative Reference
apple_id: TP40010163
resource_type: Guide
platform: iAd Producer|iOS
topic: User Experience
technology: iAd JS
published: '2012-12-13'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Reference/iAdJSDeclarativeRef/Articles/ViewProcessors.html
archived_at: '2026-07-18T02:14:10.621695Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [iAd JS HTML and CSS Declarative Reference](Introduction.md)


[Next](View%20Controller%20States.md)[Previous](iAd%20JS%20Declarative%20Classes.md)

# View Processors

View processors are powerful HTML attributes you can add to any HTML element in your iAd to dramatically simplify interactions between your HTML content and your ad’s view controllers.

The `data-ad-outlet` HTML attribute provides an element’s view controller with a reference to the element. All of a view controller’s outlets are accessible from the view controller’s `outlets` property. For example, the `div` element in the example below is accessible from `outlets.myDiv`.


```
<div data-ad-outlet="myDiv"></div>
```


Available in iAd JS 1.1 and later.

The `data-ad-action` HTML attribute registers a callback with an element’s view controller. User interaction with the element automatically triggers the callback. The view controller simply needs to the implement the callback. For example, the `div` element in the example below registers the `performAction` callback with its view controller.

You should not register a callback to handle transitions to other view controllers; use the `data-ad-transitions-to` HTML attribute instead.


```
<div data-ad-outlet="performAction"></div>
```


Available in iAd JS 1.1 and later.

The `data-ad-transitions-to` HTML attribute sets up a transition to another view controller that occurs when a user interacts with an element. The value you provide is the value of the view controller’s `id` property. For example, the `div` element in the example below sets up a transition to the `map` view controller.


```
<div data-ad-transitions-to="map"></div>
```


Available in iAd JS 1.1 and later.

[Next](View%20Controller%20States.md)[Previous](iAd%20JS%20Declarative%20Classes.md)

