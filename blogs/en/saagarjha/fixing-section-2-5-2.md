---
title: Fixing Section 2.5.2
source: Saagar Jha
source_key: saagarjha
source_url: 'https://saagarjha.com/blog/2020/11/08/fixing-section-2-5-2/'
original_language: en
published: 2020-11-08
status: active
license: CC BY-SA 4.0 → 可再分发，但译文必须同样 BY-SA 并署名
archived_at: 2026-07-27
content_hash: 'sha256:512b45e5be70196c'
translated: false
---

> 原文：[Fixing Section 2.5.2](https://saagarjha.com/blog/2020/11/08/fixing-section-2-5-2/)　·　Saagar Jha

# Fixing Section 2.5.2

Sunday, November 8, 2020

From its inception, applications that wished to make themselves available on the iOS App Store—the de-facto mechanism of third-party software distribution on the platform—have been required to conform to a set of guidelines laid out and enforced by Apple’s [App Review](https://developer.apple.com/app-store/review/) process. Apple’s [list of guidelines](https://developer.apple.com/app-store/review/guidelines/) have expanded and been amended through the years, but the focus has largely remained the same: preventing the distribution of applications that are fraudulent, malicious, contain questionable or illegal content, or undermine Apple’s business interests. Much has already been said about the review process as a whole or Apple’s choice of guidelines, but we are going to focus on one guideline that may be one of the most important of them all: the rule that dictates restrictions on downloading additional code at runtime. For the last couple years, this rule has lived in [section 2.5.2](https://developer.apple.com/app-store/review/guidelines#2.5.2) of the guidelines, and this is the name that we will be using to refer to it.

## The history and evolution of section 2.5.2

The current text of section 2.5.2 in the App Store Review Guidelines is fairly short—it’s three sentences that are just under a hundred words in total, making it concise enough to reproduce here in its entirety:

> Apps should be self-contained in their bundles, and may not read or write data outside the designated container area, nor may they download, install, or execute code which introduces or changes features or functionality of the app, including other apps. Educational apps designed to teach, develop, or allow students to test executable code may, in limited circumstances, download code provided that such code is not used for other purposes. Such apps must make the source code provided by the Application completely viewable and editable by the user.

This particular formulation is relatively new, however: its spiritual ancestor, then going by the classification “section 2.7”, was even shorter:

> Apps that download code in any way or form will be rejected

The existence of some kind of rule similar to this is fundamental to the premise of App Review—so much so that without it the entire process falls apart. Since the review process is largely done only once, it relies on an app’s behavior not changing after review has been performed on a build. iOS has effective technological protections against applications downloading additional native code at runtime, but the original “section 2.7” formulation of this rule covers the remaining cases arising from non-native (interpreted) code.

The modern 2.5.2 incarnation of this rule has additional verbiage which we will get to in a moment, but still retains the core idea of the guideline: applications that download additional code to alter their functionality as a way to bypass app review are not allowed. This has always been and must always be the intent of this guideline if the format of the App Review process is to remain unchanged. In recent years there have been a handful of modifications to the section, but even as the language of this rule has evolved its enforcement has remained consistent; developers may not create applications that remotely download code, period.

## Scripting applications

To fully understand section 2.5.2, we must first understand the environment in which the additions were written in. For this we need to talk about the rise of a new type of app, one which we will call “scripting applications”.

Scripting applications consist of two parts: a frontend that accepts code from the user, and a backend that runs it. As generating native code is generally disallowed for third-party apps distributed on the App Store, the backend is usually some sort of Turing-complete interpreter. Under the original “section 2.7” guideline, such apps would not be allowed on the store, as they would allow the addition of new code and thus violate the guidelines. However, it is important to note that these apps do not actually have the issue that the guideline was meant to solve: the app itself—neither the frontend nor the backend—changes, and scripts are user- and not developer-generated.

In recent years a number of factors have caused the guidelines to evolve into the 2.5.2 rules we have today—likely a combination of pent-up demand for being able to write scripts on iOS, Apple releasing their own scripting apps to the App Store, and the creation of a number of high-quality apps that ostensibly did not meet the guidelines but were “harmless” started getting accepted. App Review itself seemed to have started shifting to start allowing “educational” apps to execute code, where the user could fully edit and modify what was being run, with parts of this ending up into section 2.5.2 itself. Today there are many scripting apps on the App Store that will let you write scripts in programming languages such as Python, Lua, or JavaScript, some that let you run WebAssembly or LLVM IR bundles, and still others that provide custom “automations”. Apple themselves ships two scripting apps: Swift Playgrounds and Shortcuts. Our own application, iSH, is a scripting application: it interprets x86 scripts. Scripting applications are quite popular among developers, students, teachers, and power users: for many they quite literally make iOS an operating system they are willing to use.

## Problems with section 2.5.2

With such a vibrant ecosystem of scripting applications, it seems like 2.5.2 is a massive success for the App Store: it allows so many of these apps to exist, all without circumventing the App Review process. In reality, however, it does not protect these applications from being found noncompliant with the guidelines. It shares the same goal that section 2.7 has, but even with its additions it suffers from the same problem in that it does not distinguish between user and developer code, nor does it contain a rigorous definition of scripting applications. In cases where App Review does not understand the intent behind 2.5.2, this leads to erroneous rejections, such as the one that iSH received.

Most applications that allow users to create content inherently indemnify the application author against the app being used to violate the guidelines; section 2.5.2 does not do this. Apps that include explicit content are forbidden on the App Store, for example, but drawing apps are not rejected because they allow the user to create such content. However, developers of scripting apps live in constant fear of App Review finding a way to create scripts that do things that the review team feels is objectionable and rejecting their app.

This situation is made worse when the “violation” is a misinterpretation of section 2.5.2 by the review team, especially because they are not equipped to handle such cases and create nonsensical rejections. For example, iSH was once rejected with the rationale that “During review, your app installed or launched executable code, which is not permitted on the App Store.” The template itself clearly outlines the case it is meant to apply—an app that is installing code by itself, to bypass review—but in the case of iSH the reviewer chose to install code and then complained that the app did what they told it to do. In a second case we removed the package manager from iSH, but the reviewer used the wget tool to redownload it and then rejected the app because they “found that [our] app is not self-contained and has remote package updating functionality”—functionality that the reviewer added themselves and then decided to enforce the rules on. Rejecting a drawing application for what the user can draw in it is absurd, but this is exactly how section 2.5.2 is used to reject legitimate scripting applications.

These issues are not unique to iSH, they apply to every single scripting application. Not only is it impossible for an application developer to prevent their users from doing things that the App Review team doesn’t like, any additional restrictions that review asks a developer to put into place transfer to all scripting applications, including Apple’s. The App Review team seems to have been told that the ability to run code at all is some sort of “security issue”, but again, this is how every scripting application works—trying to enforce the guidelines in this way would require all of them to not be allowed on the store.

## Fixing section 2.5.2

With such severe issues with section 2.5.2, it may be difficult to see how to fix it to allow scripting apps to exist, while also preventing App Review from falling apart because we allow apps to update themselves without going through review. However, we’ve already touched on the solution: the difference between the two situations is user involvement. Trying to place restrictions on what a user can write themselves, or download, is not possible in a scripting app. But we can distinguish a scripting application from a normal app that is trying to update its app logic by downloading code quite easily: a scripting application keeps a clear boundary between its native runtime and the scripts that run on top of it, and it also allows users to freely edit scripts. Thus, we suggest the following replacement for section 2.5.2:

Not only does this ensure that applications cannot use downloaded code to update themselves, it provides a clear definition of a scripting application and tightens up some language around the platform sandbox.
