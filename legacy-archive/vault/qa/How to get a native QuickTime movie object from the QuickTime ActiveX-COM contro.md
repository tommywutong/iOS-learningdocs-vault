---
title: How to get a native QuickTime movie object from the QuickTime ActiveX/COM control
apple_id: DTS40007498
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2008-03-27'
source_url: https://developer.apple.com/library/archive/qa/qa1594/_index.html
archived_at: '2026-07-18T02:32:21.952489Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1594

# How to get a native QuickTime movie object from the QuickTime ActiveX/COM control

## Q:  I'm working with the QuickTime ActiveX/COM control in my C++ application, and I'd also like to be able to call QuickTime Movie Toolbox functions using the C/C++ API . Can I get a native QuickTime movie object from the QuickTime ActiveX/COM control?

A: Yes. The QuickTime COM interface `IQTControl` and `IQTMovie` expose the methods `get_Movie` and `get_MovieHandle`, which you can use to get the native QuickTime movie (the traditional QTML handle). Once you have the native QuickTime movie, you can use it to call the QuickTime C/C++ APIs.

Here's a sample function:

__Listing 1__  How to get the native QuickTime movie from the QuickTime ActiveX/COM.

```swift
// Get the native QuickTime movie

void MyMovieClass::GetNativeQTMovie(long* outMovie)
{
    CComPtr<IQTControl> spQTControl;

    *outMovie=NULL;

    // Get interface pointer to control
    if (SUCCEEDED( m_ax.QueryControl(&spQTControl) ))
    {
        CComPtr<IQTMovie> spQTMovie;

        // Get interface pointer to movie
        spQTControl->get_Movie(&spQTMovie);
        if (spQTMovie)
        {
            // get the native QuickTime movie
            spQTMovie->get_MovieHandle((long*) outMovie);
        }
    }

    return;
}
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2008-03-27 | New document that describes how to get a native QuickTime movie object from the QuickTime ActiveX/COM control |

