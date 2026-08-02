---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DeltaDoc/NewInWO4.052.html
archived_at: '2026-07-15T07:58:56.361571Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[What's New in WebObjects 4.0](Table%20of%20Contents.md)

[!Table of Contents](Table%20of%20Contents.md) [!Previous Section](Changes%20to%20Localization.md)

## Project Builder Support

To localize a component in Project Builder:

- Select the component to localize.
- Open the File Attributes Inspector.
- Click Localized, then check the languages to support.
- Click Apply.

Project Builder creates copies of the component in the appropriate Web Components __.lproj__ folders and offers to remove the global (non-localized) version from the disk. You localize other kinds of resources the same way. To view a localized resource, simply select it in its __.lproj__ folder.
Building a localized application or framework creates a __.woa__ or __.framework__ that contains Resources and WebServerResources directories, each containing the __.lproj__ folders for your project. The localized versions of each resource are installed their corresponding __.lproj__ folders following a successful build.

[!Table of Contents](Table%20of%20Contents.md) [!Next Section](NewInWO4.053.md)
