---
title: The Power of iOS 8
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2014/06/the-power-of-ios8/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:f5edd78cc88de88a'
translated: false
---

> 原文：[The Power of iOS 8](https://oleb.net/blog/2014/06/the-power-of-ios8/)　·　Ole Begemann

# The Power of iOS 8

Here’s why iOS 8 is a big deal. As an example, consider one of my favorite iOS apps, [1Password](https://agilebits.com/onepassword/ios). Assume you want to sign in to a web site in Mobile Safari and your login credentials are stored in 1Password. This is a very common task that I perform several times a week. Think about the steps you have to go through today on iOS 7 to accomplish this:

1. Go back to the home screen and launch 1Password.
2. Enter your 1Password master password.
3. Locate the web site’s credentials in the 1Password database. I have several hundred logins stored in 1Password, so this can require quite a bit of manual browsing or using the built-in search, which is tedious on a mobile device.
4. Copy your password to the pasteboard. And while you’re at it, if the web site requires you to enter a user name (as opposed to your email address), make sure to remember it now or you will have to switch back and forth twice between Safari and 1Password. The pasteboard only accepts one item at a time.
5. Go back to Safari.
6. Manually enter your user name/email address and paste your password.

This sucks.

## Brave New World

Let’s take a look at how this workflow might look on iOS 8 (assuming the developers of 1Password do their homework):

1. With the web site open in Mobile Safari, tap the Share/Action button.
2. From the activity sheet that pops up, tap on the 1Password icon (the 1Password app will include an [Action Extension](https://developer.apple.com/library/prerelease/ios/documentation/General/Conceptual/ExtensibilityPG/Services.html#//apple_ref/doc/uid/TP40014214-CH13-SW1) that can work with web pages/URLs).
3. The UI of the 1Password extension launches inside Safari. Rather than having to enter your master password to access your 1Password data, you will also have the option to authenticate with your fingerprint because [Touch ID now has a public API](https://developer.apple.com/library/prerelease/ios/documentation/LocalAuthentication/Reference/LocalAuthentication_Framework/index.html). Yay, no typing!
4. As an extension that works with web site content, the 1Password extension has [full access to the page’s URL and contents](https://developer.apple.com/library/prerelease/ios/documentation/General/Conceptual/ExtensibilityPG/ExtensionScenarios.html#//apple_ref/doc/uid/TP40014214-CH21-SW12). It can use this information to find the correct login credentials and automatically fill in the user name and password fields for me.^[1](#fn:1) All I will have to do is confirm. Again, no typing!

I can’t wait.

1. Extensions can run their own JavaScript code against the DOM contents of the current web page to identify elements on the page they are interested in. When the user dismisses the extension, it can pass another JavaScript snippet back to the host app (Safari) to alter the original page’s contents. This is the same thing Craig Federighi showed in the WWDC 2014 keynote when he demonstrated an extension that could translate a web page in place (at 1:30:50). [↩︎](#fnref:1)
