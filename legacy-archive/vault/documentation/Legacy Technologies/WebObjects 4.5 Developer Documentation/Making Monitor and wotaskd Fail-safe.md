---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DeployingWebObjects/Deploying-48.html
archived_at: '2026-07-15T08:05:04.773102Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Deploying WebObjects Applications

[!](Administrative%20Tasks.md) [!](Increasing%20the%20Listen%20Queue%20Depth.md) [!](Starting%20Monitor%20and%20wotaskd%20on%20Windows%20NT.md)

---

# Making Monitor and wotaskd Fail-safe

Because Monitor is a critical piece of any deployment, measures should be taken to make sure that it does not fail. As part of installation on both Windows NT and Mac OS X Server, __wotaskd__
is configured to start automatically upon boot up. As well, it is started using __woservice__
, which ensures that if __wotaskd__
crashes for any reason it is automatically restarted.

#### [Starting Monitor and wotaskd on Windows NT](Starting%20Monitor%20and%20wotaskd%20on%20Windows%20NT.md#apple-obtwmslefu4dcobz)

#### [Using woservice on Mac OS X Server](Using%20woservice%20on%20Mac%20OS%20X%20Server-2.md#apple-obtwmslefu4tsmjy)

---

© 1999 Apple Computer, Inc. – (Last Updated 25 August 99)

[!](Administrative%20Tasks.md) [!](Increasing%20the%20Listen%20Queue%20Depth.md) [!](Starting%20Monitor%20and%20wotaskd%20on%20Windows%20NT.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
