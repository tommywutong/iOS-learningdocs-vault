---
title: Managing the Network Activity Indicator
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2009/09/managing-the-network-activity-indicator/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:91e39d34c4be4108'
translated: false
---

> 原文：[Managing the Network Activity Indicator](https://oleb.net/blog/2009/09/managing-the-network-activity-indicator/)　·　Ole Begemann

# Managing the Network Activity Indicator

iPhone developers should use the little network activity indicator in the iPhone’s status bar to inform the user when their app accesses the network. Showing or hiding the indicator is simple:

```
[[UIApplication sharedApplication] setNetworkActivityIndicatorVisible:YES];
```

Most people probably call this method from their view controllers. This works fine until you have to deal with multiple concurrent tasks that access the network and/or multiple view controllers that are active simultaneously. For example, you might be running a HTTP request to download data from a webservice in the background and using a `MKMapView` instance that accesses the network whenever the user moves the map to a new location.

If you access the `networkActivityIndicatorVisible` property directly from multiple methods in these cases, chances are that you hide the indicator when the first task has finished even though your app continues to access the network. You would need to implement a counter to remember how often the network activity indicator has been shown and hidden to manage it correctly. If your code is spread among multiple view controllers, this gets even more cumbersome.

This “problem” is admittedly a small aspect of usability but the solution is so simple and elegant that I think it is worth doing even if you do not deal with multiple concurrent network activity tasks in your app.

Since the network activity indicator is displayed outside of your app’s window, the logical place to manage it is not a view controller but the application delegate. I have written a short method in my app delegate that uses a static variable to keep track of the number of times the activity indicator was asked to show or hide:

```
- (void)setNetworkActivityIndicatorVisible:(BOOL)setVisible {
    static NSInteger NumberOfCallsToSetVisible = 0;
    if (setVisible)
        NumberOfCallsToSetVisible++;
    else
        NumberOfCallsToSetVisible--;

    // The assertion helps to find programmer errors in activity indicator management.
    // Since a negative NumberOfCallsToSetVisible is not a fatal error,
    // it should probably be removed from production code.
    NSAssert(NumberOfCallsToSetVisible >= 0, @"Network Activity Indicator was asked to hide more often than shown");

    // Display the indicator as long as our static counter is > 0.
    [[UIApplication sharedApplication] setNetworkActivityIndicatorVisible:(NumberOfCallsToSetVisible > 0)];
}
```

This method alone is then responsible for the actual call to the `UIApplication` instance to show or hide the indicator. All view controllers call the method on the app delegate instead:

```
[(MyAppDelegate *)[[UIApplication sharedApplication] delegate] setNetworkActivityIndicatorVisible:YES];
```
