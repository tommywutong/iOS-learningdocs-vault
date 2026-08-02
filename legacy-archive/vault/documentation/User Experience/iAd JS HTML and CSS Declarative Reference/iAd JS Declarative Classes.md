---
title: iAd JS HTML and CSS Declarative Reference
apple_id: TP40010163
resource_type: Guide
platform: iAd Producer|iOS
topic: User Experience
technology: iAd JS
published: '2012-12-13'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Reference/iAdJSDeclarativeRef/Articles/DeclarativeClasses.html
archived_at: '2026-07-18T02:14:08.578679Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [iAd JS HTML and CSS Declarative Reference](Introduction.md)


[Next](View%20Processors.md)[Previous](Introduction.md)

# iAd JS Declarative Classes

Each iAd JS declarative CSS class corresponds to an iAd JS JavaScript class. You can customize the properties of these classes with a combination of additional CSS classes, CSS properties, and HTML attributes.

To enable the use of iAd JS declarative classes in your HTML document, assign the `ad-root-view` CSS class to an element that encloses all other uses of declarative classes in your document. The `body` element is best suited for this purpose, but other elements (such as `div`) work as well if necessary. Document fragments that are loaded by view controllers do not require an element with the `ad-root-view` class.

When you assign one of these CSS classes to an HTML element, each CSS class that represents a superclasses of that class is assigned to the element automatically. For example, if you assign the `ad-table-view` CSS class to a `div` element, the `ad-scroll-view` and `ad-view` CSS classes are also assigned to it automatically.

Certain declarative CSS classes, such as carousel views and table views, must provide their contents in a specific format. See the declaration examples for a proper implementation of each class.

Any additional CSS classes should be included in the `class` attribute of your HTML element, alongside the CSS class that represents the JavaScript class itself.

CSS properties are most easily included in the `style` attribute of your HTML element.

Read iAd JS Declarative Interface in _iAd JS Programming Guide_ for further discussion and examples of using iAd JS declarative classes.

The `ad-view` CSS class corresponds to the `iAd.View` JavaScript class.


```
<div class="ad-view" style="[css-properties]"></div>
```



```
<div class="ad-view" style="width:50px; height:50px; x:0px; y:0px;"></div>
```


The following CSS properties set additional JavaScript properties of a view.

| CSS Property | Description | Corresponding JavaScript Property |
| --- | --- | --- |
| `width` | The width of the view.  Available in iAd JS 1.0 and later. | `size``.width` |
| `height` | The height of the view.  Available in iAd JS 1.0 and later. | `size``.height` |
| `x` | The x-coordinate of the origin of the view in its superview coordinates.  Available in iAd JS 1.0 and later. | `position``.x` |
| `y` | The y-coordinate of the origin of the view in its superview coordinates.  Available in iAd JS 1.0 and later. | `position``.y` |
| `z-index` | The view’s z axis coordinate.  Available in iAd JS 1.0 and later. | `zIndex` |
| `opacity` | The view’s opacity.  Available in iAd JS 1.0 and later. | `opacity` |
| `overflow` | Defines the treatment of content that overflows the view’s bounds.  Available in iAd JS 1.0 and later. | `clipsToBounds` |
| `-webkit-backface-visibility` | Determines whether or not a transformed element is visible when it is not facing the screen.  Available in iAd JS 1.0 and later. | `doubleSided` |
| `-webkit-transform` | Specifies transformations to be applied to the view.  Available in iAd JS 1.0 and later. | `transform` |

The following HTML attributes set additional JavaScript properties of a view.

| HTML Attribute | Description | Supported Values | Corresponding JavaScript Property |
| --- | --- | --- | --- |
| `id` | A unique identifier for this view that corresponds to its layer’s identifier.  Available in iAd JS 1.0 and later. | Any | `id` |

Available in iAd JS 1.0 and later.

The `ad-root-view` CSS class corresponds to the `iAd.RootView` JavaScript class. The presence of this class enables the use of iAd JS declarative CSS classes in your HTML document. The element with this class must enclose all other uses of declarative classes in your HTML document. This class is typically assigned to the `body` element of your HTML, but other elements work as well if necessary.


```
<body class="ad-root-view"></body>
```



```
<body class="ad-root-view"></body>
```


Available in iAd JS 1.0 and later.

The `ad-bar-button` CSS class corresponds to the `iAd.BarButtonItem` JavaScript class.


```
<div class="ad-bar-button [css-classes]" style="[css-properties]" [html-attributes]></div>
```



```
<div class="ad-bar-button ad-square ad-done" style="max-width:50px;" data-ad-title="MyBarButton"></div>
```


The following CSS classes correspond to values for a bar button’s `type` JavaScript property.

| CSS Class | Description | Corresponding JavaScript Value |
| --- | --- | --- |
| `ad-plain` | A plain type with no background or borders—just displays plain text as the button.  Available in iAd JS 1.0 and later. | `TYPE_PLAIN` |
| `ad-square` | A square button type.  Available in iAd JS 1.0 and later. | `TYPE_SQUARE` |
| `ad-flexible-space` | A flexible spaced type.  Available in iAd JS 1.0 and later. | `TYPE_FLEXIBLE_SPACE` |
| `ad-fixed-space` | A fixed spaced type.  Available in iAd JS 1.0 and later. | `TYPE_FIXED_SPACE` |

The following CSS classes correspond to values for a bar button’s `style` JavaScript property.

| CSS Class | Description | Corresponding JavaScript Value |
| --- | --- | --- |
| `ad-black` | A black style.  Available in iAd JS 1.0 and later. | `STYLE_BLACK` |
| `ad-default` | The default button item style.  Available in iAd JS 1.0 and later. | `STYLE_DEFAULT` |
| `ad-done` | A light blue style.  Available in iAd JS 1.0 and later. | `STYLE_DONE` |

The following CSS properties set additional JavaScript properties of a bar button.

| CSS Property | Description | Corresponding JavaScript Property |
| --- | --- | --- |
| `max-width` | The maximum width of the button.  Available in iAd JS 1.0 and later. | `maxWidth` |

The following HTML attributes set additional JavaScript properties of a bar button.

| HTML Attribute | Description | Supported Values | Corresponding JavaScript Property |
| --- | --- | --- | --- |
| `data-ad-width` | The width of the item in pixels.  Available in iAd JS 1.0 and later. | Integers | `width` |
| `data-ad-title` | The title displayed on the item.  Available in iAd JS 1.0 and later. | Any | `title` |
| `data-ad-image` | A URL specifying the image used to represent the item.  Available in iAd JS 1.0 and later. | URLs | `image` |
| `data-ad-image-offset-x` | The horizontal offset from the top left origin of the item.  Available in iAd JS 1.0 and later. | Integers | `imageOffset``.x` |
| `data-ad-image-offset-y` | The vertical offset from the top left origin of the item.  Available in iAd JS 1.0 and later. | Integers | `imageOffset``.y` |

Available in iAd JS 1.0 and later.

The `ad-button` CSS class corresponds to the `iAd.Button` JavaScript class.


```
<div class="ad-button [css-classes]" [html-attributes]></div>
```



```
<div class="ad-button ad-rounded-rect-type" data-ad-title-for-normal-state="MyButton"></div>
```


The following CSS classes correspond to values for a button’s style.

| CSS Class | Description | Corresponding JavaScript Value |
| --- | --- | --- |
| `ad-custom-type` | A button with no preset style. You can use this type of button to create buttons with a custom CSS style.  Available in iAd JS 1.0 and later. | `TYPE_CUSTOM` |
| `ad-rounded-rect-type` | A rounded-rectangle style button.  Available in iAd JS 1.0 and later. | `TYPE_ROUNDED_RECT` |
| `ad-detail-disclosure-type` | A detail disclosure button.  Available in iAd JS 1.0 and later. | `TYPE_DETAIL_DISCLOSURE` |
| `ad-info-light-type` | An information button that has a light background.  Available in iAd JS 1.0 and later. | `TYPE_INFO_LIGHT` |
| `ad-info-dark-type` | An information button that has a dark background.  Available in iAd JS 1.0 and later. | `TYPE_INFO_DARK` |
| `ad-contact-add-type` | A button to add a contact to the user’s address book.  Available in iAd JS 1.0 and later. | `TYPE_CONTACT_ADD` |

The following HTML attributes set a button’s title for a given state. Setting these attributes is equivalent to calling the `setTitleForState` JavaScript method.

| HTML Attribute | Description | Supported Values |
| --- | --- | --- |
| `data-ad-title-for-normal-state` | The title to use for the button’s normal state.  Available in iAd JS 1.0 and later. | Any |
| `data-ad-title-for-highlighted-state` | The title to use for the button’s highlighted state.  Available in iAd JS 1.0 and later. | Any |
| `data-ad-title-for-disabled-state` | The title to use for the button’s disabled state.  Available in iAd JS 1.0 and later. | Any |
| `data-ad-title-for-selected-state` | The title to use for the button’s selected state.  Available in iAd JS 1.0 and later. | Any |

Available in iAd JS 1.0 and later.

The `ad-carousel-view` CSS class corresponds to the `iAd.CarouselView` JavaScript class.

The cells of a carousel view are declared as items in an unordered list. See the example.


```
<div class="ad-carousel-view" [html-attributes]></div>
```



```
<div class="ad-carousel-view" data-ad-cell-padding="5">
    <div class="ad-aligner">
        <ul class="ad-hosting-layer">
            <li>Contents of Cell Index 1</li>
            <li>Contents of Cell Index 2</li>
            <!-- Additional Cells -->
        </ul>
    </div>
</div>
```


The following HTML attributes set additional JavaScript properties of a carousel view.

| HTML Attribute | Description | Supported Values |
| --- | --- | --- |
| `data-ad-centers-selection` | A Boolean value that indicates whether the carousel should spin to center the selected cell when a new cell is selected.  Available in iAd JS 1.0 and later. | `true`, `false` |
| `data-ad-center-selection-duration` | The duration, in seconds, of the centering animation when a new cell is selected.  Available in iAd JS 1.0 and later. | Floats |
| `data-ad-cell-padding` | The distance, in pixels, between each cell.  Available in iAd JS 1.0 and later. | Integers |
| `data-ad-rotation` | The rotation angle, in degrees, of the carousel.  Available in iAd JS 1.0 and later. | Floats |
| `data-ad-orientation` | The orientation of the carousel view.  Available in iAd JS 1.0 and later. | `horizontal`, `vertical` |

Available in iAd JS 1.0 and later.

The `ad-control` CSS class corresponds to the `iAd.Control` JavaScript class.


```
<div class="ad-control [css-classes]" [html-attributes]></div>
```



```
<div class="ad-control ad-normal" data-ad-tag="1"></div>
```


The following CSS classes correspond to values for a control’s `state` JavaScript property.

| CSS Class | Description | Corresponding JavaScript Value |
| --- | --- | --- |
| `ad-normal` | The normal, or default state of a control—that is, enabled but neither selected nor highlighted.  Available in iAd JS 1.0 and later. | `STATE_NORMAL` |
| `ad-highlighted` | The highlighted state of a control. A control enters this state when a touch enters and exits during tracking and and when there is a touch-up event.  Available in iAd JS 1.0 and later. | `STATE_HIGHLIGHTED` |
| `ad-disabled` | The disabled state of a control. This state indicates that the control is currently disabled.  Available in iAd JS 1.0 and later. | `STATE_DISABLED` |
| `ad-selected` | The selected state of a control. For many controls, this state has no effect on behavior or appearance.  Available in iAd JS 1.0 and later. | `STATE_SELECTED` |

The following HTML attributes set additional JavaScript properties of a control.

| HTML Attribute | Description | Supported Values | Corresponding JavaScript Property / DOM Event Type |
| --- | --- | --- | --- |
| `data-ad-tag` | The control’s tag.  Available in iAd JS 1.0 and later. | Integers | `tag` |
| `data-ad-onControlTouchDown` | The code to execute when a touch-down event occurs in the control.  Available in iAd JS 1.0 and later. | JavaScript | `TOUCH_DOWN_EVENT` |
| `data-ad-onControlTouchDragInside` | The code to execute when a finger is dragged inside the bounds of the control.  Available in iAd JS 1.0 and later. | JavaScript | `TOUCH_DRAG_INSIDE_EVENT` |
| `data-ad-onControlTouchDragOutside` | The code to execute when a finger is dragged just outside the bounds of the control.  Available in iAd JS 1.0 and later. | JavaScript | `TOUCH_DRAG_OUTSIDE_EVENT` |
| `data-ad-onControlTouchDragEnter` | The code to execute when a finger is dragged into the bounds of the control.  Available in iAd JS 1.0 and later. | JavaScript | `TOUCH_DRAG_ENTER_EVENT` |
| `data-ad-onControlTouchDragExit` | The code to execute when a finger is dragged from within the control to outside its bounds.  Available in iAd JS 1.0 and later. | JavaScript | `TOUCH_DRAG_EXIT_EVENT` |
| `data-ad-onControlTouchUpInside` | The code to execute when a touch-up event occurs inside the bounds of the control.  Available in iAd JS 1.0 and later. | JavaScript | `TOUCH_UP_INSIDE_EVENT` |
| `data-ad-onControlTouchUpOutside` | The code to execute when a touch-up event occurs outside the bounds of the control.  Available in iAd JS 1.0 and later. | JavaScript | `TOUCH_UP_OUTSIDE_EVENT` |
| `data-ad-onControlTouchCancel` | The code to execute when a system event cancels all current touches for the control.  Available in iAd JS 1.0 and later. | JavaScript | `TOUCH_CANCEL_EVENT` |
| `data-ad-onControlValueChange` | The code to execute when manipulation of the control causes its value to change.  Available in iAd JS 1.0 and later. | JavaScript | `VALUE_CHANGE_EVENT` |
| `data-ad-onControlTouchStateChange` | The code to execute when the touch state of the control changes.  Available in iAd JS 1.0 and later. | JavaScript | `TOUCH_STATE_CHANGE_EVENT` |

Available in iAd JS 1.0 and later.

The `ad-flow-view` CSS class corresponds to the `iAd.FlowView` JavaScript class.

The cells of a flow view are declared as items in an unordered list. See the example.


```
<div class="ad-flow-view" [html-attributes]></div>
```



```
<div class="ad-flow-view" data-ad-side-padding="170" data-ad-cell-rotation="1.3" data-ad-cell-gap="56.9" data-ad-side-z-offset="-200" data-ad-front-cell-index="7"></div>
    <ul>
        <li>Contents of Cell Index 1</li>
        <li>Contents of Cell Index 2</li>
        <!-- Additional Cells -->
    </ul>
</div>
```


The following HTML attributes set additional JavaScript properties of a flow view.

| HTML Attribute | Description | Supported Values | Corresponding JavaScript Property |
| --- | --- | --- | --- |
| `data-ad-front-cell-index` | The index of the cell that is currently in the front, center position of the flow view.  Available in iAd JS 1.0 and later. | Integers | `frontCellIndex` |
| `data-ad-side-padding` | The distance, in pixels, between the front cell and the cells on the sides of the flow view.  Available in iAd JS 1.0 and later. | Floats | `sidePadding` |
| `data-ad-front-z-offset` | The distance, in pixels, that the front cell is translated toward the user.  Available in iAd JS 1.0 and later. | Floats | `frontZOffset` |
| `data-ad-side-z-offset` | The distance, in pixels, that the cells on the sides are translated toward the user.  Available in iAd JS 1.0 and later. | Floats | `sideZOffset` |
| `data-ad-cell-gap` | The distance, in pixels, between adjacent cells in the flow view.  Available in iAd JS 1.0 and later. | Floats | `cellGap` |
| `data-ad-drag-multiplier` | A coefficient used to convert interaction movement into the coordinate system of the flow view.  Available in iAd JS 1.0 and later. | Floats | `dragMultiplier` |
| `data-ad-cell-rotation` | The rotation, in radians, applied to side cells in the flow view.  Available in iAd JS 1.0 and later. | Floats | `cellRotation` |
| `data-ad-delegate-index-notification-delay` | A delay, in milliseconds, before the flow view informs its delegate that interaction has ceased.  Available in iAd JS 1.0 and later. | Floats | `delegateIndexNotificationDelay` |
| `data-ad-priority-ordering` | A Boolean value that indicates whether cells are arranged such that priority is given to cells with lower index numbers.  Available in iAd JS 1.0 and later. | `true`, `false` | `priorityOrdering` |
| `data-ad-track-camera` | A Boolean value that indicates whether minor horizontal finger movement is tracked by the flow view.  Available in iAd JS 1.0 and later. | `true`, `false` | `trackCamera` |

Available in iAd JS 1.0 and later.

The `ad-hosting-layer` CSS class does not correspond to a specific JavaScript class; rather, it represents the hosting layer of certain other views, such as `[“ad-scroll-view”](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytkmzzfvjvonzu)`, `[“ad-table-view”](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytkmzzfvjvoojy)`, and `[“ad-carousel-view”](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytkmzzfvjvomjx)`.


```
<div class="ad-scroll-view" data-ad-bounces="true" data-ad-shows-vertical-scroll-indicator="true" data-ad-shows-horizontal-scroll-indicator="true" data-ad-indicator-style="indicator-default">
    <div class="ad-hosting-layer">
        <div class="ad-view my-content-layer">My Scroll View Content</div>
    </div>
</div>
```


Available in iAd JS 1.0 and later.

The `ad-image-view` CSS class corresponds to the `iAd.ImageView` JavaScript class.


```
<div class="ad-image-view" [html-attributes]></div>
```



```
<div class="ad-image-view" ad-image="myImage.png"></div>
```


The following HTML attributes set additional JavaScript properties of an image view.

| HTML Attribute | Description | Supported Values | Corresponding JavaScript Property |
| --- | --- | --- | --- |
| `data-ad-image` | The image that the image view displays when it is in its normal state.  Available in iAd JS 1.0 and later. | URLs | `image` |
| `data-ad-highlighted-image` | The image that the image view displays when it is in its highlighted state.  Available in iAd JS 1.0 and later. | URLs | `highlightedImage` |

Available in iAd JS 1.0 and later.

The `ad-label` CSS class corresponds to the `iAd.Label` JavaScript class.


```
<div class="ad-label" [html-attributes]></div>
```



```
<div class="ad-label" data-ad-number-of-lines="2">
    Only the first two lines of this text should be visible. The rest should be truncated.
</div>
```


The following HTML attributes set additional JavaScript properties of a label.

| HTML Attribute | Description | Supported Values | Corresponding JavaScript Property |
| --- | --- | --- | --- |
| `data-ad-number-of-lines` | The number of lines used to display the text.  Available in iAd JS 1.2 and later. | Integers | `numberOfLines` |
| `data-ad-vertical-alignment` | Sets the position of the text within the label’s bounding box.  Available in iAd JS 1.3 and later. | `bottom`, `middle`, `top` | `verticalAlignment` |

Available in iAd JS 1.2 and later.

The `ad-navigation-bar` CSS class corresponds to the `iAd.NavigationBar` JavaScript class.


```
<div class="ad-navigation-bar [css-classes]"></div>
```



```
<div class="ad-navigation-bar ad-black"></div>
```


The following CSS classes correspond to values for a navigation bar’s `barStyle` JavaScript property.

| CSS Class | Description | Corresponding JavaScript Value |
| --- | --- | --- |
| `ad-default` | Use the default style normally associated with the given view.  Available in iAd JS 1.0 and later. | `STYLE_DEFAULT` |
| `ad-black` | Use an opaque black style.  Available in iAd JS 1.0 and later. | `STYLE_BLACK` |
| `ad-black-translucent` | Use a translucent black style.  Available in iAd JS 1.0 and later. | `STYLE_BLACK_TRANSLUCENT` |

Available in iAd JS 1.0 and later.

The `ad-page-control` CSS class corresponds to the `iAd.PageControl` JavaScript class.


```
<div class="ad-page-control" [html-attributes]></div>
```



```
<div class="ad-page-control" data-ad-number-of-pages="4"></div>
```


The following HTML attributes set additional JavaScript properties of a page control.

| HTML Attribute | Description | Supported Values | Corresponding JavaScript Property |
| --- | --- | --- | --- |
| `data-ad-number-of-pages` | The number of pages that the page control shows as dots.  Available in iAd JS 1.0 and later. | Integers | `numberOfPages` |
| `data-ad-hides-for-single-page` | A Boolean value that indicates whether the page indicator should be visible if there is only one page.  Available in iAd JS 1.0 and later. | `true`, `false` | `hidesForSinglePage` |
| `data-ad-current-page` | The index for the current page.  Available in iAd JS 1.0 and later. | Integers | `currentPage` |

Available in iAd JS 1.0 and later.

The `ad-page-controller-view` CSS class corresponds to the `iAd.PageController` JavaScript class.


```
<div class="ad-page-controller-view" [html-attributes]></div>
```



```
<div class="ad-page-controller-view" data-ad-scrolls-infinitely>
    <div class="ad-scroll-view" data-ad-outlet="scrollView">
        <div class="ad-hosting-layer">
            <div class="ad-view">Page #1</div>
            <div class="ad-view">Page #2</div>
        </div>
    </div>
    <div class="ad-page-control" data-ad-outlet="pageControl"></div>
</div>
```


The following HTML attributes set additional JavaScript properties of a page controller.

| HTML Attribute | Description | Supported Values | Corresponding JavaScript Property |
| --- | --- | --- | --- |
| `data-ad-scrolls-infinitely` | Determines whether or not scrolling stops after displaying the last view.  Available in iAd JS 1.2 and later. | Booleans | `scrollsInfinitely` |

A page controller element requires child elements with the following values for the `ad-outlet` HTML property.

| Outlet Value | Description | Required CSS Class | Corresponding JavaScript Property |
| --- | --- | --- | --- |
| `scrollView` | The scroll view object used by this view controller to display the page views.  Available in iAd JS 1.2 and later. | `[“ad-scroll-view”](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytkmzzfvjvonzu)` | `scrollView` |
| `pageControl` | The page control object used by this view controller to navigate between page views.  Available in iAd JS 1.2 and later. | `[“ad-page-control”](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytkmzzfvjvonbv)` | `pageControl` |

The `ad-progress-view` CSS class corresponds to the `iAd.ProgressView` JavaScript class.


```
<div class="ad-progress-view [css-classes]" [html-attributes]></div>
```



```
<div class="ad-progress-view ad-bar" data-ad-progress="0"></div>
```


The following CSS classes correspond to values for a progress view’s `style` JavaScript property.

| CSS Class | Description | Corresponding JavaScript Value |
| --- | --- | --- |
| `ad-default` | The default progress view style.  Available in iAd JS 1.0 and later. | `STYLE_DEFAULT` |
| `ad-bar` | The style of a progress view that is displayed in a toolbar.  Available in iAd JS 1.0 and later. | `STYLE_BAR` |

The following HTML attributes set additional JavaScript properties of a progress view.

| HTML Attribute | Description | Supported Values | Corresponding JavaScript Property |
| --- | --- | --- | --- |
| `data-ad-progress` | The current progress, as a float between 0 and 1. A value of 1 indicates that the task is complete.  Available in iAd JS 1.0 and later. | Floats | `progress` |

Available in iAd JS 1.0 and later.

The `ad-rating-control` CSS class corresponds to the `iAd.RatingControl` JavaScript class.


```
<div class="ad-rating-control" style="[css-properties]" [html-attributes]></div>
```



```
<div class="ad-rating-control" style="width:50px;" data-ad-value="3"></div>
```


The following CSS properties set additional JavaScript properties of a rating control.

| CSS Property | Description | Corresponding JavaScript Property |
| --- | --- | --- |
| `width` | The rating control’s width.  Available in iAd JS 1.0 and later. | `width` |

The following HTML attributes set additional JavaScript properties of a rating control.

| HTML Attribute | Description | Supported Values | Corresponding JavaScript Property |
| --- | --- | --- | --- |
| `data-ad-value` | The rating control’s value, between 0 and 5.  Available in iAd JS 1.0 and later. | Integers | `value` |

Available in iAd JS 1.0 and later.

The `ad-search-bar` CSS class corresponds to the `iAd.SearchBar` JavaScript class.


```
<div class="ad-search-bar [css-classes]" [html-attributes]></div>
```



```
<div class="ad-search-bar ad-black" data-ad-placeholder="Search"></div>
```


The following CSS classes correspond to values for a search bar’s `style` JavaScript property.

| CSS Class | Description | Corresponding JavaScript Value |
| --- | --- | --- |
| `ad-default` | Use the default style for the search bar.  Available in iAd JS 1.0 and later. | `STYLE_DEFAULT` |
| `ad-black` | Use a black style for the search bar.  Available in iAd JS 1.0 and later. | `STYLE_BLACK` |
| `ad-black-translucent` | Use a translucent black style for the search bar.  Available in iAd JS 1.0 and later. | `STYLE_BLACK_TRANSLUCENT` |

The following HTML attributes set additional JavaScript properties of a search bar.

| HTML Attribute | Description | Supported Values | Corresponding JavaScript Property |
| --- | --- | --- | --- |
| `data-ad-text` | The current or starting search text.  Available in iAd JS 1.0 and later. | Any | `text` |
| `data-ad-placeholder` | The string that is displayed when there is no other text in the text field.  Available in iAd JS 1.0 and later. | Any | `placeholder` |
| `data-ad-shows-cancel-button` | A Boolean value that indicates whether the cancel button is displayed.  Available in iAd JS 1.0 and later. | `true`, `false` | `showsCancelButton` |

Available in iAd JS 1.0 and later.

The `ad-scroll-view` CSS class corresponds to the `iAd.ScrollView` JavaScript class.

The content of a scroll view must be provided in a content view in the scroll view’s hosting layer. See the example.


```
<div class="ad-scroll-view" [html-attributes]></div>
```



```
<div class="ad-scroll-view" data-ad-bounces="true" data-ad-shows-vertical-scroll-indicator="true" data-ad-shows-horizontal-scroll-indicator="true" data-ad-indicator-style="indicator-default">
    <div class="ad-hosting-layer">
        <div class="ad-view my-content-layer">My Scroll View Content</div>
    </div>
</div>
```


The following HTML attributes set additional JavaScript properties of a scroll view.

| HTML Attribute | Description | Supported Values | Corresponding JavaScript Property |
| --- | --- | --- | --- |
| `data-ad-delays-content-touches` | A Boolean value that indicates whether the scroll view delays the handling of touch-down gestures.  Available in iAd JS 1.0 and later. | `true`, `false` | `delaysContentTouches` |
| `data-ad-can-cancel-content-touches` | A Boolean value that indicates whether touches in the content view always lead to tracking.  Available in iAd JS 1.0 and later. | `true`, `false` | `canCancelContentTouches` |
| `data-ad-horizontal-scroll-enabled` | A Boolean value that indicates whether horizontal scrolling is enabled.  Available in iAd JS 1.0 and later. | `true`, `false` | `horizontalScrollEnabled` |
| `data-ad-vertical-scroll-enabled` | A Boolean value that indicates whether vertical scrolling is enabled.  Available in iAd JS 1.0 and later. | `true`, `false` | `verticalScrollEnabled` |
| `data-ad-shows-horizontal-scroll-indicator` | A Boolean value that indicates whether the horizontal scroll indicator is visible.  Available in iAd JS 1.0 and later. | `true`, `false` | `showsHorizontalScrollIndicator` |
| `data-ad-shows-vertical-scroll-indicator` | A Boolean value that indicates whether the vertical scroll indicator is visible.  Available in iAd JS 1.0 and later. | `true`, `false` | `showsVerticalScrollIndicator` |
| `data-ad-bounces` | A Boolean value that indicates whether the scroll view bounces past the edge of content and back again.  Available in iAd JS 1.0 and later. | `true`, `false` | `bounces` |
| `data-ad-paging-enabled` | A Boolean value that indicates whether scrolling should snap to the nearest content page, where a page is the size of the view.  Available in iAd JS 1.0 and later. | `true`, `false` | `pagingEnabled` |
| `data-ad-scroll-indicator-inset-left` | The distance the scroll indicators are inset from the left edge of the scroll view.  Available in iAd JS 1.0 and later. | Integers | `scrollIndicatorInsets``.left` |
| `data-ad-scroll-indicator-inset-top` | The distance the scroll indicators are inset from the top edge of the scroll view.  Available in iAd JS 1.0 and later. | Integers | `scrollIndicatorInsets``.top` |
| `data-ad-scroll-indicator-inset-right` | The distance the scroll indicators are inset from the right edge of the scroll view.  Available in iAd JS 1.0 and later. | Integers | `scrollIndicatorInsets``.right` |
| `data-ad-scroll-indicator-inset-bottom` | The distance the scroll indicators are inset from the bottom edge of the scroll view.  Available in iAd JS 1.0 and later. | Integers | `scrollIndicatorInsets``.bottom` |
| `data-ad-indicator-style` | The style of the scroll indicators.  Available in iAd JS 1.0 and later. | `indicator-default`, `indicator-black`, `indicator-white` | `indicatorStyle` |

Available in iAd JS 1.0 and later.

The `ad-slider` CSS class corresponds to the `iAd.Slider` JavaScript class.


```
<div class="ad-slider" [html-attributes]></div>
```



```
<div class="ad-slider" data-ad-maximum-value="100" data-ad-continuous="false"></div>
```


The following HTML attributes set additional JavaScript properties of a slider.

| HTML Attribute | Description | Supported Values | Corresponding JavaScript Property |
| --- | --- | --- | --- |
| `data-ad-continuous` | A Boolean value that indicates whether changes in the slider’s value generate continuous update events.  Available in iAd JS 1.0 and later. | `true`, `false` | `continuous` |
| `data-ad-minimum-value` | The slider’s minimum value.  Available in iAd JS 1.0 and later. | Floats | `minimumValue` |
| `data-ad-maximum-value` | The slider’s maximum value.  Available in iAd JS 1.0 and later. | Floats | `maximumValue` |
| `data-ad-value` | The slider’s current value.  Available in iAd JS 1.0 and later. | Floats | `value` |

Available in iAd JS 1.0 and later.

The `ad-switch` CSS class corresponds to the `iAd.Switch` JavaScript class.


```
<div class="ad-switch" [html-attributes]></div>
```



```
<div class="ad-switch" data-ad-on="true"></div>
```


The following HTML attributes set additional JavaScript properties of a switch.

| HTML Attribute | Description | Supported Values | Corresponding JavaScript Property |
| --- | --- | --- | --- |
| `data-ad-on` | A Boolean value that indicates whether the switch is in its On state.  Available in iAd JS 1.0 and later. | `true`, `false` | `on` |

Available in iAd JS 1.0 and later.

The `ad-tab-bar` CSS class corresponds to the `iAd.TabBar` JavaScript class.

A tab bar contains one or more elements with the `ad-tab-bar-item` class. See the example.


```
<div class="ad-tab-bar"></div>
```



```
<div class="ad-tab-bar">
    <div class="ad-tab-bar-item" data-ad-title="Addresses" data-ad-image="images/address.png" data-ad-badge-value="10"></div>
    <div class="ad-tab-bar-item" data-ad-title="Downloads" data-ad-image="images/downloads.png" data-ad-badge-value="20"></div>
    <div class="ad-tab-bar-item" data-ad-title="Movies" data-ad-image="images/movies.png" data-ad-badge-value="30"></div>
    <div class="ad-tab-bar-item" data-ad-title="Favorites" data-ad-image="images/star.png"></div>
</div>
```


Available in iAd JS 1.0 and later.

The `ad-tab-bar-item` CSS class corresponds to the `iAd.TabBarItem` JavaScript class.


```
<div class="ad-tab-bar-item" [html-attributes]></div>
```



```
<div class="ad-tab-bar-item" data-ad-title="MyTitle"></div>
```


The following HTML attributes set additional JavaScript properties of a tab bar item.

| HTML Attribute | Description | Supported Values | Corresponding JavaScript Property |
| --- | --- | --- | --- |
| `data-ad-badge-value` | Text that is displayed in the upper-right corner of the item with a surrounding red oval.  Available in iAd JS 1.0 and later. | Integers | `badgeValue` |
| `data-ad-title` | The tab bar item’s title.  Available in iAd JS 1.0 and later. | Any | `title` |
| `data-ad-image` | The tab bar item’s image.  Available in iAd JS 1.0 and later. | URLs | `image` |

Available in iAd JS 1.0 and later.

The `ad-table-view` CSS class corresponds to the `iAd.TableView` JavaScript class.

A table view contains one or more cells in one or more sections, along with optional section titles and footers. See the example.


```
<div class="ad-table-view [css-classes]"></div>
```



```
<div class="ad-table-view data-ad-grouped">
    <div class="ad-hosting-layer">
        <div class="section">
            <div class="cells">
                <div class="ad-table-view-cell style-value-1 disclosure-accessory blue-selection" data-ad-text="One" data-ad-detailed-text="Label"></div>
                <div class="ad-table-view-cell style-value-1 disclosure-accessory blue-selection" data-ad-text="Two" data-ad-detailed-text="Label"></div>
            </div>
        </div>
        <div class="section">
            <h1>This is a pretty long title that will run over the next line</h1>
            <div class="cells">
                <div class="ad-table-view-cell style-value-1 disclosure-accessory blue-selection" data-ad-text="One" data-ad-detailed-text="Label"></div>
                <div class="ad-table-view-cell style-value-1 disclosure-accessory blue-selection" data-ad-text="Two" data-ad-detailed-text="Label"></div>
                <div class="ad-table-view-cell style-value-1 disclosure-accessory blue-selection" data-ad-text="Three" data-ad-detailed-text="Label"></div>
                <div class="ad-table-view-cell style-value-1 disclosure-accessory blue-selection" data-ad-text="Four" data-ad-detailed-text="Label"></div>
                <div class="ad-table-view-cell style-value-1 disclosure-accessory blue-selection" data-ad-text="This a pretty long title that will get trimmed" data-ad-detailed-text="Label"></div>
                <div class="ad-table-view-cell style-value-1 disclosure-accessory blue-selection" data-ad-text="Six" data-ad-detailed-text="Label"></div>
            </div>
            <span>This is a footer which is useful to provide some additional information.</span>
        </div>
        <div class="section">
            <h1>Bar</h1>
            <div class="cells">
                <div class="ad-table-view-cell style-value-1 disclosure-accessory blue-selection" data-ad-text="One" data-ad-detailed-text="Label"></div>
                <div class="ad-table-view-cell style-value-1 disclosure-accessory blue-selection" data-ad-text="Two" data-ad-detailed-text="Label"></div>
                <div class="ad-table-view-cell style-value-1 disclosure-accessory blue-selection" data-ad-text="Three" data-ad-detailed-text="Label"></div>
            </div>
        </div>
        <div class="section">
            <h1>Baz</h1>
            <div class="cells">
               <div class="ad-table-view-cell style-value-1 disclosure-accessory blue-selection" data-ad-text="One" data-ad-detailed-text="Label"></div>
               <div class="ad-table-view-cell style-value-1 disclosure-accessory blue-selection" data-ad-text="Two" data-ad-detailed-text="Label"></div>
               <div class="ad-table-view-cell style-value-1 disclosure-accessory blue-selection" data-ad-text="Three" data-ad-detailed-text="Label"></div>
               <div class="ad-table-view-cell style-value-1 disclosure-accessory blue-selection" data-ad-text="Four" data-ad-detailed-text="Label"></div>
            </div>
        </div>
        <div class="section">
            <div class="cells">
                <div class="ad-table-view-cell style-value-1 disclosure-accessory blue-selection" data-ad-text="One" data-ad-detailed-text="Label"></div>
            </div>
            <span>This is another footer for a section with no header.</span>
        </div>
    </div>
</div>
```


The following CSS classes correspond to values for a table view’s `style` JavaScript property.

| CSS Class | Description | Corresponding JavaScript Value |
| --- | --- | --- |
| `ad-plain` | A plain table view. Any section headers or footers are displayed as inline separators and float when the table view is scrolled.  Available in iAd JS 1.0 and later. | `STYLE_PLAIN` |
| `ad-custom` | A custom style table view.  Available in iAd JS 1.0 and later. | `STYLE_CUSTOM` |
| `ad-grouped` | A table view whose sections present distinct groups of rows. The section headers and footers do not float.  Available in iAd JS 1.0 and later. | `STYLE_GROUPED` |

The following CSS classes correspond to values for a table view’s `separatorStyle` JavaScript property.

| CSS Class | Description | Corresponding JavaScript Value |
| --- | --- | --- |
| `ad-separator-none` | The separator cell has no distinct style.  Available in iAd JS 1.0 and later. | `SEPARATOR_STYLE_NONE` |
| `ad-separator-single-line` | The separator cell has a single line running across its width.  Available in iAd JS 1.0 and later. | `SEPARATOR_STYLE_SINGLE_LINE` |
| `ad-separator-single-line-etched` | The separator cell has double lines running across its width, giving it an etched look. This style is currently supported only by grouped table views  Available in iAd JS 1.0 and later. | `SEPARATOR_STYLE_SINGLE_LINE_ETCHED` |

Available in iAd JS 1.0 and later.

The `ad-table-view-cell` CSS class corresponds to the `iAd.TableViewCell` JavaScript class.


```
<div class="ad-table-view-cell [css-classes]" [html-attributes]></div>
```



```
<div class="ad-table-view-cell ad-style-default ad-disclosure-accessory ad-blue-selection" data-ad-text="MyCell"></div>
```


The following CSS classes correspond to values for a table view cell’s style.

| CSS Class | Description | Corresponding JavaScript Value |
| --- | --- | --- |
| `ad-style-default` | A simple style for a cell with a text label (black and left aligned) and an optional image view.  Available in iAd JS 1.0 and later. | `STYLE_DEFAULT` |
| `ad-style-value-1` | A style for a cell with a label on the left side of the cell with left-aligned and black text; on the right side is a label that has smaller blue text and is right aligned.  Available in iAd JS 1.0 and later. | `STYLE_VALUE_1` |
| `ad-style-value-2` | A style for a cell with a label on the left side of the cell with text that is right aligned and blue; on the right side of the cell is another label with smaller text that is left aligned and black.  Available in iAd JS 1.0 and later. | `STYLE_VALUE_2` |
| `ad-style-subtitle` | A style for a cell with a left-aligned label across the top and another left-aligned label below it in smaller gray text.  Available in iAd JS 1.0 and later. | `STYLE_SUBTITLE` |

The following CSS classes correspond to values for a table view cell’s `accessoryType` JavaScript property.

| CSS Class | Description | Corresponding JavaScript Value |
| --- | --- | --- |
| `ad-no-accessory` | The cell does not have any accessory view.  Available in iAd JS 1.0 and later. | `ACCESSORY_NONE` |
| `ad-disclosure-accessory` | The cell has an accessory control shaped like a regular chevron. It is intended as a disclosure indicator. The control doesn't track touches.  Available in iAd JS 1.0 and later. | `ACCESSORY_DISCLOSURE_INDICATOR` |
| `ad-detail-accessory` | The cell has an accessory control that is a blue button with a chevron image as content. It is used for configuration purposes. The control tracks touches.  Available in iAd JS 1.0 and later. | `ACCESSORY_DETAIL_DISCLOSURE_BUTTON` |

The following CSS classes correspond to values for a table view cell’s `selectionStyle` JavaScript property.

| CSS Class | Description | Corresponding JavaScript Value |
| --- | --- | --- |
| `ad-no-selection` | The cell does not have any accessory view.  Available in iAd JS 1.0 and later. | `SELECTION_STYLE_NONE` |
| `ad-blue-selection` | The cell has an accessory control shaped like a regular chevron. It is intended as a disclosure indicator. The control doesn't track touches.  Available in iAd JS 1.0 and later. | `SELECTION_STYLE_BLUE` |
| `ad-gray-selection` | The cell has an accessory control that is a blue button with a chevron image as content. It is used for configuration purposes. The control tracks touches.  Available in iAd JS 1.0 and later. | `SELECTION_STYLE_GRAY` |

The following HTML attributes set additional JavaScript properties of a table view cell.

| HTML Attribute | Description | Supported Values | Corresponding JavaScript Property |
| --- | --- | --- | --- |
| `data-ad-text` | The text used for the main textual content of the table cell.  Available in iAd JS 1.0 and later. | Any | `text` |
| `data-ad-detailed-text` | The secondary label of the table cell, if the label exists.  Available in iAd JS 1.0 and later. | Any | `detailedText` |

Available in iAd JS 1.0 and later.

The `ad-toolbar` CSS class corresponds to the `iAd.Toolbar` JavaScript class.

A toolbar can contain elements of several different classes, including bar buttons and progress views. See the example.


```
<div class="ad-toolbar [css-classes]">
```



```
<div class="ad-toolbar ad-black-translucent"></div>
    <div class="ad-bar-button square lightblue" data-ad-title="Done"></div>
    <div class="ad-bar-button flexible-space"></div>
    <div class="ad-progress-view" data-ad-progress="0.6"></div>
    <div class="ad-bar-button flexible-space"></div>
</div>
```


The following CSS classes correspond to values for a toolbar’s `style` JavaScript property.

| CSS Class | Description | Corresponding JavaScript Value |
| --- | --- | --- |
| `ad-default` | Use the default style normally associated with the given view.  Available in iAd JS 1.0 and later. | `STYLE_DEFAULT` |
| `ad-black` | Use a black style.  Available in iAd JS 1.0 and later. | `STYLE_BLACK` |
| `ad-black-translucent` | Use a translucent opaque black style.  Available in iAd JS 1.0 and later. | `STYLE_BLACK_TRANSLUCENT` |

Available in iAd JS 1.0 and later.

[Next](View%20Processors.md)[Previous](Introduction.md)

