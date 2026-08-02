---
title: Xcode Server API Reference
apple_id: TP40016472
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/documentation/Xcode/Conceptual/XcodeServerAPIReference/Assets.html
archived_at: '2026-07-18T02:24:21.369372Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Server API Reference](index.md)



## Assets

Each integration on your server generates a number of files, known as assets. Assets include log files, Xcode archives and installable products like IPA or PKG files.

### Downloading an Asset

__GET__

`/assets/{path}`

Retrieves an asset given its relative path.

See the section [Retrieving Files for an Integration](Integrations.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dinzsfvbuqmznknltc) for more information.

__Example__

`https://server.mycompany.com:20343/api/assets/bb5b5dfa1c4abff347d28bed7e00b381-Sketch/1/sourceControl.log`

__Parameters__

_path_ (required)

- The relative path of the asset.
- Type: `string`
- Example: `bb5b5dfa1c4abff347d28bed7e00b381-Sketch/1/sourceControl.log`

__Response__: `200`

_Body_

1. `2015-08-03 10:26:53.984 XCSCheckoutIntegrationStep.m:72 [XCSCheckoutIntegrationStep enqueueOperations]`
2. `[SourceControl] Will attempt to update checkout cache for bot`
4. `2015-08-03 10:26:53.984 XCSCheckoutIntegrationStep.m:233 [XCSCheckoutIntegrationStep validateBlueprint]`
5. `[SourceControl, Info] Xcode Source Control Blueprint was valid.`
7. `2015-08-03 10:26:54.050 XCSCheckoutIntegrationStep.m:86 [XCSCheckoutIntegrationStep enqueueOperations]`
8. `[SourceControl] About to update/checkout:`
9. `https://jappleseed@server.mycompany.com.com/jappleseed/sketch.git Branch: master into Sketch/`
11. `2015-08-03 10:26:55.177 XCSCheckoutIntegrationStep.m:318 [XCSCheckoutIntegrationStep checkoutWorkingCopies]`
12. `[SourceControl, Info] Counting objects: 1737, done.`
14. `2015-08-03 10:26:55.277 XCSCheckoutIntegrationStep.m:320 [XCSCheckoutIntegrationStep checkoutWorkingCopies]`
15. `[SourceControl, Info] 90.00% Receiving objects: 806 KB done`
17. `2015-08-03 10:26:55.442 XCSCheckoutIntegrationStep.m:368 [XCSCheckoutIntegrationStep saveVersionedBlueprintToIntegration]`
18. `[SourceControl] Completed checkout of:`
19. `https://jappleseed@server.mycompany.com.com/jappleseed/sketch.git Branch: master (@3982fd5a6dd349c3673c9f91a96baf69eedc44a1) into Sketch/`
21. `2015-08-03 10:26:55.658 XCSCheckoutIntegrationStep.m:450 [XCSCheckoutIntegrationStep saveCommitHistory]`
22. `[SourceControl] This is the first integration, so we'll just load the last 5 commits.`
24. `2015-08-03 10:26:55.695 XCSCheckoutIntegrationStep.m:429 [XCSCheckoutIntegrationStep saveCommitHistory]`
25. `[SourceControl] Got 2 log items:`
26. `Revision: 3982fd5a6dd3`
27. `Author: John Appleseed`
28. `Date: 2015-06-19 18:37:31 +0000`
30. `Remove run scripts (is obsolete and was causing a warning)`
31. `Revision: c1decaa74923`
32. `Author: John Appleseed`
33. `Date: 2015-06-19 18:34:38 +0000`
35. `Merge remote-tracking branch 'origin/master'`
37. `2015-08-03 10:26:55.775 XCSCheckoutIntegrationStep.m:435 [XCSCheckoutIntegrationStep saveCommitHistory]`
38. `[SourceControl] Saving commit history, errors: (null)`

__Response__: `404`

_Body_

1. `{`
2. `"status": 404,`
3. `"message": "Not found"`
4. `}`

[Integrations](Integrations.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dinzsfvbuqmznknlte)

[Code Coverage](CodeCoverage.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dinzsfvbuqnjnknltc)
