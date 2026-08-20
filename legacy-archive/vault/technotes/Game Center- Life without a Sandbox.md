---
title: 'Game Center: Life without a Sandbox'
apple_id: DTS40016578
resource_type: Technical Note
platform: iOS|macOS
topic: General
technology: null
published: '2015-10-08'
source_url: https://developer.apple.com/library/archive/technotes/tn2417/_index.html
archived_at: '2026-07-26T19:54:15.040071Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2417

# Game Center: Life without a Sandbox

Game Center no longer provides a development sandbox. This technotes describes some of the consequences of that change and how you can manage those differences.

[Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmnjxhawugsbrfvke4vcbi4yq)[Existing Sandbox Accounts](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmnjxhawugsbrfvke4vcbi4za)[Achievements and Leaderboards](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmnjxhawugsbrfvke4vcbi4zq)[Multiplayer Compatibility](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmnjxhawugsbrfvke4vcbi42a)[Managing Multiplayer Compatibility During Development](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmnjxhawugsbrfvke4vcbi42c2tkbjzauoskoi5pu2vkmkrevatcblfcvex2dj5gvaqkujfbestcjkrmv6rcvkjeu4r27ircvmrkmj5ie2rkokq)[Server Side Authentication](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmnjxhawugsbrfvke4vcbi42q)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmnjxhawvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Introduction

As part of the release of iOS 9 and El Capitan, the Game Center development sandbox has been eliminated, allowing all pre-release development to occur in exactly the same server environment as released games. This change brings several advantages including:

- Simplifying update testing by allowing testers to play with the full player base, not just other testers
- Removing any implementation differences between the sandbox and release environments

__Note:__ While this transition is occurring as part of the release of iOS 9 and El Capitan, it is not specifically tied to those releases. After this transition all iOS and OS X devices will use the release environment not just iOS 9 and El Capitan systems.

For most developers, this change has no effect on the development process, however, there are a few side effects of this change you should be aware of.

[Back to Top](#)

## Existing Sandbox Accounts

No existing sandbox data is being preserved during this transition. As part of this change you will lose all of your data that currently resides in the sandbox environment. This includes:

- Profile data, including nickname and profile image
- Leaderboard scores
- Achievements
- Challenges
- Turn Based Game sessions
- Friends list

If the Apple ID used in the sandbox has not previously been used in the production environment, you will be prompted to create a new profile after the transition has occurred.

[Back to Top](#)

## Achievements and Leaderboards

By design the Achievements and High Scores of a particular Game Center user have always been visible to that user's friends. As part of this change, that will include Achievements and Leaderboard Scores that have not been formally released as part of a particular game version. Similarly, any game a Game Center player has played is visible to all of that players friends, even if that game has not yet been released.

If any of this data needs to be kept secret as part of your overall release strategy, then you will need to create separate accounts for pre-release testing and carefully manage which Game Center users are allowed to become friends with those accounts.

For more information on this issue, see the [WWDC 2015 Session: Going Social with ReplayKit and Game Center](https://developer.apple.com/videos/wwdc/2015/?id=605).

[Back to Top](#)

## Multiplayer Compatibility

For both turn based and realtime multiplayer games, the iTunes Connect multiplayer compatibility matrix only applies to versions approved and released to the App Store. Prerelease versions will connect with all other versions of the app, even if the compatibility matrix would have otherwise precluded it. In the worst case, this can potentially lead to crashes and data corruption in earlier versions of your app. Care should be taken when developing and testing new versions of your multiplayer communication format.

### Managing Multiplayer Compatibility During Development

When making any changes to your multiplayer communication format, particularly when those changes have not been tested yet, you must very careful which players you create Game Center matches with.

The following techniques can be used to manage this issue:

- Create dedicated test accounts and only create matches between those accounts.
- Avoid using auto-match.
- For larger scale testing, the [playerGroup](https://developer.apple.com/library/ios/documentation/GameKit/Reference/GKMatchRequest_Ref/#//apple_ref/occ/instp/GKMatchRequest/playerGroup) property of [GKMatchRequest](https://developer.apple.com/library/ios/documentation/GameKit/Reference/GKMatchRequest_Ref/) can be used to restrict matching. If you use this approach be sure to remove the restriction before submitting your app to the store.
- For larger development projects, consider creating a new test only app in iTunes Connect and use that new app bundle ID to separate all activity from your released apps.
[Back to Top](#)

## Server Side Authentication

After this change [generateIdentityVerificationSignatureWithCompletionHandler](https://developer.apple.com/library/ios/documentation/GameKit/Reference/GKLocalPlayer_Ref/index.html#//apple_ref/occ/instm/GKLocalPlayer/generateIdentityVerificationSignatureWithCompletionHandler:) will continue to work correctly and simply return the publicKeyUrl for the App Store servers instead of the sandbox. However, if your server had cached the [publicKeyUrl](https://developer.apple.com/library/ios/documentation/GameKit/Reference/GKLocalPlayer_Ref/index.html#//apple_ref/occ/instm/GKLocalPlayer/generateIdentityVerificationSignatureWithCompletionHandler:) and expected a particular environment to sign with a particular key, your server will need to be updated to match the new behavior.

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2015-10-08 | Minor editing revision |
| 2015-09-08 | New document that describes issues related to the removal of the Game Center sandbox. |

