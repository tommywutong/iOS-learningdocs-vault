---
title: App Sandbox Design Guide
apple_id: TP40011183
resource_type: Guide
platform: macOS
topic: Security
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Security/Conceptual/AppSandboxDesignGuide/RevisionHistory.html
archived_at: '2026-07-27T06:57:08.413585Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [App Sandbox Design Guide](About%20App%20Sandbox.md)


[Previous](App%20Sandbox%20Checklist.md)

# Document Revision History

This table describes the changes to _App Sandbox Design Guide_.

| __Date__ | __Notes__ |
| 2016-09-13 | Updated quick start, added a checklist, and provided more detail about migration options. |
| 2014-02-11 | Corrected the explanation of the stopAccessingSecurityScopedResource method. |
| 2013-10-22 | Added information about app group container behavior in OS X v10.9. |
| 2013-08-08 | Removed inaccurate guidance about handling issues where an app needs access to another app's preferences. |
| 2013-03-14 | Added information about related items in OS X v10.8. |
| 2012-09-19 | Clarified information about launching external tools. |
| 2012-07-23 | Added an explanation of app group containers. |
| 2012-05-14 | Improved the explanation of security-scoped bookmarks in [Security-Scoped Bookmarks and Persistent Resource Access](App%20Sandbox%20in%20Depth.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcobtfvbuqmznknltcnq); updated that section for OS X v10.7.4. |
|  | Added a brief section in the Designing for App Sandbox chapter: [Retaining Access to File System Resources](Designing%20for%20App%20Sandbox.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcobtfvbuqnbnknltcmy). |
|  | Improved the discussion in [Opening, Saving, and Tracking Documents](Designing%20for%20App%20Sandbox.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcobtfvbuqnbnknlte), adding information about using file coordinators. |
|  | Corrected the information in [Creating a Login Item for Your App](Designing%20for%20App%20Sandbox.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcobtfvbuqnbnknltg). |
| 2012-03-14 | Improved explanation of security-scoped bookmarks in [Security-Scoped Bookmarks and Persistent Resource Access](App%20Sandbox%20in%20Depth.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcobtfvbuqmznknltcnq). |
|  | Clarified the explanation of the container directory in [The App Sandbox Container Directory](App%20Sandbox%20in%20Depth.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcobtfvbuqmznknltcni) |
| 2012-02-16 | Updated for OS X v10.7.3, including an explanation of how to use security-scoped bookmarks. |
|  | Added a section explaining how to provide persistent access to file-system resources, [Security-Scoped Bookmarks and Persistent Resource Access](App%20Sandbox%20in%20Depth.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcobtfvbuqmznknltcnq). |
|  | Expanded the discussion in [Powerbox and File System Access Outside of Your Container](App%20Sandbox%20in%20Depth.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcobtfvbuqmznknltcny) to better explain how user actions expand your app’s file system access. |
|  | Added a section detailing the changes in behavior of Open and Save dialogs, [Open and Save Dialog Behavior with App Sandbox](App%20Sandbox%20in%20Depth.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcobtfvbuqmznknltq). |
| 2011-09-27 | New document that explains Apple's security technology for damage containment, and how to use it. |
|  | Portions of this document were previously published in _Code Signing and Application Sandboxing Guide_. |

[Previous](App%20Sandbox%20Checklist.md)
