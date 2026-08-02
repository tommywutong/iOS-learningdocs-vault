---
title: OldDelegateOnlyComponent
apple_id: DTS10000331
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/OldDelegateOnlyComponent/Introduction/Intro.html
archived_at: '2026-07-18T03:17:31.100505Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](MyComponent.c.md)

# OldDelegateOnlyComponent

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-10-27 Please see DelegateOnlyComponent for the current version of this sample. |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Mac OS 9 |

Please see DelegateOnlyComponent in the current QuickTime sample code archive for an updated version demonstrating concepts outlined in this original sample. This sample component pretends to be a data handler. But, all it does is delegate to the real data handler. This is a useful component sample to start with if you are writing a component to overide the functionality of another component. However, since this component relies on being installed after QuickTime is loaded, if it is used to overide a standard QuickTime component, you may need to combine this component with another installation method to have it install properly. See MyRegisterComponent. Also, see develop article in issue #15 on Manager Component Registration. Requires: QuickTime Keywords: QuickTime

[Next](MyComponent.c.md)

