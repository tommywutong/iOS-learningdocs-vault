---
title: How to work around HIMovieViewCreate failing
apple_id: DTS10003620
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2008-03-11'
source_url: https://developer.apple.com/library/archive/qa/qa1417/_index.html
archived_at: '2026-07-18T02:30:34.614015Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1417

# How to work around HIMovieViewCreate failing

## Q:  I've created a Window using Interface Builder containing an `HIMovieView` which was dragged into it from the Carbon-Enhanced Controls palette. When I call `HIViewFindByID` to find the view, the call fails with error -30584 `errUnknownControl`. I've made sure to check that the view's signature and ID are correct. I've also tried to specifically call `HIMovieViewCreate`, but that fails with error -30581 `errDataNotSupported`. Is this a known issue?

A: Yes, there is currently a bug in `HIMovieViewCreate` with QuickTime 7 (r. 3882439). Consequently, `HIViewFindByID` fails because the runtime trying to create the view from the NIB is using `HIMovieViewCreate` and fails, therefore the view is never actually created.

There are however a couple of very simple workarounds:

1) If you would like to create an `HIMovieView` programatically, simply use `HIObjectCreate` instead.

__Listing 1__  Use `HIObjectCreate` instead of `HIMovieViewCreate`

```
HIObjectRef theHIMovieView;

// create an HIMovieview
HIObjectCreate(kHIMovieViewClassID, NULL, &theHIMovieView);

// set some attributes and a movie for the HIMovieView
HIMovieViewChangeAttributes((HIViewRef)theHIMovieView, kHIMovieViewStandardAttributes, 0);
HIMovieViewSetMovie((HIViewRef)theHIMovieView, aMovie);

...
```

2) If you would like to use Interface Builder, instead of using `HIMovieView` from the Carbon-Enhanced Controls palette use `HIView` and make sure it's Class ID is set to the `kHIMovieViewClassID` identifier `com.apple.quicktime.HIMovieView` as shown in figure 1.

When this is done, using standard HIView calls will work as expected, see listing 2.

__Figure 1__  Using HIView to specify an `HIMovieView` in IB.

!!

__Listing 2__  Getting an `HIMovieView` created as a Custom Control in a NIB file.

```
HIViewID  kMovieViewID = {'moov', 0};
HIViewRef theHIMovieView;

...

// get the window
CreateWindowFromNib(nib, CFSTR("MovieWindow"), &window);

// find our HIMovieView
HIViewFindByID(HIViewGetRoot(window), kMovieViewID, &theHIMovieView);

// install some event handlers
InstallWindowEventHandler(window, &MainWindowEventHandler,
                          GetEventTypeCount(windowEvents), windowEvents, window, NULL);

InstallHIObjectEventHandler((HIObjectRef)theHIMovieView, &HIMovieViewEventSniffer,
                            GetEventTypeCount(viewEvents), viewEvents, window, NULL);

// set some attributes and a movie for the HIMovieView
HIMovieViewChangeAttributes(theHIMovieView, kHIMovieViewAutoIdlingAttribute |
                                            kHIMovieViewControllerVisibleAttribute,
                                            kHIMovieViewEditableAttribute |
                                            kHIMovieViewHandleEditingHIAttribute |
                                            kHIMovieViewAcceptsFocusAttribute);
HIMovieViewSetMovie(theHIMovieView, aMovie);

...

ShowWindow(window);

...
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2008-03-11 | Editorial |
| 2005-05-16 | New document that describes how to work around HIMovieViewCreate failing to initialize the view in QuickTime 7 |

