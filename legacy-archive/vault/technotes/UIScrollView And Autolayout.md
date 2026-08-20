---
title: UIScrollView And Autolayout
apple_id: DTS40013309
resource_type: Technical Note
platform: iOS
topic: User Experience
technology: null
published: '2014-02-20'
source_url: https://developer.apple.com/library/archive/technotes/tn2154/_index.html
archived_at: '2026-07-26T19:54:10.609158Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2154

# UIScrollView And Autolayout

This technote provides some information regarding Auto Layout support for UIScrollView.

[Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgmzqhewugsbrfvke4vcbi4yq)[In Depth Explanation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgmzqhewugsbrfvke4vcbi4za)[Mixed Approach](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgmzqhewugsbrfvguswcfirpucucqkjhucq2i)[Pure Auto Layout Approach](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgmzqhewugsbrfvke4vcbi4zq)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgmzqhewvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Introduction

This technote provides some information regarding Auto Layout support for UIScrollView. Specifically it demonstrates a "mixed" and a "pure" auto layout approach for UIScrollViews.

[Back to Top](#)

## In Depth Explanation

In general, Auto Layout considers the top, left, bottom, and right edges of a view to be the visible edges. That is, if you pin a view to the left edge of its superview, you’re really pinning it to the minimum x-value of the superview’s bounds. Changing the bounds origin of the superview does not change the position of the view.

The UIScrollView class scrolls its content by changing the origin of its bounds. To make this work with Auto Layout, the top, left, bottom, and right edges within a scroll view now mean the edges of its content view.

The constraints on the subviews of the scroll view must result in a size to fill, which is then interpreted as the content size of the scroll view. (This should not be confused with the intrinsicContentSize method used for Auto Layout.) To size the scroll view’s frame with Auto Layout, constraints must either be explicit regarding the width and height of the scroll view, or the edges of the scroll view must be tied to views outside of its subtree.

Note that you can make a subview of the scroll view appear to float (not scroll) over the other scrolling content by creating constraints between the view and a view outside the scroll view’s subtree, such as the scroll view’s superview.

Here are two examples of how to configure the scroll view, first the mixed approach, and then the pure approach.

[Back to Top](#)

## Mixed Approach

Position and size your scroll view with constraints external to the scroll view—that is, the translatesAutoresizingMaskIntoConstraints property is set to NO.

Create a plain UIView content view for your scroll view that will be the size you want your content to have. Make it a subview of the scroll view but let it continue to translate the autoresizing mask into constraints:

__Listing 1__  Mixed Approach Code Listing

```objc
- (void)viewDidLoad {
UIView *contentView;

contentView = [[UIView alloc] initWithFrame:CGRectMake(0,0,contentWidth,contentHeight)];

[scrollView addSubview:contentView];

// DON'T change contentView's translatesAutoresizingMaskIntoConstraints,
// which defaults to YES;

// Set the content size of the scroll view to match the size of the content view:
[scrollView setContentSize:CGSizeMake(contentWidth,contentHeight)];

 /* the rest of your code here... */

}
```

Create the views you want to put inside the content view and configure their constraints so as to position them within the content view.

Alternatively, you can create a view subtree to go in the scroll view, set up your constraints, and call the systemLayoutSizeFittingSize: method (with the UILayoutFittingCompressedSize option) to find the size you want to use for your content view and the contentSize property of the scroll view.

[Back to Top](#)

## Pure Auto Layout Approach

To use the pure autolayout approach do the following:

- Set translatesAutoresizingMaskIntoConstraints to NO on all views involved.
- Position and size your scroll view with constraints external to the scroll view.
- Use constraints to lay out the subviews within the scroll view, being sure that the constraints tie to all four edges of the scroll view and do not rely on the scroll view to get their size.

A simple example would be a large image view, which has an intrinsic content size derived from the size of the image. In the viewDidLoad method of your view controller, you would include code similar to the code shown in the listing below:

__Listing 2__  Pure Auto Layout Approach Code Listing

```objc
- (void)viewDidLoad {
    UIScrollView *scrollView;
    UIImageView *imageView;
    NSDictionary *viewsDictionary;

    // Create the scroll view and the image view.
    scrollView  = [[UIScrollView alloc] init];
    imageView = [[UIImageView alloc] init];

    // Add an image to the image view.
    [imageView setImage:[UIImage imageNamed:"MyReallyBigImage"]];

    // Add the scroll view to our view.
    [self.view addSubview:scrollView];

    // Add the image view to the scroll view.
    [scrollView addSubview:imageView];

    // Set the translatesAutoresizingMaskIntoConstraints to NO so that the views autoresizing mask is not translated into auto layout constraints.
    scrollView.translatesAutoresizingMaskIntoConstraints  = NO;
    imageView.translatesAutoresizingMaskIntoConstraints = NO;

    // Set the constraints for the scroll view and the image view.
    viewsDictionary = NSDictionaryOfVariableBindings(scrollView, imageView);
    [self.view addConstraints:[NSLayoutConstraint constraintsWithVisualFormat:@"H:|[scrollView]|" options:0 metrics: 0 views:viewsDictionary]];
    [self.view addConstraints:[NSLayoutConstraint constraintsWithVisualFormat:@"V:|[scrollView]|" options:0 metrics: 0 views:viewsDictionary]];
    [scrollView addConstraints:[NSLayoutConstraint constraintsWithVisualFormat:@"H:|[imageView]|" options:0 metrics: 0 views:viewsDictionary]];
    [scrollView addConstraints:[NSLayoutConstraint constraintsWithVisualFormat:@"V:|[imageView]|" options:0 metrics: 0 views:viewsDictionary]];

    /* the rest of your code here... */
}
```

This would give you a scroll view that resized as the view controller’s view resized (such as on device rotation), and the image view would be a scrolling subview. You don’t have to set the content size of the scroll view.

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-02-20 | Fixed some typographical errors. |
| 2013-05-08 | New document that describes how to work with UIScrollView and autolayout. |

