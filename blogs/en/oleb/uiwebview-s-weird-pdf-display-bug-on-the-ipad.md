---
title: 'UIWebView''s Weird PDF Display Bug on the iPad'
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2010/06/uiwebview-weird-pdf-display-bug-on-ipad/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:41387fee2499cb02'
translated: false
---

> 原文：[UIWebView's Weird PDF Display Bug on the iPad](https://oleb.net/blog/2010/06/uiwebview-weird-pdf-display-bug-on-ipad/)　·　Ole Begemann

# UIWebView's Weird PDF Display Bug on the iPad

[`UIWebView`](http://developer.apple.com/iphone/library/documentation/uikit/reference/UIWebView_Class/Reference/Reference.html) seems to have a weird display bug connected to PDFs and interface rotation in iPhone SDK 3.2. This is how a PDF displayed in a UIWebView looks on the iPad after you rotate the device from portrait to landscape:

![UIWebView PDF display bug on the iPad](https://oleb.net/media/uiwebview-pdf-display-bug-screenshot.png)

<sub>UIWebView PDF display bug on the iPad (iPhone SDK 3.2).</sub>

The PDF appears to be split in half vertically along an edge that was right in the middle of the page while the device was in portrait orientation. The right half is vertically offset from the left half. [Other people have also noticed it](http://stackoverflow.com/questions/2660578/ipad-uiwebview-pdf-rendering-is-giving-me-weird-visual-artifacts) so I believe it is a genuine bug. To reproduce it, try the following:

1. .
2. Embed the web view in a view controller that supports both portrait and landscape orientation.
3. Load a PDF file into the web view.
4. Rotate the iPad from portrait to landscape or vice versa.

Or [download the sample project](https://oleb.net/media/PDFDisplayBugDemo.zip) I have created. I can reproduce this consistently with a number of different PDF files using iPhone SDK 3.2 both in the iPad Simulator and on an actual iPad. The bug does not appear with HTML content nor is it present on the iPhone. It also disappears if you zoom into the page just a little bit or if you set `scalesPageToFit = NO`.

# Workaround: Reload the document after rotation

The only workaround I have found so far is to reload the document after the device has been rotated: `[webView reload];`. It is not very pretty because reloading can take some time and the user can still see the buggy display for a second, but other than that it works. The best place for the reloading code seems to be your view controller’s `-didRotateFromInterfaceOrientation:` method. Reported to Apple as Radar #8065859.

**Update June 12, 2010:** Apple has confirmed this bug as a duplicate to #7790957.

**Update September 9, 2010:** Another workaround, found out by Dave Keay:

> I just found a fix that works without reloading the whole document:
> 
> Inside the `UIWebView` is a `UIScrollView`, and then one of the subviews of that is a private Apple view class. If you find that and call `setNeedsDisplay` on it in your `shouldAutoRotateToInterfaceOrientation` method, then it will draw correctly.
> 
> Here’s the replacement method for your sample project:
> 
> ```
> - (BOOL)shouldAutorotateToInterfaceOrientation:(UIInterfaceOrientation)interfaceOrientation
>     {
>         // Return YES for supported orientations
>         for (UIView *v in [webView subviews]) {
>             for (UIView *v2 in [v subviews]) {
>                 if ([v2 class] != [UIImageView class])
>                     [v2 setNeedsDisplay];
>             }
>         }
>         return YES;
>     }
> ```
> 
> It seems like rotating won’t keep you at the same place in the document were at before, but that shouldn’t be terrible to fix!

**Update November 23, 2010:** This bug has been fixed in iOS 4.2.
