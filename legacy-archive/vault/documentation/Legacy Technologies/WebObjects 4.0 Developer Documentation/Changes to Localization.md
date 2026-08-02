---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DeltaDoc/NewInWO4.051.html
archived_at: '2026-07-15T07:58:55.951613Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[What's New in WebObjects 4.0](Table%20of%20Contents.md)

[!Table of Contents](Table%20of%20Contents.md) [!Previous Section](NewInWO4.050.md)

# Changes to Localization

In WebObjects 3.5 (and earlier releases), localized versions of a component's HTML templates are located in each component's __.wo__ folder, in subdirectories called language__.lproj__ (__French.lproj__, for example). This mechanism is functional, but isn't supported by developer tools such as Project Builder and WebObjects Builder.
To improve support for developing multi-language web applications, WebObjects 4.0 adopts a localization scheme that's similar to the one for Yellow Box applications. Now components (__.wo__'s) and other resources (such as __.gif__ images) are localizable from Project Builder.
The new scheme changes the locations of localized files as follows:

- Localized files go in language__.lproj__ folders in the Web Components, Resources, and Web Server Resources directories. Any component, application resource, or web server resource can have a version in one or more __.lproj__ folders.
- As with Java and Objective-C source code, script files now go at the top level of the project (or subproject), outside the __.wo__, and they are visible in Project Builder's Classes suitcase. Note that Project Builder still keeps track of the relationship between your script files and their components. For example, if you select __Main.wo/Main.html__ and then select the Classes suitcase, Project Builder automatically displays __Main.wos__.
- Similarly __.api__ files go at the top level of the project (or subproject), outside the __.wo__, as they (like the script and source files) apply to all localized versions of a component. In Project Builder, they are visible in the Resources suitcase.
- All language versions of a localized component (__.wo__) must contain both the __.html__ and __.wod__ files. If a __.woo__ file exists for the component, it must be in included in each version of the component as well.

[!Table of Contents](Table%20of%20Contents.md) [!Next Section](NewInWO4.052.md)
