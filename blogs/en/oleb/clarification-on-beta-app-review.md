---
title: Clarification on Beta App Review
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2014/06/testflight-beta-builds-app-review/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:cbc3c05179a8ff62'
translated: false
---

> 原文：[Clarification on Beta App Review](https://oleb.net/blog/2014/06/testflight-beta-builds-app-review/)　·　Ole Begemann

# Clarification on Beta App Review

> “Beta App Review” – seriously? [https://developer.apple.com/support/appstore/TestFlight/index.php](https://developer.apple.com/support/appstore/TestFlight/index.php)
> 
> — [@olebegemann](https://twitter.com/olebegemann) Ole Begemann [June 3, 2014](https://twitter.com/olebegemann/status/473773540848992256)

Following the [TestFlight acquisition](http://techcrunch.com/2014/02/21/rumor-testflight-owner-burstly-is-being-acquired-by-apple/) a few months ago, Apple announced at WWDC yesterday that they will allow [beta app distribution through the App Store](http://techcrunch.com/2014/06/02/ios-testflight/) in the future.

Overall, the program looks great, with developers being allowed to invite up to 1,000 beta testers per app and testing privileges being bound to users’ Apple IDs instead of specific iOS devices. I do not like the fact that Apple apparently plans to also do [app reviews for beta versions](https://developer.apple.com/support/appstore/TestFlight/index.php), though:

> To get going, upload builds from Xcode as you do today. Next, set up your list of testers in iTunes Connect. Once you have a build you’re ready to send to testers, just submit your app for Beta App Review and testing will begin once your app is approved.

While it is true that people may otherwise abuse the beta program to distribute apps to small audiences outside the rules of the App Store, I don’t see how review times of several days (or potentially even longer) would be feasible for an efficient beta release process.

# Clarification

Fortunately, Apple seems to have something else in mind. This is what the updated [iOS Developer Program License Agreement](https://developer.apple.com/programs/terms/ios/standard/ios_program_standard_agreement_20140602.pdf) has to say about the TestFlight program:

> **6.2 Submission to Apple for the TestFlight Program**
> 
> If You would like to distribute Your Application to Beta Testers through the TestFlight Program, You must first submit Your Application to Apple for review. By submitting such Application, You represent and warrant that Your Application complies with the Documentation and Program Requirements then in effect as well as with any additional guidelines that Apple may post on the Program web portal or in iTunes Connect. **Thereafter, Apple may permit You to distribute updates to such Application directly to Your Beta Testers without Apple’s review, unless such an update includes significant changes, in which case You agree to inform Apple in iTunes Connect and have such Application re-reviewed.** Apple reserves the right to require You to cease distribution of Your Application through the TestFlight Program, and/or to any particular Beta Tester, at any time in its sole discretion.

Emphasis mine. So it seems that your beta app has to go through review at least once, but thereafter Apple may allow you to skip the review unless you make significant changes (whatever that means). It is not a guarantee that the process will always work like this, but at least Apple has thought about the problem and hopefully has a working solution in mind.
