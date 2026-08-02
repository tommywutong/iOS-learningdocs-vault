---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DeltaDoc/NewInWO4.061.html
archived_at: '2026-07-15T07:59:02.120465Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[What's New in WebObjects 4.0](Table%20of%20Contents.md)

[!Table of Contents](Table%20of%20Contents.md) [!Previous Section](NewInWO4.060.md)

## Testing With a Web Server

When you're working in direct connect mode, few issues arise with respect to rapid turnaround. If your application has features which require a web server be used even for testing, however, there are a couple of things to know to make rapid turnaround work for you. Specifically, since you are relying on the web server to locate files within WebServerResources, you must follow these guidelines:

- Your projects must reside somewhere below your web server's document root.
- NSProjectSearchPath should point to all projects of interest.
- For application projects, the WOApplicationBaseURL user default should specify the directory containing the application project. For example, if your application's project folder is:

```
c:\web\docroot\WebObjects\MyApp
```


then the WOApplicationBaseURL user default must be "/WebObjects".

- For framework projects, the WOFrameworksBaseURL user default should specify the directory containing all framework projects used by the application. For example, if your application uses MyFramework.framework and that project resides in:

```
c:\web\docroot\WebObjects\Frameworks\MyFramework
```


then the WOFrameworksBaseURL user default must be "/WebObjects/Frameworks".

Conveniently, the two examples above use the default locations for WOApplicationBaseURL and WOFrameworksBaseURL; if your projects reside in these default locations, you need only set NSProjectSearchPath.
Also, while it is possible to point WOApplicationBaseURL and WOFrameworksBaseURL to other locations, it is not suggested that WOFrameworksBaseURL be moved since all WebObjects applications use WOExtensions.framework, which resides in the default location. If you set WOFrameworksBaseURL to point elsewhere, one side effect will be that the images in the "Raised Exception" panel will not render.

[!Table of Contents](Table%20of%20Contents.md) [!Next Section](Debugging.md)
