---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/WOClasses12.html
archived_at: '2026-07-15T08:06:10.646837Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](WebObjects%20Viewed%20Through%20Its%20Classes.md) [!Previous Section](WOClasses11.md)

### Creating or Restoring the Request Page

After the session receives the __awake__ message, the next step is to find the _request page_. Each request received by a WebObjects application is associated with one of the application's pages-the request page. The request page is usually the response page from the last request. (The response page shows the result, or output, of the request; note, however, that backtracking may alter this.)
If the user has just begun a new session (that is, if the request URL looks like the one shown in [Figure 20](WOClasses9.md#apple-g43dcnq)), the user has not requested a specific page. Therefore, the application object creates a new instance of the WOComponent class for the page named "Main." The application object performs the following steps to create a component:

- It looks in the runtime system for a WOComponent subclass that has the same name as the request page (in this case, "Main"). If it finds such a class with the same name, it creates an instance of that class.
- If the application object fails to find a class in the run-time system, it looks for a scripted component with the name of the request page-first looking in the application, and then searching any linked frameworks. When it finds the __.wo__ directory, it creates a component object using a unique WOComponent subclass for the scripted component and makes the scripted code the class implementation.
- It invokes the WOComponent subclass's __init__ method or constructor.
- It invokes the WOComponent subclass's __awake__ method to prepare it for the request.

If the request is made from an established session, the application object attempts to retrieve the request page from its cache. By default, an application caches component (or page) instances once they're created, primarily to facilitate backtracking: when users backtrack, they're revisiting pages restored by the application. The request URL contains the information needed to retrieve the page from the cache (see [Figure 23](WOClasses11.md#apple-g43teoa)). This information includes the page name and a context ID.

The component may not be in the cache for one of three reasons:

- The page-caching feature is turned off.
- The request is the first for that page during the session.
- The user has backtracked beyond the page cache limit.

If the component is not in the cache, the application object creates the component using the procedure described above. If the component is in the cache, it sends the component the __awake__ message.
Note that to retrieve the page from the cache, a context ID is required. The context ID identifies a page _as it existed at the end of a particular request-response loop_. Why is the context ID necessary? Imagine you're accessing a WebObjects application that lets you subscribe to various publications.
You navigate from the site's home page to the order page, where you select a publication, and then you go to the customer information page and fill in your address. After submitting this information, you navigate back to the home page. Next, you decide to enter a subscription for a friend. You follow the process a second time, selecting a different publication and entering your friend's address.
At this point, within a single session with the subscriptions application, you've accessed the same pages twice, entering different information each time. Let's say that you now realize that you made a mistake in your own address, so you backtrack to that page, change the address, and resubmit the information. It's important that the new address information is submitted to the customer information page as it existed during the first order so that the revised information can be associated with the right publication order.
WebObjects associates a different context ID (again, a randomly generated integer-to maintain security) with each request-response loop cycle. A request to a session includes both the name of request page and a context ID so the session object can locate, from its cache of page instances, the appropriate one to handle the request.

[!Table of Contents](WebObjects%20Viewed%20Through%20Its%20Classes.md) [!Next Section](WOClasses13.md)
