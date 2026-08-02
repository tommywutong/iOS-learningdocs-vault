---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/Deployment8.html
archived_at: '2026-07-15T08:05:23.947904Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](Deployment%20and%20Performance%20Issues.md) [!Previous Section](Performance%20Tips.md)

## Cache Component Definitions

As described in the chapter ["WebObjects Viewed Through Its Classes"](WebObjects%20Viewed%20Through%20Its%20Classes.md#apple-he2tmmy), each component has a component definition consisting of the component's template (the result of parsing the __.html__ and __.wod__ files) and information about resources the component uses. If you cache component definitions, the __.html__ and __.wod__ files are parsed only once per application rather than every time they are changed. When caching is disabled, at each new instance of a component the time stamp of the __.html__ and __.wod__ are checked to see if the files have been modified. If they have, they're reloaded.

To cache component definitions, use WOApplication's __setCachingEnabled:__ method:

```
public Application() {
    super();
    this.setCachingEnabled(true);
    ...
}
```


By default, this type of caching is disabled as a convenience for debugging. If component-definition caching is disabled and you're writing an entirely scripted application, you can change code in a scripted component and see the effects of that change without having to relaunch the application. You should always enable component-definition caching when you deploy an application, since performance improves significantly.
Instead of using __setCachingEnabled:__, you can also perform
component-definition caching by setting the WOCachingEnabled user default either on the command line or using the __defaults__ command.

```
HelloWorld -WOCachingEnabled YES
defaults write HelloWorld WOCachingEnabled YES
```


For more information on command-line options, see the online document [_Serving WebObjects_](Deploying%20WebObjects%20Applications.md).

[!Table of Contents](Deployment%20and%20Performance%20Issues.md) [!Next Section](Deployment9.md)
