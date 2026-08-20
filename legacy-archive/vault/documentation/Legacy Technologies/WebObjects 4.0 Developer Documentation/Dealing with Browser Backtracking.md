---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/Topics/DealingWithBackTracking.html
archived_at: '2026-07-15T08:01:02.943720Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Programming Topics](WebObjects%20Programming%20Topics.md)

# Dealing with Browser Backtracking

##  Synopsis

Describes solutions to the page synchronization issues that arise when users backtrack with the browser.

##  Discussion

A problem can arise in WebObjects when users are allowed to backtrack using the browser. The problem is that browsers normally cache the previous pages and repaint the cached pages when the user backtracks. The old page might contain items that are no longer part of the current result set. Thus, the user may get a response for an item he has not selected.

For example, suppose that you have a page capable of showing either a list of movies or the details of one movie. In addition, based on a detail mode flag, a WOCondition decides to show the details. Furthermore, the user clicks a movie title within the list of titles, detail mode is toggled on, the selection is remembered, and the same page instance is returned. If the user presses the browser's Backtrack button, the browser simply repaints the page with the list of movie hyperlinks. This is where the problem arises. The current state of the page is set to detailed mode. When the user selects another movie title from the list, WebObjects must figure out which action should be invoked. It does this by running through the components on the page and determining which element was selected. Since the current state is detail mode, only the detail WOCondition block of elements are checked and a mismatch occurs.

There are two ways to work around this problem.

####  Option 1: Generate Preexpired Pages

When you set the WOApplication _setPageRefreshOnBacktrackEnabled_
method to YES, WOF generates preexpired pages. This informs the browser that it must refetch the page whenever the browser is going to move back to the page.

The issues with this solution are as follows:

1. The user will always see the latest page, no matter how far he backtracks. This behavior may compromise the friendliness of your user interface. You might want the user to see the old screens and be able to reselect from them.

2. Some browsers handle preexpired pages by simply informing the user that the page must be refreshed.

3. Some browsers don't always refresh the page even at the user's explicit request, effectively eliminating backtracking with preexpired pages.

####  Option 2: Return a New Page Instance for Every Action

Create a new instance of the current page and push all of the current state into that page. Make state changes in this new page and then return the new page from the current page's action. This ensures that every page keeps its original state for future requests from a backtracking user.

The issues with this solution are as follows:

1. More memory is used to hold the pages. Ensure that you limit the WOApplication's page cache size. When a new page is accessed, the oldest page will be expired out of the page cache and users will get a "You backtracked too far" exception when trying to execute actions on the old page.

2. Since a complete set of state is kept in each page, the memory usage can grow quickly.

3. State might be invalid even though it is accessible from older pages.

There are many different combinations of these two approaches that can be used throughout a WebObjects application. You must think through the issues of both, and perform some basic testing within your environment to see what works best.

##  See Also

· WOApplication _setPageRefreshOnBacktrackEnabled()_

· WOResponse _setStatus()_

##  Questions

· How do I pre-expire all pages within WebObjects?

· How do I handle browser backtrack issues?

##  Keywords

· Backtrack

· Pre-expire pages

##  Revision History

24 July, 1998. David Scheck. First Draft.
19 November, 1998. Clif Liu. Second Draft.

```

```


Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
